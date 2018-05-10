#ORDENAMIENTO
"""
Para probar, comentar los codigos que no se desean probar (tanto main como otros algoritmos de ordenamiento)

"""

"""BUBBLESORT"""

# forma 1
# def bubble_sort(list):
#     for i in range(len(list)-1, 0, -1):
#         for j in range(0, i):
#             if list[j] > list[j+1]:
#                 list[j], list[j+1] = list[j+1], list[j]
# forma 2
# def bubble_sort(list):
#     for i in range(0, len(list)-1):
#         for j in range(0,len(list)-1-i):
#             if list[j] > list [j+1]:
#                 list[j], list[j+1] = list[j+1], list[j]

"""INSERTION SORT"""

#forma 1
# def insertion_sort(list):
#     for i in range(1, len(list)):
#         key = list[i]
#         j = i-1
#         while j >= 0 and key < list[j]:
#             list[j+1] = list[j]
#             j -= 1
#         list[j+1] = key

#forma 2
# def insertion_sort(list):
#     for i in range(1,len(list)):
#         for j in range(i-1,0,-1):
#             if list[j] > list[j+1]:
#                 list[j], list[j+1] = list[j+1], list[j]
#             else:
#                 break
#forma 3
def insertion_sort(list):
	for i in range(1, len(list)):
		j = i-1
		while list[j] > list[j+1] and j >= 0:
			list[j], list[j+1] = list[j+1], list[j]
			j -= 1

"""SELECTION SORT"""
def selection_sort(list):
    for i in range(len(list)-1, 0, -1):
        max_number_position = 0
        for j in range(1, i+1):
            if list[j] > list[max_number_position]:
                max_number_position = j
        list[max_number_position], list[i] = list[i], list[max_number_position]



# if __name__=="__main__":
#     list = [49, 91, 11, 39, 98, 66, 24, 70, 3, 16]
#     print list[9]
#     bubble_sort(list)
#     selection_sort(list)
#     merge_sort(list)
#     insertion_sort(list)

#     print(list)