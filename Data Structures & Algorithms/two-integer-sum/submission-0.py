class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Создаем словарь для хранения значений и их индексов
        num_map = {}
        
        # Проходим по массиву
        for i, num in enumerate(nums):
            # Вычисляем число, которое нам нужно
            complement = target - num
            
            # Если такое число уже есть в словаре, возвращаем индексы
            if complement in num_map:
                return [num_map[complement], i]
            
            # Сохраняем текущее число и его индекс
            num_map[num] = i
        
        # По условию задачи решение всегда существует,
        # но на всякий случай возвращаем пустой список
        return []