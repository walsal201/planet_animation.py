import streamlit as st
from streamlit.components.v1 import html

canvas_html = """
<!DOCTYPE html>
<html>
<head>
  <style>
    body { margin: 0; overflow: hidden; }
    canvas { display: block; }
  </style>
</head>
<body>
  <canvas id="canvas"></canvas>
  <script>
    var canvas = document.getElementById('canvas');
    var ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });

    var centerX = canvas.width / 2;
    var centerY = canvas.height / 2;
    var radius = Math.min(canvas.width, canvas.height) / 3;

    var points = [];
    var numPoints = 500;
    for (var i = 0; i < numPoints; i++) {
        var phi = Math.acos(2 * Math.random() - 1);
        var theta = Math.random() * 2 * Math.PI;
        points.push({ phi, theta });
    }

    var angleX = 0;
    var angleY = 0;

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        points.forEach(point => {
            var x = radius * Math.sin(point.phi) * Math.cos(point.theta);
            var y = radius * Math.sin(point.phi) * Math.sin(point.theta);
            var z = radius * Math.cos(point.phi);

            var tempY = y * Math.cos(angleX) - z * Math.sin(angleX);
            var tempZ = y * Math.sin(angleX) + z * Math.cos(angleX);
            y = tempY;
            z = tempZ;

            var tempX = x * Math.cos(angleY) + z * Math.sin(angleY);
            z = -x * Math.sin(angleY) + z * Math.cos(angleY);
            x = tempX;

            var perspective = 600 / (400 + z);
            var screenX = centerX + x * perspective;
            var screenY = centerY - y * perspective;
            var size = 1 * perspective;

            ctx.beginPath();
            ctx.arc(screenX, screenY, size, 0, Math.PI * 2);
            ctx.fillStyle = `hsl(${(point.theta / (2 * Math.PI)) * 360}, 100%, 25%, 1)`;
            ctx.fill();
        });

        angleX += 0.0025;
        angleY += 0.0055;
        requestAnimationFrame(draw);
    }

    draw();
  </script>
</body>
</html>
"""

# Embed the animation in Streamlit
html(canvas_html, height=600, width=800)
