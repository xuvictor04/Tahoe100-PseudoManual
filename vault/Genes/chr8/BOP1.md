---
symbol: "BOP1"
type: "gene"
col: 15334
ensembl_id: "ENSG00000261236"
name: "BOP1 ribosomal biogenesis factor"
location: "8q24.3"
module: 4
arm: "+"
pooled_cpm: 10.78
n_lines_expressing: 50
n_dd_up: 47
n_dd_down: 2
n_dd_up_clean: 26
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# BOP1

*BOP1 ribosomal biogenesis factor* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 47 drug-doses (21 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.15× (z +17.9, q 0e+00, up in 34 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 2.08× (z +8.0, q 1e-13, up in 33 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.596× (z -5.4, q 3e-05, down in 24 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C-33 A 0.158×, A-427 0.160×; ⚠ cell-cycle shift, would explain all of this change); [[Bortezomib (drug)]] 5 µM in 1 line (RKO 0.0418×; ⚠ toxic); [[Trimetrexate (drug)]] 5 µM in 1 line (SNU-1 0.164×); [[Procainamide (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.0932×); [[Verteporfin (drug)]] 5 µM in 1 line (A-172 0.103×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYBBP1A]] (+0.79, fdr 7e-06), [[NOC2L]] (+0.77, fdr 7e-06), [[WDR77]] (+0.77, fdr 7e-06); moves opposite to [[ZNF821]] (-0.66, fdr 1e-05), [[SELENOK]] (-0.65, fdr 7e-06), [[ZMYM5]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[JPH1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 21 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 47 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15334.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **5.15×** | +17.9 | 0e+00 | 34/36 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **4.01×** | +14.6 | 1e-45 | 16/17 (A549, A498, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **3.31×** | +13.0 | 1e-36 | 45/47 (HOP62, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.34×** | +12.2 | 7e-32 | 21/23 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.73×** | +11.0 | 7e-26 | 43/46 (HOP62, KATO III, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.64×** | +10.6 | 3e-24 | 43/46 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.29×** | +9.0 | 1e-17 | 37/46 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.08×** | +8.0 | 1e-13 | 33/45 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~15% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **2.10×** | +7.8 | 5e-13 | 26/36 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **2.09×** | +7.7 | 6e-13 | 26/37 (LOX-IMVI, HS-578T, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.94×** | +6.9 | 2e-10 | 31/46 (PANC-1, HS-578T, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.81×** | +6.5 | 5e-09 | 29/46 (PANC-1, LOX-IMVI, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **2.86×** | +6.0 | 9e-08 | 29/41 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.50×** | +5.2 | 7e-06 | 25/42 (A498, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **2.49×** | +5.2 | 8e-06 | 26/43 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **2.41×** | +5.0 | 2e-05 | 17/37 (PANC-1, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.40×** | +5.0 | 2e-05 | 27/45 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +4.3 | 4e-04 | 19/46 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.48×** | +4.2 | 6e-04 | 17/46 (NCI-H23, NCI-H460, …) | two highest doses |  |
| [[EX229 (drug)]] 0.05 µM |  | **1.48×** | +4.0 | 0.001 | 16/46 (SNU-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.001 | 16/43 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **2.00×** | +4.0 | 0.002 | 10/38 (A498, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.93×** | +3.8 | 0.003 | 15/37 (PANC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.62×** | +3.8 | 0.003 | 8/46 (LOX-IMVI, A498, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15334.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C-33 A 0.158×, A-427 0.160×; ⚠ cell-cycle shift, would explain all of this change); [[Bortezomib (drug)]] 5 µM in 1 line (RKO 0.0418×; ⚠ toxic); [[Trimetrexate (drug)]] 5 µM in 1 line (SNU-1 0.164×); [[Procainamide (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.0932×); [[Verteporfin (drug)]] 5 µM in 1 line (A-172 0.103×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.596×** | -5.4 | 3e-05 | 24/45 (C-33 A, A-172, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.685×** | -3.8 | 0.038 | 16/47 (LoVo, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Meloxicam (drug)]] 0.5 µM |  | 0.737× | -3.4 | 0.14 | 13/46 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Rifaximin (drug)]] 5 µM |  | 0.733× | -3.3 | 0.14 | 9/46 (hTERT-HPNE, HT-29, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | 0.747× | -3.2 | 0.14 | 12/47 (MIA PaCa-2, LoVo, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Bimiralisib (drug)]] 0.05 µM |  | 0.740× | -3.1 | 0.17 | 8/46 (HepG2/C3A, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.757× | -3.1 | 0.18 | 9/46 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.72 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15334. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.92 | 0 | 2 | — | [[Procainamide (hydrochloride) (drug)]] 5 µM 0.0932× (z -8.8) |
| [[A498 (line)]] | wt | 13.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[C-33 A (line)]] | alt | 16.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 17.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 13.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.69× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[C32 (line)]] | wt | 6.15 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HOP62 (line)]] | alt | 6.17 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.30× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HS-578T (line)]] | alt | 13.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.50× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LoVo (line)]] | wt | 9.02 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.1× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 14.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.12× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H460 (line)]] | wt | 7.30 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.53× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[PANC-1 (line)]] | alt | 16.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[RKO (line)]] | wt | 24.6 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0418× (z -9.1) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 9.83 | 0 | 1 | — | [[Trimetrexate (drug)]] 5 µM 0.164× (z -8.9) |
| [[AN3 CA (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15334), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYBBP1A]] | +0.79 | +0.81 / +0.73 | both halves | 7e-06 | STRING 915 |
| [[NOC2L]] | +0.77 | +0.75 / +0.73 | both halves | 7e-06 | STRING 998 |
| [[WDR77]] | +0.77 | +0.79 / +0.80 | both halves | 7e-06 | same gene group |
| [[PGAM5]] | +0.77 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[LETM1]] | +0.76 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[CAD]] | +0.75 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[LYAR]] | +0.75 | +0.74 / +0.70 | both halves | 7e-06 | STRING 635 |
| [[IPO4]] | +0.74 | +0.77 / +0.75 | both halves | 7e-06 | STRING 690 |
| [[PFAS]] | +0.74 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[TCOF1]] | +0.74 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[TMEM201]] | +0.73 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[FARSB]] | +0.73 | +0.69 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF821]] | -0.66 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[SELENOK]] | -0.65 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[ZMYM5]] | -0.65 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[ARID4B]] | -0.64 | -0.61 / -0.58 | both halves | 7e-06 | same gene group |
| [[TERF2IP]] | -0.64 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[EAPP]] | -0.62 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[HOXA5]] | -0.62 | -0.56 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JPH1]] | B | JPH1 activity lowers BOP1's level | lines that do not express JPH1 (15) vs lines expressing it (35) | 1.39× higher at baseline in the lines without JPH1 | 0.015 | ⚠ within organs, on part of the lines; also absent: UGT8, CADPS2, PTPRE |
| [[SPTBN2]] | B | SPTBN2 activity raises BOP1's level | lines that do not express SPTBN2 (9) vs lines expressing it (41) | 1.43× lower at baseline in the lines without SPTBN2 | 0.053 | ⚠ within organs, on part of the lines; also absent: CCDC88C, HID1, ASS1; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises BOP1's level | compounds that target MAP2K1: 2 of 4 lower it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.6% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FBXO32]] | B | FBXO32 activity lowers BOP1's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 1.40× higher at baseline in the lines without FBXO32 | 0.095 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[SACS]] | B | SACS activity raises BOP1's level | lines that do not express SACS (5) vs lines expressing it (45) | 1.47× lower at baseline in the lines without SACS | 0.098 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.715). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-12.6, -37.5); signed map (-6.0, -46.2). **Vector** length 86.8, 19.8% of its response variance represented; |z| ≥ 3 in 1,098 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.8 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +7.3 | +17.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +7.2 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +6.1 | +12.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.9 | +6.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.0 | +5.2 |
|  | [[EX229 (drug)]] 5 µM |  | +3.9 | +6.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.3 | +5.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.2 | +5.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -2.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -2.4 | -3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -5.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.1 | -2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.0 | -3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | BOP1 ribosomal biogenesis factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,262,045-144,291,438 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0124 |
| Gene groups (HGNC) | WD repeat domain containing; MicroRNA protein coding host genes; PeBoW complex |
| Reactome | 4 pathways, smallest: Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14137](https://www.uniprot.org/uniprotkb/Q14137) (Ribosome biogenesis protein BOP1):

> Component of the PeBoW complex, which is required for maturation of 28S and 5.8S ribosomal RNAs and formation of the 60S ribosome.

**Summary**, from NCBI Gene [23246](https://www.ncbi.nlm.nih.gov/gene/23246):

> Enables RNA binding activity. Involved in regulation of cell cycle; regulation of signal transduction by p53 class mediator; and ribosomal large subunit biogenesis. Located in chromosome; nucleolus; and nucleoplasm. Part of PeBoW complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15519](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15519) · Entrez [23246](https://www.ncbi.nlm.nih.gov/gene/23246) · UniProt [Q14137](https://www.uniprot.org/uniprotkb/Q14137) · Ensembl [ENSG00000261236](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000261236)

## Data

Gene col 15334: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15334); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15334, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15334]; `tensor/DDL_lfc|DDL_z.npy` [15334]; `embed/gene_vectors.npy` [15334]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15334 or target_col == 15334). Every well: [[BOP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BOP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
