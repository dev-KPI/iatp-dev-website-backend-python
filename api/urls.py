from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"members", views.MemberViewSet)
router.register(r"projects", views.ProjectViewSet)
router.register(r"languages", views.LanguageViewSet)
router.register(r"specializations", views.SpecializationViewSet)
router.register(r"sociallinks", views.SocialLinksViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
