import json

async def backup_table(name, client):
    data = await client.execute(f"SELECT * FROM {name}")
    json_object = json.dumps(data, indent=4)

    with open(f"{name}.json", "w") as file:
        file.write(json_object)

async def import_table(name, client):
    pass
