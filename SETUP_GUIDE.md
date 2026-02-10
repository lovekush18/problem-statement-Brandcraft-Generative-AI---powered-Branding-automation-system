# 🎨 BrandArc - Complete Modular API Setup Guide

## 📁 Project Structure

```
brandarc-project/
├── backend/                    # Flask API Backend
│   ├── api/                   # API Routes (Blueprints)
│   │   ├── __init__.py
│   │   ├── brand.py          # Brand generation endpoints
│   │   ├── logo.py           # Logo generation endpoints
│   │   ├── auth.py           # Authentication endpoints
│   │   └── chat.py           # AI chat endpoints
│   │
│   ├── services/              # Business Logic Layer
│   │   ├── __init__.py
│   │   ├── brand_service.py  # Brand generation logic
│   │   ├── logo_service.py   # Logo generation logic
│   │   ├── auth_service.py   # Authentication logic
│   │   └── chat_service.py   # AI chat logic
│   │
│   ├── utils/                 # Utility Functions
│   │   ├── __init__.py
│   │   ├── validators.py     # Input validation
│   │   └── responses.py      # Standard API responses
│   │
│   ├── app.py                 # Main Flask application
│   ├── config.py              # Configuration settings
│   └── requirements.txt       # Python dependencies
│
├── frontend/                  # Frontend Application
│   ├── js/
│   │   └── api-client.js     # JavaScript API client library
│   └── index.html             # Main frontend interface
│
└── API_DOCUMENTATION.md       # Complete API documentation
```

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Start the Backend Server

```bash
cd backend
python app.py
```

The server will start at `http://localhost:5000`

### 3. Open the Frontend

Open `frontend/index.html` in your browser, or use a local server:

```bash
# Using Python
cd frontend
python -m http.server 8080

# Or using Node.js
cd frontend
npx serve
```

Then visit `http://localhost:8080`

---

## 🎯 Features

### ✅ Modular Architecture
- Separated concerns (API routes, business logic, utilities)
- Easy to maintain and extend
- Professional project structure

### ✅ Complete API Endpoints

**Brand Generation:**
- Generate unique brand names
- Check domain/trademark availability
- Get quick suggestions

**Logo Creation:**
- Generate logo concepts in various styles
- Customize existing logos
- Export in multiple formats

**Authentication:**
- User signup and login
- Token-based authentication
- Profile management

**AI Chat:**
- Context-aware branding assistance
- Multiple response modes
- Chat history

**Additional Services:**
- Color palette generation
- Content creation (taglines, descriptions)
- Complete design system generation

### ✅ Frontend API Client
- Clean JavaScript library
- Automatic authentication handling
- Promise-based async/await syntax
- Error handling built-in

---

## 📚 API Documentation

See [API_DOCUMENTATION.md](./API_DOCUMENTATION.md) for complete API reference.

### Quick Examples

**Generate Brand Names:**
```javascript
const api = new BrandArcAPI('http://localhost:5000');

const response = await api.generateBrandNames({
  industry: 'Technology',
  keywords: 'AI, Smart, Future',
  tone: 'Modern',
  count: 10
});

console.log(response.data.names);
```

**User Authentication:**
```javascript
// Signup
await api.signup('user@example.com', 'password123', 'John Doe');

// Login
await api.login('user@example.com', 'password123');

// Get profile
const profile = await api.getProfile();

// Logout
await api.logout();
```

**Generate Logos:**
```javascript
const logos = await api.generateLogos({
  brandName: 'BrandArc',
  style: 'modern',
  colors: ['#6366f1', '#8b5cf6']
});
```

**AI Chat:**
```javascript
const chat = await api.sendChatMessage('Help me with brand naming');
console.log(chat.data.response);
```

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the `backend/` directory:

```env
# Server Configuration
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
PORT=5000
HOST=0.0.0.0

# CORS Settings
CORS_ORIGINS=http://localhost:3000,http://localhost:8080

# Database (for future use)
DATABASE_URL=postgresql://user:password@localhost/brandarc

# API Keys (for future integrations)
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key
```

### Configuration Files

Edit `backend/config.py` to customize:
- Server settings
- CORS origins
- Rate limits
- Generation defaults

---

## 🧪 Testing

### Test Backend Endpoints

**Using cURL:**
```bash
# Health check
curl http://localhost:5000/health

# Generate brands
curl -X POST http://localhost:5000/api/brand/generate \
  -H "Content-Type: application/json" \
  -d '{"industry":"Technology","keywords":"AI","tone":"Modern","count":5}'

# Login
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password123"}'
```

**Using the Frontend:**
1. Open `frontend/index.html` in your browser
2. Check the connection status (green dot = connected)
3. Test each feature:
   - Brand Names tab
   - Logos tab
   - AI Chat tab
   - Account tab

---

## 📦 API Client Usage

Include the API client in your HTML:

```html
<script src="frontend/js/api-client.js"></script>
<script>
  const api = new BrandArcAPI('http://localhost:5000');
  
  // Use the API
  async function generateBrands() {
    const response = await api.generateBrandNames({
      industry: 'Technology',
      keywords: 'AI, Smart',
      tone: 'Modern'
    });
    
    response.data.names.forEach(brand => {
      console.log(brand.name);
    });
  }
</script>
```

