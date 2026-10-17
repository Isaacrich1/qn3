students = []
seen_regs = set()
 
def add_student(reg, name, cw, exam):
    if reg in seen_regs:
        return False, 'Duplicate registration number'
    try:
        cw = float(cw)
        exam = float(exam)
    except (TypeError, ValueError):
        return False, 'Marks must be numeric'
    if not (0 <= cw <= 100) or not (0 <= exam <= 100):
        return False, 'Marks must be between 0 and 100'
    final = cw * 0.40 + exam * 0.60
    classification = classify(final)
    students.append({
        'reg': reg,
        'name': name,
        'cw': cw,
        'exam': exam,
        'final': final,
        'class': classification
    })
    seen_regs.add(reg)
    return True, 'Accepted'
