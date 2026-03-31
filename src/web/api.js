/**
 * Simple API client with retry logic.
 */

const DEFAULT_TIMEOUT = 5000;
const MAX_RETRIES = 3;

async function fetchWithRetry(url, options = {}, retries = MAX_RETRIES) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), options.timeout || DEFAULT_TIMEOUT);

  try {
    const response = await fetch(url, {
      ...options,
      signal: controller.signal,
    });

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    return await response.json();
  } catch (error) {
    if (retries > 0 && error.name !== "AbortError") {
      const delay = (MAX_RETRIES - retries + 1) * 1000;
      await new Promise((resolve) => setTimeout(resolve, delay));
      return fetchWithRetry(url, options, retries - 1);
    }
    throw error;
  } finally {
    clearTimeout(timeout);
  }
}

module.exports = { fetchWithRetry, DEFAULT_TIMEOUT, MAX_RETRIES };
