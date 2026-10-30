"""نمونهٔ کوتاه: آلیس پنل و چیدمان را خودکار می‌سازد."""

def create_ui(ui):
    first = ui.input("عدد اول را وارد کنید")
    second = ui.input("عدد دوم را وارد کنید")
    result = ui.label("حاصل جمع اینجا نمایش داده می‌شود")

    def calculate():
        try:
            result.setText(f"حاصل جمع: {float(first.text()) + float(second.text()):g}")
        except ValueError:
            result.setText("لطفاً دو عدد معتبر وارد کنید")

    ui.button("محاسبهٔ جمع", calculate)
