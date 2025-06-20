import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import Toplevel
import csv
from app.pdf_writer import save_pdf  # En üste import et
class HospitalPanel:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.pdf_data = None
        self.pdf_result = None

        master.title("🏥 AI Destekli Hasta Paneli")
        master.geometry("800x600")
        master.configure(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Hasta Giriş Paneli", font=("Segoe UI", 20), bg="#f0f0f0").pack(pady=20)

        self.inputs = {}
        fields = ["Ad Soyad", "Yaş", "Nabız", "Sistolik", "Diyastolik", "Ateş"]

        form_frame = tk.Frame(self.master, bg="#f0f0f0")
        form_frame.pack()

        for i, field in enumerate(fields):
            tk.Label(form_frame, text=field + ":", font=("Segoe UI", 12), bg="#f0f0f0").grid(row=i, column=0, sticky="e", padx=10, pady=5)
            entry = tk.Entry(form_frame, font=("Segoe UI", 12), width=20)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.inputs[field] = entry

        tk.Button(self.master, text="Tahmin Yap", command=self.handle_predict, bg="#2980b9", fg="white", font=("Segoe UI", 12), width=15).pack(pady=10)
        tk.Button(self.master, text="PDF İndir", command=self.download_pdf, bg="#8e44ad", fg="white", font=("Segoe UI", 12), width=15).pack(pady=5)
        tk.Button(self.master, text="Geçmişi Gör", command=self.show_logs, bg="#27ae60", fg="white", font=("Segoe UI", 12), width=15).pack(pady=5)

        self.result_label = tk.Label(self.master, text="", font=("Segoe UI", 14), bg="#f0f0f0", fg="darkred")
        self.result_label.pack(pady=10)

    def handle_predict(self):
        data = {key: entry.get() for key, entry in self.inputs.items()}
        try:
            tahmin = self.controller.predict_patient(data)
            self.result_label.config(text=f"AI Tahmin: {'Hasta' if tahmin == 1 else 'Sağlıklı'}")
            self.pdf_data = data
            self.pdf_result = tahmin
            for entry in self.inputs.values():
                entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Hata", str(e))

    def download_pdf(self):
        if self.pdf_data and self.pdf_result is not None:
            path = save_pdf(self.pdf_data, self.pdf_result)
            messagebox.showinfo("Başarılı", f"PDF oluşturuldu:\n{path}")
        else:
            messagebox.showwarning("Uyarı", "PDF için önce bir tahmin yapmalısın.")

    def show_logs(self):
        log_window = Toplevel(self.master)
        log_window.title("📜 Tahmin Geçmişi")
        log_window.geometry("750x400")

        tree = ttk.Treeview(log_window)
        tree["columns"] = ("Ad", "Yaş", "Nabız", "Sistolik", "Diyastolik", "Ateş", "Tahmin", "Zaman")
        tree.column("#0", width=0, stretch=tk.NO)
        for col in tree["columns"]:
            tree.heading(col, text=col)
            tree.column(col, width=90)
        tree.pack(expand=True, fill="both")

        try:
            with open("data/logs.csv", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    tree.insert("", "end", values=tuple(row[col] for col in tree["columns"]))
        except FileNotFoundError:
            messagebox.showinfo("Bilgi", "Henüz log bulunamadı.")