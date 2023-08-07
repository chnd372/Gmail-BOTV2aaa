try:
    with open(r'/storage/9C33-6BBD/Download/Gmail-BOTV2aaa-main/proxies.txt', 'r') as file:
        proxy = [line.rstrip() for line in file.readlines()]
except FileNotFoundError:
    raise Exception('proxies.txt tidak ada.')
