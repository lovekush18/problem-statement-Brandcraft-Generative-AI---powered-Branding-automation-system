/**
 * BrandArc API Client
 * Frontend JavaScript library for connecting to the backend API
 */

class BrandArcAPI {
    constructor(baseURL = 'http://localhost:5000') {
        this.baseURL = baseURL;
        this.token = localStorage.getItem('authToken') || null;
    }

    /**
     * Make API request
     */
    async request(endpoint, options = {}) {
        const url = `${this.baseURL}${endpoint}`;
        
        const headers = {
            'Content-Type': 'application/json',
            ...options.headers
        };

        if (this.token && !options.skipAuth) {
            headers['Authorization'] = `Bearer ${this.token}`;
        }

        try {
            const response = await fetch(url, {
                ...options,
                headers
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Request failed');
            }

            return data;
        } catch (error) {
            console.error('API request failed:', error);
            throw error;
        }
    }

    // =====================
    // Brand API
    // =====================

    /**
     * Generate brand names
     */
    async generateBrandNames(params) {
        return this.request('/api/brand/generate', {
            method: 'POST',
            body: JSON.stringify({
                industry: params.industry || 'Technology',
                keywords: params.keywords || '',
                tone: params.tone || 'Modern',
                count: params.count || 10
            })
        });
    }

    /**
     * Check brand name availability
     */
    async checkAvailability(brandName) {
        return this.request('/api/brand/check-availability', {
            method: 'POST',
            body: JSON.stringify({ name: brandName })
        });
    }

    /**
     * Get brand suggestions
     */
    async getBrandSuggestions(industry, tone) {
        return this.request(`/api/brand/suggestions?industry=${industry}&tone=${tone}`, {
            method: 'GET'
        });
    }

    // =====================
    // Logo API
    // =====================

    /**
     * Generate logos
     */
    async generateLogos(params) {
        return this.request('/api/logo/generate', {
            method: 'POST',
            body: JSON.stringify({
                brandName: params.brandName || 'Brand',
                style: params.style || 'modern',
                colors: params.colors || [],
                count: params.count || 8
            })
        });
    }

    /**
     * Customize logo
     */
    async customizeLogo(logoId, colors, text) {
        return this.request('/api/logo/customize', {
            method: 'POST',
            body: JSON.stringify({ logoId, colors, text })
        });
    }

    /**
     * Export logo
     */
    async exportLogo(svg, format) {
        return this.request(`/api/logo/export/${format}`, {
            method: 'POST',
            body: JSON.stringify({ svg })
        });
    }

    // =====================
    // Color Palette API
    // =====================

    /**
     * Generate color palettes
     */
    async generatePalettes(baseColor, scheme) {
        return this.request('/api/palette/generate', {
            method: 'POST',
            body: JSON.stringify({ baseColor, scheme })
        });
    }

    // =====================
    // Content API
    // =====================

    /**
     * Generate content
     */
    async generateContent(params) {
        return this.request('/api/content/generate', {
            method: 'POST',
            body: JSON.stringify({
                type: params.type || 'tagline',
                brandName: params.brandName || 'BrandArc',
                industry: params.industry || 'Technology',
                tone: params.tone || 'Professional'
            })
        });
    }

    // =====================
    // Design System API
    // =====================

    /**
     * Generate design system
     */
    async generateDesignSystem(brandName) {
        return this.request('/api/design-system/generate', {
            method: 'POST',
            body: JSON.stringify({ brandName })
        });
    }

    // =====================
    // Chat API
    // =====================

    /**
     * Send chat message
     */
    async sendChatMessage(message, timeLimit = 'normal', context = {}) {
        return this.request('/api/chat/send', {
            method: 'POST',
            body: JSON.stringify({ message, timeLimit, context })
        });
    }

    /**
     * Get chat history
     */
    async getChatHistory() {
        return this.request('/api/chat/history', {
            method: 'GET'
        });
    }

    /**
     * Clear chat history
     */
    async clearChatHistory() {
        return this.request('/api/chat/clear', {
            method: 'DELETE'
        });
    }

    // =====================
    // Authentication API
    // =====================

    /**
     * Sign up
     */
    async signup(email, password, name) {
        const response = await this.request('/api/auth/signup', {
            method: 'POST',
            body: JSON.stringify({ email, password, name }),
            skipAuth: true
        });

        if (response.success && response.data.token) {
            this.setToken(response.data.token);
        }

        return response;
    }

    /**
     * Login
     */
    async login(email, password) {
        const response = await this.request('/api/auth/login', {
            method: 'POST',
            body: JSON.stringify({ email, password }),
            skipAuth: true
        });

        if (response.success && response.data.token) {
            this.setToken(response.data.token);
        }

        return response;
    }

    /**
     * Logout
     */
    async logout() {
        const response = await this.request('/api/auth/logout', {
            method: 'POST'
        });

        this.clearToken();
        return response;
    }

    /**
     * Verify token
     */
    async verifyToken() {
        return this.request('/api/auth/verify', {
            method: 'GET'
        });
    }

    /**
     * Get user profile
     */
    async getProfile() {
        return this.request('/api/auth/profile', {
            method: 'GET'
        });
    }

    /**
     * Update user profile
     */
    async updateProfile(data) {
        return this.request('/api/auth/profile', {
            method: 'PUT',
            body: JSON.stringify(data)
        });
    }

    // =====================
    // Utility Methods
    // =====================

    /**
     * Set authentication token
     */
    setToken(token) {
        this.token = token;
        localStorage.setItem('authToken', token);
    }

    /**
     * Clear authentication token
     */
    clearToken() {
        this.token = null;
        localStorage.removeItem('authToken');
    }

    /**
     * Check if user is authenticated
     */
    isAuthenticated() {
        return !!this.token;
    }

    /**
     * Health check
     */
    async healthCheck() {
        return this.request('/health', {
            method: 'GET',
            skipAuth: true
        });
    }
}

// Export for use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = BrandArcAPI;
}
