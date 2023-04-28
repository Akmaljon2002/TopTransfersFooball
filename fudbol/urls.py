from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from asosiy.views import*
from rest_framework_simplejwt.views import (TokenRefreshView, TokenObtainPairView, )
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Top Transfer Footbal",
      default_version='v1',
      description="Yakuniy loyiha uchun",
      # terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact("Akmaljon Fayzullayev, <akmaljonfayzullayev07@gmail.com>"),
      # license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('clubs/', ClubsAPIView.as_view()),
    path('clubs/<str:country>/', ClubCountryView.as_view()),
    path('players/<int:pk>/', ClubPlayersAPIView.as_view()),
    path('players/', PlayersAPIView.as_view()),
    path('latest_tr/', Latest_trAPIView.as_view()),
    path('transfers/', TransferAPIView.as_view()),
    path('transfer/<str:m>/', Transfer_mAPIView.as_view()),
    path('tr-records/', Tr_recordsAPIView.as_view()),
    path('u20-players/', U20playersAPIView.as_view()),
    path('predictions/', AccuratePrAPIView.as_view()),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('docs2/', schema_view.with_ui('redoc', cache_timeout=0)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
