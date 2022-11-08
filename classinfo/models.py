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


class Date(models.Model):
    date_id = models.AutoField(primary_key=True)
    year = models.ForeignKey(Year, related_name='dates', on_delete=models.PROTECT)
    month = models.ForeignKey(Month, related_name='dates', on_delete=models.PROTECT)
    day = models.ForeignKey(Day, related_name='dates', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.month.month} / {self.day.day} / {self.year.year}'

    def get_absolute_url(self):
        return reverse('classinfo_date_detail_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_update_url(self):
        return reverse('classinfo_date_update_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    def get_delete_url(self):
        return reverse('classinfo_date_delete_urlpattern',
                        kwargs={'pk': self.pk}
                        )

    class Meta:
        ordering = ['year__year', 'month__month', 'day__day']
        constraints = [
            UniqueConstraint(fields=['year', 'month', 'day'], name='unique_date')
        ]


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    course_intro = models.TextField(max_length=5000)

    def __str__(self):
        return f'{self.course_name}'

    class Meta:
        ordering = ['course_name']
        constraints = [
            UniqueConstraint(fields=['course_name'], name='unique_course')
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
                             name='unique_student')
        ]


class Style(models.Model):
    style_id = models.AutoField(primary_key=True)
    style_name = models.CharField(max_length=20)
    date = models.ForeignKey(Date, related_name='styles', on_delete=models.PROTECT)
    course = models.ForeignKey(Course, related_name='styles', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.course.course_name} - {self.style_name} ({self.date.__str__()})'

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
        ordering = ['course', 'style_name', 'date']
        constraints = [
            UniqueConstraint(fields=['course', 'style_name', 'date'],
                             name='unique_section')
        ]


class Registration(models.Model):
    registration_id = models.AutoField(primary_key=True)
    learner = models.ForeignKey(Learner, related_name='registrations', on_delete=models.PROTECT)
    style = models.ForeignKey(Style, related_name='registrations', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.style} / {self.learner}'

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
        ordering = ['style', 'learner']
        constraints = [
            UniqueConstraint(fields=['style', 'learner'],
                             name='unique_registration')
        ]