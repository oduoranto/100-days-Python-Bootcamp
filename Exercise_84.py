def paint_calc(height, width, coverage):
    number_of_cans = round((height * width)/ coverage)
    print(f"The number of cans needed is {number_of_cans}")


h = float(input("Enter the height of the wall: "))
w =float(input("Enter the width of the wall: "))
coverage = 5
paint_calc(h,w,coverage)    