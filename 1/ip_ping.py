import os


domains = ['google.com', 'wikipedia.org', 'yandex.ru', 'nsu.ru', 'youtube.com', '2gis.ru', 'apple.com', 'cian.ru', 'habr.com', 'github.com']
file = open('ping.cvs', 'w')
file.write(',domain,ip,ttl\n')
for number, domain in enumerate(domains):
    command = 'ping ' + domain
    response = os.popen(command).read().split(' ')
    ip = response[10][0:-1]
    ttl = response[14][(response[14].find('=') + 1):(response[14].find('\n'))]
    file.write(str(number+1) + ',' + domain + ',' + ip + ',' + ttl + '\n')

