from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User
from django.urls import reverse


class Year(models.Model):
    year_id = models.AutoField(primary_key=True)
    year = models.IntegerField(unique=True)

    def __str__(self):
        return f'{self.year}'

    class Meta:
        ordering = ['year']


class Month(models.Model):
    month_id = models.AutoField(primary_key=True)
    month = models.IntegerField(unique=True)

    def __str__(self):
        return f'{self.month}'

    class Meta:
        ordering = ['month']


class Day(models.Model):
    day_id = models.AutoField(primary_key=True)
    day = models.IntegerField(unique=True)

    def __str__(self):
        return f'{self.day}'

    class Meta:
        ordering = ['day']


class Style(models.Model):
    style_id = models.AutoField(primary_key=True)
    style_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.style_name}'

    def get_absolute_url(self):
        return reverse('classinfo_style_detail_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_update_url(self):
        return reverse('classinfo_style_update_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_delete_url(self):
        return reverse('classinfo_style_delete_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    class Meta:
        ordering = ['style_name']
        constraints = [
            UniqueConstraint(fields=['style_name'],
                             name='unique_style')
        ]


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    course_intro = models.TextField(max_length=5000)
    style = models.ForeignKey(Style, related_name='courses', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.style} - {self.course_name}'

    class Meta:
        ordering = ['style', 'course_name']
        constraints = [
            UniqueConstraint(fields=['style', 'course_name'],
                             name='unique_course')
        ]

    def get_absolute_url(self):
        return reverse('classinfo_course_detail_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_update_url(self):
        return reverse('classinfo_course_update_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_delete_url(self):
        return reverse('classinfo_course_delete_urlpattern',
                        kwargs={'pk': self.pk}
                        )


class Learner(models.Model):
    learner_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    disambiguator = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        result = ''
        if self.disambiguator == '':
            result = f'{self.last_name}, {self.first_name}'
        else:
            result = f'{self.last_name}, {self.first_name}, {self.disambiguator}'
        return result

    def get_absolute_url(self):
        return reverse('classinfo_learner_detail_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_update_url(self):
        return reverse('classinfo_learner_update_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_delete_url(self):
        return reverse('classinfo_learner_delete_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    class Meta:
        ordering = ['last_name', 'first_name', 'disambiguator']
        constraints = [
            UniqueConstraint(fields=['last_name', 'first_name', 'disambiguator'],
                             name='unique_learner')
        ]


class Availability(models.Model):
    availability_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, related_name='availabilities', on_delete=models.PROTECT)
    year = models.ForeignKey(Year, related_name='dates', on_delete=models.PROTECT)
    month = models.ForeignKey(Month, related_name='dates', on_delete=models.PROTECT)
    day = models.ForeignKey(Day, related_name='dates', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.course} - {self.month.month}/{self.day.day}/{self.year.year}'

    def get_absolute_url(self):
        return reverse('classinfo_availability_detail_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_update_url(self):
        return reverse('classinfo_availability_update_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_delete_url(self):
        return reverse('classinfo_availability_delete_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    class Meta:
        ordering = ['course', 'year', 'month', 'day']
        constraints = [
            UniqueConstraint(fields=['course', 'year', 'month', 'day'],
                             name='unique_availability')
        ]


class Registration(models.Model):
    registration_id = models.AutoField(primary_key=True)
    learner = models.ForeignKey(Learner, related_name='registrations', on_delete=models.PROTECT)
    availability = models.ForeignKey(Availability, related_name='registrations', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.availability} - {self.learner}'

    def get_absolute_url(self):
        return reverse('classinfo_registration_detail_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_update_url(self):
        return reverse('classinfo_registration_update_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_delete_url(self):
        return reverse('classinfo_registration_delete_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    class Meta:
        ordering = ['availability', 'learner']
        constraints = [
            UniqueConstraint(fields=['availability', 'learner'],
                             name='unique_registration')
        ]