from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from chats.models import ChatThread


@login_required
def messages_page(request):
    threads = ChatThread.objects.by_user(user=request.user).prefetch_related('chat_message_thread').order_by('timestamp')
    context = {
        'Threads': threads
    }
    return render(request, 'messages.html', context)


def home(request):
    return render(request, 'home.html')
