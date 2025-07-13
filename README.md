# ALX Backend: Caching Property Listings

## Project Overview
This project implements a robust Django backend for managing property listings, with a primary focus on optimizing data retrieval through strategic caching mechanisms. It is designed to demonstrate efficient data serving for high-traffic applications.

## Key Features
-   **Property Management**: Core functionalities for listing and retrieving property data.
-   **Performance Caching**: Leverages Django's caching framework to significantly reduce database load and improve response times for frequently accessed property data.
-   **Scalable Architecture**: Built on Django, providing a solid foundation for future expansion and integration.

## Setup and Installation

This project utilizes Docker for simplified setup and dependency management.

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/O-G-W-A-L/alx-backend-caching_property_listings.git
    cd alx-backend-caching_property_listings
    ```

2.  **Build and Run with Docker Compose**:
    Ensure Docker and Docker Compose are installed on your system.
    ```bash
    docker-compose up --build -d
    ```
    This command will build the necessary Docker images and start the services in detached mode.

## Usage

Once the Docker containers are running, the Django application will be accessible.

-   **Access the API**: The API endpoints will be available, typically at `http://localhost:8000/api/properties/` (or similar, depending on your `urls.py` configuration).
-   **Caching Demonstration**: Observe the performance benefits of caching by making repeated requests to the property listing endpoint. The first request will populate the cache, and subsequent requests within the cache duration will be served much faster.

## Technologies Used
-   **Django**: Web framework
-   **Python**: Programming language
-   **Docker**: Containerization
-   **Redis (or other configured cache backend)**: For caching (implicitly used by Django's cache framework)
