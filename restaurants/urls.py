from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='landing'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('registration', views.registration, name='registration'),
    path('login', views.log_in, name='login'),
    path('logout', views.log_out, name='logout')
    # path('owner', views.owner_main, name='owner'),
    # path('owner/account', views.owner_account, name='owner_account'),
    # path('owner/institution', views.institution, name='owner_institution'),
    # path('owner/staff', views.staff, name='owner_staff'),
    # path('owner/reviews', views.reviews, name='owner_reviews'),
    # path('owner/statistics', views.statistics, name='owner_statistics'),
    # path('owner/settings', views.owner_settings, name='owner_settings'),
    # path('manager', views.manager_main, name='manager'),
    # path('manager/account', views.manager_account, name='manager_account'),
    # path('manager/staff', views.staff, name='manager_staff'),
    # path('manager/reviews', views.reviews, name='manager_reviews'),
    # path('manager/statistics', views.owner_staff, name='manager_statistics'),
    # path('manager/settings', views.owner_staff, name='manager_settings'),

]