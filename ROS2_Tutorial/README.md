# Getting Started with ROS2 (Foxy)

Actual tutorial and documentation for ROS2 can be found over here: 

https://docs.ros.org/en/foxy/Tutorials.html


This is more of a cheatsheet text file. <br>
[ I use Ubuntu 20.04, and it works good in this distro. I have also used WSL2, but Ubuntu in better ofcourse for ROS2]

<br>

## Installing ROS2 
A beautiful installation guide is provided in this link: <br>
https://docs.ros.org/en/foxy/Installation.html

If you want to get started with ROS2 directly without much effort (in ubuntu 20.04), 
just follow the exact steps provided over here :

https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html

<br>

## Creating workspace
Before getting started with any ROS work, you need to source setup file everytime you open a new terminal. <br>
`source /opt/ros/foxy/setup.bash`

So, I prefer writing this line inside bashrc or zshrc(incase you are using zsh) like this : <br>
`echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc` <br>
OR  <br>
`echo "source /opt/ros/foxy/setup.bash" >> ~/.zshrc`

This ensures setup file is sourced everytime a new terminal is opened.

Now create a workspace directory (anywhere in your system). In my case, I have named it as ROS2_ws. Inside ROS2_ws create another directory named src. We will be using python for this tutorial, so we are not going to touch CPP much.
Inside this src folder, we will keep all our ROS2 packages.

## Creating a package

Let's go to src directory <br>`cd ~/ROS2_ws/src`<br> and then type the following in terminal <br>
`ros2 pkg create --build-type ament_python <package_name>` <br>

In my case, I typed `ros2 pkg create --build-type ament_python ROS2_Tutorial`

Now we can see a directory created named ROS2_Tutorial.
Inside the directory we see another ROS2_Turorial directory, normally where we keep all our codes. Yipiee, we have created our first package.

Next, we have to build our package. Go to `ROS2_ws` directory and type in <br>
`colcon build`.
<br>
It builds all the packages inside src folder.

## Alert

Evertime you do something, look out for setup.py and package.xml
It is important to make changes out there if you are adding some dependecies or anything. 


## Msg and Srv

*THIS IS ACTUALLY IMPORTANT**. msg and srv files can't be made in a pure python package (at least as of now). So instead we create a new package of cpp just like we created for this python package. Just type in the terminal, 
`ros2 pkg create --build-type ament_cmake interfaces`
<br>

Go inside interfaces folder, and then make two directories named srv and src. After that put your data in it. Make necessary changes in your CMAKELists.txt and package.xml and you will be done!! 
In case you are finding it difficult, well you know the drill. <br>  
https://docs.ros.org/en/foxy/Tutorials/Custom-ROS2-Interfaces.html

Now you can already use all the files directly in your local computer because I have used interfaces(name of the package containing srv and msg) in some of my python files.


## Subscriber and Publisher.

Before proceeding furthur, I will assume that you have a general idea about Nodes, Subscriber, Publisher and Topics too. If not, there are numerous tutorials on youtube that you can go through. It will hardly take around 15 minutes to grasp everything out there. You can check out the codes in this repo for a simple publisher and subscriber code.
Since our example code requires std_msgs, we need to add that as a dependency in package.xml <br>
`<exec_depend>std_msgs</exec_depend>` <br>
Add this line in package.xml

Now everything is fine, but how would ROS2 know which one is a publisher node and which one is a subscriber node? We need an entry point for our package. So, in setup.py, we add the following
```       
 'console_scripts': [
            'talker = ROS2_Tutorial.publisher_member_function',
            'listener = ROS2_Tutorial.subscriber_member_function',
            .
            .
            .
 ]
```

Now we follow the same drill to build our package and run it.
Go to `ROS2_ws` directory and type in <br>
`colcon build --packages-select ROS2_Tutorial`
<br> ( I have only one package to build, so I target only this package , otherwise `colcon build` would have built all packages inside src folder)
Next we source the setup files (just in case)
`source install/setup.bash` or setup.zsh if you are using zsh

Now to run those nodes, let's open up two terminals. 
In one of them, let's run `ros2 run ROS2_Tutorial talker` and in another terminal let's run `ros2 run ROS2_Tutorial listener`

Look at the output and enjoy !

## Clients and Services

Well, I am not gonna explain everything coz this is not a tutorial, rather a cheatsheet. I will assume that you know what are clients and services. If not, youtube is the way to go.
Anyway, the client and services code are already there, check them out yo !!. I'll continue writing this "priceless" cheatsheet tomorrow :) I am too lazy for this LOL. You can contribute to this though :)

## Parameters

Parameters are cool. They help in changing some parameters in run-time. You can ofc explore parameters.py if you are stuck. Anyway, the key point over here is that, we can also pass in arrays as parameters and change arrays of parameters. I am too lazy to type everything out rn, so, why not check the file out yourself? It's almost self_explanatory. If you are stuck still, feel free to visit the documentation of ROS2 Parameters.

## Action Servers and Clients

I hope you know what are Actions. So, let's get into it pretty fast. Look at the file action_server.py which takes in a number and computes the fibonacci series.
We don't need to write a client program to run this because ROS is cool. Instead, we just type in the terminal `ros2 action send_goal --feedback fibonacci interfaces/action/Fibonacci "{order: 10}"`

Did I just forget to mention that you have to run this file in the terminal? oh! Sorry, run it in the terminal first. LOL!!

<br>

This computes fibonacci series upto 10 places. Well, for this to work, we have to ofcourse define an action file. Let's head over to interfaces and create action directory and then an action file. Now it is going to work like a charm. For dramatic effect, uncomment `time.sleep()` in action_server.py

Well, we need to write a client program to control this too(just because we want to). Pretty self_explanatory again, go through action_client.py.

Run this file in the terminal (need not `ros2 run`) and then run action_server.py and then look at the magic. COOL STUFF !!