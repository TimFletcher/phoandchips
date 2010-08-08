from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from settings import INVITE_CODES
from forms import get_rsvp_form, GuestForm

def register(request):
    
    """
    Allow a user to register their attendance to one or more of the events
    """

    context = dict()
    form = context['form'] = GuestForm(request.POST or None)
    if form.is_valid():
        guest = form.save()
        request.session['guest'] = guest
        return HttpResponseRedirect(reverse('guests_rsvp'))

    return render_to_response(
        'guest_register.html',
        context,
        context_instance=RequestContext(request)
    )


def rsvp(request):

    """
    Get from the user attendance information for the wedding and reception.
    We only allow visitors coming via the registration page.
    """

    guest = request.session.get('guest', None)
    if not guest:
        raise Http404
    context = dict()
    field_list = ['attending_reception']
    if guest.invite_code == INVITE_CODES['ceremony']:
        field_list.append('attending_ceremony')
    RSVPForm = get_rsvp_form(field_list)
    form = context['form'] = RSVPForm(request.POST or None, instance=guest)
    if form.is_valid():
        form.save()
        request.session['guest'] = guest
        return HttpResponseRedirect(reverse('guests_thanks'))

    return render_to_response(
        'guest_rsvp.html',
        context,
        context_instance=RequestContext(request)
    )