---
symbol: "DCAF7"
type: "gene"
col: 5869
ensembl_id: "ENSG00000136485"
name: "DDB1 and CUL4 associated factor 7"
location: "17q23.3"
module: 22
arm: "+"
pooled_cpm: 178.52
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# DCAF7

*DDB1 and CUL4 associated factor 7* — 17q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.68× (z +8.8, q 8e-16, up in 33 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.27× (z +6.0, q 3e-07, up in 31 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.716× (z -5.6, q 1e-05, down in 44 of 48 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.339×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC9C]] (+0.61, fdr 1e-05), [[AAMDC]] (+0.61, fdr 1e-05), [[ARID4A]] (+0.60, fdr 1e-05); moves opposite to [[PSMG1]] (-0.53, fdr 1e-05), [[TTPAL]] (-0.52, fdr 1e-04), [[RBBP8]] (-0.51, fdr 1e-04).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5869.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +8.8 | 8e-16 | 33/44 (CFPAC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.67×** | +7.1 | 3e-10 | 36/49 (SW 900, AsPC-1, …) | rises with dose | composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +6.0 | 3e-07 | 31/49 (SW1417, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.85×** | +5.7 | 2e-06 | 42/47 (NCI-H460, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.3 | 1e-05 | 36/50 (C32, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.30×** | +4.7 | 3e-04 | 29/48 (HOP62, NCI-H23, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.5 | 6e-04 | 31/48 (C32, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.007 | 30/48 (LS 180, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.23×** | +3.7 | 0.015 | 26/48 (COLO 205, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.21×** | +3.4 | 0.034 | 24/48 (COLO 205, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.035 | 25/48 (LS 180, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.050 | 26/48 (LS 180, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.057 | 22/49 (AsPC-1, CFPAC-1, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | 1.13× | +3.1 | 0.076 | 9/48 (NCI-H23, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5869.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.339×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.716×** | -5.6 | 1e-05 | 44/48 (NCI-H1792, LoVo, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.833× | -3.1 | 0.41 | 23/48 (A498, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 0.843× | -3.0 | 0.41 | 22/48 (HCT15, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5869. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 208 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.02× (z +19.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 240 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +16.6) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 150 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.78× (z +17.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +9.3) | — |
| [[C32 (line)]] | wt | 131 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 212 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.99× (z +16.2) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 113 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.47× (z +16.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 124 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HS-578T (line)]] | alt | 140 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.28× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +8.6) | — |
| [[J82 (line)]] | alt | 142 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +12.2) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 207 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.08× (z +8.9) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 158 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +16.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 180 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.49× (z +10.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 202 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.339× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[BT-474 (line)]] | alt | 112 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 165 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +10.3) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 275 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.39× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 92.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[PANC-1 (line)]] | alt | 120 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +13.8) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 103 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.55× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | — |
| [[SW48 (line)]] | wt | 134 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +8.6) | — |
| [[A-172 (line)]] | wt | 185 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 196 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 158 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 230 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 252 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 462 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 247 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 238 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 228 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 206 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 149 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 135 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 137 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 321 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5869), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC9C]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[AAMDC]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ARID4A]] | +0.60 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[CDC25C]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[TESK2]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CDK19]] | +0.57 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[PTTG1]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ZER1]] | +0.56 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[BORA]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[PRR11]] | +0.55 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[FAM193B]] | +0.55 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[CACUL1]] | +0.54 | +0.45 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMG1]] | -0.53 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[TTPAL]] | -0.52 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[RBBP8]] | -0.51 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[RABGGTB]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[ATXN7L2]] | -0.49 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[DPP3]] | -0.49 | -0.46 / -0.40 | both halves | 5e-05 | pathway: Neddylation |
| [[DPM2]] | -0.48 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[PPP2CA]] | -0.48 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[SLC35F6]] | -0.48 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[PSME3]] | -0.48 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[ZPR1]] | -0.47 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[GRWD1]] | -0.47 | -0.36 / -0.51 | both halves | 9e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DCAF7's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.385). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.7, -43.1); signed map (-53.4, -36.8). **Vector** length 104, 33.2% of its response variance represented; |z| ≥ 3 in 723 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +4.3 | +5.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.3 | +2.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +2.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.1 | +1.6 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +2.0 | +2.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.7 | -5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | -2.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | -5.0 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -4.6 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -4.3 | -3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.3 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -2.7 |
|  | [[EX229 (drug)]] 5 µM |  | -3.3 | -2.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.3 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | DDB1 and CUL4 associated factor 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.3 — chr17:63,550,222-63,594,286 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HAN11, SWAN-1; previously WDR68 |
| Gene groups (HGNC) | WD repeat domain containing; DDB1 and CUL4 associated factors |
| Reactome | 4 pathways, smallest: Association of TriC/CCT with target proteins during biosynthesis; Chaperonin-mediated protein folding; Protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [P61962](https://www.uniprot.org/uniprotkb/P61962) (DDB1- and CUL4-associated factor 7):

> Involved in craniofacial development. Acts upstream of the EDN1 pathway and is required for formation of the upper jaw equivalent, the palatoquadrate. The activity required for EDN1 pathway function differs between the first and second arches (By similarity). Associates with DIAPH1 and controls GLI1 transcriptional activity. Could be involved in normal and disease skin development. May function as a substrate receptor for CUL4-DDB1 E3 ubiquitin-protein ligase complex.

**Summary**, from NCBI Gene [10238](https://www.ncbi.nlm.nih.gov/gene/10238):

> This gene encodes a protein with multiple WD40 repeats which facilitate protein-protein interactions and thereby enable the assembly of multiprotein complexes. This protein has been shown to function as a scaffold protein for protein complexes involved in kinase signaling. This highly conserved gene is present in eukaryotic plants, fungi, and animals. The ortholog of this gene was first identified in plants as a key regulator of anthocyanin biosynthesis and flower pigmentation. Alternative …

**Accessions** — [HGNC:30915](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30915) · Entrez [10238](https://www.ncbi.nlm.nih.gov/gene/10238) · UniProt [P61962](https://www.uniprot.org/uniprotkb/P61962) · Ensembl [ENSG00000136485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136485)

## Data

Gene col 5869: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5869); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5869, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5869]; `tensor/DDL_lfc|DDL_z.npy` [5869]; `embed/gene_vectors.npy` [5869]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5869 or target_col == 5869). Every well: [[DCAF7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCAF7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
