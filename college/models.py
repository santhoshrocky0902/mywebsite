from django.db import models
#news
class New(models.Model):
    news= models.TextField(default=None)
    date = models.DateField()
    image = models.ImageField(upload_to='college/news', blank=True, default=None)
    brochure = models.ImageField(upload_to='college/news/brochure', blank=True, default=None, null = True)
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
    image = models.ImageField(upload_to='college/events', blank=True, default=None)
    brochure = models.FileField(upload_to='college/events/brochure', blank=True, default=None, null = True)
    def __str__(self):
        return str(self.title)
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image_url

# department 
program_type = (
    (1, 'Under Graduate'),
    (2, 'Post Graduate'),
   
)

dept = (
    (1, 'Physiology'),
    (2, 'Anatomy'),
    (3, 'Community Medicine'),
    (4, 'Tb & Chest Diseases'),
    (5, 'Paediatrics'),
    (6, 'Orthopaedics'),
    (7, 'Opthalmology'),
    (8, 'Psychiatry'),
    (9, 'Obstetrics & Gynaecology'),
    (10, 'General Surgery'),
    (11, 'Forensic Medicine'),
    (12, 'ENT'),
    (13, 'Dermatology'),
    (14, 'Dentistry'),
    (15, 'Anaesthesiology'),
    (16, 'Pharmacology'),
    (17, 'Bio Chemistry'),
    (18, 'Pathology'),
    (19, 'Micro Biology'),
    (20, 'Radio Diagnosis'),
    (21, 'General Medicine'),  
)

facility = (
    (1, 'Central Laboratory'),
    (2, 'Library'),
    (3, 'Infrastructure'),
    (4, 'Internet Facility'),
    (5, 'Seminar Hall'),
    (6, 'Canteen'),
    (7, 'Hostel and Quarters'),
    (8, 'Transport'),
    (9, 'Anti-ragging & Gender harassment'),  
)


class Department(models.Model):
    Name = models.PositiveIntegerField(
    choices=dept,
    default='1',
    )
    background_image= models.ImageField(upload_to='college/department', blank=False, default=None)
    vision= models.TextField(default=None)
    mission= models.TextField(default=None)
    program_type = models.PositiveIntegerField(
    choices=program_type,
    default='1',
    )
    duration = models.IntegerField(default=None, help_text='No of years')
    brochure = models.FileField(upload_to='college/department/brochure', blank=True, default=None)
    department_description= models.TextField(default=None)
    # achievement = models.ManyToManyField(Achieve, through='AttributeValue')
    def __str__(self):
        return str(self.Name)

 
        


class best_moments(models.Model):
    best_moment= models.ImageField(upload_to='college/department/best-moments', blank=False, default=None)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Best Moment'
        verbose_name_plural = 'Best Moments'

    def __str__(self):
        return str(self.pk)

class Achievement(models.Model):
    achievement = models.TextField(default=None, max_length=100)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'

    def __str__(self):
        return str(self.pk)

class Awards(models.Model):
    awards = models.TextField(default=None, max_length=100)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Award'
        verbose_name_plural = 'Awards'
    
    def __str__(self):
        return str(self.pk)

class HOD(models.Model):
    name = models.CharField(max_length=50, default=None)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='college/department/HOD', blank=False, default=None)
    Qualification_And_Specification = models.CharField(max_length=50, default=None)
    AreaOfIntrest = models.CharField(max_length=50, default=None)
    experience = models.IntegerField( default=None, null=True)
    email = models.EmailField()
    Phone = models.IntegerField()

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Head of the department'
        verbose_name_plural = 'Head of the department'

class Professor(models.Model):
    name = models.CharField(max_length=50, default=None)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    Qualification_And_Specification = models.CharField(max_length=50, default=None)
    AreaOfIntrest = models.CharField(max_length=50, default=None)
    email = models.EmailField()
    experience = models.IntegerField( default=None)
    Phone = models.IntegerField()

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professors'

class Facility(models.Model):
    name=models.CharField(max_length=50, default=None)
    quantity = models.IntegerField(default=None)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Facility'
        verbose_name_plural = 'Facilities'
   


class Gallery(models.Model):
    image = models.ImageField(upload_to='college/department/gallery', blank=False, default=None)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return str(self.pk)


# facilities


class Main_facility(models.Model):
    Name = models.PositiveIntegerField(
        choices=facility,
        default='1',
        )
    image = models.ImageField(upload_to='college/facility', blank=False, default=None)
    overview = models.TextField()

    class Meta:
        verbose_name = 'facility'
        verbose_name_plural = 'Facilities'

    def __str__(self):
        return str(self.Name)

class Hyperlink(models.Model):
    title = models.CharField(max_length=250, default=None)
    hyperlink = models.URLField( max_length=250)
    facility_name = models.ForeignKey(Main_facility, on_delete=models.CASCADE, default=None)

