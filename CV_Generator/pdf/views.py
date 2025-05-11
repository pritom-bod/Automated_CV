
from django.shortcuts import render
from .models import CvProfile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
from django.shortcuts import render, get_object_or_404
# Create your views here.


def accept(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        summary = request.POST.get('summary')
        degree = request.POST.get('degree')
        school = request.POST.get('school')
        university = request.POST.get('university')
        previous_work = request.POST.get('previous_work')
        skills = request.POST.get('skills')
    
        profile = CvProfile(name=name, email=email, phone=phone, summary=summary, degree=degree, school=school, university=university, previous_work=previous_work, skills=skills)
        profile.save()
        return render(request, 'pdf/accept.html', {'user_profile': profile})
    return render(request, 'pdf/accept.html')

def resume_view(request, id):
    profile = get_object_or_404(CvProfile, pk=id)
    return render(request, 'pdf/resume.html', {'user_profile': profile})

def resume(request, id):
    user_profile = CvProfile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({"user_profile":user_profile}) 
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
    }

    # config define
    config = pdfkit.configuration(wkhtmltopdf=r'C:\wkhtmltox\bin\wkhtmltopdf.exe')

    #config parameter 
    pdf = pdfkit.from_string(html, False, options=options, configuration=config)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    return response

def CvList(request):
    profile = CvProfile.objects.all()
    return render(request, 'pdf/list.html', {
        'profile':profile,
    })