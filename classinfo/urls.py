from django.contrib import admin
from django.urls import path
from classinfo.views import (
    StyleList,
    CourseList,
    AvailabilityList,
    LearnerList,
    RegistrationList,
    StyleDetail,
    AvailabilityDetail,
    CourseDetail,
    LearnerDetail,
    RegistrationDetail,
    StyleCreate,
    CourseCreate,
    AvailabilityCreate,
    LearnerCreate,
    RegistrationCreate,
    StyleUpdate,
    CourseUpdate,
    AvailabilityUpdate,
    RegistrationUpdate,
    LearnerUpdate,
    RegistrationDelete,
    StyleDelete,
    CourseDelete,
    AvailabilityDelete,
    LearnerDelete,
)


urlpatterns = [
    path('style/',
         StyleList.as_view(),
         name='classinfo_style_list_urlpattern'),

    path('section/<int:pk>/',
         StyleDetail.as_view(),
         name='classinfo_style_detail_urlpattern'),

    path('section/create/',
         StyleCreate.as_view(),
         name='classinfo_style_create_urlpattern'),

    path('section/<int:pk>/update/',
         StyleUpdate.as_view(),
         name='classinfo_style_update_urlpattern'),

    path('section/<int:pk>/delete/',
         StyleDelete.as_view(),
         name='classinfo_style_delete_urlpattern'),

    path('course/',
         CourseList.as_view(),
         name='classinfo_course_list_urlpattern'),

    path('course/<int:pk>/',
         CourseDetail.as_view(),
         name='classinfo_course_detail_urlpattern'),

    path('course/create/',
         CourseCreate.as_view(),
         name='classinfo_course_create_urlpattern'),

    path('course/<int:pk>/update/',
         CourseUpdate.as_view(),
         name='classinfo_course_update_urlpattern'),

    path('course/<int:pk>/delete/',
         CourseDelete.as_view(),
         name='classinfo_course_delete_urlpattern'),

    path('availability/',
         AvailabilityList.as_view(),
         name='classinfo_availability_list_urlpattern'),

    path('availability/<int:pk>/',
         AvailabilityDetail.as_view(),
         name='classinfo_availability_detail_urlpattern'),

    path('availability/create/',
         AvailabilityCreate.as_view(),
         name='classinfo_availability_create_urlpattern'),

    path('availability/<int:pk>/update/',
         AvailabilityUpdate.as_view(),
         name='classinfo_availability_update_urlpattern'),

    path('availability/<int:pk>/delete/',
         AvailabilityDelete.as_view(),
         name='classinfo_availability_delete_urlpattern'),

    path('learner/',
         LearnerList.as_view(),
         name='classinfo_learner_list_urlpattern'),

    path('learner/<int:pk>/',
         LearnerDetail.as_view(),
         name='classinfo_learner_detail_urlpattern'),

    path('learner/create/',
         LearnerCreate.as_view(),
         name='classinfo_learner_create_urlpattern'),

    path('learner/<int:pk>/update/',
         LearnerUpdate.as_view(),
         name='classinfo_learner_update_urlpattern'),

    path('learner/<int:pk>/delete/',
         LearnerDelete.as_view(),
         name='classinfo_learner_delete_urlpattern'),

    path('registration/',
         RegistrationList.as_view(),
         name='classinfo_registration_list_urlpattern'),

    path('registration/<int:pk>/',
         RegistrationDetail.as_view(),
         name='classinfo_registration_detail_urlpattern'),

    path('registration/create/',
         RegistrationCreate.as_view(),
         name='classinfo_registration_create_urlpattern'),

    path('registration/<int:pk>/update/',
         RegistrationUpdate.as_view(),
         name='classinfo_registration_update_urlpattern'),

    path('registration/<int:pk>/delete/',
         RegistrationDelete.as_view(),
         name='classinfo_registration_delete_urlpattern'),
]
