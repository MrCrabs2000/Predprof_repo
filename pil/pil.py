from PIL import Image

# Открытие изображения
img = Image.open('image.jpg')

# Сохранение изображения
img.save('new_image.png')

# Информация об изображении
print(img.size)  # (ширина, высота)
print(img.mode)  # RGB, RGBA, L (черно-белое), и т.д.
print(img.format)  # JPEG, PNG, и т.д.


from PIL import Image, ImageColor

# Создание пустого изображения
# Image.new(mode, size, color)
img1 = Image.new('RGB', (500, 300), 'white')
img2 = Image.new('RGB', (500, 300), (255, 0, 0))  # Красный
img3 = Image.new('RGBA', (500, 300), (0, 255, 0, 128))  # Полупрозрачный зеленый
img4 = Image.new('RGB', (500, 300), ImageColor.getrgb('#ff0000'))  # HEX цвет


from PIL import Image

img = Image.open('image.jpg')

# Изменение размера
resized = img.resize((300, 200))

# Пропорциональное изменение
img.thumbnail((300, 300))  # Сохраняет пропорции

# Поворот
rotated = img.rotate(45, expand=True)  # expand=True расширяет холст

# Отражение
flipped_h = img.transpose(Image.FLIP_LEFT_RIGHT)  # Горизонтально
flipped_v = img.transpose(Image.FLIP_TOP_BOTTOM)  # Вертикально

# Обрезка (crop)
cropped = img.crop(('''left, top, right, bottom'''))  # left, top, right, bottom


from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (500, 500), 'white')
draw = ImageDraw.Draw(img)

# Линия
draw.line((0, 0, 500, 500), fill='black', width=3)

# Прямоугольник
draw.rectangle((50, 50, 200, 200), fill='blue', outline='red', width=2)

# Эллипс/круг
draw.ellipse((250, 250, 400, 350), fill='green', outline='yellow')

# Многоугольник
draw.polygon([(300, 400), (350, 450), (250, 450)], fill='purple')

# Текст
font = ImageFont.truetype('arial.ttf', 36)  # Загрузка шрифта
draw.text((100, 400), "Hello World!", fill='black', font=font)

# Точка/пиксель
draw.point((250, 250), fill='red')


from PIL import Image, ImageFilter, ImageEnhance

img = Image.open('image.jpg')

# Применение фильтров
blurred = img.filter(ImageFilter.BLUR)
sharpened = img.filter(ImageFilter.SHARPEN)
contour = img.filter(ImageFilter.CONTOUR)
emboss = img.filter(ImageFilter.EMBOSS)
edge_enhance = img.filter(ImageFilter.EDGE_ENHANCE)

# Настройка яркости, контраста и т.д.
enhancer = ImageEnhance.Brightness(img)
brighter = enhancer.enhance(1.5)  # Увеличить яркость на 50%

enhancer = ImageEnhance.Contrast(img)
more_contrast = enhancer.enhance(1.5)

enhancer = ImageEnhance.Sharpness(img)
sharper = enhancer.enhance(2.0)


from PIL import Image

img = Image.open('image.jpg')

# Получение цвета пикселя
pixel = img.getpixel((100, 100))  # Возвращает кортеж (R, G, B)

# Изменение цвета пикселя
img.putpixel((100, 100), (255, 0, 0))  # Красный

# Конвертация в массив и обратно
pixels = list(img.getdata())
# Изменение пикселей...
img.putdata(pixels)

# Работа с отдельными каналами
r, g, b = img.split()  # Разделение на каналы
img = Image.merge('RGB', (r, g, b))  # Объединение каналов


from PIL import Image

img = Image.open('image.jpg')

# Конвертация в разные режимы
img_rgba = img.convert('RGBA')  # Добавить альфа-канал
img_gray = img.convert('L')     # Черно-белое
img_bw = img.convert('1')       # Черно-белое (1 бит на пиксель)
img_palette = img.convert('P')  # Палитровое изображение


from PIL import Image

background = Image.open('background.jpg')
overlay = Image.open('overlay.png')

# Вставка одного изображения в другое
background.paste(overlay, (100, 100), overlay)  # С прозрачностью

# Создание коллажа
img1 = Image.open('img1.jpg')
img2 = Image.open('img2.jpg')

# Горизонтальное объединение
total_width = img1.width + img2.width
new_img = Image.new('RGB', (total_width, max(img1.height, img2.height)))
new_img.paste(img1, (0, 0))
new_img.paste(img2, (img1.width, 0))

from PIL import Image, ImageDraw
from pathlib import Path


def create_map_with_points(points_data, filename='map.png'):
    # Создание изображения
    image = Image.new('RGB', (256, 256), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Рисование точек
    for point in points_data:
        x, y = point['x'], point['y']
        radius = 32 if point['type'] == 'listener' else 64
        color = 'red' if point['active'] else 'gray'

        # Рисование круга
        draw.ellipse(
            (x - radius, y - radius, x + radius, y + radius),
            fill=color,
            outline='black',
            width=2
        )

    # Сохранение
    image.save(filename)
    return filename