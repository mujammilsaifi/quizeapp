from . import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home ,name='home'),
    path('accounts/register',views.Register ,name='register'),
    path('all-category/',views.all_category,name='all_category'),
    path('category-questions/<int:cat_id>',views.allQuestion,name='allQuestion'),
    path('submit-answer/<int:cat_id>/<int:quest_id>',views.submit_answer,name='submit_answer'),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
