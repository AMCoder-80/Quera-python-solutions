s = 'aalavi' # 11212291827
uniforms = list()

for char in range(len(s)):
    if char != 0 and s[char-1] == s[char]:
        uniforms[-1] += s[char]
    else:
        uniforms.append(s[char])

hashed = str()
for uni in uniforms:
    this_val = str()
    for n in range(len(uni)):
        this_val += str((ord(uni[n]) - 96) * (n+1))
    hashed += this_val

print(hashed == '12121229')