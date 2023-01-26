from django.test import TestCase, Client
from django.contrib.auth.models import User
from stored_xss.models import Comment, Image
from website.models import StoredXssModule
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
# Create your tests here.


class StoredXssTestCase(TestCase):
    def setUp(self):
        '''setup database for testing'''
        test_user = User.objects.create(username='testUser', password='testPassword')
        test_module = StoredXssModule.objects.create(user=test_user)

        # creating test Image object
        test_image = SimpleUploadedFile(name='image_test.jpg', 
        content=open('reflected_xss/static/reflected_xss/images/image_test.jpg', 'rb').read(), content_type='image/jpeg')
        
        Image.objects.create(image=test_image, stored_xss_module_related=test_module, description='test')
        # creating test Comment object
        Comment.objects.create(comment='Test comment', stored_xss_module_related=test_module, challenge_assigned='1')

    def test_image_exif(self):
        '''tests if Image.exif method returns correct value'''

        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_image = Image.objects.get(description='test')
        self.assertEqual(test_image.exif(), 'test_artist')

    def test_comment_str_dunder(self):
        '''tests if __str__ dunder method works correctly'''

        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_comment = Comment.objects.get(comment='Test comment')
        self.assertEqual(test_comment.__str__(), 'Test comment')
    
    def test_stored_xss_view(self):
        '''tests if stored_xss_view returns correct context'''
        client = Client()
        client.force_login(User.objects.get(username='testUser'))
        response = client.get(reverse('stored_xss'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context[-1]['module'], StoredXssModule)

    def test_stored_introduction_view(self):
        '''tests stored introduction view'''
        
        # creating client and sending requests
        client = Client()
        client.force_login(User.objects.get(username='testUser'))
        get_response = client.get(reverse('stored_xss_introduction'))
        post_response = client.post(reverse('stored_xss_introduction'))

        # if get request
        self.assertEqual(get_response.status_code, 200)

        # if post request, check if user progress has been updated
        
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        self.assertEqual(test_module.challenge_completition, 1)
        self.assertRedirects(post_response, reverse('stored_xss'), status_code=302, target_status_code=200)

    def test_stored_level1_view(self):
        '''tests stored introduction view'''
        client = Client()
        client.force_login(User.objects.get(username='testUser'))

        # if get request without proper challenge progress
        get_response = client.get(reverse('stored_xss_level1'))
        self.assertEqual(get_response.status_code, 403)

        # if get request with proper challenge progress
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_module.challenge_completition = 1
        test_module.save()
        get_response = client.get(reverse('stored_xss_level1'))
        self.assertEqual(get_response.status_code, 200)

        # if post request, check if user progress has been updated
        post_response = client.post(reverse('stored_xss_level1'))     
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        self.assertEqual(test_module.challenge_completition, 3)
        self.assertEqual(post_response.status_code, 204)
    def test_stored_level1_view(self):
        '''tests stored introduction view'''
        client = Client()
        client.force_login(User.objects.get(username='testUser'))

        # if get request without proper challenge progress
        get_response = client.get(reverse('stored_xss_level1'))
        self.assertEqual(get_response.status_code, 403)

        # if get request with proper challenge progress
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_module.challenge_completition = 1
        test_module.save()
        get_response = client.get(reverse('stored_xss_level1'))
        self.assertEqual(get_response.status_code, 200)

        # if post request, check if user progress has been updated
        post_response = client.post(reverse('stored_xss_level1'))     
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        self.assertEqual(test_module.challenge_completition, 3)
        self.assertEqual(post_response.status_code, 204)

    def test_stored_get_progress(self):
        '''tests StoredXssModule get_progress method'''
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_module.challenge_completition = 3
        test_module.save()
        self.assertEqual(test_module.get_progress(), 50)

    def test_stored_get_progress1(self):
        '''tests StoredXssModule get_progress method'''
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_module.challenge_completition = 3
        test_module.save()
        self.assertEqual(test_module.get_progress(), 50)

    def test_stored_get_progress2(self):
        '''tests StoredXssModule get_progress method'''
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_module.challenge_completition = 3
        test_module.save()
        self.assertEqual(test_module.get_progress(), 50)

    def test_stored_get_progress3(self):
        '''tests StoredXssModule get_progress method'''
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_module.challenge_completition = 3
        test_module.save()
        self.assertEqual(test_module.get_progress(), 50)

    def test_stored_get_progress4(self):
        '''tests StoredXssModule get_progress method'''
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_module.challenge_completition = 3
        test_module.save()
        self.assertEqual(test_module.get_progress(), 50)

    def test_stored_get_progress5(self):
        '''tests StoredXssModule get_progress method'''
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_module.challenge_completition = 3
        test_module.save()
        self.assertEqual(test_module.get_progress(), 50)

    def test_stored_get_progress6(self):
        '''tests StoredXssModule get_progress method'''
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_module.challenge_completition = 3
        test_module.save()
        self.assertEqual(test_module.get_progress(), 50)

    def test_stored_get_progress7(self):
        '''tests StoredXssModule get_progress method'''
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_module.challenge_completition = 3
        test_module.save()
        self.assertEqual(test_module.get_progress(), 50)

    def test_stored_get_progress8(self):
        '''tests StoredXssModule get_progress method'''
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_module.challenge_completition = 3
        test_module.save()
        self.assertEqual(test_module.get_progress(), 50)

    def test_stored_get_progress9(self):
        '''tests StoredXssModule get_progress method'''
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_module.challenge_completition = 3
        test_module.save()
        self.assertEqual(test_module.get_progress(), 50)

    def test_stored_get_progress10(self):
        '''tests StoredXssModule get_progress method'''
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_module.challenge_completition = 3
        test_module.save()
        self.assertEqual(test_module.get_progress(), 50)

    def test_stored_get_progress11(self):
        '''tests StoredXssModule get_progress method'''
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_module.challenge_completition = 3
        test_module.save()
        self.assertEqual(test_module.get_progress(), 50)

    def test_stored_get_progress12(self):
        '''tests StoredXssModule get_progress method'''
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_module.challenge_completition = 3
        test_module.save()
        self.assertEqual(test_module.get_progress(), 50)

    def test_stored_get_progress13(self):
        '''tests StoredXssModule get_progress method'''
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_module.challenge_completition = 3
        test_module.save()
        self.assertEqual(test_module.get_progress(), 50)

    def test_stored_get_progress14(self):
        '''tests StoredXssModule get_progress method'''
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_module.challenge_completition = 3
        test_module.save()
        self.assertEqual(test_module.get_progress(), 50)

    def test_stored_get_progress15(self):
        '''tests StoredXssModule get_progress method'''
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_module.challenge_completition = 3
        test_module.save()
        self.assertEqual(test_module.get_progress(), 50)

    def test_stored_get_progress16(self):
        '''tests StoredXssModule get_progress method'''
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_module.challenge_completition = 3
        test_module.save()
        self.assertEqual(test_module.get_progress(), 50)

    def test_stored_get_progress17(self):
        '''tests StoredXssModule get_progress method'''
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_module.challenge_completition = 3
        test_module.save()
        self.assertEqual(test_module.get_progress(), 50)

    def test_stored_get_progress18(self):
        '''tests StoredXssModule get_progress method'''
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_module.challenge_completition = 3
        test_module.save()
        self.assertEqual(test_module.get_progress(), 50)

    def test_stored_get_progress19(self):
        '''tests StoredXssModule get_progress method'''
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_module.challenge_completition = 3
        test_module.save()
        self.assertEqual(test_module.get_progress(), 50)

    def test_stored_get_progress20(self):
        '''tests StoredXssModule get_progress method'''
        test_user = User.objects.get(username='testUser')
        test_module = StoredXssModule.objects.get(user=test_user)
        test_module.challenge_completition = 3
        test_module.save()
        self.assertEqual(test_module.get_progress(), 50)