import subprocess

def export_db(file, config):
    arguments = ["surreal", "export", 
                 "--conn", f"{config['url']}", 
                 "--user", f"{config['username']}", 
                 "--pass", f"{config['password']}", 
                 "--ns", f"{config['namespace']}", 
                 "--db", f"{config['database']}", file]
    subprocess.run(arguments)

def inport_db(file, config):
    arguments = ["surreal", "import", 
                 "--conn", f"{config['url']}", 
                 "--user", f"{config['username']}", 
                 "--pass", f"{config['password']}", 
                 "--ns", f"{config['namespace']}", 
                 "--db", f"{config['database']}", file]
    subprocess.run(arguments)
