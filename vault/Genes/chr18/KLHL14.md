---
symbol: "KLHL14"
type: "gene"
col: 12444
ensembl_id: "ENSG00000197705"
name: "kelch like family member 14"
location: "18q12.1"
module: 10
arm: "+"
pooled_cpm: 2.32
n_lines_expressing: 13
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 15
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# KLHL14

*kelch like family member 14* — 18q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.79× (z +14.9, q 0e+00, up in 3 of 5 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.237×); [[Bortezomib (drug)]] 0.05 µM in 1 line (PANC-1 0.160×; ⚠ cell-cycle shift, explains ~11% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (PANC-1 0.228×; ⚠ transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.0914×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD20A21P]] (+0.58, fdr 2e-05), [[TTPA]] (+0.55, fdr 2e-05), [[CARD18]] (+0.54, fdr 1e-05); moves opposite to [[BICDL1]] (-0.43, fdr 4e-04), [[FRMD8]] (-0.39, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FGF20]] → it (grade C ⚠); 15 go from it, the strongest it → [[ADAM22]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12444.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.79×** | +14.9 | 0e+00 | 3/5 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.17×** | +10.6 | 7e-24 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.80×** | +9.0 | 6e-17 | 1/5 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.91×** | +8.5 | 3e-15 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.40×** | +8.3 | 1e-14 | 3/11 (NCI-H23, SHP-77, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.82×** | +5.7 | 1e-06 | 3/11 (RKO, HepG2/C3A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.25×** | +5.7 | 1e-06 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.12×** | +5.1 | 3e-05 | 2/10 (NCI-H23, RKO) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +5.0 | 4e-05 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.14×** | +4.9 | 5e-05 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.99×** | +4.6 | 2e-04 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +4.6 | 2e-04 | 3/8 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +4.5 | 3e-04 | 0/7 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +4.4 | 4e-04 | 1/8 (A-427) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.37×** | +4.1 | 0.001 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +4.1 | 0.002 | 1/8 (SW480) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.75×** | +3.7 | 0.006 | 2/8 (HepG2/C3A, PANC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.72×** | +3.6 | 0.008 | 2/10 (LOX-IMVI, NCI-H23) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.63×** | +3.3 | 0.030 | 0/8 | inconsistent across doses | low cells (technical?) |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.030 | 0/10 | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.53×** | +2.9 | 0.097 | 0/7 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12444.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.237×); [[Bortezomib (drug)]] 0.05 µM in 1 line (PANC-1 0.160×; ⚠ cell-cycle shift, explains ~11% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (PANC-1 0.228×; ⚠ transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.0914×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | 0.595× | -3.5 | 0.25 | 1/11 (PANC-1) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.641× | -3.0 | 0.62 | 1/11 (RKO) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12444. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -12.7) |
| [[A-427 (line)]] | wt | 8.68 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0914× (z -9.1) |
| [[A-172 (line)]] | wt | 0.268 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.269 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.273 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.312 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.337 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.279 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.569 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.302 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.331 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.339 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.252 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.279 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.242 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.246 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.229 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.817 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.331 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.289 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.403 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.336 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.339 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12444), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD20A21P]] | +0.58 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[TTPA]] | +0.55 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[CARD18]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[FGF20]] | +0.53 | +0.42 / +0.40 | both halves | 5e-05 |  |
| [[COLGALT2]] | +0.53 | +0.54 / +0.25 | both halves | 4e-04 |  |
| [[HOXC4]] | +0.52 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[LINC00466]] | +0.52 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[CTNNA2]] | +0.52 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[TBX1]] | +0.51 | +0.38 / +0.43 | both halves | 6e-05 |  |
| [[TMCC1-DT]] | +0.50 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[DLX6-AS1]] | +0.49 | +0.54 / +0.32 | both halves | 2e-04 |  |
| [[PDE3B]] | +0.49 | +0.46 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BICDL1]] | -0.43 | -0.42 / -0.24 | both halves | 4e-04 |  |
| [[FRMD8]] | -0.39 | -0.37 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGF20]] | C | FGF20 activity raises KLHL14's level | lines that do not express FGF20 (41) vs lines expressing it (9) | 1.95× lower at baseline in the lines without FGF20 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, HEPHL1, GCG; co-absent with the target |
| [[JPH3]] | C | JPH3 activity raises KLHL14's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 1.08× lower at baseline in the lines without JPH3 | 0.081 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 10, C 5. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM22]] | B | KLHL14 activity raises ADAM22's level | lines that do not express KLHL14 (37) vs lines expressing it (13) | 2.34× lower at baseline in the lines without KLHL14 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55 |
| [[TMCC1-DT]] | B | KLHL14 activity raises TMCC1-DT's level | lines that do not express KLHL14 (37) vs lines expressing it (13) | 1.47× lower at baseline in the lines without KLHL14 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55 |
| [[MTERF2]] | B | KLHL14 activity raises MTERF2's level | lines that do not express KLHL14 (37) vs lines expressing it (13) | 1.33× lower at baseline in the lines without KLHL14 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55 |
| [[KCNQ5]] | B | KLHL14 activity weakens KCNQ5's drug response | lines that do not express KLHL14 (16) vs lines expressing it (8) | the lines without KLHL14 respond 1.97× as strongly (z diff -1.44); strongest at Dinaciclib 5 µM: 1.05x vs 0.45x (z diff -6.3) | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55; target measured in part of the lines; both ways; artifact flags |
| [[GCAWKR]] | B | KLHL14 activity strengthens GCAWKR's drug response | lines that do not express KLHL14 (21) vs lines expressing it (5) | the lines without KLHL14 respond 0.48× as strongly (z diff +1.84); strongest at Harringtonine 5 µM: 0.33x vs 0.16x (z diff +3.7) | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55; target measured in part of the lines; the reference differs; artifact flags |
| [[MYT1]] | B | KLHL14 activity raises MYT1's level | lines that do not express KLHL14 (37) vs lines expressing it (13) | 2.08× lower at baseline in the lines without KLHL14 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55 |
| [[TMCC1-DT]] | B | KLHL14 activity strengthens TMCC1-DT's drug response | lines that do not express KLHL14 (33) vs lines expressing it (11) | the lines without KLHL14 respond 0.61× as strongly (z diff +1.19); strongest at Harringtonine 5 µM: 0.46x vs 0.28x (z diff +2.7) | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55; target measured in part of the lines; artifact flags |
| [[CACHD1]] | B | KLHL14 activity raises CACHD1's level | lines that do not express KLHL14 (37) vs lines expressing it (13) | 1.55× lower at baseline in the lines without KLHL14 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55 |
| [[FTCDNL1]] | B | KLHL14 activity raises FTCDNL1's level | lines that do not express KLHL14 (37) vs lines expressing it (13) | 1.76× lower at baseline in the lines without KLHL14 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55 |
| [[F10]] | B | KLHL14 activity raises F10's level | lines that do not express KLHL14 (37) vs lines expressing it (13) | 1.93× lower at baseline in the lines without KLHL14 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55 |
| [[CARD18]] | C | KLHL14 activity raises CARD18's level | lines that do not express KLHL14 (37) vs lines expressing it (13) | 1.99× lower at baseline in the lines without KLHL14 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55; co-absent with the target |
| [[ANKRD20A21P]] | C | KLHL14 activity raises ANKRD20A21P's level | lines that do not express KLHL14 (37) vs lines expressing it (13) | 1.74× lower at baseline in the lines without KLHL14 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.274). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (20.2, 42.8); signed map (61.0, 18.8). **Vector** length 28.5, 7.13% of its response variance represented; |z| ≥ 3 in 283 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +14.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.4 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.4 | +8.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.3 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +0.7 | +0.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.7 | +2.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +0.7 | +0.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -0.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.7 | -2.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.7 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.6 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -0.6 | +0.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.1 — chr18:32,672,673-32,773,023 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1384 |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Matched by | ensembl_id |

UniProt [Q9P2G3](https://www.uniprot.org/uniprotkb/Q9P2G3) carries no function annotation.

**Summary**, from NCBI Gene [57565](https://www.ncbi.nlm.nih.gov/gene/57565):

> The protein encoded by this gene is a member of the Kelch-like gene family, whose members contain a BTB/POZ domain, a BACK domain, and several Kelch domains. The encoded protein possesses six Kelch domains and localizes to the endoplasmic reticulum, where it interacts with torsin-1A. [provided by RefSeq, Sep 2015]

**Accessions** — [HGNC:29266](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29266) · Entrez [57565](https://www.ncbi.nlm.nih.gov/gene/57565) · UniProt [Q9P2G3](https://www.uniprot.org/uniprotkb/Q9P2G3) · Ensembl [ENSG00000197705](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197705)

## Data

Gene col 12444: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12444); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12444, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12444]; `tensor/DDL_lfc|DDL_z.npy` [12444]; `embed/gene_vectors.npy` [12444]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12444 or target_col == 12444). Every well: [[KLHL14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
