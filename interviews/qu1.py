"""
LFU Cache (LeetCode 460, Hard)
# Market Data Subscription Cache


Thousands of traders, pricing engines, and risk systems continuously request reference information about financial instruments (tick size, exchange, currency, settlement rules, etc.).

Fetching this metadata from the central database is expensive, so we want to implement an in-memory cache.

However: Memory is limited.
- Frequently accessed instruments should remain in memory.
- Instruments that are no longer actively traded should eventually be removed.
- During volatile markets, many instruments may be requested repeatedly in short bursts.

To maximize cache efficiency, the system should prefer keeping instruments that are used often over those that are rarely used.
If two instruments have been requested the same number of times, the one that has not been accessed for the longest time should be removed first.


APIS:
InstrumentCache(int capacity)

InstrumentInfo* getInstrument(InstrumentId id)
- Returns the cached instrument information if it exists, else Null

void updateInstrument(InstrumentId id, InstrumentInfo info)
- Inserts a new instrument into the cache.
- If the instrument already exists, update its information.
- If over capacity, evict one instrument


Eviction:
- Remove the instrument that has been accessed the fewest number of times.
- If multiple instruments have the same access count, remove the one that has gone the longest without being accessed.

"""



"""

questions
- Every successful lookup counts as a use of that instrument.
- Updating an existing instrument also counts as a use.

Constraints
getInstrument() must run in O(1) average time.
updateInstrument() must also run in O(1) average time.
Capacity is fixed at construction.

"""

# ======================================================================
# 
# ======================================================================
- LFU identified
- recency as tie breaker

LRU immediately identified strategy
- doubly linked list
- heap


which of two api functions is called more?

data types of inputs/outputs

added attributes
pseudo code for each api => incl time complexity


30 MINUTES

__ important:
- made assumption: Every successful lookup counts as a use of that instrument.
- made assumption: Updating an existing instrument also counts as a use.



# ======================================================================

from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        
        # key -> value
        self.key_map = {}
        # key -> current frequency
        self.key_freq = {}
        # freq -> OrderedDict(key -> True) to maintain LRU order per frequency
        self.freq_map = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        
        self._touch(key)
        return self.key_map[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.key_map:
            self.key_map[key] = value
            self._touch(key)
            return

        # Evict LFU (tie-break with LRU) if capacity is reached
        if len(self.key_map) >= self.capacity:
            # popitem(last=False) pops in FIFO order (the least recently used)
            evict_key, _ = self.freq_map[self.min_freq].popitem(last=False)
            del self.key_map[evict_key]
            del self.key_freq[evict_key]
            
            # Clean up the freq list if empty
            if not self.freq_map[self.min_freq]:
                del self.freq_map[self.min_freq]

        # Insert new key
        self.key_map[key] = value
        self.key_freq[key] = 1
        self.freq_map[1][key] = True
        self.min_freq = 1

    def _touch(self, key: int) -> None:
        """Helper method to increment frequency and reorder tracking structures."""
        freq = self.key_freq[key]
        new_freq = freq + 1
        
        # Remove from old frequency mapping
        del self.freq_map[freq][key]
        if not self.freq_map[freq]:
            del self.freq_map[freq]
            # Update min_freq if the emptied frequency list was the lowest
            if self.min_freq == freq:
                self.min_freq += 1
                
        # Update maps to reflect new frequency
        self.key_freq[key] = new_freq
        self.freq_map[new_freq][key] = True


# ======================================================================
# 
# ======================================================================