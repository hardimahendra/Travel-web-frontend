import turtle

def draw_flower():
    # Buat objek turtle
    t = turtle.Turtle()

    # Ulangi proses menggambar sebanyak 360 derajat
    for i in range(360):
        t.forward(100)
        t.right(30)
        t.forward(20)
        t.left(60)
        t.forward(50)
        t.right(30)
        t.penup()
        t.setposition(0, 0)
        t.pendown()
        t.right(1)

    # Tunggu sebelum menutup jendela
    turtle.exitonclick()

draw_flower()
