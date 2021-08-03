import pymysql


class PybaDatabase:
    def __init__(self):
        """self.host = "localhost"
        self.port = 3306
        self.user = "b2e778b178ec8c"
        self.password = "12345"
        self.database = "bdapi"
        self.connection = self.createConnection()
        self.cursor = self.createCursor()
        """
        self.host = "us-cdbr-east-04.cleardb.com"
        self.port = 3306
        self.user = "root"
        self.password = "8da5f053"
        self.database = "heroku_2ad2c093e75dcff"
        self.connection = self.createConnection()
        self.cursor = self.createCursor()

    def createConnection(self):
        con = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password,
            database=self.database,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
        return con

    def createCursor(self):
        con = self.connection
        cursor = None
        if con is not None:
            cursor = con.cursor()
        else:
            print("app is disconnected from database")
        return cursor

    # usar este metodo solo con SELECT
    def executeQuery(self, sql):
        cursor = self.cursor
        result = None
        if cursor is not None:
            cursor.execute(sql)
            result = cursor.fetchall()
        return result




