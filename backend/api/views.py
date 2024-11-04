from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q

from api.models import Message, User


@csrf_exempt
def add_friend(request):
    """Функция добавления в друзья."""
    if request.method == 'POST' and request.user.is_authenticated:
        friend_username = request.POST.get('friend_username')
        if friend_username:
            try:
                if request.user.add_friend(friend_username):
                    return redirect('api:index')
                else:
                    return redirect('api:index')
            except User.DoesNotExist:
                return redirect('api:index')
    return redirect('api:index')


@login_required
def chat_view(request):
    """Функция выбора чата."""
    messages = Message.objects.filter(
        recipient=request.user) | Message.objects.filter(sender=request.user)
    messages = messages.order_by('timestamp')
    selected_friend = request.POST.get('recipient', None)

    if request.method == 'POST':
        message_text = request.POST.get('message')
        recipient_username = request.POST.get('recipient')

        if message_text and recipient_username:
            try:
                recipient = User.objects.get(username=recipient_username)
                Message.objects.create(
                    sender=request.user,
                    recipient=recipient,
                    text=message_text
                )
                return redirect('api:index')
            except User.DoesNotExist:
                return render(
                    request, 'api/index.html',
                    {'messages': messages, 'selected_friend': selected_friend,
                     'error': 'User does not exist.'
                     }
                )

    return render(
        request, 'api/index.html',
        {'messages': messages, 'selected_friend': selected_friend
         }
    )


@login_required
def get_chat_messages(request, recipient_username):
    """Функция получения сообщений в чате."""
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(recipient__username=recipient_username)) |
        (Q(sender__username=recipient_username) & Q(recipient=request.user))
    ).order_by('timestamp')

    message_data = [{"sender": msg.sender.username, "text": msg.text}
                    for msg in messages]
    return JsonResponse({"messages": message_data})
