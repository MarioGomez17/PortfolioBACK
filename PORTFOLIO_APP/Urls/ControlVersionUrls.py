from django.urls import path
from ..Views.ControlVersionViews.CreateControlVersion import ControlVersionCreateView
from ..Views.ControlVersionViews.DeleteControlVersion import ControlVersionDeleteView
from ..Views.ControlVersionViews.GetAllControlsVersion import ControlsVersionGetView
from ..Views.ControlVersionViews.GetOneControlVersion import ControlVersionGetView
from ..Views.ControlVersionViews.UpdateControlVersion import ControlVersionUpdateView


urlpatterns = [
    path('ControlVersion/create/', ControlVersionCreateView.as_view(), name='Create Control Version'),
    path('ControlVersion/<int:pk>/delete/', ControlVersionDeleteView.as_view(), name='Delete Control Version'),
    path('ControlVersions/', ControlsVersionGetView.as_view(), name='Control Versions List'),
    path('ControlVersion/<int:pk>/', ControlVersionGetView.as_view(), name='Control Version Detail'),
    path('ControlVersion/<int:pk>/update/', ControlVersionUpdateView.as_view(), name='Update Control Version'),
]