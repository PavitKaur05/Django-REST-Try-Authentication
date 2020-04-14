from django.urls import path
from . import views
from django.conf.urls import include,url
from rest_framework.routers import DefaultRouter #for viewset
router=DefaultRouter()
router.register('ping',views.check_active,basename='checkServer')
router.register('registration',views.UserProfileViewSet)
router.register('login',views.LoginViewSet,basename='login')
urlpatterns=[url(r'',include(router.urls))]
