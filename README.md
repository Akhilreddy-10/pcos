# PCOS Early Detection Application

This is a web-based tool for the early detection of Polycystic Ovary Syndrome (PCOS) using a questionnaire. The project is built using Streamlit, OpenAI's GPT model, and CatBoostClassifier for prediction. The tool provides an easy-to-use interface for users to answer a series of questions, which will then be analyzed to predict the likelihood of PCOS.

## Features

- **PCOS Prediction**: Uses a machine learning model to predict the likelihood of PCOS based on user inputs.
- **Interactive Questionnaire**: Users can fill in a form with details about their age, menstrual cycle, body measurements, and symptoms.
- **Chat-based Interaction**: Integrates OpenAI’s GPT for answering questions related to PCOS.
- **Dynamic Content**: Provides tailored feedback based on the user’s responses.
- **Health Tips**: Links to additional resources for PCOS testing and self-care.

## How It Works

1. **User Inputs**: The user fills out a questionnaire with personal information and symptoms related to PCOS.
2. **Prediction**: A trained CatBoost model uses the input to predict the likelihood of PCOS.
3. **Result**: The application displays a message informing the user if they should consider testing for PCOS and provides a link for further action.
4. **Chatbot**: The chatbot answers questions about PCOS based on a retrieval system using Langchain and OpenAI's models.

## Technologies Used

- **Streamlit**: For building the web interface.
- **OpenAI**: For language models and embeddings.
- **Pinecone**: For vector storage and document retrieval.
- **CatBoost**: For the machine learning model used to predict PCOS.
- **Langchain**: For handling OpenAI's embedding and Pinecone's vector search.
- **Python**: Core programming language.

## Installation

To run the application locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/pcos-diagnosis-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd pcos-diagnosis-app
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Download or train the CatBoost model and save it as `catboost_model` in the project root folder.

5. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## Usage

Once the app is running, follow these steps:

1. Answer the questions in the questionnaire to help determine if you may have PCOS.
2. Click "Submit" after entering your responses.
3. The app will display a prediction result based on your answers.
4. You can also ask questions about PCOS using the chat interface.

## File Structure
- app.py                        (Main application file)
- catboost_model                (Trained CatBoost model for PCOS prediction)
- README.md                     (Documentation for the project)
- requirements.txt              (Dependencies required for the project)
- intergene.jpeg                (Logo or image (optional))

## Model Explanation

The **CatBoost Classifier** model predicts the likelihood of PCOS based on the following inputs:
- Age
- Menstrual cycle regularity
- Weight and height
- Waist-to-hip ratio
- Other symptoms (e.g., acne, hair loss, etc.)

## Future Enhancements

- **Better Model Accuracy**: Further tuning of the CatBoost model with additional data.
- **Additional Features**: Provide more detailed health advice and self-care tips.
- **Mobile Responsiveness**: Improve the UI to be mobile-friendly.

## License

This project is licensed under the MIT License.


