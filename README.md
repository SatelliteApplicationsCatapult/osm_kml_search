# Search OSM for tags inside a bounding box

Prints out the number of osm ways with the given feature tags inside the kml's polygon

## Running

Needs to be given a KML file with the search area and a set of feature tags

The first time you run this in a shell you will need to activate the virtual environment.
linux/wsl:
```bash
source ./venv/scripts/activate
```
windows powershell:
```powershell
.\venv\Scripts\activate.ps1
```
windows cmd:
```bat
.\venv\Scripts\activate.bat
```

Now you can run the script for your input parameters. This should be roughly the same for all operating systems, though 
you may need to change the path separators depending on your shell in windows.

```bash
python -m osm_kml_search.main --kml /path/to/a.kml --features "\"landuse\"=\"quarry\"" --features "\"landuse\"=\"industrial\""
```

## Setup

Open a shell/command prompt/terminal.
Change the directory to where you want to set up this system.

You will need git installed. Have a look here if you dont: https://git-scm.com/downloads
```bash
git clone https://github.com/something something something 
```

You will need python, at least version 3.8. Have a look here if you need instructions. https://wiki.python.org/moin/BeginnersGuide/Download

Now you should be able to run the following to verify that its working

```bash
python --version
```

Create and activate a virtual environment

```bash
python -m venv venv
```

Now follow the instructions above for activating your virtual environment. You should see a change in your prompt when you do this.

Now install the dependencies


```bash
python setup.py install
```

At this point you should be ready to start using the script. 