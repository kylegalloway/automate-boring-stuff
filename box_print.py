"""
*********
*       *
*       *
*       *
*       *
*********
"""


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1.')
    if (width < 2) or (height < 2):
        raise Exception(
            '"width" and "height" must be greater than or equal to 2.')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)


boxPrint('*', 15, 5)
boxPrint('+', 5, 5)
boxPrint('|', 2, 2)
# boxPrint('**', 10, 10)
# boxPrint('*', 0, 15)


# import traceback
# try:
#     raise Exception("ERROR")
# except:
#     errorFile = open('error_log.txt', 'a')
#     errorFile.write(traceback.format_exc())
#     errorFile.close()
#     print('The traceback info was written to error_log.txt')
