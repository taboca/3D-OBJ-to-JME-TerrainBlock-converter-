Export OBJ from Sketch Up or other 3D app ( make sure you have a terrain like mesh object ) 

cp ~marciogalli/Desktop/baseterrain.obj  .

Clean 

187-26-233-41:obj_to_terrain marciogalli$ ./clean.py baseterrain.obj  > baseterrain-clean.obj 

Parse 

187-26-233-41:obj_to_terrain marciogalli$ ./parse.py baseterrain-clean.obj > file.txt

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

If you want to make sure the size of the array you can change the parse.py code and let it pring the II and JJ values

