#Interfaz XD
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel,
    QLineEdit, QPushButton, QVBoxLayout, QFormLayout,
    QFrame, QSizePolicy
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Turismo")
        self.setFixedSize(420, 480)
        self._centrar()

        central = QWidget()
        self.setCentralWidget(central)

        # Layout principal
        layout = QVBoxLayout(central)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(12)
        layout.addStretch(1)

        # Título
        titulo = QLabel("✈️ Sistema de Turismo")
        titulo.setFont(QFont("Sans", 20, QFont.Weight.Bold))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(titulo)

        subtitulo = QLabel("Inicia sesión para continuar")
        subtitulo.setFont(QFont("Sans", 10))
        subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitulo.setStyleSheet("color: #888;")
        layout.addWidget(subtitulo)

        layout.addSpacing(20)

        # Línea separadora
        linea = QFrame()
        linea.setFrameShape(QFrame.Shape.HLine)
        linea.setStyleSheet("color: #444;")
        layout.addWidget(linea)

        # Formulario
        form = QFormLayout()
        form.setSpacing(14)

        self.txt_usuario = QLineEdit()
        self.txt_usuario.setPlaceholderText("Usuario o correo")
        self.txt_usuario.setMinimumHeight(38)

        self.txt_password = QLineEdit()
        self.txt_password.setPlaceholderText("Contraseña")
        self.txt_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.txt_password.setMinimumHeight(38)

        form.addRow("Usuario:", self.txt_usuario)
        form.addRow("Contraseña:", self.txt_password)
        layout.addLayout(form)

        layout.addSpacing(10)

        # Botón de login
        self.btn_login = QPushButton("Ingresar")
        self.btn_login.setMinimumHeight(42)
        self.btn_login.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_login.clicked.connect(self._iniciar_sesion)
        layout.addWidget(self.btn_login)

        # Botón cancelar
        self.btn_cancelar = QPushButton("Cancelar")
        self.btn_cancelar.setMinimumHeight(36)
        self.btn_cancelar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_cancelar.clicked.connect(self.close)
        layout.addWidget(self.btn_cancelar)

        layout.addStretch(1)

        # Enter → login
        self.txt_password.returnPressed.connect(self.btn_login.click)

        # Estilos
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e2e;
            }
            QLabel {
                color: #cdd6f4;
                font-size: 13px;
            }
            QLineEdit {
                background-color: #313244;
                border: 1px solid #45475a;
                border-radius: 8px;
                padding: 8px 12px;
                color: #cdd6f4;
                font-size: 13px;
            }
            QLineEdit:focus {
                border: 1px solid #89b4fa;
            }
            QPushButton#btn_login, QPushButton {
                background-color: #89b4fa;
                color: #1e1e2e;
                border: none;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #74c7ec;
            }
            QPushButton:pressed {
                background-color: #5aa8e0;
            }
            QFrame {
                max-height: 1px;
            }
        """)
        self.btn_login.setObjectName("btn_login")
        self.btn_cancelar.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #6c7086;
                border: 1px solid #45475a;
                border-radius: 8px;
                font-size: 12px;
            }
            QPushButton:hover {
                color: #cdd6f4;
                border-color: #89b4fa;
            }
        """)

    def _centrar(self):
        screen = QApplication.primaryScreen().availableGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

    def _iniciar_sesion(self):
        usuario = self.txt_usuario.text().strip()
        password = self.txt_password.text()

        if not usuario or not password:
            self.txt_usuario.setStyleSheet("border: 1px solid #f38ba8;" if not usuario else "")
            self.txt_password.setStyleSheet("border: 1px solid #f38ba8;" if not password else "")
            return

        # TODO: Reemplazar con tu lógica real (BD, API, etc.)
        if usuario == "admin" and password == "1234":
            print(f"Sesión iniciada: {usuario}")
            # Aquí abres tu ventana principal:
            # self.hide()
            # main = MainWindow()
            # main.show()
        else:
            self.txt_password.setStyleSheet("border: 1px solid #f38ba8;")
            self.txt_password.setPlaceholderText("Contraseña incorrecta")
            self.txt_password.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Fuerza tema consistente en cualquier DE
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())   
