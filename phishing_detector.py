from modules.url_checker import analyze_url
from modules.email_checker import analyze_email
from modules.risk_scoring import display_results

def main():

    while True:
        print("\n===== PHISHING DETECTOR =====")
        print("1. Analyze URL")
        print("2. Analyze Email")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            url = input("Enter URL: ")
            score, reasons = analyze_url(url)
            display_results(score, reasons)

        elif choice == "2":
            email = input("Paste Email Text:\n")
            score, reasons = analyze_email(email)
            display_results(score, reasons)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()