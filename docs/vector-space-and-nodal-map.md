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

## How the gene modules are made

The modules (and their + / − arms) are groups of the nodal map, made in the graph stage (`tahoemap/graph.py`) from
the gene relations, in five steps:

1. **A graph of strong partners with the same sign in both halves of the compounds.** Each gene in the vector space
   is linked to its 15 strongest partners by |cos| ≥ 0.3 whose relation has the same sign in both halves of the
   compounds (`both halves`: the same sign in the full space and in the spaces fitted on two random halves of the
   compounds, fdr ≤ 0.10) or is very strong in one half (|cos| ≥ 0.5). The link's weight is
   |cos|: genes that move opposite are linked as strongly as genes that move together (its sign is kept for the arms).
2. **Communities.** Louvain community detection (resolution 1, fixed seed) on that weighted graph: groups of genes
   linked more densely to one another than to the rest.
3. **Split what is too broad.** Over the whole genome a first pass returns programme-sized groups of 1,000+ loosely
   related genes, so a group of more than 300 genes, or one whose members' mean |cos| is below 0.3, is split again by
   Louvain on its own subgraph (up to 4 levels).
4. **Too small is no module.** A piece of fewer than 5 genes gets module 0 (unassigned); its genes keep their place
   on the maps and their partners.
5. **Arms.** Each member is projected on the module's first principal direction. The module gets a separate − arm
   only when at least 5 members sit on the negative side and the two sides anti-correlate (mean cosine between them
   ≤ −0.2); otherwise every member is +. `graph/modules.parquet` gives the mean cosine within each arm and between
   the arms; `graph/info.json` records the numbers used; the map's help ("How the modules are made") repeats them.

Modules are then labelled by enrichment (validation: curated control programmes, Hallmark, Reactome); a module
without a significant set is named by its top genes.

**Covariate tags (graph version 6).** A module whose score rises and falls with a technical measure of the wells, or
with the cell-cycle shift, may partly be that measure. For each module, `graph/modules.parquet` gives the correlation
(`cov_<k>_r`, Pearson) and the rank correlation (`cov_<k>_rho`, Spearman) of its pooled score with six measures of
each drug-dose, over the trusted drug-doses (not 'unreliable plate only', 'position not correctable' or 'wells
disagree'): UMI per cell, genes per cell, cells per well (cell loss) and the composition shift (technical), the S-phase
shift and the G2/M shift (cell cycle). When both |r| and |rank r| reach 0.3, `covariate_tag` says so in words ('moves
with cells per well (cell loss) across drug-doses (r -0.61, rank r -0.61)') and `covariate_kinds` says 'technical',
'cell cycle' or both. It is a note, not an alert: a cell-cycle module is expected to move with the cell-cycle shift.
Chance correlations stay far below 0.3: with the measure shuffled 200 times, the largest |r| over all modules reaches
about 0.12 to 0.16 (99% quantile; `graph/info.json` covariate_null_max_r). On the real data 82 of 235 modules carry a
tag (UMI per cell 31, genes per cell 28, cells per well 36, composition 0, S phase 23, G2/M 29; over all 1,132
drug-doses instead of the 1,086 trusted ones: 30, 27, 36, 0, 22, 27, 81 modules). Examples: module 22 moves with the
G2/M shift (r +0.93), module 196 with cell loss (r -0.61), module 131 with UMI per cell (r -0.55). The composition
shift reaches |r| > 0.3 in some modules, but its rank correlation never does: those are a few extreme drug-doses.
`graph/modules.gmt` holds every module arm as a gene set ('module 12 +', 'module 12 -').

## Spreading the modules apart, and the k-D tour

t-SNE keeps many of a gene's neighbours near it, but not all of them (see "How much of a gene's neighbourhood a map
keeps", below), and it does not keep modules apart: on a large map, neighbouring modules touch and interleave. Each
map therefore also has a **spread layout** (`graph/nodes.parquet` xm, ym for the nodal map; xsm, ysm for the signed
map, where each arm of a two-armed module is its own group), and the map's **Spread** slider moves smoothly between
the two. Each module keeps its own t-SNE arrangement as one block (islands of a module are packed together); the
blocks are placed by the modules' directions in the full vector space (1 − |cos| between module directions for the
nodal map, 1 − cos for the signed map; classical MDS refined by SMACOF); overlapping blocks are pushed apart; a gene
without a module moves rigidly with one module: among the modules of its 5 nearest module genes on the t-SNE map, the
one it is most alike in the vector space (summed |cos|, or cos on the signed map, to those neighbours), keeping its
offset from the nearest of them (moves are never averaged across modules, whose blocks move in different directions).
No random draws: the same run gives the same layout. On planted data the share of a module gene's 5 nearest module
genes that belong to another group falls from 9.5% to 0.4% on the nodal map, and from 16.7% to 0.8% on the signed map;
a gene without a module has a mean |cos| of 0.29 to its 5 nearest module genes on the t-SNE layout and 0.25 spread
(signed map, mean cos 0.25 and 0.18; averaging the moves gave 0.21 and 0.11).

Both maps squeeze 64 dimensions into 2. The map's **k-D tour** tab shows the vectors themselves: the genes' unit
vectors projected onto a 2-D plane that turns smoothly through all dimensions (a grand tour; play / pause, speed,
"New direction"), or, in axis mode, one component of the space against another exactly (the components of the embed
stage, largest first). A group that stays together while the plane turns is together in the full space.

## How much of a gene's neighbourhood a map keeps (partner preservation)

A flat map cannot keep every gene next to all of its partners. `graph/info.json` partner_preservation measures how
much it keeps: for each layout, the share of the genes' 15 strongest partners (the relations table, both genes on the
map) that are among the gene's 50 nearest genes on the map. On the real data (15,076 genes):

