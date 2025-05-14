from django.urls import path
from ..Views.CompanyViews.CreateCompany import CompanyCreateView
from ..Views.CompanyViews.DeleteCompany import CompanyDeleteView
from ..Views.CompanyViews.GetAllCompanies import CompaniesGetView
from ..Views.CompanyViews.GetOneCompany import CompanyGetView
from ..Views.CompanyViews.UpdateCompany import CompanyUpdateView


urlpatterns = [
    path('Company/create/', CompanyCreateView.as_view(), name='Create Company'),
    path('Company/<int:pk>/delete/', CompanyDeleteView.as_view(), name='Delete Company'),
    path('Companyies/', CompaniesGetView.as_view(), name='Companyies List'),
    path('Company/<int:pk>/', CompanyGetView.as_view(), name='Company Detail'),
    path('Company/<int:pk>/update/', CompanyUpdateView.as_view(), name='Update Company'),
]