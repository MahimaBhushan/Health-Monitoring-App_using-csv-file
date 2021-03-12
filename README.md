# Health-Monitoring-App_using-csv-file 

We are not collecting the data from the router in real time, but using the already available data which is stored in Routerdata.csv.

1.  Routerdata.csv :this file containes the data values of 5 routers

2.  db_csv.py :extracts data from Routerdata.csv

3.  assets folder : Contains all the images,stylesheets and javascript. For css and js to be included into the dashboard.

4.  app.py : initialises an app object

5.  index.py : conatins the main dash layout

6.  callback.py : onevent functions. To change which file to be called when router added, change here

7.  layouts.py : layouts of all pages

8.  Dockerfile : Docker builds images automatically by reading the instructions from a Dockerfile -- a text file that contains all commands, in order, needed to build a given image

9.  requirements.txt : this file contains all the packages to be installed using pip install which will be used in the dockerfile.


steps to run the app:

1.  build the image 

>>docker build -t healthapp .

2.  run the image to form the container

>>docker run -p 5050:8765 healthapp

-p is used to map the port 8765 of the docker container to the port 5050 of the host system.

:go to http://127.0.0.1:5050 to view the dashboard. The live data is being read and updated on the dashboard.



Only one container is created here to run the dashboard, because we are not using any database or collect data file.
