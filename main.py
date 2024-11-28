import g4f
import asyncio
from g4f import Provider

_providers = [
    g4f.Provider.Blackbox,
    g4f.Provider.ChatGptEs
]


async def run_provider(provider: g4f.Provider.BaseProvider):
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[{"role": "user", "content": "Что такое дед инсайд?"}],
            provider=provider,
        )
        print(f"{provider.__name__}:", response)
    except Exception as e:
        print(f"{provider.__name__}:", e)


async def run_all():
    calls = [
        run_provider(provider) for provider in _providers
    ]
    await asyncio.gather(*calls)


asyncio.run(run_all())
