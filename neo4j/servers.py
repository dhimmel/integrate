import os
import argparse
import re
import subprocess
import sys

def get_instances(directory):
    """Return neo4j instances in a directory"""
    instances = list()
    for filename in os.listdir(directory):
        binary = os.path.join(directory, filename, 'bin', 'neo4j')
        if not os.path.exists(binary):
            continue
        instance = {
            'name': filename.split('_', 1)[1],
            'binary': binary,
            'path': os.path.join(directory, filename),
            'directory': filename,
        }
        config_path = os.path.join(directory, filename, 'conf', 'neo4j-server.properties')
        instance['port'] = get_port(config_path)
        instances.append(instance)

    return instances

def get_port(config_path):
    """
    Find the webserver port specified in a neo4j configuration properties file.
    """
    with open(config_path) as read_file:
        text = read_file.read()
    match = re.search(r'^org.neo4j.server.webserver.port=([0-9]+)', text, re.MULTILINE)
    port = int(match.group(1))
    return port

def is_running(instance):
    """
    Return the stdout from `neo4j status` if sever is running, else `False`.
    """
    process = subprocess.run([instance['binary'], 'status'], stdout=subprocess.PIPE)
    stdout = str(process.stdout, sys.stdout.encoding).rstrip()
    match = re.match(r'Neo4j Server is running', stdout)
    return stdout if match else False

def start_server(instance):
    """
    Start the server specified by an instance, if its not already running.
    Returns the stdout of `neo4j status` if already running, and the stdout
    from `neo4j start` otherwise.
    """
    running = is_running(instance)
    if running:
        return running
    process = subprocess.run([instance['binary'], 'start'], stdout=subprocess.PIPE)
    stdout = str(process.stdout, sys.stdout.encoding)
    match = re.search(r'process \[([0-9]+)\]', stdout)
    instance['pid'] = int(match.group(1))
    return stdout

def stop_server(instance):
    """
    Shutdown a neo4j server.
    """
    if not is_running(instance):
        return '{} is not running'.format(instance['name'])
    process = subprocess.run([instance['binary'], 'stop'], stdout=subprocess.PIPE)
    stdout = str(process.stdout, sys.stdout.encoding).rstrip()
    return stdout

def get_running(instances):
    """Return the subset of instances which are running"""
    return [instance for instance in instances if is_running(instance)]

def start_all(instances):
    for instance in instances:
        out = start_server(instance)
        print(out)

def stop_all(instances):
    for instance in instances:
        out = stop_server(instance)
        print(out)

def status_all(instances):
    for instance in instances:
        out = is_running(instance)
        if out:
            print(out)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Manage neo4j servers')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--start-all', action='store_true')
    group.add_argument('--stop-all', action='store_true')
    group.add_argument('--status-all', action='store_true')
    args = parser.parse_args()

    directory = os.path.dirname(os.path.abspath(__file__))
    instances = get_instances(directory)

    if args.start_all:
        start_all(instances)

    if args.stop_all:
        stop_all(instances)

    if args.status_all:
        status_all(instances)
