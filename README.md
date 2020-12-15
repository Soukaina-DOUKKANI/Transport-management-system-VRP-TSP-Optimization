# Transport-management-system-VRP-TSP-Optimization
Transport management system helps in solving transport management issues including traceability, cost efficiency , time saving and routes optimization. The software is based on algorithms and metaheuristic that ensure optimal solutions and minimal costs. The project consists of to parts: development of algorithms using python and creating a web interface using Flask, Html, CSS, Bootstrap and Javascript. 


*Vns.py: refers to the metaheurstic variable neighborhood search developped with Python oriented object in which we use :

-a seed function: that generates the initial route used as an initial solution 
-stochastic2opt: optimization model serving for generating random routes with there relative costs 
-local search function (VND) : used to search locally for the local minimum 
-VNS function : that use stochastic2opt and VND to calculate the global minimum consisting of the optomal solution.


*BB.py: refering to the branch and bound algorithm that uses two functions: 
-BAB: branch function that splits the route into sub-routes and calculates their costs 
-BABrec: bound function (evaluation function) that evalute results of BAB and generates optimal route.


*CW.py: in reference to the clark and wright algorithm that calculates savings between arcs and generate solution


*APP.py: python file containing the flask app and routes that generate a web app deployed in the local server.


*Templates : the frontend was developped using HTML5, CSS3, JS, BOOTSTRAP 

-Template1.html: refers to the home page in which user should insert the algorithm that he wants to apply. 
-Template2.html, VNS.html: refer to vns visualization 
-map.html : refers to generating a google map using the library : gmplot 
-Template3.html, BB.html: visualization of Branch and bound result 
-Template4.html, CW.html : visualization of clark and wright


*Data: in this project we have used moroccan cities to generate the optimal route that a salesman can take to deliver products on time. 
( the matrix of distances : distances_villes.xlsx, coordinates(logitude, latitude): tms.xlsx)


--special dedicate: this project would not be realized without the collaboration of : Ouissal TAIM, Fatiha EL MAGUI , and Ilham ESSOUSSY.
--
