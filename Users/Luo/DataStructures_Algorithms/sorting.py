class Sorting:
   def bubble_sort(self, items: list) -> list:
      items_len = len(items)
      for i in range(items_len - 1):
         for j in range(items_len - i - 1):
            if items[j] > items[j + 1]:
               items[j], items[j + 1] = items[j + 1], items[j]
      return items

   def selection_sort(self, items: list) -> list:
      items_len = len(items)
      for i in range(items_len - 1):
         min_index = i
         for j in range(i + 1, items_len):
            if items[j] < items[min_index]:
               min_index = j
         items[i], items[min_index] = items[min_index], items[i]
      return items


a = [21,5,13,55,2,12,1]
s = Sorting()
print(s.bubble_sort(a))

