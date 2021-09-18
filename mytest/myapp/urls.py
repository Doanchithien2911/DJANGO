from django.urls import path
from .views import Register,ToDoAPI,GetALLToDoAPI,GetOneToDOAPI,UpdateToDoAPI,RemoveToDoAPI,GetAllUserAPI
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',Register.as_view()),
    path('addtodo/',ToDoAPI.as_view()),
    path('getalltodo/',GetALLToDoAPI.as_view()),
    path('getonetodo/<int:id>',GetOneToDOAPI.as_view()),
    path('updatetodo/<int:id>',UpdateToDoAPI.as_view()),
    path('removetodo/<int:id>',RemoveToDoAPI.as_view()),
    path('getalluser/',GetAllUserAPI.as_view())
]