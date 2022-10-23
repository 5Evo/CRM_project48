from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    '''
    SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
    даем доступ только одним из 3-методов без возможности редактирования
    '''
    def has_permission(self, request, view):    # request - данный запроса, view - данные вьюшки
        return request.method in SAFE_METHODS


# class IsAdmin(BasePermission):
'''
заготовка для многопользовательского доступа в модели CrmUser должно быть поле is_admin, 
которое дает право редактировать Status, Action, Tag для каждого аккаунта
'''
#     def has_permission(self, request, view):
#         if request.user.is_authenticated:
#             return request.user.is_admin
#         return False
