def compound_interest(p,t,r):
    print(f"Enter the principal = {p}")
    print(f"Enter the time period = {t}")
    print(f"Enter the rate = {r}")

    amt = p * (pow((1 + r / 100), t))

    print(f"Amount = {amt}")

    ci = amt - p
    print(f"Compound interest = {ci}")

compound_interest(12000,3,2.6)   