

# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LL(object):
#     def __init__(self):
#         self.head = None
#         self.count = 0

#     def add_node(self, data, position):
#         if position > self.count:
#             return 'Position is greater than length of the list.'

#         node = Node(data)
#         if position == 0:
#             node.next = self.head
#             self.head = node

#         elif position == self.count:
#             temp = self.head
#             while temp.next is not None:
#                 temp = temp.next
#             temp.next = node

#         else:
#             prev, current = self.head, self.head.next
#             for i in xrange(1, position):
#                 prev = current
#                 current = current.next

#             prev.next = node
#             node.next = current

#         self.count += 1

#     def delete_node(self, position):
#         if position > self.count:
#             return 'Position is greater than length of the list.'

#         if position < 0:
#             return 'Position is less than 0.'

#         if position == 0:
#             self.head = self.head.next
#         else:
#             prev, current = self.head, self.head.next
#             for i in xrange(1, position):
#                 prev = current
#                 current = current.next

#             if position == self.count:
#                 prev.next = None
#             else:
#                 prev.next = current.next

#         self.count -= 1

#     def search_node(self, value):
#         temp = head
#         position = 0
#         while temp is not None:
#             if temp.data == value:
#                 return position
#             position += 1
#         return False

#     def traverse(self):
#         temp = self.head
#         while temp is not None:
#             print temp.data, '->',
#             temp = temp.next

#     def reverse(self):
#         prev, current = None, self.head

#         while current is not None:
#             next = current.next
#             current.next = prev
#             prev = current
#             current = next

#         self.head = prev

# ll = LL()
# ll.add_node(1, 0)
# ll.add_node(2, 1)
# ll.add_node(3, 2)
# ll.add_node(4, 3)
# ll.add_node(5, 4)
# ll.add_node(6, 5)
# ll.add_node(7, 6)
# ll.add_node(8, 7)
# ll.add_node(8, 4)
# ll.traverse()
# ll.reverse()
# print '\n'
# ll.traverse()



# # Python program for implementation of Quicksort Sort
 
# # This function takes last element as pivot, places
# # the pivot element at its correct position in sorted
# # array, and places all smaller (smaller than pivot)
# # to left of pivot and all greater elements to right
# # of pivot
# def partition(arr,low,high):
#     i = ( low-1 )         # index of smaller element
#     pivot = arr[high]     # pivot
#     for j in range(low , high):
#         # If current element is smaller than or
#         # equal to pivot
#         if   arr[j] <= pivot:
#             # increment index of smaller element
#             i = i+1
#             arr[i],arr[j] = arr[j],arr[i]
#     arr[i+1],arr[high] = arr[high],arr[i+1]
#     return ( i+1 )
 
# # The main function that implements QuickSort
# # arr[] --> Array to be sorted,
# # low  --> Starting index,
# # high  --> Ending index
 
# # Function to do Quick sort
# def quickSort(arr,low,high):
#     if low < high:
 
#         # pi is partitioning index, arr[p] is now
#         # at right place
#         pi = partition(arr,low,high)
 
#         # Separately sort elements before
#         # partition and after partition
#         quickSort(arr, low, pi-1)
#         quickSort(arr, pi+1, high)
 
# # Driver code to test above
# arr = [10, 7, 8, 9, 1, 5]
# n = len(arr)
# print arr
# quickSort(arr,0,n-1)
# print ("Sorted array is:")
# for i in range(n):
#     print ("%d" %arr[i]),



n = 25







