# [initail wear , bought]



[initail_socks , buy_interval] = map(int , input().split())
interval_no =  initail_socks // buy_interval
additional_no = 0 
if(interval_no >= buy_interval):
    additional_no = interval_no // buy_interval
print(initail_socks+interval_no+additional_no)