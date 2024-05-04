import tkinter as tk 

conversion_rates = {
    "USD": {"USD": 1, "EUR": 0.88, "GBP": 0.78, "JPY": 109.38, "INR": 75.05, "CAD": 1.26, "AFN": 0.013, "ARS": 0.010, "AUD": 0.73, "BDT": 0.012, "BRL": 0.18, "BTN": 0.014, "CNY": 0.15, "COP": 0.00028, "EGP": 0.064, "HKD": 0.13, "IDR": 0.000072, "IQD": 0.00068, "IRR": 0.000024, "NZD": 0.69, "NPR": 0.0086, "PHP": 0.020, "PKR": 0.0062, "RUB": 0.013, "LKR": 0.0050, "SAR": 0.27, "SGD": 0.74},
    "EUR": {"USD": 1.14, "EUR": 1, "GBP": 0.88, "JPY": 124.10, "INR": 85.72, "CAD": 1.44, "AFN": 0.015, "ARS": 0.011, "AUD": 0.64, "BDT": 0.011, "BRL": 0.15, "BTN": 0.012, "CNY": 0.13, "COP": 0.00025, "EGP": 0.057, "HKD": 0.12, "IDR": 0.000065, "IQD": 0.00061, "IRR": 0.000022, "NZD": 0.60, "NPR": 0.0075, "PHP": 0.017, "PKR": 0.0054, "RUB": 0.012, "LKR": 0.0047, "SAR": 0.25, "SGD": 0.68},
    "GBP": {"USD": 1.28, "EUR": 1.13, "GBP": 1, "JPY": 141.05, "INR": 97.23, "CAD": 1.63, "AFN": 0.017, "ARS": 0.013, "AUD": 0.77, "BDT": 0.014, "BRL": 0.20, "BTN": 0.016, "CNY": 0.17, "COP": 0.00032, "EGP": 0.073, "HKD": 0.15, "IDR": 0.000078, "IQD": 0.00073, "IRR": 0.000027, "NZD": 0.82, "NPR": 0.010, "PHP": 0.023, "PKR": 0.0071, "RUB": 0.016, "LKR": 0.0063, "SAR": 0.33, "SGD": 0.90},
    "JPY": {"USD": 0.0091, "EUR": 0.0081, "GBP": 0.0071, "JPY": 1, "INR": 0.69, "CAD": 0.0079, "AFN": 0.000082, "ARS": 0.000063, "AUD": 0.058, "BDT": 0.000054, "BRL": 0.00076, "BTN": 0.000062, "CNY": 0.0063, "COP": 0.0000012, "EGP": 0.00027, "HKD": 0.0055, "IDR": 0.00000030, "IQD": 0.0000028, "IRR": 0.00000010, "NZD": 0.0074, "NPR": 0.000092, "PHP": 0.00021, "PKR": 0.000065, "RUB": 0.00014, "LKR": 0.000054, "SAR": 0.0029, "SGD": 0.0079},
    "INR": {"USD": 0.013, "EUR": 0.012, "GBP": 0.010, "JPY": 1.45, "INR": 1, "CAD": 0.017, "AFN": 0.00018, "ARS": 0.00014, "AUD": 0.0082, "BDT": 0.00013, "BRL": 0.0018, "BTN": 0.00015, "CNY": 0.0016, "COP": 0.0000030, "EGP": 0.00068, "HKD": 0.0014, "IDR": 0.000000074, "IQD": 0.00000069, "IRR": 0.000000025, "NZD": 0.011, "NPR": 0.00014, "PHP": 0.00033, "PKR": 0.00010, "RUB": 0.00022, "LKR": 0.000086, "SAR": 0.0045, "SGD": 0.012},
    "CAD": {"USD": 0.79, "EUR": 0.69, "GBP": 0.61, "JPY": 81.48, "INR": 58.84, "CAD": 1, "AFN": 0.010, "ARS": 0.0079, "AUD": 0.57, "BDT": 0.0095, "BRL": 0.13, "BTN": 0.010, "CNY": 0.11, "COP": 0.00022, "EGP": 0.050, "HKD": 0.10, "IDR": 0.000055, "IQD": 0.00052, "IRR": 0.000018, "NZD": 0.52, "NPR": 0.0064, "PHP": 0.015, "PKR": 0.0046, "RUB": 0.0095, "LKR": 0.0037, "SAR": 0.20, "SGD": 0.54},
    "AFN": {"USD": 77.43, "EUR": 68.27, "GBP": 60.13, "JPY": 8, "INR": 579.12, "CAD": 97.45, "AFN": 1, "ARS": 0.79, "AUD": 56.99, "BDT": 0.95, "BRL": 13.01, "BTN": 1.05, "CNY": 11.15, "COP": 21.71, "EGP": 248.92, "HKD": 502.69, "IDR": 2777.27, "IQD": 26.04, "IRR": 929.38, "NZD": 49.49, "NPR": 612.88, "PHP": 1419.03, "PKR": 417.63, "RUB": 869.67, "LKR": 339.17, "SAR": 184.10, "SGD": 50.10},
    "ARS": {"USD": 100.10, "EUR": 88.17, "GBP": 77.63, "JPY": 10.24, "INR": 739.42, "CAD": 124.50, "AFN": 1.26, "ARS": 1, "AUD": 72.08, "BDT": 1.20, "BRL": 16.43, "BTN": 1.34, "CNY": 14.19, "COP": 27.65, "EGP": 317.25, "HKD": 639.91, "IDR": 3530.30, "IQD": 33.21, "IRR": 1184.56, "NZD": 63.16, "NPR": 782.19, "PHP": 1811.11, "PKR": 533.84, "RUB": 1112.05, "LKR": 433.85, "SAR": 235.68, "SGD": 63.92},
    "AUD": {"USD": 1.37, "EUR": 1.21, "GBP": 1.06, "JPY": 140.79, "INR": 75.05, "CAD": 1.75, "AFN": 0.018, "ARS": 0.014, "AUD": 1, "BDT": 0.017, "BRL": 0.23, "BTN": 0.019, "CNY": 0.20, "COP": 0.00037, "EGP": 0.085, "HKD": 0.17, "IDR": 0.000092, "IQD": 0.00086, "IRR": 0.000031, "NZD": 0.87, "NPR": 0.011, "PHP": 0.025, "PKR": 0.0077, "RUB": 0.016, "LKR": 0.0064, "SAR": 0.34, "SGD": 0.92},
    "BDT": {"USD": 84.55, "EUR": 74.57, "GBP": 65.63, "JPY": 8.67, "INR": 62.71, "CAD": 105.58, "AFN": 1.08, "ARS": 0.85, "AUD": 61.48, "BDT": 1, "BRL": 13.69, "BTN": 1.11, "CNY": 11.73, "COP": 22.86, "EGP": 262.51, "HKD": 529.41, "IDR": 2918.18, "IQD": 27.39, "IRR": 976.11, "NZD": 51.91, "NPR": 642.53, "PHP": 1486.08, "PKR": 437.83, "RUB": 911.62, "LKR": 355.38, "SAR": 193.15, "SGD": 52.45},
    "BRL": {"USD": 5.65, "EUR": 4.98, "GBP": 4.39, "JPY": 0.58, "INR": 41.88, "CAD": 7.06, "AFN": 0.072, "ARS": 0.056, "AUD": 4.05, "BDT": 0.073, "BRL": 1, "BTN": 0.081, "CNY": 0.85, "COP": 1.67, "EGP": 19.17, "HKD": 38.66, "IDR": 213.03, "IQD": 2, "IRR": 71.20, "NZD": 3.79, "NPR": 46.93, "PHP": 108.62, "PKR": 31.96, "RUB": 66.63, "LKR": 25.99, "SAR": 14.12, "SGD": 3.84},
    "BTN": {"USD": 71.90, "EUR": 63.38, "GBP": 55.88, "JPY": 7.37, "INR": 53.17, "CAD": 89.40, "AFN": 0.92, "ARS": 0.72, "AUD": 51.86, "BDT": 0.88, "BRL": 12.06, "BTN": 1, "CNY": 10.53, "COP": 20.57, "EGP": 236.17, "HKD": 476.32, "IDR": 2622.09, "IQD": 24.60, "IRR": 876.53, "NZD": 46.73, "NPR": 578.03, "PHP": 1338.55, "PKR": 394.37, "RUB": 820.41, "LKR": 320.01, "SAR": 173.82, "SGD": 47.22},
    "CNY": {"USD": 6.45, "EUR": 5.69, "GBP": 5.01, "JPY": 0.66, "INR": 47.65, "CAD": 8.02, "AFN": 0.082, "ARS": 0.064, "AUD": 4.62, "BDT": 0.078, "BRL": 1.07, "BTN": 0.087, "CNY": 1, "COP": 1.96, "EGP": 22.48, "HKD": 45.39, "IDR": 249.70, "IQD": 2.34, "IRR": 83.65, "NZD": 4.45, "NPR": 55.07, "PHP": 127.38, "PKR": 37.50, "RUB": 78.13, "LKR": 30.46, "SAR": 16.55, "SGD": 4.49},
    "COP": {"USD": 3588.32, "EUR": 3161.46, "GBP": 2783.44, "JPY": 367.34, "INR": 26445.60, "CAD": 4447.11, "AFN": 45.58, "ARS": 35.55, "AUD": 2561.02, "BDT": 42.93, "BRL": 587.85, "BTN": 47.82, "CNY": 505.51, "COP": 1, "EGP": 11474.71, "HKD": 23136.01, "IDR": 127327.27, "IQD": 1197.73, "IRR": 42703.05, "NZD": 2272.19, "NPR": 28098.70, "PHP": 65022.42, "PKR": 19147.76, "RUB": 39827.08, "LKR": 15541.10, "SAR": 8442.35, "SGD": 2295.69},
    "EGP": {"USD": 15.45, "EUR": 13.62, "GBP": 11.99, "JPY": 1.58, "INR": 113.85, "CAD": 19.15, "AFN": 0.20, "ARS": 0.16, "AUD": 11.64, "BDT": 0.19, "BRL": 2.62, "BTN": 0.21, "CNY": 2.20, "COP": 4.30, "EGP": 1, "HKD": 2.01, "IDR": 11.05, "IQD": 0.104, "IRR": 3.72, "NZD": 0.20, "NPR": 2.49, "PHP": 5.77, "PKR": 1.70, "RUB": 3.54, "LKR": 1.38, "SAR": 0.75, "SGD": 0.20},
    "HKD": {"USD": 7.77, "EUR": 6.84, "GBP": 6.02, "JPY": 0.79, "INR": 56.89, "CAD": 9.57, "AFN": 0.10, "ARS": 0.079, "AUD": 5.73, "BDT": 0.096, "BRL": 1.31, "BTN": 0.106, "CNY": 1.12, "COP": 2.18, "EGP": 24.99, "HKD": 1, "IDR": 5.49, "IQD": 0.052, "IRR": 1.86, "NZD": 9.92, "NPR": 122.77, "PHP": 284.18, "PKR": 83.72, "RUB": 174.27, "LKR": 68.01, "SAR": 36.91, "SGD": 10.03},
    "IDR": {"USD": 14280.50, "EUR": 12584.14, "GBP": 11068.89, "JPY": 1462.91, "INR": 105421.50, "CAD": 17743.23, "AFN": 182.29, "ARS": 142.23, "AUD": 10225.36, "BDT": 171.55, "BRL": 2350.57, "BTN": 191.04, "CNY": 2014.57, "COP": 393430.98, "EGP": 4522.74, "HKD": 9146.25, "IDR": 1, "IQD": 9.39, "IRR": 334.83, "NZD": 17812.15, "NPR": 220426.79, "PHP": 510593.57, "PKR": 150283.25, "RUB": 312588.97, "LKR": 121670.19, "SAR": 66126.89, "SGD": 17972.80},
    "IQD": {"USD": 1459.70, "EUR": 1285.75, "GBP": 1131.42, "JPY": 149.27, "INR": 10751.50, "CAD": 1810.51, "AFN": 18.58, "ARS": 14.52, "AUD": 1045.82, "BDT": 17.49, "BRL": 239.79, "BTN": 19.52, "CNY": 206.08, "COP": 40317.09, "EGP": 463.75, "HKD": 937.28, "IDR": 106.67, "IQD": 1, "IRR": 35.65, "NZD": 1901.66, "NPR": 23512.24, "PHP": 54420.16, "PKR": 16039.51, "RUB": 33336.29, "LKR": 12995.45, "SAR": 7067.27, "SGD": 1920.61},
    "IRR": {"USD": 42105, "EUR": 37093, "GBP": 32636, "JPY": 4311.34, "INR": 310606, "CAD": 52239.45, "AFN": 536.33, "ARS": 418.77, "AUD": 30048.64, "BDT": 503.82, "BRL": 6906.76, "BTN": 562.57, "CNY": 5935.80, "COP": 1159793.70, "EGP": 13316.79, "HKD": 26904.88, "IDR": 298.82, "IQD": 27.97, "IRR": 1, "NZD": 53318.75, "NPR": 658327.69, "PHP": 1524892.53, "PKR": 449353.20, "RUB": 934918.60, "LKR": 364128.40, "SAR": 198140.47, "SGD": 53889.35},
    "NZD": {"USD": 1.45, "EUR": 1.28, "GBP": 1.13, "JPY": 149.37, "INR": 107.53, "CAD": 1.92, "AFN": 0.020, "ARS": 0.016, "AUD": 1.15, "BDT": 0.019, "BRL": 0.26, "BTN": 0.021, "CNY": 0.22, "COP": 0.00043, "EGP": 0.098, "HKD": 0.20, "IDR": 0.00011, "IQD": 0.0010, "IRR": 0.000036, "NZD": 1, "NPR": 0.012, "PHP": 0.028, "PKR": 0.0083, "RUB": 0.017, "LKR": 0.0067, "SAR": 0.36, "SGD": 0.98},
    "NPR": {"USD": 117.30, "EUR": 103.32, "GBP": 90.88, "JPY": 11.99, "INR": 863.70, "CAD": 145.26, "AFN": 1.49, "ARS": 1.16, "AUD": 83.48, "BDT": 1.40, "BRL": 19.21, "BTN": 1.56, "CNY": 16.44, "COP": 3212.84, "EGP": 369.39, "HKD": 747.09, "IDR": 8250.00, "IQD": 77.32, "IRR": 2760.00, "NZD": 147.59, "NPR": 1, "PHP": 2311.67, "PKR": 681.97, "RUB": 1417.91, "LKR": 552.07, "SAR": 300.07, "SGD": 81.49},
    "PHP": {"USD": 47.49, "EUR": 41.85, "GBP": 36.83, "JPY": 4.85, "INR": 349.43, "CAD": 58.88, "AFN": 0.60, "ARS": 0.47, "AUD": 33.72, "BDT": 0.56, "BRL": 7.67, "BTN": 0.62, "CNY": 6.50, "COP": 1269.20, "EGP": 14.58, "HKD": 29.49, "IDR": 325.52, "IQD": 3.05, "IRR": 108.81, "NZD": 5.81, "NPR": 71.93, "PHP": 1, "PKR": 294.21, "RUB": 611.57, "LKR": 238.32, "SAR": 129.59, "SGD": 35.19},
    "PKR": {"USD": 160.61, "EUR": 141.39, "GBP": 124.30, "JPY": 16.39, "INR": 1180.33, "CAD": 198.76, "AFN": 2.04, "ARS": 1.59, "AUD": 114.22, "BDT": 1.91, "BRL": 26.18, "BTN": 2.13, "CNY": 22.49, "COP": 4389.91, "EGP": 50.46, "HKD": 102.12, "IDR": 1127.47, "IQD": 10.59, "IRR": 377.59, "NZD": 20.15, "NPR": 249.41, "PHP": 579.44, "PKR": 1, "RUB": 2079.31, "LKR": 810.65, "SAR": 440.68, "SGD": 119.76},
    "RUB": {"USD": 75.22, "EUR": 66.25, "GBP": 58.32, "JPY": 7.69, "INR": 554.26, "CAD": 93.50, "AFN": 0.96, "ARS": 0.75, "AUD": 54.19, "BDT": 0.90, "BRL": 12.34, "BTN": 1.00, "CNY": 10.55, "COP": 2060.64, "EGP": 23.68, "HKD": 47.80, "IDR": 526.95, "IQD": 4.95, "IRR": 176.68, "NZD": 9.42, "NPR": 116.57, "PHP": 270.35, "PKR": 79.14, "RUB": 1, "LKR": 389.99, "SAR": 211.70, "SGD": 57.53},
    "LKR": {"USD": 202.14, "EUR": 178.03, "GBP": 156.69, "JPY": 20.65, "INR": 1488.69, "CAD": 250.45, "AFN": 2.57, "ARS": 2.00, "AUD": 143.94, "BDT": 2.41, "BRL": 33.04, "BTN": 2.69, "CNY": 28.40, "COP": 5548.60, "EGP": 63.73, "HKD": 128.83, "IDR": 1418.18, "IQD": 13.34, "IRR": 475.45, "NZD": 25.37, "NPR": 313.80, "PHP": 727.84, "PKR": 213.67, "RUB": 441.63, "LKR": 1, "SAR": 544.40, "SGD": 147.85},
    "SAR": {"USD": 3.75, "EUR": 3.30, "GBP": 2.91, "JPY": 0.38, "INR": 27.50, "CAD": 4.64, "AFN": 0.048, "ARS": 0.038, "AUD": 2.75, "BDT": 0.046, "BRL": 0.63, "BTN": 0.051, "CNY": 0.54, "COP": 105.35, "EGP": 1.21, "HKD": 2.44, "IDR": 26.88, "IQD": 0.25, "IRR": 8.88, "NZD": 0.47, "NPR": 5.78, "PHP": 13.40, "PKR": 3.94, "RUB": 8.20, "LKR": 3.19, "SAR": 1, "SGD": 0.27},
    "SGD": {"USD": 1.35, "EUR": 1.19, "GBP": 1.05, "JPY": 0.14, "INR": 52.48, "CAD": 1.76, "AFN": 0.018, "ARS": 0.014, "AUD": 1.02, "BDT": 0.017, "BRL": 0.23, "BTN": 0.019, "CNY": 0.20, "COP": 0.00039, "EGP": 0.089, "HKD": 0.18, "IDR": 0.00010, "IQD": 0.00090, "IRR": 0.000032, "NZD": 1.02, "NPR": 0.012, "PHP": 0.029, "PKR": 0.0085, "RUB": 0.017, "LKR": 0.0068, "SAR": 3.68, "SGD": 1}
}

