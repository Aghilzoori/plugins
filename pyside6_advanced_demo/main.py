"""نمونهٔ پیشرفته: کنترل مستقیم بر چیدمان و ظاهر با PySide6."""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
)


def create_widget(parent):
    panel = QWidget(parent)
    panel.setStyleSheet("""
        QWidget { background: #171923; color: #F2F0F7; }
        QLineEdit { padding: 8px; border: 1px solid #6D5D82; border-radius: 6px; }
        QPushButton { padding: 8px 14px; background: #39314D; border-radius: 6px; }
        QPushButton:hover { background: #514568; }
    """)

    layout = QVBoxLayout(panel)
    layout.setContentsMargins(18, 18, 18, 18)  # حاشیهٔ داخلی پنل
    layout.setSpacing(12)                      # فاصلهٔ بین اجزا

    title = QLabel("ماشین‌حساب جمع")
    title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    title.setStyleSheet("font-size: 18px; font-weight: bold;")

    first = QLineEdit()
    first.setPlaceholderText("عدد اول را وارد کنید")
    first.setMinimumHeight(36)

    second = QLineEdit()
    second.setPlaceholderText("عدد دوم را وارد کنید")
    second.setMinimumHeight(36)

    result = QLabel("حاصل جمع اینجا نمایش داده می‌شود")
    result.setAlignment(Qt.AlignmentFlag.AlignCenter)
    result.setMinimumHeight(32)

    button = QPushButton("محاسبهٔ جمع")
    button.clicked.connect(lambda: show_sum(first, second, result))

    layout.addWidget(title)
    layout.addWidget(first)
    layout.addWidget(second)
    layout.addWidget(button)
    layout.addWidget(result)
    layout.addStretch(1)  # اجزا به بالای پنل نزدیک می‌مانند

    # برای چیدمان‌های دیگر می‌توان QHBoxLayout یا QGridLayout را جایگزین کرد.
    return panel


def show_sum(first, second, result):
    try:
        number1 = float(first.text())
        number2 = float(second.text())
        result.setText(f"حاصل جمع: {number1 + number2:g}")
    except ValueError:
        result.setText("لطفاً دو عدد معتبر وارد کنید")
