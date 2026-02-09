from fpdf import FPDF
from PIL import Image, ImageOps, ImageDraw

# Second part of the CV Generator - User gets asked for education: degree, school name and timeframe
# Create PDF class that sets the format for every new page added
class PDF(FPDF):
    def header(self):
        # Ask user for gender and then generate according template picture with generate_template_portrait() 
        self.generate_template_portrait()
        # Take newly generated portrait after it was resized and cropped by 'def generate_portrait() and place it in the upper left corner
        self.image("/Users/DavidT/Desktop/CS50P2/Final_Project/pictures/cv_picture.png", y = -10, x = ((210/4)/2 - 20))
        # Set font and format for first part of the CV - Personal information (name, birthday, place of birth)
        self.set_font("helvetica", style="BU", size=18)
        self.ln(42)
        self.set_x((210/4)/2 - 10)
        self.cell(20, 20, "Personal Information")
        # Separate personal info & educational info on left hand side of the page from work experience and & language skills on the right side by adding a line in the center of the page
        pdf.set_line_width(1.5)
        self.core_fonts_encoding = "windows-1252"
        self.line(pdf.w/2,297,pdf.w/2, 0)
        # Disable auto generating new page when reaching page limit
        self.set_auto_page_break(False, 20)

    # Method that is used to generate portrait according to gender, which is input by user
    def generate_template_portrait(self):
        while True:
            gender = input("Which template picture should be used? Type 'M' for Male, 'F' for Female or 'N' for no template picture: ").lower().strip()
            try:
                if gender == "m":
                    print("Generating male template picture..")
                    # Calling generate_portrait method (also in PDF class as it all happens once the page gets created)
                    self.generate_portrait(gender)
                    break
                elif gender == "f":
                    print("Generating female template picture..")
                    self.generate_portrait(gender)
                    break
                if gender == "n":
                    print("Generating template picture...")
                    self.generate_portrait(gender)
                    break
                else:
                    # Repeat process if user inputs Invalid Value
                    print("Invalid value.")
                    continue
            except ValueError:
                print("Invalid filetype")
                continue
            except FileNotFoundError:
                print("File not found")
                continue

    # Method that is called by generate_template_portrait to open, resize, crop and paste the portrait to make it circular and save it
    def generate_portrait(self, gender):
        im = Image.open(f"/Users/DavidT/Desktop/CS50P2/Final_Project/pictures/applicant{gender}.png")
        im = ImageOps.fit(im, (220,220))
        mask = Image.new("L", (220,220))
        draw = ImageDraw.Draw(mask)
        draw.ellipse((38,38,180,180), fill=255)
        im.putalpha(mask)
        im.save("/Users/DavidT/Desktop/CS50P2/Final_Project/pictures/cv_picture.png", quality = 95)



# --------------------------------------------------------------------------------------------------------------------------------------------------



# Create object PDF - Once pdf.add_page() is called all the methods in the class FPDF will be called and the newly created page will already contain some text and the portrait
pdf = PDF()

# Create page according to our own settings/format that we declared inside the class
def create_format():
    pdf.set_page_background((249,249,248))
    pdf.add_page()

# Save cv once everything is done
def save_pdf():
    pdf.output("/Users/DavidT/Desktop/CS50P2/Final_Project/cv.pdf")


# --------------------------------------------------------------------------------------------------------------------------------------------------


def generate_personal_information(personal_information):
    pdf.ln(20)
    # Prompts user for personal information so that first chapter of CV Generator can then be created
    for key, value in personal_information.items():
        pdf.set_x(5)
        pdf.set_font("helvetica", style="B", size=15)
        pdf.multi_cell(100,5, key.title() + ": " + value, align="L")
        pdf.set_x(5)
        pdf.ln(10)
    print("Adding data to CV...")
    pdf.ln(10)


# --------------------------------------------------------------------------------------------------------------------------------------------------


def create_educational_header():
    pdf.line(-210, pdf.get_y(),105,pdf.get_y())
    pdf.ln(15)
    # Set font for title 'Education', position the title in the center of the left hand side just below the newly drawn line and personal information chapter
    pdf.set_font("helvetica",style="BU", size=25)
    pdf.set_x((210/4)/2)
    pdf.write(0, "Education")
    pdf.ln(10)

