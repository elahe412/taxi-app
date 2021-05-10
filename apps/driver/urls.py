from django.urls import path

from apps.driver.views import DriverCreate, DriversListView, StartTripView, EndTripView, DriverTripsList

urlpatterns = [
    path('signup/', DriverCreate.as_view(), name='create_user'),
    path('drivers_list/', DriversListView.as_view(), name='driver_list'),
    path('start_trip/', StartTripView.as_view(), name='start_trip'),
    path('end_trip/', EndTripView.as_view(), name='end_trip'),
    path('trips_list/', DriverTripsList.as_view(), name='trips_list'),

]
