class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        hashmap = {r : ingredients[i] for i, r in enumerate(recipes)}
        cycle , ans , prepared = set() , [] , set()
        def dfs(recipe):
            if recipe in cycle:
                return False
            if recipe in prepared:
                return True
            if recipe not in hashmap:
                return False
            cycle.add(recipe)
            for i in hashmap[recipe]:
                if i not in supplies:
                    if dfs(i) == False:
                        return False
            prepared.add(recipe)
            #ans.append(recipe)
            cycle.remove(recipe)
            return True
        for food in recipes:
            if dfs(food) == True:
                ans.append(food)
        return ans