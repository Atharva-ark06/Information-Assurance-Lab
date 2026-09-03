# Risk Assessment Calculator

print("===== Risk Assessment Calculator =====")

asset = input("Enter Asset Name: ")
threat = input("Enter Threat Name: ")
vulnerability = input("Enter Vulnerability: ")

print("\nEnter values between 1 and 5")

likelihood = int(input("Likelihood (1-5): "))
impact = int(input("Impact (1-5): "))

risk = likelihood * impact

print("\n------ Risk Assessment Report ------")
print("Asset          :", asset)
print("Threat         :", threat)
print("Vulnerability  :", vulnerability)
print("Likelihood     :", likelihood)
print("Impact         :", impact)
print("Risk Score     :", risk)

if risk <= 5:
    print("Risk Level     : LOW")
elif risk <= 15:
    print("Risk Level     : MEDIUM")
else:
    print("Risk Level     : HIGH")
