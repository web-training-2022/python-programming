my_sq = lambda input_num : input_num * input_num
product = lambda input_num1, input_num2=9 : input_num1 * input_num2

king = lambda **kwargs : kwargs.get('name', 'Democratic')

tup_lambda = lambda *args : len(args)
