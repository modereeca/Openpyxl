# Yaş Grubu - Varyasyon ilişkisi

def varyasyon(ws, max_row):
    for satir in range(2, max_row+1):
        aciklama_sutun = 8
        varyasyon_sutun = 4
        ws.cell(satir, varyasyon_sutun, value="")
        a = str(ws.cell(satir, aciklama_sutun).value)
        for yas in range(3, 14):
            if a.find(yas_grubu_olusturucu(yas)) != -1:
                ws.cell(satir, varyasyon_sutun, value=varyasyon_olustucu(yas))
                break
    return ws


def yas_grubu_olusturucu(yas):
    return "Yaş Grubu : " + str(yas) + "+ Yaş"


def varyasyon_olustucu(yas):
    if 2 < yas < 6:
        return "3-5, 6-9, 10-12, 13+"
    elif yas < 10:
        return "6-9, 10-12, 13+"
    elif yas < 13:
        return "10-12, 13+"
    elif yas == 13:
        return "13+"
    else:
        raise "Yaş grubu 3 ile 13 arasında olmalıdır!. Sizin girdiğiniz değer: " + str(yas)
