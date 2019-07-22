//Created on 21/07/2019 by Mohamed Sharif and Jayasankar

//RUBICK'S CUBE Solver using Browser Automation.
//Python 3.x with Selinium Library and Chrome Driver is used.
//The inputs from rubick's cube can be images also.
//Can solve a fully scrambled cube in 20 or lesser moves.
//Can use any python IDE (recommmeded: Spyder IDE)  
//Internet Connection is required.(recommmended: 1 Mbps or above)


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Step 1: Download and add Selenium Library to python library ("https://www.seleniumhq.org/download/")

Step 2: Download  chrome driver from "https://sites.google.com/a/chromium.org/chromedriver/downloads" .
	Download the right driver version for your chrome browser version.

Step 3: Keep the chrome driver installer in the same folder as the python program and install it.

For giving image as input, Step 4 5 6 and 7 
For giving the colors in text as input, jump to step 8


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Step 4: Capture the image in given format

      xxx				
      xWx
      xxx
	
xxx   xxx  xxx  xxx
xOx   xGx  xRx  xBx
xxx   xxx  xxx  xxx
     
      xxx
      xYx
      xxx


W - white	: up 
O - orange	: left
G - green	: face
R - red		: right`16:12 22-07-201916:12 22-07-201916:12 22-07-2019
B - blue	: bottom
Y - yellow	: down

Step 5: The images can also be captured by phone camera and used in the program. For that download "WiFi File Transfer" in your android phone ("https://play.google.com/store/apps/details?id=com.smarterdroid.wififiletransfer&hl=en")

Step 6: Open "image_processing.py" file. Read, configure and then run it. "image_processing.py" file is for image processing, cube detection, colour recognition and bit sampling.

Step 7: Run "solver_image.py" to get output.

END

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

For text as input, use the format given below

      123
      4N6   
      789 
in the "solver_text.py" file

N=5=default

Step 8:Run "solver_text.py"

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

