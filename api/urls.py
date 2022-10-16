from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"members", views.MemberCreateViewSet, basename="members")
router.register(r"projects", views.ProjectCreateViewSet, basename="projects")
router.register(r"languages", views.LanguageViewSet)
router.register(r"sociallinks", views.SocialLinksViewSet)
router.register(r"specializations", views.SpecializationViewSet)
router.register(r"members-details", views.MemberDetailViewSet)
router.register(r"projects-details", views.ProjectDetailViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
