import tkinter as tk
import joblib
import numpy as np

model = joblib.load("package_predictor.joblib")

def checkpackage():
    cgpa = float(ent.get())

    cgpa_array = np.array(cgpa)
    cgpa_reshaped = cgpa_array.reshape(-1, 1)
    pkg = model.predict(cgpa_reshaped)[0]

    lblshow.config(text = f"Your Predicted Package is : {str(pkg)[ : 4]} lakh")
    

app = tk.Tk()
app.geometry("600x270")
app.title("Package Precditor")
app.config(background = "#78f745")

lbl = tk.Label(app, text = "Package Predictor", font = ("Robort", 30, "bold"), background = "#60bd3a", foreground = "#164702")
lbl.pack(fill = "x", ipady = 10)

ent = tk.Entry(app, font = ("Robort", 26))
ent.pack(pady = 15)

btn = tk.Button(app, text = "Check", font = ("Robort", 20, "bold"), bg = "#164702", fg = "#60bd3a", command = checkpackage)
btn.pack()

lblshow = tk.Label(app, text = "", font = ("Robort", 15), background = "#78f745", foreground = "#164702")
lblshow.pack(pady = 15)

app.mainloop()