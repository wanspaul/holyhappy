from django.core.urlresolvers import reverse
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.generic import View
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from bible.models import Bible
from holyhappy.utils.api_result import APIResult, APIStatusCode, APIStatusMessage, APIResultSerializer
from holyhappy.utils.connector import RedisConnector
from holyhappy.utils.jwt_util import obtain_token
from newsongy.models import Person
from pray.models import Pray, Attendance
import logging

logger = logging.getLogger(__name__)


class RootView(APIView):
    def get(self, request):
        """
        루트 경로로 접근시 메인 화면으로 리다이렉트 한다. 
        :param request:
        :return:
        """
        return HttpResponseRedirect(reverse('home'))


class HomeView(APIView):
    def get(self, request):
        return TemplateResponse(request, 'content/main.html')


class LoginView(View):
    def get(self, request):
        return TemplateResponse(request, 'account/login.html')

    def post(self, request):
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        group = request.POST.get('group')
        password = request.POST.get('password')

        print(name)
        print(dept)
        print(group)
        print(password)

        try:
            person = Person.objects.get(name=name, dept=dept, group=group)
            # aes = SimpleEncryptor(password)
            # enc_password = aes.encrypt(password)

            if person.password != password:
                raise ValueError('비밀번호가 일치하지 않습니다.')

            token = obtain_token(person)
            print('token : {}', token)

            response = HttpResponseRedirect(reverse('home'))

            response.set_cookie(key='holyhappy_token', value=token, domain=settings.COOKIE_DOMAIN)

            return response

        except Person.DoesNotExist:
            context = {
                'error': '존재하지 않는 계정입니다.'
            }
        except ValueError as e:
            logger.info(e)
            context = {
                'error': e
            }
        except Exception as e:
            logger.info(e)
            context = {
                'error': '알수 없는 에러가 발생했습니다.'
            }

        return TemplateResponse(request, 'account/login.html', context)


class PrayView(APIView):
    def get(self, request):

        person = request.user

        pray_list = Pray.objects.all()

        for pray in pray_list:
            setattr(pray, 'M', False)
            setattr(pray, 'N', False)

            attendance = Attendance.objects.filter(person_id=person.id, pray_id=pray.id).first()

            if attendance and attendance.joined_morning == 1:
                setattr(pray, 'M', True)
            if attendance and attendance.joined_afternoon == 1:
                setattr(pray, 'N', True)

        context = {
            'pray_list': pray_list
        }

        return TemplateResponse(request, 'pray/attendance.html', context)


class AttendanceEditView(APIView):

    def post(self, request):

        person = request.user

        pray_id = int(request.POST.get('pray_id'))
        pray_time = request.POST.get('pray_time')
        joined = request.POST.get('joined')

        try:
            attendance = Attendance.objects.get(person=person.id, pray_id=pray_id)
        except Attendance.DoesNotExist:
            attendance = None

        if attendance is None:
            attendance = Attendance()
            attendance.person_id = person.id
            attendance.pray_id = pray_id

        if pray_time == 'M':
            if joined == 'true':
                attendance.joined_morning = True
            else:
                attendance.joined_morning = False

        if pray_time == 'N':
            if joined == 'true':
                attendance.joined_afternoon = True
            else:
                attendance.joined_afternoon = False

        attendance.save()

        api_result = APIResult()

        if False:
            api_result.status = APIStatusCode.ERROR
            api_result.message = APIStatusMessage.ERROR

        return Response(APIResultSerializer(api_result).data)


class BibleObjectiveView(APIView):
    def get(self, request):

        conn = RedisConnector()
        client = conn.get_redis_cache()

        key = request.user.id
        value = client.get(key)
        if value:
            return HttpResponseRedirect(reverse('read_bible'))

        return TemplateResponse(request, 'bible/objective.html')


class SetObjectiveView(APIView):

    def get(self, request, page):
        objective_1 = ('요일 1', '요일 2', '요일 3', '요일 4', '요일 5')
        objective_3 = ('엡1-엡3', '엡4-엡6', '빌1-빌3', '빌4-골1', '골2-몬1')
        objective_5 = ('히1-히5', '히6-히10', '히11-약2', '약3-벧전2', '벧전3-벧후3')
        objective_10 = ('롬1-롬10', '롬11-고전4', '고전5-고전14', '고전15-고후8', '고후9-갈6')
        day_list = ('16(화)', '17(수)', '18(목)', '19(금)', '20(토)')

        conn = RedisConnector()
        client = conn.get_redis_cache()

        key = request.user.id

        client.set(key, page)

        if page == '1':
            objective_list = list(objective_1)
        elif page == '3':
            objective_list = list(objective_3)
        elif page == '5':
            objective_list = list(objective_5)
        elif page == '10':
            objective_list = list(objective_10)
        else:
            return HttpResponseRedirect(reverse('bible_objective'))

        Bible.objects.filter(person_id=request.user.id).delete()

        bible_list = []
        i = 0

        for objective in objective_list:
            bible_list.append(
                Bible(
                    person=request.user,
                    title=objective,
                    day=day_list[i],
                    memo=''
                )
            )

            i += 1


        print(bible_list)
        Bible.objects.bulk_create(bible_list)

        if Bible.objects.filter(person_id=request.user.id).count() != 5:
            client.delete(key)
            return HttpResponseRedirect(reverse('set_objective'))
        return HttpResponseRedirect(reverse('read_bible'))


class ReadBibleView(APIView):
    def get(self, request):

        placeholder_list = ('말씀읽기 시-작!', '어제 못읽어도 괜찮아요. 지금부터라도!', '이제껏 못읽었다고 포기하지 마세요!',
                            '얼마 남지 않았어요. 조금만 더 힘을 내세요.', '마지막 기회! 끝까지 포기하지 마세요.')

        read_bible_list = Bible.objects.filter(person_id=request.user.id)

        i = 0
        for read_bible in read_bible_list:
            setattr(read_bible, 'placeholder', placeholder_list[i])
            i += 1

        context = {
            'read_bible_list': read_bible_list
        }
        return TemplateResponse(request, 'bible/read_bible.html', context)


class ReadBibleEditView(APIView):
    def post(self, request):

        person = request.user

        bible_id = int(request.POST.get('bible_id'))
        read = request.POST.get('read')

        try:
            bible = Bible.objects.get(person_id=person.id, id=bible_id)
        except Bible.DoesNotExist:
            bible = None

        if bible is None:
            raise

        if read == 'true':
            bible.read = True
        else:
            bible.read = False

        bible.save()

        api_result = APIResult()

        if False:
            api_result.status = APIStatusCode.ERROR
            api_result.message = APIStatusMessage.ERROR

        return Response(APIResultSerializer(api_result).data)


class MemoEditView(APIView):
    def post(self, request):
        bible_id = int(request.POST.get('bible_id'))
        memo = request.POST.get('memo')
        Bible.objects.filter(pk=bible_id).update(memo=memo)

        api_result = APIResult()

        if False:
            api_result.status = APIStatusCode.ERROR
            api_result.message = APIStatusMessage.ERROR

        return Response(APIResultSerializer(api_result).data)


class GoalView(APIView):
    def get(self, request):

        attendance_score = Attendance.objects.aggregate(
            sum_morning=Sum('joined_morning'),
            sum_afternoon=Sum('joined_afternoon')
        )

        bible_score = Bible.objects.aggregate(
            sum_read=Sum('read')
        )

        pray_score = attendance_score['sum_morning'] + attendance_score['sum_afternoon']


        context = {
            'pray_score': pray_score,
            'bible_score': bible_score['sum_read']
        }
        return TemplateResponse(request, 'content/goal.html', context)
