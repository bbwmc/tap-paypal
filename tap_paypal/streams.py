"""Streams metadata."""
# -*- coding: utf-8 -*-
from types import MappingProxyType

# Streams metadata
STREAMS: MappingProxyType = MappingProxyType({
    'paypal_transactions': {
        # Only include scalar keys so Singer targets can hash primary keys
        'key_properties': ['transaction_id'],
        'replication_method': 'INCREMENTAL',
        'replication_key': 'transaction_info.transaction_updated_date',
        'bookmark': 'start_date',
    },
})
