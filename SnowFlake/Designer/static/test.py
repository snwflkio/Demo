# Generates file in root directory of project (where manage.py is)
def generate_test():
    f = open('files/test.txt', 'w')
    f.write('Test')
    f.close()
generate_test()
