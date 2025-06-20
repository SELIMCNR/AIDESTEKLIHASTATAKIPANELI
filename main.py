from tkinter import Tk
from app.gui import HospitalPanel
from app.controller import Controller

def main():
    # Controller (AI model ile bağlantı)
    controller = Controller()

    # GUI başlat
    root = Tk()
    app = HospitalPanel(root, controller)
    root.mainloop()

if __name__ == "__main__":
    main()