t = int(input())

if t>=1 and t<=10:
   for tcase in range(1,t+1):
      array = []
      arrayadd = []
      flag = 0
      for each in range(0,4): 
         arrayadd = [x for x in raw_input()]
         array.append(arrayadd)
   
      for i in range(0,4):
         for j in range(0,4):
            if array[i][j] == '.':
				#xx.
               if j>1 and (array[i][(j-1)] == 'x' and array[(i)][(j-2)] == 'x'):
                  flag = 1
				#.xx
               elif j<2 and (array[i][j+1] == 'x' and array[i][j+2] == 'x'):
                  flag = 1
				#.00 .x. ..x
               elif i<2 and (array[i+1][j] == 'x' and array[i+2][j] == 'x'):
                  flag = 1
				 # x.. .x. ...
               elif i>1 and (array[i-1][j] == 'x' and array[i-2][j] == 'x'):
                  flag = 1
				 #xoo oxo oox
               elif (i<2 and j<2) and (array[i+1][j+1] == 'x' and array[i+2][j+2] == 'x'):
                  flag = 1
				  #oox oxo xoo
               elif (i<2 and j>1) and (array[i+1][j-1] == 'x' and array[i+2][j-2] == 'x'):
                  flag = 1
	
               elif ((i<3 and i>1) and j>1) and (array[i-1][j-1] == 'x' and array[i-2][j-2] == 'x'):
                  flag = 1
               elif (i>1 and j<2) and (array[i-1][j+1] == 'x' and array[i-2][j+2] == 'x'):
                  flag = 1
               elif (j<3 and j>0) and (array[i][j-1] == 'x' and array[i][j+1] == 'x'):
                  flag = 1
               elif (i>0 and i<3) and (array[i-1][j] == 'x' and array[i+1][j] == 'x'):
                  flag = 1
               elif ((i>0 and i<3) and (j>0 and j<3)) and (array[i-1][j-1] == 'x' and array[i+1][j+1] == 'x'):
                  flag = 1
               elif ((i>0 and i<3) and (j<3 and j>0)) and (array[i-1][j+1] == 'x' and array[i+1][j-1] == 'x'):
                  flag = 1
               else:
                  flag = 0
	
            if flag == 1: break
         if flag == 1: break
      if flag == 1: print('YES')
      if flag == 0: print('NO')