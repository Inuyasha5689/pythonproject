pg_db_username = 'postgres'
pg_db_password = 'chhs2012'
pg_db_name = 'flask'
pg_db_hostname = 'localhost'

mysql_db_username = 'root'
mysql_db_password = 'chhs2012'
mysql_db_name = 'flask'
mysql_db_hostname = 'localhost'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER=pg_db_username,
                                                                                        DB_PASS=pg_db_password,
                                                                                        DB_ADDR=pg_db_hostname,
                                                                                        DB_NAME=pg_db_name)