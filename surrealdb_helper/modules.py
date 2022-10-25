import subprocess

def export_db(config):
    arguments = ["surreal", "export", "--conn", f"{config['url']}", "--user", f"{config['username']}", "--pass", f"{config['password']}", "--ns", f"{config['namespace']}", "--db", f"{config['database']}", "export.sql"]
    subprocess.run(arguments)
