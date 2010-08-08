from django.db import models

class Guest(models.Model):

    NUMBER_TYPES = (
        ('home', 'Home'),
        ('cell-mobile', 'Cell/Mobile'),
        ('work', 'Work')
    )
    
    CHOICES = (
        ('N', 'No'),
        ('Y', 'Yes')
    )
    
    NUMERIC_CHOICES = (
        (0,0),
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
        (7,7),
        (8,8),
        (9,9),
        (10,10)
    )

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
    attending_ceremony       = models.CharField(verbose_name='Ceremony', max_length=1, choices=CHOICES)
    attending_reception      = models.CharField(verbose_name='Reception', max_length=1, choices=CHOICES)
    number_of_extra_adults   = models.IntegerField('Adults', choices=NUMERIC_CHOICES, default=0)
    number_of_extra_children = models.IntegerField('Children', choices=NUMERIC_CHOICES, default=0)

    # Meta
    created = models.DateField(auto_now_add=True)

    # class Meta:
    #     ordering = []

    def __unicode__(self):
        return u"%s, %s" % (self.last_name, self.first_name)