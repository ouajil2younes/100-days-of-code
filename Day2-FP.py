print('welcom to the tip calculator !')
total_bill=float(input('what was the otal bill ? '))
tip_perc=float(input('how much the tip would you like to give ? '))
pp_count=float(input('how many peapl to split the bill ? '))
tip_perc_calc=(tip_perc*total_bill)/100

print(f'the tip percent calculation {tip_perc_calc}')
bill_split=total_bill/pp_count
print(f'the bill split calculations {bill_split}')
my_share=bill_split+(tip_perc_calc/pp_count)
print(f'my share with tip {my_share}')
print(f'resolt {my_share:.2f}')