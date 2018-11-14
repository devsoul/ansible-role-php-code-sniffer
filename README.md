PHP Code Sniffer tools Ansible role
=========
[![Build Status](https://travis-ci.com/devsoul/ansible-role-php-code-sniffer.svg?branch=master)](https://travis-ci.com/devsoul/ansible-role-php-code-sniffer)

If you are a PHP developer and you use PHP Code Sniffer.

Requirements
------------
  - minimum `php 5.4` 

Role Variables
--------------
None

Dependencies
------------
None

Example Playbook
----------------
    - hosts: php
      roles:
        - devsoul.phpcodesniffer

Check if it's installed:
------
    phpcs --version
    phpcbf --version

License
-------
MIT

Author Information
------------------

:-)
