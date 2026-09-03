def fibonacci(n):
    # 1. معالجة الحالات الخاصة (Edge Cases)
    # إذا كان المدخل ليس رقماً صحيحاً
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    
    # إذا كان الرقم سالباً (لا توجد رتبة سالبة في فيبوناتشي)
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
        
    # 2. الحالات الأساسية للسلسلة (Base Cases)
    if n == 0:
        return 0
    if n == 1:
        return 1
        
    # 3. الحساب الفعلي بطريقة فعالة وموفرة للذاكرة (Iterative Approach)
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
