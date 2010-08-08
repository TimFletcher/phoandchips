from django.db import models
from django.template.defaultfilters import linebreaks

class Entry(models.Model):

    # Core
    author = models.CharField(blank=False, max_length=100)
    text   = models.TextField(blank=False)

    # Meta
    created = models.DateTimeField(auto_now_add=True)
    invite_code = models.CharField(max_length=20, help_text="Just checking you're allowed!")
    
    class Meta:
        ordering = ['created']
        verbose_name_plural = "Entries"

    def __unicode__(self):
        return u"Guestbook entry by %s" % self.author

    def save(self, *args, **kwargs):
        self.text = linebreaks(self.text)
        super(Entry, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('Entry', [self.id])
        
    def get_absolute_url(self):
        return reverse('guestbook_object_detail', kwargs={'slug': self.slug})