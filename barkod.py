#'Barkod' ve 'İtem No' lu kısımların açıklama sütunundan silinmesi.

def barkod(ws, max_row):
    for satir in range(2, max_row+1):
        aciklama_sutun = 8
        a = str(ws.cell(satir, aciklama_sutun).value)
        if a.find("Barkodu"):
            ilk_index = a.find("Barkodu")
            son_index = a.find("Kutu Ö")
            if son_index:
                b = a.replace(a[ilk_index:son_index], "")
                ws.cell(satir, aciklama_sutun, value=b)

        elif a.find("BARKOD"):
            ilk_index = a.find("BARKOD")
            son_index = a.find("KUTU ")
            if son_index:
                b = a.replace(a[ilk_index:son_index], "")
                ws.cell(satir, aciklama_sutun, value=b)
