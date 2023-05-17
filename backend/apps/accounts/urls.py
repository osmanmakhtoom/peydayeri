from django.urls import include, path

app_name = "accounts"

urlpatterns = [
    path('api/', include("apps.accounts.api.urls"), name="accounts-api")
]
