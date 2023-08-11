import random
# a list of 1~33
num_pick=int(input('How much tickets you want to purchase?\n'))
red_pool=range(1,34)
blue_pool=range(1,17)
num_winred=random.sample(red_pool,6)
num_winblue=random.sample(blue_pool,1)
print('the winning numbers are red '+str(num_winred)+' blue '+str(num_winblue))
count_win=0
count_lose=0
ticket_price=2
total_price=0
win_price=0
for num_count in range(num_pick):
    red = random.sample(red_pool, 6)
    blue = random.sample(blue_pool, 1)
    total_price+=ticket_price
    if blue==num_winblue:
        count_win+=1
        win_price+=1000
    else:
        count_lose+=1
        total_price+=2
print('If you purchase %d tickets, the chance to lose is %.1f'%(num_pick,count_lose/num_pick*100)+'%')
if win_price>=total_price:
    print('If you purchase %d tickets, you will win $%d in estimation'%(num_pick,win_price-total_price))
else:
    print('If you purchase %d tickets, you will lose $%d in estimation'%(num_pick,total_price-win_price))
