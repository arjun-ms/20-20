![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)

# 20-20
![20-20](http://en.malayalamemagazine.com/wp-content/uploads/2016/10/mohanlal-mammootty-box-office-800x510.jpg?x66743)
A Image classifier that classifies actors mammooty and mohanlal. This model takes in images of mammooty or mohanlal and classifies them. It was built by training the model with large amount of cleaned data , which helps to identify between mammooty and mohanlal. The data was scrapped from Google and cleaned using opencv face detection algorithm and was manually checked after that. We used suitable algorithm to produce better results out of the model. The final product can now classify the images , but not with very high accuracy. It has good accuracy and we spend a lot of time to make it to this point where it can perform like this.
Unfortunately we couldn't host it because there isn't any free services that could host our model because of its large size.
Now we can test images by using the script we wrote , we can change image path and test any desired image.

Input taken : Image <br /> 
Output : Prediction as String <br /> 
You can download the [dataset](https://www.kaggle.com/arjunachu/mamooty-mohanlal) from here.
## Team members
1. [Arjun M S](https://github.com/arjun-ms)
2. [Muhammed Ajmal M](https://github.com/ajmalmohad)
3. [Danwand](https://github.com/DanBrown47)
## Team Id
BFH/recxiM4z57LubiX39/2021

## Link to product walkthrough
[link to video]

## How it Works ?
1. Step 1
2. Step 2

## Libraries used
Open CV - Version <br /> 
Tensorflow <br /> 
Keras <br /> 
Matplotlib <br /> 
Numpy <br /> 

## How to configure
**1.** Installing pip [Python Package Manager]

```shell
$ sudo apt-get install python3-pip
```

**2.** Clone this repository to your local drive

```shell
$ git clone https://github.com/arjun-ms/20-20
```

**3.** Install dependencies

```shell
$ pip3 install -r requirements.txt
```

**4.** Run the server

```shell
$ cd Server/

$ python3 app.py
```

**5.** Head to Browser

> http://localhost:YOUR_PORT_HERE/

## How to Run
Instructions for running

