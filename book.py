import io
from lib2to3.pgen2 import token
from gtts import gTTS
from playsound import playsound
fp=io.open("book.txt",mode="r",encoding="utf-8")
book_content = fp.read()
ob = gTTS(book_content,lang='ml')
ob.save("book.mp3")
playsound("book.mp3")