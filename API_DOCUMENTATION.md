# BrandArc API Documentation

## Base URL
```
http://localhost:5000
```

## Authentication
Most endpoints require authentication via Bearer token in the Authorization header:
```
Authorization: Bearer <your-token>
```

---

## 🏷️ Brand API

### Generate Brand Names
Generate unique brand name suggestions.

**Endpoint:** `POST /api/brand/generate`

**Request Body:**
```json
{
  "industry": "Technology",
  "keywords": "AI, Smart, Future",
  "tone": "Modern",
  "count": 10
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "names": [
      {
        "id": "brand_1_1234567890",
        "name": "NexusAI",
        "domain": "nexusai.com",
        "domainAvailable": true,
        "domainScore": 85,
        "trademarkAvailable": true,
        "trademarkScore": 78,
        "memorabilityScore": 92,
        "description": "A modern technology brand...",
        "alternativeDomains": ["nexusai.io", "nexusai.ai"]
      }
    ],
    "count": 10,
    "industry": "Technology",
    "tone": "Modern"
  }
}
```

### Check Availability
Check domain and trademark availability for a brand name.

**Endpoint:** `POST /api/brand/check-availability`

**Request Body:**
```json
{
  "name": "BrandArc"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "name": "BrandArc",
    "domain": {
      "available": true,
      "price": 15,
      "alternatives": ["brandarc.io", "brandarc.ai"]
    },
    "trademark": {
      "available": true,
      "conflicts": []
    },
    "social": {
      "twitter": true,
      "instagram": false,
      "facebook": true
    }
  }
}
```

### Get Suggestions
Get quick brand suggestions without keywords.

**Endpoint:** `GET /api/brand/suggestions?industry=Technology&tone=Modern`

**Response:**
```json
{
  "success": true,
  "data": {
    "suggestions": [...]
  }
}
```

---

## 🎨 Logo API

### Generate Logos
Create logo design concepts.

**Endpoint:** `POST /api/logo/generate`

**Request Body:**
```json
{
  "brandName": "BrandArc",
  "style": "modern",
  "colors": ["#6366f1", "#8b5cf6"],
  "count": 8
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "logos": [
      {
        "id": "logo_1",
        "style": "minimalist",
        "brandName": "BrandArc",
        "colors": ["#6366f1", "#8b5cf6"],
        "svg": "<svg>...</svg>",
        "description": "Minimalist logo design...",
        "variations": [...]
      }
    ],
    "count": 8
  }
}
```

### Customize Logo
Customize an existing logo.

**Endpoint:** `POST /api/logo/customize`

**Request Body:**
```json
{
  "logoId": "logo_1",
  "colors": ["#ff0000", "#00ff00"],
  "text": "NewBrand"
}
```

### Export Logo
Export logo in different formats.

**Endpoint:** `POST /api/logo/export/{format}`

Supported formats: `svg`, `png`, `pdf`

**Request Body:**
```json
{
  "svg": "<svg>...</svg>"
}
```

---

## 🎨 Palette API

### Generate Color Palettes
Generate color scheme suggestions.

**Endpoint:** `POST /api/palette/generate`

**Request Body:**
```json
{
  "baseColor": "#6366f1",
  "scheme": "complementary"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "palettes": [
      {
        "id": "palette_1",
        "name": "Complementary Palette 1",
        "colors": ["#6366f1", "#f1a663", "#63f1a6"],
        "scheme": "complementary"
      }
    ]
  }
}
```

---

## 📝 Content API

### Generate Content
Create marketing content (taglines, descriptions, social posts).

**Endpoint:** `POST /api/content/generate`

**Request Body:**
```json
{
  "type": "tagline",
  "brandName": "BrandArc",
  "industry": "Technology",
  "tone": "Professional"
}
```

**Content Types:**
- `tagline` - Brand taglines
- `description` - Product/company descriptions
- `social` - Social media posts

**Response:**
```json
{
  "success": true,
  "data": {
    "content": [
      {
        "text": "BrandArc - Where Innovation Meets Excellence",
        "type": "tagline",
        "tone": "Professional",
        "length": 45
      }
    ]
  }
}
```

---

## 🎨 Design System API

### Generate Design System
Create a complete design system with colors, typography, spacing.

**Endpoint:** `POST /api/design-system/generate`

**Request Body:**
```json
{
  "brandName": "BrandArc"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "designSystem": {
      "colors": {
        "primary": "#6366f1",
        "secondary": "#8b5cf6",
        ...
      },
      "typography": {
        "fontFamily": "'Inter', sans-serif",
        "fontSize": { ... },
        "fontWeight": { ... }
      },
      "spacing": { ... },
      "borderRadius": { ... },
      "shadows": { ... }
    }
  }
}
```

---

## 💬 Chat API

