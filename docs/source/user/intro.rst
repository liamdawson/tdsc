.. _introduction:

############
Introduction
############

.. image:: https://farm6.staticflickr.com/5552/14761159432_850c176b62_o_d.jpg

**********
Philosophy
**********

*tdsc* is aimed as a lightweight framework to configure environments equally
based on intent and procedure.

*****
Goals
*****

*tdsc* is designed with the following values in mind:

-----------
Portability
-----------

*tdsc* strategies (collections of states) should, in their simplest cases, be
able to run on all of the "standard environments":

+---------------+---------------------------+---------------------------------+
| Environment   | Requirements              | Notes                           |
+===============+===========================+=================================+
| Linux systems | - Python 3.4+ (preferred) | - Ideally, this definition will |
|               | - or Python 2.7           |   be expanded to encompass a    |
|               |                           |   broader set of "``*nix``"     |
|               |                           |   systems.                      |
+---------------+---------------------------+---------------------------------+
| macos         | - El Capitan (10.11),     | - Assuming system install of    |
|               |   or later                |   Python 2.7 is available.      |
+---------------+---------------------------+---------------------------------+
| Windows 10    | - Installed python 2.7,   |                                 |
|               |   or 3.4+ (preferred)     |                                 |
+---------------+---------------------------+---------------------------------+

In practice, compatibility of *tdsc* functions will be less universal,
especially with functions that only have relevance on particular platforms.
(An example would be actions that modify the Windows registry, which has no
counterpart on macos or Linux systems). Functions contained within *tdsc* are
expected to publish compatibility information as part of their documentation.

.. todo:: Document packaging approaches

*tdsc* requires a number of packages found from |pypi|_, which must be made
available at runtime.
