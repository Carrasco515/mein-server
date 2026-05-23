# Mein Server

This is my first practical DevOps learning project.

## Goal

The goal of this project is to learn how to build, containerize and run a small API with Docker and Docker Compose.

## Tech Stack

Python  
FastAPI  
Docker  
Docker Compose  
Git  
GitHub  

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Returns the main status message |
| GET | /health | Returns the health status of the application |
| GET | /docs | Opens the automatic FastAPI documentation |

## Run the project

```bash
docker compose up --build
