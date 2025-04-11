age_in_days = int(input())

years = age_in_days // 365
remaining_days = age_in_days % 365
months = remaining_days // 30
days = remaining_days % 30

print(f"{years} ano(s)")
print(f"{months} mes(es)")
print(f"{days} dia(s)")
