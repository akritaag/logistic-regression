logistic-regression
===================

logistic regression is a machine learning algorithm to perform classification on a dataset. 
  
Classiﬁcation:

    Email:Spam/Not Spam?
    Online Transactions : Fraudulent Yes/No?
    Tumor: Malignant/Benign?
  
    0:Negative class , e.g.,benign - tumor
    1:Positive Class , e.g.,malignant - tumor
    
Thus we can establish that,
  Classification: y=0 or 1
  
    hypothesis function h(x) for given theta t,
    h(x,t) can be >1 of <0
    
In Logistic Regression we have

    0 <= h(x) <= 1
  
Logistic Regression model comprises of a function g such that,
    
    h(x,t) = g(z) 
  
  where
  h(x,t) - hypothesis function h for given theta t and input x
    
and

    g(z) = 1/(1+e(-z))
    
  which is a sigmoid function whose value lies between 0 and 1
  
    z = t''x
    
where t'' - transpose of the matrix theta t
 
The aim of the logistic regression algorithm is to calculate the minimum value of theta t which best depicts the 
learning set.

Thus to minimize the value of theta t we perform gradient descent on it.

    min J(t):

    Repeat {
      t(j) := t(j) - alpha * summation ( ( h(t,x[i]) - y[i]) - x[i][j] )
      }
      
where each theta t is simulteneously updated.

    J(t) - cost function for a given theta t
    t(j) - theta t for a given feature j available in all input values x
    alpha - learning rate ; constant for any given code
    x[i] - tuple number i in the given input data x
    y[i] - tuple number i in the given output data y
    x[i][j] - tuple number i and feature number j in given input data x
    
To study more on Logistic Regression , refer here : 

  Oregon State University - http://classes.engr.oregonstate.edu/eecs/winter2011/cs434/notes/Logistic-regression-7.pdf
  
  Indiana University - http://www.indiana.edu/~jopeng51/teaching-logistic.pdf
  
  Coursera.org (Machine Learning Course) - https://class.coursera.org/ml-2012-002/class/index


Download and observe the following

    1. training the LR model with train.xls dataset 
    2. testing for accuracy of the model using test.xls 
    3. predicting the classes for a unknown test dataset predict.xls by estimating theta t

The datasets used are a part of the Kaggle competition available at  
  Data Science London + Scikit-learn - http://www.kaggle.com/c/data-science-london-scikit-learn
  
  
In case of any suggestions/issues you can write to me : info@akrita.com
  
  The MIT License (MIT)
========================================================================================================================  
  
    Copyright (c) 2013 Akrita Agarwal
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
  
  
  
  
    
  
