---
symbol: "POU2F2"
type: "gene"
col: 384
ensembl_id: "ENSG00000028277"
name: "POU class 2 homeobox 2"
location: "19q13.2"
module: 38
arm: "+"
pooled_cpm: 27.57
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 21
n_dd_up_clean: 12
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# POU2F2

*POU class 2 homeobox 2* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.36× (z +11.9, q 9e-30, up in 37 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.535× (z -6.2, q 3e-07, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ORAI2]] (+0.71, fdr 7e-06), [[MIR9-1HG]] (+0.70, fdr 7e-06), [[PDE2A]] (+0.69, fdr 7e-06); moves opposite to [[ARMC8]] (-0.59, fdr 3e-05), [[CHPT1]] (-0.56, fdr 1e-05), [[KCTD3]] (-0.55, fdr 1e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[RFX8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 384.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +11.9 | 9e-30 | 37/44 (A549, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.47×** | +8.9 | 2e-16 | 30/45 (A-172, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.16×** | +7.6 | 8e-12 | 29/44 (HepG2/C3A, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.63×** | +6.8 | 2e-09 | 31/47 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.92×** | +6.4 | 2e-08 | 28/47 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.95×** | +6.2 | 6e-08 | 30/43 (HT-29, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +5.5 | 3e-06 | 29/44 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.67×** | +5.1 | 3e-05 | 23/47 (A549, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +4.6 | 2e-04 | 23/47 (A549, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +4.6 | 3e-04 | 26/47 (A549, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.037 | 22/45 (LoVo, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **1.89×** | +3.3 | 0.049 | 14/43 (SW480, NCI-H2347, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 384.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.535×** | -6.2 | 3e-07 | 23/47 (KATO III, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.645×** | -4.3 | 0.004 | 25/47 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.651×** | -4.3 | 0.004 | 22/47 (SW480, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.654×** | -4.2 | 0.004 | 25/47 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.457×** | -4.1 | 0.006 | 25/41 (COLO 205, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.667×** | -4.0 | 0.006 | 22/47 (SNU-423, RPMI-7951, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.684×** | -3.8 | 0.012 | 19/47 (HOP62, hTERT-HPNE, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.674×** | -3.8 | 0.012 | 21/40 (COLO 205, SW 900, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.488×** | -3.7 | 0.013 | 19/44 (SW 900, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.697×** | -3.6 | 0.019 | 20/47 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | **0.777×** | -3.5 | 0.021 | 18/47 (AsPC-1, RPMI-7951, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.687×** | -3.4 | 0.027 | 20/47 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.764×** | -3.4 | 0.034 | 18/46 (HOP62, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.701×** | -3.3 | 0.036 | 21/45 (H4, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.708×** | -3.3 | 0.037 | 18/46 (HOP62, RPMI-7951, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.714×** | -3.2 | 0.042 | 17/45 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM |  | **0.796×** | -3.2 | 0.044 | 10/47 (NCI-H661, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 384. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 94.9 | 0 | 13 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.459× (z -15.6) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 0.5 µM 0.125× (z -11.6) |
| [[KATO III (line)]] | alt | 56.8 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0297× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.120× (z -13.4) |
| [[HT-29 (line)]] | alt | 48.1 | 1 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 5.20× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 14.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.182× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 9.39 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.90× (z +10.8) | — |
| [[COLO 205 (line)]] | alt | 152 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.159× (z -10.5) ⚠ toxic · without an alert: [[venetoclax (drug)]] 5 µM 0.0530× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 21.9 | 2 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 8.32× (z +9.4) | [[Pimozide (drug)]] 0.05 µM 0.0994× (z -10.3) |
| [[A-172 (line)]] | wt | 14.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 19.0× (z +16.2) | — |
| [[BT-474 (line)]] | alt | 14.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 9.99× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 16.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 8.20× (z +10.6) | — |
| [[LoVo (line)]] | wt | 36.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +14.6) | — |
| [[NCI-H2347 (line)]] | alt | 16.4 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.02× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 27.6 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.46× (z +8.8) | — |
| [[SW480 (line)]] | alt | 24.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.40× (z +11.6) | — |
| [[A549 (line)]] | wt | 20.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.89× (z +16.1) | — |
| [[CFPAC-1 (line)]] | alt | 34.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0366× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 28.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 21.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +14.4) | — |
| [[NCI-H2030 (line)]] | alt | 22.8 | 0 | 1 | — | [[Simotinib (drug)]] 0.5 µM 0.169× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 20.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 9.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 21.2 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.147× (z -8.7) |
| [[SW 900 (line)]] | alt | 50.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.125× (z -10.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW48 (line)]] | wt | 19.5 | 0 | 1 | — | [[Clofarabine (drug)]] 0.05 µM 0.0698× (z -9.8) |
| [[A-427 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.28 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 384), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ORAI2]] | +0.71 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[PDE2A]] | +0.69 | +0.65 / +0.73 | both halves | 7e-06 | same gene group |
| [[WNT2B]] | +0.69 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.69 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[LINC01588]] | +0.69 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[ACVR1C]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[LINC01619]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[SHANK1]] | +0.66 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[PHKG1]] | +0.65 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[LINC01291]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[LAT2]] | +0.64 | +0.68 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC8]] | -0.59 | -0.46 / -0.66 | both halves | 3e-05 |  |
| [[CHPT1]] | -0.56 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[KCTD3]] | -0.55 | -0.55 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RFX8]] | B | RFX8 activity raises POU2F2's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.97× lower at baseline in the lines without RFX8 | 1e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[RFX8]] | B | RFX8 activity weakens POU2F2's drug response | lines that do not express RFX8 (34) vs lines expressing it (13) | the lines without RFX8 respond 2.22× as strongly (z diff -1.91); strongest at Idarubicin (hydrochloride) 5 µM: 2.90x vs 1.14x (z diff -5.4) | 0.006 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN; target measured in part of the lines; artifact flags |
| [[NLRP1]] | B | NLRP1 activity raises POU2F2's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 1.97× lower at baseline in the lines without NLRP1 | 0.006 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12 |
| [[LSMEM2]] | B | LSMEM2 activity raises POU2F2's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 2.39× lower at baseline in the lines without LSMEM2 | 0.012 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[FHAD1]] | B | FHAD1 activity raises POU2F2's level | lines that do not express FHAD1 (14) vs lines expressing it (36) | 2.02× lower at baseline in the lines without FHAD1 | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC01798, LINC01426; maybe low, not absent |
| [[LINC01705]] | B | LINC01705 activity raises POU2F2's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 1.47× lower at baseline in the lines without LINC01705 | 0.047 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137 |
| [[NR3C1]] | B | NR3C1 activity lowers POU2F2's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[RDUR]] | B | RDUR activity raises POU2F2's level | lines that do not express RDUR (28) vs lines expressing it (22) | 1.79× lower at baseline in the lines without RDUR | 0.055 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LNCOG, ENSG00000287622, GYPC |
| [[IL11]] | B | IL11 activity raises POU2F2's level | lines that do not express IL11 (27) vs lines expressing it (23) | 1.56× lower at baseline in the lines without IL11 | 0.062 | ⚠ within organs, on part of the lines; also absent: EDNRA, LINC00973, LINC01583 |
| [[FES]] | B | FES activity raises POU2F2's level | lines that do not express FES (11) vs lines expressing it (39) | 2.00× lower at baseline in the lines without FES | 0.063 | ⚠ within organs, on part of the lines; also absent: RBPMS, GLRX, SEMA4A; maybe low, not absent |
| [[OAF]] | C | OAF activity raises POU2F2's level | lines that do not express OAF (4) vs lines expressing it (46) | 2.30× lower at baseline in the lines without OAF | 0.097 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL3, LRP1, ALPK1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.694). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.4, -11.6); signed map (18.7, 16.4). **Vector** length 129, 36.5% of its response variance represented; |z| ≥ 3 in 1,298 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.8 | +8.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +11.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +5.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.3 | +6.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.0 | +3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.7 | +2.6 |
|  | [[Vilanterol (drug)]] 5 µM |  | +3.5 | +1.0 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -5.2 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.1 | -3.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -2.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.8 | -4.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -4.8 | -4.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.5 | -4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.4 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | POU class 2 homeobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:42,086,110-42,196,585 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OCT2; previously OTF2 |
| Gene groups (HGNC) | POU class homeoboxes and pseudogenes; MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: Differentiation of naive CD4+ T cells to T helper 2 cells (Th2 cells); RNA polymerase II transcribes snRNA genes; Differentiation of T cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P09086](https://www.uniprot.org/uniprotkb/P09086) (POU domain, class 2, transcription factor 2):

> Transcription factor that specifically binds to the octamer motif (5'-ATTTGCAT-3'). Regulates IL6 expression in B cells with POU2AF1 (By similarity). Regulates transcription in a number of tissues in addition to activating immunoglobulin gene expression. Modulates transcription transactivation by NR3C1, AR and PGR.; [Isoform 5]: Activates the U2 small nuclear RNA (snRNA) promoter.

**Summary**, from NCBI Gene [5452](https://www.ncbi.nlm.nih.gov/gene/5452):

> The protein encoded by this gene is a homeobox-containing transcription factor of the POU domain family. The encoded protein binds the octamer sequence 5'-ATTTGCAT-3', a common transcription factor binding site in immunoglobulin gene promoters. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:9213](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9213) · Entrez [5452](https://www.ncbi.nlm.nih.gov/gene/5452) · UniProt [P09086](https://www.uniprot.org/uniprotkb/P09086) · Ensembl [ENSG00000028277](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000028277)

## Data

Gene col 384: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 384); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 384, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 384]; `tensor/DDL_lfc|DDL_z.npy` [384]; `embed/gene_vectors.npy` [384]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 384 or target_col == 384). Every well: [[POU2F2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POU2F2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
