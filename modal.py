diction = {
    "type": "modal",
    "callback_id": "hello-modal",
    "title": {

        "type": "plain_text",
        "text": "Input Data",
        "emoji": True
    },
    "submit": {
        "type": "plain_text",
        "text": "Submit",
        "emoji": True
    },
    "close": {
        "type": "plain_text",
        "text": "Cancel",
        "emoji": True
    },
    "blocks": [
        {
            "type": "input",
            "block_id": "block1",
            "element": {
                "type": "plain_text_input",
                "action_id": "input1",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Text"
                }
            },
            "label": {
                "type": "plain_text",
                "text": "Title"
            },
            "hint": {
                "type": "plain_text",
                "text": "HINT-Show's Title"
            }
        },
        {
            "type": "input",
            "block_id": "block2",
            "element": {
                "type": "plain_text_input",
                "action_id": "input2",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Text"
                }
            },
            "label": {
                "type": "plain_text",
                "text": "Genre"
            },
            "hint": {
                "type": "plain_text",
                "text": "HINT-SciFi,fantasy"
            }
        },
        {
            "type": "input",
            "block_id": "block3",
            "element": {
                "type": "plain_text_input",
                "action_id": "input3",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Text"
                }
            },
            "label": {
                "type": "plain_text",
                "text": "Premiere"
            },
            "hint": {
                "type": "plain_text",
                "text": "HINT-Month date, year"
            }
        },
        {
            "type": "input",
            "block_id": "block4",
            "element": {
                "type": "plain_text_input",
                "action_id": "input4",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Text"
                }
            },
            "label": {
                "type": "plain_text",
                "text": "Seasons"
            },
            "hint": {
                "type": "plain_text",
                "text": "HINT-X seasons, Y episodes"
            }
        },
        {
            "type": "input",
            "block_id": "block5",
            "element": {
                "type": "plain_text_input",
                "action_id": "input5",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Text"
                }
            },
            "label": {
                "type": "plain_text",
                "text": "Runtime"
            },
            "hint": {
                "type": "plain_text",
                "text": "HINT-X-Y min"
            }
        },
        {
            "type": "input",
            "block_id": "block6",
            "element": {
                "type": "plain_text_input",
                "action_id": "input6",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Text"
                }
            },
            "label": {
                "type": "plain_text",
                "text": "Status"
            },
            "hint": {
                "type": "plain_text",
                "text": "HINT-Pending or Renewed"
            }
        }
    ],

}
