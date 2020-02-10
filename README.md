# Morse code encoder/decoder

Morse code encoder & decoder.  

## Demo

You can encode message to morse code as follow.

```
$ cd morse-code
$ python morse.py
input mode (d: decode, e: encode) > e
input your message > hello, world!
.... . .-.. .-.. --- --..-- 
.-- --- .-. .-.. -.. -.-.--
input your message > Next Message
-. . -..- - 
-- . ... ... .- --. .
```

You can decode morse code to human message as follow.

```
$ cd morse-code
$ python morse.py
input mode (d: decode, e: encode) > d
input your message > .... . .-.. .-.. --- --..--
HELLO,
input your message > .-- --- .-. .-.. -.. -.-.--
WORLD!
```

## Description

You can encode message to morse code, and decode morse code to message with this script.  
You can also add/remove your morse_code mapping.

## Usage

Only execute `morse.py` on python3.

```
$ python morse.py
```

If you want run tests, execute shell script as follow.

```
$ cd morse-code
$ ./exec_test.sh
```

## Customize

You can add/remove morse_code map by editing `./morse.yml`.

## Limitation

* Morse code is consists of `.` and `-`. If your signal use other character, please format your signal before/after this script.
* If there are some invalid input characters, the output becomes like `.-. .--*invalid_char*. .-`.