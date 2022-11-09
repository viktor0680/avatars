from PIL import Image
from pathlib import Path
import random

num_back = 5
num_head = 6
num_mouth = 5
num_eye = 6
num_nose = 5

def get_path(a, file):
    outpath = Path.cwd()/'images'/a/file
    return outpath

# Случайно выбираем картинку
back = Image.open(get_path('/content/drive/MyDrive/images/backs', f'back{random.randint(1, num_back)}.png'))
head = Image.open(get_path('/content/drive/MyDrive/images/heads', f'head{random.randint(1, num_head)}.png'))
mouth = Image.open(get_path('/content/drive/MyDrive/images/mouths', f'mouth{random.randint(1, num_mouth)}.png'))
eye = Image.open(get_path('/content/drive/MyDrive/images/eyes', f'eye{random.randint(1, num_eye)}.png'))
nose = Image.open(get_path('/content/drive/MyDrive/images/noses', f'nose{random.randint(1, num_nose)}.png'))

# Генерируем изображение
back.paste(head.convert('RGB'), (0,0), head)
back.paste(mouth.convert('RGB'), (0,0), mouth)
back.paste(eye.convert('RGB'), (0,0), eye)
back.paste(nose.convert('RGB'), (0,0), nose)

#Сохраняем в папку
back.save(get_path('images' , '/content/drive/MyDrive/images/images/result.png'))
