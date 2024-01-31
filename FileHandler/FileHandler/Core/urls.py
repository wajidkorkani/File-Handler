from django.urls import path
from Core.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', Home, name='home'),
    path('upload/document', Upload_Document.as_view(), name='upload_document'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)