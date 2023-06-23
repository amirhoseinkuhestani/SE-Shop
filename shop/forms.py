from django import forms
from .models import Ticket, TicketReply

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['subject', 'message']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = TicketReply
        fields = ['reply_message']