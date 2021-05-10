from rest_framework import serializers

from apps.trip.models import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


class TripRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('destination', 'origin')

        def create(self, validated_data):
            trip = Trip.objects.create(
                destination=validated_data['destination'],
                origin=validated_data['origin'],
            )

            trip.save()

            return trip




