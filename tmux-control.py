#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# tmux-control                                                                 #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is a way to configure and control tmux.                         #
#                                                                              #
# copyright (C) 2015 William Breaden Madden                                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################

# tmux customised configuration and launcher

# introduction

tmux is a terminal multiplexer. It enables a number of terminals to be created,
accessed and controlled from a single screen. tmux can be detached from and
continue running in the background, then reattached. tmux is essentially a tiled
window manager for the terminal.

When launched, tmux creates a new session with a single window and displays it.
A status line at the bottom of the display details information on the current
session and is used to enter interactive commands. The status line displays the
session number, the window number and other information. An active pane has a
bright green border while inactive panes have white borders.

A session is a single collection of pseudoterminals under the management of
tmux. Each session has one or more windows linked to it. A window occupies the
entire screen and may be split into rectangular panes, each of which is a
pseudoterminal. Any number of tmux instances may connect to the same session and
any number of the windows may be present in the same session. Once all sessions
are killed, tmux exits.

Each session is persistent and can survive accidental disconnection (e.g. via
SSH timeout) or intentional detaching (Ctrl a d). tmux can be reattached using
the command tmux attach.

In tmux, a session is displayed on screen by a client and all sessions are
managed by a single server. The server and each client are separate processes
which communicate through a socket in /tmp.

# keybindings

--------------------------------------------------------------------------------
|keybinding             |description                                           |
|-----------------------|------------------------------------------------------|
|Ctrl a ?               |List all keybindings (press q to exit).               |
|Ctrl a -               |Split window horizontally.                            |
|Ctrl a |               |Split window vertically.                              |
|Ctrl a x               |Kill the current pane.                                |
|Ctrl a o               |Change to the next pane in the current window.        |
|Ctrl a p               |Change to previous pane in the current window.        |
|Ctrl a <direction>     |Change to a pane adjacent to the current pane.        |
|Ctrl a Ctrl <direction>|Resize the current pane in steps of one cell.         |
|Ctrl a Alt <direction> |Resize the current pane in steps of five cells.       |
|Ctrl a f               |Prompt to search for text in open windows.            |
|Ctrl a [               |Enter copy mode to copy text or view the history.     |
|Ctrl a ]               |Paste the most recently copied buffer of text.        |
|Ctrl a =               |Choose which buffer to paste interactively from a     |
|                       |list.                                                 |
|Ctrl a :               |Enter the tmux command prompt.                        |
|Ctrl a t               |Display the time in the current pane (press q to      |
|                       |exit).                                                |
|Ctrl a d               |Detach the current client.                            |
|Ctrl a &               |Kill the current window.                              |
--------------------------------------------------------------------------------
|Ctrl a c               |Create a new window.                                  |
|Ctrl a l               |Change to the previous window.                        |
|Ctrl a n               |Change to the next window.                            |
|Ctrl a Alt n           |Change to the next window with a bell or activity     |
|                       |marker.                                               |
|Ctrl a Alt p           |Change to the previous window with a bell or activity |
|                       |marker.                                               |
|Ctrl a Ctrl o          |rotate the panes of the current window forwards.      |
|Ctrl a Alt o           |Rotate the panes of the current window backwards.     |
|Ctrl a Alt <1 -- 5>    |Arrange panes in one of five preset layouts: even     |
|                       |horizontal, even vertical, main horizontal, main      |
|                       |vertical or tiled.                                    |
|Ctrl a {               |Swap the current pane with the previous pane.         |
|Ctrl a }               |Swap the current pane with the next pane.             |
|Ctrl a !               |Break the current pane out of the window.             |
|Ctrl a %               |Split the current pane into two, left and right.      |
|Ctrl a "               |Split the current pane into two, top and bottom.      |
|Ctrl a ;               |Change to the previously-active pane.                 |
|Ctrl a $               |Rename the current session.                           |
|Ctrl a ,               |Rename the current window.                            |
|Ctrl a <0 -- 9>        |Select window 0 to 9.                                 |
|Ctrl a q               |Display pane indexes briefly.                         |
|Ctrl a i               |Display information about the current window.         |
|Ctrl a ~               |Show previous messages from tmux, if they exist (press|
|                       |q to exit).                                           |
|Ctrl a r               |Force a redraw of the attached client.                |
|Ctrl a z               |suspend the tmux client.                              |
--------------------------------------------------------------------------------

# launch modes

edit mode (default):
-----------------------
|          |          |
|          |          |
|          |          |
|          |          |
| terminal |  ranger  |
|          |          |
|          |          |
|          |          |
|          |          |
-----------------------

analysis mode:
-----------------------
|                     |
|       ranger        |
|                     |
|                     |
|---------------------|
|                     |
|      terminal       |
|                     |
|                     |
-----------------------

detail mode:
-----------------------
|          |          |
|  ranger  |          |
|----------|          |
| terminal |          |
|----------|  ranger  |
|   top    |          |
|----------|          |
|  arXiv   |          |
|          |          |
-----------------------

