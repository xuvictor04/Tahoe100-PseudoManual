---
type: "concept"
tags: ["concept", "direction"]
source: "direction/ (tahoemap/direction.py)"
generated_by: "tahoemap"
---

# Probable direction

Which gene probably acts on which. The partners of a gene note move with it, but a correlation has no direction: CDKN1A and MDM2 rise together, and the cosine does not say that both follow TP53. The **direction** stage (`direction/`; the method is tahoemap/direction.py, explained in `docs/direction.md` of the tahoemap repository) adds arrows **SOURCE → TARGET**, computed by code from this run's own tables. Every arrow comes from a statistical test, with a p-value and a Benjamini-Hochberg q (q < 0.10 in its family of tests: a pair without such a result has no arrow), and carries a grade and its alerts.

> [!warning] A probable direction, from the screen's cell lines - not proof of direct regulation. A → B → C looks like A → C, and another alteration carried by the same lines can be the real cause; there is one time point (~24 h), and drugs act on proteins, not on mRNA.

## Where the arrows are

- A gene note's **Direction (probable)** section: *upstream of this gene* (the arrows whose target it is) and *downstream of this gene* (the arrows whose source it is: to other genes, and to the cells under a drug-dose); a sentence in its At a glance when it has arrows.
- A drug note: the genes that set how the cells fare under the drug, and the drug-target arrows of the compound classes it belongs to.
- A cell-line note: its recorded alterations as the comparison groups the stage formed, and the genes it does not express that served as natural knockouts, each with the arrows that came out of it.
- Every list is in one order: grade A, B, C, then q (smallest first), then the size of the effect. A list capped at N shows the N strongest and any of the N strongest without an alert (⚠) beyond them, and says how many more there are and how many of those carry an alert. Nothing is left out for a reason to doubt it.
- An arrow is one test. Where one test stands for several sources (compounds that share several listed targets; genes absent from exactly the same lines) the arrow names them all, and any of them could be the cause.

## The kinds of evidence

| Kind | Short | The source, and what it is set against | Arrows A / B / C (this run) |
|---|---|---|---|
| `genotype_response` | mutation: response | a recorded mutation of the source and the target's drug response | 17 / 13 / 106 |
| `genotype_baseline` | mutation: level | a recorded mutation of the source and the target's baseline level | 8 / 2 / 9 |
| `genotype_sensitivity` | mutation: cells | a recorded mutation of the source and how many cells remain under a drug-dose | 0 / 0 / 1 |
| `null_response` | not expressed: response | lines that do not express the source (natural knockouts) and the target's drug response | 0 / 2019 / 150 |
| `null_baseline` | not expressed: level | lines that do not express the source (natural knockouts) and the target's baseline level | 0 / 38228 / 41645 |
| `null_sensitivity` | not expressed: cells | lines that do not express the source (natural knockouts) and how many cells remain under a drug-dose | 0 / 4070 / 1590 |
| `drug_target` | drug target: level | compounds that target the source and the target's level | 0 / 8846 / 0 |
| `level` | natural level: response | the source's natural level across lines and the target's drug response (a glimpse) | 0 / 0 / 1359 |
| `level_sensitivity` | natural level: cells | the source's natural level across lines and how many cells remain under a drug-dose (a glimpse) | 0 / 0 / 514 |

## Grades

- **A**: strong: a recorded mutation, at least 5 lines on each side compared within organs, significant over the whole table, no other recorded alteration concentrated on either side, and not resting on a correction (any alert it carries is a note to read)
- **B**: worth taking seriously - read its alerts: a mutation result with alerts (another alteration on either side, compared across organs, ...) or only 3-4 lines on a side, a natural knockout with at least 5 lines lacking the gene, or compounds that target the gene
- **C**: a glimpse, a lead to check, not a finding: a gene's natural level, a result significant only within its own group, a comparison the tissue can explain (tissue-confounded), or a natural knockout with few lines

## The sign: what the source's activity does

