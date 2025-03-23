# Text-SummarAIzation-Tool
AI Text Summarization Tool using Streamlit and Hugging Face Transformers.
This AI-Powered Text Summarization tool allows users to upload PDFs or text files, enter text manually, and generate concise summaries using a pre-trained Hugging Face T5 model. The tool also includes dark mode support, summary length control, and a copy-to-clipboard feature.

Features:
✅ Text & File Input Support (PDF & TXT)
✅ Summarization using Hugging Face T5 model
✅ Adjustable Summary Length (Slider Control)
✅ Ensures Full Sentences in Output
✅ Dark Mode Toggle 🌙
✅ Word Count Display (Original & Summary)
✅ Copy Summary to Clipboard


📜 Usage Guide:
1️⃣ Upload a PDF or TXT file, or manually enter text.
2️⃣ Adjust summary length using the slider.
3️⃣ Click "⚡ Generate Summary" to get AI-generated output.
4️⃣ Copy the summary using the 📋 button.
🔹 Dark Mode Support: Click 🌙 Dark Mode to switch themes.

🛠️ How It Works:
🔹 Model: T5-Small
Uses Hugging Face's T5-Small for abstractive summarization.
The model rephrases text instead of just extracting key sentences.
max_length & min_length are dynamically adjusted based on the slider.

🔹 Summary Processing:
Ensures complete sentences by detecting . ! ? at the end.
Capitalizes the first letter of the summary.
Prevents very short summaries by setting a minimum length.

Project Structure:
📂 text-summarizer
 ├── summarizer.py  # Streamlit App Code
 ├── README.md      # Project Documentation
 ├── requirements.txt  # Python Dependencies

 Example Screenshot:
Local URL: http://localhost:8501
Streamlit v1.43.0
https://streamlit.io
summarization

📜 License:
This project is open-source and licensed under the MIT License.

📌 Feel free to contribute and improve the tool! 🚀

🔗 Future Enhancements:
✅ Support for more languages
✅ Better summary accuracy with fine-tuned models
✅ Multi-document summarization