def show_currency_chart():
    chart_window = tk.Toplevel(window)
    chart_window.title("Currency Chart")

    label_chart = tk.Label(chart_window, text="Available Currencies", font="Times 20 bold")
    label_chart.pack()

    for currency in conversion_rates.keys():
        label_currency = tk.Label(chart_window, text=currency, font="Times 16")
        label_currency.pack()

def clicked():
    amount = float(entry1.get())
    cur1 = entry2.get().upper()
    cur2 = entry3.get().upper()
    
    if cur1 in conversion_rates and cur2 in conversion_rates[cur1]:
        converted_amount = amount * conversion_rates[cur1][cur2]
        label4.config(text=f"{amount} {cur1} is equal to {converted_amount} {cur2}")
    else:
        label4.config(text="Invalid input! Please enter valid currencies.")

window = tk.Tk()
window.geometry("550x400")
window.title("Currency Converter")

menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

chart_menu = tk.Menu(menu_bar, tearoff=0)
chart_menu.add_command(label="View Chart", command=show_currency_chart)
menu_bar.add_cascade(label="Menu", menu=chart_menu)

label = tk.Label(window, text="Currency Converter", font="Times 20 bold")
label.place(x=120, y=40)

label1 = tk.Label(window, text="Enter Amount Here:", font="Times 16 bold")
label1.place(x=70, y=100)
entry1 = tk.Entry(window)

label2 = tk.Label(window, text="Enter Currency Here:", font="Times 16 bold")
label2.place(x=50, y=150)
entry2 = tk.Entry(window)

label3 = tk.Label(window, text="Enter Desired Currency Here:", font="Times 16 bold")
label3.place(x=2, y=200)
entry3 = tk.Entry(window)

entry1.place(x=270, y=105)
entry2.place(x=270, y=155)
entry3.place(x=270, y=205)

label4 = tk.Label(window, text="", font="Times 20 bold")
label4.place(x=20, y=300)

button = tk.Button(window, text="Convert", font="Times 16 bold", command=clicked)
button.place(x=70, y=250)  
window.mainloop()