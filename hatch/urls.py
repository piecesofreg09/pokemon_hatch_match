from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.HatchIndex, name='hatch-index'),
    path('submit_hatch', views.HatchPostHatchPairView, name='hatch-submit'),
    path('hatched', views.HatchedListView, name='hatched-list')
]