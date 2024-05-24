hour, minute = map(int, input().split())
time = int(input())

end_hour = (hour + ((minute + time) // 60)) % 24
end_minute = (minute + time) % 60

print(end_hour, end_minute)
