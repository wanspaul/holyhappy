from calendar import timegm
from datetime import datetime

import jwt
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from newsongy.models import Person


def obtain_token(person: Person):
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = {
        'person': person.name,
        'dept': person.dept,
        'group': person.group,
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
    }

    # Include original issued at time for a brand new token,
    # to allow token refresh
    if api_settings.JWT_ALLOW_REFRESH:
        payload['orig_iat'] = timegm(
            datetime.utcnow().utctimetuple()
        )

    return jwt_encode_handler(payload)


def obtain_user(token: str):
    """
    payload = {'name': '홍길동', 'exp': 1462187582}
    :param token:
    :return:
    """
    jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

    if not token or len(token) == 0:  # case1: 토큰을 분실 했을 경우
        raise serializers.ValidationError('Invalid token header. Non credentials provided.')

    try:
        payload = jwt_decode_handler(token)
    except jwt.ExpiredSignature:  # case2: 토큰이 만료되었을 경우
        raise serializers.ValidationError('Signature has expired.')
    except jwt.DecodeError:  # case3: 디코드 실패
        raise serializers.ValidationError('Error decoding signature.')

    # name = jwt_get_username_from_payload(payload)
    name = payload.get('person')
    dept = payload.get('dept')
    group = payload.get('group')
    if not name or not dept or not group:  # case4: payload 가 잘못되어 name을 가져올 수 없는 경우
        raise serializers.ValidationError('Invalid payload.')

    try:
        person = Person.objects.get(name=name, dept=dept, group=group)
    except Person.DoesNotExist:  # case5: 해당 유저가 존재하지 않는 경우
        raise serializers.ValidationError("Person doesn't exists.")

    return person

