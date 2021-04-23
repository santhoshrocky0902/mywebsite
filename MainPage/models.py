from django.db import models

NUMBER_STATUSES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)
class Main_Event(models.Model):
    unique_id = models.PositiveIntegerField(
    choices=NUMBER_STATUSES,
    default='1',
    )
    image = models.ImageField(upload_to='main-events', blank=False, default=None)
    title = models.CharField(max_length=50, null= True, default=None)
    class Meta:
        verbose_name = 'Main Event'
        verbose_name_plural = 'Main Events'
    def __str__(self):
        return str(self.unique_id)

class mci(models.Model):
    title = models.CharField(max_length=250, default=None)
    document_pdf = models.FileField(upload_to='mci', blank=True, default=None)
    href = models.URLField(default = None,blank=True)
    class Meta:
        verbose_name = 'MCI Clause'
        verbose_name_plural = 'MCI Clause'
    def __str__(self):
        return str(self.title)

class mci_subcatagory(models.Model):
    title = models.CharField(max_length=250, default=None)
    document_pdf = models.FileField(upload_to='mci', blank=True, null=True, default=None)
    href = models.URLField(default = None,blank=True)
    MCI_name = models.ForeignKey(mci, on_delete=models.CASCADE, default=None)


    # @property
    # def doc_url(self):
    #     if self.document_pdf and hasattr(self.document_pdf, 'url'):
    #         return self.doc_url


class Subscriber(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email)