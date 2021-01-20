# Desi değerleri

def desi_degeri(ws, max_row):
    for satir in range(2, max_row + 1):
        aciklama_sutun = 8
        kargoagirligi_sutun = 59
        a = str(ws.cell(satir, aciklama_sutun).value)
        str(ws.cell(satir, kargoagirligi_sutun, value=""))
        if "Desi Değeri:" in a:
            b = a.find("Desi Değeri")
            c = a[b:len(a)]
            str(ws.cell(satir, aciklama_sutun, value=a.replace(c, "")))
            str(ws.cell(satir, kargoagirligi_sutun, value=c))
    return ws
