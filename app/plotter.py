import matplotlib.pyplot as plt

def plot_patient_data(data_dict):
    # Veriyi sütun grafiği olarak çizer
    categories = list(data_dict.keys())
    values = [float(v) for v in data_dict.values() if v.strip() != ""]

    plt.figure(figsize=(8, 5))
    plt.style.use("ggplot")
    plt.bar(categories[:len(values)], values, color="teal")
    plt.title("Girilen Hasta Verileri")
    plt.xlabel("Özellikler")
    plt.ylabel("Değerler")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()