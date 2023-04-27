# StudentTrack
School/Student Management System

This is a web-based management system for a school to manage their student and teacher information. It allows the user to perform various operations like adding new students and teachers, displaying the list of students and teachers, managing results, and viewing individual student result cards.
Features

    Add new students and teachers
    Display the list of students and teachers
    Manage results
    View individual student result cards
    View result ranking
    Realtime Search Student And Teachers
    Simple Dashboard Showing Number Of Students, Teachers.

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


Contributions are welcome! If you find any bugs or have suggestions for new features, please open an issue or submit a pull request.
<h2>Screenshots </h2>

![Screenshot (49)](https://user-images.githubusercontent.com/78295593/233644826-12882438-5908-4a44-8967-7452b856e5db.png)
![Screenshot (50)](https://user-images.githubusercontent.com/78295593/233645013-276a866e-b434-4aca-a62b-ab8d1d6fc106.png)
![Screenshot (48)](https://user-images.githubusercontent.com/78295593/233645023-b5251816-34ba-43b0-9d05-7f0ba4612a10.png)
![Screenshot (47)](https://user-images.githubusercontent.com/78295593/233645029-cbc3fecb-dc40-4b22-979e-85e70b7766c4.png)
![Screenshot (46)](https://user-images.githubusercontent.com/78295593/233645033-bdc820c3-ae5b-4bc9-b4c2-f857a072b67e.png)
![Screenshot (45)](https://user-images.githubusercontent.com/78295593/233645036-2675e867-c904-453b-8180-019be8bb000e.png)
