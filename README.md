# Event Booking System Backend

This is the backend for an Event Booking System, designed to manage movies/events, shows, venues, screens, seats, and user bookings. It's built using Python, Django, and Django REST framework to provide a robust API for a frontend application.

## Table of Contents

- [Event Booking System Backend](#event-booking-system-backend)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Tech Stack](#tech-stack)
  - [Project Structure](#project-structure)
  - [Prerequisites](#prerequisites)
  - [Setup and Installation](#setup-and-installation)
  - [Running the Application](#running-the-application)
  - [API Endpoints](#api-endpoints)
  - [Key Design Choices \& Components](#key-design-choices--components)
    - [Booking Serialization (`bookings/serializers.py`)](#booking-serialization-bookingsserializerspy)
    - [Show Uniqueness (`shows/models.py`)](#show-uniqueness-showsmodelspy)
    - [Seat Uniqueness (`venues/models.py`)](#seat-uniqueness-venuesmodelspy)
  - [Further Development / To-Do](#further-development--to-do)
  - [Contributing](#contributing)

## Features

- **User Management**: (Assumed, typically includes registration, authentication, profile management)
- **Event/Movie Management**: Define events or movies that can be scheduled.
- **Venue & Screen Management**: Define venues, and screens within those venues.
- **Seat Management**: Define seat layouts (rows, numbers) for each screen.
- **Show Scheduling**: Schedule events/movies on specific screens at particular times.
- **Booking System**:
    - Allow users to book available seats for a specific show.
    - View booking history and status.
    - Handle booking requests and generate appropriate responses.
- **API-driven**: Exposes RESTful APIs for frontend consumption or other services.

## Tech Stack

- **Language**: Python (3.x)
- **Framework**: Django
- **API**: Django REST Framework (DRF)
- **Database**: (e.g., PostgreSQL, MySQL, SQLite3 - *Please specify your choice*)
- **Virtual Environment**: `venv` or `conda` (Recommended)

## Project Structure

A typical structure for this project would be:

```
bms-backend/
├── eventbooking_system/    # Django project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py             # Main project URLs
│   └── wsgi.py
├── bookings/               # App for managing bookings
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py      # Handles request/response data for bookings
│   ├── services.py         # Business logic for bookings
│   ├── tests.py
│   ├── urls.py             # Bookings app specific URLs
│   └── views.py
├── events/                 # App for managing events/movies (or could be part of shows)
│   └── ...
├── shows/                  # App for managing shows (schedules)
│   ├── migrations/
│   ├── models.py           # Defines Show model with screen, start_time, etc.
│   └── ...
├── venues/                 # App for managing venues, screens, and seats
│   ├── migrations/
│   ├── models.py           # Defines Venue, Screen, Seat models
│   └── ...
├── users/                  # App for user authentication and management (recommended)
│   └── ...
├── manage.py               # Django's command-line utility
├── requirements.txt        # Project dependencies
└── README.md               # This file
```

## Prerequisites

- Python (e.g., 3.8+ - *Please specify version*)
- Pip (Python package installer)
- Git
- A database server (if not using SQLite, e.g., PostgreSQL, MySQL)

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd bms-backend
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    # venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Ensure `requirements.txt` is up-to-date with all necessary packages like `django`, `djangorestframework`, database drivers, etc.)*

4.  **Configure environment variables:**
    It's good practice to use environment variables for sensitive settings. Create a `.env` file in the root directory (`bms-backend/`) and add necessary variables. Your `eventbooking_system/settings.py` should be configured to read these (e.g., using `python-decouple` or `django-environ`).
    Example `.env` content:
    ```env
    SECRET_KEY='your_django_secret_key_here'
    DEBUG=True
    DATABASE_URL='sqlite:///db.sqlite3' # Or: postgresql://user:password@host:port/dbname
    # Add other environment variables as needed
    ```

5.  **Apply database migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Create a superuser (for Django Admin access):**
    ```bash
    python manage.py createsuperuser
    ```

## Running the Application

1.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will typically be available at `http://120.0.0.1:8000/`. The Django Admin interface will be at `http://120.0.0.1:8000/admin/`.

## API Endpoints

The system exposes RESTful APIs. Key endpoint groups (defined in `eventbooking_system/urls.py` and respective app `urls.py` files) would include:

- `/api/users/` (or `/api/auth/`): For user registration, login, logout.
- `/api/events/`: For listing events/movies, event details.
- `/api/venues/`: For venue, screen, and seat information.
- `/api/shows/`: For listing shows, show details, available showtimes.
- `/api/bookings/`:
    - `POST /api/bookings/`: To create a new booking. Expects `show_id` and a list of `seat_ids`.
    - `GET /api/bookings/`: To list a user's bookings.
    - `GET /api/bookings/<booking_id>/`: To retrieve details of a specific booking.

*(Refer to Django REST framework's browsable API or API documentation tools like Swagger/OpenAPI for detailed endpoint specifications once implemented.)*

## Key Design Choices & Components

### Booking Serialization (`bookings/serializers.py`)
-   **`BookingRequestSerializer`**: Validates incoming data for new booking requests, ensuring `show_id` (integer) and a non-empty list of `seat_ids` (integers) are provided.
-   **`BookingResponseSerializer`**: Formats `Booking` model instances for API responses. It includes standard booking fields (`id`, `user`, `status`, `booked_at`) and uses a `SerializerMethodField` (`get_seat_ids`) to efficiently include a list of booked seat IDs.

### Show Uniqueness (`shows/models.py`)
-   The `Show` model uses `unique_together = ('screen', 'start_time')` in its `Meta` class. This enforces a database constraint preventing two shows from being scheduled on the same screen at the exact same start time, which is critical for avoiding scheduling conflicts.

### Seat Uniqueness (`venues/models.py`)
-   The `Seat` model uses `Meta.constraints` with `models.UniqueConstraint(fields=['screen', 'row', 'number'], name='unique_seat_in_screen')`. This ensures that within a given screen, the combination of row and seat number is unique, accurately modeling a physical seating arrangement.

## Further Development / To-Do

- Implement robust user authentication and authorization (e.g., JWT).
- Add payment gateway integration for paid bookings.
- Develop advanced show search and filtering capabilities (by genre, date, venue).
- Implement seat availability checks with locking mechanisms during the booking process to prevent race conditions.
- Email/SMS notifications for booking confirmations, reminders, and cancellations.
- Admin panel enhancements for easier management of shows, venues, and bookings.
- Comprehensive test coverage (unit and integration tests).
- API documentation (e.g., using Swagger/OpenAPI with `drf-spectacular` or `drf-yasg`).
- Caching strategies for frequently accessed data.

## Contributing

Contributions are welcome! If you'd like to contribute, please:
1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature/your-amazing-feature`).
3. Make your changes and commit them (`git commit -m 'Add some amazing feature'`).
4. Push to your branch (`git push origin feature/your-amazing-feature`).
5. Open a Pull Request against the `main` or `develop` branch of the original repository.

Please ensure your code adheres to the project's coding standards (e.g., PEP 8) and includes tests for new features or bug fixes.

---

*This README is a living document. Please update it as the project evolves.*
```

**Key things to customize in this README:**
*   **`<your-repository-url>`**: Replace this with the actual URL of your Git repository.
*   **Database Choice**: In the "Tech Stack" section, specify which database you are using (e.g., PostgreSQL, MySQL, or if you're sticking with SQLite3 for development).
*   **Python Version**: In "Prerequisites", specify the Python version your project is targeting.
*   **`requirements.txt`**: Make sure this file is created and maintained in your project root with all dependencies.
*   **API Endpoints**: As you build out more apps and their APIs, update the "API Endpoints" section to reflect the actual routes.
*   **Further Development**: Tailor this section to your specific project roadmap.

This should give you a solid foundation for your project's documentation!