import Quiz1Class as q


def main():
    # Creating course class instances
    course_1 = q.Course("Advanced Python", 125468, 25, "MIS4322")
    course_2 = q.Course("Database Development", 985474, 40, "MIS4340")

    # Testing Accessor methods
    """
    print("Course 1 title: ", course_1.get_title())
    print("Course 2 CRN: ", course_2.get_crn())
    print("Course 1 capacity: ", course_1.get_capacity())
    print("Course 2 code: ", course_1.get_code())
    """
    # Create dictionary
    course_dict = {
        course_1.get_crn(): course_1.get_capacity(),
        course_2.get_crn(): course_2.get_capacity(),
    }

    # Print out course dictionary
    print("Class Dictionary: CRN: Capacity\n", course_dict)


main()
