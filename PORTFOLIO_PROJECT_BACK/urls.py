"""
URL configuration for PORTFOLIO_PROJECT_BACK project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('Admin/', admin.site.urls),
    path('Portfolio/', include('PORTFOLIO_APP.Urls.AcademyUrls')),
    path('Portfolio/', include('PORTFOLIO_APP.Urls.CityUrls')),
    path('Portfolio/', include('PORTFOLIO_APP.Urls.CountryUrls')),
    path('Portfolio/', include('PORTFOLIO_APP.Urls.DepartmentUrls')),
    path('Portfolio/', include('PORTFOLIO_APP.Urls.DeveloperUrls')),
    path('Portfolio/', include('PORTFOLIO_APP.Urls.DivisionUrls')),
    path('Portfolio/', include('PORTFOLIO_APP.Urls.EducationUrls')),
    path('Portfolio/', include('PORTFOLIO_APP.Urls.EducationTypeUrls')),
    path('Portfolio/', include('PORTFOLIO_APP.Urls.LanguageUrls')),
    path('Portfolio/', include('PORTFOLIO_APP.Urls.ProgrammingLanguageUrls')),
    path('Portfolio/', include('PORTFOLIO_APP.Urls.ProjectUrls')),
    path('Portfolio/', include('PORTFOLIO_APP.Urls.TechnologyUrls'))
]
