========================
People, by Valuehorizon
========================

.. image:: https://travis-ci.org/Valuehorizon/valuehorizon-people.svg?branch=master
   :target: https://travis-ci.org/Valuehorizon/valuehorizon-people
.. image:: https://coveralls.io/repos/Valuehorizon/valuehorizon-people/badge.svg
   :target: https://coveralls.io/r/Valuehorizon/valuehorizon-people
.. image:: https://codeclimate.com/github/Valuehorizon/valuehorizon-people/badges/gpa.svg
   :target: https://codeclimate.com/github/Valuehorizon/valuehorizon-people


A Django-based People data toolkit. 
It also includes documentation, test coverage and a good amount of sample data to play around with.
This app is a part of the Valuehorizon application ecosystem.

Installation
============

Start by creating a new ``virtualenv`` for your project ::

    mkvirtualenv myproject

Next install ``numpy`` and ``pandas`` and optionally ``scipy`` ::

    pip install numpy==1.8.0
    pip install scipy==0.13.3
    pip install pandas==0.13.0

Finally, install ``valuehorizon-people`` using ``pip``::

    pip install valuehorizon-people

Q: 
    Why do we require all these numerical computation packages? It seems somewhat unnecessary.
A: 
    It might be a bit tedious to compile these packages. However, this app depends on other apps that require time series functionality. Bear with us - the end result is a pretty powerful solution.

Contributing
============

Please file bugs and send pull requests to the `GitHub repository`_ and `issue
tracker`_.

.. _GitHub repository: https://github.com/Valuehorizon/valuehorizon-people/
.. _issue tracker: https://github.com/Valuehorizon/valuehorizon-people/issues

Commercial Support
==================

This project is sponsored by Valuehorizon_. If you require assistance on
your project(s), please contact us: support@valuehorizon.com.

.. _Valuehorizon: http://www.valuehorizon.com
