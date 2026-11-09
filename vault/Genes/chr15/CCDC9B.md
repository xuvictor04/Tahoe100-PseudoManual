---
symbol: "CCDC9B"
type: "gene"
col: 12022
ensembl_id: "ENSG00000188549"
name: "coiled-coil domain containing 9B"
location: "15q15.1"
module: 96
arm: "+"
pooled_cpm: 11.32
n_lines_expressing: 37
n_dd_up: 13
n_dd_down: 25
n_dd_up_clean: 7
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# CCDC9B

*coiled-coil domain containing 9B* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.11× (z +10.2, q 1e-21, up in 25 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 1.67× (z +3.5, q 0.039, up in 9 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.271× (z -12.5, q 3e-33, down in 32 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HYI]] (+0.58, fdr 2e-05), [[RANGAP1]] (+0.58, fdr 3e-05), [[CCDC50]] (+0.56, fdr 1e-04); moves opposite to [[CFAP36]] (-0.54, fdr 3e-05), [[ESCO1]] (-0.54, fdr 4e-05), [[PRKRA]] (-0.52, fdr 1e-04).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINP1]] → it (grade B ⚠); 4 go from it, the strongest it → [[DDAH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12022.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.11×** | +10.2 | 1e-21 | 25/30 (SW1417, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.80×** | +9.5 | 5e-19 | 14/16 (SW1417, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.74×** | +9.0 | 6e-17 | 19/22 (SW1417, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.50×** | +3.9 | 0.012 | 14/34 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.49×** | +3.9 | 0.012 | 13/34 (HT-29, SW480, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.67×** | +3.5 | 0.039 | 9/32 (NCI-H460, LS 180, …) | rises with dose | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.061 | 7/33 (PANC-1, SK-MEL-2, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.061 | 11/32 (KATO III, LS 180, …) | two highest doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +3.3 | 0.071 | 4/21 (PANC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.60×** | +3.2 | 0.071 | 9/31 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.071 | 11/34 (PANC-1, SW480, …) | rises with dose | position effect removed |
| [[vincristine (drug)]] 5 µM |  | **1.88×** | +3.2 | 0.071 | 9/28 (SK-MEL-2, HT-29, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.079 | 7/34 (HT-29, KATO III, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12022.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.271×** | -12.5 | 3e-33 | 32/34 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.294×** | -11.8 | 2e-29 | 29/34 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.342×** | -10.3 | 1e-22 | 30/34 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.561×** | -7.8 | 6e-13 | 25/34 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.576×** | -7.5 | 9e-12 | 20/34 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.469×** | -7.3 | 4e-11 | 21/33 (NCI-H460, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.483×** | -7.0 | 3e-10 | 25/34 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.592×** | -5.0 | 4e-05 | 21/34 (Panc 03.27, HepG2/C3A, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.373×** | -5.0 | 5e-05 | 20/32 (HEC-1-A, RPMI-7951, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.604×** | -4.8 | 8e-05 | 17/34 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.400×** | -4.6 | 2e-04 | 15/31 (Panc 03.27, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.433×** | -4.2 | 0.001 | 11/30 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.636×** | -4.1 | 0.002 | 16/32 (PANC-1, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.445×** | -4.1 | 0.002 | 18/34 (SK-MEL-2, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.451×** | -4.0 | 0.002 | 13/33 (Panc 03.27, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.572×** | -3.8 | 0.005 | 15/35 (HEC-1-A, SK-MEL-2, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.691×** | -3.5 | 0.013 | 12/34 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12022. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 7.35 | 0 | 5 (2 ⚠) | — | [[Thymol (drug)]] 0.5 µM 0.0793× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 23.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -17.2) |
| [[HEC-1-A (line)]] | alt | 25.4 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.108× (z -13.4) |
| [[A-172 (line)]] | wt | 23.2 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.118× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 28.6 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -15.1) |
| [[SW1417 (line)]] | alt | 33.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +9.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -12.1) |
| [[J82 (line)]] | alt | 27.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -11.5) |
| [[LoVo (line)]] | wt | 5.59 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0965× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 14.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0123× (z -20.1) |
| [[AsPC-1 (line)]] | alt | 7.77 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0495× (z -10.9) |
| [[H4 (line)]] | wt | 14.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0623× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 12.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.120× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 30.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -10.7) |
| [[PANC-1 (line)]] | alt | 15.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -14.0) |
| [[RPMI-7951 (line)]] | alt | 16.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -9.3) |
| [[SW 900 (line)]] | alt | 7.46 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0714× (z -9.1) |
| [[A-427 (line)]] | wt | 0.775 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 9.31 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.938 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.41 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.918 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12022), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HYI]] | +0.58 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[RANGAP1]] | +0.58 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[CCDC50]] | +0.56 | +0.33 / +0.57 | both halves | 1e-04 |  |
| [[LTBP2]] | +0.56 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[ARFRP1]] | +0.55 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[WDR1]] | +0.55 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[PDCD1LG2]] | +0.55 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[RIPOR1]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[DBN1]] | +0.54 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[PIEZO1]] | +0.54 | +0.37 / +0.54 | both halves | 7e-05 |  |
| [[DDX5]] | +0.54 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[IDUA]] | +0.54 | +0.39 / +0.53 | both halves | 6e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP36]] | -0.54 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[ESCO1]] | -0.54 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[PRKRA]] | -0.52 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[FAM13A]] | -0.51 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[P4HA1]] | -0.50 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[EAF2]] | -0.50 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[ALKBH7]] | -0.50 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[PIK3C2A]] | -0.50 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[RAB6A]] | -0.48 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[RNASE4]] | -0.48 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[ABHD18]] | -0.48 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[RAB2B]] | -0.48 | -0.38 / -0.46 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINP1]] | B | LINP1 activity raises CCDC9B's level | lines that do not express LINP1 (29) vs lines expressing it (21) | 2.42× lower at baseline in the lines without LINP1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000285743, LINC00707, IGFN1 |
| [[MGLL]] | B | MGLL activity raises CCDC9B's level | lines that do not express MGLL (14) vs lines expressing it (36) | 2.31× lower at baseline in the lines without MGLL | 0.041 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[PDE1C]] | B | PDE1C activity raises CCDC9B's level | lines that do not express PDE1C (26) vs lines expressing it (24) | 1.66× lower at baseline in the lines without PDE1C | 0.098 | ⚠ within organs, on part of the lines; also absent: NTRK3, LINC02211, LINC02945 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDAH1]] | B | CCDC9B activity lowers DDAH1's level | lines that do not express CCDC9B (13) vs lines expressing it (37) | 1.90× higher at baseline in the lines without CCDC9B | 0.054 | ⚠ within organs, on part of the lines; also absent: LINC02220, COL16A1, CD22 |
| [[LAMA5]] | B | CCDC9B activity raises LAMA5's level | lines that do not express CCDC9B (13) vs lines expressing it (37) | 1.60× lower at baseline in the lines without CCDC9B | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC02220, COL16A1, CD22 |
| [[LINP1]] | B | CCDC9B activity raises LINP1's level | lines that do not express CCDC9B (13) vs lines expressing it (37) | 1.97× lower at baseline in the lines without CCDC9B | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC02220, COL16A1, CD22 |
| [[RAB2B]] | B | CCDC9B activity lowers RAB2B's level | lines that do not express CCDC9B (13) vs lines expressing it (37) | 1.24× higher at baseline in the lines without CCDC9B | 0.088 | ⚠ within organs, on part of the lines; also absent: LINC02220, COL16A1, CD22 |

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.464). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-1.3, -28.9); signed map (-5.2, 32.3). **Vector** length 84.5, 21.2% of its response variance represented; |z| ≥ 3 in 828 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +3.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.6 | +3.1 |
| fall | [[Abemaciclib (drug)]] 5 µM |  | -3.1 | -5.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -7.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -4.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.3 | -3.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 9B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:40,331,452-40,340,939 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ43339; previously C15orf52 |
| Matched by | ensembl_id |

UniProt [Q6ZUT6](https://www.uniprot.org/uniprotkb/Q6ZUT6) carries no function annotation.

**Summary**, from NCBI Gene [388115](https://www.ncbi.nlm.nih.gov/gene/388115):

> Enables RNA binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33488](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33488) · Entrez [388115](https://www.ncbi.nlm.nih.gov/gene/388115) · UniProt [Q6ZUT6](https://www.uniprot.org/uniprotkb/Q6ZUT6) · Ensembl [ENSG00000188549](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188549)

## Data

Gene col 12022: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12022); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12022, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12022]; `tensor/DDL_lfc|DDL_z.npy` [12022]; `embed/gene_vectors.npy` [12022]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12022 or target_col == 12022). Every well: [[CCDC9B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC9B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
