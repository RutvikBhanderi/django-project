from django.contrib import admin
from django.urls import path
from my_app.views import demo, contact_us,about_us ,add_student,edit_student, delete_student,demo1,edit_subject,add_subject,delete_subject 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', demo, name='home'),
    path('contact-us', contact_us, name='contact_us'),
    path('about-us', about_us, name='about_us'),
    path('add_student', add_student, name='add_1'),
    path('edit-student/<int:id>', edit_student, name='edit_1'),
    path('delete-student/<int:id>', delete_student, name='delete_student'),
    path('home1', demo1, name='h1'),
    path('edit-subject/<int:id>', edit_subject, name='editsub'),
    path('add-subject', add_subject, name='addsub'),
    path('delete-subject/<int:id>', delete_subject, name='deletesub')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)