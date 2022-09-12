ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
hundreds = {k*100:v+'hundred' for (k,v) in ones.items() if k < 10}
thousands = {1000: 'onethousand'}
nums = [thousands, hundreds, tens, ones]

def number_to_text(x):
    written = ''
    for num in nums:
        key_list = sorted(num.keys(), reverse=True)
        for key in key_list:
            if x >= key:
                written += num[key]
                x -= key
                if 1000 > key >= 100 and x > 0:
                    written += 'and'
            if x == 0:
                return written

total = ''
for i in range(1001):
    total += number_to_text(i)

print(len(total))