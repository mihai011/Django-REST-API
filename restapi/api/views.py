from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status

from django.core.exceptions import ValidationError

from .models import PowerRequest, FibonaciRequest, FactorialRequest
from .serializers import PowerSerializer, FibonaciSerializer, FactorialSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .utils import findIndex
import math
# Create your views here.


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def power_view(request, base=None, exponent=None):

    try:
        p, created = PowerRequest.objects.get_or_create(base=base, exponent=exponent)
        if created:
            p.full_clean()
        else:
            serializer = PowerSerializer(p)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
    except ValidationError as e:
        return Response(status=status.HTTP_400_BAD_REQUEST, exception=True)

    if request.method == "GET":
        p.response = p.base**p.exponent
        p.save()
        serializer = PowerSerializer(p)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def fibonaci_view(request, index=None):

    try:
        f, created = FibonaciRequest.objects.get_or_create(index=index)
        if created:
            f.full_clean()
        else:
            serializer = FibonaciSerializer(f)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
    except ValidationError as e:
        return Response(status=status.HTTP_400_BAD_REQUEST, exception=True)

    if request.method == "GET":
        f.response = findIndex(f.index)
        f.save()
        serializer = FibonaciSerializer(f)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def factorial_view(request, index=None):
    try:
        f, created = FactorialRequest.objects.get_or_create(index=index)
        if created:
            f.full_clean()
        else:
            serializer = FactorialSerializer(f)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
    except ValidationError as e:
        return Response(status=status.HTTP_400_BAD_REQUEST, exception=True)

    if request.method == "GET":
        f.response = math.factorial(f.index)
        f.save()
        serializer = FactorialSerializer(f)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
