from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET", "POST"])
def getTodoList(request):
    if request.method == "GET":
        # Retrieve and return a list of all to-do items
        pass

    else:
        # Create a new to-do item
        pass


@api_view(["GET", "PUT", "DELETE"])
def getTodoTask(request, id):
    if request.method == "GET":
        # Retrieve and return a single to-do item by ID
        pass

    elif request.method == "POST":
        # Update an existing to-do item by ID
        pass

    else:
        # Delete a to-do item by ID
        pass


@api_view(["POST"])
def completedTask(request):
    # Mark a to-do item completed
    pass
