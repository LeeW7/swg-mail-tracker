"""
Theme configuration matching swgtracker.com
"""

# Color palette matching swgtracker.com dark theme
COLORS = {
    'bg_primary': '#0a0f0a',      # Very dark green-black background
    'bg_secondary': '#1a1f1a',    # Panel background
    'bg_tertiary': '#0f140f',     # Card/input background
    'border': '#2a3f2a',          # Border color (dark green tint)
    'accent_red': '#dc2626',      # Primary action color (buttons, tabs)
    'accent_green': '#16a34a',    # Success/start button
    'text_primary': '#ffffff',    # White text
    'text_secondary': '#9ca3af',  # Gray text
    'text_muted': '#6b7280',      # Muted/disabled text
    'success': '#22c55e',         # Success messages
    'error': '#ef4444',           # Error messages
    'info': '#3b82f6',            # Info messages
    'warning': '#f59e0b',         # Warning messages
}

# CustomTkinter theme settings
CTK_THEME = {
    "CTk": {
        "fg_color": [COLORS['bg_primary'], COLORS['bg_primary']]
    },
    "CTkFrame": {
        "fg_color": [COLORS['bg_secondary'], COLORS['bg_secondary']],
        "border_color": [COLORS['border'], COLORS['border']],
        "border_width": 1
    },
    "CTkButton": {
        "fg_color": [COLORS['accent_red'], COLORS['accent_red']],
        "hover_color": ["#b91c1c", "#b91c1c"],
        "text_color": [COLORS['text_primary'], COLORS['text_primary']],
        "border_width": 0
    },
    "CTkEntry": {
        "fg_color": [COLORS['bg_tertiary'], COLORS['bg_tertiary']],
        "border_color": [COLORS['border'], COLORS['border']],
        "text_color": [COLORS['text_primary'], COLORS['text_primary']],
        "placeholder_text_color": [COLORS['text_muted'], COLORS['text_muted']]
    },
    "CTkLabel": {
        "text_color": [COLORS['text_primary'], COLORS['text_primary']]
    },
    "CTkTextbox": {
        "fg_color": [COLORS['bg_tertiary'], COLORS['bg_tertiary']],
        "border_color": [COLORS['border'], COLORS['border']],
        "text_color": [COLORS['text_primary'], COLORS['text_primary']]
    },
    "CTkSwitch": {
        "progress_color": [COLORS['accent_green'], COLORS['accent_green']],
        "button_color": [COLORS['text_primary'], COLORS['text_primary']],
        "button_hover_color": [COLORS['text_secondary'], COLORS['text_secondary']]
    },
    "CTkTabview": {
        "fg_color": [COLORS['bg_secondary'], COLORS['bg_secondary']],
        "segmented_button_fg_color": [COLORS['bg_tertiary'], COLORS['bg_tertiary']],
        "segmented_button_selected_color": [COLORS['accent_red'], COLORS['accent_red']],
        "segmented_button_selected_hover_color": ["#b91c1c", "#b91c1c"]
    }
}

# Font settings
FONTS = {
    'title': ('Segoe UI', 16, 'bold'),
    'heading': ('Segoe UI', 14, 'bold'),
    'body': ('Segoe UI', 12),
    'small': ('Segoe UI', 10),
    'mono': ('Consolas', 11)
}
