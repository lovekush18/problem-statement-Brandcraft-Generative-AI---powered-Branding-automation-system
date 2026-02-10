"""
Brand Generation API Routes
"""
from flask import Blueprint, request, jsonify
from services.brand_service import BrandService

brand_bp = Blueprint('brand', __name__)
brand_service = BrandService()

@brand_bp.route('/generate', methods=['POST'])
def generate_brand_names():
    """
    Generate brand name suggestions
    
    Request JSON:
    {
        "industry": "Technology",
        "keywords": "AI, Smart, Future",
        "tone": "Modern",
        "count": 10
    }
    
    Response:
    {
        "success": true,
        "data": {
            "names": [...],
            "count": 10,
            "industry": "Technology",
            "tone": "Modern"
        }
    }
    """
    try:
        data = request.get_json()
        
        # Validate input
        if not data:
            return jsonify({
                'success': False,
                'error': 'No data provided'
            }), 400
        
        industry = data.get('industry', 'Technology')
        keywords = data.get('keywords', '')
        tone = data.get('tone', 'Modern')
        count = min(int(data.get('count', 10)), 50)  # Max 50
        
        # Generate names
        names = brand_service.generate_names(
            industry=industry,
            keywords=keywords,
            tone=tone,
            count=count
        )
        
        return jsonify({
            'success': True,
            'data': {
                'names': names,
                'count': len(names),
                'industry': industry,
                'tone': tone
            }
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@brand_bp.route('/check-availability', methods=['POST'])
def check_availability():
    """
    Check domain and trademark availability for a brand name
    
    Request JSON:
    {
        "name": "BrandArc"
    }
    """
    try:
        data = request.get_json()
        name = data.get('name', '')
        
        if not name:
            return jsonify({
                'success': False,
                'error': 'Brand name is required'
            }), 400
        
        availability = brand_service.check_availability(name)
        
        return jsonify({
            'success': True,
            'data': availability
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@brand_bp.route('/suggestions', methods=['GET'])
def get_suggestions():
    """
    Get quick brand name suggestions based on query parameters
    """
    try:
        industry = request.args.get('industry', 'Technology')
        tone = request.args.get('tone', 'Modern')
        
        suggestions = brand_service.get_quick_suggestions(industry, tone)
        
        return jsonify({
            'success': True,
            'data': {
                'suggestions': suggestions
            }
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
