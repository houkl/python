MysqlHost = '172.28.66.47'
MysqlUser = 'qbcmdb'
MysqlPass = 'qbcmdb'
MysqlDB = 'qbcmdb'
SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s/%s' % (MysqlUser, MysqlPass, MysqlHost, MysqlDB)
SECRET_KEY = '\x88ZZQ\xd3\x83G\xe3\xb5<\x1c\x1e"\x17\xf1\x1f\xdah(L'
