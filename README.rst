~~~~~~~~~~~~~~~~~~~~~~~
ofxstatement-1822direkt
~~~~~~~~~~~~~~~~~~~~~~~

`ofxstatement`_ plugin to support 1822direkt.com bank statements

`ofxstatement`_ is a tool
to convert proprietary bank statement to OFX format, suitable for
importing to GnuCash. Plugin for `ofxstatement`_ parses a particular
proprietary bank statement format and produces common data structure,
that is then formatted into an OFX file.

This project provides an `ofxstatement`_ plugin for the German bank
1822direkt.com

.. _ofxstatement: https://github.com/kedder/ofxstatement

1822direkt used to provide OFX downloads but canceld this without
warning last weekend.  Shame on them.

Using `ofxstatement`_ and this plugin, I  successfully converted the
standard CSV statements (the first of the two available) to OFX and
import this into my banking software.


Requirements
============

You need python 3.x to run this as ofxstament seems to requires python3


Installation
============

There are multiple ways of installing Python packages. This is just one
example:

.. code:: bash

  pip3 install --user ofxstatement
  git clone https://github.com/MirkoDziadzka/ofxstatement-1822direkt
  cd ofxstatement-1822direkt
  pip3 install --user .

Check the Python documentation on instructions for you operating system and
setup. Remember you must use Python 3.


Setup
=====

Check if plugin is installed:

.. code:: bash

  ofxstatement list-plugins

Expected output::

  germany_1822direkt

Edit config. The *account* is the ID used by your accounting program to
associate the transactions with a certain account. Probably you want to use
your bank account number (Kontonummer) i.e. the last 10 digits of your IBAN.

.. code:: bash

  ofxstatement edit-config

A text editor will open. Configure something like this::

  [1822direkt]
  plugin = germany_1822direkt
  account = 0123456789

Some other config options you may set are:

* *bank* (default: 50050201)
* *currency* (default: EUR)
* *charset* (default: iso-8859-1)


Usage
=====

.. code:: bash

  ofxstatement convert -t 1822direkt umsaetze-0123456789-03.02.2018_15_05.csv test.ofx

You may then import *test.ofx* into gnuCash or a similar accounting program.
