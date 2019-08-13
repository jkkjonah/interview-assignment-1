# Requirements
Create a simple todo application where users can:

- Add, edit, remove tasks, and assign due date/time to task
- View their tasks list as either a list or a calendar
- Filter and sort their tasks list/calendar by label or other attribute
- This assignment should be written in Django
- Write some unit tests for this application
- Add a readme with a description of how to run and test your application
- Front end should be simple and does not have to be very polished (we care more about backend functionality)
- Do not spend more than a couple hours on this task


**Tasks attributes:**

- Title
- Description
- Whether or not the task was completed
- Zero or more task labels (Task can be associated with many different labels)
- Calendar event associated with task (can be null)


**Task label attributes:**

- Name (unique)
- One label can be associated with many tasks

**Calendar event attributes:**

- datetime
