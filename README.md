## BuildFeed CLI
### Example
![Example](https://raw.githubusercontent.com/nickurt/buildfeed-cli/master/examples/example.gif)

### Requirements
    pip install -r requirements.txt

### Using BuildFeed

#### Latest
Retrieve the latest builds added to BuildFeed

    bf.py latest

#### Highest
Retrieve the highest builds from BuildFeed

    bf.py highest

#### Flights
Retrieve the flights builds (logging/win10) from BuildFeed

    bf.py flights -r wis        // Windows Insider Slow
    bf.py flights -r wif		// Windows Insider Fast

    bf.py flights -r msit       // Microsoft Internal
    bf.py flights -r osg        // Operating Systems Group
    bf.py flights -r canary     // Canary

#### Branch
Retrieve the latest builds from a branch

    bf.py branch -b fbl_mgmt

#### Help

    bf.py -h