class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we only care about the time taken for them to reach target
        # we should look at the cars closest to target first
        # why? so that eerything that could block it already has gone through

        stack = []

        for pos, spd in sorted(zip(position, speed), reverse=True):
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                # this means the time it has its own fleet
                stack.append(time)
        return len(stack)