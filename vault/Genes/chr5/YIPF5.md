---
symbol: "YIPF5"
type: "gene"
col: 7029
ensembl_id: "ENSG00000145817"
name: "Yip1 domain family member 5"
location: "5q31.3"
module: 41
arm: "+"
pooled_cpm: 79.14
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# YIPF5

*Yip1 domain family member 5* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.48× (z +6.0, q 9e-07, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.529× (z -9.8, q 6e-20, down in 38 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.563× (z -8.8, q 3e-16, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPTY2D1]] (+0.84, fdr 7e-06), [[ACBD3]] (+0.81, fdr 7e-06), [[GOLGA5]] (+0.78, fdr 7e-06).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TBC1D8B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7029.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +6.0 | 9e-07 | 35/48 (HEC-1-A, RKO, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.91×** | +5.2 | 5e-05 | 31/49 (LoVo, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.61×** | +3.9 | 0.022 | 21/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.1 | 0.28 | 20/49 (MIA PaCa-2, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7029.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.529×** | -9.8 | 6e-20 | 38/48 (BT-474, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.563×** | -8.8 | 3e-16 | 42/48 (H4, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.583×** | -7.7 | 3e-12 | 32/44 (A-427, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.611×** | -7.3 | 5e-11 | 38/47 (SNU-423, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.635×** | -7.0 | 3e-10 | 37/48 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.658×** | -6.4 | 1e-08 | 34/48 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.723×** | -4.8 | 1e-04 | 23/41 (A-427, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.804×** | -4.7 | 2e-04 | 30/48 (AsPC-1, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.751×** | -4.4 | 7e-04 | 28/49 (LS 180, SW 1271, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.768×** | -4.1 | 0.003 | 29/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.774×** | -3.9 | 0.004 | 24/48 (A498, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.801×** | -3.3 | 0.050 | 21/48 (LoVo, J82, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.803×** | -3.2 | 0.054 | 19/49 (SNU-423, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.809×** | -3.1 | 0.070 | 25/48 (H4, SW 1088, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7029. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 139 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.241× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 117 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.341× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.553× (z -8.9) |
| [[LS 180 (line)]] | wt | 59.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.304× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 87.0 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.51× (z +12.8) ⚠ cell-cycle shift, explains ~45% of this change | [[Dinaciclib (drug)]] 5 µM 0.314× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 68.0 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.322× (z -11.7) |
| [[SHP-77 (line)]] | alt | 50.0 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.253× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -9.1) |
| [[A-427 (line)]] | wt | 55.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -16.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 123 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.551× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 105 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -14.5) |
| [[HEC-1-A (line)]] | alt | 67.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.40× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -10.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 116 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -13.5) |
| [[KATO III (line)]] | alt | 75.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.263× (z -11.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 55.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -8.6) ⚠ cell-cycle shift, explains ~45% of this change |
| [[BT-474 (line)]] | alt | 44.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.120× (z -15.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 59.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0793× (z -18.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.468× (z -9.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 93.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -10.0) |
| [[LoVo (line)]] | wt | 76.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -9.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 57.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 70.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.153× (z -16.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 57.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 90.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 94.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -10.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.329× (z -11.9) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 203 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -9.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 89.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 90.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 83.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 68.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 115 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 153 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 49.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 57.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 52.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7029), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTY2D1]] | +0.84 | +0.82 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[ACBD3]] | +0.81 | +0.78 / +0.82 | both halves | 7e-06 |  |
| [[GOLGA5]] | +0.78 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[SRP54]] | +0.77 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[OSBP]] | +0.77 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[MTF1]] | +0.73 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[COPB1]] | +0.73 | +0.73 / +0.67 | both halves | 7e-06 | STRING 443 |
| [[SSR2]] | +0.72 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[NRBF2]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.71 | +0.61 / +0.76 | both halves | 7e-06 |  |
| [[RARS1]] | +0.70 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[TBC1D23]] | +0.70 | +0.79 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBC1D8B]] | B | TBC1D8B activity raises YIPF5's level | lines that do not express TBC1D8B (6) vs lines expressing it (44) | 1.40× lower at baseline in the lines without TBC1D8B | 0.063 | ⚠ within organs, on part of the lines; also absent: AHR, MYO1B, RND3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.826). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (11.7, -36.7); signed map (-50.5, 13.1). **Vector** length 144, 47.1% of its response variance represented; |z| ≥ 3 in 872 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Intra-Golgi and retrograde Golgi-to-ER traffic* (reactome, mean cos +0.52 to 12); *Asparagine N-linked glycosylation* (reactome, mean cos +0.57 to 12); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.60 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.1 | +6.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.2 | +5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.1 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +4.5 | +2.4 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.2 | +2.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -7.4 | -7.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.2 | -9.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.1 | -7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.6 | -7.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.3 | -6.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.6 | -3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | -2.7 | -1.2 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -2.5 | -2.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -2.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | Yip1 domain family member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:144,158,162-144,170,714 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SMAP-5, FinGER5, Yip1a, YIPFalpha1A |
| Gene groups (HGNC) | Yip1 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969M3](https://www.uniprot.org/uniprotkb/Q969M3) (Protein YIPF5):

> Plays a role in transport between endoplasmic reticulum and Golgi. In pancreatic beta cells, required to transport pro-insulin from endoplasmic reticulum into the Golgi.

**Summary**, from NCBI Gene [81555](https://www.ncbi.nlm.nih.gov/gene/81555):

> Involved in insulin processing and regulation of ER to Golgi vesicle-mediated transport. Located in Golgi apparatus and endoplasmic reticulum. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24877](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24877) · Entrez [81555](https://www.ncbi.nlm.nih.gov/gene/81555) · UniProt [Q969M3](https://www.uniprot.org/uniprotkb/Q969M3) · Ensembl [ENSG00000145817](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145817)

## Data

Gene col 7029: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7029); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7029, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7029]; `tensor/DDL_lfc|DDL_z.npy` [7029]; `embed/gene_vectors.npy` [7029]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7029 or target_col == 7029). Every well: [[YIPF5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YIPF5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
