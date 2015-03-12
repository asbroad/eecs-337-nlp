# Team 3 : Alex Broad, Seth McCammon, Zavier Henry, Taoran Yue

### EECS 337 - Project 1

There are 3 different aspects of this project (all run with Python 2.7 from the project\_01/src/ directory)


 1. The main project which will run and output a .json file to be used in the autograder
      * To run (from the src folder) : 'python main.py'.
      * This file has two parameters that need to be set inside the main.py file, at the top of the file there are 'year' and 'save_filename' strings.  The year can take the value '2013' or '2015' both must be strings.  save_filename can take any name you want and will save the .json file with that name.
 2. The GUI
      * To run (from the src folder) : 'python GUI.py'
      * When it loads up, you will first have to select a year (2013 or 2015). Then you can select an award and press the 'Go' button.
 3. The fun stuff
      * To run (from the src folder) : 'python fun_thing.py'
      * It will ask you for a name, enter the name of an actor/actress that you enjoy and watch it do it's magic!

### EECS 337 - Project 2

For the second project, we used Python 2.7

For non-standard packages, we only used NLTK.  There are a number of easy ways to install this package depending on your OS. [This site](http://www.nltk.org/install.html) explains the options well.

To run the code, the structure of our GitHub repo is the same as Project 1.  All code should be run from the project_02/src/ directory.


 1. The main project which will run and output a .json file with the dishes name
      * To run (from the src folder) : 'python main.py'.
      * This will output a file called '[dishes_name].json'
 2. The GUI
      * To run (from the src folder) : 'python gui.py'
      * All of the parameters of the recipe transformations can be set here and run with the GO button
 3. The autograder
      * To run the autograder (from the src folder) : 'python autograder.py'

In addition to the code, you can find pictoral descriptions of our knowledge base and recipe representation in the main project_02/ directory.

The transformations that are possible are:

  * Transform a recipe to either 'italian' or 'chinese'
  * Transform a recipe to either 'vegetarian' or 'pescatarian'
  * Transform a recipe to either 'low-fat' or 'low-sodium'
  * Transform the number of servings (1x, 2x or 3x of what the recipe calls for)

