import asyncio
import os
from openai import OpenAI
from env.environment import SupportEnv
from env.models import Action

API_KEY = os.getenv("HF_TOKEN")
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")

client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)

async def run_task(task_name):
    env = SupportEnv()
    result = await env.reset(task_name)

    print(f"[START] task={task_name} env=support-env model={MODEL_NAME}")

    rewards = []
    steps = 0

    for step in range(1, 6):
        prompt = f"Customer Ticket: {result.observation.ticket}\nWhat should agent do?"

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )

        action_text = response.choices[0].message.content.strip()

        action = Action(action_type="respond", content=action_text)

        result = await env.step(action)

        reward = result.reward
        done = result.done

        rewards.append(reward)
        steps = step

        print(f"[STEP] step={step} action={action_text} reward={reward:.2f} done={str(done).lower()} error=null")

        if done:
            break

    score = sum(rewards) / len(rewards) if rewards else 0.0
    score = min(max(score, 0.0), 1.0)
    success = score >= 0.5

    rewards_str = ",".join(f"{r:.2f}" for r in rewards)

    print(f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}")

async def main():
    for task in ["easy", "medium", "hard"]:
        await run_task(task)

if __name__ == "__main__":
    asyncio.run(main())