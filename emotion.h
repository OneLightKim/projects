// Luquid Crystal Display Custom Character Code for Arduino 16X2 Character LCD

// Dust, Temprature, Humidity Icon, Temprature measurement
byte temp[] = {
  B00100,
  B01010,
  B01010,
  B01110,
  B01110,
  B11111,
  B11111,
  B01110
};

byte humi[] = {
  B00100,
  B00100,
  B01010,
  B01010,
  B10001,
  B11111,
  B11111,
  B01110
};

byte dust[] = {
  B01010,
  B10101,
  B00000,
  B01010,
  B10101,
  B00000,
  B01010,
  B10101
};

byte C[] = {
  B10000,
  B00110,
  B01001,
  B01000,
  B01000,
  B01001,
  B00110,
  B00000
};


// Smile Emoticon Top
byte topSmile1[] = {
  B00000,
  B00111,
  B01000,
  B10000,
  B10000,
  B10010,
  B10010,
  B10000
};


byte topSmile2[] = {
  B00000,
  B11100,
  B00010,
  B00001,
  B00001,
  B01001,
  B01001,
  B00001
};

// SoSo Emoticon Top
byte topSoSo1[] = {
  B00000,
  B00111,
  B01000,
  B10000,
  B10000,
  B10010,
  B10000,
  B10000
};


byte topSoSo2[] = {
  B00000,
  B11100,
  B00010,
  B00001,
  B00001,
  B01001,
  B00001,
  B00001
};

// Angry Emoticon Top
byte topAngry1[] = {
  B00000,
  B00111,
  B01000,
  B10000,
  B10100,
  B10010,
  B10000,
  B10000
};


byte topAngry2[] = {
  B00000,
  B11100,
  B00010,
  B00001,
  B00101,
  B01001,
  B00001,
  B00001
};

// Smile Emoticon Bottom
byte bottomSmile1[] = {
  B10000,
  B10000,
  B10100,
  B10011,
  B01000,
  B00111,
  B00000,
  B00000
};

byte bottomSmile2[] = {
  B00001,
  B00001,
  B00101,
  B11001,
  B00010,
  B11100,
  B00000,
  B00000
};

// SoSo Emoticon Bottom
byte bottomSoSo1[] = {
  B10000,
  B10000,
  B10011,
  B10000,
  B01000,
  B00111,
  B00000,
  B00000
};

byte bottomSoSo2[] = {
  B00001,
  B00001,
  B11001,
  B00001,
  B00010,
  B11100,
  B00000,
  B00000
};

// Angry Emoticon Bottom
byte bottomAngry1[] = {
  B10000,
  B10000,
  B10001,
  B10010,
  B01000,
  B00111,
  B00000,
  B00000
};

byte bottomAngry2[] = {
  B00001,
  B00001,
  B10001,
  B01001,
  B00010,
  B11100,
  B00000,
  B00000
};
