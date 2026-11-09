---
symbol: "SGCB"
type: "gene"
col: 8626
ensembl_id: "ENSG00000163069"
name: "sarcoglycan beta"
location: "4q12"
module: 25
arm: "+"
pooled_cpm: 26.58
n_lines_expressing: 48
n_dd_up: 9
n_dd_down: 17
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# SGCB

*sarcoglycan beta* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.71× (z +17.3, q 0e+00, up in 31 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.34× (z +7.5, q 1e-11, up in 30 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.637× (z -11.5, q 8e-28, down in 28 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARPP19]] (+0.67, fdr 6e-05), [[DCK]] (+0.63, fdr 9e-06), [[GMFB]] (+0.61, fdr 1e-04); moves opposite to [[IL9RP3]] (-0.56, fdr 8e-05), [[C16orf91]] (-0.56, fdr 2e-04), [[KCNJ14]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KATNAL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8626.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.71×** | +17.3 | 0e+00 | 31/32 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +15.4 | 0e+00 | 38/43 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +10.1 | 8e-22 | 28/37 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +7.5 | 1e-11 | 30/46 (LS 180, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +7.3 | 3e-11 | 27/46 (SW480, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +5.4 | 5e-06 | 24/46 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.7 | 0.016 | 11/46 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.019 | 11/46 (NCI-H2347, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.21×** | +3.4 | 0.047 | 12/42 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.074 | 7/46 (NCI-H23, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8626.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.637×** | -11.5 | 8e-28 | 28/45 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.624×** | -8.5 | 6e-15 | 30/46 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.683×** | -6.9 | 1e-09 | 25/45 (SNU-1, H4, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.694×** | -6.6 | 7e-09 | 24/46 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.713×** | -5.8 | 1e-06 | 28/46 (CHP-212, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.730×** | -5.3 | 1e-05 | 23/46 (C32, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.824×** | -4.9 | 7e-05 | 21/46 (NCI-H1573, Hs 766T, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.768×** | -4.8 | 1e-04 | 23/46 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.924× | -4.7 | 2e-04 | 1/46 (SW 1088) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.775×** | -4.3 | 0.001 | 21/46 (A-172, SW 1088, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.786×** | -4.2 | 0.002 | 18/46 (SW 1088, HOP62, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.790×** | -4.1 | 0.002 | 20/46 (CFPAC-1, LOX-IMVI, …) | top dose only | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.799×** | -4.0 | 0.002 | 17/46 (MIA PaCa-2, SNU-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.792×** | -3.9 | 0.004 | 18/46 (HEC-1-A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.808×** | -3.8 | 0.005 | 21/45 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.869× | -3.6 | 0.013 | 14/46 (A-427, A498, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.877× | -3.3 | 0.029 | 12/46 (KATO III, A-172, …) | top dose only |  |
| [[PH-797804 (drug)]] 0.5 µM |  | **0.748×** | -3.1 | 0.049 | 8/46 (HCT15, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.759×** | -3.0 | 0.080 | 7/46 (MIA PaCa-2, LS 180, …) | all doses, flat | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8626. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 49.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.24× (z +12.7) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 31.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.50× (z +10.4) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.287× (z -8.7) |
| [[HOP62 (line)]] | alt | 55.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.64× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -15.5) |
| [[HS-578T (line)]] | alt | 38.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -12.0) |
| [[LS 180 (line)]] | wt | 37.0 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.99× (z +9.2) | [[Bortezomib (drug)]] 5 µM 0.112× (z -10.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.448× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 22.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.02× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -11.9) |
| [[PANC-1 (line)]] | alt | 23.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.66× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -12.4) |
| [[A-172 (line)]] | wt | 63.0 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.300× (z -11.3) |
| [[CHP-212 (line)]] | wt | 32.7 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.0704× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 24.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 27.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -16.6) |
| [[HEC-1-A (line)]] | alt | 41.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -9.3) |
| [[J82 (line)]] | alt | 24.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 8.51 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.22× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 23.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 18.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.43× (z +13.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 30.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -9.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.66 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.32 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8626), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARPP19]] | +0.67 | +0.38 / +0.72 | both halves | 6e-05 |  |
| [[DCK]] | +0.63 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[GMFB]] | +0.61 | +0.34 / +0.70 | both halves | 1e-04 |  |
| [[DHFR]] | +0.61 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[SCCPDH]] | +0.61 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[DCTN1]] | +0.61 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[MANEA]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[MMGT1]] | +0.59 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[FSTL1]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[DR1]] | +0.58 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[TMEM106B]] | +0.58 | +0.35 / +0.63 | both halves | 1e-04 |  |
| [[AIDA]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL9RP3]] | -0.56 | -0.37 / -0.57 | both halves | 8e-05 |  |
| [[C16orf91]] | -0.56 | -0.29 / -0.59 | both halves | 2e-04 |  |
| [[KCNJ14]] | -0.55 | -0.42 / -0.66 | both halves | 4e-05 |  |
| [[MRPL36]] | -0.54 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[DRD4]] | -0.54 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[FBXL18]] | -0.54 | -0.37 / -0.59 | both halves | 9e-05 |  |
| [[ZNF593]] | -0.54 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[RPL36AL]] ⚠ | -0.53 | -0.33 / -0.56 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[NUDT22]] | -0.53 | -0.28 / -0.55 | both halves | 3e-04 |  |
| [[DTX2P1-UPK3BP1-PMS2P11]] | -0.53 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[MRPL23]] | -0.52 | -0.23 / -0.60 | both halves | 5e-04 |  |
| [[EIF5B]] | -0.52 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[ZBTB7A]] | -0.52 | -0.32 / -0.62 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL1]] | B | KATNAL1 activity weakens SGCB's drug response | lines that do not express KATNAL1 (6) vs lines expressing it (40) | the lines without KATNAL1 respond 1.09× as strongly (z diff +0.06); strongest at Tucidinostat 5 µM: 2.29x vs 1.23x (z diff -5.0) | 0.099 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.643). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-28.7, -19.9); signed map (-18.2, -38.7). **Vector** length 101, 23.5% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +17.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.5 | +10.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +7.1 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +7.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.3 | +2.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +2.7 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -3.4 | -5.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.6 | -3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.6 | -11.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.6 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.4 | -8.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.4 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | sarcoglycan beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:52,020,706-52,038,299 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SGC, A3b; previously LGMD2E |
| Gene groups (HGNC) | Sarcoglycans |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 3 pathways, smallest: Formation of the dystrophin-glycoprotein complex (DGC); Non-integrin membrane-ECM interactions; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16585](https://www.uniprot.org/uniprotkb/Q16585) (Beta-sarcoglycan):

> Component of the sarcoglycan complex, a subcomplex of the dystrophin-glycoprotein complex which forms a link between the F-actin cytoskeleton and the extracellular matrix.

**Summary**, from NCBI Gene [6443](https://www.ncbi.nlm.nih.gov/gene/6443):

> This gene encodes a member of the sarcoglycan family. Sarcoglycans are transmembrane components in the dystrophin-glycoprotein complex which help stabilize the muscle fiber membranes and link the muscle cytoskeleton to the extracellular matrix. Mutations in this gene have been associated with limb-girdle muscular dystrophy.[provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:10806](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10806) · Entrez [6443](https://www.ncbi.nlm.nih.gov/gene/6443) · UniProt [Q16585](https://www.uniprot.org/uniprotkb/Q16585) · Ensembl [ENSG00000163069](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163069)

## Data

Gene col 8626: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8626); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8626, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8626]; `tensor/DDL_lfc|DDL_z.npy` [8626]; `embed/gene_vectors.npy` [8626]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8626 or target_col == 8626). Every well: [[SGCB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SGCB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
