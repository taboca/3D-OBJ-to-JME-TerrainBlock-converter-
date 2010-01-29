Warning - how to use
===

If you are designing, with your application 3D, make sure you are designing a terrain like object. What I mean by that is that you need to make sure you are just lifiting faces in the Y ( to sky or down the ground ) axis. For example, you are not making for example a sphere. You just want to get a grid of faces and lift vertexes in the Y axis. If you do that this may work. Other thing.. do NOT rotate the base of the grid of faces. For example, when you start you make sure you start with a GRID like this:


o o o o o o o o o o 
o o o o o o o o o o 
o o o o o o o o o o 
o o o o o o o o o o 
o o o o o o o o o o 
o o o o o o o o o o 
o o o o o o o o o o 
o o o o o o o o o o 
o o o o o o o o o o 
o o o o o o o o o o 
 
+
/\ x
|
---> Z +  

* X rows by X cols view from top.
* Make sure this sits under the positive side of X and Z axis. You dont want to have negative numbers in X or Z
* Fine to have positive or negative numbers in the Y ( mountains or lakes :) 
* Export OBJ file 

Proceed: 
=======


Export OBJ from Sketch Up or other 3D app ( make sure you have a terrain like mesh object ) 

./clean.py exportedfile.obj  > new-clean.obj 

Check the file and see if you see things like "v X Y Z" with X and Z values being positive. Also notice that if you have NOT rotated your initial grid, which is fine and expected, then you should expect lots of repeteaded values in the X and Y. This is fine and expected and that is the only way things will work. The python will *sort* arrays to get the matrix in order and extract just the Y values for the points. 

Parse 

./parse.py new-clean.obj > file.txt

Copy the file.txt as an array of Float like this: 

  float[] map=new float[]{
        		   
	// contents of file.txt

  				 000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,
  				 000f,000f,010f,070f,020f,005f,040f,112f,123f,140f,160f,185f,220f,010f,000f,
  				 000f,005f,020f,010f,070f,015f,045f,112f,123f,140f,160f,185f,220f,120f,000f,
  				 000f,007f,030f,030f,110f,055f,050f,112f,123f,140f,160f,185f,220f,150f,000f,
  				 000f,010f,040f,040f,100f,085f,010f,112f,123f,140f,160f,185f,220f,170f,000f,
  				 000f,010f,050f,040f,100f,105f,020f,112f,123f,140f,160f,185f,220f,210f,000f,
  				 000f,010f,040f,030f,090f,085f,030f,112f,123f,120f,120f,085f,080f,180f,000f,
  				 000f,007f,030f,010f,040f,055f,040f,080f,073f,110f,090f,035f,060f,170f,000f,
  				 000f,005f,020f,000f,030f,035f,030f,050f,053f,090f,010f,035f,050f,160f,000f,
  				 000f,002f,010f,000f,010f,005f,020f,012f,013f,060f,000f,015f,020f,010f,000f,
  				 000f,001f,000f,000f,000f,001f,000f,002f,003f,000f,000f,001f,000f,000f,000f,
  				 000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,
  				 000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,
  				 000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,
  				 000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f,000f
				 
           };

If you want to make sure the size of the array you can change the parse.py code and let it print the II and JJ values. JME terrainBlock will only work if it is equal numbers of cols and rows. Good luck or write to me mgalli @ mgalli dot com

