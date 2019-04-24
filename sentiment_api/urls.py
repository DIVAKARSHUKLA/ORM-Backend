from django.contrib import admin
from django.urls import path, include
from main import views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from admin import views as admin_views

router = routers.DefaultRouter()
router.register('user', views.UserView)
router.register('profile', views.UserProfile)

urlpatterns = [
    path('', include(router.urls)),
    # path('realAdmin',admin.site.urls),
    path('admin/', admin_views.index, name='admin'),
    path('login/', admin_views.login_view, name='login'),
    path('logout/', admin_views.logout_view, name='logout'),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('userProfile/<int:id>/', admin_views.userProfile, name="userProfile"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
