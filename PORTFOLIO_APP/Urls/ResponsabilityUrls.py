from django.urls import path
from ..Views.ResponsabilityViews.CreateResponsability import ResponsabilityCreateView
from ..Views.ResponsabilityViews.DeleteResponsability import ResponsabilityDeleteView
from ..Views.ResponsabilityViews.GetAllResponsabilities import ResponsabilitiesGetView
from ..Views.ResponsabilityViews.GetOneResponsability import ResponsabilityGetView
from ..Views.ResponsabilityViews.UpdateResponsability import ResponsabilityUpdateView


urlpatterns = [
    path('Responsability/create/', ResponsabilityCreateView.as_view(), name='Create Responsability'),
    path('Responsability/<int:pk>/delete/', ResponsabilityDeleteView.as_view(), name='Delete Responsability'),
    path('Responsabilities/', ResponsabilitiesGetView.as_view(), name='Responsabilitcies List'),
    path('Responsability/<int:pk>/', ResponsabilityGetView.as_view(), name='Responsability Detail'),
    path('Responsability/<int:pk>/update/', ResponsabilityUpdateView.as_view(), name='Update Responsability'),
]