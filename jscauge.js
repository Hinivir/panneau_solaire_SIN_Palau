var gauge = new RadialGauge({
    renderTo: 'canvas-id',
    minValue: 0,
    maxValue: 360,
    majorTicks: [
        "N",
        "NE",
        "E",
        "SE",
        "S",
        "SW",
        "W",
        "NW",
        "N"
    ],
    minorTicks: 22,
    ticksAngle: 360,
    startAngle: 180,
    strokeTicks: false,
    highlights: false,
    colorPlate: "#33a",
    colorMajorTicks: "#f5f5f5",
    colorMinorTicks: "#ddd",
    colorNumbers: "#ccc",
    colorNeedle: "rgba(240, 128, 128, 1)",
    colorNeedleEnd: "rgba(255, 160, 122, .9)",
    valueBox: false,
    valueTextShadow: false,
    colorCircleInner: "#fff",
    colorNeedleCircleOuter: "#ccc",
    needleCircleSize: 15,
    needleCircleOuter: false,
    animationRule: "linear",
    needleType: "line",
    needleStart: 75,
    needleEnd: 99,
    needleWidth: 3,
    borders: true,
    borderInnerWidth: 0,
    borderMiddleWidth: 0,
    borderOuterWidth: 10,
    colorBorderOuter: "#ccc",
    colorBorderOuterEnd: "#ccc",
    colorNeedleShadowDown: "#222",
    borderShadowWidth: 0,
    animationTarget: "plate",
    units: "ᵍ",
    title: "DIRECTION",
    fontTitleSize: 19,
    colorTitle: "#f5f5f5",
    animationDuration: 1500
}).draw();