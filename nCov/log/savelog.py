import logging


def logs(logname):
    logger = logging.getLogger("%s" % logname)
    logger.setLevel(level=logging.DEBUG)
    filehandler = logging.FileHandler('./nCov/log/%s.txt' % logname)
    famatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
    filehandler.setFormatter(famatter)
    logger.addHandler(filehandler)
    return logger
