# StudentTrack
School/Student Management System

This is a web-based management system for a school to manage their student and teacher information. It allows the user to perform various operations like adding new students and teachers, displaying the list of students and teachers, managing results, and viewing individual student result cards.
Features

    Add new students and teachers
    Display the list of students and teachers
    Manage results
    View individual student result cards
    View result ranking

Installation

To run this system locally, follow these steps:

    Clone the repository to your local machine:

bash

git clone https://github.com/your-username/school-management-system.git

    Create and activate a virtual environment:

bash

python -m venv env
source env/bin/activate

    Install the required packages:

pip install -r requirements.txt

    Migrate the database:

python manage.py migrate

    Create a superuser:

python manage.py createsuperuser

    Run the development server:

python manage.py runserver

    Open your browser and go to http://localhost:8000/admin to access the admin panel. Use the credentials of the superuser created in step 5 to log in.

Usage
Students and Teachers

To add new students or teachers, go to the admin panel and click on the "Students" or "Teachers" link. Then click on the "Add Student" or "Add Teacher" button and fill in the required information.

To display the list of students or teachers, click on the "Students" or "Teachers" link in the admin panel.
Results

To manage results, go to the admin panel and click on the "Results" link. Then click on the "Add Result" button and select the student and subject for which you want to add the result. Fill in the marks obtained and click on the "Save" button.

To view individual student result cards, go to the admin panel and click on the "Students" link. Then click on the name of the student whose result card you want to view. This will take you to a page displaying the student's result card.

To view result ranking, go to the admin panel and click on the "Results" link. Then click on the "Result Ranking" button to see the ranking of students based on their marks.
Contributing

Contributions are welcome! If you find any bugs or have suggestions for new features, please open an issue or submit a pull request.
<h2>Screenshots </h2>
![Screenshot (50)](https://user-images.githubusercontent.com/78295593/233644623-d8534863-03f7-44c7-9231-a4ef0279bd57.png)
![Screenshot (49)](https://user-images.githubusercontent.com/78295593/233644627-c9851dc1-d99e-4790-b918-7b42d38ffccd.png)
![Screenshot (48)](https://user-images.githubusercontent.com/78295593/233644631-b8387385-9d9c-4f0e-88eb-33934ba93de4.png)
![Screenshot (46)](https://user-images.githubusercontent.com/78295593/2![Screenshot (47)](https://user-images.githubusercontent.com/78295593/233644650-29977f41-b51a-4788-aae0-2df27753714b.png)
33644640-7072d8f7-9dab-4b91-a067-9b86be9c1cd0.png)![Screenshot (45)](https://user-images.githubusercontent.com/78295593/233644644-dc01a409-d227-43e5-a657-0fe2354ad29b.png)

