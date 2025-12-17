export async function runWithConcurrency<T>(
  items: readonly T[],
  limit: number,
  worker: (item: T, index: number) => Promise<void>,
): Promise<void> {
  const max = Math.max(1, Math.floor(limit));
  let nextIndex = 0;

  async function runOne(): Promise<void> {
    while (true) {
      const index = nextIndex++;
      if (index >= items.length) return;
      await worker(items[index]!, index);
    }
  }

  await Promise.all(Array.from({ length: Math.min(max, items.length) }, () => runOne()));
}
