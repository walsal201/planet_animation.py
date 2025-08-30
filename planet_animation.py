import streamlit as st
from streamlit.components.v1 import html

canvas_html = """
<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      margin: 0;
      overflow: hidden;
      background: radial-gradient(circle at center, #000010, #000000);
      font-family: 'Segoe UI', sans-serif;
    }
    canvas {
      display: block;
      position: absolute;
      top: 0;
      left: 0;
      z-index: 0;
    }
    .overlay {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      z-index: 1;
      text-align: center;
      font-size: 3em;
      font-style: italic;
      font-weight: bold;
      animation: colorShift 6s infinite alternate ease-in-out, pulse 4s infinite, seesaw 3s infinite ease-in-out;
    }
    @keyframes colorShift {
      0%   { color: #ff00ff; text-shadow: 0 0 20px #ff00ff; }
      25%  { color: #00ffff; text-shadow: 0 0 20px #00ffff; }
      50%  { color: #ffff00; text-shadow: 0 0 20px #ffff00; }
      75%  { color: #ff6600; text-shadow: 0 0 20px #ff6600; }
      100% { color: #00ff00; text-shadow: 0 0 20px #00ff00; }
    }
    @keyframes pulse {
      0%, 100% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
      50%      { transform: translate(-50%, -50%) scale(1.05); opacity: 0.8; }
    }
    @keyframes seesaw {
      0%   { transform: translate(-50%, -50%) rotate(-2deg); }
      50%  { transform: translate(-50%, -50%) rotate(2deg); }
      100% { transform: translate(-50%, -50%) rotate(-2deg); }
    }
  </style>
</head>
<body>
  <div class="overlay">Welcome to Walid Sphere 🌌</div>
  <canvas id="canvas"></canvas>
  <script>
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    window.addEventListener('resize', () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    });

    let centerX = canvas.width / 2;
    let centerY = canvas.height / 2;
    let radius = Math.min(canvas.width, canvas.height) / 3;

    let points = [];
    const numPoints = 600;
    for (let i = 0; i < numPoints; i++) {
      let phi = Math.acos(2 * Math.random() - 1);
      let theta = Math.random() * 2 * Math.PI;
      points.push({ phi, theta });
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      centerX = canvas.width / 2;
      centerY = canvas.height / 2;
      radius = Math.min(canvas.width, canvas.height) / 3;

      const time = Date.now() * 0.002;
      const angleX = Math.sin(time / 2) * 0.3;
      const angleY = Math.cos(time / 3) * 0.3