class PaperPublication(models.Model):
    title = models.CharField(max_length=250, default=None)
    author = models.CharField(max_length=150, default=None)
    date = models.DateField()
    pdf_file = models.FileField(upload_to="college/department/paper_publications")
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE, default =None)


class OnlineApplication(models.Model):
    degree = models.CharField(max_length=20, default=None)
    image = models.ImageField(upload_to='college/online-application', blank=False, default=None)
    course_type = models.CharField(max_length=20, default=None)
    year = models.CharField(max_length=20, default=None)
    branch = models.CharField(max_length=20, default=None)

    applicant_name = models.CharField(max_length=50, default=None)
    date_of_birth = models.CharField(max_length=20, default=None)
    age = models.IntegerField(default=None, null=True)
    blood_group = models.CharField(max_length=3, default=None)
    mother_tounge = models.CharField(max_length=15, default=None)
    religion = models.CharField(max_length=20, default=None)
    cast = models.CharField(max_length=50, default=None)
    community =models.CharField(max_length=20, default=None)
    reserved_category = models.CharField(max_length=20, default=None)
    physically_handicapped = models.CharField(max_length=20, default=None)

    father_name = models.CharField(max_length=30, default=None)
    father_occupation = models.CharField(max_length=50, default=None)
    father_income = models.CharField(max_length=20, default=None)
    mother_name = models.CharField(max_length=30, default=None)
    mother_occupation = models.CharField(max_length=50, default=None)
    mother_income = models.CharField(max_length=20, default=None)
    gaurdian_name = models.CharField(max_length=30, default=None)
    gaurdian_occupation = models.CharField(max_length=50, default=None)
    gaurdian_income = models.CharField(max_length=20, default=None)

    nationality = models.CharField(max_length=20, default=None)
    native_place = models.CharField(max_length=20, default=None)
    state = models.CharField(max_length=20, default=None)
    email = models.EmailField(default=None)
    phone = models.CharField(max_length=20, default=None)
    currrent_address_line1 = models.CharField(max_length=100, default=None,null=True)
    current_address_line2 = models.CharField(max_length=100, default=None)
    current_city = models.CharField(max_length=50, default=None,verbose_name="City")
    current_pincode = models.CharField(max_length=15, default=None, verbose_name="Pincode")
    current_phone = models.CharField(max_length=20, default=None, verbose_name="Phone")
    permanent_address_line1 = models.CharField(max_length=100, default=None)
    permanent_address_line2 = models.CharField(max_length=100, default=None)
    permanent_city = models.CharField(max_length=50, default=None,verbose_name="City")
    permanent_pincode = models.CharField(max_length=15, default=None,verbose_name="Pincode")
    permanent_phone = models.CharField(max_length=20, default=None,verbose_name="Phone")
    
    tc_no = models.CharField(max_length=20, default=None)
    tc_date = models.CharField(max_length=20, default=None)
    medium_of_instruction = models.CharField(max_length=20, default=None)
    reg_no = models.CharField(max_length=20, default=None, verbose_name="Registration number")
    month_and_year_of_passing = models.CharField(max_length=20, default=None)
    percentage_of_marks = models.CharField(max_length=3, default=None)
    board = models.CharField(max_length=10, default=None)
    name_of_institution = models.CharField(max_length=100, default=None)
    language = models.CharField(max_length=20, default=None)
    english = models.CharField(max_length=20, default=None)
    maths = models.CharField(max_length=20, default=None)
    physics = models.CharField(max_length=20, default=None)
    chemistry = models.CharField(max_length=20, default=None)
    biology = models.CharField(max_length=20, default=None)
    eligible_percentage = models.CharField(max_length=20, default=None)

    reg_no1 = models.CharField(max_length=20, default=None, verbose_name="Registration number")
    month_and_year_of_passing1 = models.CharField(max_length=20, default=None ,verbose_name="Month And Year of Passing")
    percentage_of_marks1 = models.CharField(max_length=3, default=None,verbose_name="Percentage of Marks")
    board1 = models.CharField(max_length=10, default=None,verbose_name="    Board")
    name_of_institution1 = models.CharField(max_length=100, default=None,verbose_name="Name of Institution")
    language1 = models.CharField(max_length=20, default=None,verbose_name="Language")
    english1 = models.CharField(max_length=20, default=None,verbose_name="English")
    maths1 = models.CharField(max_length=20, default=None,verbose_name=" Maths")
    physics1 = models.CharField(max_length=20, default=None,verbose_name="Physics")
    chemistry1 = models.CharField(max_length=20, default=None,verbose_name="Chemistry")
    biology1 = models.CharField(max_length=20, default=None,verbose_name="Biology")
    eligible_percentage1 = models.CharField(max_length=20, default=None,verbose_name="Eligible Percentage")

    has_enquired = models.BooleanField(default=False, null=True)

    def __str__(self):
        return str(self.applicant_name)



   








