# Career Guidance Expert System


print("======================================")
print("     Career Guidance Expert System")
print("======================================\n")

name = input("Enter your name: ")

tenth = float(input("Enter your 10th Percentage: "))
twelfth = float(input("Enter your 12th Percentage: "))

print("\nChoose your stream:")
print("1. PCM")
print("2. PCB")
print("3. PCMB")

stream = input("Enter choice (PCM/PCB/PCMB): ").upper()

print("\nAnswer the following questions with yes or no\n")

maths = input("Do you like Mathematics? ").lower()
biology = input("Do you like Biology? ").lower()
technology = input("Are you interested in Technology and Computers? ").lower()
machines = input("Do you like machines and automobiles? ").lower()
construction = input("Are you interested in buildings and construction? ").lower()
medicine = input("Do you want to help people in healthcare? ").lower()
research = input("Are you interested in medical research and medicines? ").lower()

print("\n======================================")
print("      Career Recommendation")
print("======================================\n")

print("Student Name:", name)
print("10th Percentage:", tenth)
print("12th Percentage:", twelfth)
print("Selected Stream:", stream)

# PCM Students
if stream == "PCM":
    if technology == "yes":
        print("\nRecommended Career: Computer Engineering / IT")
        print("Fields: Software Development, AI, Cybersecurity, Data Science")

    elif machines == "yes":
        print("\nRecommended Career: Mechanical Engineering")
        print("Fields: Automobile, Manufacturing, Robotics")

    elif construction == "yes":
        print("\nRecommended Career: Civil Engineering")
        print("Fields: Construction, Architecture, Infrastructure")

    elif maths == "yes":
        print("\nRecommended Career: Engineering")
        print("Fields: Electronics, Electrical, Aerospace")

    else:
        print("\nYou can explore Diploma or General Science fields.")

# PCB Students
elif stream == "PCB":
    if medicine == "yes":
        print("\nRecommended Career: MBBS")
        print("Career: Doctor, Surgeon, Healthcare")

    elif research == "yes":
        print("\nRecommended Career: Pharmacy / Biotechnology")
        print("Career: Pharmacist, Medical Research, Pharma Industry")

    elif biology == "yes":
        print("\nRecommended Career: B.Sc Biology / Microbiology")
        print("Career: Research, Lab Specialist")

    else:
        print("\nYou can explore Allied Health Sciences.")

# PCMB Students
elif stream == "PCMB":
    if technology == "yes":
        print("\nRecommended Career: Computer Engineering")
        print("Fields: AI, Software, Data Science")

    elif medicine == "yes":
        print("\nRecommended Career: MBBS")
        print("Career: Doctor, Healthcare")

    elif research == "yes":
        print("\nRecommended Career: Biotechnology")
        print("Career: Genetics, Pharma Research")

    elif machines == "yes":
        print("\nRecommended Career: Mechanical Engineering")
        print("Fields: Automobile, Robotics")

    else:
        print("\nYou have multiple career options in Engineering and Medical fields.")

else:
    print("\nInvalid Stream Selection")

print("\n======================================")
print("Thank You for using the Expert System")
print("======================================")
