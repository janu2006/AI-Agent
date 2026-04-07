from env.models import Observation, Action, StepResult
from env.tasks import TASKS
from env.graders import compute_reward

class SupportEnv:

    def __init__(self):
        self.task_name = None
        self.task = None
        self.step_count = 0
        self.done = False
        self.history = []

    async def reset(self, task_name="easy"):
        self.task_name = task_name
        self.task = TASKS[task_name]
        self.step_count = 0
        self.done = False
        self.history = []

        return StepResult(
            observation=self._get_obs(),
            reward=0.0,
            done=False,
            info={}
        )

    def state(self):
        return {
            "task": self.task_name,
            "step": self.step_count,
            "history": self.history
        }

    async def step(self, action: Action):
        if self.done:
            return StepResult(
                observation=self._get_obs(),
                reward=0.0,
                done=True,
                info={"error": "Episode finished"}
            )

        self.step_count += 1

        reward = compute_reward(action, self.task["expected"], self.step_count)

        self.history.append({
            "action": action.dict(),
            "reward": reward
        })

        if reward > 0.8 or self.step_count >= 5:
            self.done = True

        return StepResult(
            observation=self._get_obs(),
            reward=reward,
            done=self.done,
            info={}
        )

    def _get_obs(self):
        return Observation(
            ticket=self.task["ticket"],
            conversation_history=self.history,
            status="closed" if self.done else "open"
        )