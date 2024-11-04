from django.urls import path

from api.views import chat_view, add_friend, get_chat_messages


app_name = 'api'

urlpatterns = [
    path('add_friend/', add_friend, name='add_friend'),
    path('api/messages/<str:recipient_username>/', get_chat_messages, name='get_chat_messages'),
    path('', chat_view, name='index'),
]
