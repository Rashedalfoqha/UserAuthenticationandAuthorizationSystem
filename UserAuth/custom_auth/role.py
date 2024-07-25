from .models import Role

def create_role(name):
    role = Role(name=name)
    role.save()
    return role

def assign_role_to_user(user, role_name):
    role = Role.objects.get(name=role_name)
    user.role = role
    user.save()