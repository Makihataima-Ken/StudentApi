from django.http import JsonResponse

def get_students(request):
    students = [
        {"id": 1, "name": "Alice", "age": 21, "Major":"Computer Science"},
        {"id": 2, "name": "Bob", "age": 22, "Major":"Engineering"},
        {"id": 3, "name": "Charlie", "age": 20, "Major":"Physics"},
        {"id": 4, "name": "Mani" , "age": 19, "Major":"Computer Science"}
    ]
    return JsonResponse({"students": students})
