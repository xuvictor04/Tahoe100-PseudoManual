---
symbol: "AASS"
type: "gene"
col: 168
ensembl_id: "ENSG00000008311"
name: "aminoadipate-semialdehyde synthase"
location: "7q31.32"
module: 217
arm: "+"
pooled_cpm: 32.14
n_lines_expressing: 43
n_dd_up: 28
n_dd_down: 6
n_dd_up_clean: 26
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/217"]
generated_by: "tahoemap"
---

# AASS

*aminoadipate-semialdehyde synthase* — 7q31.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.38× (z +48.9, q 0e+00, up in 41 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.904× (z -7.1, q 8e-10, down in 4 of 41 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.776× (z -5.2, q 4e-05, down in 21 of 41 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WASL]] (+0.57, fdr 3e-05), [[BCL6]] (+0.55, fdr 3e-05), [[ZNF608]] (+0.48, fdr 4e-05); moves opposite to [[POP1]] (-0.49, fdr 4e-05), [[DGCR8]] (-0.47, fdr 4e-05), [[LINC02985]] (-0.47, fdr 3e-05).
> It is in [[Module 217]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[ZFP36]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 2 with an alert ⚠; shown: the 15 strongest. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 168.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.38×** | +48.9 | 0e+00 | 41/41 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +21.7 | 0e+00 | 37/41 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.81×** | +21.2 | 0e+00 | 41/41 (SW1417, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.90×** | +21.0 | 0e+00 | 36/41 (NCI-H1792, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.78×** | +21.0 | 0e+00 | 40/41 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.66×** | +20.1 | 0e+00 | 40/41 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.60×** | +19.6 | 0e+00 | 32/40 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.14×** | +15.7 | 0e+00 | 38/41 (SW1417, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +11.6 | 5e-29 | 29/41 (A-172, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.70×** | +10.9 | 7e-26 | 32/40 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +10.1 | 2e-22 | 27/40 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +9.2 | 2e-18 | 27/41 (A-172, HOP62, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.12×** | +8.1 | 2e-14 | 34/41 (LoVo, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.45×** | +7.6 | 1e-12 | 27/40 (H4, NCI-H460, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +6.5 | 3e-09 | 18/41 (LOX-IMVI, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 168.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.904× | -7.1 | 8e-10 | 4/41 (HCT15, C32, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.746×** | -6.0 | 6e-07 | 22/41 (A498, A-427, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.776×** | -5.2 | 4e-05 | 21/41 (NCI-H2030, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~9% of this change | 0.837× | -3.6 | 0.041 | 13/40 (CHP-212, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **0.828×** | -3.6 | 0.042 | 16/40 (HepG2/C3A, HCT15, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.838× | -3.5 | 0.046 | 15/39 (NCI-H1573, SW480, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.725×** | -3.4 | 0.046 | 10/41 (A498, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.729×** | -3.4 | 0.052 | 14/41 (A498, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -3.2 | 0.076 | 15/41 (SW480, NCI-H1573, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.744×** | -3.2 | 0.089 | 9/40 (A498, A-427, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.751× | -3.1 | 0.11 | 15/41 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cyclosporin A (drug)]] 5 µM |  | 0.861× | -3.0 | 0.11 | 6/41 (A498, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 168. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 44.1 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +21.5) | — |
| [[C32 (line)]] | wt | 36.2 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 46.5× (z +31.4) | — |
| [[LoVo (line)]] | wt | 55.0 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.68× (z +31.9) | — |
| [[LS 180 (line)]] | wt | 33.6 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.32× (z +22.2) | — |
| [[NCI-H460 (line)]] | wt | 14.1 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +26.5) | — |
| [[SW480 (line)]] | alt | 29.1 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +25.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.402× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 44.7 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +23.4) | — |
| [[HOP62 (line)]] | alt | 34.2 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +28.8) | — |
| [[J82 (line)]] | alt | 57.2 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +20.6) | — |
| [[LOX-IMVI (line)]] | wt | 59.0 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.43× (z +28.4) | — |
| [[RPMI-7951 (line)]] | alt | 62.2 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.73× (z +25.0) | — |
| [[SK-MEL-2 (line)]] | alt | 75.8 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +22.5) | — |
| [[SW1417 (line)]] | alt | 31.9 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.03× (z +22.0) | — |
| [[A498 (line)]] | wt | 36.6 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +19.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.370× (z -9.2) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 55.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +16.9) | — |
| [[SW 900 (line)]] | alt | 45.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.42× (z +24.4) | — |
| [[NCI-H2347 (line)]] | alt | 21.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.43× (z +21.6) | — |
| [[Panc 03.27 (line)]] | alt | 43.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +19.4) | — |
| [[CFPAC-1 (line)]] | alt | 28.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.89× (z +23.3) | — |
| [[hTERT-HPNE (line)]] | wt | 56.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.0× (z +27.6) | — |
| [[NCI-H1573 (line)]] | alt | 12.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +13.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.189× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 76.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.98× (z +33.2) | — |
| [[NCI-H2030 (line)]] | alt | 22.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +13.5) | — |
| [[RKO (line)]] | wt | 129 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +17.5) | — |
| [[BT-474 (line)]] | alt | 10.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +15.2) | — |
| [[NCI-H23 (line)]] | alt | 16.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.95× (z +11.3) | — |
| [[CHP-212 (line)]] | wt | 49.3 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0786× (z -11.5) ⚠ transcription drop; cell-cycle shift, explains ~9% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.224× (z -9.6) |
| [[HS-578T (line)]] | alt | 26.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.09× (z +20.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 47.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +19.1) | — |
| [[SW 1271 (line)]] | alt | 100.0 | 0 | 2 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.101× (z -10.6) |
| [[A-427 (line)]] | wt | 14.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +10.0) | — |
| [[HCT15 (line)]] | alt | 56.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +12.9) | — |
| [[HepG2_C3A (line)]] | wt | 13.8 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.132× (z -8.5) |
| [[Hs 766T (line)]] | wt | 28.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +10.0) | — |
| [[NCI-H2122 (line)]] | alt | 27.8 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.54× (z +17.1) | — |
| [[SHP-77 (line)]] | alt | 38.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 37.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +11.7) | — |
| [[SW 1088 (line)]] | alt | 33.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +9.3) | — |
| [[SW48 (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0903× (z -10.5) ⚠ transcription drop |
| [[A549 (line)]] | wt | 4.98 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 167 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.30 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.33 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.71 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 168), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASL]] | +0.57 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[BCL6]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[ZNF608]] | +0.48 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[TPCN1]] | +0.48 | +0.33 / +0.51 | both halves | 1e-04 |  |
| [[TXNDC16]] | +0.48 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[KLF9]] | +0.48 | +0.40 / +0.48 | both halves | 4e-05 |  |
| [[LINC00598]] | +0.47 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[FOXG1]] | +0.47 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[ATOSA]] | +0.46 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[NBR1]] | +0.46 | +0.59 / +0.33 | both halves | 1e-04 |  |
| [[BMAL1]] | +0.46 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[DPYD]] | +0.46 | +0.48 / +0.47 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*46 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POP1]] | -0.49 | -0.43 / -0.43 | both halves | 4e-05 |  |
| [[DGCR8]] | -0.47 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[LINC02985]] | -0.47 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[CHCHD6]] | -0.47 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[SORD]] | -0.47 | -0.52 / -0.39 | both halves | 6e-05 | same gene group |
| [[LSP1P4]] | -0.46 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[LIMD1]] | -0.46 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[RRP7BP]] | -0.46 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[MRPS23]] | -0.46 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[ARMH3]] | -0.46 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[EYA3]] | -0.45 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[SNX21]] | -0.44 | -0.45 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AASS's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RHOBTB3]] | B | RHOBTB3 activity raises AASS's level | lines that do not express RHOBTB3 (10) vs lines expressing it (40) | 2.45× lower at baseline in the lines without RHOBTB3 | 0.049 | ⚠ within organs, on part of the lines; also absent: FYN, POGLUT3; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity raises AASS's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFP36]] | B | AASS activity lowers ZFP36's level | lines that do not express AASS (7) vs lines expressing it (43) | 2.08× higher at baseline in the lines without AASS | 0.029 | ⚠ within organs, on part of the lines; also absent: LINC00159, ZNF391, DISC1 |
| [[EPS15L1]] | B | AASS activity raises EPS15L1's level | lines that do not express AASS (7) vs lines expressing it (43) | 1.35× lower at baseline in the lines without AASS | 0.069 | ⚠ within organs, on part of the lines; also absent: LINC00159, ZNF391, DISC1 |
| [[SHOC2]] | B | AASS activity lowers SHOC2's level | lines that do not express AASS (7) vs lines expressing it (43) | 1.25× higher at baseline in the lines without AASS | 0.088 | ⚠ within organs, on part of the lines; also absent: LINC00159, ZNF391, DISC1 |

