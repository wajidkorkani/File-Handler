from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from .models import File
# Create your views here.
def Home(request):
    files = File.objects.all().order_by('-time_stamp')
    template = 'index.html'
    context = {
        'files':files,
    }
    return render(request, template, context)

class Upload_Document(CreateView):
    model = File
    fields = '__all__'
    template_name = 'Upload_Document.html'
    success_url = '/'

