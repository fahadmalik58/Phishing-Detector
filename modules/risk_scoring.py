def classify(score):

    if score <= 30:
        return "SAFE"

    elif score <= 70:
        return "SUSPICIOUS"

    else:
        return "PHISHING"


def display_results(score, reasons):

    print("\n===== RESULTS =====")

    print(f"Risk Score: {score}/100")
    print(f"Classification: {classify(score)}")

    print("\nReasons:")

    if reasons:
        for reason in reasons:
            print("-", reason)
    else:
        print("No suspicious indicators detected.")