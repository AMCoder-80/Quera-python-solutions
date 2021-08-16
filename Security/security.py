import re


class Security:
    def encrypt(self, s):
        content = dict()
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

        return hashed

    def is_social_account_info(self, param):
        pattern = r'\b[A-Z][a-z]*:www.[a-z0-9\.]*.com/[\w\d_]*\b'
        if re.search(pattern, param):
            return True
        return False

    def secure(self, info):
        info = info.split()
        pattern = r'/([\w\d_]*$)'
        for data in range(len(info)):
            if self.is_social_account_info(info[data]):
                hashed = self.encrypt(re.findall(pattern, info[data])[0])
                info[data] = re.sub(pattern, '/'+hashed, info[data])
        return ' '.join(info)

# test = Security()
# test.secure('FirstName:Ali, LastName:Alavi, BirthDate:1990/02/02 Gender:male Instagram:www.instagram.com/aalavi Degree:Master Twitter:www.twiter.com/alaviii imdb:www.imdb.com/alavi')