| layout | share of the 15 strongest partners among the 50 nearest genes |
|---|---|
| nodal map (x, y) | 0.358 |
| signed map (xs, ys) | 0.357 |
| nodal map, spread (xm, ym) | 0.314 |
| signed map, spread (xsm, ysm) | 0.310 |
| chance (50 of 15,075 genes) | 0.0033 |

So a map keeps about a third of each gene's closest partners nearby: about 100 times more than chance, but far from
all of them. Two genes side by side on a map are probably related; two genes far apart may still be close partners.
For a gene's partners read its partner list (the side panel, the vault note, `tahoe gene`), not the distance on the
map.

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
cosine between its arms is −0.69. Random gene pairs have a mean cosine of +0.01. So: anti-aligned in the vector
space, one island on the nodal map.

## What this looks like on the real data

Your run tests the same prediction on real biology, and reports it in `validation/report.md` ("opposite-pair
test"): the p53-induced targets (CDKN1A, MDM2, BBC3, …) against the G2/M genes that p53 represses through
p21–DREAM (`tahoemap/data/control_sets.json`). The prediction is a negative mean cosine between the two sets in the
vector space, no shared neighbourhood on the signed map, and a shared island on the nodal map. A second,
exploratory pair (ATF4 stress targets against ribosome biogenesis) is reported the same way. Both sets come from the
literature, not from Tahoe, so the test is independent of the data it is run on.

## Partners: how far to trust each relation

`relations/gene_relations.parquet` keeps each gene's 100 strongest partners. Every pair stays in its ranked place; a
reason to doubt it is an alert (⚠) shown with it, never a removal.

**Counting units.** The table has one row per (gene, partner): each gene's top 100, so a pair can appear twice, once
from each side. `relations/info.json` gives every count in both units: `rows_*` (rows) and `pairs_*` (distinct
unordered gene pairs). On the real data: 1,507,600 rows, 1,102,322 pairs.

**The same sign in both halves of the compounds.** The compounds (salt forms together) are split into two random
halves, and the space is fitted again on each. A relation is `both halves` when it has the same sign in the full space
and in both half spaces, with |cos| ≥ 0.2 in each half and fdr ≤ 0.10. The halves share the lines and plates, so this
guards against single-compound effects, not against everything; 98% of the top-100 partners pass it (1,483,872 of
1,507,600 rows; 1,080,453 pairs). It is not called "replicated": it is a weak filter, and the alerts below catch
causes it cannot see.

**Lineage pairs.** Genes that only some cell lines express often move together whatever their regulation: their
contexts are the responses of the same few lines. Among the real genes expressed in at most 30 of 50 lines, the share
of pairs with |cos| ≥ 0.5 rises with the overlap of their expressing lines (Jaccard J):

| J | < 0.3 | 0.3-0.5 | 0.5-0.6 | 0.6-0.7 | 0.7-0.8 | 0.8-0.9 | ≥ 0.9 |
|---|---|---|---|---|---|---|---|
| pairs with \|cos\| ≥ 0.5 | 0.43% | 2.2% | 5.8% | 10.6% | 17.1% | 27.1% | 38.3% |

(random pairs of genes expressed in at least 48 lines: 1.6%). The zeros of the lines that do not express a gene do not
make the cosine (their offset is below 0.001); the shared lines' responses do. So a pair of two such genes (each in at
most 0.6 × the lines, 30 of 50) with J ≥ 0.5 is a **lineage pair** (`lineage_pair`), with `n_lines_a`, `n_lines_b`,
`lines_shared` and `lines_jaccard`. Its `lineage_p` compares it with every pair of such genes in the same J bin
(0.5-0.6, 0.6-0.7, 0.7-0.8, 0.8-0.9, 0.9-1): (1 + pairs at least as strong) / (1 + pairs in the bin). Its alert says:
'lineage: both genes are expressed in few lines, mostly the same (6 and 9 of 50, 6 shared): such genes often move
together whatever their regulation (10.6% of such pairs reach |cos| >= 0.5 here, and this pair is stronger than 99.99%
of them)'. On the real data 27,798 rows (17,026 pairs) are lineage pairs; 661 of the 2,815 novel candidate pairs are,
and 213 of those have lineage_p ≥ 0.01 (no stronger than a typical pair that shares its lines as much). SYT4-ASCL1
(neuroendocrine genes, 6 and 9 lines) is the strongest pair of its bin (lineage_p 7e-5): lineage is a reason to doubt
it, not a verdict.

