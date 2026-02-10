"""
BrandArc Backend - Modular Flask Application
Main application file with blueprint registration
"""
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from config import get_config
import os

# Import blueprints
from api.brand import brand_bp
from api.logo import logo_bp
from api.auth import auth_bp
from api.chat import chat_bp

def create_app(config_name=None):
    """Application factory"""
    app = Flask(__name__)
    
    # Load configuration
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    config_class = get_config()
    app.config.from_object(config_class)
    
    # Enable CORS
    CORS(app, origins=config_class.CORS_ORIGINS)
    
    # Register blueprints
    app.register_blueprint(brand_bp, url_prefix='/api/brand')
    app.register_blueprint(logo_bp, url_prefix='/api/logo')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(chat_bp, url_prefix='/api/chat')
    
    # Additional API routes
    @app.route('/api/palette/generate', methods=['POST'])
    def generate_palette():
        """Generate color palettes"""
        from flask import request
        import random
        
        data = request.get_json()
        base_color = data.get('baseColor', '#6366f1')
        scheme = data.get('scheme', 'complementary')
        
        palettes = []
        for i in range(5):
            colors = [base_color]
            for _ in range(4):
                colors.append(f'#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}')
            
            palettes.append({
                'id': f'palette_{i+1}',
                'name': f'{scheme.capitalize()} Palette {i+1}',
                'colors': colors,
                'scheme': scheme
            })
        
        return jsonify({
            'success': True,
            'data': {
                'palettes': palettes
            }
        }), 200
    
    @app.route('/api/content/generate', methods=['POST'])
    def generate_content():
        """Generate marketing content"""
        from flask import request
        import random
        
        data = request.get_json()
        content_type = data.get('type', 'tagline')
        brand_name = data.get('brandName', 'BrandArc')
        industry = data.get('industry', 'Technology')
        tone = data.get('tone', 'Professional')
        
        templates = {
            'tagline': [
                f"{brand_name} - Where Innovation Meets Excellence",
                f"Transform Your {industry} Experience with {brand_name}",
                f"{brand_name}: Empowering {industry} for Tomorrow",
                f"The Future of {industry} Starts Here",
            ],
            'description': [
                f"{brand_name} is a leading {industry} platform that helps businesses grow and succeed through innovative solutions.",
                f"Discover how {brand_name} is revolutionizing the {industry} industry with cutting-edge technology and expert insights.",
                f"Join thousands of satisfied customers who trust {brand_name} for their {industry} needs.",
            ],
            'social': [
                f"🚀 Excited to announce our latest update! #Innovation #{industry}",
                f"💡 Did you know? {brand_name} helps you achieve more in less time.",
                f"🌟 Join us on this incredible journey. Let's transform {industry} together!",
            ]
        }
        
        content_list = templates.get(content_type, templates['tagline'])
        results = []
        
        for text in content_list:
            results.append({
                'text': text,
                'type': content_type,
                'tone': tone,
                'length': len(text)
            })
        
        return jsonify({
            'success': True,
            'data': {
                'content': results
            }
        }), 200
    
    @app.route('/api/design-system/generate', methods=['POST'])
    def generate_design_system():
        """Generate complete design system"""
        from flask import request
        
        data = request.get_json()
        brand_name = data.get('brandName', 'BrandArc')
        
        design_system = {
            'colors': {
                'primary': '#6366f1',
                'secondary': '#8b5cf6',
                'accent': '#ec4899',
                'success': '#10b981',
                'warning': '#f59e0b',
                'error': '#ef4444',
                'background': '#ffffff',
                'surface': '#f8fafc',
                'text': '#1e293b',
                'textSecondary': '#64748b'
            },
            'typography': {
                'fontFamily': "'Inter', sans-serif",
                'headingFont': "'Poppins', sans-serif",
                'fontSize': {
                    'xs': '12px',
                    'sm': '14px',
                    'base': '16px',
                    'lg': '18px',
                    'xl': '20px',
                    '2xl': '24px',
                    '3xl': '30px',
                    '4xl': '36px'
                },
                'fontWeight': {
                    'normal': 400,
                    'medium': 500,
                    'semibold': 600,
                    'bold': 700
                }
            },
            'spacing': {
                'xs': '4px',
                'sm': '8px',
                'md': '16px',
                'lg': '24px',
                'xl': '32px',
                '2xl': '48px'
            },
            'borderRadius': {
                'sm': '4px',
                'md': '8px',
                'lg': '12px',
                'xl': '16px',
                'full': '9999px'
            },
            'shadows': {
                'sm': '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
                'md': '0 4px 6px -1px rgba(0, 0, 0, 0.1)',
                'lg': '0 10px 15px -3px rgba(0, 0, 0, 0.1)',
                'xl': '0 20px 25px -5px rgba(0, 0, 0, 0.1)'
            }
        }
        
        return jsonify({
            'success': True,
            'data': {
                'designSystem': design_system
            }
        }), 200
    
    # Root and utility routes
    @app.route('/')
    def index():
        """API information"""
        return jsonify({
            'name': 'BrandArc API',
            'version': '1.0.0',
            'status': 'running',
            'endpoints': {
                'brand': '/api/brand',
                'logo': '/api/logo',
                'auth': '/api/auth',
                'chat': '/api/chat',
                'palette': '/api/palette',
                'content': '/api/content',
                'designSystem': '/api/design-system'
            }
        })
    
    @app.route('/health')
    def health():
        """Health check endpoint"""
        return jsonify({
            'status': 'healthy',
            'timestamp': __import__('datetime').datetime.now().isoformat(),
            'version': '1.0.0'
        })
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({
            'success': False,
            'error': 'Endpoint not found',
            'message': 'The requested resource does not exist'
        }), 404
    
    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({
            'success': False,
            'error': 'Internal server error',
            'message': 'Something went wrong on our end'
        }), 500
    
    @app.errorhandler(405)
    def method_not_allowed(e):
        return jsonify({
            'success': False,
            'error': 'Method not allowed',
            'message': 'This HTTP method is not supported for this endpoint'
        }), 405
    
    return app

