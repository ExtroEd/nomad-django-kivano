from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.utils import swagger_auto_schema


class TokenObtainPairViewCustom(TokenObtainPairView):
    pass


class TokenRefreshViewCustom(TokenRefreshView):
    pass


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        security=[{'Bearer': []}]
    )
    def get(self, request):
        return Response({"message": "This is a protected resource"})
