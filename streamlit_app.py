import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st

text = '''MR. CHIEF JUSTICE WARREN delivered the opinion of the Court.
This case presents a constitutional question never addressed by this Court: whether a statutory scheme adopted by the State of Virginia to prevent marriages between persons solely on the basis of racial classifications violates the Equal Protection and Due Process Clauses of the Fourteenth Amendment. [Footnote 1] For reasons which seem to us to reflect the central meaning of those constitutional commands, we conclude that these statutes cannot stand consistently with the Fourteenth Amendment.
In June, 1958, two residents of Virginia, Mildred Jeter, a Negro woman, and Richard Loving, a white man, were married in the District of Columbia pursuant to its laws. Shortly after their marriage, the Lovings returned to Virginia and established their marital abode in Caroline County. At the October Term, 1958, of the Circuit Court
Page 388 U. S. 3
of Caroline County, a grand jury issued an indictment charging the Lovings with violating Virginia's ban on interracial marriages. On January 6, 1959, the Lovings pleaded guilty to the charge, and were sentenced to one year in jail; however, the trial judge suspended the sentence for a period of 25 years on the condition that the Lovings leave the State and not return to Virginia together for 25 years. He stated in an opinion that:
"Almighty God created the races white, black, yellow, malay and red, and he placed them on separate continents. And, but for the interference with his arrangement, there would be no cause for such marriage. The fact that he separated the races shows that he did not intend for the races to mix."
After their convictions, the Lovings took up residence in the District of Columbia. On November 6, 1963, they filed a motion in the state trial court to vacate the judgment and set aside the sentence on the ground that the statutes which they had violated were repugnant to the Fourteenth Amendment. The motion not having been decided by October 28, 1964, the Lovings instituted a class action in the United States District Court for the Eastern District of Virginia requesting that a three-judge court be convened to declare the Virginia anti-miscegenation statutes unconstitutional and to enjoin state officials from enforcing their convictions. On January 22, 1965, the state trial judge denied the motion to vacate the sentences, and the Lovings perfected an appeal to the Supreme Court of Appeals of Virginia. On February 11, 1965, the three-judge District Court continued the case to allow the Lovings to present their constitutional claims to the highest state court.
The Supreme Court of Appeals upheld the constitutionality of the anti-miscegenation statutes and, after
Page 388 U. S. 4'''


wc = WordCloud()
wc.generate(text)

plt.axis("off")
plt.imshow(wc, interpolation="bilinear")
plt.show()