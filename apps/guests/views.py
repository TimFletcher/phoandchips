from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views.generic.simple import direct_to_template
from settings import INVITE_CODES
from forms import get_rsvp_form, GuestForm
from models import Guest

def register(request):

    """
    Allow a user to register their attendance to one or more of the events
    """

    form = GuestForm(request.POST or None)
    if form.is_valid():
        request.session['guest'] = form.save().id
        return HttpResponseRedirect(reverse('guests_rsvp'))
    return render_to_response(
        'guest_register.html', {
            'form': form
        },
        context_instance=RequestContext(request)
    )

def rsvp(request):

    """
    Get from the user attendance information for the wedding and reception.
    We only allow visitors coming via the registration page.
    """

    guest = get_object_or_404(Guest, pk=request.session.get('guest', None))
    field_list = ['attending_reception']
    if guest.invite_code == INVITE_CODES['ceremony']:
        field_list.append('attending_ceremony')
    RSVPForm = get_rsvp_form(field_list)
    form = RSVPForm(request.POST or None, instance=guest)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('guests_thanks'))
    return render_to_response(
        'guest_rsvp.html', {
            'guest': guest,
            'form': form
        },
        context_instance=RequestContext(request)
    )

def thanks(request):
    guest = get_object_or_404(Guest, pk=request.session.get('guest', None))
    request.session.clear()
    return direct_to_template(
        request,
        template = 'guest_thanks.html',
        extra_context = {
            'guest': guest
        }
    )