from tastypie.api import Api

from .api import TagResource, TopicCategoryResource, ProfileResource, \
    GroupResource, RegionResource
from .resourcebase_api import LayerResource, MapResource, DocumentResource, \
    ResourceBaseResource, FeaturedResourceBaseResource, \
    LatestDocumentResource, LatestDocumentHazardResource

api = Api(api_name='api')

api.register(LayerResource())
api.register(MapResource())
api.register(DocumentResource())
api.register(ProfileResource())
api.register(ResourceBaseResource())
api.register(TagResource())
api.register(RegionResource())
api.register(TopicCategoryResource())
api.register(GroupResource())
api.register(FeaturedResourceBaseResource())

# added
api.register(LatestDocumentResource())
api.register(LatestDocumentHazardResource())
