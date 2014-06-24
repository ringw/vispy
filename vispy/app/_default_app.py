# -*- coding: utf-8 -*-
# Copyright (c) 2014, Vispy Development Team.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from .application import Application

# Initialize default app
# Only for use thin *this* module. 
# One should always call use() to obtain the default app.
default_app = None


def use(backend_name=None):
    """Create and get the default Application object. It is safe to
    call this function multiple times, as long as backend_name is None
    or matches the already selected backend.
    
    See Application for details on available backends.
    """
    global default_app
    
    # If we already have a default_app, raise error or return
    if default_app is not None:
        names = default_app.backend_name.lower().replace('(', ' ').strip(') ')
        names = [name for name in names.split(' ') if name]
        if backend_name and backend_name.lower() not in names:
            raise RuntimeError('Can only select a backend once.')
        else:
            return default_app  # Current backend matches backend_name
    
    # Create default app
    default_app = Application(backend_name)
    return default_app


def create():
    """Create the native application.
    """
    default_app = use()
    return default_app.create()


def run():
    """Enter the native GUI event loop.
    """
    default_app = use()
    return default_app.run()


def quit():
    """Quit the native GUI event loop.
    """
    default_app = use()
    return default_app.quit()


def process_events():
    """Process all pending GUI events

    If the mainloop is not running, this should be done regularly to
    keep the visualization interactive and to keep the event system going.
    """
    default_app = use()
    return default_app.process_events()
