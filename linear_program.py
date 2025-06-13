import streamlit as st
from scipy.optimize import linprog
import matplotlib.pyplot as plt
import numpy as np

st.title("Aplikasi Linear Programming")

st.sidebar.title("📊 Input Parameter")

# Fungsi Objektif
c1 = st.sidebar.number_input("Koefisien x (Produk A)", value=-30.0)
c2 = st.sidebar.number_input("Koefisien y (Produk B)", value=-40.0)

# Kendala 1
a1_1 = st.sidebar.number_input("Mesin: x koefisien", value=2.0)
a1_2 = st.sidebar.number_input("Mesin: y koefisien", value=4.0)
b1 = st.sidebar.number_input("Mesin: batas maksimum", value=100.0)

# Kendala 2
a2_1 = st.sidebar.number_input("Kerja: x koefisien", value=3.0)
a2_2 = st.sidebar.number_input("Kerja: y koefisien", value=2.0)
b2 = st.sidebar.number_input("Kerja: batas maksimum", value=90.0)

# Fungsi Objektif
c = [c1, c2]  # Negatif karena linprog meminimalkan

# Matriks kendala dan batas
A = [[a1_1, a1_2],
     [a2_1, a2_2]]
b = [b1, b2]

# Syarat non-negatif
x_bounds = (0, None)
y_bounds = (0, None)

# Optimasi
res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

if res.success:
    st.success("Optimasi berhasil!")
    st.write(f"Jumlah produk A (x): {res.x[0]:.2f}")
    st.write(f"Jumlah produk B (y): {res.x[1]:.2f}")
    st.write(f"Keuntungan maksimum: Rp {-res.fun:,.2f}")
else:
    st.error("Optimasi gagal.")

# Visualisasi grafik
st.subheader("Visualisasi Daerah Feasible (2D)")

x = np.linspace(0, 100, 500)
y1 = (b1 - a1_1 * x) / a1_2
y2 = (b2 - a2_1 * x) / a2_2

plt.figure(figsize=(8, 5))
plt.plot(x, y1, label="Mesin")
plt.plot(x, y2, label="Kerja")
plt.xlim(0, max(x))
plt.ylim(0, max(max(y1), max(y2)))
plt.fill_between(x, 0, np.minimum(y1, y2), where=(np.minimum(y1, y2) > 0), alpha=0.3)
