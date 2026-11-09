---
symbol: "CCT8"
type: "gene"
col: 7964
ensembl_id: "ENSG00000156261"
name: "chaperonin containing TCP1 subunit 8"
location: "21q21.3"
module: 4
arm: "+"
pooled_cpm: 130.12
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# CCT8

*chaperonin containing TCP1 subunit 8* — 21q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.41× (z +13.2, q 3e-37, up in 40 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.68× (z +8.1, q 1e-13, up in 43 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (AN3 CA 0.373×, A-427 0.562×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHB1]] (+0.69, fdr 7e-06), [[CCT7]] (+0.64, fdr 7e-06), [[KARS1]] (+0.63, fdr 1e-05); moves opposite to [[CHKB]] (-0.59, fdr 1e-05), [[RFX1]] (-0.58, fdr 1e-05), [[NFKBIB]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 20 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7964.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.41×** | +13.2 | 3e-37 | 40/44 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.32×** | +13.2 | 4e-37 | 44/49 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +8.1 | 1e-13 | 43/48 (HEC-1-A, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.74×** | +7.3 | 4e-11 | 39/45 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +6.8 | 9e-10 | 40/48 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.49×** | +6.3 | 4e-08 | 41/48 (A498, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.46×** | +5.9 | 3e-07 | 38/48 (A-172, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +5.9 | 3e-07 | 39/48 (NCI-H1792, HOP62, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.30×** | +5.8 | 3e-07 | 29/49 (NCI-H2347, Hs 766T, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.56×** | +5.7 | 8e-07 | 39/48 (CFPAC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.43×** | +5.6 | 1e-06 | 36/48 (A-172, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **1.43×** | +5.4 | 3e-06 | 38/47 (LoVo, COLO 205, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +5.1 | 2e-05 | 37/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.38×** | +5.1 | 2e-05 | 39/48 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.40×** | +5.0 | 2e-05 | 32/48 (A-172, SW 900, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.64×** | +4.0 | 0.002 | 34/48 (AsPC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.63×** | +4.0 | 0.002 | 30/48 (LS 180, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.9 | 0.003 | 30/48 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.0 | 0.054 | 15/49 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +2.9 | 0.068 | 15/48 (A-172, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7964.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (AN3 CA 0.373×, A-427 0.562×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 0.787× | -3.5 | 0.28 | 26/50 (NCI-H23, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.805× | -3.3 | 0.28 | 23/47 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.812× | -3.2 | 0.29 | 25/48 (KATO III, hTERT-HPNE, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7964. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 140 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 195 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H1792 (line)]] | alt | 90.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.65× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 116 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H2347 (line)]] | alt | 115 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +11.0) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A498 (line)]] | wt | 154 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.01× (z +15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[A549 (line)]] | wt | 102 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[HCT15 (line)]] | alt | 159 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[HOP62 (line)]] | alt | 127 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[HS-578T (line)]] | alt | 117 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.16× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HT-29 (line)]] | alt | 87.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[J82 (line)]] | alt | 95.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.91× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[KATO III (line)]] | alt | 79.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.14× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LoVo (line)]] | wt | 135 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.24× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H2030 (line)]] | alt | 154 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.46× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H23 (line)]] | alt | 185 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H460 (line)]] | wt | 105 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[PANC-1 (line)]] | alt | 113 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.77× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[RPMI-7951 (line)]] | alt | 106 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[SNU-423 (line)]] | alt | 108 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.24× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SW 900 (line)]] | alt | 92.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SW480 (line)]] | alt | 184 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[A-427 (line)]] | wt | 187 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 147 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 95.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.27× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[C32 (line)]] | wt | 93.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[COLO 205 (line)]] | alt | 69.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[HEC-1-A (line)]] | alt | 142 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.22× (z +10.5) | — |
| [[hTERT-HPNE (line)]] | wt | 104 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[LOX-IMVI (line)]] | wt | 219 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.35× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LS 180 (line)]] | wt | 140 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H1573 (line)]] | alt | 67.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.77× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[Panc 03.27 (line)]] | alt | 116 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 124 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[SNU-1 (line)]] | wt | 136 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.72× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SW1417 (line)]] | alt | 123 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.02× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[SW48 (line)]] | wt | 163 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[BT-474 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 153 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 152 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 158 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 97.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 211 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7964), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHB1]] | +0.69 | +0.72 / +0.58 | both halves | 7e-06 | STRING 421 |
| [[CCT7]] | +0.64 | +0.67 / +0.64 | both halves | 7e-06 | same gene group; pathway: Association of TriC/CCT with target proteins during biosynthesis; STRING 999 |
| [[KARS1]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 | STRING 596 |
| [[CCT3]] | +0.63 | +0.66 / +0.54 | both halves | 1e-05 | same gene group; pathway: Assembly of the 9+0 primary cilium; STRING 999 |
| [[NKRF]] | +0.61 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[CCT6A]] | +0.61 | +0.69 / +0.45 | both halves | 3e-05 | same gene group; pathway: Association of TriC/CCT with target proteins during biosynthesis; STRING 999 |
| [[RPL6]] | +0.60 | +0.63 / +0.49 | both halves | 1e-05 | STRING 780 |
| [[ADH5]] | +0.60 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[CCT4]] | +0.60 | +0.64 / +0.56 | both halves | 1e-05 | same gene group; pathway: Assembly of the 9+0 primary cilium; STRING 999 |
| [[GLO1]] | +0.59 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[C1QBP]] | +0.59 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[PAICS]] | +0.59 | +0.61 / +0.53 | both halves | 1e-05 | STRING 497 |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHKB]] | -0.59 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[RFX1]] | -0.58 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[NFKBIB]] | -0.56 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[TP53INP2]] | -0.55 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[ATP6V0C]] | -0.54 | -0.55 / -0.38 | both halves | 7e-05 |  |
| [[TNRC6C]] | -0.53 | -0.55 / -0.40 | both halves | 4e-05 | pathway: Cilium Assembly |
| [[ZFTRAF1]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[MNT]] | -0.52 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[TERF2IP]] | -0.52 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.51 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[GABARAP]] ⚠ | -0.51 | -0.52 / -0.46 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[WBP4]] | -0.50 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[EGLN2]] | -0.50 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.503). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-21.3, -32.1); signed map (-12.1, -43.7). **Vector** length 82.6, 27.4% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +5.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | +3.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.6 | +5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +6.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.3 | +4.0 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.8 | +1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.7 | +0.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | +2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | +1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.9 | +0.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.8 | -1.2 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | -1.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | chaperonin containing TCP1 subunit 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q21.3 — chr21:29,055,805-29,073,797 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Cctq, PRED71; previously C21orf112 |
| Gene groups (HGNC) | Chaperonin containing TCP1 |
| Reactome | 15 pathways, smallest: Folding of actin by CCT/TriC; Formation of tubulin folding intermediates by CCT/TriC; BBSome-mediated cargo-targeting to cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [P50990](https://www.uniprot.org/uniprotkb/P50990) (T-complex protein 1 subunit theta):

> Component of the chaperonin-containing T-complex (TRiC), a molecular chaperone complex that assists the folding of actin, tubulin and other proteins upon ATP hydrolysis. The TRiC complex mediates the folding of WRAP53/TCAB1, thereby regulating telomere maintenance. As part of the TRiC complex may play a role in the assembly of BBSome, a complex involved in ciliogenesis regulating transports vesicles to the cilia.

**Summary**, from NCBI Gene [10694](https://www.ncbi.nlm.nih.gov/gene/10694):

> This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:1623](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1623) · Entrez [10694](https://www.ncbi.nlm.nih.gov/gene/10694) · UniProt [P50990](https://www.uniprot.org/uniprotkb/P50990) · Ensembl [ENSG00000156261](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156261)

## Data

Gene col 7964: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7964); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7964, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7964]; `tensor/DDL_lfc|DDL_z.npy` [7964]; `embed/gene_vectors.npy` [7964]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7964 or target_col == 7964). Every well: [[CCT8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCT8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