Every arrow says what the source's **activity** does to the target. For a level (the target's baseline level, or its level under the compounds that target the source) and for the cells' numbers: *raises* or *lowers*. For a drug response: *strengthens* or *weakens* - how strongly the target responds, in its own direction at each drug-dose. Where the target falls under the drugs, *strengthens* means it falls further (the source deepens the fall, i.e. represses it there), and *weakens* means it falls less; where it rises, *strengthens* means it rises more. Read which from all the drug-doses an arrow lists (e.g. 0.49x vs 0.80x: a fall), not the first alone: a target can rise under some drugs and fall under others, and such an arrow is alerted *rises at some drug-doses, falls at others* - its sign then says how strongly the target responds, not whether the source induces or represses it. *Not inferred*: the mechanism of the alteration is not recorded.

For a loss-of-function mutation, the source's activity raises (strengthens) the target when the target is higher (responds more strongly) where the source is intact; for a gain of function it is the reverse. For a gene that some lines do not express, the same with the lines that express it. For compounds that target the source: an inhibitor that raises the target means the source's activity lowers it. For the cells: *raises the cells' numbers* = the source protects the cells under that drug-dose; *lowers* = it makes them more sensitive. For a natural level: the lines with more of the source respond more strongly (strengthens) or less (weakens), or have more (raises) or fewer (lowers) cells.

## Alerts

An arrow with a reason for doubt keeps its place, marked ⚠ with the reason; the doubts lower its grade where the grade rules say so. The tables show each reason by a short label; every reason in full is in `direction/edges.parquet` (column alerts).

The labels in this run, with the number of arrows that carry each, and one reason in full (from the strongest arrow that carries it):

