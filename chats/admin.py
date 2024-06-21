from django.contrib import admin
from chats.models import ChatThread, ChatMessage

admin.site.register(ChatMessage)


class AdminMessage(admin.TabularInline):
    model = ChatMessage


class ThreadAdmin(admin.ModelAdmin):
    inlines = [AdminMessage]

    class Meta:
        model = ChatThread


admin.site.register(ChatThread, ThreadAdmin)
