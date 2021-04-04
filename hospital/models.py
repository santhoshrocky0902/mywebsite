from django.db import models


facility = (
    (1, '24*7 Service'),
    (2, 'Ambulance'),
    (3, 'Blood Bank'),
    (4, "covid'19"),
    (5, 'ICU'),
    (6, 'IP & OP Service'),
    (7, 'Pharmacy'),
     
)
superspeciality = (
    (1, 'Cardiology'),
    (2, 'Gastroenterology'),
    (3, 'Nephrology'),
    (4, 'Plastic Surgery'),
    (5, 'Paediatric Surgery'),
    (6, 'Surgical Gastroenterology'),
    (7, 'Surgical Onocology'),
    (8, 'Urology'),
    (9, 'Vascular Surgery'),
    (10,'neurology'),  
)
clinical = (
    (1, 'Anaesthesiology'),
    (2, 'Dentistry'),
    (3, 'Dermatology'),
    (4, 'ENT'),
    (5, 'General Medicine'),
    (6, 'General Surgery'),
    (7, 'OBG'),
    (8, 'Ophthalmology'),
    (9, 'Orthopaedics'),  
    (10, 'Paediatrics'), 
    (11, 'Physiotherapy'), 
    (12, 'Psychiatry'), 
    (13, 'Radio Diagnosis'), 
    (14, 'Pulmonology'), 
)

#news
class New(models.Model):
    news= models.TextField(default=None)
    date = models.DateField()
    image = models.ImageField(upload_to='hospital/news', blank=True, default=None)
    brochure = models.ImageField(upload_to='hospital/news/brochure', blank=True, default=None, null = True)
    def __str__(self):
        return str(self.date)
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image_url
# events
class Event(models.Model):
    title = models.CharField(max_length=50, default=None)
    description= models.TextField(default=None)
    date = models.DateField()
    image = models.ImageField(upload_to='hospital/events', blank=True, default=None)
    brochure = models.FileField(upload_to='hospital/events/brochure', blank=True, default=None, null = True)
    def __str__(self):
        return str(self.title)
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image_url

class indexvideo(models.Model):
    Video_Title= models.CharField(max_length=500, default=None)
    Video_Description= models.TextField(max_length=500, default=None)
    bg_file= models.ImageField(upload_to='hospital/videos', null=True, verbose_name="Background image ")
    videofile= models.FileField(upload_to='hospital/videos', null=True, verbose_name="video")

    def __str__(self):
        return str(self.Video_Title)
    
    class Meta:
        verbose_name = 'Home page video update'
        verbose_name_plural = 'Home page video update'

class gallery(models.Model):
    image = models.ImageField(upload_to='hospital/gallery', blank=False, default=None)
    title = models.CharField(max_length=50,default= None, null=False )
    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Hospital Gallery'
        verbose_name_plural = 'Hospital Gallery'


class Clinical(models.Model):
    Name = models.PositiveIntegerField(
        choices=clinical,
        default='1',
        )
    image = models.ImageField(upload_to='hospital/clinical', blank=True, default=None)
    overview = models.TextField()

    class Meta:
        verbose_name = 'Clinical'
        verbose_name_plural = 'Clinical'

    def __str__(self):
        return str(self.Name)

class Sspeciality(models.Model):
    Name = models.PositiveIntegerField(
        choices=superspeciality,
        default='1',
        )
    image = models.ImageField(upload_to='hospital/super-speciality', blank=True, default=None)
    overview = models.TextField()

    class Meta:
        verbose_name = 'Super Speciality'
        verbose_name_plural = 'Super Specialities'

    def __str__(self):
        return str(self.Name)

class Main_facility(models.Model):
    Name = models.PositiveIntegerField(
        choices=facility,
        default='1',
        )
    image = models.ImageField(upload_to='hospital/facilities', blank=True, default=None)
    overview = models.TextField()

    class Meta:
        verbose_name = 'Facility'
        verbose_name_plural = 'Facilities'

    def __str__(self):
        return str(self.Name)