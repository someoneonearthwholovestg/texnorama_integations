from PIL import Image, ImageFont, ImageDraw
from PIL import ImageOps
import textwrap
import requests
from io import BytesIO


class FrameMaker:
    def __init__(self, ramka_path, font_path, font_size:int=50):
        self.ramka_path = ramka_path
        self.font_path = font_path
        self.font_size = font_size

    def make_instagram_photo(self, title, image_url):
        ramka = Image.open(self.ramka_path)

        response = requests.get(image_url)
        back = Image.open(BytesIO(response.content))
        w, h = back.size
        if w >= h:
            back = back.resize((1000 * w // h, 1000), Image.ANTIALIAS)
        else:
            back = back.resize((1000, 1000 * h // w), Image.ANTIALIAS)

        back = ImageOps.fit(back, ramka.size, Image.ANTIALIAS)
        back.putalpha(150)
        back.paste(ramka, (0, 0), ramka)

        draw = ImageDraw.Draw(back)
        font = ImageFont.truetype(self.font_path, self.font_size)

        x, y = back.size

        POST_TITLE = title.upper()

        offset = 3 * y // 4
        for line in textwrap.wrap(POST_TITLE, width=35)[:3]:
            draw.text((x //15, offset), line, (255, 255, 255), font=font)
            offset += font.getsize(line)[1] + 10

        return back

fm = FrameMaker('static/ramka.png', "fonts/segoeuib.ttf", 48)

photo = fm.make_instagram_photo("Biologlar boshqa sayyoralarda hayotni aniqlashning yangi usulini topdilar", "https://texnorama.uz/content/images/size/w300/2019/12/jIHy5FMWSY3RF8JE9Ot5gou0EQ5JtoILT5Cd.jpg")

photo.save("sample.png")