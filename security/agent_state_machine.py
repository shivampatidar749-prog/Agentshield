# security/agent_state_machine.py

class AgentStateMachine:

    def __init__(self, goal):
        self.goal = goal
        self.state = "INITIAL"
        self.action_plan = None
        self.history = []

    def transition(self, new_state):
        self.history.append((self.state, new_state))
        self.state = new_state

    def perceive(self, parsed_dom):
        self.transition("PERCEIVE")
        self.dom = parsed_dom

    def plan(self, planner_function):
        self.transition("PLAN")
        self.action_plan = planner_function(self.dom, self.goal)
        return self.action_plan

    def validate(self):
        self.transition("VALIDATE")

    def execute(self):
        self.transition("EXECUTE")

    def terminate(self):
        self.transition("TERMINATE")
