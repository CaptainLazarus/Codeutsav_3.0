from rest_framework import routers
from .api import StartupsViewSet,InvestorsViewSet,MentorsViewSet,ProgressViewSet,supViewSet,sumViewSet,InvestedViewSet,SpaceViewSet

router = routers.DefaultRouter()
router.register('api/startups', StartupsViewSet, 'Startups')
router.register('api/investors', InvestorsViewSet, 'Investors')
router.register('api/mentors', MentorsViewSet, 'Mentors')
router.register('api/progress', ProgressViewSet, 'progress')
router.register('api/sup', supViewSet, 'sup')
router.register('api/sum', sumViewSet, 'sum')
router.register('api/invested', InvestedViewSet, 'invested')
router.register('api/offices', SpaceViewSet, 'offices')

ProgressViewSet,supViewSet,sumViewSet,InvestedViewSet,SpaceViewSet

urlpatterns = router.urls