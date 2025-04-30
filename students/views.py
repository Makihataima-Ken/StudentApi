from django.http import JsonResponse

def get_students(request):
    students = [
        {"id": 1, "name": "Alice", "age": 21},
        {"id": 2, "name": "Bob", "age": 22},
        {"id": 3, "name": "Charlie", "age": 20},
        {"id": 4, "name": "Mani" , "age": 19}
    ]
    return JsonResponse({"students": students})