**Read-sharing copies.** Reads of near-identical sequences can be counted for either gene, so such genes correlate
without any regulation. A pair is a read-sharing copy (`read_sharing`, with `read_sharing_risk`) when it is:
(a) a pair of Ensembl Compara paralogues with ≥ 95% protein identity (NOTCH2NLA/B/C, NBPF10/14, CNTNAP3/3B,
WASHC2A/C, POM121/C; MT1X-MT2A at 90% and SERPINB3/4 at 92% are not); (b) an HGNC pseudogene and its parent - its
symbol is the parent's plus 'P' and digits (HERC2P2 → HERC2, NAMPTP1 → NAMPT), or it differs from a gene in a last
single digit (PDXDC2P → PDXDC1, HSP90AB3P → HSP90AB1; ZNF271P is not a copy of ZNF275), or HGNC names it 'X
pseudogene N' - or two pseudogenes of one parent (HERC2P2-HERC2P3); (c) an HGNC read-through transcript and a gene it
contains (KLRC4-KLRK1 and KLRK1). On the real data 535 such pairs exist among Tahoe's genes; 189 of them (349 rows)
are partners, 237 rows of which had no other alert, and 14 were novel candidates (among them PDXDC1-PDXDC2P and
HSP90AB3P-HSP90AB2P). `relations/info.json` read_sharing_source says what could be checked ('Compara 112 + HGNC',
'HGNC only (paralogues not loaded)', or 'not assessed ...').

## Drug-doses that act alike

`embed/drug_similarity.parquet` lists, for every drug-dose, its 50 most similar of the other 1,131 (all are compared;
the table keeps the top 50 of each, ranked by `cos_pooled`): `cos_pooled` compares the pooled signatures (z clipped to
±10 on the genes the drug-dose moves, |z| ≥ 3 or q < 0.10, 0 elsewhere), `cos_contexts` the drug-doses' responses in
each line (their context vectors), `n_shared_sig` counts the significant genes both change the same way, and the other
drug-dose's class, mechanism classes and flags come with it. On the real data a drug's nearest drugs share its Tahoe
class more often than chance (AUROC 0.578 pooled, 0.584 by contexts; 18% and 21% of the 5 nearest).

Two notes come from it, never flags:
- **Unexpected similarity** (`embed/drugdoses.parquet` resembles_*): when at least 4 of a drug-dose's 10 most similar
  drug-doses of other compounds (cosine ≥ 0.5, ≥ 10 shared significant genes) share one Tahoe class that is not its
  own. On the real data 8 drug-doses: Phenylephrine 5 µM, Econazole 5 µM, Citalopram 0.05 µM and Clobetasol
  propionate 0.5 and 5 µM resemble the glucocorticoids, Brivudine 5 µM the HDAC inhibitors, Elimusertib 0.05 µM the
  MEK inhibitors and Ixazomib 5 µM tofacitinib. Phenylephrine 5 and Econazole 5 touch no glucocorticoid well, so the
  neighbouring-well rule cannot explain them; the note says 'It may act like them, or carry a signal from another
  well'.
