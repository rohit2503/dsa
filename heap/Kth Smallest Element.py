import heapq

class KthSmallestElement:
    """
    This class provides a method to find the k-th smallest element in an unsorted array using a min-heap.
    """
    @staticmethod
    def find_kth_smallest_using_min_heap(arr, k):
        """
        Finds the k-th smallest element in the given array.

        :param arr: List[int] - The input array
        :param k: int - The k-th position to find the smallest element
        :return: int - The k-th smallest element
        """
        if k <= 0 or k > len(arr):
            raise ValueError("k must be between 1 and the length of the array")

        # Create a min-heap from the array
        min_heap = arr[:]
        heapq.heapify(min_heap)

        # Extract the minimum element k-1 times
        for _ in range(k - 1):
            heapq.heappop(min_heap)

        # The k-th smallest element is now at the root of the heap
        return heapq.heappop(min_heap)


