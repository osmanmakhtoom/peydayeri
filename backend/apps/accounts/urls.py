from django.urls import include, path

app_name = "accounts"

urlpatterns = [
    path('api/', include("accounts.api.urls"), name="accounts-api")
]
