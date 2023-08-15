from rest_framework.routers import DefaultRouter

from apps.accounts.api.views import (
    ActivationViewSet,
    ProfileView,
    RegisterViewSet,
    SocialAccountsView,
    UserView
)
from django.urls import path

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path("user-info/", UserView.as_view(), name="user"),
    path("social-accounts/", SocialAccountsView.as_view(),
         name="social_accounts"),
]

router = DefaultRouter()
router.register("authentication", RegisterViewSet, basename="authentication")
router.register("activation", ActivationViewSet, basename="activation")
urlpatterns += router.urls
