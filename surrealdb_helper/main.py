import modules
import argparse
import sys

def get_config():
    import json

    try:
        config_file = open("surrealdb.json")
        config = json.load(config_file)
        config_file.close()
        return config
    except FileNotFoundError:
        print("There is no file named surrealdb.json, please change the content of the newly created surrealdb.json")
        content = {
                "url": "http://localhost:8000",
                "namespace": "test",
                "database": "test",
                "username": "root",
                "password": "root"
                }
        config_file = open("surrealdb.json", "w")
        config_file.write(json.dumps(content))
        config_file.close()
        sys.exit(1)



def run():
    config = get_config()
    parser = argparse.ArgumentParser(description='Helper script to help you import and export project database')
    subparsers = parser.add_subparsers()

    export_parser = subparsers.add_parser('export', help="Export database to SQL file")
    export_parser.add_argument('file_name', help="File name to be exported", nargs="?", default="export.db")
    export_parser.set_defaults(func=modules.export_db)

    import_parser = subparsers.add_parser('import', help="Import SQL file to database")
    import_parser.add_argument('file_name', help="File name to be imported", nargs="?", default="export.db")
    import_parser.set_defaults(func=modules.export_db)
    
    args = parser.parse_args()
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args.func(args.file_name, config)
    


if __name__ == "__main__":
    run()
