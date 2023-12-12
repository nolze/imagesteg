# imagesteg

`imagesteg` (formerly `imgsteg`) is a simple image steganalysis (steganography analysis) tool in Python with web-based GUI.
A quick alternative to [StegSolve](http://www.caesum.com/handbook/stego.htm).

## Features

* Provides Python API, CLI, and interactive web interface

## Usage examples

```bash
$ imagesteg ui examples/problem.png # Launch web interface
Listening on http://localhost:8080/
Hit Ctrl-C to quit.
```

```bash
$ imagesteg extract_bit_plane examples/problem.png output.png --bit b0
```

```bash
$ imagesteg extract_bits examples/stg300.png --bits r0
Congrats
You win!
The
Flag
is
4E34B38257200616FB75CD869B8C3CF0 *** Congrats
...
```

## Install

```
pip install imagesteg
```

Uninstall:

```
pip uninstall imagesteg
```

## Todo

* [ ] Add examples
* [ ] Add usage

## References

* StegSolve <http://www.caesum.com/handbook/stego.htm>
* Stegpy <https://www.balda.ch/posts/2013/Jun/04/release-stegpy/>
* 青い空を見上げればいつもそこに白い猫 <https://digitaltravesia.jp/usamimihurricane/webhelp/_RESOURCE/MenuItem/another/anotherAboutSteganography.html>
