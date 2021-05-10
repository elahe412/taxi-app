from rest_framework import mixins, generics
from rest_framework.permissions import IsAuthenticated

from apps.trip.models import Trip
from apps.trip.serializers import TripSerializer


class TripsList(mixins.ListModelMixin,
                generics.GenericAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# class RequestTripView(APIView):
#     def post(self, request):
#         driver = Driver.random.get_random_driver()
#         price = specify_price()
#         passenger = Passenger.objects.get(user=self.request.user)
#         ts = TripRequestSerializer(data=request.data)
#         if ts.is_valid():
#             ts.save(passenger=passenger, status='REQUESTED', price=price,
#                     driver=driver)
#             driver.status = 'toward_the_passenger'
#             passenger.status = 'waiting_for_driver'
#             passenger.save()
#             driver.save()
#             return JsonResponse(ts.data, status=status.HTTP_201_CREATED)
#
#
# class StartTripView(APIView):
#     def post(self, request):
#         driver = Driver.objects.get(user=self.request.user)
#         now = timezone.now()
#         trip = Trip.objects.get(driver=driver, status="REQUESTED")
#         passenger = trip.passenger
#         trip.save(status='IN_PROGRESS', start_time=now)
#         driver.save(status='busy')
#         passenger.save(status='busy')
#         return Response({'message': 'trip started'}, status=status.HTTP_200_OK)
#
#
# class EndTripView(APIView):
#     def post(self, request):
#         driver = Driver.objects.get(user=self.request.user)
#         now = timezone.now()
#         trip = Trip.objects.get(driver=driver, status="IN_PROGRESS")
#         passenger = trip.passenger
#         trip.save(status='COMPLETED', end_time=now)
#         driver.save(status='waiting')
#         passenger.save(status='free')
#         return Response({'message': 'trip ended'}, status=status.HTTP_200_OK)
