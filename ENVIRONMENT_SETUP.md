# Environment Configuration Guide

## Step 3: Environment Configuration

You need to create a `.env` file in your `navi_chat_backend` directory with the following environment variables:

### 1. Create .env file

Create a file named `.env` in the `navi_chat_backend` directory with the following content:

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/navi_chat_db
TEST_DATABASE_URL=postgresql://user:password@localhost:5432/navi_chat_test_db

# Security
SECRET_KEY=your-super-secret-key-here-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# External Services
MAPBOX_ACCESS_TOKEN=your_mapbox_token_here
DIALOGFLOW_PROJECT_ID=your_dialogflow_project_id
DIALOGFLOW_PRIVATE_KEY_ID=your_private_key_id
DIALOGFLOW_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
DIALOGFLOW_CLIENT_EMAIL=your_service_account_email

# Firebase
FIREBASE_PROJECT_ID=your_firebase_project_id
FIREBASE_PRIVATE_KEY_ID=your_firebase_private_key_id
FIREBASE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
FIREBASE_CLIENT_EMAIL=your_firebase_client_email

# Redis (for caching)
REDIS_URL=redis://localhost:6379

# App Settings
DEBUG=True
ENVIRONMENT=development
CORS_ORIGINS=["http://localhost:3000", "http://localhost:8080"]
```

### 2. Update .gitignore

Make sure your `.gitignore` file includes:

```gitignore
# Environment variables
.env
.env.local
.env.*.local

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```

### 3. Generate a Secure Secret Key

For the `SECRET_KEY`, you can generate a secure key using Python:

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 4. Development vs Production

For development, you can use placeholder values for external services. For production, you'll need to:

- Set up a PostgreSQL database (Supabase recommended)
- Create a Firebase project and get service account credentials
- Set up a Dialogflow project and get service account credentials
- Get a Mapbox access token
- Set up Redis for caching

### 5. Test Configuration

To test if your configuration is working, you can run:

```bash
cd navi_chat_backend
python -c "from app.config import settings; print('Configuration loaded successfully')"
```

### Next Steps

Once you've created the `.env` file, we can proceed to:
1. **Step 4**: Database Setup
2. **Step 5**: Models Setup
3. **Step 6**: Schemas Setup

Would you like me to help you with any of these next steps?
