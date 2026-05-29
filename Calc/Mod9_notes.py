quit = False
while quit == False:
    print("1)Ellipse\n2.)Hyperbola\n3.)Equastion of asymtopes\n4.)Parabola\n5.)Identification")

    selection = int(input(">Select: "))


    if selection == 1:
        print("Equastion:Horazontal/Vertical:\n[(x-h)^2/a^2]+[(y-k)^2/b^2]\n[(x-h)^2/b^2]+[(y-k)^2/a^2]")
        input("")
        print("Center: (h,k)\n Foci: C^(2)=a^(2)-b^(2)")
        input("A>B")
    
    elif selection == 2:
        print("Equastion:Horazontal/Vertical:\n[(x-h)^2/a^2]-[(y-k)^2/b^2]\n[(y-k)^2/a^2]-[(x-h)^2/b^2]")
        input("")
        print("Vertex: a\nCo-vertex: b\ncenter: (h,k)\nFoci: C^(2)=a^(2)+b^(2)")
        input("")

    elif selection == 3:
        #skip till better understanding
        print("filler")

    elif selection == 4:
        print("Ax^2+Cy^2+Dx+Ey+F=0")
        print("Circle: A = C")
        print("Ellipse:AC>0, A ≠ C")
        print("Parabola: AC=0")
        print("Hyperbola: AC<0")
        input("")
        print("Ax^2+Bxy+Cy^2+Dx+Ey+F=0")
        print("P=V^(2)-4AC")
        print("P=0: Porabola\nP<0:Ellipse\nP>0:Hyperbola")
        input("")
    else:
        print("incorrect selection")

