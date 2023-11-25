from django.test import TestCase
from .models import Project, MindMapField

# Create your tests here.
class ProjectTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.model_test_cases = {
            'normal_sentence_form_test': Project.objects.create(name='Aincrad', text='Brainstorm'),
            'normal_newline_form_text': Project.objects.create(name='Hogwarts Fanfiction', text='Brainstorm with phrases/sentences separated by new lines'),
            'normal_bulletpoint_form_text': Project.objects.create(name='My next short programming project', text='Brainstorm with phrases/sentences separated by bullet points (dashes, special character markers, etc.)'),
            'no_name_test': Project.objects.create(name='', text='Brainstorm'),
            'nonsense_test': Project.objects.create(name='JAjdncincO*U0923u', text='pawirfh9 q8c39q8w hdhv uuag974q 807yf 87yfr qy48 7yf0q847y9843t68974y 08q74yt8q7yc08q7rf 8rt 9q43y08 iufh 47 8743yt fgy q37 y0378yg eufhv8q74 yt87g iufgh 983yg 087rygqeh 3487 5gh8fdfuhv7es y4h g80y 58308rhg 0587058 ghisdfjhgosiu ghsdif higudf dfhgo sidf 90wg if bowuert08u'),
            'small_text_test': Project.objects.create(name='Jump mechanics in my new video game', text='Brainstorm with less that 15 unique ideas'),
            'no_text_test': ('My story\'s magic system', ''),
            'empty_test': ('', ''),
        }
    
    def test_create_model_success(self):
        success = ['normal_sentence_form_test', 'normal_newline_form_text', 'normal_bulletpoint_form_text', 'no_name_test']
        for test in success:
            self.assertNotEqual(self.model_test_cases[test].mind_map, 'Unable to create mind map')
