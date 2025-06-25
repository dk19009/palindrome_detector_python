import re
from datetime import datetime

# Removes non-alphanumeric characters and converts the string to lowercase.
# Returns True if the cleaned string is equal to its reverse (i.e., a palindrome).
def is_palindrome(text: str) -> bool:
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    return cleaned == cleaned[::-1]

# Main program
def main():
    print(f"🔁 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Palindrome Checker 🔁")
    user_input = input("Enter text: ")
    
    if is_palindrome(user_input):
        print("✅ It's a palindrome!")
    else:
        print("❌ Not a palindrome.")

if __name__ == "__main__":
    main()
