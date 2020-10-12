from django.views import View
from django.shortcuts import render, redirect
from .models import Resume
from django.forms import ModelForm
from django.http import HttpResponseForbidden
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


# class MainPage(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'resume/index.html')


class Resumes(View):
    def get(self, request, *args, **kwargs):
        resumes_list = Resume.objects.all()
        return render(request, 'resume/resumes.html', {'resumes': resumes_list})


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ['description']
    # description = forms.CharField(max_length=100)


class CreateResume(View):
    def get(self, request, *args, **kwargs):
        form = ResumeForm()
        return render(request, 'resume/new.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = ResumeForm(request.POST)
            if form.is_valid():
                resume = form.save(commit=False)
                resume.author = request.user
                resume.save()
                # Resume.objects.create(description=request.POST['description'])
                return redirect('/home')
            else:
                return redirect(HttpResponseForbidden)
