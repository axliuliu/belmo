import reflex as rx

from app.states.counter_state import CounterState


def counter_card() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.div(
                rx.icon("calculator", class_name="h-6 w-6 text-blue-600"),
                rx.el.h1(
                    "Counter",
                    class_name="text-2xl font-semibold text-gray-900",
                ),
                class_name="flex items-center gap-3",
            ),
            rx.el.p(
                "A simple Reflex counter with dependable controls.",
                class_name="mt-2 text-sm text-gray-600",
            ),
            rx.el.div(
                rx.el.p(
                    CounterState.count,
                    class_name="text-6xl font-bold tabular-nums text-blue-600",
                ),
                class_name="flex min-h-40 items-center justify-center rounded-lg border border-gray-200 bg-gray-50 px-6 py-8",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("minus", class_name="h-4 w-4"),
                    "Decrement",
                    on_click=CounterState.decrement,
                    class_name="flex flex-1 items-center justify-center gap-2 rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 transition hover:border-blue-400 hover:bg-blue-50 hover:text-blue-700",
                ),
                rx.el.button(
                    rx.icon("plus", class_name="h-4 w-4"),
                    "Increment",
                    on_click=CounterState.increment,
                    class_name="flex flex-1 items-center justify-center gap-2 rounded-md bg-blue-600 px-4 py-2 text-sm font-medium text-white transition hover:bg-blue-700",
                ),
                class_name="flex flex-col gap-3 sm:flex-row",
            ),
            rx.el.button(
                rx.icon("rotate-ccw", class_name="h-4 w-4"),
                "Reset counter",
                on_click=CounterState.reset_count,
                class_name="flex w-full items-center justify-center gap-2 rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-600 transition hover:border-blue-400 hover:bg-blue-50 hover:text-blue-700",
            ),
            class_name="w-full max-w-md space-y-6 rounded-xl border border-gray-200 bg-white p-6",
        ),
        class_name="flex min-h-screen w-full items-center justify-center bg-gray-100 px-4 py-8",
    )


def index() -> rx.Component:
    return counter_card()


app = rx.App(theme=rx.theme(appearance="light"))
app.add_page(index, route="/")
