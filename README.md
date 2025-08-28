📌Social(Google) Authentication System


A Full-Stack Authentication System built with Django REST Framework and React, featuring email-based registration and login with JWT authentication.


The backend leverages django-allauth and dj-rest-auth for user registration, login, and email verification, while the frontend uses Axios interceptors for automatic token handling. The UI is built with Chakra UI and shadcn components, providing a clean, responsive design for modern web apps.



🔑 Features

Email Authentication → Register and login without usernames.

JWT Authentication → Secure token-based session handling with refresh tokens.

Email Verification → Automatic confirmation via verification links sent to users.

Axios Interceptors → Automatically attach JWT access tokens to API requests.

React Frontend → Responsive UI using Chakra UI and shadcn components.

Form Validation & Error Handling → Field-level error messages and toast notifications.

Swagger Documentation → API endpoints documented using drf-yasg.

CORS Support → Configured with django-cors-headers for frontend integration.

Google OAuth Ready → Social login integration via django-allauth.



🛠 Tech Stack

Backend: Django, Django REST Framework, dj-rest-auth, django-allauth, drf-yasg

Frontend: React, Chakra UI, shadcn components, Axios

Authentication: JWT (via djangorestframework-simplejwt)

Database: Default SQLite (can be replaced with PostgreSQL or MySQL)

Environment Management: python-dotenv / environs

Email: SMTP
