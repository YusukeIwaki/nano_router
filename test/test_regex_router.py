import unittest
from nano_router import RegexRouter

class TestRegexRouter(unittest.TestCase):
    def setUp(self):
        router = RegexRouter()
        
        @router.Route("^(P|J)ython$")
        def good(arg):
            return "Good!", arg
        
        @router.DefaultRoute
        def bad(arg):
            return "Bad!", arg
    
        self.router = router
    
    def test_handle_route(self):
        self.assertEqual(("Good!", None), self.router.handle("Python", None))
        self.assertEqual(("Good!", (2,7,10)), self.router.handle("Jython", (2,7,10)))

    def test_handle_default_route(self):
        self.assertEqual(("Bad!", 2.5), self.router.handle("Ruby", 2.5))
        self.assertEqual(("Bad!", 3), self.router.handle("python", 3))
        self.assertEqual(("Bad!", None), self.router.handle("Python 3", None))
        self.assertEqual(("Bad!", ""), self.router.handle(("Python", ), ""))
        self.assertEqual(("Bad!", None), self.router.handle("", None))
        self.assertEqual(("Bad!", None), self.router.handle(None, None))

class TestStrangeRegexRouter(unittest.TestCase):
    def test_nonstring_route_definition_error(self):
        router = RegexRouter()
        
        with self.assertRaises(TypeError):
            @router.Route(123)
            def strange1():
                pass

        with self.assertRaises(TypeError):
            @router.Route(("hoge",))
            def strange2():
                pass
        

if __name__ == "__main__":
    unittest.main()