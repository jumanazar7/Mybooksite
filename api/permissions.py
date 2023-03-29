from rest_framework.permissions import BasePermission,SAFE_METHODS



class IsAuthorOrReadOnly(BasePermission):
    def has_object_permishin(self,request,view,obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

class CustomDjangoModelPermission(BasePermission):
    def __init__(self) -> None:
        self.perms_map["GET"] =['%(app_label)s.view_%(model_name)s']