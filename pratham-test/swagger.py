# 🍕 PIZZA RESTAURANT ANALOGY 🍕
# Think of this code like running a pizza restaurant:
# - Flask = The restaurant building
# - Swagger = The menu board that shows all available pizzas
# - API endpoints = Different pizza types customers can order
# - Users data = The customer database

from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields

# 🏪 CREATE THE RESTAURANT (Flask app)
# This is like opening a new restaurant building
app = Flask(__name__)

# 📋 CREATE THE MENU BOARD (Swagger documentation)
# Analogy: Like putting up a fancy digital menu board that shows:
# - What pizzas we serve
# - What ingredients each pizza has
# - How much each costs
# - How to place an order
api = Api(app, 
    title='Simple API',  # Restaurant name on the menu board
    description='Learning Swagger basics',  # Tagline under restaurant name
    doc='/docs/'  # Where customers can see the menu (http://localhost:5000/docs/)
)

# 🧾 DEFINE WHAT A "CUSTOMER PROFILE" LOOKS LIKE
# Analogy: Like creating a customer registration form that says:
# "Every customer must have: ID number, name, and email"
# This helps the restaurant (API) know what information to expect
user_model = api.model('User', {
    'id': fields.Integer(description='Customer ID number', example=1),
    'name': fields.String(description='Customer full name', example='John'),
    'email': fields.String(description='Customer email for receipts', example='john@email.com')
})

# 📚 OUR CUSTOMER DATABASE (Sample data)
# Analogy: Like a simple notebook where we write down regular customers
# In real life, this would be a proper database like MySQL
users = [
    {'id': 1, 'name': 'John', 'email': 'john@email.com'},
    {'id': 2, 'name': 'Jane', 'email': 'jane@email.com'}
]

# 🍕 PIZZA MENU SECTIONS (API Endpoints)
# Each section below is like a different part of our restaurant menu

# 📋 "ALL CUSTOMERS" SECTION
@api.route('/users')  # This is like the URL: restaurant.com/users
class UserList(Resource):
    
    # 👀 "SHOW ME ALL CUSTOMERS" (GET request)
    # Analogy: Like a waiter bringing you the customer list book
    def get(self):
        """Get all customers in our database"""
        # Return the entire customer list (like photocopying the customer book)
        return users
    
    # ➕ "ADD NEW CUSTOMER" (POST request) 
    @api.expect(user_model)  # Tell Swagger: "Expect customer info in this format"
    def post(self):
        """Register a new customer"""
        # Analogy: Customer fills out registration form, we add them to our book
        
        new_user = request.json  # Get the customer info they sent us
        new_user['id'] = len(users) + 1  # Give them the next available ID number
        users.append(new_user)  # Add them to our customer book
        
        # Return the new customer info + status 201 (means "successfully created")
        return new_user, 201

# 🎯 "SPECIFIC CUSTOMER" SECTION
@api.route('/users/<int:user_id>')  # URL like: restaurant.com/users/1
class User(Resource):
    
    # 🔍 "FIND ONE SPECIFIC CUSTOMER" (GET request)
    def get(self, user_id):
        """Find a customer by their ID number"""
        # Analogy: Customer says "Show me customer #5's info"
        # We flip through our customer book looking for ID #5
        
        for user in users:  # Look through each customer in our book
            if user['id'] == user_id:  # Found the customer they're looking for!
                return user  # Give them the customer's info
        
        # If we get here, we didn't find that customer ID
        return {'message': 'Customer not found'}, 404  # 404 = "Not found"

# 🚀 START THE RESTAURANT (Run the server)
# Analogy: Like opening the restaurant doors and turning on the "OPEN" sign
if __name__ == '__main__':
    app.run(debug=True)  # debug=True means we can see detailed error messages

# 🎉 HOW TO USE THIS:
# 1. Run this file: python swagger.py
# 2. Go to: http://localhost:5000/docs/
# 3. You'll see a beautiful menu (Swagger UI) showing:
#    - All available "orders" (API endpoints)
#    - What information each order needs
#    - Examples of how to place orders
#    - A "Try it out" button to test each order!

# 🌟 WHAT SWAGGER GIVES US:
# - Automatic documentation (no more writing docs by hand!)
# - Interactive testing (click buttons to test the API)
# - Clear contracts (everyone knows what data format to use)
# - Professional look (makes your API look serious and trustworthy)