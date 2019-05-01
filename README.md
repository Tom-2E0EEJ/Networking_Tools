# Networking Tools

This project is a series of python scripts for testing networks and for gathering infomation about networks.
All the python scripts are based to work on a Linux system and will also likely run on MacOS. Very few of 
this scripts will work on a windows machine.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install to get the software working on your system.
Some of these scripts will need third party modules form pip3.

First off we need to install python and git if it is not alreaqdy installed:
```
sudo apt-get install python3 git
```

Next we need to install pip3:
```
sudo apt-get install python3-pip
```

Next we need to install the module from pip3:
```
sudo pip3 install sockets
```

That should be all the setup done and finished.

### Installing

Now we are going to go through a step by step guide on how to install the applications.

First we will download the scripts. (This saves the repository to your current directory.)

```
git clone https://github.com/Tom-2E0EEJ/Networking_Tools
```

Now we must navigate to the file the scripts are in.

```
cd Networking_Tools/Applications
```

To list all the current applications tyoe: (This display all scripts.)
``` 
ls
```



## Running the applications

Running the application is simple and straight forward.
This is as simple as running any other python3 application for the command line.

an example of launching the pinger application is shown below.
```
sudo python3 Pinger.py
```


## Deployment

They way to develop the application is to copy the applications or choosen
application to the location fo use and run the application as instructed above.
No further steps need to be taken to deploy these tools to your system.



## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Thomas Scott** - *Initial work* - [Tom-2E0EEJ](https://github.com/Tom-2E0EEJ)



## License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who contributes any code for this project.
