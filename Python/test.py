n = int(input("Enter number of matches: "))
runs = input("Enter runs of matches (separate by space): ")

# Convert input string to a list of integers
lst = list(map(int, runs.split()))

if n == len(lst):
    print(lst)
else:
    while len(lst) < n:
        additional_runs = input(f"Enter runs for match {len(lst)+1}: ")
        # Convert the new input to integers and add it to the list
        lst.extend(map(int, additional_runs.split()))
        # If we have entered enough matches, print the list
        if len(lst) == n:
            print(lst)
            break
