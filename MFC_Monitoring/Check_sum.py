def check_sum(data):    
    x = '0000 0010' # 82    command #1 사용 시 02로 변경
    for i in range(0, len(data)):
        check_sum = ""
        for j in range(0,9):
            if data[i][j] == ' ':
                check_sum += ' ' 
            elif data[i][j] == x[j]:
                check_sum += '0'
            else:
                check_sum += '1'
        x = check_sum
    print('Check Sum : {}'.format(check_sum))

if __name__ == '__main__':    

    # device s/n : 02400802
    tag_name_02400802 = ['1000 0000',    # 80
                        '0000 1011',    # 0B
                        '0000 0110',    # 06
                        '1100 0011',    # C3
                        '0010 1101',    # 2D
                        '0011 0000',    # 30
                        '1100 0011',    # C3
                        '1000 1100',    # 8C
                        '0011 0010']    # 32
    
    # device s/n : 13701001
    tag_name_13701001 = ['1000 0000',    # 80
                        '0000 1011',    # 0B
                        '0000 0110',    # 06
                        '1100 0111',    # C7
                        '0011 1101',    # 3D
                        '1111 0000',    # F0
                        '1100 0111',    # C7
                        '0000 1100',    # 0C
                        '0011 0001']    # 31
    
    # device s/n : 01800251    
    tag_name_01800251 = ['1000 0000',    # 80
                        '0000 1011',    # 0B
                        '0000 0110',    # 06
                        '1100 0011',    # C3
                        '0001 1110',    # 1E
                        '0011 0000',    # 30
                        '1100 0011',    # C3
                        '0010 1101',    # 2D
                        '0111 0001']    # 71
    # read flow
    w_01_02400802 = ['1000 1010', # 8A
                    '0110 0100', # 64
                    '0010 0100', # 24
                    '1010 0010', # A2
                    '0010 0010', # 22
                    '0000 0001', # 01
                    '0000 0000'] # 00

    w_01_13701001 = ['0000 1010', # 0A
                    '0110 0100', # 64
                    '1101 0001', # D1
                    '0000 1111', # 0F
                    '1000 1001', # 89
                    '0000 0001', # 01
                    '0000 0000'] # 00

    w_01_01800251 = ['1000 1010', # 8A
                    '0110 0100', # 64
                    '0001 1011', # 1B
                    '0111 1000', # 78
                    '0011 1011', # 3B
                    '0000 0001', # 01
                    '0000 0000'] # 00
    # set point
    w_236_02400802 = ['1000 1010', # 8A
                    '0110 0100', # 64
                    '0010 0100', # 24
                    '1010 0010', # A2
                    '0010 0010', # 22
                    '1110 1100', # EC
                    '0000 0101', # 05
                    '0011 1001', # 39
                    '0100 0010', # 42
                    '1100 1000', # C8
                    '0000 0000', # 00 
                    '0000 0000'] # 00    
        
    w_236_13701001 = ['0000 1010', # 0A
                    '0110 0100', # 64
                    '1101 0001', # D1
                    '0000 1111', # 0F
                    '1000 1001', # 89
                    '1110 1100', # EC
                    '0000 0101', # 05
                    '0011 1001', # 39
                    '0100 0010', # 42
                    '1100 1000', # C8
                    '0000 0000', # 00 
                    '0000 0000'] # 00
    
    w_236_01800251 = ['1000 1010', # 8A Address
                    '0110 0100', # 64
                    '0001 1011', # 1B
                    '0111 1000', # 78
                    '0011 1011', # 3B
                    '1110 1100', # EC
                    '0000 0101', # 05 Byte count
                    '0011 1001', # 39 unit code percent
                    '0100 0010', # 42 IEEE 754 floating
                    '1100 1000', # C8
                    '0000 0000', # 00 
                    '0000 0000'] # 00

    check_sum(tag_name_02400802)

    # 0100 0010 1100 1000 0000 0000 0000 0000 IEEE 100
    # 62C8 0000 0000

# 0 : 0000
# 1 : 0001
# 2 : 0010
# 3 : 0011
# 4 : 0100
# 5 : 0101
# 6 : 0110
# 7 : 0111
# 8 : 1000
# 9 : 1001
# A : 1010
# B : 1011
# C : 1100
# D : 1101
# E : 1110
# F : 1111