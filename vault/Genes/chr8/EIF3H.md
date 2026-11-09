---
symbol: "EIF3H"
type: "gene"
col: 7214
ensembl_id: "ENSG00000147677"
name: "eukaryotic translation initiation factor 3 subunit H"
location: "8q23.3-q24.11"
module: 20
arm: "+"
pooled_cpm: 231.69
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# EIF3H

*eukaryotic translation initiation factor 3 subunit H* — 8q23.3-q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (15 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.07× (z +20.4, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.810× (z -4.4, q 0.006, down in 25 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[(S)-Crizotinib (drug)]] 0.5 µM in 1 line (SW 1088 0.125×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STRAP]] (+0.71, fdr 7e-06), [[EIF3L]] (+0.70, fdr 7e-06), [[EIF2S3]] (+0.66, fdr 7e-06); moves opposite to [[UNK]] (-0.61, fdr 1e-05), [[UPF3B]] (-0.59, fdr 1e-05), [[CROCCP2-1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 19 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7214.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.07×** | +20.4 | 0e+00 | 49/49 (RKO, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.04×** | +15.8 | 0e+00 | 47/48 (C32, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.96×** | +14.5 | 3e-45 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +10.8 | 3e-25 | 46/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.59×** | +10.1 | 9e-22 | 42/49 (LoVo, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.62×** | +9.6 | 1e-19 | 40/45 (NCI-H460, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.51×** | +8.8 | 9e-17 | 38/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +8.7 | 2e-16 | 44/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.48×** | +8.5 | 1e-15 | 42/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +8.5 | 1e-15 | 43/48 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +8.3 | 5e-15 | 36/47 (LoVo, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.01×** | +7.9 | 2e-13 | 33/38 (SK-MEL-2, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.94×** | +7.5 | 3e-12 | 44/45 (HT-29, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.40×** | +7.2 | 3e-11 | 43/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +6.6 | 1e-09 | 39/48 (HT-29, Hs 766T, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +6.4 | 4e-09 | 34/48 (SK-MEL-2, SNU-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.49×** | +4.5 | 2e-04 | 36/48 (HT-29, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.32×** | +4.3 | 4e-04 | 35/49 (PANC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.12× | +3.5 | 0.009 | 3/49 (HS-578T, NCI-H2030, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.020 | 21/48 (PANC-1, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.033 | 23/48 (PANC-1, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.036 | 21/48 (NCI-H1792, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7214.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[(S)-Crizotinib (drug)]] 0.5 µM in 1 line (SW 1088 0.125×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.810×** | -4.4 | 0.006 | 25/47 (NCI-H23, hTERT-HPNE, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.846× | -3.6 | 0.077 | 20/48 (RKO, J82, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.863× | -3.2 | 0.23 | 14/48 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | 0.864× | -3.1 | 0.23 | 10/48 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Sacubitril_Valsartan (drug)]] 5 µM |  | 0.863× | -3.1 | 0.23 | 5/48 (C32, A498, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7214. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 152 | 10 (8 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +19.5) | — |
| [[PANC-1 (line)]] | alt | 243 | 10 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +18.3) | — |
| [[BT-474 (line)]] | alt | 240 | 9 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +13.5) | — |
| [[Hs 766T (line)]] | wt | 162 | 8 (5 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.1× (z +15.4) | — |
| [[SK-MEL-2 (line)]] | alt | 192 | 8 (5 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.21× (z +15.0) | — |
| [[HT-29 (line)]] | alt | 625 | 7 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.70× (z +16.1) | — |
| [[KATO III (line)]] | alt | 189 | 7 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.34× (z +17.8) | — |
| [[LoVo (line)]] | wt | 206 | 7 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.99× (z +17.0) | — |
| [[HOP62 (line)]] | alt | 186 | 6 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.51× (z +14.3) | — |
| [[NCI-H1573 (line)]] | alt | 222 | 6 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.86× (z +15.0) | — |
| [[NCI-H1792 (line)]] | alt | 147 | 6 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +11.5) | — |
| [[COLO 205 (line)]] | alt | 185 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 17.0× (z +17.6) | — |
| [[LS 180 (line)]] | wt | 183 | 5 (2 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 7.78× (z +15.9) | — |
| [[SW48 (line)]] | wt | 203 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 0.05 µM 5.86× (z +20.2) | — |
| [[LOX-IMVI (line)]] | wt | 384 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 8.12× (z +14.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 114 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.93× (z +13.0) | — |
| [[RKO (line)]] | wt | 500 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 6.80× (z +18.2) | — |
| [[SW1417 (line)]] | alt | 363 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 4.93× (z +13.2) | — |
| [[SW480 (line)]] | alt | 193 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.34× (z +17.2) | — |
| [[A-172 (line)]] | wt | 86.9 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.13× (z +10.2) | — |
| [[C32 (line)]] | wt | 202 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 15.0× (z +16.3) | — |
| [[HepG2_C3A (line)]] | wt | 181 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.03× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 219 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.81× (z +12.0) | — |
| [[A-427 (line)]] | wt | 141 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.08× (z +13.5) | — |
| [[A549 (line)]] | wt | 203 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.69× (z +11.6) | — |
| [[AsPC-1 (line)]] | alt | 387 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +12.8) | — |
| [[C-33 A (line)]] | alt | 167 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.57× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 153 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 7.22× (z +14.5) | — |
| [[HS-578T (line)]] | alt | 282 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.33× (z +11.3) | — |
| [[hTERT-HPNE (line)]] | wt | 169 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.63× (z +10.9) | — |
| [[J82 (line)]] | alt | 228 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 173 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.79× (z +12.5) | — |
| [[NCI-H2347 (line)]] | alt | 318 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.49× (z +12.4) | — |
| [[Panc 03.27 (line)]] | alt | 255 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.03× (z +15.4) | — |
| [[RPMI-7951 (line)]] | alt | 211 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.36× (z +13.1) | — |
| [[A498 (line)]] | wt | 351 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.68× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 216 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.38× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 167 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.32× (z +11.6) | — |
| [[H4 (line)]] | wt | 181 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.65× (z +10.5) | — |
| [[HCT15 (line)]] | alt | 168 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.45× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 279 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.63× (z +11.3) | — |
| [[SNU-1 (line)]] | wt | 222 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.17× (z +11.5) | — |
| [[SNU-423 (line)]] | alt | 138 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[SW 1088 (line)]] | alt | 139 | 0 | 1 | — | [[(S)-Crizotinib (drug)]] 0.5 µM 0.125× (z -9.3) |
| [[CHP-212 (line)]] | wt | 211 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 329 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 130 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7214), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRAP]] | +0.71 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[EIF3L]] | +0.70 | +0.72 / +0.63 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[EIF2S3]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 | pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 969 |
| [[RPL4]] | +0.64 | +0.64 / +0.63 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 730 |
| [[OPA1]] | +0.63 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[SLC25A6]] | +0.62 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[MTPN]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[LRPPRC]] | +0.61 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[FTO]] | +0.61 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[DCAF13]] | +0.61 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[PHB2]] | +0.60 | +0.71 / +0.41 | both halves | 4e-05 |  |
| [[RPL29]] | +0.60 | +0.70 / +0.40 | both halves | 5e-05 | pathway: Cap-dependent Translation Initiation; STRING 422 |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNK]] | -0.61 | -0.69 / -0.50 | both halves | 1e-05 |  |
| [[UPF3B]] | -0.59 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | -0.58 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[ERF]] | -0.58 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[LRCH3]] | -0.58 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[CHKB]] | -0.57 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[RBX1]] | -0.57 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[FOXA2]] | -0.57 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[WBP4]] | -0.56 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[ZIC2]] | -0.56 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[TOPORS]] | -0.55 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[NFYB]] | -0.55 | -0.56 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.627). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-29.7, -27.0); signed map (-55.3, -8.7). **Vector** length 91.1, 32.5% of its response variance represented; |z| ≥ 3 in 1,337 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.55 to 10); *Cotranslational targeting of proteins to the endoplasmic reticulum* (reactome, mean cos +0.52 to 11); *Peptide chain elongation* (reactome, mean cos +0.57 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +5.4 | +9.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.0 | +20.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +4.6 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | +4.3 | +5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +15.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +8.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.0 | +0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -9.4 | +0.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -7.8 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -5.6 | +4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.2 | -0.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | +0.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -2.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.8 | -0.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 3 subunit H |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q23.3-q24.11 — chr8:116,642,130-116,766,925 (-) |
| Ensembl biotype | protein_coding |
| Also known as | eIF3-gamma, eIF3-p40; previously EIF3S3 |
| Gene groups (HGNC) | JAMM/MPN+ metallopeptidase family; Eukaryotic translation initiation factor 3 complex subunits |
| Reactome | 14 pathways, smallest: Formation of the ternary complex, and subsequently, the 43S complex; Ribosomal scanning and start codon recognition; Translation initiation complex formation |
| Matched by | ensembl_id |

**Function**, from UniProt [O15372](https://www.uniprot.org/uniprotkb/O15372) (Eukaryotic translation initiation factor 3 subunit H):

> Component of the eukaryotic translation initiation factor 3 (eIF-3) complex, which is required for several steps in the initiation of protein synthesis. The eIF-3 complex associates with the 40S ribosome and facilitates the recruitment of eIF-1, eIF-1A, eIF-2:GTP:methionyl-tRNAi and eIF-5 to form the 43S pre-initiation complex (43S PIC). The eIF-3 complex stimulates mRNA recruitment to the 43S PIC and scanning of the mRNA for AUG recognition. The eIF-3 complex is also required for disassembly …

**Summary**, from NCBI Gene [8667](https://www.ncbi.nlm.nih.gov/gene/8667):

> Enables metal-dependent deubiquitinase activity. Contributes to translation initiation factor activity. Involved in negative regulation of proteasomal ubiquitin-dependent protein catabolic process and translational initiation. Located in extracellular exosome and membrane. Part of eukaryotic translation initiation factor 3 complex. Implicated in breast cancer; prostate cancer; and prostate carcinoma. Biomarker of prostate cancer. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:3273](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3273) · Entrez [8667](https://www.ncbi.nlm.nih.gov/gene/8667) · UniProt [O15372](https://www.uniprot.org/uniprotkb/O15372) · Ensembl [ENSG00000147677](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147677)

## Data

Gene col 7214: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7214); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7214, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7214]; `tensor/DDL_lfc|DDL_z.npy` [7214]; `embed/gene_vectors.npy` [7214]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7214 or target_col == 7214). Every well: [[EIF3H — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF3H.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
