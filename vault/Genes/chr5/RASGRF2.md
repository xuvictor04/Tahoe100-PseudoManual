---
symbol: "RASGRF2"
type: "gene"
col: 3449
ensembl_id: "ENSG00000113319"
name: "Ras protein specific guanine nucleotide releasing factor 2"
location: "5q14.1"
module: 92
arm: "+"
pooled_cpm: 31.32
n_lines_expressing: 29
n_dd_up: 20
n_dd_down: 11
n_dd_up_clean: 15
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# RASGRF2

*Ras protein specific guanine nucleotide releasing factor 2* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.00× (z +15.2, q 0e+00, up in 14 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.613× (z -7.6, q 1e-11, down in 17 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRBC2]] (+0.69, fdr 7e-06), [[ADGRL4]] (+0.69, fdr 7e-06), [[CCND1]] (+0.62, fdr 1e-05); moves opposite to [[RNF20]] (-0.49, fdr 1e-04), [[ARNT]] (-0.49, fdr 5e-05), [[HACE1]] (-0.48, fdr 8e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[ARSG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3449.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +15.2 | 0e+00 | 14/25 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +8.1 | 2e-13 | 5/19 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +8.0 | 3e-13 | 2/16 (J82, hTERT-HPNE) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +7.3 | 3e-11 | 9/25 (NCI-H460, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +6.1 | 2e-07 | 13/27 (NCI-H460, A-427, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +5.4 | 8e-06 | 11/25 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +5.3 | 9e-06 | 14/26 (CFPAC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +4.7 | 2e-04 | 15/24 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.6 | 2e-04 | 8/27 (NCI-H460, hTERT-HPNE, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +4.6 | 3e-04 | 12/26 (HT-29, J82, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +4.4 | 6e-04 | 9/27 (NCI-H1792, CFPAC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.3 | 9e-04 | 8/26 (NCI-H460, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.31×** | +4.2 | 0.001 | 12/27 (SNU-423, HT-29, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.63×** | +4.0 | 0.003 | 9/26 (HOP62, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.005 | 10/27 (NCI-H460, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.022 | 5/27 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.033 | 1/27 (H4) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.067 | 4/27 (HepG2/C3A, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3449.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.613×** | -7.6 | 1e-11 | 17/27 (SW480, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.655×** | -6.6 | 1e-08 | 17/27 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.723×** | -5.0 | 8e-05 | 14/27 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.767×** | -4.3 | 0.003 | 11/27 (HepG2/C3A, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.745×** | -4.2 | 0.003 | 7/27 (HepG2/C3A, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.803×** | -4.0 | 0.006 | 13/27 (HepG2/C3A, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.779×** | -4.0 | 0.006 | 13/27 (HepG2/C3A, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.839× | -3.8 | 0.010 | 6/27 (HepG2/C3A, LoVo, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.773×** | -3.7 | 0.013 | 10/25 (HepG2/C3A, SW480, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.823×** | -3.4 | 0.033 | 11/27 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.804×** | -3.2 | 0.068 | 9/27 (HepG2/C3A, LoVo, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.681×** | -3.1 | 0.084 | 3/22 (HCT15, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3449. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 284 | 0 | 16 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.118× (z -15.1) |
| [[SW480 (line)]] | alt | 130 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.134× (z -16.9) |
| [[LoVo (line)]] | wt | 136 | 1 | 6 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.403× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 50.8 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.98× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 4.19× (z +10.2) | — |
| [[HT-29 (line)]] | alt | 58.7 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +15.4) | — |
| [[NCI-H460 (line)]] | wt | 7.89 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.81× (z +18.7) | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -9.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 41.2 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.303× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.460× (z -9.5) |
| [[CHP-212 (line)]] | wt | 131 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0969× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.158× (z -9.9) |
| [[HOP62 (line)]] | alt | 106 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.266× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 71.7 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.665× (z -11.4) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.454× (z -8.8) |
| [[SNU-423 (line)]] | alt | 54.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.232× (z -11.3) |
| [[A549 (line)]] | wt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -8.7) |
| [[H4 (line)]] | wt | 50.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.130× (z -8.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 8.37 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0911× (z -9.0) ⚠ transcription drop |
| [[J82 (line)]] | alt | 9.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0766× (z -12.8) |
| [[RPMI-7951 (line)]] | alt | 11.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0970× (z -8.8) |
| [[A-172 (line)]] | wt | 3.68 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.31 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.47 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.35 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.08 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.71 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.81 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.94 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.13 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.16 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.77 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3449), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRBC2]] | +0.69 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[ADGRL4]] | +0.69 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[CCND1]] | +0.62 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[AGO2]] | +0.61 | +0.60 / +0.46 | both halves | 2e-05 | pathway: MAPK family signaling cascades |
| [[CNIH3]] | +0.60 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[GPR39]] | +0.60 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[PPP1R1C]] | +0.59 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[LINC00973]] | +0.58 | +0.58 / +0.57 | both halves | 8e-06 |  |
| [[SPRY2]] | +0.58 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[EPHB2]] | +0.57 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[PHLDA1]] | +0.55 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[B4GALT6]] | +0.55 | +0.42 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF20]] | -0.49 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[ARNT]] | -0.49 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[HACE1]] | -0.48 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[HTT]] | -0.48 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[UFSP2]] | -0.48 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[UBAC1]] | -0.48 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[BAD]] | -0.47 | -0.47 / -0.34 | both halves | 1e-04 | pathway: Cell death signalling via NRAGE, NRIF and NADE |
| [[CLINT1]] | -0.47 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[PLD3]] | -0.46 | -0.41 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RASGRF2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity raises RASGRF2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FMNL1-DT]] | B | FMNL1-DT activity raises RASGRF2's level | lines that do not express FMNL1-DT (23) vs lines expressing it (27) | 1.89× lower at baseline in the lines without FMNL1-DT | 0.080 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises RASGRF2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity raises RASGRF2's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARSG]] | B | RASGRF2 activity raises ARSG's level | lines that do not express RASGRF2 (21) vs lines expressing it (29) | 2.03× lower at baseline in the lines without RASGRF2 | 0.006 | ⚠ within organs, on part of the lines; also absent: SFRP1, MT1A, RGCC |
| [[KLF12]] | B | RASGRF2 activity raises KLF12's level | lines that do not express RASGRF2 (21) vs lines expressing it (29) | 1.77× lower at baseline in the lines without RASGRF2 | 0.012 | ⚠ within organs, on part of the lines; also absent: SFRP1, MT1A, RGCC |
| [[HBEGF]] | B | RASGRF2 activity lowers HBEGF's level | lines that do not express RASGRF2 (21) vs lines expressing it (29) | 1.36× higher at baseline in the lines without RASGRF2 | 0.055 | ⚠ within organs, on part of the lines; also absent: SFRP1, MT1A, RGCC |
| [[NTNG2]] | B | RASGRF2 activity raises NTNG2's level | lines that do not express RASGRF2 (21) vs lines expressing it (29) | 1.53× lower at baseline in the lines without RASGRF2 | 0.065 | ⚠ within organs, on part of the lines; also absent: SFRP1, MT1A, RGCC |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.709). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.0, 9.7); signed map (11.1, 43.9). **Vector** length 75.6, 17.3% of its response variance represented; |z| ≥ 3 in 803 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MAPK output* (control, mean cos +0.50 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.1 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.6 | +4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +15.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +6.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +2.7 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.5 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.1 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.1 | -4.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.8 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | Ras protein specific guanine nucleotide releasing factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.1 — chr5:80,960,363-81,230,162 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GRF2, Ras-GRF2 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs |
| Reactome | 23 pathways, smallest: Ras activation upon Ca2+ influx through NMDA receptor; CREB1 phosphorylation through NMDA receptor-mediated activation of RAS signaling; NRAGE signals death through JNK |
| Matched by | ensembl_id |

