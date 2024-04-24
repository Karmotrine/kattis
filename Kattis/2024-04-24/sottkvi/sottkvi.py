friend_count, d_day, today = [int(x) for x in list(input().split())]
birthday = d_day + today
count_going = 0
for i in range(friend_count):
    friend_nthday = int(input())
    finish_quarantine = friend_nthday + 14
    if finish_quarantine <= birthday:
        count_going += 1

print(count_going)