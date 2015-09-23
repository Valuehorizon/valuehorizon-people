# Import Django libraries
from django.db import models

# Import Valuehorizon libraries
from countries.models import Country

# Import other libraries
from datetime import date

class Person(models.Model):
    """
    Represents a person, such as John Doe, Joe Public, or Jiminy Cricket.
    """

    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    TITLE_CHOICES = (
        (u'DR', u'Dr.'),
        (u'MR', u'Mr.'),
        (u'MS', u'Ms.'),
        (u'MRS', u'Mrs.'),
        (u'SIR', u'Sir'),
        (u'LORD', u'Lord'),
    )
    title = models.CharField(max_length=10, choices=TITLE_CHOICES)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    other_names = models.CharField(max_length=255, blank=True, help_text="Middle names, space separated")
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    profile = models.TextField(blank=True, help_text="Description of Person")
    is_deceased = models.BooleanField(default=False)
    nationalities = models.ManyToManyField(Country, related_name="nationalities")
    
    # Cached Data
    date_modified = models.DateTimeField(null=True, blank=True, editable=False, auto_now=True)
    date_created = models.DateTimeField(null=True, blank=True, editable=False, auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'People'
        verbose_name = 'Person'
        ordering = ['last_name', 'first_name', 'date_of_birth']

    def __unicode__(self):
        return u'%s' % (unicode(self.full_name))
    
    
    @property
    def age(self, as_at_date=None):
        """
        Compute the person's age
        """
        as_at_date = date.today() if as_at_date == None else as_at_date
        
        if self.date_of_birth != None:
            if (as_at_date.month >= self.date_of_birth.month) and (as_at_date.day >= self.date_of_birth.day):
                return (as_at_date.year - self.date_of_birth.year)
            else:
                return ((as_at_date.year - self.date_of_birth.year) -1)
        else:
            return None
    
    @property
    def short_name(self):
        """
        Return the title and last name
        """
        return "%s %s" (self.get_title_display(), self.last_name)
    
    @property
    def name(self):
        """
        Return the person's name. If we have special titles, use them, otherwise,
        don't include the title.
        """
        if self.title in ["DR", "SIR", "LORD"]:
            return "%s %s %s" % (self.get_title_display(), self.first_name, self.last_name)
        else:
            return "%s %s" (self.first_name, self.last_name)
    
    @property
    def full_name(self):
        """
        Return the title and full name
        """
        return "%s %s %s %s" % (self.get_title_display(), 
                                self.first_name,
                                self.other_names.replace(",", ""),
                                self.last_name)
    
    def get_absolute_url(self):
        return ('person_profile', (), { 'person_id': self.id})
    get_absolute_url = models.permalink(get_absolute_url)
    
    def save(self, *args, **kwargs):
        """
        If date of death is specified, set is_deceased to true
        """
        if self.date_of_death != None:
            self.is_deceased = True
            
        # Since we often copy and paste names from strange sources, do some basic cleanup
        self.first_name = self.first_name.strip()
        self.last_name = self.last_name.strip()
        self.other_names = self.other_names.strip()
        
        # Call save method
        super(Person, self).save(*args, **kwargs) # Call the "real" save() method.
            
        


