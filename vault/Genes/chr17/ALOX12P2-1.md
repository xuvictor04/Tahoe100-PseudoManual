---
symbol: "ALOX12P2-1"
type: "gene"
col: 16574
ensembl_id: "ENSG00000291084"
name: ""
location: ""
module: 117
arm: "+"
pooled_cpm: 21.43
n_lines_expressing: 21
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 9
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# ALOX12P2-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.09× (z +14.3, q 2e-43, up in 16 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.710× (z -4.7, q 0.001, down in 15 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 6 lines (NCI-H1573 0.148×, HEC-1-A 0.191×, Panc 03.27 0.175×, HepG2/C3A 0.173×, …); [[Panobinostat (drug)]] 5 µM in 4 lines (NCI-H1573 0.145×, Panc 03.27 0.194×, HEC-1-A 0.284×, HepG2/C3A 0.230×; ⚠ cell-cycle shift, explains ~2% of this change); [[Belinostat (drug)]] 5 µM in 4 lines (NCI-H1573 0.216×, KATO III 0.203×, HEC-1-A 0.295×, Panc 03.27 0.237×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (Panc 03.27 0.407×, HEC-1-A 0.486×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAPS2]] (+0.76, fdr 8e-06), [[PSMD7]] (+0.72, fdr 1e-05), [[TRIM16L]] (+0.71, fdr 7e-06); moves opposite to [[GMCL1]] (-0.62, fdr 1e-04), [[SMARCD2]] (-0.59, fdr 4e-05), [[LIX1L]] (-0.59, fdr 1e-04).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLCO2B1]] → it (grade B ⚠); 9 go from it, the strongest it → [[TRIM16L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16574.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.09×** | +14.3 | 2e-43 | 16/18 (A549, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +12.5 | 2e-33 | 4/18 (HS-578T, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.39×** | +11.5 | 4e-28 | 3/13 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.24×** | +11.1 | 3e-26 | 5/18 (LoVo, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.24×** | +11.0 | 3e-26 | 17/18 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.03×** | +9.7 | 3e-20 | 17/18 (HEC-1-A, CFPAC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.09×** | +9.2 | 4e-18 | 15/17 (HEC-1-A, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.82×** | +8.2 | 1e-14 | 17/18 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +7.7 | 6e-13 | 16/18 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +6.1 | 7e-08 | 4/16 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +5.1 | 2e-05 | 1/16 (SNU-423) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.9 | 4e-05 | 6/19 (SNU-423, NCI-H1573, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.77×** | +4.8 | 9e-05 | 9/19 (HEC-1-A, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.4 | 4e-04 | 2/19 (SNU-423, HS-578T) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +4.0 | 0.002 | 5/15 (HEC-1-A, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.036 | 4/18 (NCI-H460, HS-578T, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.057 | 0/19 | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.059 | 4/17 (A549, NCI-H23, …) | top dose only |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.44×** | +3.0 | 0.075 | 0/18 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +2.9 | 0.097 | 1/18 (A498) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16574.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 6 lines (NCI-H1573 0.148×, HEC-1-A 0.191×, Panc 03.27 0.175×, HepG2/C3A 0.173×, …); [[Panobinostat (drug)]] 5 µM in 4 lines (NCI-H1573 0.145×, Panc 03.27 0.194×, HEC-1-A 0.284×, HepG2/C3A 0.230×; ⚠ cell-cycle shift, explains ~2% of this change); [[Belinostat (drug)]] 5 µM in 4 lines (NCI-H1573 0.216×, KATO III 0.203×, HEC-1-A 0.295×, Panc 03.27 0.237×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (Panc 03.27 0.407×, HEC-1-A 0.486×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.710×** | -4.7 | 0.001 | 15/18 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.917× | -4.0 | 0.018 | 2/20 (HS-578T, SW 1088) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | 0.784× | -3.3 | 0.13 | 7/17 (KATO III, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.786× | -3.3 | 0.13 | 13/18 (NCI-H1573, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.797× | -3.1 | 0.21 | 2/19 (SW 1088, CHP-212) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16574. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 138 | 4 | 4 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 5.38× (z +14.9) | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -14.8) |
| [[NCI-H1573 (line)]] | alt | 176 | 5 (1 ⚠) | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.98× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.145× (z -16.3) ⚠ cell-cycle shift, explains ~2% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.148× (z -16.1) |
| [[KATO III (line)]] | alt | 33.4 | 2 | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.24× (z +10.7) | [[Belinostat (drug)]] 5 µM 0.203× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 55.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +12.1) | — |
| [[Panc 03.27 (line)]] | alt | 90.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.175× (z -13.2) |
| [[HepG2_C3A (line)]] | wt | 140 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 30.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.158× (z -11.9) |
| [[A549 (line)]] | wt | 37.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +12.4) | — |
| [[HS-578T (line)]] | alt | 6.25 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0756× (z -9.2) |
| [[SNU-423 (line)]] | alt | 6.27 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0841× (z -8.9) |
| [[A-172 (line)]] | wt | 4.41 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.72 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.96 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.86 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.89 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.63 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.26 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.76 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.88 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.22 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.56 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.92 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.02 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16574), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPS2]] | +0.76 | +0.76 / +0.58 | both halves | 8e-06 |  |
| [[PSMD7]] | +0.72 | +0.77 / +0.55 | both halves | 1e-05 |  |
| [[TRIM16L]] | +0.71 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[PSMA4]] | +0.71 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[LRP1B]] | +0.70 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[RHBDD3]] | +0.68 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[PSMD11]] | +0.68 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[ABCC2]] | +0.68 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[GNGT1]] | +0.68 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[NQO1-DT]] | +0.68 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[NMRAL2P-1]] | +0.66 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[UBXN4]] | +0.66 | +0.67 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMCL1]] | -0.62 | -0.67 / -0.36 | both halves | 1e-04 |  |
| [[SMARCD2]] | -0.59 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[LIX1L]] | -0.59 | -0.67 / -0.33 | both halves | 1e-04 |  |
| [[POGLUT2]] | -0.58 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[SRD5A1]] | -0.58 | -0.60 / -0.39 | both halves | 5e-05 |  |
| [[FUCA1]] | -0.58 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[RAP1A]] | -0.58 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[SETD3]] | -0.57 | -0.62 / -0.39 | both halves | 6e-05 |  |
| [[PIGF]] | -0.57 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[SOCS7]] | -0.56 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[ARL3]] | -0.56 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[TMEM120B]] | -0.56 | -0.55 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLCO2B1]] | B | SLCO2B1 activity raises ALOX12P2-1's level | lines that do not express SLCO2B1 (21) vs lines expressing it (29) | 2.02× lower at baseline in the lines without SLCO2B1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000253227, ENSG00000254261, PDE1C; maybe low, not absent |
| [[CYP4F11]] | C | CYP4F11 activity raises ALOX12P2-1's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 3.50× lower at baseline in the lines without CYP4F11 | 0.002 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM16L]] | B | ALOX12P2-1 activity raises TRIM16L's level | lines that do not express ALOX12P2-1 (29) vs lines expressing it (21) | 1.63× lower at baseline in the lines without ALOX12P2-1 | 0.043 | ⚠ within organs, on part of the lines; also absent: NID2, MEG8, UNC5D; maybe low, not absent |
| [[FBXW10B]] | B | ALOX12P2-1 activity raises FBXW10B's level | lines that do not express ALOX12P2-1 (29) vs lines expressing it (21) | 1.70× lower at baseline in the lines without ALOX12P2-1 | 0.046 | ⚠ within organs, on part of the lines; also absent: NID2, MEG8, UNC5D; maybe low, not absent |
| [[TRIM16]] | B | ALOX12P2-1 activity raises TRIM16's level | lines that do not express ALOX12P2-1 (29) vs lines expressing it (21) | 1.31× lower at baseline in the lines without ALOX12P2-1 | 0.047 | ⚠ within organs, on part of the lines; also absent: NID2, MEG8, UNC5D; maybe low, not absent |
| [[TRIM16L-1]] | B | ALOX12P2-1 activity raises TRIM16L-1's level | lines that do not express ALOX12P2-1 (29) vs lines expressing it (21) | 1.55× lower at baseline in the lines without ALOX12P2-1 | 0.060 | ⚠ within organs, on part of the lines; also absent: NID2, MEG8, UNC5D; maybe low, not absent |
| [[ANKEF1]] | B | ALOX12P2-1 activity raises ANKEF1's level | lines that do not express ALOX12P2-1 (29) vs lines expressing it (21) | 1.65× lower at baseline in the lines without ALOX12P2-1 | 0.067 | ⚠ within organs, on part of the lines; also absent: NID2, MEG8, UNC5D; maybe low, not absent |
| [[ZSCAN29]] | B | ALOX12P2-1 activity raises ZSCAN29's level | lines that do not express ALOX12P2-1 (29) vs lines expressing it (21) | 1.06× lower at baseline in the lines without ALOX12P2-1 | 0.067 | ⚠ within organs, on part of the lines; also absent: NID2, MEG8, UNC5D; maybe low, not absent |
| [[CLHC1]] | B | ALOX12P2-1 activity raises CLHC1's level | lines that do not express ALOX12P2-1 (29) vs lines expressing it (21) | 1.45× lower at baseline in the lines without ALOX12P2-1 | 0.074 | ⚠ within organs, on part of the lines; also absent: NID2, MEG8, UNC5D; maybe low, not absent |
| [[MAP7]] | B | ALOX12P2-1 activity raises MAP7's level | lines that do not express ALOX12P2-1 (29) vs lines expressing it (21) | 1.55× lower at baseline in the lines without ALOX12P2-1 | 0.091 | ⚠ within organs, on part of the lines; also absent: NID2, MEG8, UNC5D; maybe low, not absent |
| [[CYP4F11]] | C | ALOX12P2-1 activity raises CYP4F11's level | lines that do not express ALOX12P2-1 (29) vs lines expressing it (21) | 2.51× lower at baseline in the lines without ALOX12P2-1 | 0.045 | ⚠ within organs, on part of the lines; also absent: NID2, MEG8, UNC5D; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.782). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-6.9, 48.0); signed map (50.2, -8.9). **Vector** length 56.6, 15.0% of its response variance represented; |z| ≥ 3 in 453 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nuclear events mediated by NFE2L2* (reactome, mean cos +0.52 to 7); *KEAP1-NFE2L2 pathway* (reactome, mean cos +0.52 to 7); *Cellular response to chemical stress* (reactome, mean cos +0.52 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +14.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.6 | +9.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.5 | +8.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.5 | +11.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +4.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +3.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.6 | -4.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.5 | -3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | -2.2 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -2.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.3 |

## What is on record

> [!warning] No registry record
> ALOX12P2-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16574: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16574); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16574, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16574]; `tensor/DDL_lfc|DDL_z.npy` [16574]; `embed/gene_vectors.npy` [16574]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16574 or target_col == 16574). Every well: [[ALOX12P2-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALOX12P2-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
