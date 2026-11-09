---
symbol: "SIX4"
type: "gene"
col: 2003
ensembl_id: "ENSG00000100625"
name: "SIX homeobox 4"
location: "14q23.1"
module: 46
arm: "+"
pooled_cpm: 19.0
n_lines_expressing: 45
n_dd_up: 27
n_dd_down: 9
n_dd_up_clean: 20
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# SIX4

*SIX homeobox 4* — 14q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.62× (z +42.4, q 0e+00, up in 40 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Belumosudil (drug)]] 5 µM: 0.678× (z -6.0, q 1e-06, down in 25 of 42 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IRF2]] (+0.66, fdr 1e-05), [[GALNT7-DT]] (+0.64, fdr 9e-05), [[SATB1]] (+0.61, fdr 3e-05); moves opposite to [[RBM6]] (-0.62, fdr 1e-05), [[PIGU]] (-0.59, fdr 2e-05), [[NOL10]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[WDR70]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2003.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.62×** | +42.4 | 0e+00 | 40/41 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.52×** | +28.2 | 0e+00 | 41/43 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.83×** | +24.1 | 0e+00 | 40/42 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.03×** | +17.6 | 0e+00 | 35/40 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.58×** | +15.1 | 0e+00 | 34/42 (HOP62, RKO, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +12.9 | 4e-36 | 35/42 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +12.4 | 2e-33 | 33/42 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.01×** | +11.0 | 2e-26 | 34/42 (BT-474, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.28×** | +9.9 | 4e-21 | 31/42 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.81×** | +9.4 | 2e-19 | 30/42 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +9.4 | 4e-19 | 30/40 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.66×** | +8.1 | 4e-14 | 24/42 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +8.0 | 7e-14 | 26/43 (HOP62, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +7.1 | 4e-11 | 29/42 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +6.4 | 8e-09 | 25/42 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +6.1 | 3e-08 | 25/41 (CFPAC-1, LoVo, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.35×** | +4.7 | 8e-05 | 14/42 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2003.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **0.678×** | -6.0 | 1e-06 | 25/42 (SW 1271, Panc 03.27, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.744×** | -4.7 | 7e-04 | 19/37 (C32, J82, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.777×** | -4.0 | 0.008 | 20/42 (NCI-H1573, Panc 03.27, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.619×** | -4.0 | 0.008 | 15/41 (BT-474, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.620×** | -4.0 | 0.008 | 12/38 (HepG2/C3A, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.776×** | -3.9 | 0.010 | 15/29 (HepG2/C3A, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.802×** | -3.4 | 0.056 | 10/42 (SNU-1, C32, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.815×** | -3.3 | 0.079 | 8/42 (HCT15, HOP62, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **0.818×** | -3.2 | 0.082 | 16/40 (SHP-77, HT-29, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | 0.692× | -3.1 | 0.12 | 10/41 (SW480, J82, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.827× | -3.0 | 0.12 | 12/42 (BT-474, NCI-H2347, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2003. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 31.6 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +23.3) | — |
| [[PANC-1 (line)]] | alt | 17.7 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +31.0) | — |
| [[BT-474 (line)]] | alt | 39.6 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.49× (z +22.6) | — |
| [[HEC-1-A (line)]] | alt | 26.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.5× (z +32.2) | — |
| [[HOP62 (line)]] | alt | 16.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +20.2) | — |
| [[A-172 (line)]] | wt | 12.8 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +19.9) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -8.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 16.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +30.0) | — |
| [[NCI-H460 (line)]] | wt | 11.2 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.62× (z +16.5) | — |
| [[SW 900 (line)]] | alt | 24.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.98× (z +18.1) | — |
| [[SW480 (line)]] | alt | 27.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +19.4) | — |
| [[A549 (line)]] | wt | 8.90 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.2× (z +21.4) | — |
| [[CFPAC-1 (line)]] | alt | 21.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.7× (z +26.3) | — |
| [[NCI-H2347 (line)]] | alt | 39.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.70× (z +28.5) | — |
| [[Panc 03.27 (line)]] | alt | 64.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.50× (z +27.5) | — |
| [[C32 (line)]] | wt | 14.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -11.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 25.9 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +13.3) | [[Ipatasertib (drug)]] 0.5 µM 0.107× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 36.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +19.4) | [[Dinaciclib (drug)]] 5 µM 0.0849× (z -13.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 8.55 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.77× (z +14.0) | — |
| [[LOX-IMVI (line)]] | wt | 12.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +13.3) | — |
| [[NCI-H1792 (line)]] | alt | 18.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.64× (z +17.5) | — |
| [[SNU-423 (line)]] | alt | 15.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +19.5) | — |
| [[SW1417 (line)]] | alt | 22.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +21.3) | — |
| [[AsPC-1 (line)]] | alt | 9.32 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.99× (z +13.0) | — |
| [[H4 (line)]] | wt | 12.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +12.8) | — |
| [[HS-578T (line)]] | alt | 14.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +10.8) | — |
| [[hTERT-HPNE (line)]] | wt | 15.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +14.6) | — |
| [[J82 (line)]] | alt | 23.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.34× (z +20.7) | — |
| [[NCI-H1573 (line)]] | alt | 19.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +16.5) | — |
| [[NCI-H2030 (line)]] | alt | 8.07 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +10.4) | — |
| [[AN3 CA (line)]] | alt | 42.3 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.105× (z -9.2) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 25.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.33× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 29.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 9.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.77× (z +15.5) | — |
| [[NCI-H23 (line)]] | alt | 14.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.47× (z +10.9) | — |
| [[RKO (line)]] | wt | 34.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.77× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 14.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.18× (z +10.5) | — |
| [[A-427 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.81 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2003), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IRF2]] | +0.66 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[GALNT7-DT]] | +0.64 | +0.58 / +0.37 | both halves | 9e-05 |  |
| [[SATB1]] | +0.61 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[CDKN1B]] | +0.59 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[SIM2]] | +0.58 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[ZBED5]] | +0.58 | +0.50 / +0.38 | both halves | 6e-05 |  |
| [[ZNF827]] | +0.57 | +0.55 / +0.29 | both halves | 3e-04 |  |
| [[HIVEP1]] | +0.57 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[SETD1B]] | +0.57 | +0.47 / +0.26 | both halves | 4e-04 |  |
| [[LINC00938]] | +0.57 | +0.47 / +0.33 | both halves | 1e-04 |  |
| [[RARG]] | +0.57 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[CILK1]] | +0.57 | +0.57 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM6]] | -0.62 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[PIGU]] | -0.59 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[NOL10]] | -0.59 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[PPIL2]] | -0.58 | -0.54 / -0.40 | both halves | 4e-05 |  |
| [[ATG5]] | -0.57 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[STX8]] | -0.56 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[FAM13B]] | -0.56 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[WDR70]] | -0.56 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[MICU2]] | -0.54 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[ARPC1A]] | -0.54 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[CTNNBL1]] | -0.54 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[CLTCL1]] | -0.54 | -0.41 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SIX4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CLTCL1]] | C | CLTCL1 activity raises SIX4's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 4.13× lower at baseline in the lines without CLTCL1 | 0.026 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WDR70]] | B | SIX4 activity raises WDR70's level | lines that do not express SIX4 (5) vs lines expressing it (45) | 1.47× lower at baseline in the lines without SIX4 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CPLANE1, FGFR1 |
| [[ARHGEF17]] | B | SIX4 activity raises ARHGEF17's level | lines that do not express SIX4 (5) vs lines expressing it (45) | 3.36× lower at baseline in the lines without SIX4 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CPLANE1, FGFR1 |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.543). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (16.1, 8.1); signed map (24.8, -11.8). **Vector** length 91.8, 21.7% of its response variance represented; |z| ≥ 3 in 1,065 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +28.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.8 | +15.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.7 | +24.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +12.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +12.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +8.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.8 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +1.8 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -0.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.2 | -0.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +2.7 |
|  | [[EX229 (drug)]] 5 µM |  | -4.2 | -4.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | +0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | +2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | -0.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | SIX homeobox 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.1 — chr14:60,709,539-60,724,351 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AREC3 |
| Gene groups (HGNC) | SINE class homeoboxes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UIU6](https://www.uniprot.org/uniprotkb/Q9UIU6) (Homeobox protein SIX4):

> Transcriptional regulator which can act as both a transcriptional repressor and activator by binding a DNA sequence on these target genes and is involved in processes like cell differentiation, cell migration and cell survival. Transactivates gene expression by binding a 5'-[CAT]A[CT][CT][CTG]GA[GAT]-3' motif present in the Trex site and a 5'-TCA[AG][AG]TTNC-3' motif present in the MEF3 site of the muscle-specific genes enhancer. Acts cooperatively with EYA proteins to transactivate their …

**Summary**, from NCBI Gene [51804](https://www.ncbi.nlm.nih.gov/gene/51804):

> This gene encodes a member of the homeobox family, subfamily SIX. The drosophila homolog is a nuclear homeoprotein required for eye development. Studies in mouse show that this gene product functions as a transcription factor, and may have a role in the differentiation or maturation of neuronal cells. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:10890](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10890) · Entrez [51804](https://www.ncbi.nlm.nih.gov/gene/51804) · UniProt [Q9UIU6](https://www.uniprot.org/uniprotkb/Q9UIU6) · Ensembl [ENSG00000100625](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100625)

## Data

Gene col 2003: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2003); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2003, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2003]; `tensor/DDL_lfc|DDL_z.npy` [2003]; `embed/gene_vectors.npy` [2003]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2003 or target_col == 2003). Every well: [[SIX4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIX4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
