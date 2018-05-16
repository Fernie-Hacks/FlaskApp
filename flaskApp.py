#!/usr/bin/python

from flask import Flask
app = Flask(__name__)

# Routes for all Web Pages
# Default landings page show all restaurants
@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    return "This page will show all my restaurants"

# Page to show all a restaurant and its menu
@app.route('/restaurant/<int:restaurant_id>/menu')
@app.route('/restaurant/<int:restaurant_id>')
def showMenu(restaurant_id):
    return "This page is the menu for restaurant %s" % restaurant_id

# Page to create a new restaurant
@app.route('/restaurant/new')
def newRestaurant():
    return "This page will make a new restaurant"

# Page to edit a restaurant
@app.route('/restaurant/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    return "This page will be for editing restaurant %s" % restaurant_id

# Page to delete a restaurant
@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    return "This page will be for deleting restaurant %s" % restaurant_id

# Page to create a new menu entry
@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
    return "This page will be for making a new menu item for restaurant %s" % restaurant_id

# Page to edit a menu entry
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    return "This page will be for editing menu item %s" % menu_id

# Page to delete a menu entry
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
    return "This page will be for deleting menu item %s" % menu_id

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)