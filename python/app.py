import gradio as gr
import threading
from time import sleep
from basic_tool import *
from arm_servo import Gripper
from client import communicate, Capture

videocap = Capture()
gripper = Gripper()
video_thread = threading.Thread(target=videocap.show)
video_thread.start()

def locate_the_object(object_name):
    '''
    turn the robot to forward the object
    '''
    rotate()
    for _ in range(400):
        # get the image
        sleep(0.1)
        if videocap.checkDir(object_name):
            stop()
            return True
    stop()
    print('timeout')
    return False
    
def move_to_location(object_name):
    '''
    move the robot to the location of the object
    '''
    foward()
    for _ in range(100):
        # get the image
        sleep(0.1)
        if videocap.checkDis(object_name):
            stop()
            return True
    stop()
    print('timeout')
    return False
    # need to rotate to point to the object

def pick_up_object():
    gripper.grab()

def place_object():
    gripper.release()

def control_robot(todo):
    '''
    todo is a json object with the following keys:
    '''
    # todo = {'obj': '', 'area': ''}
    if not todo['obj']:
        stop()
        return
    if not locate_the_object(todo['obj']):
        stop()
        return
    print("obj detected")
    move_to_location(todo['obj'])
    pick_up_object()
    print('pick success')
    backward()
    time.sleep(1.5)
    if not locate_the_object(todo['area']):
        stop()
        return
    print('locate destination')
    move_to_location(todo['area'])
    place_object()
    # prevent the robot from hit the placed object
    backward()
    time.sleep(5)
    stop()

def echo(message, history):
    response = communicate(message)
    # Start a new thread to control the robot without blocking
    robot_thread = threading.Thread(target=control_robot, args=(response['function'],))
    robot_thread.start()
    return response['response']


demo = gr.ChatInterface(fn=echo, examples=["move the red cube to the upper right", "move the blue cube to the upper left", "hi"], title="TidyBot")
demo.launch()
