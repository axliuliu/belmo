import reflex as rx


class CounterState(rx.State):
    count: int = 0

    @rx.event
    def increment(self) -> None:
        self.count += 1

    @rx.event
    def decrement(self) -> None:
        self.count -= 1

    @rx.event
    def reset_count(self) -> None:
        self.count = 0
