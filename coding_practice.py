# Ask user for their name can add methods to variable to reduce lines of code
name = input("What's your name? ").strip().title()

# Say hello to user
# 1 argument concatenation have to add space
# print("hello, " + name)

# 2 arguments below don't need to add space after 1st argument
print("Hello,", name)

# Remove whitespace from str and can add capitalize user's name
name = name.strip().title()

# Capitalize user's name. Only first letter.
name = name.capitalize()

# Capitalize each first letter of the word
name = name.title()
