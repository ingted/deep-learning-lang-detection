angular.module('app', ['ngRoute'])
    .factory('sessionFactory', sessionFactory)
    .service('userService', userService)
    .service('todoService', todoService)
    .service('teamService', teamService)
    .service('playerService', playerService)
    .controller('mainController', mainController)
    .controller('navbarController', navbarController)
    .controller('loginController', loginController)
    .controller('createController', createController)
    .controller('listTeamController', listTeamController)
    .config(routes)
    .run(loginStatus);
