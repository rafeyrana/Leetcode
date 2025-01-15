class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = list(zip(position, speed))
        sorted_combined = sorted(combined, key=lambda x: x[0], reverse = True)
        stack = []
        for pos, speed in sorted_combined:
            if not stack:
                stack.append((pos, speed))
            if stack:
                car_ahead_position , car_ahead_speed = stack[-1]
                time_till_arrival_ahead = (target - car_ahead_position) / car_ahead_speed
                time_till_arrival_behind = (target - pos) / speed
                if time_till_arrival_behind > time_till_arrival_ahead:
                    stack.append((pos,speed))
        return len(stack)
                