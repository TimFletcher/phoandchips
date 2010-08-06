from django.db import models

class Guest(models.Model):

    NUMBER_TYPES = (
        ('home', 'Home'),
        ('cell', 'Cell'),
        ('work', 'Work')
    )
    
    CHOICES = (
        (0, 'No'),
        (1, 'Yes')
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
    phone_type  = models.CharField(blank=False, max_length=80, choices=NUMBER_TYPES, default=NUMBER_TYPES[0])
    address     = models.TextField(blank=True)
    invite_code = models.CharField(max_length=20)

    # Step 2
    attending_ceremony       = models.IntegerField('I will be attending the ceremony', choices=CHOICES, default=0)
    attending_reception      = models.IntegerField('I will be attending the reception', choices=CHOICES, default=0)
    number_of_extra_adults   = models.IntegerField('Adults', choices=NUMERIC_CHOICES, default=0)
    number_of_extra_children = models.IntegerField('Children', choices=NUMERIC_CHOICES, default=0)

    # Meta
    date_added = models.DateField(auto_now_add=True)

    # class Meta:
    #     ordering = []

    def __unicode__(self):
        return u"%s, %s" % (self.last_name, self.first_name)


# class GuestPlusX(models.Model):
#     
#     PERSON_TYPE = (
#         ('adult', 'Adult'),
#         ('child', 'Child')
#     )
# 
#     guest      = models.ForeignKey(Guest)
#     first_name = models.CharField(max_length=80)
#     last_name  = models.CharField(max_length=80)
#     type       = models.CharField(max_length=80, choices=PERSON_TYPE)
# 
#     # class Meta:
#     #     ordering = []
#     #     verbose_name, verbose_name_plural = "", "s"
#     
#     def __unicode__(self):
#         return u"Guest: %s %s" % (self.first_name, self.last_name)
#     
#     # @models.permalink
#     # def get_absolute_url(self):
#     #     return ('Guest', [self.id])