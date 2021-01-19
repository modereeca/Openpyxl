# Bu "DİĞER" kısmı

def breadcrumb(ws, max_row):
    for satir in range(2, max_row+1):
        breadcrumb_sutun = 17
        a = ws.cell(satir, breadcrumb_sutun).value
        if a is not None:
            b = str(a).replace("Diğer>", "")
            ws.cell(satir, breadcrumb_sutun, value=b)
    return ws
