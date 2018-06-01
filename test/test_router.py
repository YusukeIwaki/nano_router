import unittest
from nano_router import Router

class TestRouterWithDefaultRoute(unittest.TestCase):
    def setUp(self):
        router = Router()
        
        @router.Route("Python")
        def good(arg):
            return "Good!", arg
        
        @router.DefaultRoute
        def bad(arg):
            return "Bad!", arg
    
        self.router = router
    
    def test_handle_route(self):
        self.assertEqual(("Good!", None), self.router.handle("Python", None))
        self.assertEqual(("Good!", (2,7,10)), self.router.handle("Python", (2,7,10)))

    def test_handle_default_route(self):
        self.assertEqual(("Bad!", 2.5), self.router.handle("Ruby", 2.5))
        self.assertEqual(("Bad!", 3), self.router.handle("python", 3))
        self.assertEqual(("Bad!", None), self.router.handle("Python3", None))
        self.assertEqual(("Bad!", ""), self.router.handle(("Python", ), ""))
        self.assertEqual(("Bad!", None), self.router.handle("", None))
        self.assertEqual(("Bad!", None), self.router.handle(None, None))

class TestRouterWithoutDefaultRoute(unittest.TestCase):
    def setUp(self):
        router = Router()
        
        @router.Route("Python")
        def good(arg):
            return "Good!", arg

        self.router = router
    
    def test_handle_route(self):
        self.assertEqual(("Good!", None), self.router.handle("Python", None))
        self.assertEqual(("Good!", (2,7,10)), self.router.handle("Python", (2,7,10)))

    def test_handle_unknown_route(self):
        self.assertEqual(None, self.router.handle("Ruby", 2.5))
        self.assertEqual(None, self.router.handle("python", 3))
        self.assertEqual(None, self.router.handle("Python3", None))
        self.assertEqual(None, self.router.handle(("Python", ), ""))
        self.assertEqual(None, self.router.handle("", None))
        self.assertEqual(None, self.router.handle(None, None))

if __name__ == "__main__":
    unittest.main()