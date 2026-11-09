---
symbol: "ALKBH5"
type: "gene"
col: 1669
ensembl_id: "ENSG00000091542"
name: "alkB homolog 5, RNA demethylase"
location: "17p11.2"
module: 99
arm: "+"
pooled_cpm: 71.43
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# ALKBH5

*alkB homolog 5, RNA demethylase* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.62× (z +16.8, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.560× (z -12.3, q 3e-32, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED26]] (+0.75, fdr 7e-06), [[SEC24C]] (+0.73, fdr 7e-06), [[HK2]] (+0.71, fdr 1e-05); moves opposite to [[GCFC2]] (-0.67, fdr 7e-06), [[ITPA]] (-0.67, fdr 7e-06), [[YTHDC2]] (-0.66, fdr 7e-06).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NXPH4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1669.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.62×** | +16.8 | 0e+00 | 49/49 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +11.3 | 5e-27 | 42/49 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.37×** | +10.8 | 5e-25 | 39/48 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.51×** | +7.0 | 4e-10 | 34/48 (SHP-77, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.44×** | +6.2 | 6e-08 | 34/48 (SHP-77, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +6.0 | 3e-07 | 36/48 (A-172, C-33 A, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.40×** | +5.8 | 6e-07 | 32/48 (SW480, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +5.0 | 5e-05 | 32/48 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.27×** | +4.0 | 0.004 | 24/50 (MIA PaCa-2, SW1417, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | **1.26×** | +4.0 | 0.004 | 23/48 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +3.5 | 0.021 | 25/48 (Hs 766T, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.21×** | +3.3 | 0.044 | 19/48 (A-172, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1669.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.560×** | -12.3 | 3e-32 | 37/48 (AN3 CA, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.543×** | -10.4 | 7e-23 | 40/48 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.543×** | -10.0 | 3e-21 | 43/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.689×** | -6.1 | 1e-07 | 32/48 (NCI-H1573, COLO 205, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.712×** | -5.8 | 8e-07 | 29/48 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.762×** | -4.6 | 3e-04 | 32/48 (HCT15, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.791×** | -4.0 | 0.005 | 23/49 (COLO 205, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Demeclocycline (drug)]] 5 µM |  | **0.831×** | -3.7 | 0.016 | 20/48 (HEC-1-A, SW480, …) | top dose only | position effect removed |
| [[Afatinib (drug)]] 0.5 µM |  | 0.864× | -3.3 | 0.058 | 11/49 (HT-29, hTERT-HPNE, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.834× | -3.1 | 0.11 | 17/48 (SW 900, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.838× | -3.0 | 0.13 | 21/48 (A498, SNU-1, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.866× | -3.0 | 0.13 | 13/48 (AsPC-1, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1669. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 54.7 | 6 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.65× (z +11.3) | — |
| [[AsPC-1 (line)]] | alt | 58.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -14.4) |
| [[NCI-H1573 (line)]] | alt | 56.8 | 2 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -12.7) |
| [[SW480 (line)]] | alt | 62.8 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.77× (z +15.4) | — |
| [[A-172 (line)]] | wt | 65.4 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.250× (z -14.6) |
| [[A498 (line)]] | wt | 119 | 1 (1 ⚠) | 3 | [[Ixazomib citrate (drug)]] 5 µM 2.03× (z +8.5) ⚠ cell-cycle shift, explains ~11% of this change | [[Harringtonine (drug)]] 0.5 µM 0.315× (z -14.1) |
| [[A549 (line)]] | wt | 65.6 | 2 | 2 | [[TAK-901 (drug)]] 5 µM 7.37× (z +10.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.339× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 91.3 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -16.4) |
| [[NCI-H23 (line)]] | alt | 79.9 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 8.41× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -16.0) |
| [[NCI-H2347 (line)]] | alt | 46.5 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.287× (z -12.0) |
| [[BT-474 (line)]] | alt | 49.5 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.227× (z -12.0) |
| [[C32 (line)]] | wt | 80.1 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 19.9× (z +14.2) | — |
| [[HOP62 (line)]] | alt | 105 | 2 | 1 | [[PH-797804 (drug)]] 5 µM 7.28× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -11.7) |
| [[KATO III (line)]] | alt | 91.3 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.22× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.373× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 93.4 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.36× (z +9.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.09× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 103 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -16.8) |
| [[C-33 A (line)]] | alt | 152 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.42× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -11.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 60.8 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 15.1× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -15.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 61.1 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 10.1× (z +13.8) | — |
| [[LoVo (line)]] | wt | 68.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.6× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.416× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 86.4 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.73× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 66.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.97× (z +11.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 82.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +9.9) | — |
| [[PANC-1 (line)]] | alt | 59.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.34× (z +10.2) | — |
| [[SW1417 (line)]] | alt | 52.2 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.74× (z +10.2) | — |
| [[CHP-212 (line)]] | wt | 93.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -8.5) |
| [[H4 (line)]] | wt | 82.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -9.1) |
| [[HCT15 (line)]] | alt | 91.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 41.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.71× (z +9.3) | — |
| [[RKO (line)]] | wt | 63.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.28× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 77.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.85× (z +9.0) | — |
| [[SNU-1 (line)]] | wt | 68.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.7× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 126 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.03× (z +9.5) | — |
| [[SW48 (line)]] | wt | 97.0 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 11.8× (z +10.2) | — |
| [[A-427 (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 65.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 136 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 66.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 145 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1669), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED26]] | +0.75 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[SEC24C]] | +0.73 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[HK2]] | +0.71 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[ERO1A]] | +0.71 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[KDELR1]] | +0.71 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[GRB2]] | +0.70 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.70 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[DERL1]] | +0.69 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[UBE2O]] | +0.69 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[IER3IP1]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[BMT2]] | +0.68 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[MOSPD3]] | +0.68 | +0.64 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCFC2]] | -0.67 | -0.67 / -0.59 | both halves | 7e-06 |  |
| [[ITPA]] | -0.67 | -0.72 / -0.58 | both halves | 7e-06 |  |
| [[YTHDC2]] | -0.66 | -0.64 / -0.62 | both halves | 7e-06 | STRING 921 |
| [[GPATCH4]] | -0.65 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[ZC3H7B]] | -0.65 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[SLC25A13]] | -0.63 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[SH3D19]] | -0.63 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[TRMT13]] | -0.62 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[ST7L]] | -0.62 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[MAPK1IP1L]] | -0.61 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[FKRP]] | -0.61 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[RPL7L1]] | -0.61 | -0.60 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NXPH4]] | B | NXPH4 activity raises ALKBH5's level | lines that do not express NXPH4 (13) vs lines expressing it (37) | 1.48× lower at baseline in the lines without NXPH4 | 0.036 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.720). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.8, -17.8); signed map (-43.1, 16.0). **Vector** length 136, 41.5% of its response variance represented; |z| ≥ 3 in 876 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.7 | +16.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.8 | +10.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +11.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.5 | +5.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +5.1 | +5.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +6.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.8 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +0.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -11.8 | -10.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.1 | -10.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -9.8 | -12.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.1 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.1 | -3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -6.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.2 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.0 | -4.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | alkB homolog 5, RNA demethylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:18,183,078-18,209,954 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20308; previously OFOXD1 |
| Gene groups (HGNC) | Alkylation repair homologs |
| Reactome | 3 pathways, smallest: Reversal of alkylation damage by DNA dioxygenases; DNA Damage Reversal; DNA Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P6C2](https://www.uniprot.org/uniprotkb/Q6P6C2) (RNA demethylase ALKBH5):

> Dioxygenase that specifically demethylates N(6)-methyladenosine (m6A) RNA, the most prevalent internal modification of messenger RNA (mRNA) in higher eukaryotes. Demethylates RNA by oxidative demethylation, which requires molecular oxygen, alpha-ketoglutarate and iron. Demethylation of m6A mRNA affects mRNA processing, translation and export. Can also demethylate N(6)-methyladenosine in single-stranded DNA (in vitro). Required for the late meiotic and haploid phases of spermatogenesis by …

**Summary**, from NCBI Gene [54890](https://www.ncbi.nlm.nih.gov/gene/54890):

> Enables mRNA N6-methyladenosine dioxygenase activity and molecular condensate scaffold activity. Involved in membraneless organelle assembly; post-transcriptional regulation of gene expression; and response to hypoxia. Acts upstream of or within regulation of mRNA export from nucleus and regulation of mRNA processing. Located in nuclear speck. Is active in paraspeckles. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25996](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25996) · Entrez [54890](https://www.ncbi.nlm.nih.gov/gene/54890) · UniProt [Q6P6C2](https://www.uniprot.org/uniprotkb/Q6P6C2) · Ensembl [ENSG00000091542](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091542)

## Data

Gene col 1669: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1669); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1669, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1669]; `tensor/DDL_lfc|DDL_z.npy` [1669]; `embed/gene_vectors.npy` [1669]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1669 or target_col == 1669). Every well: [[ALKBH5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALKBH5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
