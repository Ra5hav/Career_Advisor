{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6a8b2246-1270-4ce1-be98-931d9208a8c4",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-01-12 15:22:16.514 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.515 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.516 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.516 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.517 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.517 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.518 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.518 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.519 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.520 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.520 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.521 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.521 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.522 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.523 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.524 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.525 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.525 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.525 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.526 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.527 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.527 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.528 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.529 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.529 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.530 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.531 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.531 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.532 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.533 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.533 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.534 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.534 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.535 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.535 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.536 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.537 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.537 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.538 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.538 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.538 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.539 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.540 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.540 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.540 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.542 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.542 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.542 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.543 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.543 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.544 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.544 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.544 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.545 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.545 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.546 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.546 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.546 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.547 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.548 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.548 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.549 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.550 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.551 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.551 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.552 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.552 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.553 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.554 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.554 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.555 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.556 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.557 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.558 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.558 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.558 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.559 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.559 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.561 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.561 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.562 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.562 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.563 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.563 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.564 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.564 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.565 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.565 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.566 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.566 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.567 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.567 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.568 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.568 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.569 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.570 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.570 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.571 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.572 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.572 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.572 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.573 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.573 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.574 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.574 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.574 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.575 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.576 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.576 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.577 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.577 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-12 15:22:16.577 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import openai\n",
    "import streamlit as st\n",
    "\n",
    "# Set up OpenAI API key securely (use a secrets manager on deployment)\n",
    "openai.api_key = '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'  # For local testing (never hardcode in production)\n",
    "\n",
    "# Function to get career path suggestions based on profession\n",
    "def get_recommended_paths_for_profession(profession):\n",
    "    prompt = f\"\"\"\n",
    "    If a student wants to pursue a career as a {profession}, list a few career paths they could take and what steps they should follow.\n",
    "    Include steps and fields of study.\n",
    "    \"\"\"\n",
    "    response = openai.Completion.create(\n",
    "        model=\"text-davinci-003\",\n",
    "        prompt=prompt,\n",
    "        max_tokens=1500,\n",
    "        temperature=0.7\n",
    "    )\n",
    "    return response.choices[0].text.strip()\n",
    "\n",
    "# Function to get career-related subjects with detailed descriptions\n",
    "def get_subjects_involved_with_description(profession):\n",
    "    prompt = f\"\"\"\n",
    "    List the core subjects a student will study if they pursue a career in {profession}.\n",
    "    Include the subject names along with a description explaining the main topics of each subject and its relevance to the career.\n",
    "    \"\"\"\n",
    "    response = openai.Completion.create(\n",
    "        model=\"text-davinci-003\",\n",
    "        prompt=prompt,\n",
    "        max_tokens=1500,\n",
    "        temperature=0.7\n",
    "    )\n",
    "    return response.choices[0].text.strip()\n",
    "\n",
    "# Function to analyze mistakes made by students in career choices\n",
    "def get_common_mistakes():\n",
    "    prompt = \"\"\"\n",
    "    Describe common mistakes that students often make when choosing a career path, and provide advice on how they can avoid those mistakes. \n",
    "    Include how personality traits like introversion, decision style, and stress response might impact career choices.\n",
    "    \"\"\"\n",
    "    response = openai.Completion.create(\n",
    "        model=\"text-davinci-003\",\n",
    "        prompt=prompt,\n",
    "        max_tokens=1500,\n",
    "        temperature=0.7\n",
    "    )\n",
    "    return response.choices[0].text.strip()\n",
    "\n",
    "# Streamlit UI\n",
    "st.set_page_config(page_title=\"Career Path Advisor\", layout=\"centered\")\n",
    "\n",
    "st.title(\"Career Path Advisor for Class 10th and 12th Students\")\n",
    "\n",
    "# Brief description\n",
    "st.markdown(\"\"\"\n",
    "This tool provides personalized career advice based on your personality, interests, and preferences. \n",
    "It helps you explore various career paths, subjects to study, and common mistakes to avoid when making career decisions.\n",
    "\"\"\")\n",
    "\n",
    "# Separator\n",
    "st.markdown(\"---\")\n",
    "\n",
    "# Part 1: Profession-Based Career Path Selection\n",
    "st.header(\"Explore Career Paths\")\n",
    "\n",
    "desired_profession = st.text_input(\n",
    "    \"Enter the profession you are interested in (e.g., Doctor, Engineer, Designer, etc.):\",\n",
    "    placeholder=\"Type the profession here...\"\n",
    ")\n",
    "\n",
    "if st.button(\"Get Career Advice\") and desired_profession.strip():\n",
    "    st.subheader(f\"Career Paths to Pursue as a {desired_profession}:\")\n",
    "    \n",
    "    # Fetch career paths for the given profession\n",
    "    career_paths = get_recommended_paths_for_profession(desired_profession)\n",
    "    st.write(career_paths)\n",
    "    \n",
    "    # Display subjects involved in the desired career path\n",
    "    if st.button(f\"Get Subjects Related to {desired_profession}\"):\n",
    "        subjects_info = get_subjects_involved_with_description(desired_profession)\n",
    "        st.subheader(f\"Subjects You Will Study to Pursue a Career in {desired_profession}:\")\n",
    "        st.write(subjects_info)\n",
    "\n",
    "# Separator\n",
    "st.markdown(\"---\")\n",
    "\n",
    "# Part 2: Personality & Behavioral Questionnaire\n",
    "st.header(\"Your Personality and Career Fit\")\n",
    "\n",
    "st.markdown(\"\"\"\n",
    "Understanding your personality, learning style, and behavior will help us recommend the most suitable career paths for you.\n",
    "Please answer the following questions to assist with our analysis.\n",
    "\"\"\")\n",
    "\n",
    "motivation_type = st.text_area(\n",
    "    \"What motivates you the most? (e.g., personal satisfaction, external rewards like money, impact on others)\"\n",
    ")\n",
    "\n",
    "learning_style = st.text_area(\n",
    "    \"What is your preferred learning style? (e.g., visual, auditory, hands-on experience)\"\n",
    ")\n",
    "\n",
    "teamwork_independence = st.text_area(\n",
    "    \"How do you prefer to work? (e.g., independently, as part of a team, or a mix of both)\"\n",
    ")\n",
    "\n",
    "time_management = st.text_area(\n",
    "    \"How do you manage time and deadlines? (e.g., do you plan well in advance or work better under pressure?)\"\n",
    ")\n",
    "\n",
    "stress_response = st.text_area(\n",
    "    \"How do you typically respond to stress and pressure? (e.g., remain calm, feel anxious, get overwhelmed)\"\n",
    ")\n",
    "\n",
    "problem_solving = st.text_area(\n",
    "    \"When faced with a problem, what is your usual approach? (e.g., do you analyze the situation logically, think creatively, or seek advice?)\"\n",
    ")\n",
    "\n",
    "# Button to analyze mistakes students make when choosing careers\n",
    "if st.button(\"Learn Common Mistakes Students Make When Choosing Careers\"):\n",
    "    mistakes_advice = get_common_mistakes()\n",
    "    st.subheader(\"Common Mistakes in Career Decision Making\")\n",
    "    st.write(mistakes_advice)\n",
    "\n",
    "# Separator\n",
    "st.markdown(\"---\")\n",
    "\n",
    "# Part 3: Desired Future Life\n",
    "st.header(\"What Kind of Life Do You Want in the Future?\")\n",
    "\n",
    "st.markdown(\"\"\"\n",
    "Share your lifestyle preferences and work environment expectations to help us suggest career paths that align with your vision of the future.\n",
    "\"\"\")\n",
    "\n",
    "work_life_balance = st.text_area(\n",
    "    \"What type of work-life balance would you like? (e.g., highly demanding career, balanced lifestyle, flexibility)\"\n",
    ")\n",
    "\n",
    "income_expectations = st.text_area(\n",
    "    \"What kind of salary range would you expect in the future? (e.g., high-paying, comfortable salary, modest income but fulfilling)\"\n",
    ")\n",
    "\n",
    "career_flexibility = st.text_area(\n",
    "    \"Would you prefer a structured career path or a flexible one? (e.g., clear roles vs variety and freedom)\"\n",
    ")\n",
    "\n",
    "location_preference = st.text_area(\n",
    "    \"Where would you like to work and live? (e.g., big city, small town, remote work, abroad)\"\n",
    ")\n",
    "\n",
    "social_impact = st.text_area(\n",
    "    \"How important is social impact to you in your career? (e.g., very important, somewhat important, not a priority)\"\n",
    ")\n",
    "\n",
    "if st.button(\"Get Career Recommendations Based on Your Lifestyle Preferences\"):\n",
    "    st.subheader(\"Your Future Life Preferences\")\n",
    "    st.write(\"We are analyzing your responses and providing customized career suggestions!\")\n",
    "\n",
    "# Separator\n",
    "st.markdown(\"---\")\n",
    "\n",
    "# Footer with closing message\n",
    "st.markdown(\"\"\"\n",
    "Remember, career decisions are a reflection of your personality, interests, and life goals. Trust yourself and take one step at a time towards building the future you dream of. Feel free to revisit this tool anytime for more guidance.\n",
    "\"\"\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c2e6707-801c-42a3-82b7-701a1a53b37f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
