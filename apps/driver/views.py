from django.utils import timezone
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.driver.models import Driver
from apps.driver.permissions import DriversPermission
from apps.driver.serializers import DriverRegisterSerializer, DriverSerializer
from apps.trip.models import Trip
from apps.trip.serializers import TripSerializer


class DriverCreate(CreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverRegisterSerializer
    permission_classes = (AllowAny,)


class DriversListView(ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = (AllowAny,)


class StartTripView(APIView):
    permission_classes = [IsAuthenticated, DriversPermission]

    def post(self, request):
        driver = Driver.objects.get(user=self.request.user)
        now = timezone.now()
        trips = Trip.objects.filter(driver=driver, status="REQUESTED")
        if not trips:
            return Response({'message': 'no requested trip yet'})
        else:
            trip = Trip.objects.get(driver=driver, status="REQUESTED")
            passenger = trip.passenger
            trip.status = 'IN_PROGRESS'
            trip.start_time = now
            driver.status = 'busy'
            passenger.status = 'busy'
            trip.save()
            driver.save()
            passenger.save()
            return Response({'message': 'trip started'}, status=status.HTTP_200_OK)


class EndTripView(APIView):
    permission_classes = [IsAuthenticated, DriversPermission]

    # def get(self, request):
    #     driver = Driver.objects.get(user=self.request.user)
    #     trips = Trip.objects.filter(driver=driver, status="IN_PROGRESS")
    #     if not trips:
    #         return Response({'message': 'no started trip yet'})
    #     else:
    #         return Response({'message': 'do you want to end trip?'})

    def post(self, request):
        driver = Driver.objects.get(user=self.request.user)
        now = timezone.now()
        trips = Trip.objects.filter(driver=driver, status="IN_PROGRESS")
        if not trips:
            return Response({'message': 'no started trip yet'})
        else:
            trip = Trip.objects.get(driver=driver, status="IN_PROGRESS")
            passenger = trip.passenger
            trip.status = 'COMPLETED'
            trip.end_time = now
            driver.status = 'waiting'
            passenger.status = 'free'
            trip.save()
            driver.save()
            passenger.save()
            return Response({'message': 'trip ended'}, status=status.HTTP_200_OK)


class DriverTripsList(ListAPIView):
    permission_classes = [IsAuthenticated,DriversPermission]
    serializer_class = TripSerializer

    def get_queryset(self):
        driver = Driver.objects.get(user=self.request.user)
        trips = Trip.objects.filter(driver=driver)
        return trips
