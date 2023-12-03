# animalZooProgram
Final program option for Python Programming

CIT-95 Final Program (Zoo Option) 
youTube presentation of code and working program due December 9, 11:59 PM.
Your final program can be a collaboration of lab partners. You will present your program by creating a youTube video of your code. Use a screen capture program such as Zoom to record your computer screen while you narrate. In order to constrain program scope to class instruction, please limit input to four animals from each of four species (16 animals total).

The following programming concepts must be demonstrated:
-- Clear, Concise, and Correct Code: Program must be written in proper Python programming style.
-- File I/O: Create a file, write to a file, open a file, read from a file, close a file, delete a file, append to a file, etc.
-- Exception Handling: Standard file IO exceptions, Create an exception to handle adding an animal to a habitat that does not have enough room for the new animal.
-- Functions, arrays, and other data structures: Use functions, arrays, and other data structures that you have studied this semester to organize the data read from the input zoo document.
-- Input - File and String Handling: Parse string data from input files. 
-- Output - Formatted Output: Output a report listing the zoo animals with their attributes and their habitats (zooPopulation.txt)
Animals are arriving from zoos around the world and you must assign names, and birth dates, and a new home to each animal. You must organize the animals into species habitats. To accomplish this task, you will write a Python program that:

1) Finds the age, sex, species, color, and weight of each animal from and an input text file (arrivingAnimals.txt)
2) Calculates a birthday based on input data
3) Creates a name for each animal using names collected from a recent community fund raiser (animalNames.txt)
4) Creates a unique ID for each animal to be used in your zoo information system
5) Processes the animals into appropriate habitats.
6) Outputs a report (zooPopulation.txt) containing all zoo animals and their information.
 
Use at least four functions with the following names. These functions must be explained in your youTube presentation. The four functions will be named:
gen_birthday(), gen_animal_ID(), gen_animal_name(), gen_zoo_habitats()

•	Calculate a birthday from the originating zoo information. What will you do if the birth season is unknown?
•	Calculate a unique ID to identify each animal in your zoo.
•	Create an animal name based on input from a community fundraiser (animalNames.txt) 
•	Assign each new animal a habitat. Each species must have its own habitat.

Use fileIO to parse and input the file named arrivingAnimals.txt. Use fileIO to create a report named zooPopulation.txt.  Use arrays, functions, string parsing, and other data structures to organize your zoo.

Information will arrive in the following format (sample files are attached).

4 year old female hyena, born in spring, tan color, 70 pounds, from Friguia Park, Tunisia
12 year old male hyena, born in fall, brown color, 150 pounds, from Friguia Park, Tunisia
4 year old male hyena, born in spring, black color, 120 pounds, from Friguia Park, Tunisia
8 year old female hyena, unknown birth season, black and tan striped color, 105 pounds, from Friguia Park, Tunisia
6 year old female lion, born in spring, tan color, 300 pounds, from Zanzibar, Tanzania

Calculate the following data elements for each animal: Unique animal ID, animal name, birth date, color, weight, origin
Organize species in their own habitat and output in a report similar to:

Hyena Habitat:
Hy01; Kamari; 4 years old; birth date Mar 21, 2018; tan color; female; 70 pounds; from Friguia Park, Tunisia; arrived Sept 27, 2022
Lion Habitat:
Li01; Kiara; 6 years old; birth date Sept 21, 2016; tan color; female; 305 pounds; from Zanzibar, Tanzania; arrived Sept 23, 2022

