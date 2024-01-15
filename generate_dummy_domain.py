import string
from itertools import product, islice
import os

# 生成隨機的字母和數字
letters_and_digits = string.ascii_letters + string.digits
letters_and_digits_len = len(list(letters_and_digits))

if __name__ == '__main__':        
    dummy_domains = product(list(letters_and_digits), repeat=4)  # 可重複的排序
    
    one_file_domain_len = 1000000
    i = 1
    while True:
        one_file_domain = islice(dummy_domains, one_file_domain_len)
        file_path = f'dummydomainname{i}.txt'
        with open(file_path, 'w', encoding='utf-8') as f:
            for domain in one_file_domain:
                f.write(''.join(domain) + '.dummydomainname.com\n')
        
        file_size = os.stat(file_path).st_size
        if file_size == 0:
            os.remove(file_path)
            break
        
        print(f'file {file_path} generated, {file_size / 1024 / 1024} MB.')
        i += 1
                