from rest_framework import authentication

from holyhappy.utils.jwt_util import obtain_user


class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        """
        쿠키에 저장되어 있는 token 값으로 유저를 가져옵니다. 가져오는 상황에서 예외가 발생할 수 있으며 정상적으로 가져온 경우에는 인증된 유저라고 판단합니다.
        :param request:
        :return:
        """
        token = request.COOKIES.get('holyhappy_token', None)
        user = obtain_user(token)
        return (user, None)

