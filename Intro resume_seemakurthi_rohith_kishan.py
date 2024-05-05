class Person:
    def __init__(self, name):
        self.name = name

class Education:
    def __init__(self, school, year):
        self.school = school
        self.year = year

if __name__ == "__main__":
    name = "Seemakurthi Rohith Kishan"
    school_1 = Education("Narayana Concept School", 2016)
    school_2 = Education("Narayana Junior College", 2018)
    school_3 = Education("Presidency University", 2022)
    hobbies = ["watching movies", "playing badminton", "editing videos", "reading novels"]
    email = "seemakurthiKishan@gmail.com"
    contact_number = "+91 7794879128"
    instagram_id = "Rohith rama"
    facebook_id = "Rohith Seemakurthi"

    print("=====================================")
    print("             RESUME                  ")
    print("=====================================")
    print("Name:", name)
    print("\nEducational Background:")
    print("- {} in the year {}".format(school_1.school, school_1.year))
    print("- {} in the year {}".format(school_2.school, school_2.year))
    print("- {} in the year {}".format(school_3.school, school_3.year))
    print("\nHobbies:", ', '.join(hobbies))
    print("\nContact Details:")
    print("- Mail Id:", email)
    print("- Contact Number:", contact_number)
    print("\nSocial Media:")
    print("- Instagram ID:", instagram_id)
    print("- Facebook ID:", facebook_id)
    print("=====================================")
