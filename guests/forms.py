from django import forms
from models import Guest
# from models import CHOICES
from settings import INVITE_CODES

class GuestForm(forms.ModelForm):
    
    """ Build a signup form without the rsvp information """
    
    class Meta:
        model = Guest
        exclude = ['attending_ceremony', 'attending_reception',
                   'number_of_extra_adults', 'number_of_extra_children']

    def clean_invite_code(self):
        code = self.cleaned_data['invite_code']        
        if not code in INVITE_CODES.values():
            raise forms.ValidationError('Invite code not valid.')
        return code


def get_rsvp_form(field_list, *args, **kwargs):
    
    """
    Function to dynamically create an RSVP form. We show fields based on
    whether the guest is invited to the ceremony or not.
    """
    
    class RSVPForm(forms.ModelForm):

        class Meta:
            model = Guest
            fields = field_list + ['number_of_extra_adults', 'number_of_extra_children']

        def __init__(self, *args, **kwargs):
            super(RSVPForm, self).__init__(*args, **kwargs)
            if self.fields.get('attending_reception', False):
                self.fields['attending_reception'].widget = forms.RadioSelect(choices=Guest.CHOICES)                
                self.fields['attending_reception'].initial=None
            if self.fields.get('attending_ceremony', False):
                self.fields['attending_ceremony'].widget = forms.RadioSelect(choices=Guest.CHOICES)
                self.fields['attending_ceremony'].initial=None

    return RSVPForm