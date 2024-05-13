from django.urls import path
from .views import home, profile, RegisterView, project, my_projects, edit_project

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('upload-project', project, name='upload-project'),
    path('my-projects/', my_projects, name='my-projects'),
    path('edit-project/<int:project_id>/', edit_project, name='edit-project'),
]
