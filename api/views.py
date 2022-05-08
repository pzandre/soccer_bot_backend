import json

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.utils import RedisContextManager


class MatchesBaseAPIView(APIView):
    permission_classes = [
        AllowAny,
    ]
    renderer_classes = [JSONRenderer]
    def get(self, request, *args, **kwargs):
        with RedisContextManager() as redis_connection:
            data = {"matches": [json.loads(match) for match in redis_connection.lrange("cached_matches", 0, -1)]}
        return Response(status=status.HTTP_200_OK, data=data)

