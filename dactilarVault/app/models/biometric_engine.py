from typing import Optional
from dataclasses import dataclass
import hashlib
import time


@dataclass
class FingerprintRecord:
    finger_id: int
    template_hash: str
    created_at: float


class BiometricEngine:
    def __init__(self) -> None:
        self._enrolled_fingers: dict[int, FingerprintRecord] = {}
        self._last_scan_result: Optional[bool] = None
        self._is_scanning = False

    def is_hardware_available(self) -> bool:
        return False

    def enroll_finger(self, finger_id: int) -> tuple[bool, str]:
        if finger_id in self._enrolled_fingers:
            return False, "Huella ya registrada"

        template_data = f"finger_{finger_id}_{time.time()}".encode()
        template_hash = hashlib.sha256(template_data).hexdigest()

        record = FingerprintRecord(
            finger_id=finger_id,
            template_hash=template_hash,
            created_at=time.time(),
        )
        self._enrolled_fingers[finger_id] = record
        return True, "Huella enrollada exitosamente"

    def verify_finger(self, finger_id: int) -> bool:
        self._is_scanning = True
        time.sleep(0.5)
        self._is_scanning = False

        if finger_id in self._enrolled_fingers:
            self._last_scan_result = True
            return True
        self._last_scan_result = False
        return False

    def delete_finger(self, finger_id: int) -> bool:
        if finger_id in self._enrolled_fingers:
            del self._enrolled_fingers[finger_id]
            return True
        return False

    def get_enrolled_count(self) -> int:
        return len(self._enrolled_fingers)

    def get_enrolled_ids(self) -> list[int]:
        return list(self._enrolled_fingers.keys())
