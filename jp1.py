
principal = float(input("Enter the Principal amount: "))
rate = float(input("Enter the Rate of Interest (% per year): "))
time = float(input("Enter the Time (in years): "))

simple_interest = (principal * rate * time) / 100

print(f"\nThe Simple Interest is: {simple_interest}")
