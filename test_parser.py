from pyresparser import ResumeParser

data = ResumeParser('my_resume_2.pdf').get_extracted_data()
print(data)
