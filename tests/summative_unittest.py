import unittest
from summative_users_parents_class import Agents
from summative_students_child_class import Students


class testAgents(unittest.TestCase):

    def testviewHouseByAgent(self):
        agent = Students()
        self.assertEqual(agent.get_house(10), 1)

    # def testRemoveHouse(self):
    #     agent = Agents()
    #     self.assertEqual(agent.remove_house(10, 201), True)

    def testUpdateHouse(self):
        agent = Agents()
        self.assertEqual(agent.update_house(10, 200), True)

    def testCheckingAgentInfo(self):
        agent = Agents()
        self.assertTrue(agent.get_User_Info(1000))

    def testCheckingStudentInfo(self):
        agent = Students()
        self.assertEqual(agent.get_User_Info(40), 1)


if __name__ == "__main__":
    unittest.main()
