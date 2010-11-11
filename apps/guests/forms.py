from django import forms
from models import Guest
from settings import INVITE_CODES

class GuestForm(forms.ModelForm):
    
    """ Build a signup form without the rsvp information """
    
    class Meta:
        model = Guest
        exclude = [
            'attending_ceremony',
            'attending_reception',
            'number_of_adults',
            'number_of_children'
        ]

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
            fields = field_list + ['number_of_adults', 'number_of_children']

        def __init__(self, *args, **kwargs):
            
            """
            Override the form's fields to display the appropriate RSVP options.
            """
            
            super(RSVPForm, self).__init__(*args, **kwargs)
            if self.fields.get('attending_ceremony'):
                self.fields['attending_ceremony'].required = True
                self.fields['attending_ceremony'].widget=forms.RadioSelect(choices=Guest.ATTENDANCE_CHOICES)
            if self.fields.get('attending_reception'):
                self.fields['attending_reception'].required = True
                self.fields['attending_reception'].widget=forms.RadioSelect(choices=Guest.ATTENDANCE_CHOICES)
            
        def clean(self):
            
            """
            Validate that if they have selected to come to an event,
            they've specified at least one person.
            """
            
            cleaned_data = self.cleaned_data
            attending_ceremony = cleaned_data.get('attending_ceremony')
            attending_reception = cleaned_data.get('attending_reception', False)
            number_of_adults = cleaned_data.get('number_of_adults')
            if not number_of_adults:
                if attending_reception:
                    self._errors["number_of_adults"] = self.error_class(["Please specify how many adults will be attending"])
                if attending_ceremony:
                    self._errors["number_of_adults"] = self.error_class(["Please specify how many adults will be attending"])            
            del cleaned_data["number_of_adults"]
            return cleaned_data
 
    return RSVPForm

# This works
# self.fields['attending_ceremony'].required = True
# self.fields['attending_ceremony'].widget=forms.RadioSelect()
# self.fields['attending_ceremony'].choices=Guest.ATTENDANCE_CHOICES

# This works
# self.fields['attending_ceremony'] = forms.TypedChoiceField(
#     required=True,
#     widget=forms.RadioSelect,
#     choices=Guest.CHOICES
# )

# This doesn't - the choices aren't set (it's an empty list)
# Is this because (as noted in Pro Django) that a widget is instantiated
# at the same time as the field itself?
# self.fields['attending_ceremony'] = forms.TypedChoiceField(
#     required=True,
#     widget=forms.RadioSelect(choices=Guest.CHOICES)
# )