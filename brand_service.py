"""
Brand Generation Service
Contains business logic for brand name generation
"""
import random
from datetime import datetime

class BrandService:
    def __init__(self):
        self.prefixes = {
            'Modern': ['Apex', 'Nexus', 'Pulse', 'Vortex', 'Zenith', 'Prism', 'Vertex', 'Echo', 'Nova', 'Flux'],
            'Playful': ['Zap', 'Buzz', 'Pop', 'Fizz', 'Spark', 'Bounce', 'Glow', 'Dash', 'Zoom', 'Snap'],
            'Professional': ['Prime', 'Elite', 'Core', 'Sage', 'Crown', 'Atlas', 'Summit', 'Noble', 'Titan', 'Sterling'],
            'Creative': ['Muse', 'Canvas', 'Sketch', 'Palette', 'Vision', 'Dream', 'Quest', 'Craft', 'Inspire', 'Imagine'],
            'Tech': ['Byte', 'Pixel', 'Data', 'Code', 'Cloud', 'Cyber', 'Digi', 'Tech', 'Nano', 'Quantum']
        }
        
        self.suffixes = {
            'Modern': ['ify', 'ly', 'wise', 'flow', 'hub', 'labs', 'ai', 'io', 'space', 'verse'],
            'Playful': ['pop', 'box', 'ville', 'land', 'joy', 'fun', 'pal', 'buddy', 'zone', 'spot'],
            'Professional': ['pro', 'corp', 'group', 'solutions', 'ventures', 'capital', 'partners', 'holdings', 'enterprises', 'global'],
            'Creative': ['studio', 'works', 'collective', 'house', 'space', 'loft', 'gallery', 'atelier', 'forge', 'lab'],
            'Tech': ['tech', 'soft', 'sys', 'net', 'link', 'zone', 'grid', 'base', 'ware', 'logic']
        }
        
        self.industry_words = {
            'Technology': ['tech', 'digital', 'smart', 'cloud', 'cyber', 'data', 'ai', 'quantum', 'neural', 'bit'],
            'Healthcare': ['health', 'care', 'med', 'vita', 'life', 'wellness', 'cure', 'heal', 'bio', 'pulse'],
            'Finance': ['fin', 'pay', 'wealth', 'trust', 'capital', 'invest', 'money', 'coin', 'ledger', 'vault'],
            'Education': ['edu', 'learn', 'scholar', 'academy', 'brain', 'study', 'teach', 'knowledge', 'wise', 'mind'],
            'Retail': ['shop', 'mart', 'store', 'market', 'buy', 'trade', 'commerce', 'bazaar', 'emporium', 'exchange'],
            'Food': ['food', 'taste', 'flavor', 'dish', 'kitchen', 'cook', 'fresh', 'bite', 'feast', 'savory'],
            'Fashion': ['style', 'chic', 'mode', 'vogue', 'wear', 'thread', 'fabric', 'couture', 'trend', 'glam'],
            'Travel': ['go', 'voyage', 'journey', 'trip', 'explore', 'wander', 'roam', 'nomad', 'quest', 'venture']
        }
    
    def generate_names(self, industry, keywords, tone, count):
        """Generate brand names based on parameters"""
        names = []
        keywords_list = [k.strip() for k in keywords.split(',') if k.strip()]
        
        prefixes = self.prefixes.get(tone, self.prefixes['Modern'])
        suffixes = self.suffixes.get(tone, self.suffixes['Modern'])
        industry_words = self.industry_words.get(industry, self.industry_words['Technology'])
        
        strategies = [
            self._strategy_prefix_suffix,
            self._strategy_keyword_suffix,
            self._strategy_blend,
            self._strategy_creative,
            self._strategy_compound
        ]
        
        for i in range(count):
            strategy = random.choice(strategies)
            name = strategy(prefixes, suffixes, industry_words, keywords_list)
            
            # Calculate scores
            domain_score = random.randint(65, 98)
            trademark_score = random.randint(55, 95)
            memorability_score = self._calculate_memorability(name)
            
            names.append({
                'id': f'brand_{i+1}_{int(datetime.now().timestamp() * 1000)}',
                'name': name,
                'domain': f"{name.lower()}.com",
                'domainAvailable': domain_score > 70,
                'domainScore': domain_score,
                'trademarkAvailable': trademark_score > 60,
                'trademarkScore': trademark_score,
                'memorabilityScore': memorability_score,
                'description': self._generate_description(name, industry, tone),
                'alternativeDomains': [
                    f"{name.lower()}.io",
                    f"{name.lower()}.ai",
                    f"{name.lower()}.co"
                ]
            })
        
        return names
    
    def _strategy_prefix_suffix(self, prefixes, suffixes, industry_words, keywords):
        """Combine prefix and suffix"""
        return random.choice(prefixes) + random.choice(suffixes).capitalize()
    
    def _strategy_keyword_suffix(self, prefixes, suffixes, industry_words, keywords):
        """Use keyword with suffix"""
        if keywords:
            keyword = random.choice(keywords).strip().capitalize()
            return keyword + random.choice(suffixes).capitalize()
        return self._strategy_prefix_suffix(prefixes, suffixes, industry_words, keywords)
    
    def _strategy_blend(self, prefixes, suffixes, industry_words, keywords):
        """Blend keyword with industry word"""
        if keywords:
            kw = random.choice(keywords).strip()
            return kw[:4].capitalize() + random.choice(industry_words)[:4].capitalize()
        return random.choice(prefixes) + random.choice(industry_words).capitalize()
    
    def _strategy_creative(self, prefixes, suffixes, industry_words, keywords):
        """Creative combination"""
        parts = [
            random.choice(prefixes),
            random.choice(industry_words),
            random.choice(suffixes)
        ]
        # Use 2 random parts
        selected = random.sample(parts, 2)
        return ''.join([p.capitalize() for p in selected])
    
    def _strategy_compound(self, prefixes, suffixes, industry_words, keywords):
        """Compound word strategy"""
        if keywords and len(keywords) >= 2:
            kw1 = random.choice(keywords).strip()
            kw2 = random.choice(keywords).strip()
            return kw1[:4].capitalize() + kw2[:4].capitalize()
        return random.choice(prefixes) + random.choice(industry_words).capitalize()
    
    def _calculate_memorability(self, name):
        """Calculate how memorable a name is"""
        score = 100
        
        # Penalize long names
        if len(name) > 12:
            score -= (len(name) - 12) * 5
        
        # Bonus for short names
        if len(name) <= 8:
            score += 10
        
        # Check for difficult letter combinations
        difficult_combos = ['xz', 'qx', 'zq', 'pf', 'vw']
        for combo in difficult_combos:
            if combo in name.lower():
                score -= 15
        
        # Bonus for vowel distribution
        vowels = sum(1 for c in name.lower() if c in 'aeiou')
        if 0.3 <= vowels / len(name) <= 0.5:
            score += 10
        
        return max(0, min(100, score))
    
    def _generate_description(self, name, industry, tone):
        """Generate description for the brand"""
        templates = [
            f"A {tone.lower()} {industry.lower()} brand that combines innovation with reliability.",
            f"{name} represents the future of {industry.lower()} with a {tone.lower()} approach.",
            f"Transforming {industry.lower()} through {tone.lower()} solutions and cutting-edge technology.",
            f"Experience {industry.lower()} reimagined with {name}'s {tone.lower()} vision.",
        ]
        return random.choice(templates)
    
    def check_availability(self, name):
        """Check domain and trademark availability"""
        # Mock implementation - in production, use real APIs
        domain_available = random.choice([True, False])
        trademark_available = random.choice([True, False])
        
        return {
            'name': name,
            'domain': {
                'available': domain_available,
                'price': random.randint(10, 50) if domain_available else None,
                'alternatives': [
                    f"{name.lower()}.io",
                    f"{name.lower()}.ai",
                    f"{name.lower()}.co",
                    f"get{name.lower()}.com"
                ]
            },
            'trademark': {
                'available': trademark_available,
                'conflicts': [] if trademark_available else ['Similar trademark found in class 42']
            },
            'social': {
                'twitter': random.choice([True, False]),
                'instagram': random.choice([True, False]),
                'facebook': random.choice([True, False])
            }
        }
    
    def get_quick_suggestions(self, industry, tone):
        """Get quick brand suggestions without keywords"""
        keywords = ', '.join(random.sample(self.industry_words.get(industry, []), 3))
        return self.generate_names(industry, keywords, tone, 5)
