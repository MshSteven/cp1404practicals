"""
estimate time: 50 minutes
actual time:
"""
from prac_07.project import Project
import datetime

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n" \
       "- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    """Run the menu and get option from users."""
    options = ("l", "s", "d", "f", "a", "u", 'q')
    filename = "projects.txt"
    projects = []

    print(MENU)
    option = input(">>> ").lower()
    while option != options[-1]:
        if option == options[0]:
            projects = load_projects(filename)

        if option == options[1]:
            save_projects(filename, projects)

        if option == options[2]:
            display_projects(projects)

        if option == options[3]:
            start_after_date = input("Show projects that start after date (dd/mm/yy):")
            filter_projects_by_date(projects, start_after_date)

        if option == options[4]:
            new_project = add_new_project()
            projects.append(new_project)

        if option == options[5]:
            update_project(projects)

        print(MENU)
        option = input(">>> ").lower()
    print("Thank you for using custom-built project management software.")

    # projects = load_projects(filename)
    # save_projects(filename, projects)
    # display_projects(projects)
    # start_after_date = input("Show projects that start after date (dd/mm/yy):")
    # filter_projects_by_date(projects, start_after_date)
    # project = add_new_project()
    # projects.append(project)
    # update_project(projects)


def load_projects(filename):
    """Load details from projects.txt and store into a projects list."""
    projects = []
    in_file = open(filename, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('\t')

        # Below figures out the attributes of the project object.
        name = parts[0]
        start_date = parts[1]
        priority = int(parts[2])
        cost_estimate = float(parts[3])
        completion_percentage = int(parts[4])

        # Append project element into projects list.
        project = Project(name, start_date, priority, cost_estimate, completion_percentage)
        projects.append(project)
    in_file.close()
    return projects


def save_projects(filename, projects):
    """Save details into projects.txt from projects list."""
    out_file = open(filename, 'w')
    print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
    for project in projects:
        # Below write project's attribute into projects.txt
        name = project.name
        start_date = project.start_date_str
        priority = project.priority
        cost_estimate = project.cost_estimate
        completion_percentage = project.completion_percentage
        print(f"{name}\t{start_date}\t{priority}\t{cost_estimate}\t{completion_percentage}", file=out_file)

    out_file.close()


def display_projects(projects):
    """Display projects details by Incomplete or Completed."""
    projects.sort()
    print("Incomplete projects:")
    for project in projects:
        if project.completion_percentage < 100:
            print(project)
    print("Completed projects:")
    for project in projects:
        if project.completion_percentage == 100:
            print(project)


def filter_projects_by_date(projects, start_after_date):
    """Filter project after user input a date, which is sorted by date."""
    dates = []
    for project in projects:
        if project.compare_date_with_input_date(start_after_date):
            dates.append(project.start_date)
    dates.sort()
    for date in dates:
        for project in projects:
            if date == project.start_date:
                print(project)


def add_new_project():
    """Add new project into the projects list."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    return project


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    project_choice = int(input("Project choice: "))
    choosed_project = projects[project_choice]
    new_percentage = input("New Percentage: ")
    if new_percentage != "":
        choosed_project.completion_percentage = int(new_percentage)
    new_priority = input("New Priority: ")
    if new_priority != "":
        choosed_project.priority = int(new_priority)


main()
