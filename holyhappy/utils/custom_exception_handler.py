from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # 발생한 exception을 가져온다.
    response = exception_handler(exc, context)
    if response is not None:
        # 예외가 발생할 경우엔 token쿠키를 지워준다
        response.delete_cookie('holyhappy_token', domain=settings.COOKIE_DOMAIN)

        return HttpResponseRedirect(reverse('login'))
    else:
        return None
