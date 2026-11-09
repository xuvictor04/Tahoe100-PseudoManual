---
symbol: "SMU1"
type: "gene"
col: 4366
ensembl_id: "ENSG00000122692"
name: "SMU1 DNA replication regulator and spliceosomal factor"
location: "9p21.1"
module: 25
arm: "+"
pooled_cpm: 64.1
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# SMU1

*SMU1 DNA replication regulator and spliceosomal factor* — 9p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.63× (z +12.2, q 2e-31, up in 38 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.57× (z +11.3, q 4e-27, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.794× (z -5.7, q 5e-06, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TARDBP]] (+0.75, fdr 7e-06), [[PEX19]] (+0.74, fdr 7e-06), [[SPTLC1]] (+0.72, fdr 7e-06); moves opposite to [[COX5A]] (-0.71, fdr 1e-05, ⚠ COX5A in the vector space only through flagged drug-doses), [[CDKN2D]] (-0.65, fdr 3e-05), [[RPL36]] (-0.64, fdr 5e-05), [[TBC1D12]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4366.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +12.2 | 2e-31 | 38/49 (MIA PaCa-2, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +11.3 | 4e-27 | 41/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.28×** | +10.8 | 9e-25 | 40/49 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +9.7 | 4e-20 | 40/48 (SW480, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.46×** | +9.1 | 1e-17 | 32/44 (NCI-H1573, SNU-423, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +8.9 | 3e-17 | 32/45 (A-172, SW480, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.66×** | +6.6 | 3e-09 | 32/48 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +6.5 | 6e-09 | 30/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +6.2 | 4e-08 | 30/48 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.18× | +5.8 | 4e-07 | 17/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.16× | +5.3 | 5e-06 | 18/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.23×** | +5.2 | 1e-05 | 22/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +5.0 | 3e-05 | 22/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +4.8 | 5e-05 | 21/48 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.4 | 3e-04 | 19/45 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.20×** | +4.4 | 5e-04 | 19/48 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.20×** | +4.2 | 9e-04 | 18/47 (Panc 03.27, SNU-1, …) | all doses, flat | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +4.1 | 0.001 | 12/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.18× | +3.8 | 0.003 | 18/47 (HEC-1-A, SW1417, …) | inconsistent across doses |  |
| [[Isocorydine (drug)]] 5 µM |  | 1.09× | +3.1 | 0.050 | 5/49 (NCI-H1792, HCT15, …) | inconsistent across doses | position effect removed |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.052 | 7/49 (RPMI-7951, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Furosemide (drug)]] 5 µM |  | 1.08× | +2.9 | 0.076 | 1/48 (hTERT-HPNE) | top dose only | position effect removed |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | 1.14× | +2.9 | 0.076 | 9/48 (SW48, J82, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4366.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.794×** | -5.7 | 5e-06 | 27/48 (SW1417, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.802×** | -5.5 | 1e-05 | 27/48 (AsPC-1, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.810×** | -5.3 | 3e-05 | 25/48 (C-33 A, AN3 CA, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.943× | -4.7 | 4e-04 | 1/49 (SW 1088) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.772×** | -4.6 | 5e-04 | 25/48 (HOP62, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 0.840× | -4.2 | 0.003 | 17/48 (J82, BT-474, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.873× | -3.4 | 0.062 | 10/48 (A-427, NCI-H23, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.875× | -3.3 | 0.063 | 6/48 (Panc 03.27, PANC-1, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.870× | -3.1 | 0.098 | 13/48 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 0.883× | -3.1 | 0.098 | 13/48 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.871× | -3.1 | 0.098 | 10/48 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.916× | -3.1 | 0.098 | 8/48 (A-172, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4366. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 64.8 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 43.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.80× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[PANC-1 (line)]] | alt | 87.6 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +8.8) | — |
| [[A-172 (line)]] | wt | 47.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.44× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 49.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 89.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.03× (z +8.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 85.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.392× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 78.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.98× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 48.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 52.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.98× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 68.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 85.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 73.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 89.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 70.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 65.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 75.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 78.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 78.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 74.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4366), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TARDBP]] | +0.75 | +0.63 / +0.73 | both halves | 7e-06 | STRING 439 |
| [[PEX19]] | +0.74 | +0.61 / +0.76 | both halves | 7e-06 |  |
| [[SPTLC1]] | +0.72 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[ZNF460]] | +0.71 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[NRAS]] | +0.71 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[LIN7C]] | +0.70 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[RTF2]] | +0.68 | +0.63 / +0.77 | both halves | 7e-06 |  |
| [[MFN2]] | +0.64 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[SSU72]] | +0.64 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[EMC1]] | +0.64 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[NCSTN]] | +0.63 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[RCN1]] | +0.63 | +0.50 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 14 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX5A]] ⚠ | -0.71 | -0.49 / -0.76 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CDKN2D]] | -0.65 | -0.44 / -0.69 | both halves | 3e-05 |  |
| [[RPL36]] | -0.64 | -0.39 / -0.72 | both halves | 5e-05 |  |
| [[TBC1D12]] | -0.63 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | -0.63 | -0.28 / -0.71 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[CCDC85B]] | -0.63 | -0.36 / -0.68 | both halves | 9e-05 |  |
| [[RNF114]] | -0.63 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[C15orf61]] ⚠ | -0.61 | -0.36 / -0.64 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ORAI1]] | -0.61 | -0.40 / -0.64 | both halves | 5e-05 |  |
| [[LIN7B]] | -0.61 | -0.39 / -0.64 | both halves | 6e-05 |  |
| [[PPP1R35]] ⚠ | -0.61 | -0.38 / -0.64 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG9]] | -0.61 | -0.40 / -0.70 | both halves | 5e-05 |  |
| [[NSUN5P1-1]] | -0.61 | -0.40 / -0.66 | both halves | 5e-05 |  |
| [[C4orf48]] | -0.60 | -0.28 / -0.66 | both halves | 3e-04 |  |
| [[HOTAIRM1]] | -0.60 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[GPX4]] | -0.60 | -0.35 / -0.67 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SMU1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.636). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-31.7, -21.4); signed map (-15.7, -36.2). **Vector** length 95.4, 21.8% of its response variance represented; |z| ≥ 3 in 911 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.8 | +12.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +8.6 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.8 | +8.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.5 | +9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +6.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +2.3 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.5 | -5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.7 | -5.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | SMU1 DNA replication regulator and spliceosomal factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.1 — chr9:33,041,765-33,076,674 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SMU-1, FLJ10805, BWD, fSAP57 |
| Gene groups (HGNC) | WD repeat domain containing; Spliceosomal B complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2TAY7](https://www.uniprot.org/uniprotkb/Q2TAY7) (WD40 repeat-containing protein SMU1):

> Involved in pre-mRNA splicing as a component of the spliceosome. Regulates alternative splicing of the HSPG2 pre-mRNA (By similarity). Required for normal accumulation of IK. Required for normal mitotic spindle assembly and normal progress through mitosis (By similarity).; (Microbial infection) Required, together with IK, for normal splicing of influenza A virus NS1 pre-mRNA, which is required for the production of the exportin NS2 and for the production of influenza A virus particles. Not …

**Summary**, from NCBI Gene [55234](https://www.ncbi.nlm.nih.gov/gene/55234):

> Involved in mRNA splicing, via spliceosome. Located in nucleus. Part of U2-type precatalytic spliceosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18247](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18247) · Entrez [55234](https://www.ncbi.nlm.nih.gov/gene/55234) · UniProt [Q2TAY7](https://www.uniprot.org/uniprotkb/Q2TAY7) · Ensembl [ENSG00000122692](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122692)

## Data

Gene col 4366: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4366); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4366, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4366]; `tensor/DDL_lfc|DDL_z.npy` [4366]; `embed/gene_vectors.npy` [4366]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4366 or target_col == 4366). Every well: [[SMU1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMU1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
