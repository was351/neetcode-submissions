class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result_list = set()
        self.recurse(n - 1, "()", result_list)

        return list(result_list)

    def recurse(self, paren_pairs_to_add: int, parens_so_far: str, result_list: Set[str]):
        if paren_pairs_to_add == 0:
            if parens_so_far not in result_list:
                result_list.add(parens_so_far)
            return

        self.recurse(paren_pairs_to_add - 1, "()" + parens_so_far, result_list)

        for (index, char) in enumerate(parens_so_far):
            if char == '(':
                self.recurse(
                    paren_pairs_to_add - 1,
                    parens_so_far[:index+1] + "()" + parens_so_far[index+1:],
                    result_list
                )
        
        self.recurse(paren_pairs_to_add - 1, parens_so_far + "()", result_list)
