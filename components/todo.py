import flet as ft

class Task(ft.UserControl):
    def __init__(self, title: str, description: str | None, deadline: str | None, task_delete, status_change, task_edit, task_view):
        super().__init__()

        self.title: str = title # Task title, to be shown in list view
        self.description: str | None = description # Task description, to be shown in "More details view"
        self.deadline: str | None = deadline # Optional deadline date
        self.done = False # Wheter task is done or not, bu default: False

        # Functions
        self.task_delete = task_delete
        self.status_change = status_change
        self.task_edit = task_edit
        self.task_view = task_view
    
    def build(self):
        self.task_title = ft.Text(
            value=self.title,
        )

        self.task_description = ft.TextField(
            value=self.description,
            read_only=True,
            adaptive=True
        )

        self.check_done = ft.Checkbox(
            value=False,
            label=self.title,
            on_change=self.fn_status_change
        )

        self.btn_delete = ft.IconButton(
            icon=ft.icons.DELETE,
            on_click=self.fn_task_delete
        )

        self.btn_edit = ft.IconButton(
            icon=ft.icons.EDIT,
            on_click=self.fn_task_edit
        )

        self.btn_view_details = ft.IconButton(
            icon=ft.icons.REMOVE_RED_EYE,
            on_click=self.fn_task_view
        )

        self.list_view = ft.Row(
            controls=[
                self.check_done,
                #self.task_title,
                ft.Row(
                    controls=[
                        self.btn_view_details,
                        self.btn_edit,
                        self.btn_delete
                    ],
                    alignment=ft.MainAxisAlignment.END
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
        return self.list_view
    
    def get_task_data(self):
        return {
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline,
            "done": self.done
        }

    async def fn_status_change(self, _e):
        self.done = self.check_done.value
        await self.status_change(self)

    async def fn_task_delete(self, _e):
        await self.task_delete(self)
    
    async def fn_task_view(self, _e):
        task_data = self.get_task_data()
        await self.task_view(self, task_data)

    async def fn_task_edit(self, _e):
        task_data = self.get_task_data()
        await self.task_edit(self, task_data)

class TaskEdit(ft.UserControl):
    def __init__(self, title: str, description: str, deadline: str):
        super().__init__()

        self.title = title
        self.description = description
        self.deadline = deadline
    
    def build(self):
        self.edit_title_field = ft.TextField(
            value=self.title,
            multiline=False,
            adaptive=True,
            label="Title"
        )

        self.edit_description_field = ft.TextField(
            value=self.description,
            multiline=True,
            adaptive=True,
            label="Description"
        )

        self.deadline_label = ft.Text(
            value=self.deadline
        )

        self.btn_deadline_change = ft.IconButton(
            icon=ft.icons.CALENDAR_TODAY,
            on_click=lambda _: print("TODO: CHANGE DATE"),
            tooltip="Change deadline"
        )

        self.btn_deadline_remove = ft.IconButton(
            icon=ft.icons.DELETE,
            on_click=lambda _: print("TODO: DELETE DATE"),
            tooltip="Remove deadline"
        )

        self.btn_done = ft.ElevatedButton(
            text="Done",
            icon=ft.icons.DONE,
            on_click=lambda _: print("TODO: Save changes")
        )

        self.btn_cancel = ft.OutlinedButton(
            text="Cancel",
            on_click=lambda _: print("TODO: CANCEL EDITION")
        )