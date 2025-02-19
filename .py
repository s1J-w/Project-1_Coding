def gravitational_force():
    G = 6.674 * 10**-11

    try:
        m1 = float(input("กรุณาป้อนมวลของวัตถุ 1 (kg): "))
        m2 = float(input("กรุณาป้อนมวลของวัตถุ 2 (kg): "))
        r = float(input("กรุณาป้อนระยะห่างระหว่างวัตถุ (m): "))

        if m1 <= 0 or m2 <= 0:
            print("มวลของวัตถุต้องมีค่ามากกว่า 0")
        elif r <= 0:
            print("ระยะห่างระหว่างวัตถุต้องมีค่ามากกว่า 0")
        else:
            F = G * m1 * m2 / r**2
            print(f"แรงดึงดูดระหว่างวัตถุ 1 และ 2 คือ: {F} นิวตัน")

    except ValueError:
        print("กรุณากรอกค่าที่ถูกต้อง (เป็นตัวเลขเท่านั้น)")

gravitational_force()