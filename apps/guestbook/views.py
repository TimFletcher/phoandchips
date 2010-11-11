from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib import messages
from forms import EntryForm
from models import Entry

def guestbook(request):
    
    """
    Allow a user to add to the guestbook
    """

    context = dict()
    context['entry_list'] = Entry.objects.all().order_by('-created')
    form = context['form'] = EntryForm(request.POST or None)
    if form.is_valid():
        entry = form.save()
        messages.success(request, 'Thanks %s, your message was successfully added!' % entry.author)
        return HttpResponseRedirect(reverse('guestbook_guestbook_guestbook'))

    return render_to_response(
        'guestbook.html',
        context,
        context_instance=RequestContext(request)
    )