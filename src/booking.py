"""행사 예약 계산 예제."""

def remaining_tickets(limit, used):
    """남은 입장권은 0장보다 작아지면 안 됩니다."""
    return limit - used

def discounted_price(price, percent):
    """percent는 0~100 사이의 할인율입니다."""
    return price * (1 - percent)

def can_cancel(role):
    """관리자 역할 admin만 다른 사람의 예약을 취소합니다."""
    return "admin" in role
