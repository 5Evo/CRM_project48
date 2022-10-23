from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import ReadOnly
from .models import Lead, Status, Action, NextAction, Tag, UserDataMixin
from .serializers import LeadSerializer, StatusSerializer, ActionSerializer, NextActionSerializer, TagSerializer


class LeadViewSet(UserDataMixin, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]   # даем доступ только залогиненым пользователям к собственным лидам
    # оптимизация запроса: select_related('user') - для foreign_key
    # оптимизация запроса: prefetch_related('tags'): - для many_to_many
    queryset = Lead.objects.select_related('user').prefetch_related('tags')
    serializer_class = LeadSerializer


class StatusViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]   # IsAdminUser - права администратора Django
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class ActionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]   # IsAdminUser - права администратора Django
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class NextActionViewSet(viewsets.ModelViewSet):
    queryset = NextAction.objects.all()
    serializer_class = NextActionSerializer


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]   # IsAdminUser - права администратора Django
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