badass mode (does not work via SSH):
-----------------------
| ranger   |          |
|----------|          |
| terminal |          |
|----------|          |
| top      |  ranger  |
|----------|          |
| arXiv    |          |
|----------|          |
| cmus     |          |
-----------------------

Usage:
    program [options]

Options:
    -h, --help    display help message
    --version     display version and exit
    --analysis    analysis configuration
    --edit        edit configuration
    --detail      detail configuration
    --work        work configuration
    --badass      badass configuration
"""

name    = "tmux-control"
version = "2015-06-18T1217Z"

import os
import sys
import docopt

def main(options):

    # access options and arguments
    engageConfigurationAnalysis = options["--analysis"]
    engageConfigurationEdit     = options["--edit"]
    engageConfigurationDetail   = options["--detail"]
    engageConfigurationWork     = options["--work"]
    engageConfigurationBadass   = options["--badass"]

    # set up prerequisites
    prerequisites = [
        "tmux",
        "ranger",
        "htop",
        "elinks",
        "cmus"
    ]
    ensure_prerequisites(prerequisites)

    # set up executable
    hostName = os.uname()[1]
    if "physics.gla.ac.uk" in hostName:
        executable = "/afs/phas.gla.ac.uk/user/w/wbm/local/bin/tmux"
    elif "cern.ch" in hostName:
        executable = "/afs/phas.gla.ac.uk/user/w/wbm/local/bin/tmux"
    else:
        executable = "tmux"

    configurationAnalysis = \
    """
    set -g set-remain-on-exit on
    new -s "ANALYSIS"
    set-option -g prefix C-a
    unbind C-b
    bind - split-window -v
    bind | split-window -h
    ## colours
    set-option -g window-status-current-bg yellow
    set-option -g pane-active-border-fg yellow
    set -g status-fg black
    set -g status-bg '#FEFE0A'
    set -g message-fg black
    set -g message-bg '#FEFE0A'
    set -g message-command-fg black
    set -g message-command-bg '#FEFE0A'
    set-option -g mode-keys vi
    set -g history-limit 5000
    ## mouse mode
    set -g mode-mouse on
    set -g mouse-select-pane on
    set -g mouse-select-window on
    set -g mouse-resize-pane on # resize panes with mouse (drag borders)
    ## status
    set-option -g status-interval 1
    set-option -g status-left-length 20
    set-option -g status-left ''
    set-option -g status-right '%Y-%m-%dT%H%M%S '
    ## run programs in panes
    # split up-down
    split-window -v
    # split left up
    select-pane -t 0
    send-keys 'ranger' Enter
    select-pane -t 1
    send-keys 'clear' Enter
    set -g set-remain-on-exit off
    """

    configurationEdit = \
    """
    set -g set-remain-on-exit on
    new -s "EDITING"
    set-option -g prefix C-a
    unbind C-b
    bind - split-window -v
    bind | split-window -h
    ## colours
    set-option -g window-status-current-bg yellow
    set-option -g pane-active-border-fg yellow
    set -g status-fg black
    set -g status-bg '#FEFE0A'
    set -g message-fg black
    set -g message-bg '#FEFE0A'
    set -g message-command-fg black
    set -g message-command-bg '#FEFE0A'
    set-option -g mode-keys vi
    set -g history-limit 5000
    ## mouse mode
    set -g mode-mouse on
    set -g mouse-select-pane on
    set -g mouse-select-window on
    set -g mouse-resize-pane on # resize panes with mouse (drag borders)
    ## status
    set-option -g status-interval 1
    set-option -g status-left-length 20
    set-option -g status-left ''
    set-option -g status-right '%Y-%m-%dT%H%M%S '
    ## run programs in panes
    # split left-right
    split-window -h
    select-pane -t 0
    send-keys 'clear' Enter
    select-pane -t 1
    send-keys 'ranger' Enter
    set -g set-remain-on-exit off
    """

    configurationDetail = \
    """
    set -g set-remain-on-exit on
    new -s "DETAIL"
    set-option -g prefix C-a
    unbind C-b
    bind - split-window -v
    bind | split-window -h
    ## colours
    set-option -g window-status-current-bg yellow
    set-option -g pane-active-border-fg yellow
    set -g status-fg black
    set -g status-bg '#FEFE0A'
    set -g message-fg black
    set -g message-bg '#FEFE0A'
    set -g message-command-fg black
    set -g message-command-bg '#FEFE0A'
    set-option -g mode-keys vi
    set -g history-limit 5000
    ## mouse mode
    set -g mode-mouse on
    set -g mouse-select-pane on
    set -g mouse-select-window on
    set -g mouse-resize-pane on # resize panes with mouse (drag borders)
    ## status
    set-option -g status-interval 1
    set-option -g status-left-length 20
    set-option -g status-left ''
    set-option -g status-right '%Y-%m-%dT%H%M%S '
    ## run programs in panes
    # split left-right
    split-window -h
    # split left up
    select-pane -t 0
    split-window -v
    select-pane -t 0
    split-window -v
    select-pane -t 0
    split-window -v
    select-pane -t 0
    send-keys 'ranger' Enter
    select-pane -t 1
    send-keys 'clear' Enter
    select-pane -t 2
    #send-keys 'htop' Enter
    select-pane -t 3
    send-keys 'elinks http://arxiv.org/list/hep-ph/new' Enter
    select-pane -t 4
    send-keys 'ranger' Enter
    set -g set-remain-on-exit off
    """

    configurationWork = \
    """
    set -g set-remain-on-exit on
    new -s "WORK"
    set-option -g prefix C-a
    unbind C-b
    bind - split-window -v
    bind | split-window -h
    ## colours
    set-option -g window-status-current-bg yellow
    set-option -g pane-active-border-fg yellow
    set -g status-fg black
    set -g status-bg '#FEFE0A'
    set -g message-fg black
    set -g message-bg '#FEFE0A'
    set -g message-command-fg black
    set -g message-command-bg '#FEFE0A'
    set-option -g mode-keys vi
    set -g history-limit 5000
    ## mouse mode
    set -g mode-mouse on
    set -g mouse-select-pane on
    set -g mouse-select-window on
    set -g mouse-resize-pane on # resize panes with mouse (drag borders)
    ## status
    set-option -g status-interval 1
    set-option -g status-left-length 20
    set-option -g status-left ''
    set-option -g status-right '%Y-%m-%dT%H%M%S '
    ## run programs in panes
    split-window -v
    select-pane -t 1
    split-window -v
    select-pane -t 3
    split-window -h
    select-pane -t 0
    send-keys 'ranger' Enter
    select-pane -t 1
    send-keys 'clear' Enter
    select-pane -t 2
    send-keys 'ranger' Enter
    select-pane -t 3
    send-keys 'cmus' Enter
    set -g set-remain-on-exit off
    """

    configurationBadass = \
    """
    set -g set-remain-on-exit on
    new -s "BADASS"
    set-option -g prefix C-a
    unbind C-b
    bind - split-window -v
    bind | split-window -h
    ## colours
    set-option -g window-status-current-bg yellow
    set-option -g pane-active-border-fg yellow
    set -g status-fg black
    set -g status-bg '#FEFE0A'
    set -g message-fg black
    set -g message-bg '#FEFE0A'
    set -g message-command-fg black
    set -g message-command-bg '#FEFE0A'
    set-option -g mode-keys vi
    set -g history-limit 5000
    ## mouse mode
    set -g mode-mouse on
    set -g mouse-select-pane on
    set -g mouse-select-window on
    set -g mouse-resize-pane on # resize panes with mouse (drag borders)
    ## status
    set-option -g status-interval 1
    set-option -g status-left-length 20
    set-option -g status-left ''
    set-option -g status-right '%Y-%m-%dT%H%M%S '
    ## run programs in panes
    # split left-right
    split-window -h
    # split left up
    select-pane -t 0
    split-window -v
    select-pane -t 0
    split-window -v
    select-pane -t 0
    split-window -v
    select-pane -t 3
    split-window -v
    select-pane -t 0
    send-keys 'ranger' Enter
    select-pane -t 1
    send-keys 'clear' Enter
    select-pane -t 2
    #send-keys 'htop' Enter
    select-pane -t 3
    send-keys 'elinks http://arxiv.org/list/hep-ph/new' Enter
    select-pane -t 4
    send-keys 'cmus' Enter
    select-pane -t 5
    send-keys 'ranger' Enter
    select-pane -t 4
    set -g set-remain-on-exit off
    """

    if engageConfigurationAnalysis is True:
        configurationtmux = configurationAnalysis
    elif engageConfigurationEdit is True:
        configurationtmux = configurationEdit
    elif engageConfigurationDetail is True:
        configurationtmux = configurationDetail
    elif engageConfigurationWork is True:
        configurationtmux = configurationWork
    elif engageConfigurationBadass is True:
        configurationtmux = configurationBadass
    else:
        configurationtmux = configurationWork

    command = \
        "configurationtmux=\"$(mktemp)\" && { echo \"" + \
        configurationtmux + \
        "\" > \"${configurationtmux}\"; " + \
        executable + \
        " -f \"${configurationtmux}\" attach; " + \
        "unlink \"${configurationtmux}\"; }"
    os.system(command)

    sys.exit()

def ensure_prerequisites(prerequisites):
    for prerequisite in prerequisites:
        if which(prerequisite) is None:
            instate(prerequisite)

def instate(program):
    print("instate {program}".format(program = program))
    command = "sudo apt-get -y install " + program
    os.system(command)

def which(program):
    def is_exe(fpath):
        return(os.path.isfile(fpath) and os.access(fpath, os.X_OK))
    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return(program)
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return(exe_file)
    return(None)

if __name__ == "__main__":
    options = docopt.docopt(__doc__)
    if options["--version"]:
        print(version)
        exit()
    main(options)