
# amblyopia-helper-api

#### จัดทำโดย
- นายเพชรายุทธ พลคุมพล
- นายนนทกร จิตรชิรานันท์
โรงเรียนขอนแก่นวิทยายน

ใช้ PyTesseract สำหรับการอ่านตัวอักษร และ Keras สำหรับรัน Model MobileNet ในการจำแนกรูปภาพ
ใช้ Django และ Django REST Framework สำหรับระบบ API

# สามารถทดลองข้อมูลได้ด้วยวิธีการดังนี้
https://amblyopia-helper.herokuapp.com

`POST /mbn/` สำหรับ request การทำนายจาก mobilenet

`POST /ocr/` สำหรับ request การทำนายจาก tesseract-ocr
