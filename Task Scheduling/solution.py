class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        x = max(cnt.values())
        idle = (x - 1) * (n + 1)
        s = sum(v == x for v in cnt.values())
        return max(len(tasks), idle + s)