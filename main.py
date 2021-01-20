from os import path
from excel import wb, ws, max_row
from varyasyon import varyasyon
from breadcrumb import breadcrumb
from barkod import barkod
from desidegeri import desi_degeri

# ws = varyasyon(ws, max_row)
print("Varyasyon tanımlandı")
# ws = breadcrumb(ws, max_row)
print("Diğer> işareti değiştirildi")
# ws = barkod(ws, max_row)
print("Barkod ve Item No satırları silindi")
ws = desi_degeri(ws, max_row)
print("desi değeri bulundu")

print("Kaydediliyor...")
wb.save(path.join(path.curdir, 'output.xlsx'))
print("Kayıt tamamlandı.")
