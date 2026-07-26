class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = []
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)

        for p, s in cars:
            time = (target - p)/s
            if res and res[-1] >= time:
                continue
            else:
                res.append(time)
        return len(res)