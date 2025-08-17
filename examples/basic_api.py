#!/usr/bin/env python3
"""
Basic Flask API Example for Auto-DocGen

This is a simple Flask application that demonstrates various endpoint types
that can be documented using Auto-DocGen.
"""

from flask import Flask, request, jsonify
import uuid
from datetime import datetime

app = Flask(__name__)

# Sample data store
users = []
posts = []

@app.route('/', methods=['GET'])
def home():
    """Home endpoint with API information"""
    return jsonify({
        'message': 'Welcome to the Basic API Example',
        'version': '1.0.0',
        'endpoints': [
            '/users',
            '/posts',
            '/health'
        ]
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'service': 'basic-api'
    })

@app.route('/users', methods=['GET'])
def get_users():
    """Get all users"""
    return jsonify({
        'users': users,
        'total': len(users)
    })

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user"""
    data = request.get_json()
    
    if not data or 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
    
    user = {
        'id': str(uuid.uuid4()),
        'name': data['name'],
        'email': data.get('email'),
        'created_at': datetime.utcnow().isoformat()
    }
    
    users.append(user)
    return jsonify(user), 201

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """Get a specific user by ID"""
    user = next((u for u in users if u['id'] == user_id), None)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify(user)

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """Update a user"""
    user = next((u for u in users if u['id'] == user_id), None)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    user.update(data)
    user['updated_at'] = datetime.utcnow().isoformat()
    
    return jsonify(user)

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user"""
    global users
    user = next((u for u in users if u['id'] == user_id), None)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    users = [u for u in users if u['id'] != user_id]
    return jsonify({'message': 'User deleted successfully'})

@app.route('/posts', methods=['GET'])
def get_posts():
    """Get all posts with optional filtering"""
    author = request.args.get('author')
    limit = request.args.get('limit', type=int)
    
    filtered_posts = posts
    
    if author:
        filtered_posts = [p for p in posts if author.lower() in p.get('author', '').lower()]
    
    if limit:
        filtered_posts = filtered_posts[:limit]
    
    return jsonify({
        'posts': filtered_posts,
        'total': len(filtered_posts),
        'filters': {
            'author': author,
            'limit': limit
        }
    })

@app.route('/posts', methods=['POST'])
def create_post():
    """Create a new post"""
    data = request.get_json()
    
    required_fields = ['title', 'content', 'author']
    if not data or not all(field in data for field in required_fields):
        return jsonify({
            'error': 'Missing required fields',
            'required': required_fields
        }), 400
    
    post = {
        'id': str(uuid.uuid4()),
        'title': data['title'],
        'content': data['content'],
        'author': data['author'],
        'tags': data.get('tags', []),
        'created_at': datetime.utcnow().isoformat(),
        'published': data.get('published', False)
    }
    
    posts.append(post)
    return jsonify(post), 201

@app.route('/posts/<post_id>', methods=['GET'])
def get_post(post_id):
    """Get a specific post by ID"""
    post = next((p for p in posts if p['id'] == post_id), None)
    
    if not post:
        return jsonify({'error': 'Post not found'}), 404
    
    return jsonify(post)

if __name__ == '__main__':
    # Add some sample data
    sample_user = {
        'id': str(uuid.uuid4()),
        'name': 'John Doe',
        'email': 'john@example.com',
        'created_at': datetime.utcnow().isoformat()
    }
    users.append(sample_user)
    
    sample_post = {
        'id': str(uuid.uuid4()),
        'title': 'Welcome to Auto-DocGen',
        'content': 'This is a sample post created for demonstration purposes.',
        'author': 'John Doe',
        'tags': ['demo', 'api', 'documentation'],
        'created_at': datetime.utcnow().isoformat(),
        'published': True
    }
    posts.append(sample_post)
    
    print("🚀 Starting Basic API Example...")
    print("📋 Sample data loaded:")
    print(f"   • {len(users)} users")
    print(f"   • {len(posts)} posts")
    print("🌐 Available at: http://localhost:5000")
    print("📖 Generate docs with: python generate_docs_pydantic_ai.py")
    
    app.run(debug=True, port=5000)
