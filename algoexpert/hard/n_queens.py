import turtle
   
# create screen object 
sc = turtle.Screen() 
   
# create turtle object 
pen = turtle.Turtle() 

def solve(result, queens, n):
    if len(queens) == n:
        result.append(queens[:])
        return 
    # try to place queen on each column
    for i in range(0, n):
        if check_valid_pos(queens, i, n):
            queens.append(i)
            solve(result, queens, n)
            queens.pop()

    return result

def check_valid_pos(queens, pos, n):
    if not queens:
        return True
    if pos in queens:
        return False
    for ppos in queens:
        diagnols = []
        for j in range(ppos, n):
            diagnols.append(ppos - 1)
            diagnols.append(ppos + 1)
    if pos in diagnols:
        return False
    return True

def main():
    result = []
    queens = []
    n = 4
    solve(result, queens, n)
    response = []
    for sol in result:
        str_soln = []
        for col in sol:
            col_str = ["."]*n
            col_str[col] = "Q"
            str_soln.append("".join(col_str))
        response.append(str_soln)
    print(response)
    sc.setup(600, 600)
    pen.speed(200)

    for i in range(n):
        pen.up()
        pen.setpos(0, 30 * i)
        pen.down()

        for j in range(n):
            if (i + j)%2 == 0:
                col = 'black'
            else:
                col = 'white'
            pen.fillcolor(col) 
       
            # start filling with colour 
            pen.begin_fill() 
            # call method 
            draw() 
            # stop filling 
            pen.end_fill() 

        pen.hideturtle()
    turtle.exitonclick()
    
def draw(): 
   
  for i in range(4): 
    pen.forward(30) 
    pen.left(90) 
   
  pen.forward(30) 
   
if __name__ =="__main__":
    main()