| Label | Arrows | In full (an example) |
|---|---|---|
| also absent: (other genes absent from most of these lines) | 86,698 | other genes are absent from most of these lines too: GRHL2 (+1 absent from the same lines) (overlap 0.97), ST14 (overlap 0.97), TMEM30B (overlap 0.94) (and 1018 more line sets): any of them could be the cause |
| within organs, on part of the lines | 85,331 | compared within organs: 27 of the 33 TP53-altered lines and 15 of the 17 others share an organ with lines of the other side (the comparison rests on those) |
| co-absent with the target | 38,254 | UTY is also absent from most of these lines: which of the two drives the other cannot be told |
| maybe low, not absent | 24,261 | the lines counted as lacking it still read 0.15x its pooled level (maybe low rather than absent) |
| co-occurs with (another gene's altered lines) | 21,228 | co-occurs with CDKN2A-altered lines (overlap 0.53) |
| artifact flags | 9,969 | supporting drug-doses with artifact flags: Selinexor 5 µM (low cells (technical?), cell-cycle shift), Idarubicin (hydrochloride) 0.5 µM (cell-cycle shift), Topotecan (hydrochloride) 5 µM (toxic, cell-cycle shift) |
| N compounds | 8,846 | consistent across 5 compounds (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) |
| off-target possible | 8,846 | drugs can act on other proteins too |
| few lines (N vs N) | 5,057 | few lines (3 vs 47) |
| co-absent genes | 2,859 | 1 other gene(s) are absent from exactly these lines (OVOL1): any of them could be the cause |
| across organs | 2,527 | compared across organs (too few lines of the same organ on both sides for a within-organ comparison) |
| target measured in part of the lines | 2,245 | BAX measured in 31 of the 33 and 17 of the 17 lines |
| its own permutation p | 2,128 | PRRX1's own shuffles of the labels spread differently from the other genes': its own permutation p is used |
| tissue can mimic it | 1,873 | from natural expression differences between lines, tissue and other differences can mimic it |
| precision caveat | 1,359 | a stronger correlation one way can reflect how precisely, or how closely to a shared cause, each gene's level is measured, rather than which gene acts first |
| direction unclear | 1,253 | the reverse (ADAR's level and EIF2AK2's response, r +0.66) is not clearly weaker once it is allowed for that this arrow was written because it is strong, which alone makes it look the stronger (p 0.91): the direction is unclear |
| shared targets | 933 | the 6 targets named share these compounds (Panobinostat, Tucidinostat) and this result: any of them could be the cause |
| tissue-confounded | 860 | tissue-confounded: the organs of the lines without TBILA differ from the other lines' (Cervix: 1 of the 5 lines without TBILA vs 0 of the 45 others, organ-enrichment p 0.025): the comparison cannot separate the gene from the tissue |
| within its drug-dose only (a lead) | 514 | significant among the genes tested for this drug-dose (q 0.00033) but not over all 5,758,605 (gene, drug-dose) tests (q 0.12): a lead (the same tests with the levels permuted give 37 such edges) |
| both ways | 480 | the difference goes the other way at some of its drug-doses (37% of the evidence) |
| rises at some drug-doses, falls at others | 313 | TMEM131 rises at some of the drug-doses carrying the difference and falls at others (42% of the evidence from rises): the sign says how strongly it responds, not whether the source induces or represses it |
| (the source) not expressed in N of the N altered lines | 130 | TP53 itself is not expressed in 3 of the 33 altered lines (deletion or silencing) |
| within its group only (a lead) | 103 | significant within this group (q 0.003 over its 16352 tests) but not over the whole table of genotype groups (q 0.1): a lead, not a finding (random pseudo-groups give 0.27 such edges per group, about 17.1 over the 64 groups) |
| the reference differs | 81 | the reference genes at Dexamethasone 5 µM respond 0.63x as strongly in the lines without FST as in the others (the correction removed that part of the difference) |
| cell counts less trustworthy | 52 | the drug-dose's cell counts are less trustworthy (unreliable plate only) |
| rests on the correction | 28 | the difference exists only relative to the other genes responding at these drug-doses, which themselves differ between the two sides (at Homoharringtonine 5 µM the reference responds 0.64x as strongly in the lines without PMAIP1 as in the others): either those lines respond differently to the drugs in general, or most of those genes depend on PMAIP1 themselves, without the correction JUN's … |
| lower baseline (lost expression?) | 14 | FDXR is 3.9x lower at baseline in the TP53-LoF lines: a weaker response may be lower expression |
| mechanism partly not recorded | 13 | mechanism not recorded for 8 of the 8 lines: the sign of the gene's activity is not inferred |
| line-wide correction only | 4 | at 1 of the 4 drug-doses carrying the difference (52% of the evidence) too few other genes respond to check for a resistance specific to those drugs: only the lines' overall responsiveness was corrected there |
| deletion recorded too | 2 | the lines lacking CDKN2B carry a recorded loss of CDKN2B (overlap 0.92): genotype evidence too |

## This run, and how much to trust it

98,577 arrows (102,590 edges of `direction/edges.parquet`: an arrow that names several sources stands for one edge per source), 98,577 of them with an alert ⚠; grade A 25, B 53,178, C 45,374.

**Positive controls** (known biology that has to come back):

- TP53 (TP53 loss of function (33 lines) vs not recorded (17)) → p53 targets (response): 22 of the 39 target genes present come back as arrows with the expected sign (sign +1: the targets respond less where TP53 is lost), 2 with the other sign; their median rank among the 16,352 genes tested: 50. Found (rank, grade; ⚠ = the arrow carries an alert): [[FDXR]] (rank 1, grade A ⚠), [[BAX]] (rank 2, grade A ⚠), [[ACER2]] (rank 3, grade A ⚠), [[ZMAT3]] (rank 4, grade A ⚠), [[DDB2]] (rank 7, grade A ⚠), [[RRM2B]] (rank 10, grade A ⚠), [[CDKN1A]] (rank 11, grade A ⚠), [[SESN1]] (rank 15, grade A ⚠), [[TRIAP1]] (rank 17, grade A ⚠), [[ZNF79]] (rank 22, grade B ⚠), [[PHLDA3]] (rank 23, grade B ⚠), [[GDF15]] (rank 25, grade B ⚠), [[MDM2]] (rank 28, grade C ⚠), [[FAS]] (rank 32, grade C ⚠), [[TP53I3]] (rank 37, grade C ⚠), [[RPS27L]] (rank 40, grade C ⚠), [[BBC3]] (rank 50, grade C ⚠), [[ASCC3]] (rank 52, grade C ⚠), [[BTG2]] (rank 54, grade C ⚠), [[AEN]] (rank 69, grade C ⚠), [[TIGAR]] (rank 86, grade C ⚠), [[XPC]] (rank 95, grade C ⚠). Not found (rank): [[EDA2R]] (12), [[CCNG1]] (18), [[POLH]] (27), [[SPATA18]] (70), [[PPM1D]] (147), [[PLK3]] (156), [[DRAM1]] (158), [[TP53INP1]] (163), [[GADD45A]] (171), [[TNFRSF10D]] (641), [[TNFRSF10B]] (929), [[SUSD6]] (2,002), [[SERPINB5]] (2,671), [[KITLG]] (8,120), [[APAF1]] (11,512), and 2 more.
- TP53 (TP53 loss of function (33 lines) vs not recorded (17)) → cells under DNA-damaging drugs (sensitivity): 0 arrows among the 42 drug-doses tested, 0 with the expected sign (sign -1: TP53 activity makes the cells more sensitive).
- KEAP1 → NRF2 targets (baseline): not assessable here (KEAP1 is not recorded as altered in >= 3 lines).

**Arrows against the false arrows the controls expect.** Random pseudo-genotype groups (line sets drawn at random, tested exactly like the recorded groups and counted at the real table's cut) give the false arrows a group without any real effect adds; for the natural levels, the same tests with every gene's level shuffled over its lines.

| Evidence | Which arrows | Written | Expected false |  |
|---|---|---|---|---|
| mutation: response | over the whole table | 43 | 12.8 (up to 20.7) |  |
| mutation: response | significant only within its group (grade C: leads) | 93 | 4.27 (up to 9.76) |  |
| mutation: level | over the whole table | 10 | 0 (up to 3.2) |  |
| mutation: level | significant only within its group (grade C: leads) | 9 | 13.9 (up to 22.1) | ⚠ about half or more may be false: read them as leads |
| mutation: cells | over the whole table | 0 | 0 (up to 3.2) |  |
| mutation: cells | significant only within its group (grade C: leads) | 1 | 1.07 (up to 5.06) | ⚠ about half or more may be false: read them as leads |
| natural level: response | over the whole table | 1,359 | 102 (up to 120) |  |
| natural level: cells | over the whole table | 0 | 0 (up to 3) |  |
| natural level: cells | significant only within its drug-dose (grade C: leads) | 514 | 37 (up to 48.7) |  |

'Up to' is the 95% upper bound of that estimate: the controls are a small sample (no false arrow from 60 random groups still allows about 3 per 60 groups), and the natural-level controls are one shuffle each. The estimate can be low when the real groups overlap other alterations, tissue programmes or each other, which random groups do not.

The natural knockouts and the drug-target arrows have no random control: each arrow's alerts say what to doubt.

**Random pseudo-groups** (60 groups): arrows per group, random vs recorded groups:

- response: over the whole table 0.2 vs 0.672; within the group only 0.267 vs 2.12.
- baseline: over the whole table 0 vs 0.172; within the group only 0.217 vs 0.312.
- sensitivity: over the whole table 0 vs 0; within the group only 0.0167 vs 0.0156.

**Natural levels, shuffled** (every gene's level permuted over its lines, the same tests):

- natural level: response: 1,992,533 tests, 1,359 arrows; with the levels shuffled 102.
- natural level: cells: 5,758,605 tests, 0 arrows; with the levels shuffled 0 (and 37 within a drug-dose only, against 514).

## What an arrow does not say

- It is not proof of direct regulation: A → B → C looks like A → C, and another alteration carried by the same lines can be the real cause (the co-occurrence alerts name the ones the metadata records).
- 'Not recorded' is not 'wild type': the metadata lists driver alterations, and a line may carry one that is not listed.
- One time point (~24 h): fast and slow effects are mixed; compensation and feedback are not seen.
- Drugs act on proteins, not on mRNA, and a compound can act on other proteins than its listed target.
- An arrow from a gene's natural level comes from natural differences between lines: tissue and other differences can produce the same pattern, and a stronger correlation one way can come from one gene's level being measured more precisely, not from it acting first.

## Files

- `direction/edges.parquet`: one row per edge (its README.md lists every column); `direction/groups.parquet`: the comparison groups (recorded alterations, natural knockouts, random pseudo-groups); `direction/controls.json`; `direction/info.json`.
- Generated by `tahoe vault` (v4) from `direction/`; rebuilt on every run: do not edit it.
