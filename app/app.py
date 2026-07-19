import reflex as rx

from app.states.counter_state import CounterState


def index() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.div(
                rx.icon("sparkles", class_name="h-8 w-8 text-blue-600"),
                rx.el.h1(
                    "A simple place to get started",
                    class_name="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl",
                ),
                rx.el.p(
                    "This minimal Reflex app is ready for you to explore. Use the counter below to confirm that state and events are connected.",
                    class_name="max-w-xl text-center text-base leading-7 text-gray-600",
                ),
                class_name="flex flex-col items-center gap-5 text-center",
            ),
            rx.el.div(
                rx.el.p(
                    "Interactive counter",
                    class_name="text-sm font-semibold uppercase tracking-wide text-gray-500",
                ),
                rx.el.div(
                    rx.el.button(
                        rx.icon("minus", class_name="h-5 w-5"),
                        aria_label="Decrease counter",
                        on_click=CounterState.decrement,
                        class_name="flex h-11 w-11 items-center justify-center rounded-lg border border-blue-200 bg-white text-blue-600 transition hover:bg-blue-50 focus:outline-2 focus:outline-offset-2 focus:outline-blue-600",
                    ),
                    rx.el.span(
                        CounterState.count,
                        class_name="min-w-16 text-center text-3xl font-bold tabular-nums text-gray-900",
                    ),
                    rx.el.button(
                        rx.icon("plus", class_name="h-5 w-5"),
                        aria_label="Increase counter",
                        on_click=CounterState.increment,
                        class_name="flex h-11 w-11 items-center justify-center rounded-lg bg-blue-600 text-white transition hover:bg-blue-700 focus:outline-2 focus:outline-offset-2 focus:outline-blue-600",
                    ),
                    class_name="flex items-center justify-center gap-5",
                ),
                rx.el.button(
                    "Reset",
                    on_click=CounterState.reset_count,
                    class_name="text-sm font-medium text-blue-600 transition hover:text-blue-800 focus:outline-2 focus:outline-offset-2 focus:outline-blue-600",
                ),
                class_name="flex w-full max-w-sm flex-col items-center gap-5 rounded-xl border border-gray-200 bg-white p-6",
            ),
            class_name="flex w-full max-w-2xl flex-col items-center gap-10 rounded-2xl border border-gray-200 bg-white p-8 sm:p-12",
        ),
        class_name="flex min-h-screen items-center justify-center bg-gray-100 px-4 py-12 font-['Inter']",
    )


app = rx.App(theme=rx.theme(appearance="light"))
app.add_page(index, route="/")
