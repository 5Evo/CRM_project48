from .models import Lead, Status, Action, NextAction
from rest_framework import serializers


# Serializers define the API representation.
class LeadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lead
        fields = ['first_name', 'middle_name', 'last_name', 'mail']


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ['name']


class ActionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Action
        fields = ['name']


class NextActionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NextAction
        fields = ['name', 'action_type', 'action_date']