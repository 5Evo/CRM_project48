from rest_framework import viewsets
from .models import Lead, Status, Action, NextAction
from .serializers import LeadSerializer, StatusSerializer, ActionSerializer, NextActionSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class NextActionViewSet(viewsets.ModelViewSet):
    queryset = NextAction.objects.all()
    serializer_class = NextActionSerializer
