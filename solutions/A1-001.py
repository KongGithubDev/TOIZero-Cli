import sys

def main():
    # Read all input at once
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    
    fname = input_data[0]
    lname = input_data[1]
    
    # Requirement: Hello [Firstname] [Lastname]
    # Requirement: [First 2 chars of Firstname][First 2 chars of Lastname]
    print(f"Hello {fname} {lname}")
    print(f"{fname[:2]}{lname[:2]}")

if __name__ == "__main__":
    main()