**Function**, from UniProt [O14827](https://www.uniprot.org/uniprotkb/O14827) (Ras-specific guanine nucleotide-releasing factor 2):

> Functions as a calcium-regulated nucleotide exchange factor activating both Ras and RAC1 through the exchange of bound GDP for GTP. Preferentially activates HRAS in vivo compared to RRAS based on their different types of prenylation. Functions in synaptic plasticity by contributing to the induction of long term potentiation.

**Summary**, from NCBI Gene [5924](https://www.ncbi.nlm.nih.gov/gene/5924):

> RAS GTPases cycle between an inactive GDP-bound state and an active GTP-bound state. This gene encodes a calcium-regulated nucleotide exchange factor activating both RAS and RAS-related protein, RAC1, through the exchange of bound GDP for GTP, thereby, coordinating the signaling of distinct mitogen-activated protein kinase pathways. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:9876](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9876) · Entrez [5924](https://www.ncbi.nlm.nih.gov/gene/5924) · UniProt [O14827](https://www.uniprot.org/uniprotkb/O14827) · Ensembl [ENSG00000113319](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113319)

## Data

Gene col 3449: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3449); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3449, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3449]; `tensor/DDL_lfc|DDL_z.npy` [3449]; `embed/gene_vectors.npy` [3449]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3449 or target_col == 3449). Every well: [[RASGRF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RASGRF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
