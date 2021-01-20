from os import path
from excel import wb, ws, max_row
from varyasyon import varyasyon
from breadcrumb import breadcrumb
from barkod import barkod

ws = varyasyon(ws, max_row)
print("Varyasyon tanımlandı")
ws = breadcrumb(ws, max_row)
print("Diğer> işareti değiştirildi")
ws = barkod(ws, max_row)
print("Barkod ve Item No satırları silindi")

print("Kaydediliyor...")
wb.save(path.join(path.curdir, 'output.xlsx'))
print("Kayıt tamamlandı.")
