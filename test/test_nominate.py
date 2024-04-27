from unittest.mock import patch
from main import handle_nominate
from mockfirestore import MockFirestore

sample_payload = {
        "app_permissions": "442368",
        "application_id": "1233603538651713666",
        "channel": {
            "flags": 0,
            "guild_id": "767879878636339210",
            "id": "767921648224960532",
            "last_message_id": "1233640676726673439",
            "last_pin_timestamp": "2020-11-14T01:23:32.570000+00:00",
            "name": "general",
            "nsfw": False,
            "parent_id": "767879878636339211",
            "permissions": "1125899906842623",
            "position": 0,
            "rate_limit_per_user": 0,
            "topic": None,
            "type": 0,
        },
        "channel_id": "767921648224960532",
        "data": {
            "id": "1233616675837055047",
            "name": "nominate",
            "options": [{"name": "movie", "type": 3, "value": "test"}],
            "type": 1,
        },
        "entitlement_sku_ids": [],
        "entitlements": [],
        "guild": {"features": [], "id": "767879878636339210", "locale": "en-US"},
        "guild_id": "767879878636339210",
        "guild_locale": "en-US",
        "id": "1233649968812654642",
        "locale": "en-US",
        "member": {
            "avatar": None,
            "communication_disabled_until": None,
            "deaf": False,
            "flags": 0,
            "joined_at": "2020-10-19T22:40:29.595000+00:00",
            "mute": False,
            "nick": "Arnie",
            "pending": False,
            "permissions": "1125899906842623",
            "premium_since": None,
            "roles": ["767884300988186625"],
            "unusual_dm_activity_until": None,
            "user": {
                "avatar": "c6ca17624b3581983b24f6f52794f712",
                "avatar_decoration_data": None,
                "clan": None,
                "discriminator": "0",
                "global_name": "Quaznal",
                "id": "146849859905781760",
                "public_flags": 0,
                "username": "quaznal",
            },
        },
        "token": "xxx",
        "type": 2,
        "version": 1,
    }


@patch("main.get_db_client")
def test_nominate(mock_db):
	mock_db.return_value = MockFirestore()
	result = handle_nominate(sample_payload)
	assert result == "Registered nomination!"