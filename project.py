from cvgenerator import create_format, generate_personal_information, create_educational_header, generate_educational_information, generate_language_information, generate_work_experience, save_pdf

def main():
    create_format()
    personal_information = get_personal_information()
    if validate_personal_information(personal_information) == "y":
        generate_personal_information(personal_information)
    else:
        template_personal_info = {'name': 'XY', 'birthday': 'XY', 'place of birth': 'XY'}
        generate_personal_information(template_personal_info)
    
    create_educational_header()
    educational_information = get_educational_information()
    if validate_educational_information(educational_information) == "y":
        generate_educational_information(educational_information)
    else:
        template_educational_info = {"degree0": {'Degree': 'XY','Name': 'XY','Timeframe': 'XY'}}
        generate_educational_information(template_educational_info)

    language_information = get_language_skills()
    if validate_language_information(language_information) == "y":
        generate_language_information(language_information)
    else:
        template_language_info = {"language0": {'language': 'XY','proficiency': 'native'}}
        generate_language_information(template_language_info)

    
    work_experience = get_work_experience()
    if validate_work_information(work_experience) == "y":
        generate_work_experience(work_experience)
    else:
        template_work_info = {"work0": {'job': 'XY','company': 'Company Name', 'time': '20XX-20YY'}}
        generate_work_experience(template_work_info)

    save_pdf()


# --------------------------------------------------------------------------------------------------------------------------------------------------

def get_personal_information():
    personal_information = {}
    while True:
        print("Enter your name, birthday and place of birth. ")
        name = input("Enter your full name: ").strip().rstrip()
        birthday = input("Enter your birthday: ").strip().rstrip()
        place = input("Enter your place of birth: ").strip().rstrip()
        if name == "" or birthday == "" or place == "":
            choice = input("No data found. Press 'Y' to try again. Press any other button to proceed to the next part. ").lower().strip()
            if choice == 'y':
                continue
            else:
                break
        else:
            personal_information = {'name': name, 'birthday': birthday, 'place of birth': place}
            return personal_information
        


def validate_personal_information(personal_info):
    if personal_info == None:
        print("No personal information found. Adding template information. ")
        return 'n'
    else:
        print("First part of your CV is being generated...")
        return 'y'


# --------------------------------------------------------------------------------------------------------------------------------------------------


def get_educational_information():
    educational_information = {
        "degree0": {
            'Degree': 'XY',
            'Name': 'XY',
            'Timeframe': 'XY'
        }
    }
    i = 0
    while True:
        print("Add your various degrees, school names and the timeframe needed for every degree. ")
        print("Keep the information as short as possible.")
        degree = input("Degree: ")
        schoolname = input("School name: ")
        timeframe = input("Timeframe: ")
        if degree == "" or schoolname == "" or timeframe == "":
            choice = input("No data found. Press 'Y' to try again. Press any other button to proceed to the next part. ").lower().strip()
            if choice == "y":
                continue
            else:
                print("Proceeding to next part...")
                return educational_information
        else:
            print("Adding information...")
            educational_information[f"degree{i}"] = {'Degree': degree, 'Name': schoolname, 'Timeframe': timeframe}
            choice = input("Press 'Y' to add more information. Press any other button to proceed to the next part. ").lower().strip()
            if choice == "y":
                i += 1
                continue
            else:
                return educational_information
            

def validate_educational_information(educational_information):
    if educational_information["degree0"]["Degree"] == "XY":
        print("No information found. Proceeding to next part of CV Generation...")
        return 'n'
    else:
        print("Second part of your CV is being generated...")
        return 'y'
            

# --------------------------------------------------------------------------------------------------------------------------------------------------

def get_language_skills():
    print("First input the language you speak. Then input the according language proficiency.")
    print("A1-Beginner / A2-Elementary / B1-Intermediate / B2-Upper Intermediate / C1-Advanced / C2-Near native")
    language_information = {
        'language0': 
        {
            'language': 'XY',
            'proficiency': 'native'
        }
    }
    i = 0
    while True:
        language = input("Language: ")
        proficiency = input("Proficiency: ")
        if language == "" or proficiency == "":
            choice = input("Missing information. Press 'Y to try again. Press any other button to proceed to the next part.").lower().strip()
            if choice == "y":
                continue
            else:
                print("Proceeding to next part...")
                return language_information
        else:
            print("Adding information..")
            language_information[f"language{i}"] = {'language': language, 'proficiency': proficiency}
            choice = input("Do you want to add more data? Press 'Y' to add more. Press any other button to proceed to the next part. ").lower().strip()
            if choice == "y":
                i += 1
                continue
            else:
                return language_information

def validate_language_information(language_information):
    if language_information["language0"]["language"] == "XY":
        print("No information found. Proceeding to next part of CV Generation...")
        return 'n'
    else:
        print("Third part of your CV is being generated...")
        return 'y'

# --------------------------------------------------------------------------------------------------------------------------------------------------

def get_work_experience():
    print("Now add your work experience. First input the job title, then the company name and lastly the timeframe (start to finish). ")
    work_information = {
        'work0': 
        {
            'job': 'XY',
            'company': 'XY',
            'time': 'XY'
        }
    }
    i = 0
    while True:
        job = input("Work title: ")
        company = input("Company name: ")
        time = input("Timeframe: ")
        if job == "" or company == "" or time == "":
            choice = input("Missing information. Press 'Y to try again. Press any other button to proceed to the next part. ").lower().strip()
            if choice == "y":
                continue
            else:
                print("Finishing cv...")
                return work_information
        else:
            print("Adding information..")
            work_information[f"work{i}"] = {'job': job, 'company': company, 'time': time}
            choice = input("Do you want to add more data? Press 'Y' to add more. Press any other button to proceed to the next part. ").lower().strip()
            if choice == "y":
                i += 1
                continue
            else:
                return work_information

def validate_work_information(work_information):
    if work_information["work0"]["job"] == "XY":
        print("No information found. Finishing CV...")
        return 'n'
    else:
        print("Last part of your CV is being generated...")
        return 'y'

 
if __name__ == "__main__":
    main()