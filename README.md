# rr-notifications
Application for mass texting to specific groups. It uses Twilio to send the messages and Django to manage administration and signup


## Installation for Dev

You'll need a few things on your machine to get started. Currently, this guide assumes you are using a Linux or Mac.

### Prerequisites
Make sure to have the following installed

* Python 3.6.*
* [pipenv](https://docs.pipenv.org/)
	* [Basic Usage Docs](https://docs.pipenv.org/basics/)
* [yarn](https://yarnpkg.com/en/) or npm (for frontend work)

### Django Setup

Django 2.0 is being used. All the required Python packages are managed using pipenv. It's probably worthwhile to learn a bit about pipenv. 



To install what's needed move to the nested rr-notifications directory. There will be a `Pipfile` and `Pipfile.lock`

In the terminal,
  
  ```bash
  pipenv shell
  ```
That will activate a Python virtual environment for the project.

Next install all the required packages

```bash
pipenv install
```


## The template

```
# *Project title*

*Short description of your project, in one or two sentences.* 

## Setup 

### Dependencies

*Provide links and descriptions for the third-party libraries you're having your users install.*

### Installation

* Mac OS X
* Ubuntu
* Windows (if applicable)

### Getting started

*What does your user need to know to get everything ready after installation?*
*Think about databases, config files, and settings.*

## Usage

*Give your users a sense of the workflow for using your project/tool.*
*For a website this might include code for running locally.*
*For an API this might include method and parameter specs.*

## Demo

*Grab a simple block of code that makes use of your project/tool and paste it here.*

## Team

* *Name, Organization - role or tasks worked on*

*Add a "contributors" section if you've incorporated pull requests.*

## Errors and bugs

If something is not behaving intuitively, it is a bug and should be reported.
Report it here by creating an issue: https://github.com/datamade/your-repo-here/issues

Help us fix the problem as quickly as possible by following [Mozilla's guidelines for reporting bugs.](https://developer.mozilla.org/en-US/docs/Mozilla/QA/Bug_writing_guidelines#General_Outline_of_a_Bug_Report)

## Patches and pull requests

Your patches are welcome. Here's our suggested workflow:
 
* Fork the project.
* Make your feature addition or bug fix.
* Send us a pull request with a description of your work. Bonus points for topic branches!

## Copyright and attribution

Copyright (c) 2016 DataMade. Released under the [MIT License](https://github.com/datamade/your-repo-here/blob/master/LICENSE).
```
