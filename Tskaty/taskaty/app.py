from argparse import ArgumentParser
from .TaskController import TaskController


def main():
    controller = TaskController('tasks.txt')
    parser = ArgumentParser(description='Simple CLI Task Manager')
    subparsers = parser.add_subparsers(dest='command')

    add_task = subparsers.add_parser('add', help='Add the given task')
    add_task.add_argument('title', help='Title of the task', type=str)
    add_task.add_argument('-d', '--description', type=str, default=None)
    add_task.add_argument('-s', '--start_date', type=str, default=None)
    add_task.add_argument('-e', '--end_date', type=str, default=None)
    add_task.add_argument('--done', action='store_true', default=False)
    add_task.set_defaults(func=controller.add_task)

    list_tasks = subparsers.add_parser('list', help='List unfinished tasks')
    list_tasks.add_argument('-a', '--all', action='store_true')
    list_tasks.set_defaults(func=controller.display)

    check_task = subparsers.add_parser('check', help='Check the given task')
    check_task.add_argument('-t', '--task', type=int, default=None)
    check_task.set_defaults(func=controller.check_task)

    remove = subparsers.add_parser('remove', help='Remove a task')
    remove.add_argument('-t', '--task', type=int, default=None)
    remove.set_defaults(func=controller.remove)

    reset = subparsers.add_parser('reset', help='Remove all tasks')
    reset.set_defaults(func=controller.reset)

    args = parser.parse_args()
    if not hasattr(args, 'func'):
        parser.print_help()
        return
    args.func(args)


if __name__ == '__main__':
    main()