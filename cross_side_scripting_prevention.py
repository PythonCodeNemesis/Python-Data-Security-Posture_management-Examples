import html
# Sanitize user input to prevent XSS attacks
def sanitize_user_input(user_input):
   sanitized_input = html.escape(user_input)
   return sanitized_input
# Usage example
user_input = input("Enter some user-generated content: ")
sanitized_input = sanitize_user_input(user_input)
print("Sanitized content:", sanitized_input)
