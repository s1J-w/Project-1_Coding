import tkinter as tk
from tkinter import messagebox

def calculate_gravitational_force():
    try:
        G = 6.674 * 10**-11
        
        m1 = float(entry_m1.get())
        m2 = float(entry_m2.get())
        r = float(entry_r.get())
        
        if m1 <= 0 or m2 <= 0:
            messagebox.showerror("Error", "มวลของวัตถุต้องมีค่ามากกว่า 0")
        elif r <= 0:
            messagebox.showerror("Error", "ระยะห่างระหว่างวัตถุต้องมีค่ามากกว่า 0")
        else:
            F = G * m1 * m2 / r**2
            label_result.config(text=f"แรงดึงดูดระหว่างวัตถุ 1 และ 2 คือ: {F:.2e} นิวตัน")
    
    except ValueError:
        messagebox.showerror("Error", "กรุณากรอกค่าที่ถูกต้อง (เป็นตัวเลขเท่านั้น)")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("คำนวณแรงดึงดูดระหว่างวัตถุ")

# สร้างป้ายข้อความและช่องกรอกข้อมูล
label_m1 = tk.Label(root, text="มวลของวัตถุ 1 (kg):")
label_m1.grid(row=0, column=0, padx=10, pady=5)
entry_m1 = tk.Entry(root)
entry_m1.grid(row=0, column=1, padx=10, pady=5)

label_m2 = tk.Label(root, text="มวลของวัตถุ 2 (kg):")
label_m2.grid(row=1, column=0, padx=10, pady=5)
entry_m2 = tk.Entry(root)
entry_m2.grid(row=1, column=1, padx=10, pady=5)

label_r = tk.Label(root, text="ระยะห่างระหว่างวัตถุ (m):")
label_r.grid(row=2, column=0, padx=10, pady=5)
entry_r = tk.Entry(root)
entry_r.grid(row=2, column=1, padx=10, pady=5)

# สร้างปุ่มสำหรับคำนวณ
button_calculate = tk.Button(root, text="คำนวณ", command=calculate_gravitational_force)
button_calculate.grid(row=3, column=0, columnspan=2, pady=10)

# สร้างป้ายสำหรับแสดงผลลัพธ์
label_result = tk.Label(root, text="แรงดึงดูดระหว่างวัตถุ 1 และ 2 คือ:")
label_result.grid(row=4, column=0, columnspan=2, pady=5)

# เริ่มการทำงานของ GUI
root.mainloop()
