class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # so each hour we can eat k bananas and if we finish before an hour we will just stay there and move on to the next pile in the next hour
        # so the max number of bananas we can eat in each hour should be teh maximum number of bananas in the piles because why else would we waste time waiting for next one irght
        # this would be the minimum after which eating more bananas per hour becomes useless
        # now we have to eat it in h hours, how can we check if the banana eating rate will finish in h hours (write a function for this first)


        def kokoCanEatInK(k, h):
            # find the number of hours taken to eat all the piles at the rate of k per hour
            hours = 0 
            for pile in piles:
                hours += math.ceil(pile / k) # since we cannot move on after eating in less than the given amount we will take the ceil for it
            
            return hours <= h

        max_bananas = max(piles)
        min_eating_rate = max_bananas
        # since this is running in an ordered way what if we replace this part with a binary search
        # at each point we can check for the mid to be eatable or not, if it is then we can continue searching for the min on the this side or else we search for the other sode
        # since we are making a search in a defined range we should be able to reduce the search space by half everytime because of the ordering


        # the range for this search will be from 1... max_bananas - now should we do this in reverse or the right way
        l ,r = 1 , max_bananas
        while l <= r:
            mid = l + (r - l) // 2
            if kokoCanEatInK(mid, h): # if the banana pile is eatable in the mid rate we can go lower
                min_eating_rate = mid
                r = mid - 1
            else:
                l = mid + 1
        return min_eating_rate



        # for rate in range(max_bananas, 0, -1): 
        #     if kokoCanEatInK(rate, h):
        #         min_eating_rate = rate
        # return min_eating_rate


        # we are running a for loop on this which is really inefficient hm. what else can we do for this
