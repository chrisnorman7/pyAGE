from abc import ABC
from typing import Callable, List

from pyage.constants import KEY, MOD
from pyage.events.key import KeyEvent


class MenuItem(ABC):

    _keys: List[KeyEvent]

    def __init__(self) -> None:

        self._keys = []

    def add_key_event(
        self,
        key: KEY,
        function: Callable[[bool], None],
        mod: MOD = MOD.NONE,
        repeat: float = 0.0,
    ) -> None:

        e: KeyEvent = KeyEvent(key=key, function=function, mod=mod, repeat=repeat)

        if e not in self._keys:
            self._keys.append(e)

    def selected(self) -> None:

        e: KeyEvent

        from pyage.app import App

        app: App = App()

        for e in self._keys:
            app._event_processor.add_key_event(
                key=e._key,
                function=e._function,
                mod=e._mod,
                repeat=e._repeat,
            )

    def deselected(self) -> None:

        e: KeyEvent

        from pyage.app import App

        app: App = App()

        for e in self._keys:
            app._event_processor.remove_key_event(key=e._key, mod=e._mod)
