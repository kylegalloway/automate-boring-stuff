import logging

logging.basicConfig(  # filename='myProgramLog.txt',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')

logging.disable(logging.WARNING)
# Levels
# debug
# info
# warning
# error
# critical

logging.debug('Start of program')


def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('Return value is %s' % (total))
    if(total < 1):
        logging.error('Problem')
    return total


print(factorial(5))

logging.debug('End of program')
