const scene = new THREE.Scene({ color: 0xfff });
const camera = new THREE.PerspectiveCamera(
  100,
  window.innerWidth / window.innerHeight,
  1,
  1000
);
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setSize(window.innerWidth, window.innerHeight);

document.body.appendChild(renderer.domElement);

const light = new THREE.PointLight(0xffffff, 1, 300);
light.position.set(-5, -1, 0.5);
camera.add(light);
scene.add(camera);

const material = new THREE.MeshPhongMaterial({
  color: 0x000000,
});

const points = [
  { x: 1.2, y: 0 },
  { x: 1.2, y: 0.4 },
  { x: 1.1, y: 0.3 },
  { x: 0.9, y: 0.4 },
  { x: 0.78, y: 1 },

  { x: 0.5, y: 4 },
  { x: 0.7, y: 4.25 },
  { x: 0.7, y: 4.5 },
  { x: 0.75, y: 4.6 },
];

const geometry = new THREE.LatheGeometry(points, 32);
const lathe = new THREE.Mesh(geometry, material);
lathe.position.set(0, -4, 0);
scene.add(lathe);

function animate() {
  requestAnimationFrame(animate);
  renderer.render(scene, camera);
}

camera.position.z = 7;

animate();
