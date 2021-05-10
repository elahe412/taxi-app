from django.urls import path

from apps.passenger.views import PassengerCreate, PassengerListView, RequestTripView, PassengerTripsList

urlpatterns = [
    path('signup/', PassengerCreate.as_view(), name='signup_passenger'),
    path('passengers_list/', PassengerListView.as_view(), name='passengers_list'),
    path('request_trip/', RequestTripView.as_view(), name='request_trip'),
    path('trips_list/', PassengerTripsList.as_view(), name='trips_list'),


]
