import pandas as pd


if __name__ == "__main__":
    data = pd.read_csv("ventas_producto.csv")
    data["Precio_total"] = data["Cantidad"] * data["Precio"]
