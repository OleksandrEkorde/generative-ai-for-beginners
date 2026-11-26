# Setup Your Dev Environment

We setup this repository and course with a [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) that has a Universal runtime that can support Python3, .NET, Node.js and Java development. The related configuration is defined in the `devcontainer.json` file located in the `.devcontainer/` folder at the root of this repository.

To activate the dev container, launch it in [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (for a cloud-hosted runtime) or in [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (for a local device-hosted runtime). Read [this documentation](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) for more details on how dev containers work within VS Code.  

> [!TIP]  
> We recommend using GitHub Codespaces for a quick start with minimal effort. It provides a generous [free usage quota](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) for personal accounts. Configure [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) to stop or delete inactive codespaces to maximize your quota usage.


## 1. Executing Assignments

Each lesson will have _optional_ assignments that may be provided in one or more programming languages including: Python, .NET/C#, Java and JavaScript/TypeScript. This section provides general guidance related to executing those assignments.

### 1.1 Python Assignments

Python assignments are provided either as applications (`.py` files) or Jupyter notebooks (`.ipynb` files). 
- To run the notebook, open it in Visual Studio Code then click _Select Kernel_ (at top right) and select the default Python 3 option shown. You can now _Run All_ to execute the notebook.
- To run Python applications from command-line, follow assignment-specific instructions to ensure you select the right files and provide required arguments

## 2. Configuring Providers

Assignments are configured to work with Large Language Models (LLMs) through the **Google Gemini API**. Gemini provides a _hosted endpoint_ (API) that we can access programmatically with an API key. In this course we use these providers:

 - [Google Gemini](https://ai.google.dev/gemini-api/docs/models) — the main course provider (Gemini models for text generation and embeddings).
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) for open-source models and inference server (optional).

**You will need to use your own Google account for these exercises**. Some guidance for signup:

| Signup | Cost | API Key | Playground | Comments |
|:---|:---|:---|:---|:---|
| [Google AI Studio](https://aistudio.google.com/) | [Pricing](https://ai.google.dev/gemini-api/docs/pricing) (free tier available) | [Get API key](https://aistudio.google.com/app/apikey) | [Google AI Studio](https://aistudio.google.com/) | Multiple Gemini models available |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Pricing](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat has limited models](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

### 2.1. Create `.env` file

We assume that you have already signed up with Google AI Studio and obtained a Gemini API key.

The next step is to configure your **local environment variables** as follows:

1. Look in the root folder for a `.env.copy` file that should have contents like this:

   ```bash
   # Google Gemini Provider
   GEMINI_API_KEY='<add your Gemini API key here>'
   GEMINI_MODEL='gemini-3.8-flash' # Default is set!
   GEMINI_EMBEDDING_MODEL='gemini-embedding-001' # Default is set!

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Copy that file to `.env` using the command below. This file is _gitignore-d_, keeping secrets safe.

   ```bash
   cp .env.copy .env
   ```

3. Fill in the values (replace placeholders on right side of `=`) as described in the next section.

4. (Optional) If you use GitHub Codespaces, you can save environment variables as _Codespaces secrets_ associated with this repository. In that case, you won't need a local .env file. **This option works only with GitHub Codespaces.** You will still need the .env file if you use Docker Desktop or a local environment.

### 2.2. Populate `.env` file

| Variable  | Description  |
| :--- | :--- |
| GEMINI_API_KEY | The authorization key for the Google Gemini API |
| GEMINI_MODEL | The _text generation_ model (default `gemini-3.8-flash`) |
| GEMINI_EMBEDDING_MODEL | The _text embeddings_ model (default `gemini-embedding-001`) |
| HUGGING_FACE_API_KEY | The user access token you setup in your Hugging Face profile |
| | |

### 2.3 Configure Gemini: Google AI Studio

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey) and sign in with your Google account.
1. Click **Create API key** and select or create a Google Cloud project.
1. Copy the key into the `GEMINI_API_KEY` variable in the `.env` file.
1. Install the Python SDK: `pip install google-genai python-dotenv`

Example usage:

```python
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
response = client.models.generate_content(
    model=os.getenv("GEMINI_MODEL", "gemini-3.8-flash"),
    contents="Hi! Explain what generative AI is.",
)
print(response.text)
```

Don't post or share your key publicly. **Don't forget to save the .env file when done**.

### 2.4 Configure Hugging Face: From Profile

Your Hugging Face token can be found in your profile under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Don't post or share these publicly. Instead, create a new token for this project usage and copy that into the `.env` file under the `HUGGING_FACE_API_KEY` variable. _Note:_ This is technically not an API key but is used for authentication so we are keeping that naming convention for consistency.
