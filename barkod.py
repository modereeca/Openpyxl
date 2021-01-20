# 'Barkod' ve 'İtem No' lu kısımların açıklama sütunundan silinmesi.

def barkod(ws, max_row):
    for satir in range(2, max_row + 1):
        aciklama_sutun = 8
        a = str(ws.cell(satir, aciklama_sutun).value)
        a = clear_from_text_with_br(a, "Barkodu:")
        a = clear_from_text_with_br(a, "Barkodu :")
        a = clear_from_text_with_br(a, "BARKOD")
        a = clear_from_text_with_br(a, "Item No")
        a = clear_from_text_with_br(a, "İtem No")
        a = clear_from_text_with_br(a, "ITEM NO")
        ws.cell(satir, aciklama_sutun, value=a)
    return ws


def clear_from_text_with_br(text, subtext):
    ilk_index = text.find(subtext)

    if ilk_index == -1:
        return text

    son_index = -1
    for test_index in range(ilk_index, len(text) - 7):
        br_etiketi = text[test_index:test_index + 1]
        if br_etiketi == "<":
            son_index = test_index + 1
            break

    if son_index == -1:
        return text

    new_text = text.replace(text[ilk_index:son_index], "")
    return new_text
