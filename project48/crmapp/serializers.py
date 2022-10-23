from .models import Lead, Status, Action, NextAction, Tag
from rest_framework import serializers


# Serializers define the API representation.
class LeadSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField()             # user выводим в виде строки
    tags = serializers.StringRelatedField(many=True)    # tags выводим в виде строк

    class Meta:
        model = Lead
        fields = '__all__'


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
        fields = ['lead', 'action_type', 'action_date']


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'