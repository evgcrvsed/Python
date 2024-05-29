from django.urls import path

import pets.views as pets

urlpatterns = [
    path('pets/<int:cat_id>/', pets.index)
]