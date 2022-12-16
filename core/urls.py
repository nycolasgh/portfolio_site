from django.urls import path
from . import views


urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerPage, name='register'),
    path('', views.home, name='home'),
    path('profile/<int:pk>', views.userProfile, name='profile'),
    path('client/<int:pk>', views.clientDetails, name='client-details'),
    path('feedback/', views.feedbackForm, name='feedback'),
    path('update-feedback/<int:pk>', views.updateFeedback, name='update-feedback'),
    path('delete-feedback/<int:pk>', views.deleteFeedback, name='delete-feedback'),

]
