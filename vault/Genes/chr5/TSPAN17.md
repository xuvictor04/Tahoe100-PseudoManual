---
symbol: "TSPAN17"
type: "gene"
col: 530
ensembl_id: "ENSG00000048140"
name: "tetraspanin 17"
location: "5q35.2"
module: 2
arm: "+"
pooled_cpm: 13.2
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 6
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# TSPAN17

*tetraspanin 17* — 5q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.93× (z +11.2, q 2e-26, up in 23 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.40× (z +8.1, q 2e-13, up in 27 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.325× (z -27.2, q 0e+00, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GIT1]] (+0.68, fdr 7e-06), [[RNF38]] (+0.68, fdr 7e-06), [[SRPK2]] (+0.66, fdr 1e-05); moves opposite to [[PEX12]] (-0.64, fdr 4e-05), [[HELQ]] (-0.62, fdr 4e-05), [[RBM23]] (-0.61, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MFAP3L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 530.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.93×** | +11.2 | 2e-26 | 23/38 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +8.1 | 2e-13 | 27/46 (A549, RKO, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +7.6 | 7e-12 | 16/24 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +6.6 | 5e-09 | 23/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.46×** | +6.4 | 1e-08 | 22/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +5.9 | 3e-07 | 20/40 (HEC-1-A, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +5.7 | 7e-07 | 20/45 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.39×** | +5.7 | 1e-06 | 20/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.6 | 1e-06 | 15/48 (LS 180, NCI-H23, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +5.4 | 5e-06 | 15/47 (HCT15, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **1.36×** | +5.0 | 3e-05 | 18/40 (LoVo, SW 900, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.30×** | +4.4 | 5e-04 | 13/45 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.29×** | +4.3 | 7e-04 | 10/46 (SW1417, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.29×** | +4.2 | 0.001 | 17/45 (A498, NCI-H23, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.39×** | +4.0 | 0.002 | 7/41 (MIA PaCa-2, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.007 | 6/37 (LoVo, C-33 A, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.7 | 0.008 | 11/48 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.008 | 9/44 (PANC-1, COLO 205, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.4 | 0.018 | 12/48 (A-427, Hs 766T, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +3.2 | 0.039 | 7/47 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.058 | 5/47 (NCI-H2030, SW 900, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.19× | +2.9 | 0.093 | 9/47 (RKO, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 530.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.325×** | -27.2 | 0e+00 | 39/46 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.449×** | -13.7 | 3e-40 | 36/46 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.600×** | -8.4 | 8e-15 | 28/47 (J82, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.392×** | -8.4 | 9e-15 | 30/47 (LoVo, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.517×** | -5.9 | 4e-07 | 20/43 (LoVo, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.802×** | -3.8 | 0.015 | 6/48 (PANC-1, SW1417, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.713× | -3.0 | 0.20 | 5/46 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 530. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 14.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -22.7) |
| [[A-172 (line)]] | wt | 24.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -18.5) |
| [[A549 (line)]] | wt | 14.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -15.0) |
| [[C-33 A (line)]] | alt | 15.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -10.1) |
| [[HS-578T (line)]] | alt | 16.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -13.4) |
| [[J82 (line)]] | alt | 12.5 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.152× (z -11.0) |
| [[LoVo (line)]] | wt | 19.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -20.4) |
| [[LOX-IMVI (line)]] | wt | 13.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 11.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -18.5) |
| [[RKO (line)]] | wt | 14.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 22.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -13.5) |
| [[A-427 (line)]] | wt | 22.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -13.4) |
| [[BT-474 (line)]] | alt | 14.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -10.1) |
| [[C32 (line)]] | wt | 11.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -8.9) |
| [[HCT15 (line)]] | alt | 9.54 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 16.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -11.4) |
| [[HepG2_C3A (line)]] | wt | 11.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -8.7) |
| [[HOP62 (line)]] | alt | 9.33 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -13.4) |
| [[Hs 766T (line)]] | wt | 9.01 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -13.5) |
| [[HT-29 (line)]] | alt | 10.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -9.0) |
| [[LS 180 (line)]] | wt | 10.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -13.8) |
| [[NCI-H23 (line)]] | alt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 21.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 13.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 5.22 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -10.3) |
| [[SW 900 (line)]] | alt | 16.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -10.3) |
| [[A498 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 530), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GIT1]] | +0.68 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[RNF38]] | +0.68 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[SRPK2]] | +0.66 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[SLC27A4]] | +0.66 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[INPP4A]] | +0.66 | +0.71 / +0.39 | both halves | 5e-05 |  |
| [[UBE2F]] | +0.65 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[TBC1D24]] | +0.64 | +0.70 / +0.43 | both halves | 3e-05 |  |
| [[CORO7]] | +0.64 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[TESK1]] | +0.64 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[MIIP]] | +0.63 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[SGPP1]] | +0.63 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[MAST2]] | +0.63 | +0.69 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX12]] | -0.64 | -0.72 / -0.42 | both halves | 4e-05 |  |
| [[HELQ]] | -0.62 | -0.70 / -0.41 | both halves | 4e-05 |  |
| [[RBM23]] | -0.61 | -0.68 / -0.41 | both halves | 4e-05 |  |
| [[MYSM1]] | -0.60 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[OCIAD1]] | -0.60 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[NDUFA5]] | -0.59 | -0.68 / -0.51 | both halves | 1e-05 |  |
| [[ZNF585A]] | -0.59 | -0.69 / -0.34 | both halves | 1e-04 |  |
| [[PAN2]] | -0.59 | -0.67 / -0.36 | both halves | 9e-05 |  |
| [[ICE2]] | -0.59 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[LINC00174]] | -0.58 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[AIMP1]] | -0.58 | -0.63 / -0.37 | both halves | 8e-05 |  |
| [[GOSR1]] | -0.58 | -0.70 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MFAP3L]] | B | MFAP3L activity raises TSPAN17's level | lines that do not express MFAP3L (9) vs lines expressing it (41) | 1.50× lower at baseline in the lines without MFAP3L | 0.028 | ⚠ within organs, on part of the lines; also absent: CRACD, FILIP1, TSPAN33; maybe low, not absent |
| [[CTXN1]] | B | CTXN1 activity raises TSPAN17's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 1.44× lower at baseline in the lines without CTXN1 | 0.055 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |
| [[TP53I13]] | C | TP53I13 activity lowers TSPAN17's level | lines that do not express TP53I13 (4) vs lines expressing it (46) | 1.35× higher at baseline in the lines without TP53I13 | 0.082 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SLC25A37; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.626). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-10.4, -7.2); signed map (-44.5, -6.3). **Vector** length 77.1, 14.2% of its response variance represented; |z| ≥ 3 in 807 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +3.7 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +2.9 | +5.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.8 | +1.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.8 | +5.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.3 | +4.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.4 | -27.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.6 | -13.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.9 | -8.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.0 | -8.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -5.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | tetraspanin 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.2 — chr5:176,647,387-176,659,054 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FBX23; previously FBXO23, TM4SF17 |
| Gene groups (HGNC) | Tetraspanin family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FV3](https://www.uniprot.org/uniprotkb/Q96FV3) (Tetraspanin-17):

> Part of TspanC8 subgroup, composed of 6 members that interact with the transmembrane metalloprotease ADAM10. This interaction is required for ADAM10 exit from the endoplasmic reticulum and for enzymatic maturation and trafficking to the cell surface as well as substrate specificity. Different TspanC8/ADAM10 complexes have distinct substrates. Seems to regulate VE-cadherin expression in endothelial cells probably through interaction with ADAM10, promoting leukocyte transmigration.

**Summary**, from NCBI Gene [26262](https://www.ncbi.nlm.nih.gov/gene/26262):

> This gene encodes a member of the transmembrane 4 superfamily. It is characterized by four tetraspanin transmembrane segments. The function of this gene has not yet been determined. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:13594](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13594) · Entrez [26262](https://www.ncbi.nlm.nih.gov/gene/26262) · UniProt [Q96FV3](https://www.uniprot.org/uniprotkb/Q96FV3) · Ensembl [ENSG00000048140](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000048140)

## Data

Gene col 530: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 530); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 530, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 530]; `tensor/DDL_lfc|DDL_z.npy` [530]; `embed/gene_vectors.npy` [530]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 530 or target_col == 530). Every well: [[TSPAN17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSPAN17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
