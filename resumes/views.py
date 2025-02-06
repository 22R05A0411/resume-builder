from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Resume
from django.template.loader import render_to_string
import pdfkit  # Make sure to install pdfkit and wkhtmltopdf

def generate_pdf(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    
    # Load the selected template
    template_map = {
        "classic": "resumes/resume_template_classic.html",
        "modern": "resumes/resume_template_modern.html",
        "elegant": "resumes/resume_template_elegant.html",
    }
    selected_template = template_map.get(resume.template_choice, "resumes/resume_template_classic.html")

    html = render_to_string(selected_template, {'resume': resume})
    pdf = pdfkit.from_string(html, False)

    response = HttpResponse(pdf, content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    return response
