///
// Copyright (C) 2022  University of Alberta
//
// This program is free software; you can redistribute it and/or
// modify it under the terms of the GNU General Public License
// as published by the Free Software Foundation; either version 2
// of the License, or (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
///
///
// @file pythoncontrol.h
// @author Charles Nokes
// @date 2022-06-22
///

int relay1Pin = 36; //assign relay1 for polarity switch control to Pin 36
int relay2Pin = 38; //assign relay2 for TX/RX switch control to Pin 38
int incomingData;

void setup() {
  // initialize serial communication
  Serial.begin(9600);
  // initialize the Relay pin as an output
  pinMode(relay1Pin, OUTPUT);
  pinMode(relay2Pin, OUTPUT);

}

void loop() {
  // see if there's incoming serial data
  if (Serial.available() > 0) {

    incomingData = Serial.read();

    if (incomingData == 'L') {
      digitalWrite(relay1Pin, HIGH); //Turn the polarity switch relay ON, activating LHCP port
    }

    if (incomingData == 'R') {
      digitalWrite(relay1Pin, LOW); //Turn the polarity switch relay OFF, activating RHCP port
    }

    if (incomingData == 'U') {
      digitalWrite(relay2Pin, HIGH); //Turn the TX/RX switch relay ON, activating Uplink
    }

    if (incomingData == 'D') {
      digitalWrite(relay2Pin, HIGH); //Turn the TX/RX switch relay OFF, activating Downlink
    }

    if (incomingData == 'Q') {
      digitalWrite(relay1Pin, LOW); //Turn the polarity switch relay OFF, activating RHCP
      digitalWrite(relay2Pin, LOW); //Turn the TX/RX switch relay OFF, activating Downlink
    }
  }

}