- **Salt forms that disagree** (`embed/drugs.parquet` salt_form_alert): two salt forms of one compound at one dose
  should agree. 'signatures differ' when both have ≥ 100 significant genes and their signature cosine is below 0.3;
  'strength differs' when one has at least 10 times the other's significant genes (+1 each) and ≥ 30. On the real
  data 13 of 57 pair-doses (19 compounds): Docetaxel 0.5 µM 'signatures differ' (101 vs 829 genes, cosine 0.06) and 12
  'strength differs'.

## Cell lines, drugs and "where"

Drugs, drug-doses, every drug-dose × cell-line context and every cell line get vectors in the **same** space:

- a gene vector · a drug-dose vector ≈ that drug-dose's z on that gene (so comparing vectors reproduces the observed
  activity);
- a drug-dose's vector points towards the programmes (sets of genes) it moves — its nearest gene modules say which
  pathway it acts through;
- a cell line's response vector says, programme by programme, how strongly that line responds compared with the
  typical line (1 typical, 0 not at all) — the "where";
- each (drug-dose, line) context vector says what that drug did in that line.

## Arrows on the maps: probable direction

Neither map has arrows of its own: a cosine is symmetric. The arrows come from the direction stage
([direction.md](direction.md)), which asks what differs between the cell lines (a recorded mutation, a gene that some
lines do not express, compounds that target a gene, a gene's natural level) and which genes follow it. The map shows
them in three places:

- **The side panel** of the selected gene: *Upstream* (what probably acts on it), *Downstream* (what it probably acts
  on) and *Cells under drug-doses* (how it probably acts on the cells' numbers under a drug). Each list shows its 8
  strongest rows and any of the 8 strongest without an alert that come after them, says how many more there are and
  how many of those carry an alert, and opens fully with *show all*.
- **The neighbourhood tab**, with its **Direction** control: *off*; *arrows* between the genes shown; or *+ its genes*
  (the default), which also adds the selected gene's up- and downstream genes around it (a violet ring). That is how a
  gene that is not on the map (it responds too little to the drugs to be in the vector space, as TP53 in the synthetic
  test data) is shown with the genes it probably acts on. The added genes are held near it by a link that is not
  drawn and is not a relation.
- **The nodal and signed maps**, with the **Direction arrows** box: the selected gene's arrows to and from the genes
  on the map.

The line shows the grade (A thick, B thin, C dashed), the head the sign (a filled head: the source's activity raises
the target's level or the cells' numbers; a bar: lowers it; an open head: strengthens the target's drug response; a
double bar: weakens it; an open circle: not inferred). Hover a gene to see the rows between it and the selected
gene. An arrow is a probable direction from the cell lines, not proof of direct regulation, and its alerts (⚠) say
what to doubt.

## Limits

- The space is built from responses to drugs, not from genetic perturbations: "moves with" is co-regulation across
  perturbations, not a regulatory arrow (the probable arrows come from the direction stage, above). Opposite movement
  often means one pathway with two arms (an induced arm and a repressed arm), but it can also mean two pathways that
  the same drugs push in opposite directions.
- t-SNE layouts keep part of each neighbourhood (about a third of a gene's 15 strongest partners are among its 50
  nearest genes on the map) and no long distances: two islands far apart on the nodal map are "not neighbours", not
  "maximally different". Use the cosine (`tahoe pair A B`) and the partner lists for any quantitative question.
- Genes without evidence of a response (no significant pooled drug-dose and no strong per-line response in two
  lines of one drug-dose) are not in the space; they still have tables and notes, which say why ('⚠ not in the
  vector space' and the reason). A gene whose only evidence is significant drug-doses with an artifact flag (toxic,
  transcription drop, a cell-cycle shift that explains its change ...) is in the space but marked ⚠ everywhere: its
  place, partners and module may reflect the artifact.
- A module's − arm exists only when its two sides really anti-correlate; `graph/modules.parquet` gives the mean
  cosine between the arms, and the vault says when a module is single-armed.
