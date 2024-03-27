# Griaffe AI Lite
### Welcome to Giraffe AI Lite! An AI powered personal knowledge base system.<br>
<p>The heart of Giraffe AI Lite lies in its retrieval-augmented generation approach. By combining retrieval-based techniques with generative models, it achieves accurate and flexible information synthesis. This project is specifically tailored for individuals who have <strong>no experience in AI application development</strong> and <strong>lack access to high-performance computing resources</strong>. 
<p>Here are its key features:<br>
<ol>
  <li><strong>Accessible Learning with LLM</strong>: Giraffe AI utilizes the OpenAI API for vector embeddings and LLM to reduce the need for high-performance computers, rather than using locally sourced LLM. This approach is cost-effective, as the expense of API calls (at $1.5 per million tokens for GPT-3.5 Turbo) is significantly lower than building a PC with a dedicated GPU.</li>
  <li><strong>Lightweight and User-Friendly</strong>: Giraffe AI Lite is designed with a strong emphasis on simplicity and user-friendliness. By intentionally reducing unnecessary functionality—such as compatibility with other embeddings or LLMs—and eliminating a graphical user interface, the project streamlines the user experience. As a result, users won’t need to install an excessive number of libraries, making environmental setup and maintenance significantly easier. </li>
  <li><strong>Self-Query Techniques</strong>: Giraffe AI Lite empowers the retriever with advanced capabilities. Not only does it utilize the user-input query for semantic similarity comparison with stored document contents, but it also extracts filters from the user query based on the metadata of stored documents. These filters are then executed to enhance the precision and flexibility of information retrieval.</li>
</ol>
<p><strong>Explore Giraffe AI Lite and unlock the power of AI without the complexity! 🚀</strong>

## Installation Guide
### 1. Build environment
#### 1.1 Download and install Anaconda from https://www.anaconda.com/
#### 1.2 Create and activate python (version 3.10.0) virtual environment
```
conda create -n GiraffeAI python=3.10.0
conda activate GiraffeAI
```
### 2. Setup Giraffe AI
#### 2.1 Install all required libraries from requirements.txt
```
pip install -r requirements.txt
```
#### 2.2 OpenAI API 
Create a .txt file in the current directory with your OpenAI API Key, rename the file to *openAI_API.txt*<br>
OpenAI API price is listed on https://openai.com/pricing

### 3. Launch Giraffe AI
Run Giraffe_AI_run.py in your virtual environment
```
python Giraffe_AI_run.py
```
## Development Log
### Version 1.0 (3/27/2024)
- Databse: Chroma
- Record management: document upload, removal and replacement
- Source document format: .pdf/.txt
- Embeddings: OpenAI text-embedding-3-small	
- LLM: OpenAI GPT3.5-turbo


