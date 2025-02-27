import argparse

# parser = argparse.ArgumentParser(prog="main")
# subparsers = parser.add_subparsers(dest="command")

# # First-level subparser
# subparser_a = subparsers.add_parser("level1")
# subparser_a_subparsers = subparser_a.add_subparsers(dest="subcommand")

# # Second-level subparser
# subparser_b = subparser_a_subparsers.add_parser("level2")
# subparser_b_subparsers = subparser_b.add_subparsers(dest="subsubcommand")

# # Third-level subparser
# subparser_c = subparser_b_subparsers.add_parser("level3")
# subparser_c.add_argument("--option", help="An option for level3")

# args = parser.parse_args()
# print(args)




parser = argparse.ArgumentParser(description='Manage tasks through a CLI')
subparsers = parser.add_subparsers(dest='command')

# task-cli add "Buy groceries"
add_parser = subparsers.add_parser('add', help='Add new task description')
add_parser.add_argument('description')

# task-cli update 1 "Buy groceries and cook dinner"
update_parser = subparsers.add_parser('update', help='update new task description')
update_parser.add_argument('id')
update_parser.add_argument('description')

# task-cli delete 1
delete_parser = subparsers.add_parser('delete', help='delete specified task using its id')
delete_parser.add_argument('id')

# task-cli mark-in-progress 1
mark_parser = subparsers.add_parser('mark', help='change task status (todo, in-progress, done)')
mark_parser.add_argument('id')

args = parser.parse_args()

# verify which command on input
if args.command == 'add':
    print(args.description)

elif args.command == 'update':
    print(args.id)
    print(args.description)

