low_nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
teens = ['elevin', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty-', 'thirty-', 'forty-', 'fifty-', 'sixty-', 'seventy-', 'eighty-', 'ninety-']


def spell():
    while True:
        x = int(input('Give me a number to spell out: '))
        
        if x > 0 and x <= 10:
            print('Here is your number spelled out:',low_nums[x])
        elif x > 10 and x < 20:
            print('Here is your number spelled out:',teens[x - 11])
        elif x >= 20 and x < 30:
            print(f'Here is your number spelled out: {tens[0]}{low_nums[x - 20]}')
        elif x >= 30 and x < 40:
            print(f'Here is your number spelled out: {tens[1]}{low_nums[x - 30]}')
        elif x >= 40 and x < 50:
            print(f'Here is your number spelled out: {tens[2]}{low_nums[x - 40]}')
        elif x >= 50 and x < 60:
            print(f'Here is your number spelled out: {tens[3]}{low_nums[x - 50]}')
        elif x >= 60 and x < 70:
            print(f'Here is your number spelled out: {tens[4]}{low_nums[x - 60]}')
        elif x >= 70 and x < 80:
            print(f'Here is your number spelled out: {tens[5]}{low_nums[x - 70]}')
        elif x >= 80 and x < 90:
            print(f'Here is your number spelled out: {tens[6]}{low_nums[x - 80]}')
        elif x >= 90 and x < 100:
            print(f'Here is your number spelled out: {tens[7]}{low_nums[x - 90]}')
        elif x == 0:
            break

spell()




