from django.db.models import Q
from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from apps.common import specify_price
from apps.driver.models import Driver
from apps.passenger.models import Passenger
from apps.passenger.permissions import PassengersPermission
from apps.passenger.serializers import PassengerRegisterSerializer, PassengerSerializer
from apps.trip.models import Trip
from apps.trip.serializers import TripRequestSerializer, TripSerializer


class PassengerCreate(CreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerRegisterSerializer
    permission_classes = (AllowAny,)


class PassengerListView(ListAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = (AllowAny,)


class RequestTripView(APIView):
    permission_classes = [IsAuthenticated,PassengersPermission]

    def post(self, request):
        passenger = Passenger.objects.get(user=self.request.user)
        passenger_trips = Trip.objects.filter(Q(status='IN_PROGRESS') | Q(status='REQUESTED'), passenger=passenger)
        if not passenger_trips:
            if not Driver.random.get_random_driver():
                return JsonResponse({'message': 'sorry no drivers found try again later.'})
            else:
                driver = Driver.random.get_random_driver()
                price = specify_price()
                ts = TripRequestSerializer(data=request.data)
                if ts.is_valid():
                    ts.save(passenger=passenger, status='REQUESTED', price=price,
                            driver=driver)
                    driver.status = 'toward_the_passenger'
                    passenger.status = 'waiting_for_driver'
                    passenger.save()
                    driver.save()
                    return JsonResponse({'message': 'trip requested'}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'message': 'you cant have multiple trips at the same time '})


class PassengerTripsList(ListAPIView):
    permission_classes = [IsAuthenticated,PassengersPermission]
    serializer_class = TripSerializer

    def get_queryset(self):
        passenger = Passenger.objects.get(user=self.request.user)
        trips = Trip.objects.filter(passenger=passenger)
        return trips
