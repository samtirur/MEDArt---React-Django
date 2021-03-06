from django.urls import path
from django.urls.conf import include
from .views import index,HospitalViewSet,MyTokenObtainPairView,getUserProfile,getUSers,registerUser,getHospitals,getHospital,registerHospital
from rest_framework import routers

from api import views


router = routers.DefaultRouter()
# router.register('users',UserViewSet)
router.register('hpt',HospitalViewSet)


urlpatterns = [
    path('api/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/users/register/',registerUser),
    path('api/hospitals/',getHospitals),
    path('api/hospitals/register/',registerHospital),
    path('api/hospital/<str:pk>',getHospital),
    path('api/users/profile',getUserProfile,name="users-profile"),
    path('api/users/',getUSers),
    path('api/',include(router.urls)),
    path('',index)
]