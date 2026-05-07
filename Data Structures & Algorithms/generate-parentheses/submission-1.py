class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        variation_list = set()
        result_list = []
        self.recurse(n - 1, "()", variation_list, result_list)

        return result_list

    def recurse(self, paren_pairs_to_add: int, parens_so_far: str, variations_seen: Set[str], result_list: List[str]):
        if parens_so_far in variations_seen:
            return
        variations_seen.add(parens_so_far)

        if paren_pairs_to_add == 0:
            result_list.append(parens_so_far)
            return

        self.recurse(paren_pairs_to_add - 1, "()" + parens_so_far, variations_seen, result_list)

        for (index, char) in enumerate(parens_so_far):
            if char == '(':
                self.recurse(
                    paren_pairs_to_add - 1,
                    parens_so_far[:index+1] + "()" + parens_so_far[index+1:],
                    variations_seen, 
                    result_list
                )
        
        self.recurse(paren_pairs_to_add - 1, parens_so_far + "()", variations_seen, result_list)
