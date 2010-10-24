from django.db import models

class Guest(models.Model):

    NUMBER_TYPES = (
        ('home', 'Home'),
        ('cell-mobile', 'Cell/Mobile'),
        ('work', 'Work')
    )    
    ATTENDANCE_CHOICES = (
        (0, 'No'),
        (1, 'Yes')
    )
    NUMERIC_CHOICES = [(i,i) for i in range(0,11)]

    def __unicode__(self):
        return u"%s (%s)" % (self.phone, self.number_type)

    # Step 1
    first_name  = models.CharField(max_length=80)
    last_name   = models.CharField(max_length=80)
    phone       = models.CharField(blank=True, max_length=80)
    phone_type  = models.CharField(blank=True, max_length=80, choices=NUMBER_TYPES, default=NUMBER_TYPES[0])
    email       = models.EmailField(blank=True)
    address     = models.TextField(blank=True, help_text="So we can say thanks!")
    invite_code = models.CharField(max_length=20)

    # Step 2
    attending_ceremony  = models.IntegerField('Ceremony', choices=ATTENDANCE_CHOICES, null=True)
    attending_reception = models.IntegerField('Reception', choices=ATTENDANCE_CHOICES, null=True)
    number_of_adults    = models.IntegerField('Adults', choices=NUMERIC_CHOICES, default=0)
    number_of_children  = models.IntegerField('Children', choices=NUMERIC_CHOICES, default=0)

    # Meta
    created = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return u"%s, %s" % (self.last_name, self.first_name)