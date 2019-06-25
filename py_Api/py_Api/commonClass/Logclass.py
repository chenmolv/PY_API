import logging
import os
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.dirname(current_dir)
path = parent_path + '\\' + 'relust' + '\\'
fm='[%(asctime)s-%(filename)s-%(levelname)s]:%(message)s'
class lgtest():
 def error(msg):
  logging.basicConfig(filename=path + __name__ + '.log',
                         format=fm, level=logging.DEBUG,
                         filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p', )

  logging.error(msg)
  print(msg)
 def info(msg):
    logging.basicConfig(filename=path + __name__ + '.log',
                         format=fm, level=logging.DEBUG,
                         filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p', )
    logging.info(msg)
    print(msg)
 def warning(msg):
     logging.basicConfig(filename=path + __name__ + '.log',
                         format=fm, level=logging.DEBUG,
                         filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p', )
     logging.warning(msg)
     print(msg)

if __name__ == '__main__':
   x=lgtest()
   x.info("asd")
   x.info("111")