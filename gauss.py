import os
import Problems as op

class Gauss(object):
    def __init__(self):
        pass

    def eliminacion4x4(self):
        os.system('clear') #linux is clear
        op.Problems.msj('s')
        print('Datos del Primer Array ')
        a11 = float(input())
        a12 = float(input())
        a13 = float(input())
        a14 = float(input())
        b1 = float(input())
        os.system('clear')
        op.Problems.msj('s')
        print('Datos del Segundo Array ')
        a21 = float(input())
        a22 = float(input())
        a23 = float(input())
        a24 = float(input())
        b2 = float(input())
        os.system('clear')
        op.Problems.msj('s')
        print('Datos del Tercer Array ')
        a31 = float(input())
        a32 = float(input())
        a33 = float(input())
        a34 = float(input())
        b3 = float(input())
        os.system('clear')
        op.Problems.msj('s')
        print('Datos del Cuarto Array ')
        a41 = float(input())
        a42 = float(input())
        a43 = float(input())
        a44 = float(input())
        b4 =  float(input())
        os.system('clear')

        a = [[a11,a12,a13,a14,b1],[a21,a22,a23,a24,b2],[a31,a32,a33,a34,b3],[a41,a42,a43,a44,b4]]
       
        op1 = op.Problems.form('d',a22,a21,a11,a12)
        op2 = op.Problems.form('d',a23,a21,a11,a13)
        op3 = op.Problems.form('d',a24,a21,a11,a14)
        op4 = op.Problems.form('d',b2,a21,a11,b1)

        op5 = op.Problems.form('d',a32,a31,a11,a12)
        op6 = op.Problems.form('d',a33,a31,a11,a13)
        op7 = op.Problems.form('d',a34,a31,a11,a14)
        op8 = op.Problems.form('d',b3,a31,a11,b1)

        op9 = op.Problems.form('d',a42,a41,a11,a12)
        op10 = op.Problems.form('d',a43,a41,a11,a13)
        op11 = op.Problems.form('d',a44,a41,a11,a14)
        op12 = op.Problems.form('d',b4,a41,a11,b1)
       
        b = [[op1,op2,op3,op4],[op5,op6,op7,op8],[op9,op10,op11,op12]]

        ope1 = op.Problems.form('d',op6,op5,op1,op2)
        ope2 = op.Problems.form('d',op7,op5,op1,op3)
        ope3 = op.Problems.form('d',op8,op5,op1,op4)

        ope4 = op.Problems.form('d',op10,op9,op1,op2)
        ope5 = op.Problems.form('d',op11,op9,op1,op3)
        ope6 = op.Problems.form('d',op12,op9,op1,op4)

        c = [[ope1,ope2,ope3],[ope4,ope5,ope6]]

        oper1 = op.Problems.form('d',ope5,ope4,ope1,ope2)
        oper2 = op.Problems.form('d',ope6,ope4,ope1,ope3)

        d = [[oper1,oper2]]


        l = [[1,0,0,0],[a21/a11,1,0,0],[a31/a11,op5/op1,1,0],[a41/a11,op9/op1,ope4/ope1,1]]

        print('Matriz L ')
        print(l[0][0]," ", l[0][1]," ", l[0][2]," ", l[0][3])
        print("{0:.2f}".format(l[1][0])," ", l[1][1]," ", l[1][2]," ", l[1][3])
        print("{0:.2f}".format(l[2][0])," ","{0:.2f}".format(l[2][1])," ", l[2][2]," ",l[2][3])
        print("{0:.2f}".format(l[3][0])," ","{0:.2f}".format(l[3][1])," ","{0:.2f}".format(l[3][2])," ", l[3][3])

        print(' ')
        u = [[a11,a12,a13,a14],[0,op1,op2,op3],[0,0,ope1,ope2],[0,0,0,oper1]]

        print('Matriz U ')
        print(u[0][0], " ", u[0][1]," ",u[0][2]," ",u[0][3])
        print(u[1][0], " ", u[1][1]," ",u[1][2]," ",u[1][3])
        print(u[2][0], " ", u[2][1]," ",u[2][2]," ",u[2][3])
        print(u[3][0], " ", u[3][1]," ",u[3][2]," ",u[3][3])
        
       
        lu1 = op.Problems.form1('d',l[0][0],u[0][0],l[0][1],u[1][0],l[0][2],u[2][0],l[0][3],u[3][0])
        lu2 = op.Problems.form1('d',l[0][0],u[0][1],l[0][1],u[1][1],l[0][2],u[2][1],l[0][3],u[3][1])
        lu3 = op.Problems.form1('d',l[0][0],u[0][2],l[0][1],u[1][2],l[0][2],u[2][2],l[0][3],u[3][2])
        lu4 = op.Problems.form1('d',l[0][0],u[0][3],l[0][1],u[1][3],l[0][2],u[2][3],l[0][3],u[3][3])
       
        lu5 = op.Problems.form1('d',l[1][0],u[0][0],l[1][1],u[1][0],l[1][2],u[2][0],l[1][3],u[3][0])
        lu6 = op.Problems.form1('d',l[1][0],u[0][1],l[1][1],u[1][1],l[1][2],u[2][1],l[1][3],u[3][1])
        lu7 = op.Problems.form1('d',l[1][0],u[0][2],l[1][1],u[1][2],l[1][2],u[2][2],l[1][3],u[3][2])
        lu8 = op.Problems.form1('d',l[1][0],u[0][3],l[1][1],u[1][3],l[1][2],u[2][3],l[1][3],u[3][3])
  
        lu9 = op.Problems.form1('d',l[2][0],u[0][0],l[2][1],u[1][0],l[2][2],u[2][0],l[2][3],u[3][0])
        lu10 = op.Problems.form1('d',l[2][0],u[0][1],l[2][1],u[1][1],l[2][2],u[2][1],l[2][3],u[3][1])
        lu11 = op.Problems.form1('d',l[2][0],u[0][2],l[2][1],u[1][2],l[2][2],u[2][2],l[2][3],u[3][2])
        lu12 = op.Problems.form1('d',l[2][0],u[0][3],l[2][1],u[1][3],l[2][2],u[2][3],l[2][3],u[3][3])
       
        lu13 = op.Problems.form1('d',l[3][0],u[0][0],l[3][1],u[1][0],l[3][2],u[2][0],l[3][3],u[3][0])
        lu14 = op.Problems.form1('d',l[3][0],u[0][1],l[3][1],u[1][1],l[3][2],u[2][1],l[3][3],u[3][1])
        lu15 = op.Problems.form1('d',l[3][0],u[0][2],l[3][1],u[1][2],l[3][2],u[2][2],l[3][3],u[3][2])
        lu16 = op.Problems.form1('d',l[3][0],u[0][3],l[3][1],u[1][3],l[3][2],u[2][3],l[3][3],u[3][3])
   
        lxu = [[lu1,lu2,lu3,lu4],[lu5,lu6,lu7,lu8],[lu9,lu10,lu11,lu12],[lu13,lu14,lu15,lu16]]

        print(' ')
        print(' Matriz L*U ')
        print("{:.1f}".format(lxu[0][0])," ","{:.1f}".format(lxu[0][1])," ","{:.1f}".format(lxu[0][2])," ","{:.1f}".format(lxu[0][3]))
        print("{:.1f}".format(lxu[1][0])," ","{:.1f}".format(lxu[1][1])," ","{:.1f}".format(lxu[1][2])," ","{:.1f}".format(lxu[1][3]))
        print("{:.1f}".format(lxu[2][0])," ","{:.1f}".format(lxu[2][1])," ","{:.1f}".format(lxu[2][2])," ","{:.1f}".format(lxu[2][3]))
        print("{:.1f}".format(lxu[3][0])," ","{:.1f}".format(lxu[3][1])," ","{:.1f}".format(lxu[3][2])," ","{:.1f}".format(lxu[3][3]))

