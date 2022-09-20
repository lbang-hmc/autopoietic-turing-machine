#include "Keyboard.h"
/*
  Keyboard Message test

  For the Arduino Leonardo and Micro.

  Sends a text string when a button is pressed.

  The circuit:
  - pushbutton attached from pin 4 to +5V
  - 10 kilohm resistor attached from pin 4 to ground

  created 24 Oct 2011
  modified 27 Mar 2012
  by Tom Igoe
  modified 11 Nov 2013
  by Scott Fitzgerald

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/KeyboardMessage
*/



const int buttonPin4 = 4;          // input pin for pushbutton
const int buttonPin5 = 5;          // input pin for pushbutton
const int buttonPin6 = 6; 
const int buttonPin7 = 7; 
const int buttonPin8 = 8; 
const int buttonPin9 = 9;

int previousButtonState4 = HIGH;   // for checking the state of a pushButton
int previousButtonState5 = HIGH;   // for checking the state of a pushButton
int previousButtonState6 = HIGH;   // for checking the state of a pushButton
int previousButtonState7 = HIGH;   // for checking the state of a pushButton
int previousButtonState8 = HIGH;   // for checking the state of a pushButton
int previousButtonState9 = HIGH;   // for checking the state of a pushButton


int counter = 0;                  // button push counter

void setup() {
  // make the pushButton pin an input:
  pinMode(buttonPin4, INPUT);
  pinMode(buttonPin5, INPUT);
  pinMode(buttonPin6, INPUT);
  pinMode(buttonPin7, INPUT);
  pinMode(buttonPin8, INPUT);
  pinMode(buttonPin9, INPUT);
  // initialize control over the keyboard:
  Keyboard.begin();
}

void loop() {
  // read the pushbutton:
  int buttonState4 = digitalRead(buttonPin4);
  int buttonState5 = digitalRead(buttonPin5);
  int buttonState6 = digitalRead(buttonPin6);
  int buttonState7 = digitalRead(buttonPin7);
  int buttonState8 = digitalRead(buttonPin8);
  int buttonState9 = digitalRead(buttonPin9);
  
  // if the button state has changed,
  if ((buttonState4 != previousButtonState4 && counter < 50)
      // and it's currently pressed:
      && (buttonState4 == HIGH)) {
    // increment the button counter
    counter++;
    // type out a message
    Keyboard.print("d");
//    Keyboard.print(counter);
//    Keyboard.println(" times.");
  }
  if ((buttonState5 != previousButtonState5 && counter < 50)
      // and it's currently pressed:
      && (buttonState5 == HIGH)) {
    // increment the button counter
    counter++;
    // type out a message
    Keyboard.print("f");
//    Keyboard.print(counter);
//    Keyboard.println(" times.");
  }
  else if ((buttonState6 != previousButtonState6 && counter < 50)
      // and it's currently pressed:
      && (buttonState6 == HIGH)) {
    // increment the button counter
    counter++;
    // type out a message
    Keyboard.print("h");
//    Keyboard.print(counter);
//    Keyboard.println(" times.");
  }
  else if ((buttonState7 != previousButtonState7 && counter < 50)
      // and it's currently pressed:
      && (buttonState7 == HIGH)) {
    // increment the button counter
    counter++;
    // type out a message
    Keyboard.print("j");
//    Keyboard.print(counter);
//    Keyboard.println(" times.");
  }
  else if ((buttonState8 != previousButtonState8 && counter < 50)
      // and it's currently pressed:
      && (buttonState8 == HIGH)) {
    // increment the button counter
    counter++;
    // type out a message
    Keyboard.print("k");
//    Keyboard.print(counter);
//    Keyboard.println(" times.");
  }
  else if ((buttonState9 != previousButtonState9 && counter < 50)
      // and it's currently pressed:
      && (buttonState9 == HIGH)) {
    // increment the button counter
    counter++;
    // type out a message
    Keyboard.print("L");
//    Keyboard.print(counter);
//    Keyboard.println(" times.");
  }

  
  
  // save the current button state for comparison next time:
  previousButtonState4 = buttonState4;
  previousButtonState5 = buttonState5;
  previousButtonState6 = buttonState6;
  previousButtonState7 = buttonState7;
  previousButtonState8 = buttonState8;
  previousButtonState9 = buttonState9;


}
