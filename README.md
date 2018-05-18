# FlaskApp

## Problems to Solve
**Create Restaurant Application using Flask Web Development Framework** 

1. Create all application routes
2. Add templates and forms to all pages
3. Add CRUD functionality
4. Add API Endpoints
5. Add Style to webpages

## Environment
* Python  2.7.12
* Flask   0.12.2

## Suggested Setup

### Virtual Machine with Vagrant
***Requirements***

1. The VirtualBox VM environment
2. The Vagrant configuration program
3. Installing VirtualBox

**VirtualBox** 
VirtualBox is the software that actually runs the virtual machine. You can download it from virtualbox.org, [here](https://www.virtualbox.org/wiki/Downloads). Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

**Installing Vagrant**
Vagrant is the program that will download a Linux operating system and run it inside the virtual machine. [Install it from this site](https://www.vagrantup.com/downloads.html).

Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

Bringing up the database server
Vagrant takes a configuration file called Vagrantfile that tells it how to start your Linux VM. All vagrant files for this project can be found in the vagrant folder of this repo [vagrant](vagrant). Once you have a copy of this in your machine go to that directory, and run the command ```$ vagrant up```. Once completed you should see something like this:

*Successful vagrant up results: "Done installing your virtual machine!"*

Now you have a PostgreSQL server running in a Linux virtual machine. This setup is independent of any other database or web services you might have running on your computer, for instance for other projects you might work on. The VM is linked to the directory where you ran vagrant up.

To log into the VM, use a terminal in that same directory and run the following command ```$ vagrant ssh```. You'll then see something like this:

*A shell prompt on the Vagrant-managed Linux VM.*

In this shell, if you change directory to /vagrant and run *ls* there, you will see the Vagrantfile you downloaded ... and any other files you put into that directory from your computer, that will be the shared folder between VM and your computer.

### Logged in!
If you are now looking at a shell prompt that starts with the word vagrant ex ```vagrant@vagrant:/vagrant$```, congratulations — you've gotten logged into your Linux VM.

## How to execute
1. Populate DB
```cmd
$ python lotsofmenus.py 
```
2. Load the data onto the database
```sql
python flaskApp.py
```
