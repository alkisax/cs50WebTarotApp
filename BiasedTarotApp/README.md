# Biased Tarot Reading Web Application

**Name:** Pelopidas Kopakakis
**GitHub Username:** Alkisax
**edX Username:** PelopKop
**City and Country:** Athens, Greece
**Date of Video:** 13/8/2024
**Video URL:** https://www.youtube.com/watch?v=n66XWSNZfQo

## Description

Welcome to the **Tarot Reading Web Application**, a sophisticated and engaging digital tool crafted to offer **personalized Tarot card readings** with remarkable depth and accuracy. This web-based application is designed to provide users with a **unique and insightful Tarot experience**, leveraging the power of modern AI technology to interpret Tarot cards in relation to individual queries.

The application is tailored for those who seek not just a Tarot reading but a comprehensive exploration of their questions through the lens of Tarot, enhanced by advanced AI interpretation. By utilizing **OpenAI's GPT-4 model**, this application stands out in its ability to deliver nuanced and highly personalized readings that cater to a wide range of emotional and contextual needs.

### Overview

The Tarot Reading Web Application combines the art of Tarot with the cutting-edge capabilities of artificial intelligence to offer users a rich and immersive reading experience. It is designed to cater to a broad audience, from seasoned Tarot enthusiasts to those new to the practice. The application is built to be both user-friendly and powerful, offering features that allow for deep customization and dynamic interaction with the Tarot.

**Key Aspects of the Application Include:**

- **Random Tarot Card Selection:**
  - **Innovative Randomization:** The application starts by generating three Tarot cards randomly from a complete deck of 78. This random selection ensures that each reading is unique and tailored to the moment, providing users with a fresh and dynamic experience every time they use the tool.
  - **Unpredictable Insights:** The randomness of the card selection process adds an element of unpredictability and excitement, making each reading a new journey into the realm of Tarot.

- **Customizable Prompts:**
  - **Flexible Interpretation:** Users can influence the tone and style of their Tarot reading by specifying additional text or flags. This customization allows for a range of interpretations, from positive and uplifting to negative and somber, or even flirtatious.
  - **Enhanced Personalization:** For those seeking even more control, the application supports the use of a custom text file. This feature enables users to provide detailed instructions or thematic elements that tailor the reading to their specific needs or preferences.

- **OpenAI Integration:**
  - **Advanced AI Capabilities:** The application integrates with OpenAI’s GPT-4 model to generate in-depth and contextually relevant interpretations of the drawn Tarot cards. This advanced AI provides a sophisticated analysis that captures the nuances of each card and its relevance to the user’s question.
  - **Contextual Precision:** By leveraging GPT-4, the application ensures that the interpretations are not only accurate but also deeply reflective of the user’s personal inquiry, enhancing the overall quality of the reading.

- **Dynamic Tarot Card Mapping:**
  - **Visual Enhancement:** The application maps each card number to its corresponding Tarot card name and image. This dynamic mapping allows users to visualize the cards drawn, making the reading more engaging and easier to understand.
  - **Comprehensive Visualization:** By including images and detailed descriptions of the cards, the application provides users with a richer, more immersive Tarot experience that goes beyond mere text-based interpretations.

- **Responsive Web Design:**
  - **Intuitive User Interface:** The web interface is designed to be clean, intuitive, and user-friendly. It ensures that users can easily navigate the application, input their questions, and view their readings with minimal effort.
  - **Device Adaptability:** The responsive design guarantees that the application performs well across a variety of devices and screen sizes, from desktop computers to smartphones, providing a seamless experience regardless of how users access the tool.

### How It Works

1. **Card Selection:**
   - **Randomized Drawing:** The backend of the application performs a random draw of three Tarot cards from a complete deck of 78. This process is designed to ensure that the cards selected are unique to each reading.
   - **Card Association:** Each selected card is then associated with its name and meaning, setting the foundation for a personalized Tarot reading.

2. **Prompt Generation:**
   - **Crafting the Query:** Based on the user's input question and any optional flags or additional text, the application generates a tailored prompt for the AI. This prompt guides the GPT-4 model in interpreting the cards in the context of the user’s query.
   - **Customization Options:** Users can influence the prompt with specific instructions or themes, which helps to tailor the interpretation to their individual preferences.

3. **API Interaction:**
   - **Sending the Prompt:** The generated prompt is sent to OpenAI’s API, where the GPT-4 model processes the request and generates a detailed interpretation of the Tarot cards.
   - **Detailed Analysis:** The AI response includes a thorough analysis of each card and its relevance to the user’s question, providing a comprehensive and insightful reading.

4. **Display Results:**
   - **Presenting the Reading:** The results, along with images of the Tarot cards, are displayed through a Flask-based web interface. This presentation is designed to be clear and engaging, making it easy for users to understand and connect with their reading.
   - **User Engagement:** The results are formatted to enhance user engagement, combining visual elements with detailed text to provide a complete and satisfying Tarot reading experience.

### Setup

To deploy and run the Tarot Reading Web Application on your local machine, use the following command:
```bash
python -m flask run

### Customization

**Flags:**

*   **Positive Tone (`-g`):** Utilize this flag to receive a reading characterized by a **positive and optimistic tone**. This option emphasizes uplifting aspects, providing encouraging and supportive insights that focus on the potential for growth and positivity in the situation or question at hand.

*   **Negative Tone (`-b`):** Apply this flag for a reading with a **more somber and cautionary tone**. This option highlights potential challenges, warnings, and areas where caution may be needed. It offers a more realistic and perhaps cautionary perspective on the situation, focusing on obstacles and difficulties that may arise.

*   **Flirtatious Tone (`-l`):** Choose this flag for a reading with a **flirtatious and suggestive style**. This tone adds an element of charm and allure, creating a reading that is engaging and enticing. It implies a focus on aspects related to love, attraction, and personal relationships with a playful and flirtatious twist.

*   **Custom Text (`-t`):** Use this flag to integrate a **custom text file with specific instructions or themes**. This allows for highly personalized and detailed readings, as you can provide unique guidelines or themes that tailor the interpretation to suit specific needs or preferences. Whether it’s detailed instructions or a particular focus, this flag ensures that the reading aligns closely with your desired context.

**Additional Text:**

*   **Adjusting `extraprompt.txt`:** The `extraprompt.txt` file can be modified to **influence the style and tone of the Tarot interpretations**. This feature provides additional flexibility, allowing users to tailor the reading experience to their specific desires or contexts. By editing this file, you can set particular themes, styles, or instructions that affect how the Tarot cards are interpreted, ensuring that the reading meets your unique preferences or requirements. This customization option enhances the ability to align the reading with individual expectations and needs, offering a truly personalized experience.
