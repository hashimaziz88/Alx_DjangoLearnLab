# Managing Permissions and Groups in Django

## Overview
This application demonstrates the use of Django's built-in permissions and groups to control access to different parts of the application. Permissions are assigned to user groups, which then govern the actions users can perform.

## Custom Permissions
The `Book` model has the following custom permissions defined in `models.py`:
- `can_view`: Allows viewing of books.
- `can_create`: Allows creating new books.
- `can_edit`: Allows editing existing books.
- `can_delete`: Allows deleting books.

## Groups
The following groups have been set up with their respective permissions:
- **Viewers:** Can view books.
- **Editors:** Can view, create, and edit books.
- **Admins:** Can view, create, edit, and delete books.

## Enforcing Permissions
The views in `views.py` enforce these permissions using Django's `permission_required` decorator. This ensures that only users with the appropriate permissions can perform certain actions.

## Testing
To test the permissions:
1. Log in as a user in the `Viewers`, `Editors`, or `Admins` group.
2. Attempt to view, create, edit, or delete books as per the group’s permissions.

## Conclusion
This setup provides a robust system for managing user access in Django, ensuring that only authorized users can perform specific actions.
