import base64
import binascii
from contextlib import closing
from datetime import datetime

import os

from django.db import connection
from methodism import dictfetchone

from src.settings import BASE_DIR, MEDIA_PATIENTS


def code_hashing(key: str, decode=False):
    if decode:
        return base64.b64decode(key.encode()).decode()
    else:
        return base64.b64encode(key.encode()).decode()


def generate_key(x: int):
    return binascii.hexlify(os.urandom(x)).decode()


def check_otp(otp, code):
    if otp.is_expired:
        return {
            "error": 'Bu maxsus kod eskirgan!'
        }
    if (datetime.now() - otp.created).total_seconds() > 120:
        otp.is_expired = True
        otp.save()
        return {
            "error": "Maxsus kod uchun ajratilgan vaqt tugadi"
        }

    if str(code_hashing(otp.key, decode=True)).split("$")[1] != str(code):
        otp.tries += 1
        otp.save()
        return {
            "error": "Kod Xato Boshqatdan urunib ko'ring"
        }
    otp.step = "checked"
    otp.save()
    return {
        "status": True
    }


def card_mask(number):
    return number[0:4] + ' **** **** ' + number[12:16]


def ImageGenerator(fio: str, age, dignoz, suggests: list):
    import cv2
    path = BASE_DIR.absolute().__str__() + r'\media\blank.png'
    image = cv2.imread(path)
    font = cv2.FONT_ITALIC
    fontScale = 0.6

    color = (0, 0, 0)
    thickness = 1

    symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯқҚ ",
               u"abvgdeejziyklmnoprstufhzcss_y_euaABVGDEEJZIYKLMNOPRSTUFHZCSS_Y_EUAqQ ")

    tr = {ord(a): ord(b) for a, b in zip(*symbols)}
    image = cv2.putText(image, fio.translate(tr), (250, 255), font,
                        fontScale, color, thickness, cv2.LINE_AA)

    image = cv2.putText(image, str(age), (150, 285), font,
                        fontScale, color, thickness, cv2.LINE_AA)

    image = cv2.putText(image, dignoz.translate(tr),
                        (200, 310), font, 0.6, color, thickness, cv2.LINE_AA)
    step = 360
    for i, j in enumerate(suggests, 1):
        word = f"{i}) {j}"
        image = cv2.putText(image, word.translate(tr),
                            (100, step), font, 0.5, color, thickness, cv2.LINE_AA)
        step += 20
    date = datetime.now().strftime(f"%d-%m-%Y-%M")
    filename = date + fio.replace(' ', '') + ".jpg"
    cv2.imwrite(os.path.join(MEDIA_PATIENTS, filename), image)

    return BASE_DIR.absolute().__str__() + filename


def cnts():
    sql = """
        SELECT (SELECT COUNT(*)
        FROM   dashboard_tablets) AS tb,
        (SELECT COUNT(*)
        FROM   dashboard_patients) AS patient,
        (SELECT COUNT(*)
        FROM   dashboard_doctor) AS docs, 
        
        (SELECT COUNT(*) FROM  dashboard_new) AS news
        FROM dashboard_contact
        limit 1
    """
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        res = dictfetchone(cursor)

    return res
