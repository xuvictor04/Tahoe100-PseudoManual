# The vector space and the nodal map: why there are two, and how they differ

The plan for this project said:

> The difference between the vector space and nodal map is that closely related genes, doing opposite functions,
> would likely be far apart (at least on one vector), whereas on the nodal map, it would be close to each other.

That is right, and it is what the pipeline builds. This note says exactly why, with the numbers that confirm it.

## One response pattern per gene

Each gene gets one row of numbers: its z in every (drug-dose, cell line) context where a drug actually did
something (tens of thousands of contexts on the real data). Two genes "do the same thing" if their rows rise and fall
together; they "do opposite things" if one rises wherever the other falls. After the noise is removed (a truncated
SVD keeps the 64 strongest independent patterns), each gene is a **vector** in a 64-dimensional space, and the
**cosine** between two genes' vectors is the correlation of their cleaned response patterns:

| cosine | meaning | example |
|---|---|---|
| near +1 | move together | two proteasome subunits after proteasome inhibition |
| near 0 | unrelated | most random pairs (mean ≈ 0.01) |
| near −1 | move in exactly opposite directions | a p53 target that rises and a cell-cycle gene that p53 represses |

## The vector space keeps the sign; the nodal map drops it

- **Vector space (and the "signed map" in the HTML viewer).** Distance follows `1 − cos`. A gene pair at cos −0.9 is
  as far apart as two genes can be: the opposite ends of the same axis. So two arms of one pathway, one switched on
  and one switched off, sit on **opposite sides** of the space. You are right that they are "far apart on at least
  one vector": they share an axis and sit at its two ends; on the other axes they can be close.
- **Nodal map.** Distance follows `1 − |cos|`. Moving opposite counts as being related exactly as much as moving
  together, so the two arms land **together**, in one island. Within an island, each gene carries an **arm** label
  (+ or −) and the edges carry their sign (green: moves with, red: moves opposite), so the information is kept; it
  is just not used for placement.

Put differently: the vector space answers "does this gene do what that gene does?", the nodal map answers "is this
gene part of the same response as that gene?". A pathway's activators and its repressed targets fail the first
question and pass the second.

## What this looks like on planted data

The synthetic test data plant modules whose genes go up together, and pairs of modules that one set of drugs moves in
opposite directions (e.g. 40 genes raised and 25 lowered by the same three HDAC inhibitors). After the full pipeline:

| | HDAC up / down | COLOC up / down | COLOC2 up / down |
|---|---|---|---|
| mean cosine within each module | 0.75 / 0.66 | 0.66 / 0.71 | 0.71 / 0.74 |
| mean cosine **between** the two modules | **−0.69** | **−0.69** | **−0.73** |
| same nodal-map module? arms | yes, + / − | yes, − / + | yes, − / + |
| centre-to-centre distance, nodal map (in map spreads, √(var x + var y)) | **0.05** | **0.03** | **0.02** |
| neighbourhood mixing, nodal map (1 = as mixed as chance) | **0.84** | **0.98** | **0.88** |
| neighbourhood mixing, signed map (0 = no shared neighbourhood) | **0.00** | **0.00** | **0.00** |
| centre-to-centre distance, signed map (varies by machine, see below) | 3.00 | 1.45 | 2.47 |

On the signed map the two sides of each pair never share a neighbourhood, on every machine. How far apart their two
islands land does vary: t-SNE keeps neighbourhoods, not long distances, and tiny floating-point differences between
machines move whole islands (the COLOC pair's signed-map centre distance ranged from 0.4 to 2.0 map spreads under
one-in-a-million perturbations of its input). So the tests and `validation/report.md` judge "apart" by the mixing,
and "together" by the nodal-map centre distance and mixing, never by the signed-map centre distance.

The HDAC module of the nodal map holds 63 genes, 40 on its + arm and 23 on its − arm (planted: 40 and 25); the mean
cosine between its arms is −0.69. Random gene pairs have a mean cosine of +0.01. So: anti-aligned in the vector space, one island on the nodal map.

## What this looks like on the real data

Your run tests the same prediction on real biology, and reports it in `validation/report.md` ("opposite-pair
test"): the p53-induced targets (CDKN1A, MDM2, BBC3, …) against the G2/M genes that p53 represses through
p21–DREAM (`tahoemap/data/control_sets.json`). The prediction is a negative mean cosine between the two sets in the
vector space, no shared neighbourhood on the signed map, and a shared island on the nodal map. A second,
exploratory pair (ATF4 stress targets against ribosome biogenesis) is reported the same way. Both sets come from the
literature, not from Tahoe, so the test is independent of the data it is run on.

## Cell lines, drugs and "where"

Drugs, drug-doses, every drug-dose × cell-line context and every cell line get vectors in the **same** space:

- a gene vector · a drug-dose vector ≈ that drug-dose's z on that gene (so comparing vectors reproduces the observed
  activity);
- a drug-dose's vector points towards the programmes (sets of genes) it moves — its nearest gene modules say which
  pathway it acts through;
- a cell line's response vector says, programme by programme, how strongly that line responds compared with the
  typical line (1 typical, 0 not at all) — the "where";
- each (drug-dose, line) context vector says what that drug did in that line.

## Limits

- The space is built from responses to drugs, not from genetic perturbations: "moves with" is co-regulation across
  perturbations, not a regulatory arrow. Opposite movement often means one pathway with two arms (an induced arm and
  a repressed arm), but it can also mean two pathways that the same drugs push in opposite directions.
- t-SNE layouts preserve neighbourhoods, not long distances: two islands far apart on the nodal map are "not
  neighbours", not "maximally different". Use the cosine (`tahoe pair A B`) for any quantitative question.
- Genes without evidence of a response (no significant clean pooled drug-dose and no strong per-line response in
  two lines of one drug-dose) are not in the space; they still have tables and notes, which say why.
- A module's − arm exists only when its two sides really anti-correlate; `graph/modules.parquet` gives the mean
  cosine between the arms, and the vault says when a module is single-armed.
