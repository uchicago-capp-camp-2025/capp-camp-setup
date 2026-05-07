CAPP Camp: Git self-evaluation
==============================

CAPP Camp introduces students to the Linux operating system, the Git
version control system, and the workflow used in most of the CAPP CS
core courses. CAPP Camp also provides an excellent opportunity to get
to know your classmates and the CAPP team ahead of the start of the
quarter.

While most incoming students do not have exposure to the tools used in
CS courses, every year there are a few students who have prior
experience with the tool that is most challenging to learn on your
own, namely Git.  This self-test is intended to help such students
determine whether they should plan to attend CAPP Camp.

If you have little or no prior experience with Git, please plan to
attend CAPP Camp (or makeup CAPP Camp, if you are unable to be in
Chicago at the end of August).

**There is no benefit to gaming this assessment, so please do not use
a generative AI tool to determine the steps needed to complete it.**
If you need to rely on a tool to help you do the work in this
assessment then your knowledge of Git is insufficient and you should
plan to attend CAPP Camp.

In this assessment, you will work with a repository that will be
pre-loaded with a set of files.  Your task will be to make changes to
the existing file organization, modify an existing file, create a new
file, and record all of these changes using the appropriate Git
commands.

Tools
-----

Before you get started on the assessment, you may need to install a
couple of tools.

**Linux**

During CAPP Camp, we will cover using the Linux command-line to work
with directories and files and to run Git commands.  These skills will
be important for your CS coursework.  To ensure that you are prepared,
we encourage you to do the work for this assessment from the
command-line rather than using a point-and-click interface.

If you are using a machine running the Windows operating system and do
not have the Windows Subsystem for Linux (WSL) installed, please
install it.  You can find installation instructions at this :ref:`link
<wsl-install>`.  (Please note: we require students using Windows to
run Windows 11.)  Once you have it installed, open a window running
WSL.

MacOS users should plan to use the terminal application for this
assessment.  See this `link
<https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/mac>`__ for instructions on how to open a MacOS terminal.

**Python**

You you will be using ``uv`` to manage your Python environment in CAPP
30121 and CAPP 30122.  You can find information about how to install
``uv`` and how to install Python using ``uv`` at this :ref:`link <python_setup>`.

If you already have Python 3.13 (or newer) installed, you can use it
for this assessment and install ``uv`` later.


Getting Started
---------------

As is done in many CS courses, we will be using GitHub classroom to
create the repository that you will be using for this assessment.

To create your repository, click on the following
`URL <https://classroom.github.com/a/I6j5YwnB>`__ and then authorize GitHub
to connect your account to our GitHub classroom.  You will be asked to
choose a team name.  Please use your **CNetID** (that is, the part of
your UChicago email address that comes before ``@uchicago.edu``) as
your team name.

Once you have accepted the assignment, you will be able to find your
repository on GitHub at the URL ``https://github.com/uchicago-capp-camp-2026/self-assessment-TEAM_NAME``,
where ``TEAM_NAME`` the team name you chose.

The next step is to clone your repository. It will contain the
following:

- ``README.md`` - a basic README file,
- ``check.py`` - a python script that verifies that your directory structure is organized as expected, and
- ``files/`` - a directory with a collection of text files.

You can check your work at anytime by running the Python script
``check.py``.  If you have installed ``uv``, you can use the following
command to run the script:

::

   $ uv run python check.py


Tasks
-----

**Task 1:** Create the following directories: ``animals``,
``space/planets``, and ``space/comets`` and then move the files related to:

- animals from ``files`` to ``animals``,
- planets from ``files`` to ``space/planets``, and
- comets from ``files`` to ``space/comets``.

**Task 2:** Update the file for Jupiter to have 95 moons, as confirmed in 2023, instead of 92 as currently listed.

**Task 3:** Add a new file named ``venus.txt`` to ``space/planets``. Venus has no moons, so the new file should contain the following text: ``moons: 0``.

**Task 4:** Create a commit with all of your changes and push it to GitHub.

Submitting your work
--------------------

Once you have pushed your changes to GitHub, please complete this
short `form <https://forms.gle/ZkybKYESWRZRkKTE9>`__ to let us know
that you have completed the self-evaluation.  One of Anne Rogers and
James Turk will review your work and let you know if we have any
concerns.

If you were able to complete this assessment in 20-30 minutes and
without having to rely on doing web searches or using an LLM-based
tool, then you can safely skip CAPP Camp. Please note, though, if you
do not have prior experience with Linux or with basic debugging and
you are available, you are welcome to come to the main CAPP Camp or
makeup CAPP Camp to help develop those skills.





	

