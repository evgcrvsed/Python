from django.urls import path

import pages.views as pages

urlpatterns = [
    path('page1/', pages.index1),
    path('page2/', pages.index2)
]