## Where it sits

- **Module**: [[Module 217]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.564). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.8, 15.6); signed map (14.3, 25.7). **Vector** length 84.6, 19.5% of its response variance represented; |z| ≥ 3 in 1,304 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +48.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.6 | +21.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +11.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.2 | +7.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.1 | +4.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.1 | +4.9 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.1 | +2.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.1 | +5.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -7.4 | -3.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.1 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.0 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -1.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.4 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -1.5 |
|  | [[EX229 (drug)]] 5 µM |  | -3.2 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.2 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | aminoadipate-semialdehyde synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.32 — chr7:122,064,583-122,144,308 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LORSDH, LKRSDH, LKR/SDH |
| Gene groups (HGNC) | Oxidoreductases |
| Reactome | 2 pathways, smallest: Lysine catabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UDR5](https://www.uniprot.org/uniprotkb/Q9UDR5) (Alpha-aminoadipic semialdehyde synthase, mitochondrial):

> Bifunctional enzyme that catalyzes the first two steps in lysine degradation.

**Summary**, from NCBI Gene [10157](https://www.ncbi.nlm.nih.gov/gene/10157):

> This gene encodes a bifunctional enzyme that catalyzes the first two steps in the mammalian lysine degradation pathway. The N-terminal and the C-terminal portions of this enzyme contain lysine-ketoglutarate reductase and saccharopine dehydrogenase activity, respectively, resulting in the conversion of lysine to alpha-aminoadipic semialdehyde. Mutations in this gene are associated with familial hyperlysinemia. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17366](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17366) · Entrez [10157](https://www.ncbi.nlm.nih.gov/gene/10157) · UniProt [Q9UDR5](https://www.uniprot.org/uniprotkb/Q9UDR5) · Ensembl [ENSG00000008311](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008311)

## Data

Gene col 168: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 168); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 168, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 168]; `tensor/DDL_lfc|DDL_z.npy` [168]; `embed/gene_vectors.npy` [168]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 168 or target_col == 168). Every well: [[AASS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AASS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
