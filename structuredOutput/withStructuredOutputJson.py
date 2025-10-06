from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model = GoogleGenerativeAI(model="gemini-2.5-flash")

review = """One battle after another: When Grand Conflicts Meets Personal Drama
"One Battle After Another" is truly a remarkable piece of cinema, one that is difficult to review or rank because it defies the conventions of a typical film. Anderson crafts a work with a distinctive style - unique in its writing, storytelling and characters. With a runtime of nearly three hours, this movie is not for everyone, but I understand why critics love it so much (even though I think some tend to overpraise it a little), and it will likely be a strong contender for next year's Best Picture Oscar.

The story revolves around a radical left-wing organization called French 75, whose members bomb infrastructure and rob banks in pursuit of a revolution. At least, that is the premise established in the first act. The opening is extremely fast-paced, with numerous scenes cut together in quick succession, all underscored by relentless music. There is little breathing room in the beginning. Personally, I am not fond of films that rely so heavily on this montage-style, but here it works quite effectively at times, even if it feels somewhat chaotic because we are plunged into the story with minimal introduction to the characters.

Eventually, there is a noticeable shift-both in story and in storytelling. The montage style gradually gives way to longer, uninterrupted scenes. While the first act functions almost as an extended prologue (for me a bit too long), the second act emerges as the true main story. Tonally, the film becomes more intimate and personal, with humor beginning to surface.

The structure and style initially felt unfamiliar, and it took me over half the runtime to fully immerse myself in the film-but once I did, I was completely invested, eagerly anticipating each new scene and wishing the film would not end so quickly.

One of the film's greatest strengths is its characters.

Leonardo DiCaprio's Bob Ferguson, the central figure, is not only brilliantly performed but also exceptionally well-written: a former revolutionary hero now struggling with drugs and a strained relationship with his daughter, who must confront his past.

Colonel Lockjaw is a uniquely menacing antagonist, more akin to a caricature, yet brought vividly to life by Sean Penn's performance.

Benicio Del Toro's character (an absolute scene stealer) is hilarious and perfectly executed, leaving a lasting impression despite limited screen time.

However, one weakness of the film is that it doesn't reach the same emotional depth as it does in its action and storytelling. You don't feel deeply attached to the characters on an emotional level; instead your investment comes more from the momentum of the story, the intensity of the action, and the power of the music.

At the same time, the film balances this with well-placed humor, which is woven naturally into the story. It manages to be genuinely funny at times without ever undercutting the more serious or dramatic moments. Especially DiCaprio and Del Toro show their comedic skills.

The musical score, composed by Jonny Greenwood, is another standout. Its fast-paced, innovative sounds heighten the tension and exhilaration of every scene, drawing the audience deeper into the story.

Visually, the film isn't overwhelmingly stylized, and its overall look is fairly restrained. However, there are several shots and camera movements that are truly remarkable, creating moments of cinematic grandeur that leave a lasting impression.

What I find most impressive, however, is how the film functions simultaneously as a political action thriller and a deeply personal character drama with moments of comedy. Yes, it depicts near-civil-war conditions, but at its core, the conflict is personal and character-driven. This combination works brilliantly, setting the film apart from others in its genre.

Ultimately, One Battle After Another' is both a warning and a reflection: it explores the consequences of ideologies turning violent, while also telling a story about hope, responsibility, and love."""


# schema
json_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "key_themes": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Write down all the key themes discussed in the review in a list",
        },
        "summary": {"type": "string", "description": "A brief summary of the review"},
        "sentiment": {
            "type": "string",
            "enum": ["pos", "neg"],
            "description": "Return sentiment of the review either negative, positive or neutral",
        },
        "pros": {
            "type": ["array", "null"],
            "items": {"type": "string"},
            "description": "Write down all the pros inside a list",
        },
        "cons": {
            "type": ["array", "null"],
            "items": {"type": "string"},
            "description": "Write down all the cons inside a list",
        },
        "name": {
            "type": ["string", "null"],
            "description": "Write the name of the reviewer",
        },
    },
    "required": ["key_themes", "summary", "sentiment"],
}


structured_model = model.with_structured_output(json_schema)
result = structured_model.invoke(review)
print(result.key_themes)
# we get NotImplementedError cause gemini still doesn't have structured_output function.
