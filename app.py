from openai import OpenAI
import streamlit as st
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import Pinecone
from catboost import CatBoostClassifier
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="PCOS Diagnosis", page_icon=":female_sign:")


#col1, col2 = st.columns([1, 5])

#col1.image("intergene.jpeg", width=100) 
#col2.markdown("<h1 style='color: green;font-family: Times New Roman;font-size: 40px;'>Intergene Biosciences Pvt Ltd.</h1>", unsafe_allow_html=True)


st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("<h1 style='font-size: 30px;color:green'>Polycystic Ovary Syndrome (PCOS) Early Detection</h1>", unsafe_allow_html=True)
st.markdown("")
st.markdown("")
st.markdown("Take this Questionnaire to Discover if a PCOS test is Required:")

st.session_state["model_result"] = None

def predict_with_model(inputs):
    param=["-" for i in range(5)]
    param[0]=float(inputs[0])
    param[1]=2 if inputs[1]=='R' or inputs[1]=='r' else 4
    param[2]=float(inputs[2])
    param[3]=float(inputs[3])/((float(inputs[4])/100)**2)
    param[4]=float(inputs[5])
    for i in range(6,len(inputs)):
        if inputs[i].isalpha():
            if inputs[i].lower()=='yes':
                param.append(1)
            else:
                param.append(0)
    model = CatBoostClassifier()   
    model.load_model('catboost_model')
    y=model.predict(param)
    if y:
        return "You most probably have PCOS, [click here](http://www.example.com) to order the at home self testing kit."
    else:
        return "You most probably do not have PCOS."


def collect_user_inputs():
    with st.form(key='user_input_form'):
        attributes = []
        questions = [
    "How old are you?",
    "Do you experience regular (R) or irregular (I) menstrual cycles?",
    "On average, how many days is your menstrual cycle?",
    "What is your weight in kg?",
    "What is your height in cm?",
    "Provide the ratio of your waist circumference to hip circumference.",
    "Have you experienced significant weight gain recently? (Yes/No)",
    "Have you noticed increased hair growth on your body or face? (Yes/No)",
    "Is there any noticeable darkening of your skin? (Yes/No)",
    "Have you experienced hair loss? (Yes/No)",
    "Do you frequently experience pimples or acne? (Yes/No)",
    "Do you consume fast food regularly? (Yes/No)",
    "Do you engage in regular exercise? (Yes/No)"]

        for i in range(13):
            attribute = st.text_input(questions[i], key=f"attribute_{i}")
            attributes.append(attribute)
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            st.session_state["model_result"] = predict_with_model(attributes)
            st.session_state["model_completed"] = True




def context(query):
    docs = retriever.get_relevant_documents(query)
    return "\n\n".join(doc.page_content for doc in docs)




if "model_completed" not in st.session_state:
    st.session_state["model_completed"] = False



client = OpenAI()
embeddings = OpenAIEmbeddings()
vectorstore = Pinecone( embedding=embeddings)
retriever = vectorstore.as_retriever()


collect_user_inputs()

if st.session_state["model_result"] is not None:
    st.write(f"Result: {st.session_state['model_result']}")

if st.session_state["model_completed"]:
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    if "messages" not in st.session_state or not st.session_state.messages:
        st.session_state.messages = [{"role": "assistant", "content": "Do you have any other questions about PCOS?","context":""}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Enter you query"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        context = context(prompt)

        system_prompt_template = """
        Answer the user's questions based on the below context. 
        If the context doesn't contain any relevant information to the question, don't make something up and just say "I don't have information about this topic. Do you have any other questions related to PCOS?" just say this and nothing else:

        <context>
        {context}
        </context>
        """

        system_prompt = system_prompt_template.format(context=context)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ]
            messages.append({"role":"system","content":system_prompt})
            for response in client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=messages,
                stream=True,
            ):
                full_response += (response.choices[0].delta.content or "")
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
