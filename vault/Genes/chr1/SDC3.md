---
symbol: "SDC3"
type: "gene"
col: 8525
ensembl_id: "ENSG00000162512"
name: "syndecan 3"
location: "1p35.2"
module: 132
arm: "+"
pooled_cpm: 17.41
n_lines_expressing: 46
n_dd_up: 11
n_dd_down: 21
n_dd_up_clean: 7
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 12
direction_downstream: 24
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# SDC3

*syndecan 3* — 1p35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.73× (z +7.4, q 7e-11, up in 13 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.43× (z +7.1, q 3e-10, up in 32 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.529× (z -12.6, q 8e-34, down in 29 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNAZ]] (+0.69, fdr 7e-06), [[NBEAL2]] (+0.65, fdr 1e-05), [[SHANK3]] (+0.64, fdr 7e-06); moves opposite to [[MBD5]] (-0.50, fdr 2e-05), [[TRMT1L]] (-0.50, fdr 4e-05), [[DCP1A]] (-0.50, fdr 3e-05).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[PDZD4]] → it (grade B ⚠); 24 go from it, the strongest it → cells under [[Capmatinib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8525.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +7.4 | 7e-11 | 13/23 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +7.1 | 3e-10 | 32/44 (SHP-77, PANC-1, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +6.8 | 2e-09 | 22/39 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +5.5 | 6e-06 | 22/41 (NCI-H1573, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +5.4 | 6e-06 | 19/44 (SHP-77, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +4.4 | 0.001 | 16/43 (HCT15, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.59×** | +3.4 | 0.049 | 5/42 (C32, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.049 | 13/44 (J82, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.27×** | +3.4 | 0.049 | 13/39 (RPMI-7951, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Almonertinib (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.050 | 5/43 (J82, BT-474, …) | inconsistent across doses | position effect removed |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.097 | 6/43 (C-33 A, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.05 µM |  | 1.26× | +3.0 | 0.11 | 8/44 (HOP62, C32, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.24× | +3.0 | 0.11 | 6/43 (SHP-77, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | 1.24× | +3.0 | 0.11 | 9/43 (PANC-1, NCI-H23, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8525.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.529×** | -12.6 | 8e-34 | 29/43 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.467×** | -10.3 | 3e-22 | 27/44 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.495×** | -9.8 | 1e-20 | 25/43 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.667×** | -5.7 | 2e-06 | 20/44 (SK-MEL-2, C32, …) | two highest doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.681×** | -5.2 | 3e-05 | 19/43 (SNU-1, HEC-1-A, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.792×** | -4.6 | 4e-04 | 15/44 (SW480, NCI-H23, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.727×** | -4.5 | 7e-04 | 15/43 (J82, A-172, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.553×** | -4.3 | 0.001 | 18/43 (LOX-IMVI, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.749×** | -4.0 | 0.003 | 16/44 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.754×** | -4.0 | 0.004 | 16/42 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.755×** | -3.9 | 0.004 | 15/44 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.756×** | -3.9 | 0.004 | 21/44 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.590×** | -3.9 | 0.005 | 19/44 (NCI-H23, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.756×** | -3.8 | 0.007 | 15/40 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.924× | -3.7 | 0.009 | 12/44 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.778×** | -3.5 | 0.014 | 14/43 (PANC-1, NCI-H1792, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.780×** | -3.5 | 0.016 | 14/43 (C32, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.793×** | -3.1 | 0.060 | 13/43 (C32, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sulfisoxazole (drug)]] 5 µM |  | 0.861× | -3.0 | 0.078 | 4/44 (LoVo, HOP62, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8525. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 117 | 1 (1 ⚠) | 12 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.59× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -18.3) |
| [[SW480 (line)]] | alt | 32.9 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 22.2 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0956× (z -15.8) |
| [[NCI-H23 (line)]] | alt | 31.6 | 0 | 4 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0499× (z -11.6) |
| [[SK-MEL-2 (line)]] | alt | 61.2 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.65× (z +12.2) ⚠ toxic; transcription drop | [[Cobimetinib (drug)]] 5 µM 0.188× (z -13.3) |
| [[HEC-1-A (line)]] | alt | 26.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -18.5) |
| [[MIA PaCa-2 (line)]] | alt | 23.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -17.0) |
| [[SNU-1 (line)]] | wt | 18.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0533× (z -12.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.111× (z -8.9) |
| [[SW48 (line)]] | wt | 12.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0719× (z -9.7) |
| [[A-172 (line)]] | wt | 13.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -15.0) |
| [[A-427 (line)]] | wt | 27.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -9.4) |
| [[A498 (line)]] | wt | 6.36 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.70× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -12.3) |
| [[HOP62 (line)]] | alt | 20.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -12.2) |
| [[LoVo (line)]] | wt | 17.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.239× (z -10.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 7.17 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.188× (z -9.2) ⚠ cell-cycle shift, explains ~18% of this change |
| [[PANC-1 (line)]] | alt | 18.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -9.4) |
| [[SNU-423 (line)]] | alt | 5.55 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -8.6) |
| [[AN3 CA (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8525), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAZ]] | +0.69 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[NBEAL2]] | +0.65 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[SHANK3]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[CACNA1H]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[SLC48A1]] | +0.61 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[SLC4A3]] | +0.61 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[PLXNA1]] | +0.59 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[USP31]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[RASGEF1C]] | +0.58 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[MAPKAPK3]] | +0.58 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[ADAMTSL5]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 | pathway: Diseases of glycosylation |
| [[ATP13A2]] | +0.57 | +0.54 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBD5]] | -0.50 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[TRMT1L]] | -0.50 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[DCP1A]] | -0.50 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[CDKN1B]] | -0.49 | -0.48 / -0.46 | both halves | 2e-05 | pathway: HALLMARK_HYPOXIA |
| [[FMC1]] | -0.49 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[SYNRG]] | -0.49 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[ATP6V1G1]] | -0.48 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[SLC4A1AP]] | -0.47 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[BBOF1]] | -0.47 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[TBCK]] | -0.47 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[MORN2]] | -0.47 | -0.37 / -0.46 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDZD4]] | B | PDZD4 activity raises SDC3's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 2.10× lower at baseline in the lines without PDZD4 | 0.004 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[KIF26A]] | B | KIF26A activity raises SDC3's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 1.48× lower at baseline in the lines without KIF26A | 0.008 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[VASH1]] | B | VASH1 activity raises SDC3's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 2.22× lower at baseline in the lines without VASH1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B |
| [[GNAZ]] | B | GNAZ activity raises SDC3's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.92× lower at baseline in the lines without GNAZ | 0.020 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[KCNC4]] | B | KCNC4 activity raises SDC3's level | lines that do not express KCNC4 (6) vs lines expressing it (44) | 2.43× lower at baseline in the lines without KCNC4 | 0.032 | ⚠ within organs, on part of the lines; also absent: CRTAP, FKBP7, SACS; maybe low, not absent |
| [[SLC4A3]] | B | SLC4A3 activity raises SDC3's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 2.26× lower at baseline in the lines without SLC4A3 | 0.042 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[LAMC3]] | B | LAMC3 activity raises SDC3's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.75× lower at baseline in the lines without LAMC3 | 0.048 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[ANKRD20A1]] | B | ANKRD20A1 activity raises SDC3's level | lines that do not express ANKRD20A1 (20) vs lines expressing it (30) | 1.89× lower at baseline in the lines without ANKRD20A1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ANKRD20A4P, CTNNA2, SCN8A |
| [[FAM78B]] | B | FAM78B activity raises SDC3's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.94× lower at baseline in the lines without FAM78B | 0.054 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[PTPRZ1]] | B | PTPRZ1 activity raises SDC3's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 2.12× lower at baseline in the lines without PTPRZ1 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029 |
| [[ADCY3]] | B | ADCY3 activity raises SDC3's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.70× lower at baseline in the lines without ADCY3 | 0.076 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[PARVB]] | B | PARVB activity raises SDC3's level | lines that do not express PARVB (13) vs lines expressing it (37) | 1.94× lower at baseline in the lines without PARVB | 0.089 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8 |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 0, C 24. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Capmatinib (drug)]] 5 µM | C | SDC3 activity raises the cells' numbers under Capmatinib 5 µM (protects the cells) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 0.62× the cells of the other lines | 0.004 | ⚠ few lines (4 vs 46); across organs |
| cells under [[Trametinib (drug)]] 0.5 µM | C | SDC3 activity raises the cells' numbers under Trametinib 0.5 µM (protects the cells) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 0.66× the cells of the other lines | 0.010 | ⚠ few lines (4 vs 46); across organs |
| cells under [[SBI-0640756 (drug)]] 5 µM | C | SDC3 activity lowers the cells' numbers under SBI-0640756 5 µM (makes them more sensitive) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 1.42× the cells of the other lines | 0.011 | ⚠ few lines (4 vs 46); across organs |
| cells under [[Binimetinib (drug)]] 0.05 µM | C | SDC3 activity raises the cells' numbers under Binimetinib 0.05 µM (protects the cells) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 0.72× the cells of the other lines | 0.021 | ⚠ few lines (4 vs 46); across organs |
| cells under [[palbociclib (drug)]] 5 µM | C | SDC3 activity raises the cells' numbers under palbociclib 5 µM (protects the cells) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 0.69× the cells of the other lines | 0.022 | ⚠ few lines (4 vs 46); across organs |
| cells under [[Binimetinib (drug)]] 0.5 µM | C | SDC3 activity raises the cells' numbers under Binimetinib 0.5 µM (protects the cells) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 0.72× the cells of the other lines | 0.023 | ⚠ few lines (4 vs 46); across organs |
| cells under [[DT-061 (drug)]] 5 µM | C | SDC3 activity raises the cells' numbers under DT-061 5 µM (protects the cells) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 0.71× the cells of the other lines | 0.026 | ⚠ few lines (4 vs 46); across organs |
| cells under [[Almonertinib (hydrochloride) (drug)]] 5 µM | C | SDC3 activity raises the cells' numbers under Almonertinib (hydrochloride) 5 µM (protects the cells) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 0.83× the cells of the other lines | 0.027 | ⚠ few lines (4 vs 46); across organs |
| cells under [[Trametinib (drug)]] 5 µM | C | SDC3 activity raises the cells' numbers under Trametinib 5 µM (protects the cells) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 0.64× the cells of the other lines | 0.028 | ⚠ few lines (4 vs 46); across organs |
| cells under [[PF-06260933 (drug)]] 5 µM | C | SDC3 activity lowers the cells' numbers under PF-06260933 5 µM (makes them more sensitive) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 1.56× the cells of the other lines | 0.028 | ⚠ few lines (4 vs 46); across organs |
| cells under [[AZD-7648 (drug)]] 5 µM | C | SDC3 activity raises the cells' numbers under AZD-7648 5 µM (protects the cells) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 0.66× the cells of the other lines | 0.028 | ⚠ few lines (4 vs 46); across organs |
| cells under [[Binimetinib (drug)]] 5 µM | C | SDC3 activity raises the cells' numbers under Binimetinib 5 µM (protects the cells) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 0.68× the cells of the other lines | 0.029 | ⚠ few lines (4 vs 46); across organs |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.707). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.2, 42.3); signed map (-15.4, 41.7). **Vector** length 97.3, 21.6% of its response variance represented; |z| ≥ 3 in 1,031 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +7.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.3 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +5.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.4 | +0.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +1.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -10.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -9.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -3.1 | -3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.1 | -5.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.6 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -1.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.2 | -2.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | syndecan 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.2 — chr1:30,869,466-30,908,758 (-) |
| Ensembl biotype | protein_coding |
| Also known as | N-syndecan, SYND3 |
| Gene groups (HGNC) | Syndecans |
| Hallmark sets | APICAL_JUNCTION, GLYCOLYSIS, HYPOXIA |
| Reactome | 38 pathways, smallest: Defective EXT1 causes exostoses 1, TRPS2 and CHDS; Defective EXT2 causes exostoses 2; Defective B3GALT6 causes EDSP2 and SEMDJL1 |
| Matched by | ensembl_id |

**Function**, from UniProt [O75056](https://www.uniprot.org/uniprotkb/O75056) (Syndecan-3):

> Cell surface proteoglycan that may bear heparan sulfate (By similarity). May have a role in the organization of cell shape by affecting the actin cytoskeleton, possibly by transferring signals from the cell surface in a sugar-dependent mechanism.

**Summary**, from NCBI Gene [9672](https://www.ncbi.nlm.nih.gov/gene/9672):

> The protein encoded by this gene belongs to the syndecan proteoglycan family. It may play a role in the organization of cell shape by affecting the actin cytoskeleton, possibly by transferring signals from the cell surface in a sugar-dependent mechanism. Allelic variants of this gene have been associated with obesity. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:10660](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10660) · Entrez [9672](https://www.ncbi.nlm.nih.gov/gene/9672) · UniProt [O75056](https://www.uniprot.org/uniprotkb/O75056) · Ensembl [ENSG00000162512](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162512)

## Data

Gene col 8525: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8525); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8525, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8525]; `tensor/DDL_lfc|DDL_z.npy` [8525]; `embed/gene_vectors.npy` [8525]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8525 or target_col == 8525). Every well: [[SDC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
