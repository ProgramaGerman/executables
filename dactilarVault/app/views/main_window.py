import customtkinter as ctk
from typing import Optional, Callable

from app.presenters.vault_presenter import VaultPresenter


class MainWindow(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self._presenter = VaultPresenter()
        self._presenter.attach_view(self)

        self.title("DactilarVault")
        self.geometry("800x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self._setup_ui()
        self._show_setup_or_login()

    def _setup_ui(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.main_container = ctk.CTkFrame(self)
        self.main_container.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.main_container.grid_columnconfigure(0, weight=1)

    def _clear_container(self) -> None:
        for widget in self.main_container.winfo_children():
            widget.destroy()

    def _show_setup_or_login(self) -> None:
        self._clear_container()

        if not self._presenter._vault.has_master_password():
            self._show_setup_screen()
        else:
            self._show_login_screen()

    def _show_setup_screen(self) -> None:
        title = ctk.CTkLabel(
            self.main_container,
            text="Configurar DactilarVault",
            font=ctk.CTkFont(size=24, weight="bold"),
        )
        title.pack(pady=20)

        self.password_entry = ctk.CTkEntry(
            self.main_container,
            placeholder_text="Nueva contraseña maestra",
            show="*",
            width=300,
        )
        self.password_entry.pack(pady=10)

        self.confirm_entry = ctk.CTkEntry(
            self.main_container,
            placeholder_text="Confirmar contraseña",
            show="*",
            width=300,
        )
        self.confirm_entry.pack(pady=10)

        self.status_label = ctk.CTkLabel(
            self.main_container, text="", text_color="orange"
        )
        self.status_label.pack(pady=10)

        btn = ctk.CTkButton(
            self.main_container,
            text="Crear Bóveda",
            command=self._on_setup_clicked,
            width=200,
        )
        btn.pack(pady=20)

    def _show_login_screen(self) -> None:
        title = ctk.CTkLabel(
            self.main_container,
            text="DactilarVault - Acceso",
            font=ctk.CTkFont(size=24, weight="bold"),
        )
        title.pack(pady=20)

        self.password_entry = ctk.CTkEntry(
            self.main_container,
            placeholder_text="Contraseña maestra",
            show="*",
            width=300,
        )
        self.password_entry.pack(pady=10)

        self.status_label = ctk.CTkLabel(
            self.main_container, text="", text_color="orange"
        )
        self.status_label.pack(pady=10)

        btn = ctk.CTkButton(
            self.main_container,
            text="Desbloquear",
            command=self._on_login_clicked,
            width=200,
        )
        btn.pack(pady=10)

        if self._presenter.is_hardware_available():
            bio_btn = ctk.CTkButton(
                self.main_container,
                text="Usar Huella",
                command=self._on_fingerprint_click,
                width=200,
            )
            bio_btn.pack(pady=10)

    def _show_vault_screen(self) -> None:
        self._clear_container()

        header = ctk.CTkFrame(self.main_container)
        header.pack(fill="x", pady=(0, 20))

        title = ctk.CTkLabel(
            header,
            text="DactilarVault",
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        title.pack(side="left", padx=10)

        lock_btn = ctk.CTkButton(
            header,
            text="Bloquear",
            command=self._on_lock_clicked,
            width=100,
        )
        lock_btn.pack(side="right", padx=10)

        add_btn = ctk.CTkButton(
            self.main_container,
            text="+ Nueva Entrada",
            command=self._show_add_entry_dialog,
        )
        add_btn.pack(pady=10)

        self.entries_frame = ctk.CTkScrollableFrame(self.main_container)
        self.entries_frame.pack(fill="both", expand=True, pady=10)

        self._refresh_entries()

    def _refresh_entries(self) -> None:
        for widget in self.entries_frame.winfo_children():
            widget.destroy()

        entries = self._presenter.get_entries()
        if not entries:
            empty = ctk.CTkLabel(
                self.entries_frame,
                text="No hay entradas guardadas",
                text_color="gray",
            )
            empty.pack(pady=50)
            return

        for entry in entries:
            card = ctk.CTkFrame(self.entries_frame)
            card.pack(fill="x", pady=5, padx=5)

            ctk.CTkLabel(card, text=entry.title, font=ctk.CTkFont(weight="bold")).pack(
                side="left", padx=10, pady=10
            )
            ctk.CTkLabel(card, text=entry.category, text_color="gray").pack(
                side="left", padx=10
            )

            delete_btn = ctk.CTkButton(
                card,
                text="X",
                width=40,
                fg_color="red",
                command=lambda e=entry: self._delete_entry(e.entry_id),
            )
            delete_btn.pack(side="right", padx=5)

    def _show_add_entry_dialog(self) -> None:
        dialog = ctk.CTkToplevel(self)
        dialog.title("Nueva Entrada")
        dialog.geometry("400x300")
        dialog.transient(self)
        dialog.grab_set()

        ctk.CTkLabel(dialog, text="Título:", anchor="w").pack(
            fill="x", padx=20, pady=(20, 5)
        )
        title_entry = ctk.CTkEntry(dialog, width=360)
        title_entry.pack(padx=20, pady=(0, 10))

        ctk.CTkLabel(dialog, text="Categoría:", anchor="w").pack(
            fill="x", padx=20, pady=(0, 5)
        )
        category_entry = ctk.CTkEntry(dialog, width=360)
        category_entry.pack(padx=20, pady=(0, 10))

        ctk.CTkLabel(dialog, text="Datos secretos:", anchor="w").pack(
            fill="x", padx=20, pady=(0, 5)
        )
        data_entry = ctk.CTkTextbox(dialog, width=360, height=100)
        data_entry.pack(padx=20, pady=(0, 10))

        def _save() -> None:
            title = title_entry.get()
            category = category_entry.get()
            data = data_entry.get("1.0", "end-1c")

            if title and data:
                success, msg = self._presenter.add_vault_entry(title, category, data)
                if success:
                    dialog.destroy()
                    self._refresh_entries()

        ctk.CTkButton(dialog, text="Guardar", command=_save, width=150).pack(pady=20)

    def _delete_entry(self, entry_id: str) -> None:
        self._presenter.delete_entry(entry_id)
        self._refresh_entries()

    def _on_setup_clicked(self) -> None:
        password = self.password_entry.get()
        confirm = self.confirm_entry.get()

        if password != confirm:
            self.status_label.configure(
                text="Las contraseñas no coinciden", text_color="red"
            )
            return

        success, msg = self._presenter.setup_master_password(password)
        self.status_label.configure(text=msg, text_color="green" if success else "red")

        if success:
            self.after(1000, self._show_vault_screen)

    def _on_login_clicked(self) -> None:
        password = self.password_entry.get()
        success, msg = self._presenter.verify_master_password(password)
        self.status_label.configure(text=msg, text_color="green" if success else "red")

        if success:
            self.after(500, self._show_vault_screen)

    def _on_fingerprint_click(self) -> None:
        pass

    def _on_lock_clicked(self) -> None:
        self._presenter.lock_vault()
        self._show_setup_or_login()

    def on_auth_result(self, success: bool) -> None:
        if success:
            self._show_vault_screen()
        else:
            self.status_label.configure(text="Huella no reconocida", text_color="red")

    def run(self) -> None:
        self.mainloop()
