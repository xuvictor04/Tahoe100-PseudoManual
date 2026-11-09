---
symbol: "PKD1L2"
type: "gene"
col: 9315
ensembl_id: "ENSG00000166473"
name: "polycystin 1 like 2 (gene/pseudogene)"
location: "16q23.2"
module: 75
arm: "+"
pooled_cpm: 7.24
n_lines_expressing: 37
n_dd_up: 36
n_dd_down: 1
n_dd_up_clean: 31
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 8
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# PKD1L2

*polycystin 1 like 2 (gene/pseudogene)* — 16q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.86× (z +14.9, q 0e+00, up in 19 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.669× (z -4.1, q 0.028, down in 14 of 33 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HepG2/C3A 0.159×, SNU-423 0.291×); [[Digitoxin (drug)]] 5 µM in 1 line (HepG2/C3A 0.0254×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0695×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Ponatinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.122×); [[Homoharringtonine (drug)]] 5 µM in 1 line (Panc 03.27 0.195×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CUTA]] (+0.57, fdr 1e-05), [[CLDN14]] (+0.57, fdr 3e-05), [[NDUFV2-AS1]] (+0.56, fdr 1e-05); moves opposite to [[CSE1L]] (-0.51, fdr 3e-05), [[TTI1]] (-0.50, fdr 3e-05), [[MCM6]] (-0.50, fdr 3e-05).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DCDC2]] → it (grade B ⚠); 8 go from it, the strongest it → [[WDSUB1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9315.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.86×** | +14.9 | 0e+00 | 19/29 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.91×** | +13.2 | 4e-37 | 5/10 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.92×** | +10.8 | 1e-24 | 12/21 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +9.6 | 9e-20 | 16/29 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.93×** | +9.3 | 1e-18 | 21/32 (NCI-H460, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.96×** | +6.8 | 1e-09 | 14/33 (MIA PaCa-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.05×** | +6.7 | 2e-09 | 2/12 (Panc 03.27, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.87×** | +6.3 | 3e-08 | 16/32 (MIA PaCa-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.75×** | +5.6 | 1e-06 | 18/33 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.70×** | +5.3 | 6e-06 | 13/31 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +5.1 | 2e-05 | 13/27 (A-172, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +4.9 | 4e-05 | 13/31 (MIA PaCa-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.36×** | +4.4 | 5e-04 | 11/31 (SNU-1, MIA PaCa-2, …) | top dose only |  |
| [[Temsirolimus (drug)]] 5 µM |  | **1.36×** | +4.3 | 6e-04 | 12/32 (SW480, A549, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +4.3 | 6e-04 | 11/32 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.35×** | +4.3 | 6e-04 | 9/32 (A549, NCI-H2030, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +4.3 | 7e-04 | 7/31 (A-172, HOP62, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.78×** | +4.1 | 0.001 | 3/26 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9315.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HepG2/C3A 0.159×, SNU-423 0.291×); [[Digitoxin (drug)]] 5 µM in 1 line (HepG2/C3A 0.0254×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0695×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Ponatinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.122×); [[Homoharringtonine (drug)]] 5 µM in 1 line (Panc 03.27 0.195×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.669×** | -4.1 | 0.028 | 14/33 (MIA PaCa-2, SNU-1, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.714× | -3.4 | 0.14 | 10/31 (NCI-H2030, SW480, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | 0.526× | -3.4 | 0.14 | 7/29 (SNU-1, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.729× | -3.2 | 0.18 | 12/31 (HepG2/C3A, SNU-423, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 0.731× | -3.2 | 0.18 | 10/33 (SNU-423, H4, …) | top dose only |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | 0.740× | -3.0 | 0.23 | 4/31 (Panc 03.27, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9315. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 96.2 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0254× (z -20.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -14.7) |
| [[MIA PaCa-2 (line)]] | alt | 20.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.89× (z +13.5) | — |
| [[SNU-423 (line)]] | alt | 29.0 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0737× (z -13.0) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -8.7) |
| [[A-172 (line)]] | wt | 7.71 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.7× (z +17.1) | — |
| [[A549 (line)]] | wt | 18.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 7.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.89× (z +11.3) | — |
| [[Panc 03.27 (line)]] | alt | 19.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +10.2) | — |
| [[A-427 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 13.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9315), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CUTA]] | +0.57 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[CLDN14]] | +0.57 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[NDUFV2-AS1]] | +0.56 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[LINC02154]] | +0.56 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[RRAGC-DT]] | +0.55 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[MIR4300HG]] | +0.54 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[SMDT1]] | +0.53 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[KCP]] | +0.53 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[LYST]] | +0.53 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[TSC1]] | +0.52 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[KIF6]] | +0.52 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[UAP1L1]] | +0.52 | +0.51 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSE1L]] | -0.51 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[TTI1]] | -0.50 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[MCM6]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[TUBG1]] | -0.49 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[PA2G4]] | -0.49 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[VRK1]] | -0.49 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ALMS1]] | -0.49 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[NUP205]] | -0.49 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[NUP155]] | -0.48 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[PRKDC]] | -0.48 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[BLTP2]] | -0.48 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[TOPBP1]] | -0.47 | -0.55 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCDC2]] | B | DCDC2 activity raises PKD1L2's level | lines that do not express DCDC2 (25) vs lines expressing it (25) | 1.68× lower at baseline in the lines without DCDC2 | 0.055 | ⚠ within organs, on part of the lines; also absent: FXYD2, PGBD5, HAVCR1 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WDSUB1]] | B | PKD1L2 activity raises WDSUB1's level | lines that do not express PKD1L2 (13) vs lines expressing it (37) | 1.40× lower at baseline in the lines without PKD1L2 | 0.007 | ⚠ within organs, on part of the lines; also absent: SPDYE10; maybe low, not absent |
| [[CSE1L]] | B | PKD1L2 activity raises CSE1L's level | lines that do not express PKD1L2 (13) vs lines expressing it (37) | 1.33× lower at baseline in the lines without PKD1L2 | 0.044 | ⚠ within organs, on part of the lines; also absent: SPDYE10; maybe low, not absent |
| [[ITSN2]] | B | PKD1L2 activity raises ITSN2's level | lines that do not express PKD1L2 (13) vs lines expressing it (37) | 1.36× lower at baseline in the lines without PKD1L2 | 0.046 | ⚠ within organs, on part of the lines; also absent: SPDYE10; maybe low, not absent |
| [[NDUFV2-AS1]] | B | PKD1L2 activity raises NDUFV2-AS1's level | lines that do not express PKD1L2 (13) vs lines expressing it (37) | 1.23× lower at baseline in the lines without PKD1L2 | 0.056 | ⚠ within organs, on part of the lines; also absent: SPDYE10; maybe low, not absent |
| [[GEM]] | B | PKD1L2 activity lowers GEM's level | lines that do not express PKD1L2 (13) vs lines expressing it (37) | 1.79× higher at baseline in the lines without PKD1L2 | 0.074 | ⚠ within organs, on part of the lines; also absent: SPDYE10; maybe low, not absent |
| [[DCDC2]] | B | PKD1L2 activity raises DCDC2's level | lines that do not express PKD1L2 (13) vs lines expressing it (37) | 1.41× lower at baseline in the lines without PKD1L2 | 0.082 | ⚠ within organs, on part of the lines; also absent: SPDYE10; maybe low, not absent |
| [[RRAGC-DT]] | B | PKD1L2 activity raises RRAGC-DT's level | lines that do not express PKD1L2 (13) vs lines expressing it (37) | 1.50× lower at baseline in the lines without PKD1L2 | 0.083 | ⚠ within organs, on part of the lines; also absent: SPDYE10; maybe low, not absent |
| [[LINC01273]] | B | PKD1L2 activity raises LINC01273's level | lines that do not express PKD1L2 (13) vs lines expressing it (37) | 1.51× lower at baseline in the lines without PKD1L2 | 0.097 | ⚠ within organs, on part of the lines; also absent: SPDYE10; maybe low, not absent |

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.485). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.1, 23.8); signed map (34.2, 9.8). **Vector** length 78.9, 18.5% of its response variance represented; |z| ≥ 3 in 873 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +10.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +9.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +5.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +4.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -3.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.5 | -2.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.0 | -3.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | polycystin 1 like 2 (gene/pseudogene) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.2 — chr16:81,100,875-81,220,370 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1879 |
| Gene groups (HGNC) | C-type lectin domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z442](https://www.uniprot.org/uniprotkb/Q7Z442) (Polycystin-1-like protein 2):

> May function as a G protein-coupled receptor.

**Summary**, from NCBI Gene [114780](https://www.ncbi.nlm.nih.gov/gene/114780):

> This gene encodes a member of the polycystin protein family. This protein may function as a G-protein-coupled component or regulator of cation channel pores. The long isoform of this protein contains 11 transmembrane domains, a latrophilin/CL-1-like GPCR proteolytic site (GPS) domain, and a polycystin-1, lipoxygenase, alpha-toxin (PLAT) domain. Alternative splicing results in multiple transcript variants encoding distinct isoforms. This gene is a polymorphic pseudogene in humans. [provided by …

**Accessions** — [HGNC:21715](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21715) · Entrez [114780](https://www.ncbi.nlm.nih.gov/gene/114780) · UniProt [Q7Z442](https://www.uniprot.org/uniprotkb/Q7Z442) · Ensembl [ENSG00000166473](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166473)

## Data

Gene col 9315: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9315); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9315, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9315]; `tensor/DDL_lfc|DDL_z.npy` [9315]; `embed/gene_vectors.npy` [9315]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9315 or target_col == 9315). Every well: [[PKD1L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKD1L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
