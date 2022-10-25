import modules

def get_config():
    import json

    config_file = open("surrealdb.json")
    config = json.load(config_file)
    return config


def run():
    config = get_config()
    modules.export_db(config)
    


if __name__ == "__main__":
    run()