### Send Message
Send a message to the AI assistant.

**Endpoint:** `POST /api/chat/send`

**Request Body:**
```json
{
  "message": "Help me with brand naming",
  "timeLimit": "normal",
  "context": {}
}
```

**Time Limits:**
- `urgent` - Quick answer
- `fast` - Fast response
- `normal` - Standard (default)
- `detailed` - Detailed answer
- `comprehensive` - Comprehensive response
- `expert` - Expert analysis

**Response:**
```json
{
  "success": true,
  "data": {
    "response": [
      "Quick tip: Focus on memorability...",
      "How-to checklist: ..."
    ],
    "timestamp": "2024-01-01T12:00:00",
    "suggestions": [
      "Generate some brand names",
      "What makes a good brand name?"
    ]
  }
}
```

### Get Chat History
Retrieve chat history (requires authentication).

**Endpoint:** `GET /api/chat/history`

**Headers:**
```
Authorization: Bearer <token>
```

### Clear Chat History
Clear all chat history (requires authentication).

**Endpoint:** `DELETE /api/chat/clear`

---

## 🔐 Authentication API

### Sign Up
Create a new user account.

**Endpoint:** `POST /api/auth/signup`

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password123",
  "name": "John Doe"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Account created successfully",
  "data": {
    "token": "abc123...",
    "user": {
      "id": "user_123",
      "email": "user@example.com",
      "name": "John Doe"
    }
  }
}
```

### Login
Authenticate an existing user.

**Endpoint:** `POST /api/auth/login`

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Login successful",
  "data": {
    "token": "abc123...",
    "user": {
      "id": "user_123",
      "email": "user@example.com",
      "name": "John Doe"
    }
  }
}
```

### Logout
End user session.

**Endpoint:** `POST /api/auth/logout`

**Headers:**
```
Authorization: Bearer <token>
```

### Verify Token
Verify if authentication token is valid.

**Endpoint:** `GET /api/auth/verify`

**Headers:**
```
Authorization: Bearer <token>
```

### Get Profile
Retrieve user profile information.

**Endpoint:** `GET /api/auth/profile`

**Headers:**
```
Authorization: Bearer <token>
```

### Update Profile
Update user profile information.

**Endpoint:** `PUT /api/auth/profile`

**Headers:**
```
Authorization: Bearer <token>
```

**Request Body:**
```json
{
  "name": "New Name",
  "email": "newemail@example.com"
}
```

---

## 🏥 Utility Endpoints

### Health Check
Check if the API is running.

**Endpoint:** `GET /health`

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00",
  "version": "1.0.0"
}
```

### API Info
Get API information and available endpoints.

**Endpoint:** `GET /`

**Response:**
```json
{
  "name": "BrandArc API",
  "version": "1.0.0",
  "status": "running",
  "endpoints": {
    "brand": "/api/brand",
    "logo": "/api/logo",
    ...
  }
}
```

---

## Error Responses

All errors follow this format:

```json
{
  "success": false,
  "error": "Error message here"
}
```

### HTTP Status Codes
- `200` - Success
- `201` - Created
- `400` - Bad Request
- `401` - Unauthorized
- `403` - Forbidden
- `404` - Not Found
- `405` - Method Not Allowed
- `500` - Internal Server Error

---

## Rate Limiting
- Default: 100 requests per hour
- Authenticated users: Higher limits

---

## CORS
The API supports Cross-Origin Resource Sharing (CORS) for the following origins:
- `http://localhost:3000`
- `http://localhost:8080`
- `http://127.0.0.1:5500`

Configure additional origins in `config.py`.

---

## Examples

### Using cURL

**Generate Brand Names:**
```bash
curl -X POST http://localhost:5000/api/brand/generate \
  -H "Content-Type: application/json" \
  -d '{"industry":"Technology","keywords":"AI,Smart","tone":"Modern","count":5}'
```

**Login:**
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password123"}'
```

**Get Profile (with auth):**
```bash
curl -X GET http://localhost:5000/api/auth/profile \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

### Using JavaScript Fetch

```javascript
// Generate brand names
const response = await fetch('http://localhost:5000/api/brand/generate', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    industry: 'Technology',
    keywords: 'AI, Smart',
    tone: 'Modern',
    count: 10
  })
});

const data = await response.json();
console.log(data);
```

### Using the API Client

```javascript
const api = new BrandArcAPI('http://localhost:5000');

// Generate brands
const brands = await api.generateBrandNames({
  industry: 'Technology',
  keywords: 'AI, Smart',
  tone: 'Modern'
});

// Login
const result = await api.login('user@example.com', 'password123');

// Send chat
const chat = await api.sendChatMessage('Help with brand naming');
```

---

## Support
For issues or questions, check the logs or contact support.
