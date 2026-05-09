# Career Guidance Expert System

print("===== Career Guidance Expert System =====\n")
print("Answer the following questions with yes or no\n")

science = input("Do you like Science subjects? ").lower()
maths = input("Are you interested in Mathematics? ").lower()
biology = input("Do you like Biology? ").lower()
technology = input("Are you interested in Technology and Computers? ").lower()
medicine = input("Do you want to help people in healthcare? ").lower()
business = input("Are you interested in Business and Management? ").lower()
creativity = input("Do you enjoy creative work like design or art? ").lower()

print("\n===== Recommended Career Stream =====\n")

if science == "yes" and maths == "yes" and technology == "yes":
    print("Recommended Stream: Engineering")
    print("Fields: Computer, Mechanical, Civil, AI, Electronics")

elif science == "yes" and biology == "yes" and medicine == "yes":
    print("Recommended Stream: MBBS")
    print("Career: Doctor, Surgeon, Healthcare")

elif science == "yes" and biology == "yes":
    print("Recommended Stream: Pharmacy / Biotechnology")
    print("Career: Pharmacist, Research, Pharma Industry")

elif business == "yes":
    print("Recommended Stream: BBA / Commerce")
    print("Career: Business, Finance, Management")

elif creativity == "yes":
    print("Recommended Stream: Designing")
    print("Career: UI/UX, Graphic Design, Fashion Design")

else:
    print("Try exploring different career options based on your interests.")

print("\nThank You for using the Expert System")
