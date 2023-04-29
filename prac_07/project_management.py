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

    # print(MENU)
    # option = input(">>> ").lower()
    # while option != options[-1]:
    #     if option == options[0]:
    #         projects = load_projects(filename)
    #
    #     if option == options[1]:
    #         save_projects(filename, projects)
    #
    #     if option == options[2]:
    #         display_projects(projects)
    #
    #     if option == options[3]:
    #         filter_projects_by_date(projects, start_after_date)
    #
    #     if option == options[4]:
    #         add_new_project()
    #
    #     if option == options[5]:
    #         update_project()
    #
    #     print(MENU)
    #     option = input(">>> ").lower()

    projects = load_projects(filename)
    # save_projects(filename, projects)
    # display_projects(projects)
    start_after_date = "20/7/2022"
    for project in projects:
        if project.filter_projects_by_date(start_after_date):
            print(project)


def run_test():

    return "projects"


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
        start_date = project.start_date.strftime("%d/%m/%Y")  # Convert date object into date string.
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


def add_new_project():
    return ""


def update_project():
    return ""


main()
