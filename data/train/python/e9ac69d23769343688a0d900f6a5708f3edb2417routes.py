urls = (
    '/', 'app.controller.site.IndexAction',
    '/tweet/*', 'app.controller.post.PostAction',
    '/repost/([0-9]+)/?', 'app.controller.post.RePostAction',
    '/signup/?', 'app.controller.site.SignUpAction',
    '/signin/?', 'app.controller.site.SignInAction',
    '/signout/?', 'app.controller.site.SignOutAction',
    '/topic/?', 'app.controller.topic.ListAction',
    '/topic/([^#]+)/?', 'app.controller.topic.ViewAction',
    '/@([\w]+)/?', 'app.controller.profile.ViewAction',
    '/follow/([\w]+)/?', 'app.controller.follow.FollowAction',
    '/unfollow/([\w]+)/?', 'app.controller.follow.UnFollowAction',
    '/@([\w]+)/following', 'app.controller.follow.FollowingAction',
    '/@([\w]+)/follower', 'app.controller.follow.FollowerAction',
    '/test/?', 'app.controller.site.TestAction',
    '/post/([0-9]+)/?', 'app.controller.post.ReadUpdateAction',
    '/post/delete/([0-9]+)/?', 'app.controller.post.DeleteAction',
    '/post/?', 'app.controller.post.ListCreateAction',
)
