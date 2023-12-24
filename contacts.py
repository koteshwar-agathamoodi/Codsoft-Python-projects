contacts = []

def add_contact(name, phone, email):
    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    contacts.append(contact)
    print(f"Contact '{name}' added successfully!")

def search_contact(name):
    for contact in contacts:
        if contact['name'] == name:
            print(f"Contact found: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            return
    print(f"No contact found with the name '{name}'.")

def update_contact(name, phone, email):
    for contact in contacts:
        if contact['name'] == name:
            contact['phone'] = phone
            contact['email'] = email
            print(f"Contact '{name}' updated successfully!")
            return
    print(f"No contact found with the name '{name}'.")

def delete_contact(name):
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print(f"Contact '{name}' deleted successfully!")
            return
    print(f"No contact found with the name '{name}'.")
    # Example usage:
add_contact("John Doe", "1234567890", "john@example.com")
add_contact("Jane Smith", "9876543210", "jane@example.com")
search_contact("John Doe")
update_contact("John Doe", "5555555555", "john.doe@example.com")
delete_contact("Jane Smith")
