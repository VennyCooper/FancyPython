class Sorting:

    def bubble_sort(self, items: list, desc = False) -> list:
        items_len = len(items)
        if items_len <= 1:
            return items
        has_sorted = True
        for i in range(items_len):
            for j in range(1, items_len - i):
                if items[j - 1] > items[j]:
                    items[j - 1], items[j] = items[j], items[j - 1]
                    has_sorted = False
            if has_sorted:
                break
        if desc:
            items.reverse()
        return items


    def selection_sort(self, items: list) -> list:
        items_len = len(items)
        if items_len <= 1:
            return items
        for i in range(items_len):
            min_index = i
            for j in range(i + 1, items_len):
                if items[j] < items[min_index]:
                    min_index = j
            items[i], items[min_index] = items[min_index], items[i]
        return items


    def insertion_sort(self, items: list) -> list:
        items_len = len(items)
        if items_len <= 1:
            return items
        for i in range(1, items_len):
            j = i
            while j > 0:
                if items[j - 1] < items[j]:
                    break
                items[j - 1], items[j] = items[j], items[j - 1]
                j -= 1
        return items


    def merge_sort(self, items: list) -> list:
        # T(n/2) + n
        def _divide(sub_items: list) -> list:
            sub_items_len = len(sub_items)
            if sub_items_len <= 1:
                return sub_items
            ###########################################
            # optimization: if the length sub-list is not larger than a defined length n
            # we use insertion sort to save save time and space
            # in Python, sorted is achieved by hybrid sort (merge sort + insertion sort)
            ###########################################
            # if sub_items_len <= n:
            #     return self.insertion_sort(sub_items)
            ###########################################
            mid = sub_items_len // 2
            return _merge(_divide(sub_items[:mid]), _divide(sub_items[mid:]))
        # O(n)
        # merge two ordered sub-list to one ordered list
        # e.g. left = [1,3,4], right = [2,6,7,10]
        def _merge(left: list, right: list) -> list:
            ###########################################
            # optimization: max of left list is not larger than min of right list
            # e.g. left = [1,3,4], right = [5,8,10]
            ###########################################
            if left[-1] <= right[0]:
                return left + right
            ###########################################
            result = []
            while len(left) > 0 and len(right) > 0:
                if left[0] > right[0]:
                    result.append(right[0])
                    right.remove(right[0])
                else:
                    result.append(left[0])
                    left.remove(left[0])
            if len(left) > 0:
                result += left
            if len(right) > 0:
                result += right
            return result
        # T(n) = 2T(n/2) + n = nlogn
        return _divide(items)


    def quick_sort(self, items: list) -> list:
        pass

    def partition(self, items: list) -> list:
        items_len = len(items)
        pivot = 0
        i = 1
        j = items_len - 1
        while i < j:
            if items[i] > items[pivot]:
                while items[j] > items[pivot]:
                    j -= 1
                if i >= j:
                    break
                items[i], items[j] = items[j], items[i]
            i += 1
        items[i - 1], items[pivot] = items[pivot], items[i - 1]
        return items


a = [9,21,5,13,55,2,12,1]
s = Sorting()
print(s.partition(a))

