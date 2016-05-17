import re
for _ in range(int(input())):
    s = input().strip()
    print("Valid" if re.search(r'^[456]\d{3}(-?)\d{4}(\1\d{4}){2}$', s) and not re.search(r'(\d)\1{3}', s.replace('-', '')) else "Invalid")