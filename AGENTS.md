# Whether Weather

This project is a Python web application that generates and serves a PNG image with weather information, designed to be used as a home screen widget.

## Project Overview

*   **Purpose:** To provide a dynamic weather image for display in a home screen widget.
*   **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
*   **Key Libraries:**
    *   [Pillow](https://python-pillow.org/): For image generation.
    *   [astral](https://astral.readthedocs.io/en/latest/): For calculating sunrise and dawn times.
    *   [uvicorn](https://www.uvicorn.org/): As the ASGI server.
*   **Deployment:** The application is configured for deployment on [fly.io](https://fly.io/) using a Docker container.

## Building and Running

### Local Development

For a rapid feedback loop during development, open the `preview.html` file in your browser while the development server is running.

1.  **Set up the virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application in development mode:**
    ```bash
    python -m uvicorn app:app --host 0.0.0.0 --port 8000 --reload
    ```

4.  **Open `preview.html` in your browser.** This will show the image from `http://localhost:8000/render` and automatically refresh when you make changes to the code.

### Docker

1.  **Build the Docker image:**
    ```bash
    docker build -t whetherweather .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -p 8000:8000 whetherweather
    ```

## Development Conventions

*   **Linting:** The project uses [Ruff](https://docs.astral.sh/ruff/) for linting. The configuration can be found in `pyproject.toml`.
*   **Coding Style:** The code follows standard Python conventions. Key formatting rules are enforced by Ruff.
