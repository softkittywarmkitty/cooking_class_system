from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from classinfo.forms import StyleForm, LearnerForm, RegistrationForm, CourseForm, AvailabilityForm
from classinfo.utils import PageLinksMixin
from classinfo.models import (
    Style,
    Learner,
    Registration,
    Course,
    Availability,
)


class StyleList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Style
    permission_required = 'classinfo.view_style'


class StyleDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Style
    permission_required = 'classinfo.view_style'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        style = self.get_object()
        course_list = style.registrations.all()
        context['course_list'] = course_list
        return context


class StyleCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = StyleForm
    model = Style
    permission_required = 'classinfo.add_style'


class StyleUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = StyleForm
    model = Style
    template_name = 'classinfo/style_form_update.html'
    permission_required = 'classinfo.change_style'


class StyleDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Style
    success_url = reverse_lazy('classinfo_style_list_urlpattern')
    permission_required = 'classinfo.delete_style'

    def get(self, request, pk):
        style = get_object_or_404(Style, pk=pk)
        courses = style.courses.all()
        if courses.count() > 0:
            return render(
                request,
                'classinfo/style_refuse_delete.html',
                {'style': style,
                 'courses': courses,
                 }
            )
        else:
            return render(
                request,
                'classinfo/style_confirm_delete.html',
                {'style': style}
            )


class CourseList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Course
    permission_required = 'classinfo.view_course'


class CourseDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Course
    permission_required = 'classinfo.view_course'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        course = self.get_object()
        style = course.style
        availability_list = course.availabilities.all()
        context['style'] = style
        context['availability_list'] = availability_list
        return context


class CourseCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CourseForm
    model = Course
    permission_required = 'classinfo.add_course'


class CourseUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = CourseForm
    model = Course
    template_name = 'classinfo/course_form_update.html'
    permission_required = 'classinfo.change_course'


class CourseDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('classinfo_course_list_urlpattern')
    permission_required = 'classinfo.delete_course'

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        availabilities = course.availabilities.all()
        if availabilities.count() > 0:
            return render(
                request,
                'classinfo/course_refuse_delete.html',
                {'course': course,
                 'availabilities': availabilities,
                 }
            )
        else:
            return render(
                request,
                'classinfo/course_confirm_delete.html',
                {'course': course}
            )


class AvailabilityList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Availability
    permission_required = 'classinfo.view_availability'


class AvailabilityDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Availability
    permission_required = 'classinfo.view_availability'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        availability = self.get_object()
        course = availability.course
        year = availability.year
        month = availability.month
        day = availability.day
        registration_list = availability.registrations.all()
        context['course'] = course
        context['year'] = year
        context['month'] = month
        context['day'] = day
        context['registration_list'] = registration_list
        return context


class AvailabilityCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = AvailabilityForm
    model = Availability
    permission_required = 'classinfo.add_availability'


class AvailabilityUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = AvailabilityForm
    model = Availability
    template_name = 'classinfo/availability_form_update.html'
    permission_required = 'classinfo.change_availability'


class AvailabilityDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Availability
    success_url = reverse_lazy('classinfo_availability_list_urlpattern')
    permission_required = 'classinfo.delete_availability'

    def get(self, request, pk):
        availability = get_object_or_404(Availability,pk=pk)
        registrations = availability.registrations.all()
        if registrations.count() > 0:
            return render(
                request,
                'classinfo/availability_refuse_delete.html',
                {'availability': availability,
                 'registrations': registrations,
                 }
            )
        else:
            return render(
                request,
                'classinfo/availability_confirm_delete.html',
                {'availability': availability}
            )


class LearnerList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Learner
    permission_required = 'classinfo.view_learner'


class LearnerDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Learner
    permission_required = 'classinfo.view_learner'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        learner = self.get_object()
        registration_list = learner.registrations.all()
        context['registration_list'] = registration_list
        return context


class LearnerCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = LearnerForm
    model = Learner
    permission_required = 'classinfo.add_learner'


class LearnerUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = LearnerForm
    model = Learner
    template_name = 'classinfo/learner_form_update.html'
    permission_required = 'classinfo.change_learner'


class LearnerDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Learner
    success_url = reverse_lazy('classinfo_learner_list_urlpattern')
    permission_required = 'classinfo.delete_learner'

    def get(self, request, pk):
        learner = get_object_or_404(Learner, pk=pk)
        registrations = learner.registrations.all()
        if registrations.count() > 0:
            return render(
                request,
                'classinfo/learner_refuse_delete.html',
                {'learner': learner,
                 'registrations': registrations,
                 }
            )
        else:
            return render(
                request,
                'classinfo/learner_confirm_delete.html',
                {'learner': learner}
            )


class RegistrationList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Registration
    permission_required = 'classinfo.view_registration'


class RegistrationDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Registration
    permission_required = 'classinfo.view_registration'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        registration = self.get_object()
        learner = registration.learner
        availability = registration.availability
        context['learner'] = learner
        context['availability'] = availability
        return context


class RegistrationCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = RegistrationForm
    model = Registration
    permission_required = 'classinfo.add_registration'


class RegistrationUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = RegistrationForm
    model = Registration
    template_name = 'classinfo/registration_form_update.html'
    permission_required = 'classinfo.change_registration'


class RegistrationDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Registration
    success_url = reverse_lazy('classinfo_registration_list_urlpattern')
    permission_required = 'classinfo.delete_registration'