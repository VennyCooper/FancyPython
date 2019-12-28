# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
# (Here, the distance between two points on a plane is the Euclidean distance.)
# You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

# Example 1:
# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

# Example 2:
# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)

# Note:
#     1 <= K <= points.length <= 10000
#     -10000 < points[i][0] < 10000
#     -10000 < points[i][1] < 10000

# Divide and Conquer
class Solution_1:
    import random as rd
    def kClosest(self, points: list, K: int) -> list:
        return self.sort(0, len(points) - 1, K)

    def sort(self, p: list, start, end, K) -> list:
        r = rd.randint(start, end) # index of the pivot
        p[start], p[r] = p[r], p[start] # move the pivot to the start of current partition
        pass

    def partition(self, p: list, start, end) -> int:
        old_start = start
        pivot_dist = self.cal_dist_sq(p[start][0], p[start][1])
        start += 1 # move start(left pointer) to the right by 1
        while True:
            while self.cal_dist_sq(p[start][0], p[start][1]) < pivot_dist:
                start += 1
            while self.cal_dist_sq(p[end][0], p[end][1]) >= pivot_dist:
                end -= 1
            if start >= end:
                break
        # TODO
        p[old_start], []

        pass

    def cal_dist_sq(self, x, y):
        return x**2 + y**2

s = Solution_1()

points = [[1,3],[-2,2]]
K = 1
print(s.kClosest(points, K))

points = [[3,3],[5,-1],[-2,4]]
K=2
print(s.kClosest(points, K))