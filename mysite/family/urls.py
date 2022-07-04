from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('saludar/<nombre>', views.saludar),
    path('createFamilyMemberForm', views.create_family_member_form),
    path('createFamilyMember', views.create_family_member),
]