import argparse
import json
import os
from tabulate import tabulate
from datetime import datetime
from collections import defaultdict
from pprint import pprint



def create_json(filename):
    with open(f'{filename}.json', 'w', encoding='utf-8') as file:
        json.dump({}, file)

def read_json(filename):
    with open(f'{filename}.json', 'r') as infile:
        return json.load(infile)
    
def write_json(filename, dict):
    with open(f'{filename}.json', 'w') as outfile:
        json.dump(dict, outfile, ensure_ascii=False, indent=4)

def add_task(filename, description):

    json_dict = read_json(filename) # Read json file content

    current_time = datetime.now().isoformat()
    id = str(int(max("0", *json_dict.keys())) + 1)
    json_dict[id] = {
        'description': description,
        'status': 'todo',
        'created_at': current_time,
        'modified_at': current_time
    }

    write_json(filename, json_dict) # Write dict to json file

def update_task(filename, id, description):

    json_dict = read_json(filename) # Read json file content
    json_dict[str(id)]['description'] = description
    write_json(filename, json_dict) # Write dict to json file

def delete_task(filename, id):
    
    json_dict = read_json(filename) # Read json file content
    json_dict.pop(str(id))
    write_json(filename, json_dict) # Write dict to json file


def mark_as_in_progress(filename, id):

    json_dict = read_json(filename) # Read json file content
    json_dict[str(id)]['status'] = 'in-progress'
    write_json(filename, json_dict) # Write dict to json file

def list_tasks(filename, *filter):

    json_dict = read_json(filename) # Read json file content
    table = format_as_table(json_dict, filter)
    
    return table

def format_as_table(payload, filter):

    table_dict = defaultdict(list)
    for id, properties in payload.items(): 
        if not filter or properties['status'] in filter:
            table_dict['ID'].append(id)
            table_dict['Description'].append(properties['description'])
            table_dict['Status'].append(properties['status'])
            table_dict['Created At'].append(properties['created_at'])
            table_dict['Modified At'].append(properties['modified_at'])

    return tabulate(table_dict, headers="keys", tablefmt="fancy_grid")




if __name__ == '__main__':

    filename = 'data/database'
    if not os.path.exists(f'{filename}.json'):
        create_json(filename)

    # Create parser and subparsers
    parser = argparse.ArgumentParser(description='Manage tasks through a CLI')
    subparsers = parser.add_subparsers(dest='command')

    # add
    add_parser = subparsers.add_parser('add', help='Add new task description')
    add_parser.add_argument('description')
    
    # update
    update_parser = subparsers.add_parser('update', help='Update given task id description')
    update_parser.add_argument('id', type=int)
    update_parser.add_argument('description')

    # delete
    delete_parser = subparsers.add_parser('delete', help='Delete task according to given id')
    delete_parser.add_argument('id', type=int)

    # list all
    list_parser = subparsers.add_parser('list', help='Return a list of all tasks')

    # mark-in-progress
    mark_in_progress_parser = subparsers.add_parser('mark-in-progress', help="Mark given task id as 'In Progress'")
    mark_in_progress_parser.add_argument('id', type=int)

    # Process query
    args = parser.parse_args()

    if args.command == 'add':
        add_task(filename, args.description)

    elif args.command == 'update':
        update_task(filename, args.id, args.description)

    elif args.command == 'delete':
        delete_task(filename, args.id)

    elif args.command == 'mark-in-progress':
        mark_as_in_progress(filename, args.id)
    
    print(list_tasks(filename))

