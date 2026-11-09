---
symbol: "CAPN15"
type: "gene"
col: 2353
ensembl_id: "ENSG00000103326"
name: "calpain 15"
location: "16p13.3"
module: 18
arm: "+"
pooled_cpm: 15.87
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 14
n_dd_up_clean: 22
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# CAPN15

*calpain 15* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (10 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.54× (z +13.7, q 4e-40, up in 39 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.528× (z -9.5, q 2e-18, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD13B]] (+0.68, fdr 7e-06), [[MACROD1]] (+0.65, fdr 9e-06), [[TRMT1]] (+0.65, fdr 1e-05); moves opposite to [[SNAPIN]] (-0.60, fdr 1e-05), [[IFTAP]] (-0.60, fdr 1e-05), [[TTBK2]] (-0.57, fdr 4e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2353.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.54×** | +13.7 | 4e-40 | 39/46 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.95×** | +9.8 | 3e-20 | 40/48 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +8.7 | 7e-16 | 33/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +8.2 | 5e-14 | 34/46 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.71×** | +7.4 | 1e-11 | 34/47 (SW48, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.65×** | +7.4 | 1e-11 | 26/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +7.2 | 4e-11 | 17/33 (A549, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.54×** | +7.2 | 5e-11 | 17/25 (SW480, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.59×** | +6.8 | 6e-10 | 30/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +6.2 | 3e-08 | 20/43 (NCI-H2030, SW 900, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +6.2 | 4e-08 | 25/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +6.0 | 1e-07 | 24/43 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.47×** | +5.6 | 8e-07 | 26/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.02×** | +5.4 | 3e-06 | 21/44 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.94×** | +5.1 | 1e-05 | 19/45 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.92×** | +5.0 | 2e-05 | 16/43 (NCI-H460, A549, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +4.8 | 5e-05 | 21/48 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.84×** | +4.7 | 9e-05 | 16/45 (A498, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 2e-04 | 14/45 (PANC-1, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.47×** | +4.0 | 0.002 | 12/47 (NCI-H23, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.002 | 14/48 (PANC-1, J82, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2353.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.528×** | -9.5 | 2e-18 | 34/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.540×** | -8.8 | 5e-16 | 35/47 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.557×** | -8.7 | 8e-16 | 30/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.728×** | -6.7 | 4e-09 | 27/48 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.767×** | -5.6 | 3e-06 | 23/47 (A-172, A-427, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.729×** | -4.7 | 2e-04 | 23/47 (A-172, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.737×** | -4.5 | 5e-04 | 17/48 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.742×** | -4.4 | 6e-04 | 19/47 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.803×** | -4.1 | 0.002 | 13/48 (LoVo, AsPC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.798×** | -4.1 | 0.003 | 16/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.927× | -4.1 | 0.003 | 5/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.792×** | -3.9 | 0.006 | 12/48 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.791×** | -3.4 | 0.035 | 13/46 (LoVo, BT-474, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.808×** | -3.2 | 0.059 | 12/47 (MIA PaCa-2, LoVo, …) | two highest doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.803×** | -3.1 | 0.078 | 8/47 (MIA PaCa-2, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2353. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 34.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -14.2) |
| [[A549 (line)]] | wt | 16.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.244× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[SW480 (line)]] | alt | 15.1 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.85× (z +13.4) | — |
| [[A-427 (line)]] | wt | 14.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 13.1 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0950× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 21.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.83× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.621× (z -8.8) ⚠ position not correctable |
| [[PANC-1 (line)]] | alt | 12.0 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.31× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 15.3 | 0 | 1 | — | [[Selinexor (drug)]] 0.5 µM 0.0776× (z -10.2) |
| [[A498 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2353), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD13B]] | +0.68 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[MACROD1]] | +0.65 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[TRMT1]] | +0.65 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[KCTD15]] | +0.64 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[THAP4]] | +0.64 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[SENP3]] | +0.63 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[ADCY3]] | +0.63 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[TMEM11-DT]] | +0.62 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[PRDM15]] | +0.62 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[MAD1L1]] | +0.61 | +0.49 / +0.66 | both halves | 1e-05 | same gene group |
| [[BUD23]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[NPIPB11]] | +0.61 | +0.42 / +0.66 | both halves | 4e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAPIN]] | -0.60 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[IFTAP]] | -0.60 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[TTBK2]] | -0.57 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[ZNF184]] | -0.57 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[ASB8]] | -0.57 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[TMEM14C]] | -0.56 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[NDUFA5]] | -0.55 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[ATP5PO]] ⚠ | -0.55 | -0.59 / -0.44 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NFKBIZ]] | -0.55 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[TIMM17B]] ⚠ | -0.55 | -0.46 / -0.49 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[VWA5A]] | -0.55 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[ING3]] | -0.55 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[COMMD3]] | -0.54 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[ISCA2]] | -0.54 | -0.36 / -0.53 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises CAPN15's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[BEGAIN]] | B | BEGAIN activity raises CAPN15's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 1.26× lower at baseline in the lines without BEGAIN | 0.079 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.534). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-13.9, -31.1); signed map (-0.7, -52.9). **Vector** length 93.8, 20.7% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.8 | +13.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +8.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.9 | +9.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +1.2 |
|  | [[EX229 (drug)]] 5 µM |  | +3.8 | +5.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +4.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +1.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.3 | -8.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.8 | -5.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +0.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.4 | -1.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.9 | -4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -6.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.8 | -0.7 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | calpain 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:527,712-554,636 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SOLH |
| Gene groups (HGNC) | Zinc fingers RANBP2-type; Calpains; MicroRNA protein coding host genes |
| Reactome | 2 pathways, smallest: Degradation of the extracellular matrix; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [O75808](https://www.uniprot.org/uniprotkb/O75808) (Calpain-15):

> Calcium-dependent cysteine protease that functions as a non-proteasomal, ubiquitin-directed protease regulating cell adhesion through cleavage of E-cadherin/CDH1. Binds to ubiquitinated proteins via its N-terminal, preferentially recognizing longer polyubiquitin chains including both 'Lys-48- and 'Lys-63'-linked chains. Recognizes the ubiquitinated E-cadherin-catenin complex and cleaves E-cadherin in a calcium- and ubiquitination-dependent manner resulting in lysosomal degradation of the …

**Summary**, from NCBI Gene [6650](https://www.ncbi.nlm.nih.gov/gene/6650):

> This gene encodes a protein containing zinc-finger-like repeats and a calpain-like protease domain. The encoded protein may function as a transcription factor, RNA-binding protein, or in protein-protein interactions during visual system development. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11182](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11182) · Entrez [6650](https://www.ncbi.nlm.nih.gov/gene/6650) · UniProt [O75808](https://www.uniprot.org/uniprotkb/O75808) · Ensembl [ENSG00000103326](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103326)

## Data

Gene col 2353: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2353); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2353, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2353]; `tensor/DDL_lfc|DDL_z.npy` [2353]; `embed/gene_vectors.npy` [2353]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2353 or target_col == 2353). Every well: [[CAPN15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAPN15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
