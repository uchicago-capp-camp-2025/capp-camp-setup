.. _python_setup:

Setting up Python
=================

There are many tools available for setting up Python environments
(virtualenv, pip, conda, etc).  You will be using the ``uv`` tool in
CAPP 30121 and CAPP 30122 for managing Python environments.

This tool will make it easy for your instructors to ensure that
everyone is using the same development environment, which will help
eliminate the kinds of problems that can arise when students use the
wrong version of a library.  Fortunately, it is easy to install and
easy to use.

We will discuss why we chose ``uv`` over other tools during Friday's
session.

This document explains how to install ``uv`` and then how to use it to
install the version of Python specified by your CAPP 30121 instructor.


Installing uv
-------------

First, open a MacOS or WSL Terminal.

To install ``uv`` run::

   $ curl -LsSf https://astral.sh/uv/install.sh | sh

Then, on MacOS with zsh::

   $ echo -e "autoload -Uz compinit\ncompinit" >> ~/.zshrc
   $ echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc

Or, on WSL with bash::

   $ echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc

If you have chosen to use a shell other than the default, see
https://docs.astral.sh/uv/getting-started/installation/#shell-autocompletion

Installing Python using uv
--------------------------

To install the version of Python specified by the CAPP 30121 instructor, run::

  $ uv python install 3.13

the output will look something like::

  $  uv python install 3.13
  Installed Python 3.13.5 in 1.24s
   + cpython-3.13.5-macos-aarch64-none (python3.13)

Your output may vary depending on your platform.

You can check the installed version of Python with the following command::

  $ uv run python -V

the output will look something like::

  Python 3.13.5
  
If you see a version that does not start with 3.13, please ask for help.
  

