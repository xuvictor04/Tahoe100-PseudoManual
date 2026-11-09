---
symbol: "ACVR1C"
type: "gene"
col: 4451
ensembl_id: "ENSG00000123612"
name: "activin A receptor type 1C"
location: "2q24.1"
module: 37
arm: "+"
pooled_cpm: 9.52
n_lines_expressing: 46
n_dd_up: 31
n_dd_down: 22
n_dd_up_clean: 29
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# ACVR1C

*activin A receptor type 1C* — 2q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.04× (z +20.2, q 0e+00, up in 29 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.888× (z -5.3, q 8e-05, down in 8 of 44 measured lines) ⚠ position not correctable. The strongest without an alert is [[Dexamethasone (drug)]] 5 µM: 0.688× (z -4.8, q 5e-04, down in 17 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPHS1]] (+0.70, fdr 7e-06), [[POU2F2]] (+0.67, fdr 7e-06), [[LINC01033]] (+0.65, fdr 7e-06); moves opposite to [[COPS8]] (-0.62, fdr 1e-05), [[PPP5C]] (-0.58, fdr 1e-05), [[ARMC8]] (-0.58, fdr 4e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LINC01060]] → it (grade B ⚠); 2 go from it, the strongest it → [[NPHS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 2 with an alert ⚠; shown: the 15 strongest. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4451.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.04×** | +20.2 | 0e+00 | 29/37 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.98×** | +14.0 | 3e-42 | 31/36 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.91×** | +13.7 | 2e-40 | 37/42 (A-172, NCI-H23, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.12×** | +13.6 | 5e-40 | 33/42 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +12.0 | 6e-31 | 25/40 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.22×** | +10.3 | 1e-22 | 29/41 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +7.0 | 2e-10 | 17/43 (RPMI-7951, H4, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.72×** | +6.9 | 3e-10 | 22/43 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.65×** | +6.4 | 1e-08 | 23/42 (hTERT-HPNE, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.62×** | +6.2 | 3e-08 | 16/42 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.61×** | +6.1 | 6e-08 | 18/41 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.47×** | +6.1 | 6e-08 | 18/40 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +5.7 | 4e-07 | 17/42 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.51×** | +5.3 | 5e-06 | 12/41 (NCI-H460, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +5.0 | 2e-05 | 16/42 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4451.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.888× | -5.3 | 8e-05 | 8/44 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.688×** | -4.8 | 5e-04 | 17/42 (HOP62, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.499×** | -4.7 | 6e-04 | 16/40 (NCI-H1573, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.704×** | -4.5 | 8e-04 | 15/42 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.705×** | -4.5 | 8e-04 | 20/43 (HOP62, RKO, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.704×** | -4.3 | 0.001 | 14/32 (LOX-IMVI, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **0.733×** | -4.0 | 0.005 | 15/41 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.734×** | -4.0 | 0.005 | 13/43 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.737×** | -3.9 | 0.006 | 16/42 (NCI-H460, HOP62, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.569×** | -3.8 | 0.009 | 12/36 (HS-578T, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.817×** | -3.7 | 0.012 | 12/41 (HS-578T, HOP62, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.757×** | -3.6 | 0.015 | 16/41 (HOP62, NCI-H460, …) | two highest doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.758×** | -3.6 | 0.015 | 15/41 (HOP62, NCI-H2030, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.758×** | -3.6 | 0.015 | 12/42 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.761×** | -3.3 | 0.044 | 12/39 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.783×** | -3.1 | 0.060 | 12/41 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[Econazole (drug)]] 5 µM |  | **0.787×** | -3.1 | 0.070 | 8/43 (NCI-H460, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4451. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.8 | 13 (6 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.75× (z +24.0) | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.303× (z -8.9) |
| [[HOP62 (line)]] | alt | 18.5 | 0 | 6 (3 ⚠) | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.128× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 28.6 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0434× (z -18.5) ⚠ toxic |
| [[LoVo (line)]] | wt | 7.65 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +13.6) | [[Belumosudil (drug)]] 5 µM 0.156× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 14.0 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0565× (z -13.4) ⚠ toxic |
| [[SW480 (line)]] | alt | 4.79 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.80× (z +11.9) | — |
| [[A-172 (line)]] | wt | 5.56 | 1 | 0 | [[Auranofin (drug)]] 5 µM 19.7× (z +10.3) | — |
| [[C32 (line)]] | wt | 13.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 5.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.94× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 8.51 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0934× (z -8.7) ⚠ toxic |
| [[J82 (line)]] | alt | 4.53 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0898× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 21.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 10.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 6.50 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0989× (z -8.5) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 11.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.125× (z -8.8) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 16.1 | 0 | 1 | — | [[Nevirapine (drug)]] 0.05 µM 0.0842× (z -9.2) |
| [[A-427 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.98 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4451), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPHS1]] | +0.70 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[POU2F2]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[LINC01033]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[LINC01619]] | +0.63 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[C12orf50]] | +0.62 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[CFAP53]] | +0.61 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[CCNP]] | +0.60 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[LINC01291]] | +0.60 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[ZNNT1]] | +0.60 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[LINC02154]] | +0.60 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[LINC02220]] | +0.60 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[PIWIL2]] | +0.60 | +0.60 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS8]] | -0.62 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[PPP5C]] | -0.58 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[ARMC8]] | -0.58 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[NDUFV1]] | -0.57 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[MRPL3]] | -0.56 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[WDR5]] | -0.56 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[CSE1L]] | -0.55 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[MTERF3]] | -0.55 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[PRMT7]] | -0.54 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[SNRNP40]] | -0.54 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[TTI1]] | -0.54 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[ALG6]] | -0.53 | -0.58 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01060]] | B | LINC01060 activity raises ACVR1C's level | lines that do not express LINC01060 (29) vs lines expressing it (21) | 1.86× lower at baseline in the lines without LINC01060 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000260289, ENSG00000287598, NTM |
| [[KCNIP4]] | B | KCNIP4 activity raises ACVR1C's level | lines that do not express KCNIP4 (6) vs lines expressing it (44) | 2.74× lower at baseline in the lines without KCNIP4 | 0.022 | ⚠ within organs, on part of the lines; also absent: MLLT3, TEX9, MAMDC2-AS1; maybe low, not absent |
| [[INHBA]] | B | INHBA activity raises ACVR1C's level | lines that do not express INHBA (32) vs lines expressing it (18) | 1.87× lower at baseline in the lines without INHBA | 0.024 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, DSCAM, TNIP3 |
| [[CCL3]] | B | CCL3 activity raises ACVR1C's level | lines that do not express CCL3 (37) vs lines expressing it (13) | 1.97× lower at baseline in the lines without CCL3 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1 |
| [[SNCAIP]] | B | SNCAIP activity raises ACVR1C's level | lines that do not express SNCAIP (20) vs lines expressing it (30) | 1.69× lower at baseline in the lines without SNCAIP | 0.032 | ⚠ within organs, on part of the lines; also absent: LIMCH1, RNF152, FLT1 |
| [[NR3C1]] | B | NR3C1 activity lowers ACVR1C's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPHS1]] | C | ACVR1C activity lowers NPHS1's level | lines that do not express ACVR1C (4) vs lines expressing it (46) | 1.98× higher at baseline in the lines without ACVR1C | 0.018 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CORIN, HDAC2-AS2, ENSG00000249951; maybe low, not absent |
| [[CLN8]] | C | ACVR1C activity strengthens CLN8's drug response | lines that do not express ACVR1C (4) vs lines expressing it (43) | the lines without ACVR1C respond 0.28× as strongly (z diff +2.87); strongest at Homoharringtonine 5 µM: 0.81x vs 1.48x (z diff +6.4) | 0.045 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CORIN, HDAC2-AS2, ENSG00000249951; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.507). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.5, -11.3); signed map (18.9, 16.5). **Vector** length 93.8, 19.5% of its response variance represented; |z| ≥ 3 in 1,197 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.9 | +13.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.6 | +13.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.1 | +10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +12.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +20.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +6.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.4 | +2.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.4 | -4.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.0 | -4.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.5 | -4.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.4 | -4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -3.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | activin A receptor type 1C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.1 — chr2:157,526,767-157,628,864 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ALK7, ACVRLK7 |
| Gene groups (HGNC) | Type 1 receptor serine/threonine kinases |
| Reactome | 4 pathways, smallest: Regulation of signaling by NODAL; Signaling by NODAL; Signaling by Activin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NER5](https://www.uniprot.org/uniprotkb/Q8NER5) (Activin receptor type-1C):

> Serine/threonine protein kinase which forms a receptor complex on ligand binding. The receptor complex consists of 2 type II and 2 type I transmembrane serine/threonine kinases. Type II receptors phosphorylate and activate type I receptors which autophosphorylate, then bind and activate SMAD transcriptional regulators, SMAD2 and SMAD3. Receptor for activin AB, activin B, activin E and NODAL. Upon NODAL binding, activation results in increased apoptosis and reduced proliferation through …

**Summary**, from NCBI Gene [130399](https://www.ncbi.nlm.nih.gov/gene/130399):

> ACVR1C is a type I receptor for the TGFB (see MIM 190180) family of signaling molecules. Upon ligand binding, type I receptors phosphorylate cytoplasmic SMAD transcription factors, which then translocate to the nucleus and interact directly with DNA or in complex with other transcription factors (Bondestam et al., 2001 [PubMed 12063393]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:18123](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18123) · Entrez [130399](https://www.ncbi.nlm.nih.gov/gene/130399) · UniProt [Q8NER5](https://www.uniprot.org/uniprotkb/Q8NER5) · Ensembl [ENSG00000123612](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123612)

## Data

Gene col 4451: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4451); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4451, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4451]; `tensor/DDL_lfc|DDL_z.npy` [4451]; `embed/gene_vectors.npy` [4451]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4451 or target_col == 4451). Every well: [[ACVR1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACVR1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