if __name__ == '__main__':
    app = create_app()
    
    print("\n" + "="*60)
    print("🚀 BrandArc Backend Server Starting...")
    print("="*60)
    print(f"📍 Server running at: http://localhost:{app.config['PORT']}")
    print(f"🌐 Environment: {os.getenv('FLASK_ENV', 'development')}")
    print(f"🔧 Debug mode: {app.config['DEBUG']}")
    print("\n📋 Available API Endpoints:")
    print("   Brand Generation:")
    print("   - POST /api/brand/generate")
    print("   - POST /api/brand/check-availability")
    print("   - GET  /api/brand/suggestions")
    print("\n   Logo Generation:")
    print("   - POST /api/logo/generate")
    print("   - POST /api/logo/customize")
    print("   - POST /api/logo/export/<format>")
    print("\n   Authentication:")
    print("   - POST /api/auth/signup")
    print("   - POST /api/auth/login")
    print("   - POST /api/auth/logout")
    print("   - GET  /api/auth/verify")
    print("   - GET  /api/auth/profile")
    print("   - PUT  /api/auth/profile")
    print("\n   AI Chat:")
    print("   - POST /api/chat/send")
    print("   - GET  /api/chat/history")
    print("   - DEL  /api/chat/clear")
    print("\n   Other Services:")
    print("   - POST /api/palette/generate")
    print("   - POST /api/content/generate")
    print("   - POST /api/design-system/generate")
    print("\n   Utility:")
    print("   - GET  / (API info)")
    print("   - GET  /health (Health check)")
    print("\n✅ Server ready to accept requests!")
    print("="*60 + "\n")
    
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )
