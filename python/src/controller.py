from python.src.edp_ui import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = Window()
    screen.show()
    sys.exit(app.exec_())