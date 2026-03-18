from typing import Callable, Optional
import threading

from app.models.biometric_engine import BiometricEngine
from app.models.vault_manager import VaultManager, VaultEntry


class VaultPresenter:
    def __init__(self) -> None:
        self._biometric = BiometricEngine()
        self._vault = VaultManager()
        self._view: Optional[object] = None
        self._auth_method: Optional[str] = None

    def attach_view(self, view: object) -> None:
        self._view = view

    def setup_master_password(self, password: str) -> tuple[bool, str]:
        if len(password) < 6:
            return False, "La contraseña debe tener al menos 6 caracteres"
        if self._vault.setup_master(password):
            self._auth_method = "master"
            return True, "Contraseña maestra configurada"
        return False, "Error al configurar contraseña"

    def verify_master_password(self, password: str) -> tuple[bool, str]:
        if self._vault.verify_master(password):
            self._auth_method = "master"
            return True, "Acceso concedido"
        return False, "Contraseña incorrecta"

    def enroll_fingerprint(self, finger_id: int) -> tuple[bool, str]:
        return self._biometric.enroll_finger(finger_id)

    def verify_fingerprint(
        self, finger_id: int, callback: Callable[[bool], None]
    ) -> None:
        def _verify() -> None:
            result = self._biometric.verify_finger(finger_id)
            if result:
                self._auth_method = "fingerprint"
            if self._view and hasattr(self._view, "on_auth_result"):
                self._view.on_auth_result(result)

        thread = threading.Thread(target=_verify, daemon=True)
        thread.start()

    def is_authenticated(self) -> bool:
        return self._vault.is_unlocked()

    def lock_vault(self) -> None:
        self._vault.lock()
        self._auth_method = None

    def add_vault_entry(self, title: str, category: str, data: str) -> tuple[bool, str]:
        try:
            entry_id = self._vault.add_entry(title, category, data)
            return True, f"Entrada guardada (ID: {entry_id})"
        except PermissionError:
            return False, "Bóveda bloqueada"
        except Exception as e:
            return False, f"Error: {str(e)}"

    def get_entries(self) -> list[VaultEntry]:
        return self._vault.get_all_entries()

    def delete_entry(self, entry_id: str) -> tuple[bool, str]:
        if self._vault.delete_entry(entry_id):
            return True, "Entrada eliminada"
        return False, "Entrada no encontrada"

    def is_hardware_available(self) -> bool:
        return self._biometric.is_hardware_available()

    def get_enrolled_fingers(self) -> list[int]:
        return self._biometric.get_enrolled_ids()
