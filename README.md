# AI Chat App

Welcome to the AI Chat App! This project is part of my portfolio and showcases my skills in building conversational AI applications.

## Introduction

The AI Chat App is an API that provides access to a custom-built conversational AI model. This AI is trained specifically to answer questions about me and my projects. Whether you're curious about my technical skills, past experiences, or projects I've worked on, this AI can provide informative responses.


![AI Chat App Demo](![AI Chat App Demo](https://github.com/yourusername/yourrepository/raw/main/path/to/your/gif.gif))

## Features

- Interactive chat interface powered by AI technology
- Available on my portfolio website: [humza-aamir.vercel.app](https://humza-aamir.vercel.app/)

## Installation

To run this project locally, follow these steps:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/humza-Aa/AI_Chat_App.git
2. Navigate to the project directory:
   ```bash
   cd Chatbot_Portfolio
3. Create a virtual environment:
   ```bash
   python -m venv venv
4. Activate the virtual environment:
  - On Windows:
    ```bash
    venv\Scripts\activate
  - On macOS and Linux:
    ```bash
    source venv/bin/activate
5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
6. Run the Flask application:
   ```bash
   flask run
7. Open your web browser and navigate to http://localhost:5000 to use the AI Chat App locally.

## Usage

To interact with the AI, you can send messages to the `/chat` endpoint using the HTTP POST method. Include your message in the body of the request using a form field named "message".

### Example JavaScript Code:
  ```javascript
  try {
    const formData = new FormData();
    formData.append("message", message);
  
    const response = await fetch("https://chat-app-zl6s.onrender.com/chat", {
      method: "POST",
      body: formData,
    });
  
    if (!response.ok) {
      throw new Error("Failed to send message");
    }
  
    // Handle response if needed
    const data = await response.text();
    return data;
  } catch (error) {
    console.error("Error:", error);
  }
```
## Support and Feedback

For any issues or feedback regarding this project, feel free to reach out to me at humzaaamir31@gmail.com.




