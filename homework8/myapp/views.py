import os
from django.shortcuts import render, redirect
from django.urls import reverse

from homework8.settings import BASE_DIR
from .forms import UploadForm

def upload_view(request):
    if request.method == 'GET':
        form = UploadForm()
        return render(request, 'hw_upload.html', {'form': form})

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = request.FILES.get('img')
            file_name = os.path.basename(img.name)  # 提取文件名
            file_path = os.path.join(BASE_DIR, 'upload_files', file_name)
            with open(file_path, "wb") as f:
                for chunk in img.chunks():
                    f.write(chunk)
            return redirect(reverse('homework:success', args=(file_name,)))
        else:
            return render(request, 'hw_upload.html', {'form': form})

def show_img(request, file_name):
    return render(request, 'hw_success.html', {'file_name': file_name})

