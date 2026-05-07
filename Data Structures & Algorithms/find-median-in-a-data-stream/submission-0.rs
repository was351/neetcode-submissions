use std::collections::BinaryHeap;
use core::cmp::Reverse;

struct MedianFinder {
    min_heap: BinaryHeap<Reverse<i32>>,
    max_heap: BinaryHeap<i32>,
}

impl MedianFinder {
    pub fn new() -> Self {
        Self {
            min_heap: BinaryHeap::new(),
            max_heap: BinaryHeap::new()
        }
    }

    pub fn add_num(&mut self, num: i32) {
        if let Some(&Reverse(min_val)) = self.min_heap.peek()
            && num >= min_val {
            self.min_heap.push(Reverse(num));

            if self.min_heap.len() - 1 > self.max_heap.len() {
                self.max_heap.push(self.min_heap.pop().unwrap().0);
            }
        } else {
            self.max_heap.push(num);

            if self.max_heap.len() - 1 > self.min_heap.len() {
                self.min_heap.push(Reverse(self.max_heap.pop().unwrap()));
            }
        }
    }

    /// Invariants:
    ///  - `(min_len - max_len).abs() <= 1`
    ///  - `min_len.max(max_len) >= 1`
    pub fn find_median(&self) -> f64 {
        let min_len = self.min_heap.len();
        let max_len = self.max_heap.len();

        if min_len < max_len {
            *self.max_heap
                .peek()
                .unwrap() as f64
        } else if max_len < min_len {
            self.min_heap
                .peek()
                .unwrap().0 as f64
        } else {
            (*self.max_heap
                .peek()
                .unwrap() as f64)
                .midpoint(self.min_heap.peek().unwrap().0 as f64)
        }
    }
}
