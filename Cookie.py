""" Cookie Clicker """
def main():
    """ greedy? """
    total_time = 0
    cookie_per_sec = 2
    price = float(input())
    extra = float(input())
    target = float(input())
    while 1:
    	# Time calculate by current cookie per sec
        normal_way = target/cookie_per_sec

        # Price / Cookie per sec for calculate how long time to buy extra rate and plus the (target / cookie per sec + extra) to find if buy extra cookie rate, how long time to take (This is another way)?
        another_way = (price/cookie_per_sec) + target/(cookie_per_sec+extra)

    	# if the another_way take time less than normal way and target is more than price to buy an extra rate (If a price is more than target, It shouldn't buy)
        if another_way < normal_way and price < target:

        	# Buy an extra rate
            total_time += price/cookie_per_sec # Waiting for cookie is enough to buy an extra rate (Take time).
            cookie_per_sec += extra
        else:
            break
    total_time = total_time + target/cookie_per_sec
    print("%.04f" %total_time)
 
main()