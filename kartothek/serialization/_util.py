# -*- coding: utf-8 -*-


def _check_contains_null(val):
    if isinstance(val, bytes):
        for byte in val:
            compare_to = chr(0) if isinstance(byte, bytes) else 0
            if byte == compare_to:
                return True
    return False


def ensure_unicode_string_type(obj):
    """
    ensures obj is a of native string type:
    """
    return obj.decode("utf8") if isinstance(obj, bytes) else str(obj)
