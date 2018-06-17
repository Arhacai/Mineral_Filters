from django.core.urlresolvers import reverse
from django.test import TestCase

from minerals.views import rand_mineral
from .models import Mineral



class MineralModelTest(TestCase):
    def test_mineral_creation(self):
        mineral = Mineral.objects.create(
            name="Testcyte"
        )
        self.assertIn(mineral, Mineral.objects.all())
        self.assertEqual(str(mineral), "Testcyte")


class MineralCatalogViewsTest(TestCase):
    def test_redirect_to_mineral_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/index.html')


class MineralViewsTest(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name="Abescyte",
            group='Sulfides',
            color='White'
        )

    def test_rand_mineral(self):
        result = rand_mineral()
        self.assertIsInstance(result, int)
        self.assertLess(result, Mineral.objects.all().count())

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/index.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail', kwargs={
            'pk': self.mineral.pk
        }))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral.name, resp.context['header']['name'])
        self.assertTemplateUsed(resp, 'minerals/detail.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_list_letter_filter_view(self):
        resp = self.client.get(reverse('minerals:letter_filter', kwargs={'letter': 'A'}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/index.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_list_group_filter_view(self):
        resp = self.client.get(reverse('minerals:group_filter', kwargs={'group': 'Sulfides'}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/index.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_list_color_filter_view(self):
        resp = self.client.get(reverse('minerals:color_filter', kwargs={'color': 'White'}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/index.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_list_other_color_filter_view(self):
        resp = self.client.get(reverse('minerals:color_filter', kwargs={'color': 'Other'}))
        self.assertEqual(resp.status_code, 200)
        self.assertNotIn(self.mineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/index.html')

