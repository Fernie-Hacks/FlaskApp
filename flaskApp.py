#!/usr/bin/python

from flask import Flask, render_template
app = Flask(__name__)

#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}

# Routes for all Web Pages
# Default landings page show all restaurants
@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    return render_template('restaurants.html', restaurants = restaurants)

# Page to show all a restaurant and its menu
@app.route('/restaurant/<int:restaurant_id>/menu')
@app.route('/restaurant/<int:restaurant_id>')
def showMenu(restaurant_id):
    return render_template('menu.html', restaurant = restaurants[restaurant_id - 1], items = items )

# Page to create a new restaurant
@app.route('/restaurant/new', methods=['GET', 'POST'])
def newRestaurant():
    return render_template('newRestaurant.html')

# Page to edit a restaurant
@app.route('/restaurant/<int:restaurant_id>/edit', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    return render_template('editRestaurant.html', restaurant = restaurants[restaurant_id - 1])

# Page to delete a restaurant
@app.route('/restaurant/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    return render_template('deleteRestaurant.html', restaurant = restaurants[restaurant_id - 1])

# Page to create a new menu entry
@app.route('/restaurant/<int:restaurant_id>/menu/new', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    return render_template('newMenuItem.html')

# Page to edit a menu entry
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    return render_template('editMenuItem.html', restaurant = 
                           restaurants[restaurant_id - 1], item = items[menu_id - 1])

# Page to delete a menu entry
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    return render_template('deleteMenuItem.html', restaurant = 
                           restaurants[restaurant_id - 1], item = items[menu_id - 1])

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)