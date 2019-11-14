#Shape identifier


####Problem
Consider a two dimensional co-ordinate system with two 
axes; X & Y. This system is identified by positive integer 
co-ordinates. Meaning, every valid point in this system is
 represented by two values (x, y) where 0 < x,y <100.

#####Input 
Json Format
~~~~
{
     "Lines":[ 
       "(A1,B1), (C1,D1)",
       "(A2,B2), (C2,D2)",
       "(An,Bn), (Cn,Dn)"
       ]
}

~~~~


#####Expected Response
~~~~
{
   "shapes": [{
           "name": "Square",
           "Vertices": "[(a1, b1), (a2, b2), (a8, b8), (a6, b6)]"
       },
       {
           "name": "Triangle",
           "Vertices": "[(a7, b7), (a4, b4), (a9, b9)]"
       },
       {
           "name": "Triangle",
           "Vertices": "[(a1, b1), (a2, b2), (a3, b3)]"
       }
   ]
}
~~~~

####NOTE
Note:
1. The input data may be such that some shapes overlap.
2. You don't have to find shapes formed by intersection of two shapes. For example, if a square and triangle overlap such that there is another small triangle formed at the intersection, you don't have to report that.
3. For the sake of scope, report only the following shapes, if any - triangle, any quadrilateral, pentagon.
