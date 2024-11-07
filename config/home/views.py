from django.shortcuts import render
from . import models
from django.http import FileResponse
from django.conf import settings
import os
from django.http import HttpResponse, Http404
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.



def download_pdf(request):
    # مسیر کامل فایل PDF را تعیین می‌کنیم
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'pdfs/e.pdf')

        # چک کردن وجود فایل PDF
    if os.path.exists(pdf_path):
            # ارسال فایل PDF برای دانلود
            with open(pdf_path, 'rb') as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="e.pdf"'
                return response
    else:
            raise Http404("PDF مورد نظر یافت نشد.")



def showHome(request):
    portofilos = models.PortfolioItem.objects.all().order_by('-created_at')
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # ذخیره پیام در دیتابیس
            return render(request, 'index.html', {'port' : portofilos, 'form' : form})  # پیام تایید
    else:
        form = ContactForm()


    

    return render(request, 'index.html', {'port' : portofilos, 'form' : form})