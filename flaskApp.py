#!/usr/bin/python

from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Routes for all Web Pages
# Default landings page show all restaurants
@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants = restaurants)

# Page to show all a restaurant and its menu
@app.route('/restaurant/<int:restaurant_id>/menu')
@app.route('/restaurant/<int:restaurant_id>')
def showMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).all()
    return render_template('menu.html', restaurant=restaurant, items = items)

# Page to create a new restaurant
@app.route('/restaurant/new', methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST':
        if request.form['name']:
            newRestaurantEntry = Restaurant(name = request.form['name'])
            session.add(newRestaurantEntry)
            session.commit()
            return redirect(url_for('showRestaurants'))
        return redirect(url_for('newRestaurant.html'))
    else:
        return render_template('newRestaurant.html') 

# Page to edit a restaurant
@app.route('/restaurant/<int:restaurant_id>/edit', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    modifiedRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            modifiedRestaurant.name = request.form['name']
        session.add(modifiedRestaurant)
        session.commit()
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('editRestaurant.html', restaurant = modifiedRestaurant)

# Page to delete a restaurant
@app.route('/restaurant/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    restaurantToDelete = session.query(Restaurant).filter_by(id = restaurant_id).one()
    if request.method == 'POST':
        session.delete(restaurantToDelete)
        session.commit()
        return redirect(url_for('showRestaurants')) 
    else:
        return render_template('deleteRestaurant.html', restaurant = restaurantToDelete)

# Page to create a new menu entry
@app.route('/restaurant/<int:restaurant_id>/menu/new', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        if request.form['name']:
            itemName = request.form['name']
            if request.form['price']:
                itemPrice = "$" + request.form['price']
            itemPrice = "$0.00"
            if request.form['description']:
                itemDescription = request.form['description']
            itemDescription = "Not Available"
            newItem = MenuItem(name = itemName, price = itemPrice, description = 
                               itemDescription, restaurant_id = restaurant_id)
            session.add(newItem)
            session.commit()
            return redirect(url_for('showMenu', restaurant_id = restaurant_id))
        return redirect(url_for('newMenuItem', restaurant_id = restaurant_id))
    else:
        return render_template('newMenuItem.html', restaurant_id = restaurant_id)

# Page to edit a menu entry
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    itemToEdit = session.query(MenuItem).filter_by(id=menu_id).one()
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            itemToEdit.name = request.form['name']
        if request.form['price']:
            itemToEdit.price = "$" + request.form['price']
        if request.form['description']:
            itemToEdit.description = request.form['description']
        session.add(itemToEdit)
        session.commit()
        return redirect(url_for('editMenuItem', restaurant_id = 
                                restaurant_id, menu_id = menu_id))
    else:        
        return render_template('editMenuItem.html', restaurant = 
                               restaurant, item = itemToEdit)

# Page to delete a menu entry
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    itemToRemove = session.query(MenuItem).filter_by(id=menu_id).one()
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        session.delete(itemToRemove)
        session.commit()
        return redirect(url_for('showMenu')) 
    else:        
        return render_template('deleteMenuItem.html', restaurant = 
                               restaurant, item = itemToRemove)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)