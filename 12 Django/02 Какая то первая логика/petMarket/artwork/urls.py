from django.urls import path

import artwork.views as artwork

urlpatterns = [
    path('artwork/mona-lisa/', artwork.mona_lisa),
    path('artwork/starry-night/', artwork.starry_night)
]