# imgsteg

imgsteg is a simple steganalysis tool for images.

## Features

* Provides Python API, CLI, and web interface

## Usage examples

```bash
$ imgsteg ui examples/problem.png # Launch web interface
Listening on http://localhost:8080/
Hit Ctrl-C to quit.
```

```bash
$ imgsteg extract_bit_plane examples/problem.png output.png --bit b0
```

```bash
$ imgsteg extract_bits examples/stg300.png --bits r0
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
python setup.py install
```

Uninstall:

```
pip uninstall imgsteg
```

## Todo

* [ ] Add examples
* [ ] Add usage

## References

* Stegsolve <http://www.caesum.com/handbook/stego.htm>
* Stegpy <https://www.balda.ch/posts/2013/Jun/04/release-stegpy/>
* 青い空を見上げればいつもそこに白い猫 <https://digitaltravesia.jp/usamimihurricane/webhelp/_RESOURCE/MenuItem/another/anotherAboutSteganography.html>
