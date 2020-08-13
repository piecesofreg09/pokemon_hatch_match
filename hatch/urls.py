from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.HatchIndex, name='hatch-index'),
    path('prepare_hatch', views.HatchPrepareView, name='hatch-prepare'),
    path('submit_hatch', views.HatchPostHatchPairView, name='hatch-submit'),
    path('hatched', views.HatchedListView, name='hatched-list')
]