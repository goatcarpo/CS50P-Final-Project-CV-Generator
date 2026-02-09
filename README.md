# Final Project: CV Generator

#### Video Demo: https://youtu.be/bMwCCGnbpfU

#### Description:

This program's goal is to take user's input and then automatically create a one page, A4 formatted CV with the user's information.
The format and design is very basic and input is given through the command-line for now. For now it was my goal to set a foundation for simplifying the process of creating a CV.

## project.py

The whole project is split into two files (+1 for testing). Project.py is the 'main' file, that contains the main() function and all the functions that take the user's input, validate that input and then return it. The resulting CV.pdf itself is split into four parts: 1. Personal Information, 2. Education, 3. Qualifications (in this case, languages specifically) and 4. Work Experience. So every function in the main project file was created to get that information so it can then be added to the CV itself.
The main project.py file has two main tasks:

1. It includes our main() function that calls everything step by step with some simple conditionals to get different results depending if the user inputs any data or not.
2. It includes all the functions to actually get user input. If there isn't any user input, it also contains functions that generate some placeholder data just so showcase the general layout of our CV.
   All the functions that ask for the user's input contain some additional information for the user that gives hints about what information to input. In most cases, the user gets reprompted after adding some data so that the user can decide if there is more information to add or not. All the information is stored in dictionaries, that then get checked by functions that start with the word validate. These validate functions are simple but important because if there was no user input, they fill the dictionary with some template information and return it. If the dictionaries actually contain some user input, the dictionary will be returned just the way it is. From there the dictionaries are used as arguments for our generate function inside main(). These generate functions have the task of looping through these dictionaries and adding the information to our CV PDF step by step. That brings us to the second file, cvgenerator.py.

## cvgenerator.py

As mentioned this file contains everything that actually creates the CV. For every part of the CV (Personal info, education,...) there is a function in this file that will take the input after it has been validated and will loop through that data with the result of it being added to the CV in a specific format. So for example, in the first part of the program the user is asked to input a name, birthday and place of birth. If the user actually inputs data, the next step is adding said data to our CV. For that, the function 'generate_personal_information', which is located in this file (cvgenerator.py), is imported to our main project.py file and called from the main() after the input has been checked. If the user didn't add any data, placeholder information is added to our CV. The reason why I decided to split my final project into two parts is to have better organized code while working on it. This file makes heavy use of the FPDF library. The first part is creating a PDF class, which contains all the necessary parameters and methods to set the format of our .pdf. Here, the template picture, titles and lines for our general layout are added. Once the Object itself is actually created and pdf.add_page() is called, the PDF gets created. Then, all the functions add the information to the pdf until there is no more data to be added. I would love to limit what the user can and cannot input based on the space left on the A4 page but for now the user can potentially input infinite data. The program contains a couple of checks that stop the program once the bottom of page is reached but those checks don't work they way I would like them to, for now. In addition, there is also a function called cursor_position in the cvgenerator file that resets the position and sets margins based on the current position of the cursor.

## test_project.py

This file contains all the tests that are run with pytest. The only functions being tested are the validate_functions because although the functions and tests seem pretty simple, they still play an important role for our whole project. According to the dictionaries they receive, the validate_functions have the task to either return a template dictionary if no data was found in the given dictionary or return the data that was input by the user. This was implemented to showcase the general layout and formatting of the CV even if the user decides to not input any data at all (which would be weird considering everyone has a name, birthday or should at least speak one language :D)

## applicantf.png, applicantm.png, applicantn.png, cv_picture.png

applicantf.png, applicantm.png, applicantn.png are the three template pictures that can be chosen when creating the CV. I would like to let the user upload own pictures in the future, but for now we only work with these template pictures until I learn how to actually let the user upload files.
The cv_picture.png is created once the user has selected a gender/or no gender for the template portrait and add_page() is run. cv_picture is just one of the template pictures, resized and cropped so that is displayed with a circular frame in the upper left corner of the CV. The whole process of resizing and cropping happens inside the PDF class, so once the object is created the user can select a template portrait and it will be resized, cropped and added to the CV.

## cv.pdf

This file is created once everything is done. The last function that is called in our main() function is called save_pdf() and this is exactly where this process happens. I wish to implement a way to limit what the user actually can or cannot input to let the user know once the page is almost full. Although I have some small checks here and there, if someone really wishes to add thousands of lines, the resulting CV is a complete mess because much of the data is added before those checks even happen. That is something I want to work on in the future but for now I just expect users to respect the formating and given rules (which is not realistic I know :D).
