from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status

from django.core.exceptions import ValidationError

from .models import PowerRequest, FibonaciRequest, FactorialRequest
from .serializers import PowerSerializer, FibonaciSerializer, FactorialSerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


from .utils import findIndex
import math
# Create your views here.


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def power_view(request, base=None, exponent=None):

    try:
        p = PowerRequest(base=base, exponent=exponent)
        p.full_clean()
    except ValidationError as e:
        return Response(status=status.HTTP_400_BAD_REQUEST, exception=True)

    if request.method == "GET":
        p.response = p.base**p.exponent
        p.save()
        serializer = PowerSerializer(p)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET"])
def fibonaci_view(request, index=None):

    try:
        f = FibonaciRequest(index=index)
        f.full_clean()
    except ValidationError as e:
        return Response(status=status.HTTP_400_BAD_REQUEST, exception=True)

    if request.method == "GET":
        f.response = findIndex(f.index)
        f.save()
        serializer = FibonaciSerializer(f)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET"])
def factorial_view(request, index=None):
    try:
        f = FactorialRequest(index=index)
        f.full_clean()
    except ValidationError as e:
        return Response(status=status.HTTP_400_BAD_REQUEST, exception=True)

    if request.method == "GET":
        f.response = math.factorial(f.index)
        f.save()
        serializer = FactorialSerializer(f)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
