#Copyright (c) 2013 Akrita Agarwal
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

import sys,math
from xlrd import open_workbook,cellname
from xlwt import Workbook

#learning rate alpha is a constant and can be assumed according to the dataset.
alpha = 0.01

def hypothesis(x,theta):
    power = 0.0
    for val in range(0,len(x)):
        #print(theta,x)
        power = power + theta[val]*float(x[val])
    power = round(power,2)
    #print(power)
    if power<-500:
        h = 0.0
    elif power>=500:
        h = 1.0
    else:
        h = 1/(1+math.exp(-power))
    #print(h,"h")
    return h

 
def mincostfunction(x,y,theta,j):
    summation = 0
    for i in range(0,len(x)):
        summation = summation + ((hypothesis(x[i],theta)-float(y[i]))*float(x[i][j]))
    return summation
        

def estimation(x,y,theta,count):
    #ntheta: new theta defined for enabling simultaneous update of theta
    ntheta = theta
    for j in range(0,len(x[0])):
        ntheta[j] = theta[j] - alpha*mincostfunction(x,y,theta,j)
    theta = ntheta
    count = count+1
    #we can choose the number of iterations according to the dataset. 
    if count == 30:
        return theta
    else:
        return estimation(x,y,theta,count)


def main(args):
    #train.xls - initial training set having 700 tuples of input data x 
    book = open_workbook('train.xls')
    sheet = book.sheet_by_index(0)
    length = sheet.nrows
    x = []
    for row in range(0,sheet.nrows):
        #a represents each tuple of the training set
        a = "" 
        for col in range(0,sheet.ncols):
            a = a+str(sheet.cell(row,col).value)+" "
            a = str(a)
        a = a.split()
        x.append(a)

    #trainLabels.xls - initial training set having 700 tuples of output data y
    book = open_workbook('trainLabels.xls')
    sheet = book.sheet_by_index(0)
    
    y = []
    for row in range(0,length):
        y.append(sheet.cell(row,0).value)

    #initializing theta to zero . other values can also be assumed
    theta = [0 for g in range(0,len(x[0]))]
    
    #function to estimate the value of theta
    theta = estimation(x,y,theta,0) 

    #test.xls - test set having 300 tuples of input data x
    book = open_workbook('test.xls')
    sheet = book.sheet_by_index(0)

    for row in range(0,sheet.nrows):
        #a represents each tuple of the training set
        a = "" 
        for col in range(0,sheet.ncols):
            a = a+str(sheet.cell(row,col).value)+" "
            a = str(a)
        a = a.split()
        x.append(a)

    val = [0 for i in range(0,len(x))]
    for i in range(0,len(x)):
        val[i] = hypothesis(x[i],theta)
        if val[i] >=0.5:
            val[i] = 1
        elif val[i]<0.5:
            val[i] = 0

    count = 0

    #testLabels.xls - test set having 300 tuples of output data y
    book = open_workbook('testLabels.xls')
    sheet = book.sheet_by_index(0)

    for row in range(0,sheet.nrows):
        if (sheet.cell(row,0).value)!=val[row]:
            count = count+1

    #accuracy calculation
    print('accuracy:',100 - (count*100/float(sheet.nrows)))

    #predict.xls - new dataset of 9000 tuples for which we predict class.
    book = open_workbook('predict.xls')
    sheet = book.sheet_by_index(0)

    new = []
    for row in range(0,sheet.nrows):
        #a represents each tuple of the prediction set
        a = "" 
        for col in range(0,sheet.ncols):
            a = a+str(sheet.cell(row,col).value)+" "
            a = str(a)
        a = a.split()
        new.append(a)
    
    x = new
    print('predicted values:')
    val = [0 for i in range(0,len(x))]
    for i in range(0,len(x)):
        val[i] = hypothesis(x[i],theta)
        if val[i] >=0.5:
            val[i] = 1
        elif val[i]<0.5:
            val[i] = 0
    print(val)
    book = Workbook()
    sheet1 = book.add_sheet('sheet 1')

    for i in range(0,len(val)):
        sheet1.write(i,0,val[i])

    book.save('predicted_values.xls')
    
if __name__ == "__main__": main(sys.argv)
