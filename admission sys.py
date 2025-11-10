age = int(input("Enter the age: "))

if age >= 18 and age <= 25:          # all statements under the if block
    print("✅ Welcome! Student is eligible.")
    student = input("Enter the student's name: ")
    marks = int(input("Enter the student's marks: "))

    if marks >= 80 and marks <= 100:
        print("🎉 Admission without donation 👍")

    elif marks >= 65 and marks < 80:
        print("💰 Pay ₹1,00,000 donation and take the admission.")
        print("🏫 Criteria of Vidya Pratishthan Baramati College.")

    elif marks >= 50 and marks <= 64:
        print("💰 Pay ₹2,00,000 donation and take the admission.")
        print("🏫 Criteria of Vidya Pratishthan Baramati College.")

    elif marks >= 35 and marks <= 49:
        print("💰 Pay ₹4,00,000 donation and take the admission.")
        print("🏫 Criteria of Vidya Pratishthan Baramati College.")

    else:
        print("❌ Fail . Student does not fit in this criteria.")
    
else:
    print("⚠️  Age does not match 🥲!")
