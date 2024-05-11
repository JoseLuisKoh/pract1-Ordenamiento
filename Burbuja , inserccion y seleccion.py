



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


print("Bienvenido al programa de ordenamiento de números.")
numbers = input("Por favor, ingresa una lista de números separados por espacios: ")
numbers_list = [int(num) for num in numbers.split()]

print("\nElige el método de ordenamiento que deseas aplicar:")
print("1. Burbuja")
print("2. Inserción")
print("3. Selección")
choice = int(input("Ingrese el número correspondiente al método de ordenamiento: "))

if choice == 1:
    bubble_sort(numbers_list)
    print("\nLista ordenada usando Burbuja:")
    print(numbers_list)
elif choice == 2:
    insertion_sort(numbers_list)
    print("\nLista ordenada usando Inserción:")
    print(numbers_list)
elif choice == 3:
    selection_sort(numbers_list)
    print("\nLista ordenada usando Selección:")
    print(numbers_list)
else:
    print("\nOpción no válida. Por favor, elija un número entre 1 y 3.")
