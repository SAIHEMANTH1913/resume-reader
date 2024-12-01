import os
import re
import PyPDF2

resume_file = input("Enter the full path to your resume file (e.g., C:/Users/YourName/Documents/resume.pdf): ")

if os.path.isfile(resume_file):
    try:
        with open(resume_file, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

            # Regular expression pattern to match skills
            skill_pattern = r"\b(Python|Java|C++|Machine Learning|Data Science|PostgreSQL|AI|SQL|AWS|Azure|DevOps|React|Angular|Vue|JavaScript|CSS|HTML)\b"

            # Find and print skills using regular expressions
            found_skills = set(re.findall(skill_pattern, text))

            print("Found Skills:")
            for skill in found_skills:
                print(skill)

    except Exception as e:
        print(f"Error processing the PDF file: {e}")
else:
    print("Error: File not found or inaccessible.")