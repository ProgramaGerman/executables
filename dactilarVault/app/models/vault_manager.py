from typing import Optional
from dataclasses import dataclass, field
import json
import hashlib
import base64
import time
from pathlib import Path


@dataclass
class VaultEntry:
    entry_id: str
    title: str
    category: str
    encrypted_data: str
    created_at: float
    modified_at: float


@dataclass
class VaultData:
    entries: dict[str, VaultEntry] = field(default_factory=dict)


class VaultManager:
    def __init__(self, vault_path: Optional[Path] = None) -> None:
        self._vault_path = vault_path or Path("vault.dat")
        self._master_key_hash: Optional[str] = None
        self._is_unlocked = False
        self._vault_data = VaultData()
        self._load_vault()

    def _load_vault(self) -> None:
        if self._vault_path.exists():
            try:
                with open(self._vault_path, "r") as f:
                    data = json.load(f)
                    self._vault_data = VaultData(
                        entries={
                            k: VaultEntry(**v)
                            for k, v in data.get("entries", {}).items()
                        }
                    )
                    self._master_key_hash = data.get("master_key_hash")
            except (json.JSONDecodeError, TypeError):
                pass

    def _save_vault(self) -> None:
        if self._vault_path.exists():
            self._vault_path.unlink()
        with open(self._vault_path, "w") as f:
            json.dump(
                {
                    "master_key_hash": self._master_key_hash,
                    "entries": {
                        k: vars(v) for k, v in self._vault_data.entries.items()
                    },
                },
                f,
                indent=2,
            )

    def setup_master(self, master_password: str) -> bool:
        self._master_key_hash = hashlib.sha256(master_password.encode()).hexdigest()
        self._is_unlocked = True
        self._save_vault()
        return True

    def verify_master(self, master_password: str) -> bool:
        if not self._master_key_hash:
            return False
        provided_hash = hashlib.sha256(master_password.encode()).hexdigest()
        if provided_hash == self._master_key_hash:
            self._is_unlocked = True
            return True
        return False

    def lock(self) -> None:
        self._is_unlocked = False

    def is_unlocked(self) -> bool:
        return self._is_unlocked

    def has_master_password(self) -> bool:
        return self._master_key_hash is not None

    def add_entry(self, title: str, category: str, data: str) -> str:
        if not self._is_unlocked:
            raise PermissionError("Bóveda bloqueada")

        entry_id = hashlib.md5(f"{title}{time.time()}".encode()).hexdigest()[:8]
        encrypted = self._encrypt_data(data)

        entry = VaultEntry(
            entry_id=entry_id,
            title=title,
            category=category,
            encrypted_data=encrypted,
            created_at=time.time(),
            modified_at=time.time(),
        )
        self._vault_data.entries[entry_id] = entry
        self._save_vault()
        return entry_id

    def get_entry(self, entry_id: str) -> Optional[VaultEntry]:
        if not self._is_unlocked:
            return None
        return self._vault_data.entries.get(entry_id)

    def get_all_entries(self) -> list[VaultEntry]:
        if not self._is_unlocked:
            return []
        return list(self._vault_data.entries.values())

    def delete_entry(self, entry_id: str) -> bool:
        if entry_id in self._vault_data.entries:
            del self._vault_data.entries[entry_id]
            self._save_vault()
            return True
        return False

    def _encrypt_data(self, data: str) -> str:
        return base64.b64encode(data.encode()).decode()
