from django import forms
from models import Entry
from settings import INVITE_CODES

class EntryForm(forms.ModelForm):
    
    """ Build a guestbook form validating the invite code """
    
    class Meta:
        model = Entry

    def clean_invite_code(self):
        code = self.cleaned_data['invite_code']        
        if not code in INVITE_CODES.values():
            raise forms.ValidationError('Invite code not valid.')
        return code