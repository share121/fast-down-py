import fastdown


async def main():
    task = await fastdown.prefetch("https://example.com/test.zip")
    await task.start(task.info.filename())


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
