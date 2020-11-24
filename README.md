# If, elif and else

To complete our initial survey of logic we now need to consider what programs we might write if we have multiple logic propositions.  

The first way we might use multiple logical propositions is within an `elif` statement as is illustrated in the code below:

````
if a==1 : 
   b = 2
elif a==2 : 
   b = 3
elif a==3 : 
   b = 4
else : 
   b = 5
````   

`elif` is short for else if so this code sets the variable `b` equal to 2 if the variable `a` is equal to 1, the value of `b` equal to 3 if `a` is equal to 2, the value of `b` equal to 4 if `a` is equal to 3 and the value of `b` equal to 5 if a takes any value that is not 1, 2 or 3.  

Notice that only one of the four logical propositions above can have a truth value of 1 for a particular value of a as `a` cannot take multiple values simultaneously.  Code such as the one below should be avoided as, if `a` is equal to 2 here then `a<3` and `a>1`.  

````
if a < 3 : 
   b = 2 
elif a > 1 : 
   b = 3
````
 
__I would like you to use the information that has been provided here to fix the code on the left__.  If you run it now you should see `nnn` is equal to the output from the function `numberLessThan`.  `mmm` and `kkk` are not equal to the quantities that they should be equal to, however.  __To pass the test you should adjust the if/elif/else statements in the loop at the end of the code so as to ensure that the variables `mmm` and `kkk` are set in accordance with the description that is output.__
  
