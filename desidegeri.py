# Desi değerleri

def desi_degeri(ws, max_row):
    for satir in range(2, max_row + 1):
        aciklama_sutun = 8
        kargoagirligi_sutun = 59

        a = ws.cell(satir, aciklama_sutun).value

        if a is None:
            break

        a = str(a)

        if a.find("Desi Değeri") == -1:
            break

        index = a.find("Desi Değeri")
        c = a[index:len(a)]
        ws.cell(satir, aciklama_sutun, value=a.replace(c, ""))
        ws.cell(satir, kargoagirligi_sutun, value=c)
    return ws
