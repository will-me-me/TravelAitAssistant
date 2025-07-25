# Travel and User Management API

## Purpose

This project is a RESTful API designed to manage Travel Documentation Assistant data and user information. It provides endpoints for user authentication, travel management, and other related services. The API is built using Python and FastAPI, ensuring high performance and scalability.

---

## Requirements

To run this project, ensure you have the following installed:

- Python 3.8 or higher
- `pip3` (Python package manager)
- A virtual environment tool (e.g., `venv`)

Dependencies are listed in the `requirements.txt` file.

---

## Project Structure

The project is organized as follows:

- `auth/`: Handles user authentication (e.g., JWT-based authentication).
  - `jwt_auth.py`: Implements JWT token generation and validation.
- `travel/`: Manages travel-related data.
  - `travel_model.py`: Defines the data models for travel.
  - `travel_routes.py`: Contains the API routes for travel operations.
  - `travel_services.py`: Implements the business logic for travel operations.
- `users/`: Manages user-related data.
  - `users_model.py`: Defines the data models for users.
  - `users_routes.py`: Contains the API routes for user operations.
  - `users_services.py`: Implements the business logic for user operations.
- `main.py`: The entry point of the application.
- `database.py`: Configures the database connection.

---

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .env
   source .env/bin/activate  # On Windows: .env\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory with the following content:

   ```env
   SECRET_KEY=your-secret-key-here-change-in-production
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   DATABASE_URL=sqlite:///./travel_api.db
   ANTHROPIC_API_KEY=your-anthropic-api-key-here
   ```

   **Important**: Make sure to add your `ANTHROPIC_API_KEY` to the `.env` file for proper functionality.

---

## Running the Project

1. Start the application:

   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at http://127.0.0.1:8000.

2. Access the interactive API documentation:
   - **Swagger UI**: http://127.0.0.1:8000/docs
   - **ReDoc**: http://127.0.0.1:8000/redoc

---

## Testing the Endpoints

1. Use tools like **Postman** or **cURL** to test the endpoints.
2. Run automated tests (if available):
   ```bash
   pytest
   ```

---

## API Endpoints

### User Endpoints

#### **POST /users/register**

Register a new user.

- **Request Body**:
  ```json
  {
    "confirm_password": "password123#W",
    "email": "ddoh12@gmail.com",
    "name": "john doe",
    "password": "password123#W"
  }
  ```
- **Response**: `201 Created`
  ```json
  {
    "user": {
      "id": "688370aca017e8bccb2adb32",
      "name": "john doe",
      "email": "ddoh12@gmail.com"
    },
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkZG9oMTJAZ21haWwuY29tIiwiZXhwIjoxNzUzNDQ1NDI0fQ.GHv6omIn0H9WbOEhHlChxQDXhcXRaCLmbNwb45fjFnc",
    "token_type": "bearer"
  }
  ```

#### **POST /users/login**

Authenticate a user and return a JWT token.

- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "string"
  }
  ```
- **Response**: `200 OK`
  ```json
  {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer"
  }
  ```

#### **GET /users/me**

Get current user profile (requires authentication).

- **Headers**: `Authorization: Bearer <token>`
- **Response**: `200 OK` with user details

#### **GET /users/**

Retrieve a list of all users (requires authentication).

- **Headers**: `Authorization: Bearer <token>`
- **Query Parameters**:
  - `skip`: Number of records to skip (default: 0)
  - `limit`: Maximum number of records to return (default: 100)
- **Response**: `200 OK` with a list of users

### Travel Endpoints

#### **GET /travels/**

Retrieve a list of all travel records for the authenticated user.

- **Headers**: `Authorization: Bearer <token>`
- **Query Parameters**:
  - `skip`: Number of records to skip (default: 0)
  - `limit`: Maximum number of records to return (default: 100)
  - `status`: Filter by travel status (optional)
- **Response**: `200 OK` with a list of travel data

#### **POST /travels/query**

Create a new query record.

- **Headers**: `Authorization: Bearer <token>`
- **Request Body**:
  ```json
  {
    "query": "data require to visit kenya"
  }
  ```
- **Response**: `{
  "id": "6883713b2a0fd1eecb55fb7b",
  "query": "data require to visit kenya",
  "response": "Here are the travel documentation requirements for visiting Kenya:\n\n1. **Visa Requirements**:\n   - Most nationalities require a visa to enter Kenya.\n   - Visitors can obtain an e-visa online prior to arrival or get a visa upon arrival at the Kenyan border.\n   - The e-visa can be applied for through the official Kenyan government website.\n   - Visa fees vary depending on the nationality, but typically range from $50 to $100 USD.\n\n2. **Passport Requirements**:\n   - Travelers must have a valid passport with at least 6 months of remaining validity beyond the planned stay in Kenya.\n   - Some nationalities may be required to have at least 2 blank pages in their passport.\n\n3. **Additional Documentation**:\n   - Proof of onward or return travel, such as a flight itinerary or ticket, may be required.\n   - Travelers may need to provide evidence of sufficient funds for their stay, such as bank statements or a letter from their employer.\n   - If traveling with children, additional documentation like birth certificates or parental consent letters may be necessary.\n\n4. **Important Notes**:\n   - Travelers should check the latest visa requirements and application procedures, as they are subject to change.\n   - Visa requirements and fees may vary depending on the traveler's nationality and the purpose of their visit.\n   - It is recommended to apply for the e-visa well in advance to avoid delays.\n\n5. **Processing Time**:\n   - The e-visa application can be processed within 7 working days, but it is advisable to apply at least 2-3 weeks before the planned travel date.\n   - Visa-on-arrival applications may take longer to process, and travelers should be prepared to wait at the border.\n\n6. **Useful Tips**:\n   - Travelers should ensure they have all the required documents and information ready before applying for the visa.\n   - It is recommended to check the official Kenyan government website or consult with a travel agent for the most up-to-date visa information.\n   - Travelers should also be aware of any COVID-19 related entry requirements or restrictions that may be in place.\n\nPlease note that the information provided is accurate as of 2024, but it is always recommended to double-check with official sources, such as the Kenyan government website or your local embassy or consulate, as visa requirements and procedures are subject to change.",
  "success": true,
  "user_id": "688370aca017e8bccb2adb32",
  "created_at": "2025-07-25T11:57:47.642706"
}`

#### **GET /travels/{id}**

Retrieve details of a specific travel record by ID.

- **Headers**: `Authorization: Bearer <token>`
- **Path Parameters**: `id` - Travel record ID
- **Response**: `200 OK` with travel details

#### **DELETE /travels/{id}**

Delete a specific travel record.

- **Headers**: `Authorization: Bearer <token>`
- **Path Parameters**: `id` - Travel record ID
- **Response**: `200 OK` with confirmation message

### System Endpoints

#### **GET /**

Welcome message and API information.

- **Response**: `200 OK` with API details

#### **GET /health**

Health check endpoint.

- **Response**: `200 OK` with status information

---

## Authentication

This API uses JWT (JSON Web Token) based authentication:

1. **Register** a new user via `/users/register`
2. **Login** via `/users/login` to receive a JWT token
3. **Include the token** in the Authorization header for protected endpoints:
   ```
   Authorization: Bearer <your-jwt-token>
   ```

---

---

## Database

The API uses MongoDB as the database. Update the `DATABASE_URL` in your `.env` file to configure the connection string for your MongoDB instance. For example:

```env
DATABASE_URL=mongodb://username:password@host:port/database_name
```

Ensure that the MongoDB server is running and accessible before starting the application.

---

## Error Handling

The API returns standard HTTP status codes:

- `200` - Success
- `201` - Created
- `400` - Bad Request
- `401` - Unauthorized
- `404` - Not Found
- `422` - Validation Error
- `500` - Internal Server Error

Error responses include detailed messages to help with debugging.

---

## Development

### Running in Development Mode

```bash
fastapi dev main.py
```

### Environment Variables

Make sure to set strong secret keys in production and never commit your `.env` file to version control.

---

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.
