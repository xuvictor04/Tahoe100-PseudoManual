---
symbol: "NEK4"
type: "gene"
col: 3601
ensembl_id: "ENSG00000114904"
name: "NIMA related kinase 4"
location: "3p21.1"
module: 36
arm: "+"
pooled_cpm: 27.63
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# NEK4

*NIMA related kinase 4* — 3p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.13× (z +18.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.663× (z -10.3, q 4e-22, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAF3IP1]] (+0.71, fdr 7e-06), [[DNAL1]] (+0.60, fdr 3e-05), [[TMEM254]] (+0.60, fdr 1e-05); moves opposite to [[EPHA1-AS1]] (-0.50, fdr 1e-04), [[OXSM]] (-0.50, fdr 0.002, ⚠ one half only (not replicated)), [[TUBA4A]] (-0.49, fdr 4e-04), [[MORF4L2]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAFB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3601.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.13×** | +18.9 | 0e+00 | 47/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.99×** | +17.2 | 0e+00 | 45/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.98×** | +17.1 | 0e+00 | 44/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +16.8 | 0e+00 | 41/44 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +16.5 | 0e+00 | 28/37 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +12.6 | 3e-34 | 28/41 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +12.2 | 2e-32 | 35/46 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.61×** | +11.9 | 5e-31 | 36/48 (LoVo, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +10.6 | 3e-24 | 29/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +10.3 | 6e-23 | 29/47 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +9.2 | 2e-18 | 28/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +7.7 | 6e-13 | 27/47 (C-33 A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +7.6 | 9e-13 | 27/48 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.79×** | +7.6 | 1e-12 | 28/48 (HEC-1-A, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.25×** | +5.5 | 1e-06 | 14/47 (hTERT-HPNE, A-172, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.52×** | +5.5 | 2e-06 | 17/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.26×** | +5.4 | 2e-06 | 20/47 (Panc 03.27, BT-474, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.21×** | +4.7 | 7e-05 | 16/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.20× | +4.6 | 1e-04 | 14/48 (HOP62, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +4.3 | 5e-04 | 7/48 (J82, LoVo, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.17× | +3.9 | 0.002 | 6/48 (HEC-1-A, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3601.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.663×** | -10.3 | 4e-22 | 35/47 (SW480, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.769×** | -6.6 | 1e-08 | 26/48 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.850× | -5.7 | 2e-06 | 19/48 (HOP62, CHP-212, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.861× | -5.3 | 2e-05 | 21/48 (HOP62, A-172, …) | top dose only |  |
| [[Simotinib (drug)]] 0.05 µM |  | 0.843× | -4.0 | 0.009 | 10/47 (LoVo, COLO 205, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.955× | -3.9 | 0.011 | 2/48 (CHP-212, SW 1271) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.752×** | -3.7 | 0.016 | 16/46 (CHP-212, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | 0.868× | -3.5 | 0.028 | 10/47 (RPMI-7951, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3601. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 39.5 | 7 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.97× (z +13.3) | [[Auranofin (drug)]] 5 µM 0.468× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 47.3 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +12.4) | [[Auranofin (drug)]] 5 µM 0.491× (z -8.6) |
| [[PANC-1 (line)]] | alt | 19.3 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.62× (z +9.9) | — |
| [[LoVo (line)]] | wt | 34.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 36.6 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.41× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 36.2 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.434× (z -12.6) |
| [[KATO III (line)]] | alt | 29.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.14× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 30.1 | 1 (1 ⚠) | 1 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.08× (z +8.5) ⚠ toxic | [[Auranofin (drug)]] 5 µM 0.463× (z -9.4) |
| [[A-427 (line)]] | wt | 34.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.51× (z +11.4) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 26.3 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0865× (z -8.6) |
| [[H4 (line)]] | wt | 11.7 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0744× (z -9.3) |
| [[Hs 766T (line)]] | wt | 14.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 34.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -11.4) |
| [[LS 180 (line)]] | wt | 27.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.69× (z +10.2) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 21.8 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.38× (z +9.0) ⚠ toxic | — |
| [[NCI-H1573 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.110× (z -16.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 26.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.9) | — |
| [[A-172 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3601), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAF3IP1]] | +0.71 | +0.64 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[DNAL1]] | +0.60 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[TMEM254]] | +0.60 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[ENTPD5]] | +0.55 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[IQCE]] | +0.54 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[ZC3H14]] | +0.54 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[MRPL16]] | +0.54 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[DNAJC16]] | +0.53 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[TMTC3]] | +0.53 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[MDM1]] | +0.53 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[RMDN3]] | +0.53 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[GFM1]] | +0.53 | +0.44 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHA1-AS1]] | -0.50 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[OXSM]] | -0.50 | -0.12 / -0.62 | ⚠ one half (not replicated) | 0.002 |  |
| [[TUBA4A]] | -0.49 | -0.25 / -0.57 | both halves | 4e-04 |  |
| [[MORF4L2]] | -0.49 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[IFRD1]] | -0.47 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[MAFB]] | -0.47 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[F12]] | -0.47 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[LIPE-AS1]] | -0.47 | -0.25 / -0.53 | both halves | 4e-04 |  |
| [[DHDH]] | -0.46 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[MSX1]] | -0.46 | -0.11 / -0.49 | ⚠ not reproduced | 0.002 |  |
| [[DDIT3]] | -0.45 | -0.37 / -0.47 | both halves | 7e-05 |  |
| [[KLHL29]] | -0.45 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[GTF2B]] | -0.45 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[SELPLG]] | -0.44 | -0.38 / -0.43 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAFB]] | B | MAFB activity lowers NEK4's level | lines that do not express MAFB (19) vs lines expressing it (31) | 1.29× higher at baseline in the lines without MAFB | 0.076 | ⚠ within organs, on part of the lines; also absent: LBH, TREM1, IL2RG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.314). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-25.6, 0.8); signed map (-20.5, -18.4). **Vector** length 90.9, 19.5% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.5 | +16.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.9 | +16.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +12.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.9 | +12.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.1 | +18.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +5.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +4.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +3.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.5 | +2.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.1 | -10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.1 | -5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.4 | -6.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.4 | -2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -5.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | NIMA related kinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.1 — chr3:52,708,444-52,770,946 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NRK2, pp12301; previously STK2 |
| Gene groups (HGNC) | NIMA related kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [P51957](https://www.uniprot.org/uniprotkb/P51957) (Serine/threonine-protein kinase Nek4):

> Protein kinase that seems to act exclusively upon threonine residues (By similarity). Required for normal entry into proliferative arrest after a limited number of cell divisions, also called replicative senescence. Required for normal cell cycle arrest in response to double-stranded DNA damage.

**Summary**, from NCBI Gene [6787](https://www.ncbi.nlm.nih.gov/gene/6787):

> The protein encoded by this gene is a serine/threonine protein kinase required for normal entry into replicative senescence. The encoded protein also is involved in cell cycle arrest in response to double-stranded DNA damage. Finally, this protein plays a role in maintaining cilium integrity, and defects in this gene have been associated with ciliopathies. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:11399](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11399) · Entrez [6787](https://www.ncbi.nlm.nih.gov/gene/6787) · UniProt [P51957](https://www.uniprot.org/uniprotkb/P51957) · Ensembl [ENSG00000114904](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114904)

## Data

Gene col 3601: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3601); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3601, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3601]; `tensor/DDL_lfc|DDL_z.npy` [3601]; `embed/gene_vectors.npy` [3601]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3601 or target_col == 3601). Every well: [[NEK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
