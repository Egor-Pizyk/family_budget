from django.urls import path
from . import views

app_name = 'b_app'
urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', views.AuthUserView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('password-reset/', views.password_reset, name='password-reset'),
    path('password-reset/done/<int:pk>', views.password_reset_done, name='password-reset-done'),

    path('create_category/', views.create_category, name='create_category'),
    path('create_count/', views.create_count, name='create_count'),
    path('create_trasaction/', views.create_transaction, name='create_transaction'),
    path('set-transfer/', views.set_transfer_to_card, name='set_transfer_to_card'),


    path('', views.home, name='home'),
    # path('message-page', views.messages_page, name='messages_page'),

]
