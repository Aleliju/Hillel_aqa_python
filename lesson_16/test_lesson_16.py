from pytest import mark

from lesson_16 import TeamLead


class TestLesson16:
    @mark.parametrize("attribute", [
        'name',
        'salary',
        'department',
        'programming_language',
        'team_size'
    ])
    def test_presence_of_attribute(self, attribute):
        assert hasattr(TeamLead, attribute)
