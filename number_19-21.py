# 847

# def f(s, m):
#     if s >= 34:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#     h = [f(s + 1, m - 1), f(s + 2, m - 1), f(s + 3, m - 1), f(s * 2, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
#
# print('19)', [s for s in range(1, 34) if f(s, 2)])
# print('20)', [s for s in range(1, 34) if not f(s, 1) and f(s, 3)])
# print('21)', [s for s in range(1, 34) if not f(s, 2) and f(s, 4)])


# 845

# def f(s, m):
#     if 36 <= s <= 60:
#         return m % 2 == 0
#     if s > 60:
#         return m % 2 != 0
#     if m == 0:
#         return 0
#     h = [f(s + 1, m - 1), f(s * 2, m - 1), f(s * 3, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
#
# print('19)', [s for s in range(1, 36) if f(s, 2)])
# print('20)', [s for s in range(1, 36) if not f(s, 1) and f(s, 3)])
# print('21)', [s for s in range(1, 36) if not f(s, 2) and f(s, 4)])


# 1202

# def f(a, b, m):
#     if a + b >= 59:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#     h = [f(a + 1, b, m - 1), f(a * 2, b, m - 1), f(a, b + 1, m - 1), f(a, b * 2, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
#
# print('19)', [s for s in range(2, 53) if f(5, s, 1)])
# print('20)', [s for s in range(2, 53) if not f(5, s, 1) and f(5, s, 3)])
# print('21)', [s for s in range(2, 53) if not f(5, s, 2) and f(5, s, 4)])


# 853

# def f(a, b, m):
#     if a + b >= 77:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#     h = [f(a + 1, b, m - 1), f(a * 2, b, m - 1), f(a, b + 1, m - 1), f(a, b * 2, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
#
# print('19)', [s for s in range(1, 70) if f(7, s, 2)])  # all --> any
# print('20)', [s for s in range(1, 70) if not f(7, s, 1) and f(7, s, 3)])
# print('21)', [s for s in range(1, 70) if not f(7, s, 2) and f(7, s, 4)])


# 1135

# def f(a, b, m):
#     if a + b >= 68:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#     h = [f(a + 1, b, m - 1), f(a + b, b, m - 1), f(a, b + 1, m - 1), f(a, b + a, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
#
# print('19)', [s for s in range(1, 60) if f(8, s, 2)])  # all --> any
# print('20)', [s for s in range(1, 60) if not f(8, s, 1) and f(8, s, 3)])
# print('21)', [s for s in range(1, 60) if not f(8, s, 2) and f(8, s, 4)])


# 1420

# def f(a, b, m):
#     if a * b >= 63:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#     h = [f(a + 1, b, m - 1), f(a * 2, b, m - 1), f(a, b + 1, m - 1), f(a, b * 2, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
#
# print('19)', [s for s in range(1, 32) if not f(2, s, 1) and f(2, s, 2)])
# print('20)', [s for s in range(1, 32) if not f(2, s, 1) and f(2, s, 3)])
# print('21)', [s for s in range(1, 32) if not f(2, s, 2) and f(2, s, 4)])


# 2369

# def f(a, b, c, m):
#     if a + b + c >= 73:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#     h = [
#         f(a + 3, b, c, m - 1), f(a + 13, b, c, m - 1), f(a + 23, b, c, m - 1),
#         f(a, b + 3, c, m - 1), f(a, b + 13, c, m - 1), f(a, b + 23, c, m - 1),
#         f(a, b, c + 3, m - 1), f(a, b, c + 13, m - 1), f(a, b, c + 23, m - 1)
#     ]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
#
# print('19)', [s for s in range(1, 24) if f(2, s, 2*s, 2)])  # all --> any
# print('20)', [s for s in range(1, 24) if not f(2, s, 2*s, 1) and f(2, s, s*2, 3)])
# print('21)', [s for s in range(1, 24) if not f(2, s, 2*s, 2) and f(2, s, 2*s, 4)])


# 843

# def f(a, b, m):
#     if a + b <= 20:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#     h = [f(a - 1, b, m - 1), f((a + 1) // 2, b, m - 1), f(a, b - 1, m - 1), f(a, (b + 1) // 2, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
#
# print('19)', [s for s in range(11, 30) if f(10, s, 2)])
# print('20)', [s for s in range(11, 3000) if not f(10, s, 1) and f(10, s, 3)])
# print('21)', [s for s in range(11, 3000) if not f(10, s, 2) and f(10, s, 4)])


# 2370

# def f(s, m):
#     if s >= 2163:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#     h = [f(s + 1, m - 1), f(s * 3, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
#
# print('19)', [s for s in range(1, 2163) if not f(s, 1) and f(s, 2)])
# print('20)', [s for s in range(1, 2163) if not f(s, 1) and f(s, 3)])
# print('21)', [s for s in range(1, 2163) if not f(s, 2) and f(s, 4)])


