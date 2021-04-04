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

    def __str__(self):
        return str(self.unique_id)

class mci(models.Model):
    title = models.CharField(max_length=250, default=None)
    document_pdf = models.FileField(upload_to='mci', blank=False, default=None)

    def __str__(self):
        return str(self.title)


class Subscriber(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email)