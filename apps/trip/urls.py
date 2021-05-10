from django.urls import path

from apps.trip.views import TripsList

urlpatterns = [

    path('trips/', TripsList.as_view(), name='trips_list'),
    # path('request_trip/', RequestTripView.as_view(), name='request_trip'),
    # path('start_trip/', StartTripView.as_view(), name='start_trip'),
    # path('end_trip/', EndTripView.as_view(), name='end_trip'),

]