### API Client Methods

**Brand:**
- `generateBrandNames(params)`
- `checkAvailability(brandName)`
- `getBrandSuggestions(industry, tone)`

**Logo:**
- `generateLogos(params)`
- `customizeLogo(logoId, colors, text)`
- `exportLogo(svg, format)`

**Authentication:**
- `signup(email, password, name)`
- `login(email, password)`
- `logout()`
- `verifyToken()`
- `getProfile()`
- `updateProfile(data)`

**Chat:**
- `sendChatMessage(message, timeLimit, context)`
- `getChatHistory()`
- `clearChatHistory()`

**Other Services:**
- `generatePalettes(baseColor, scheme)`
- `generateContent(params)`
- `generateDesignSystem(brandName)`

**Utilities:**
- `healthCheck()`
- `setToken(token)`
- `clearToken()`
- `isAuthenticated()`

---

## 🔒 Security Best Practices

### For Production:

1. **Password Hashing:**
```python
# Install bcrypt
pip install bcrypt

# In auth_service.py
import bcrypt

# Hash password
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Verify password
bcrypt.checkpw(password.encode('utf-8'), hashed)
```

2. **Use JWT Tokens:**
```python
# Install PyJWT
pip install PyJWT

# Generate token
import jwt
token = jwt.encode({'user_id': user_id}, SECRET_KEY, algorithm='HS256')

# Verify token
payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
```

3. **Environment Variables:**
- Never commit `.env` files
- Use different secrets for dev/prod
- Store secrets securely

4. **HTTPS Only:**
- Use SSL certificates in production
- Redirect HTTP to HTTPS

5. **Rate Limiting:**
```python
# Install Flask-Limiter
pip install Flask-Limiter

from flask_limiter import Limiter

limiter = Limiter(app, default_limits=["100 per hour"])
```

---

## 🗄️ Database Integration (Future)

To add persistent storage:

1. **Install SQLAlchemy:**
```bash
pip install flask-sqlalchemy psycopg2-binary
```

2. **Create Models:**
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(100))
```

3. **Update Services:**
Replace in-memory storage with database queries.

---

## 🚢 Deployment

### Using Docker

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install -r requirements.txt

COPY backend/ .

EXPOSE 5000

CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t brandarc-api .
docker run -p 5000:5000 brandarc-api
```

### Using Heroku

```bash
heroku create brandarc-api
git push heroku main
```

### Using AWS/GCP/Azure

See deployment documentation for your chosen platform.

---

## 📈 Extending the API

### Adding New Endpoints

1. **Create New Service:**
```python
# backend/services/new_service.py
class NewService:
    def do_something(self, params):
        # Business logic here
        return result
```

2. **Create API Blueprint:**
```python
# backend/api/new_endpoint.py
from flask import Blueprint
from services.new_service import NewService

new_bp = Blueprint('new', __name__)
service = NewService()

@new_bp.route('/action', methods=['POST'])
def action():
    # Handle request
    return jsonify(result)
```

3. **Register Blueprint:**
```python
# backend/app.py
from api.new_endpoint import new_bp

app.register_blueprint(new_bp, url_prefix='/api/new')
```

4. **Add to API Client:**
```javascript
// frontend/js/api-client.js
async doNewAction(params) {
    return this.request('/api/new/action', {
        method: 'POST',
        body: JSON.stringify(params)
    });
}
```

---

## 🐛 Troubleshooting

### Backend Won't Start
```bash
# Check Python version
python --version  # Should be 3.8+

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Check port availability
lsof -i :5000  # On Unix
netstat -ano | findstr :5000  # On Windows
```

### CORS Errors
- Update `CORS_ORIGINS` in `config.py`
- Make sure backend is running
- Check browser console for specific error

### Connection Refused
- Verify backend is running: `curl http://localhost:5000/health`
- Check firewall settings
- Ensure correct URL in frontend

### Import Errors
```bash
# Make sure you're in the backend directory
cd backend

# Run with Python module syntax
python -m app
```

---

## 📝 Development Workflow

1. **Start Backend:**
```bash
cd backend
python app.py
```

2. **Make Changes:**
- Edit service files for business logic
- Edit API files for endpoints
- Backend auto-reloads in debug mode

3. **Test Changes:**
- Use frontend interface
- Or use cURL/Postman
- Check logs in terminal

4. **Update Frontend:**
- Modify `frontend/index.html` for UI
- Update `frontend/js/api-client.js` for API calls

---

## 🎓 Learning Resources

- **Flask Documentation:** https://flask.palletsprojects.com/
- **REST API Best Practices:** https://restfulapi.net/
- **JavaScript Fetch API:** https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API

---

## 📄 License

MIT License - Feel free to use and modify as needed.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## 📧 Support

For issues or questions:
1. Check the troubleshooting section
2. Review API documentation
3. Check server logs
4. Open an issue on GitHub

---

**Happy Coding! 🚀**

Your modular, production-ready BrandArc API is ready to use and extend!
