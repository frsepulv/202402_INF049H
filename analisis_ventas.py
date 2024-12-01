import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    data = pd.read_csv("ventas_producto.csv")
    data["Precio_total"] = data["Cantidad"] * data["Precio"]
    plt.bar(data["Producto"], data["Precio_total"])
    plt.xlabel("Producto")
    plt.ylabel("Precio total")
    plt.title("Total ventas por producto")
    # Para pruebas
    # plt.show()
    plt.savefig("grafico.png")
