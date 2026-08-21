# talennt_nation
# a repository were all my lesson from talent nation is been put to practice, all the project's iv'e done so far are here all




## Smart Toaster Verification Service

An automated notification and email verification utility built in Python. This service handles email authentication and notification dispatch for toaster device events using Google SMTP SSL integration and environment variable protection.

---

## Features

* **Email Notification Dispatch:** Automatically constructs and sends plain-text verification emails and status alerts via Gmail SMTP.
* **Environment Variable Protection:** Employs `.env` configuration files to keep sender credentials and app passwords secure.
* **Terminal Diagnostics:** Built-in test execution scripts to verify SMTP configuration and credential authorization independently.

---

## Project Structure

```text
smart_toaster/
├── .env.example            # Environment variable template
├── .gitignore              # Git ignore rules for private environment files
├── email_verification.py   # Core verification and email dispatch module
└── toaster.py              # Main appliance event logic and execution flow
```




## AI-Powered Transaction Logger & Negotiation Service

An interactive CLI transaction logger built in Python that integrates with Groq's LLM APIs (`qwen/qwen3.6-27b` / `groq/compound-mini`) to perform real-time price estimations and multi-turn price negotiations, automatically issuing email receipts upon purchase confirmation.

---

## Features

* **AI Price Estimation & Negotiation:** Uses Groq's LLM models to provide realistic market price estimates and manage dynamic interactive chat negotiations with buyers.
* **PIN Validation & Security:** Secure payment loop requiring 4-digit numeric PIN inputs for transaction processing.
* **Automated Email Receipts:** Dispatches clean, formatted transaction receipts directly to buyers via Google SMTP SSL integration.
* **Colored Terminal Output:** Uses ANSI escape sequences to provide visual feedback and formatted transaction logs in the terminal interface.
* **Environment Variable Protection:** Stores API keys and sensitive app credentials securely using `.env` configurations.

---

## Project Structure

```text
transaction_logger/
├── .env.example        # Environment variable template
├── .gitignore          # Git ignore rules for sensitive credentials
├── ai_service.py       # Groq API integration and price lookup logic
├── email_sender.py     # TransactionEmailer SMTP receipt delivery module
└── logger.py           # Main CLI application entry point and payment flow
