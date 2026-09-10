class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        # cars = [(10,2), (8,4), (0,1), (5,1), (3,3)]

        cars.sort(reverse=True)

        stack = []

        for pos, spd in cars:
            distance = target - pos
            time = distance / spd

            if len(stack) == 0:
                stack.append(time)
                continue
            
            fleet_ahead = stack[-1]

            if time > fleet_ahead:
                stack.append(time)
            else:
                pass

        return len(stack)
