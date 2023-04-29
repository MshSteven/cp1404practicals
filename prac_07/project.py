import datetime


class Project:
    def __init__(self, name="", start_date="", priority=0, cost_estimate=0, completion_percentage=0):
        """

        name:                   name of the project
        start_date:             start date of the project
        priority:               priority of the project
        cost_estimate:          cost estimate of the project
        completion_percentage:  completion percentage of the project
        """
        self.name = name
        # Below convert date string into date object.
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.start_date_str = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, start: {self.start_date_str}, priority {self.priority}, " \
               f"estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Sort project object by priority."""
        return self.priority < other.priority

    def filter_projects_by_date(self, start_after_date):
        """Filter project after user input a date."""
        start_after_date = datetime.datetime.strptime(start_after_date, "%d/%m/%Y").date()
        return self.start_date >= start_after_date

