import base64
from random import randint
from time import sleep
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from vkr_zinnurov.settings import BASE_DIR
from .forms import BoardForm
from .models import BoardExample
from .service.main import detect
import cv2


def index(request):
    return render(request, 'index.html')

def author(request):
    return render(request, 'aboutauthor.html')

def image_to_base64(image_file, format_img='jpg'):
    return base64.b64encode(image_file.read()).decode()


def dashboard(request):
    if request.method == 'POST':
        context = {}
        board_name = request.FILES['test_image'].name.split('.')[0]
        file = request.FILES['test_image']
        fs = FileSystemStorage()
        filename = fs.save('tmp.jpg', file)
        try:
            context['board_example'] = BoardExample.objects.get(board_model=board_name)
            imageA = cv2.imread(f'{BASE_DIR}\media\{BoardExample.objects.get(board_model=board_name).photo}')
            imageB = cv2.imread(f'{BASE_DIR}\media\{filename}')
            context['board_test'] = filename
            res = detect(imageA, imageB)
            cv2.imwrite(f'{BASE_DIR}\media\g{filename}', res)
            context['result'] = f'g{filename}'
            return render(request, 'result.html', context=context)
        except:
            context['error'] = 'Плата не найдена, попробуйте снова!'
            return render(request, 'result.html', context=context)
    return render(request, 'dashboard.html')


def examples(request):
    form = BoardForm()
    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    examples_list = BoardExample.objects.all()
    return render(request, 'example_list.html', context={'form': form, 'examples_list': examples_list})
