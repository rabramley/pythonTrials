import pymssql, argparse

def main():
    args = getArgs()
    connectAndSelect(args.server, args.username, args.password, args.database)

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", required=True, help="Username")
    parser.add_argument("-p", "--password", required=True, help="Password")
    parser.add_argument("-s", "--server", required=True, help="Server")
    parser.add_argument("-d", "--database", required=True, help="Database")
    return parser.parse_args()

def connectAndSelect(server, username, password, database):
    with pymssql.connect(server, username, password, database) as conn:
        # as_dict means that cursor returns a dictionary so column names can be used
        with conn.cursor(as_dict=True) as cursor:
            cursor.execute('SELECT TOP 100 * FROM concept_dimension WHERE concept_cd LIKE %s', 'CBO:%')
            row = cursor.fetchone()
            while row:
                print("Name=%s" % (row['name_char']))
                row = cursor.fetchone()

if __name__ == "__main__":
    main()