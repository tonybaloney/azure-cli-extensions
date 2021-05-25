Microsoft Azure CLI EZ Extension
================================

An extension to the Azure CLI with quick, simple commands for creating web apps.

Installation
------------

To install: 

.. code-block::

    > az extension add --source https://github.com/tonybaloney/azure-cli-extensions/releases/download/0.0.1/ez-0.1.0-py3-none-any.whl

Creating a project
------------------

Initialize your project:

.. code-block::

    > az ez init --location westus


This will create a ``.azure/settings.json`` file in the local directory with the configuration.
Your application will have an automatically generated resource group and application name.
You can change this by using the ``-r`` flag: 

.. code-block::

    > az ez init --location westus -r my-app-name

Deploying a basic app
---------------------

Run the ``ez app create`` command to create a web application, plan, logging and configured SCM deployment on Azure:

.. code-block::

    > az ez app create

It will prompt you to choose the runtime and version. Alternatively, you can set those ahead of time:

.. code-block::

    > az ez app create --runtime python --version 3.8

Pushing your code to Azure
--------------------------

After creating your basic application code to the local directory. Use git to check it in and push to the ``azure`` remote:

.. code-block::

    > git add * 
    > git commit -m "initial project"
    > git push master azure

This will kick off the automated deployment.

Deleting your project
---------------------

To remove the local settings and the resources on Azure, run:

.. code-block::

    > az ez destroy
