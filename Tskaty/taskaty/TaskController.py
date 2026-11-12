from .task import Task
from datetime import date
from tabulate import tabulate
from argparse import Namespace


class TaskController:
    def __init__(self, file_name):
        self.file_name = file_name

    # ---------- helpers ----------
    def _read_tasks(self):
        """Read all tasks safely, skipping empty/broken lines."""
        tasks = []
        try:
            with open(self.file_name, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(', ')
                    if len(parts) != 5:
                        continue  # skip corrupted line
                    title, description, start_date, end_date, done = parts
                    end_date = None if end_date == 'None' else end_date
                    start_date = None if start_date == 'None' else start_date
                    done = (done == 'True')
                    tasks.append({
                        'title': title,
                        'description': description,
                        'start_date': start_date,
                        'end_date': end_date,
                        'done': done,
                    })
        except FileNotFoundError:
            pass
        return tasks

    def _write_tasks(self, tasks):
        with open(self.file_name, 'w', encoding='utf-8') as f:
            for t in tasks:
                obj = Task(t['title'], t['description'], t['start_date'],
                           t['end_date'], t['done'])
                f.write(str(obj) + '\n')

    # ---------- commands ----------
    def add_task(self, args):
        start_date = args.start_date or date.today().isoformat()
        task = Task(args.title, args.description, start_date,
                    args.end_date, args.done)
        with open(self.file_name, 'a', encoding='utf-8') as f:
            f.write(str(task) + '\n')
        print(f"Task added: {task.title}")

    def list_tasks(self):
        return [t for t in self._read_tasks() if not t['done']]

    def list_all_tasks(self):
        return self._read_tasks()

    def due_date(self, start, end):
        start_date = date.fromisoformat(start)
        end_date = date.fromisoformat(end)
        return f'{(end_date - start_date).days} days left.'

    def print_table(self, tasks):
        formatted = []
        for number, task in enumerate(tasks, 1):
            if task['start_date'] and task['end_date']:
                due = self.due_date(task['start_date'], task['end_date'])
            else:
                due = 'Open'
            formatted.append({'no.': number, **task, 'due_date': due})
        print(tabulate(formatted, headers='keys'))

    def display(self, args):
        all_tasks = self.list_all_tasks()

        if not all_tasks:
            print('There are no tasks. To add a task use: add "<task>"')
            return

        if getattr(args, 'all', False):
            self.print_table(all_tasks)
        else:
            unchecked = self.list_tasks()
            if unchecked:
                self.print_table(unchecked)
            else:
                print('All tasks are checked!')

    def check_task(self, args):
        tasks = self.list_all_tasks()
        if not tasks:
            print('No tasks to check.')
            return

        index = args.task if args.task is not None else len(tasks)
        if index < 1 or index > len(tasks):
            print(f'Task number ({index}) does not exist!')
            return

        tasks[index - 1]['done'] = True
        self._write_tasks(tasks)
        print(f'Task {index} marked as done.')

    def remove(self, args):
        tasks = self.list_all_tasks()
        if not tasks:
            print('No tasks to remove.')
            return

        index = args.task if args.task is not None else len(tasks)
        if index < 1 or index > len(tasks):
            print(f'Task number ({index}) does not exist!')
            return

        tasks.pop(index - 1)
        self._write_tasks(tasks)
        print(f'Task {index} removed.')

    def reset(self, *args):
        with open(self.file_name, 'w', encoding='utf-8') as f:
            f.write('')
        print('You have deleted all tasks!')