def generate_educational_information(educational_info):
    pdf.set_left_margin(5)
    for i in range(len(educational_info)):
        pdf.set_font("helvetica", style="BU",size=15)
        # Multicell is used - the width of 97 makes sure that the format is respected and the linebreak happens right before the center of the A4 format of the CV
        pdf.multi_cell(100,7, educational_info[f"degree{i}"]["Degree"], align="L", new_x='Left',new_y='NEXT')
        pdf.ln(5)
        pdf.set_font("helvetica",style="I",size=13)
        # Here we suffix a - manually to present the educational information in a nice overview - later we use a more 'pythonic' way to display bullet points
        pdf.multi_cell(97,5, "- " + educational_info[f"degree{i}"]["Name"],align="L", new_x='Left',new_y='NEXT')
        pdf.ln(3)
        pdf.multi_cell(97,5, "- " + educational_info[f"degree{i}"]["Timeframe"],align="L", new_x='Left',new_y='NEXT')
        pdf.ln(5)
        i += 1
        if pdf.get_y() > 270:
            pdf.set_xy(115,15)
            pdf.set_left_margin(120)

# --------------------------------------------------------------------------------------------------------------------------------------------------

            
 
def cursor_position():
    if pdf.get_x() > 100:
        if pdf.get_y() > 260:
            print("Page limit reached. Saving and generating CV...")
            save_pdf()
        else:
            pdf.ln(10)
            pdf.line((pdf.w/2)+1, pdf.get_y(),210,pdf.get_y())
            pdf.ln(10)
            pdf.set_left_margin(110)
            pdf.set_x(130)
            pdf.set_font("helvetica", style="BU",size=18)
            pdf.write(0 ,"Qualifications")
            pdf.ln(10)
    else:
        pdf.set_xy(130,15)
        pdf.set_left_margin(110)
        pdf.set_font("helvetica", style="BU",size=18)
        pdf.write(0 ,"Qualifications")
        pdf.ln(10)
        pdf.set_x(115)


# --------------------------------------------------------------------------------------------------------------------------------------------------



# # Next part of the CV - repositions cursor in top right corner because the right side of the A4 CV will contain language skills and work experience
def generate_language_information(language_information):
    cursor_position()
    pdf.set_font("helvetica", style = "B", size=15)
    pdf.write(6,"Languages: ")
    for i in range(len(language_information)):
        pdf.set_font("helvetica", size=15)
        pdf.multi_cell(60,6, text=f"\u2022 {language_information[f'language{i}']['language']} - {language_information[f'language{i}']['proficiency']}", align="L",new_x='Left',new_y='NEXT')
        if pdf.will_page_break(20) == False:
            continue
        else:
            print("Page limit reached. Saving and generating CV...")
            save_pdf()
    pdf.ln(10)
    pdf.line((pdf.w/2)+1, pdf.get_y(),210,pdf.get_y())
    pdf.ln(4)



# --------------------------------------------------------------------------------------------------------------------------------------------------


# Last function of the program - similar to generate_educational_information this function adds the users work experience
def generate_work_experience(work_experience):
    if pdf.get_y() > 270:
        print("Page limit reached. Saving and generating CV...")
        save_pdf()
    # Add line break
    else:
        pdf.ln(10)
        pdf.set_x(112)
        pdf.set_left_margin(110)
        pdf.set_right_margin(205)
    # Set font for title and then add title called 'Work experience'
        pdf.set_font("helvetica", style="BU", size=20)
        pdf.cell(90, 0, "Work Experience", align="C")
        pdf.ln(10)
    # Loop to add all the work experience so far - user gets asked if there is any work experience that should be added
        for i in range(len(work_experience)):
            pdf.set_font("helvetica",style="B", size=17)
            pdf.multi_cell(95, 10, work_experience[f"work{i}"]["job"], align="C")
            pdf.ln(5)
            pdf.set_font("helvetica", size=15)
            pdf.multi_cell(95, 10, work_experience[f"work{i}"]["company"], align="C")
            pdf.ln(5)
            pdf.multi_cell(95, 10, work_experience[f"work{i}"]["time"], align="C")
            pdf.ln(10)
            if pdf.will_page_break(20) == True:
                print("Page Limit reached. Finishing cv...")
                break
           