def telegram_safety_text(text):
	chars = ('*', '_', '`')
	for char in chars:
		if text.count(char) % 2 != 0:
			text = text.replace(char, f'\{char}', 1)

	return text