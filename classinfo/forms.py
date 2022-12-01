from django import forms

from classinfo.models import Style, Learner, Registration, Course, Availability


class StyleForm(forms.ModelForm):
    class Meta:
        model = Style
        fields = '__all__'

    def clean_style_name(self):
        return self.cleaned_data['style_name'].strip()


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def clean_course_name(self):
        return self.cleaned_data['course_name'].strip()

    def clean_course_intro(self):
        return self.cleaned_data['course_intro'].strip()


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = '__all__'


class LearnerForm(forms.ModelForm):
    class Meta:
        model = Learner
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            result = self.cleaned_data['disambiguator']
        else:
            result = self.cleaned_data['disambiguator'].strip()
        return result


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'