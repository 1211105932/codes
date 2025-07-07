def bouncing_ball(h, bounce, window):
    ans = 1
    if  h > window > 0 and 0 < bounce < 1:
        while True:
            h *= bounce
            if h > window:
                ans += 2
            else:
                break
        return ans
    return -1