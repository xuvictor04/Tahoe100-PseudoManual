---
symbol: "SETDB2"
type: "gene"
col: 5831
ensembl_id: "ENSG00000136169"
name: "SET domain bifurcated histone lysine methyltransferase 2"
location: "13q14.2"
module: 36
arm: "-"
pooled_cpm: 19.54
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 10
n_dd_up_clean: 15
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# SETDB2

*SET domain bifurcated histone lysine methyltransferase 2* — 13q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.50× (z +24.5, q 0e+00, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.596× (z -9.8, q 1e-19, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PATL1]] (+0.58, fdr 3e-05), [[ETFRF1]] (+0.56, fdr 3e-05), [[CYB5RL]] (+0.55, fdr 2e-05); moves opposite to [[ARPC5L]] (-0.60, fdr 4e-05), [[RAB5IF]] (-0.56, fdr 2e-05), [[FBXW11]] (-0.55, fdr 8e-06).
> It sits in the **-** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5831.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.50×** | +24.5 | 0e+00 | 40/47 (A-172, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.02×** | +12.8 | 7e-35 | 32/47 (COLO 205, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +11.2 | 1e-26 | 32/47 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +9.1 | 1e-17 | 32/48 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +8.2 | 2e-14 | 27/47 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.38×** | +6.1 | 8e-08 | 24/48 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +6.0 | 2e-07 | 18/47 (A-172, Hs 766T, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +6.0 | 2e-07 | 22/45 (NCI-H23, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +5.4 | 5e-06 | 18/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +5.4 | 5e-06 | 18/47 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +5.1 | 2e-05 | 19/48 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.20×** | +4.9 | 4e-05 | 16/47 (NCI-H2347, COLO 205, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.19× | +4.7 | 1e-04 | 16/48 (C32, J82, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +4.7 | 1e-04 | 18/47 (SW480, SW48, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.57×** | +4.5 | 3e-04 | 7/48 (HT-29, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.4 | 5e-04 | 14/48 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.010 | 12/48 (HT-29, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Afatinib (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.034 | 8/48 (HEC-1-A, BT-474, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5831.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.596×** | -9.8 | 1e-19 | 32/47 (SW480, A-427, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.700×** | -6.7 | 5e-09 | 25/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.701×** | -6.3 | 5e-08 | 20/48 (SW48, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.921× | -5.5 | 5e-06 | 4/48 (AsPC-1, SHP-77, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **0.610×** | -4.9 | 1e-04 | 17/43 (C32, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.628×** | -4.6 | 4e-04 | 10/25 (SW480, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.797×** | -4.3 | 0.001 | 18/47 (SW480, HEC-1-A, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.816×** | -3.8 | 0.009 | 13/47 (KATO III, PANC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.693×** | -3.6 | 0.018 | 9/48 (PANC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.757×** | -3.6 | 0.018 | 12/47 (RPMI-7951, SW1417, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.710×** | -3.4 | 0.039 | 11/36 (HCT15, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.839× | -3.3 | 0.043 | 7/47 (HCT15, HepG2/C3A, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.840× | -3.3 | 0.043 | 10/47 (NCI-H23, C32, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.848× | -3.1 | 0.074 | 9/47 (NCI-H661, H4, …) | two highest doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5831. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 50.9 | 3 | 4 (1 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.39× (z +9.7) | [[Auranofin (drug)]] 5 µM 0.352× (z -12.1) |
| [[A-172 (line)]] | wt | 28.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +22.2) | — |
| [[NCI-H460 (line)]] | wt | 15.5 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.26× (z +18.6) | — |
| [[COLO 205 (line)]] | alt | 48.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.18× (z +19.2) | — |
| [[NCI-H2347 (line)]] | alt | 7.53 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.44× (z +15.5) | — |
| [[Hs 766T (line)]] | wt | 33.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +16.4) | — |
| [[LS 180 (line)]] | wt | 15.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +13.8) | — |
| [[NCI-H1573 (line)]] | alt | 16.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +13.1) | — |
| [[A-427 (line)]] | wt | 24.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +13.5) | — |
| [[A498 (line)]] | wt | 18.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +11.5) | — |
| [[C32 (line)]] | wt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 9.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +9.4) | — |
| [[H4 (line)]] | wt | 20.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +10.9) | — |
| [[HT-29 (line)]] | alt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +10.7) | — |
| [[LoVo (line)]] | wt | 12.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 23.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +12.1) | — |
| [[Panc 03.27 (line)]] | alt | 20.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change |
| [[SK-MEL-2 (line)]] | alt | 12.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +11.0) | — |
| [[SNU-423 (line)]] | alt | 36.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +9.0) | — |
| [[SW48 (line)]] | wt | 17.3 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0442× (z -12.6) |
| [[A549 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5831), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PATL1]] | +0.58 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[ETFRF1]] | +0.56 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[CYB5RL]] | +0.55 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[VPS13C]] | +0.55 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[TRMT13]] | +0.55 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[CLK4]] | +0.54 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[ABCA5]] | +0.54 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[ZC3H6]] | +0.54 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[TAF9]] | +0.53 | +0.55 / +0.47 | both halves | 2e-05 | pathway: Chromatin modifying enzymes |
| [[KPNA5]] | +0.53 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[C1orf43]] | +0.53 | +0.64 / +0.32 | both halves | 1e-04 |  |
| [[WDSUB1]] | +0.52 | +0.51 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARPC5L]] | -0.60 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[RAB5IF]] | -0.56 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[FBXW11]] | -0.55 | -0.57 / -0.57 | both halves | 8e-06 |  |
| [[LRRC8A]] | -0.55 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[CAP1]] | -0.55 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[TRAPPC10]] | -0.54 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[FRMD8]] | -0.53 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[PPP6R1]] | -0.53 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[RNF216]] | -0.53 | -0.64 / -0.32 | both halves | 1e-04 |  |
| [[PRDX1]] | -0.53 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[FBXL18]] | -0.52 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[MYO9B]] | -0.52 | -0.58 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises SETDB2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers SETDB2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **-** arm (projection on the module's main direction -0.462). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (16.9, -8.5); signed map (10.5, -21.2). **Vector** length 85.0, 16.9% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.2 | +12.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +24.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +11.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.9 | +5.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +5.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | +3.2 |
|  | [[Afatinib (drug)]] 5 µM |  | +1.6 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | -1.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.0 | -9.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.4 | -6.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.0 | -6.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.3 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -4.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -0.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | SET domain bifurcated histone lysine methyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.2 — chr13:49,444,274-49,495,003 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CLLD8, CLLL8, KMT1F; previously C13orf4 |
| Gene groups (HGNC) | Histone lysine methyltransferases; Methyl-CpG binding domain containing; SET domain containing |
| Reactome | 3 pathways, smallest: PKMTs methylate histone lysines; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96T68](https://www.uniprot.org/uniprotkb/Q96T68) (Histone-lysine N-methyltransferase SETDB2):

> Histone methyltransferase involved in left-right axis specification in early development and mitosis. Specifically trimethylates 'Lys-9' of histone H3 (H3K9me3). H3K9me3 is a specific tag for epigenetic transcriptional repression that recruits HP1 (CBX1, CBX3 and/or CBX5) proteins to methylated histones. Contributes to H3K9me3 in both the interspersed repetitive elements and centromere-associated repeats. Plays a role in chromosome condensation and segregation during mitosis.

**Summary**, from NCBI Gene [83852](https://www.ncbi.nlm.nih.gov/gene/83852):

> This gene encodes a member of a family of proteins that contain a methyl-CpG-binding domain (MBD) and a SET domain and function as histone methyltransferases. This protein is recruited to heterochromatin and plays a role in the regulation of chromosome segregation. This region is commonly deleted in chronic lymphocytic leukemia. Naturally-occuring readthrough transcription occurs from this gene to the downstream PHF11 (PHD finger protein 11) gene. Alternative splicing results in multiple …

**Accessions** — [HGNC:20263](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20263) · Entrez [83852](https://www.ncbi.nlm.nih.gov/gene/83852) · UniProt [Q96T68](https://www.uniprot.org/uniprotkb/Q96T68) · Ensembl [ENSG00000136169](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136169)

## Data

Gene col 5831: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5831); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5831, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5831]; `tensor/DDL_lfc|DDL_z.npy` [5831]; `embed/gene_vectors.npy` [5831]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5831 or target_col == 5831). Every well: [[SETDB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SETDB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
