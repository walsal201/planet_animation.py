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
      font-weight: bold;
      animation: colorShift 6s infinite alternate ease-in-out, pulse 4s infinite;
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

    let baseAngleX = 0;
    let baseAngleY = 0;

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      centerX = canvas.width / 2;
      centerY = canvas.height / 2;
      radius = Math.min(canvas.width, canvas.height) / 3;

      const time = Date.now() * 0.002;
      const angleX = Math.sin(time / 2) * 0.3; // See-saw effect
      const angleY = Math.cos(time / 3) * 0.3;

      points.forEach(point => {
        let x = radius * Math.sin(point.phi) * Math.cos(point.theta);
        let y = radius * Math.sin(point.phi) * Math.sin(point.theta);
        let z = radius * Math.cos(point.phi);

        let tempY = y * Math.cos(angleX) - z * Math.sin(angleX);
        let tempZ = y * Math.sin(angleX) + z * Math.cos(angleX);
        y = tempY;
        z = tempZ;

        let tempX = x * Math.cos(angleY) + z * Math.sin(angleY);
        z = -x * Math.sin(angleY) + z * Math.cos(angleY);
        x = tempX;

        let perspective = 600 / (400 + z);
        let screenX = centerX + x * perspective;
        let screenY = centerY - y * perspective;
        let size = 1.5 * perspective;

        let hue = ((point.theta / (2 * Math.PI)) * 360 + time * 10) % 360;
        let glow = Math.sin(time / 10 + point.phi * 5) * 0.5 + 0.5;

        ctx.beginPath();
        ctx.arc(screenX, screenY, size * glow, 0, Math.PI * 2);
        ctx.fillStyle = `hsla(${hue}, 100%, ${40 + glow * 30}%, ${0.8 + glow * 0.2})`;
        ctx.fill();

        ctx.beginPath();
        ctx.arc(screenX, screenY, size * 2.5 * glow, 0, Math.PI * 2);
        ctx.strokeStyle = `hsla(${(hue + 60) % 360}, 100%, 70%, 0.1)`;
        ctx.lineWidth = 0.5;
        ctx.stroke();

        if (Math.random() < 0.01) {
          ctx.beginPath();
          ctx.arc(screenX, screenY, size * 0.5, 0, Math.PI * 2);
          ctx.fillStyle = `white`;
          ctx.fill();
        }
      });

      requestAnimationFrame(draw);
    }

    draw();
  </script>
</body>
</html>
"""

html(canvas_html, height=700, width=1000)
