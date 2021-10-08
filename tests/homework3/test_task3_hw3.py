from homework3.task3_with_errors import make_filter

sample_data  =  [
     {
         "name": "Bill",
         "last_name": "Gilbert",
         "occupation": "was here",
         "type": "person",
     },
     {
         "is_dead": True,
         "kind": "parrot",
         "type": "bird",
         "name": "polly"
     }
]


def test_for_function_with_errors():
    assert make_filter(name='polly', type='bird').apply(sample_data) == [{'is_dead': True, 'kind': 'parrot', 'type': 'bird', 'name': 'polly'}]

