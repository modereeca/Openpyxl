# 'Barkod' ve 'İtem No' lu kısımların açıklama sütunundan silinmesi.

"""
Barkodu: 8681689375997<br />
Item No : LOL7599<br />
"""


def barkod(ws, max_row):
    for satir in range(2, max_row+1):
        aciklama_sutun = 8
        a = str(ws.cell(satir, aciklama_sutun).value)

        if a.find("Barkodu") != -1:
            ilk_index = a.find("Barkodu")
            son_index = -1
            for test_index in range(1, 35):
                if (ilk_index + test_index) >= len(a):
                    break
                character = a[ilk_index + test_index]
                if character == ">":
                    son_index = ilk_index + test_index
                    break
            if son_index != -1:
                b = a.replace(a[ilk_index:son_index], "")
                ws.cell(satir, aciklama_sutun, value=b)

        elif a.find("BARKOD") != -1:
            ilk_index = a.find("BARKOD")
            son_index = -1
            for test_index in range(1, 35):
                if (ilk_index + test_index) >= len(a):
                    break
                character = a[ilk_index + test_index]
                if character == ">":
                    son_index = ilk_index + test_index
                    break
            if son_index != -1:
                b = a.replace(a[ilk_index:son_index], "")
                ws.cell(satir, aciklama_sutun, value=b)
    return ws
