# Event Booking System

Backend API service built with Django and Django Rest Framework for event booking and management.

## Features

- User Authentication and Authorization
- Event Creation and Management
- Ticket Booking System
- Event Search and Filtering
- Seat Management
- Payment Integration (coming soon)

## Tech Stack

- Python 3.x
- Django
- Django Rest Framework
- PostgreSQL
- Docker (optional)

## Setup

1. Clone the repository
```bash
git clone <repository-url>
cd eventbooking_system
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # For Unix/MacOS
# or
venv\Scripts\activate  # For Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables
```bash
cp .env.example .env
# Update .env with your configurations
```

5. Run migrations
```bash
python manage.py migrate
```

6. Start development server
```bash
python manage.py runserver
```

## API Documentation

API documentation is available at `/api/docs/` after running the server.

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

MIT