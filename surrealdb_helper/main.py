import asyncio
import modules

def connect_db():
    from surrealdb.clients.http import HTTPClient
    import json

    config_file = open("surrealdb.json")
    config = json.load(config_file)

    client = HTTPClient(
        config["url"],
        namespace=config["namespace"],
        database=config["database"],
        username=config["username"],
        password=config["password"],
    )

    return client

async def run():
    client = connect_db()
    output = await client.execute("INFO FOR DB")
    print(output)
    await modules.backup_table("skills", client)
    


if __name__ == "__main__":
    asyncio.run(run())
    
