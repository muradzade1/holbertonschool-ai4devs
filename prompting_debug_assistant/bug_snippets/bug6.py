def countdown(n):
    if n > 0:
        print(n)
        return countdown(n)
    else:
        print("Done!")

countdown(5)
