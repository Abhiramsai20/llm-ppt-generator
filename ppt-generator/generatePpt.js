const pptxgen = require("pptxgenjs");
const fs = require("fs");

const pptx = new pptxgen();

pptx.layout = "LAYOUT_WIDE";
pptx.author = "PPT LLM";
pptx.company = "PPT LLM";

const data = JSON.parse(
    fs.readFileSync("slides.json", "utf8")
);

const COLORS = {
    primary: "1F4E79",
    secondary: "D9EAF7",
    accent: "4472C4",
    text: "222222",
    light: "F8F9FA"
};


// =========================
// TITLE SLIDE
// =========================

let titleSlide = pptx.addSlide();

titleSlide.background = {
    color: COLORS.primary
};

titleSlide.addText(
    data.title,
    {
        x: 1,
        y: 2.2,
        w: 11,
        h: 1,
        fontSize: 32,
        fontFace: "Segoe UI",
        bold: true,
        color: "FFFFFF",
        align: "center"
    }
);

titleSlide.addText(
    "Professional AI Generated Presentation",
    {
        x: 2,
        y: 3.2,
        w: 9,
        h: 0.5,
        fontSize: 18,
        fontFace: "Aptos",
        color: "FFFFFF",
        align: "center"
    }
);


// =========================
// AGENDA SLIDE
// =========================

let agendaSlide = pptx.addSlide();

agendaSlide.addText(
    "Agenda",
    {
        x: 0.5,
        y: 0.5,
        w: 5,
        h: 0.5,
        fontSize: 28,
        fontFace: "Segoe UI",
        bold: true,
        color: COLORS.primary
    }
);

const agendaText = data.slides
    .map((slide, index) => `${index + 1}. ${slide.title}`)
    .join("\n");

agendaSlide.addText(
    agendaText,
    {
        x: 0.8,
        y: 1.2,
        w: 7,
        h: 5,
        fontSize: 18,
        fontFace: "Aptos"
    }
);


// =========================
// CONTENT SLIDES
// =========================

data.slides.forEach((slideData, index) => {

    let slide = pptx.addSlide();

    const hasImage =
        slideData.image_path &&
        fs.existsSync("../backend/" + slideData.image_path);

    const textWidth = hasImage ? 7 : 12;

    // Header Bar
    slide.addShape(
        pptx.ShapeType.rect,
        {
            x: 0,
            y: 0,
            w: 13.33,
            h: 0.35,
            fill: { color: COLORS.primary },
            line: { color: COLORS.primary }
        }
    );

    // Title
    slide.addText(
        slideData.title,
        {
            x: 0.5,
            y: 0.5,
            w: textWidth,
            h: 0.4,
            fontSize: 22,
            fontFace: "Aptos",
            bold: true,
            color: COLORS.primary
        }
    );

    // Summary
    slide.addText(
        slideData.summary || "",
        {
            x: 0.5,
            y: 1.0,
            w: textWidth,
            h: 0.3,
            fontSize: 13,
            italic: true,
            fontFace: "Aptos",
            color: "666666"
        }
    );

    // Content
    slide.addText(
    slideData.content || "",
    {
        x: 0.5,
        y: 1.5,
        w: textWidth,
        h: hasImage ? 1.2 : 1.8,
        fontSize: 14,
        fontFace: "Aptos",
        color: COLORS.text,
        fit: "shrink"
    }
);

    // Bullets
    if (
        slideData.bullets &&
        slideData.bullets.length > 0
    ) {

        slide.addText(
            slideData.bullets.map(item => ({
                text: item,
                options: { bullet: true }
            })),
            {
                 x: 0.7,
                 y: 2.4,
                w: textWidth,
                 h: hasImage ? 2 : 3.5,
                fontSize: 15,
                 fontFace: "Aptos",
                  fit: "shrink"
}
        );
    }

    // Example
    if (
        slideData.example &&
        slideData.example.trim() !== ""
    ) {

        slide.addShape(
            pptx.ShapeType.roundRect,
            {
                x: 0.5,
                y: 4.8,
                w: textWidth,
                h: 0.8,
                fill: {
                    color: "FFF2CC"
                }
            }
        );

        slide.addText(
            "Example: " + slideData.example,
            {
                x: 0.7,
                y: 5.0,
                w: textWidth - 0.3,
                h: 0.4,
                fontSize: 13,
                fontFace: "Aptos"
            }
        );
    }

    // Takeaway
    if (
        slideData.takeaway &&
        slideData.takeaway.trim() !== ""
    ) {

        slide.addShape(
            pptx.ShapeType.roundRect,
            {
                x: 0.5,
                y: 5.8,
                w: textWidth,
                h: 0.7,
                fill: {
                    color: "E2F0D9"
                }
            }
        );

        slide.addText(
            "Takeaway: " + slideData.takeaway,
            {
                x: 0.7,
                y: 5.95,
                w: textWidth - 0.3,
                h: 0.3,
                fontSize: 13,
                fontFace: "Aptos"
            }
        );
    }

    // Image
    // Image
    if (hasImage) {

        slide.addImage({
            path: "../backend/" + slideData.image_path,
            x: 8,
            y: 1.2,
            w: 4.4,
            h: 3.4
    }
);

}

    // Footer
    slide.addText(
        "Generated by PPT LLM",
        {
            x: 0.2,
            y: 7.05,
            w: 2,
            h: 0.2,
            fontSize: 8,
            fontFace: "Aptos",
            color: "777777"
        }
    );

    slide.addText(
        String(index + 1),
        {
            x: 12.5,
            y: 7.05,
            w: 0.3,
            h: 0.2,
            fontSize: 10,
            fontFace: "Aptos"
        }
    );

});



// =========================
// Q&A SLIDE
// =========================

let qaSlide = pptx.addSlide();

qaSlide.addText(
    "Questions & Answers",
    {
        x: 2,
        y: 2.5,
        w: 8,
        h: 1,
        fontSize: 30,
        fontFace: "Segoe UI",
        bold: true,
        align: "center",
        color: COLORS.primary
    }
);


// =========================
// THANK YOU SLIDE
// =========================

let thankYouSlide = pptx.addSlide();

thankYouSlide.background = {
    color: COLORS.primary
};

thankYouSlide.addText(
    "THANK YOU",
    {
        x: 2,
        y: 2.3,
        w: 8,
        h: 1,
        fontSize: 36,
        fontFace: "Segoe UI",
        bold: true,
        color: "FFFFFF",
        align: "center"
    }
);

thankYouSlide.addText(
    "Questions & Discussion",
    {
        x: 2,
        y: 3.4,
        w: 8,
        h: 0.5,
        fontSize: 18,
        fontFace: "Aptos",
        color: "FFFFFF",
        align: "center"
    }
);


// =========================
// SAVE PPT
// =========================

pptx.writeFile({
    fileName: "../backend/output/generated_presentation.pptx"
});