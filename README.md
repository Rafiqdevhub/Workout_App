# Workout App

A modern and user-friendly workout application built using Next.js 15 for the frontend with TailwindCSS and FastAPI for the backend.

## Features

- **User Authentication**: Secure login and signup system.
- **Responsive UI**: Built with TailwindCSS for a seamless experience across devices.
- **API Integration**: FastAPI backend for efficient data handling.

## Tech Stack

### Frontend

- Next.js 15
- TailwindCSS

### Backend

- FastAPI
- JWT Authentication

## Installation

### Prerequisites

- Node.js and npm/yarn installed
- Python 3.9+ installed

### Frontend Setup

```sh
cd frontend
npm install
npm run dev
```

### Backend Setup

```sh
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use `.\.venv\Scripts\activate`
pip install -r requirements.txt
uvicorn main:app --reload
```

## Environment Variables

Create a `.env` file in the backend directory and add:

DATABASE_URL=
SECRET_KEY=your_secret_key
