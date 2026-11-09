---
symbol: "KIDINS220"
type: "gene"
col: 5543
ensembl_id: "ENSG00000134313"
name: "kinase D interacting substrate 220"
location: "2p25.1"
module: 5
arm: "-"
pooled_cpm: 137.31
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# KIDINS220

*kinase D interacting substrate 220* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.16× (z +27.6, q 0e+00, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (CFPAC-1 0.433×, SW1417 0.490×, A-172 0.538×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (CFPAC-1 0.530×, AsPC-1 0.461×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (CFPAC-1 0.504×, H4 0.331×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.106×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AHNAK2]] (+0.65, fdr 1e-05), [[WASHC4]] (+0.60, fdr 7e-06), [[OPTN]] (+0.59, fdr 1e-05); moves opposite to [[BEND3]] (-0.59, fdr 1e-05), [[SCLY]] (-0.56, fdr 6e-05), [[ZNF668]] (-0.55, fdr 1e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5543.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.16×** | +27.6 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.73×** | +24.1 | 0e+00 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.97×** | +22.9 | 0e+00 | 47/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.30×** | +20.0 | 0e+00 | 48/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +11.3 | 2e-27 | 37/48 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +11.3 | 2e-27 | 45/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.56×** | +10.3 | 6e-23 | 41/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +7.4 | 8e-12 | 30/48 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +7.4 | 8e-12 | 32/48 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.93×** | +5.7 | 7e-07 | 35/49 (HT-29, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.16× | +5.1 | 2e-05 | 17/48 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.23×** | +4.8 | 6e-05 | 24/48 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.73×** | +4.8 | 8e-05 | 33/49 (BT-474, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.21×** | +4.5 | 3e-04 | 22/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.20×** | +4.4 | 5e-04 | 24/48 (A-427, A498, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.021 | 18/49 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.13× | +3.4 | 0.021 | 10/48 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5543.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (CFPAC-1 0.433×, SW1417 0.490×, A-172 0.538×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (CFPAC-1 0.530×, AsPC-1 0.461×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (CFPAC-1 0.504×, H4 0.331×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.106×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.846× | -3.9 | 0.054 | 21/47 (SNU-1, Hs 766T, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.903× | -3.6 | 0.11 | 2/49 (H4, NCI-H1792) | rises with dose |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.863× | -3.1 | 0.35 | 13/48 (NCI-H460, SNU-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5543. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 129 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +29.6) | — |
| [[NCI-H1573 (line)]] | alt | 108 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +26.6) | — |
| [[A-427 (line)]] | wt | 144 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.95× (z +16.2) | — |
| [[PANC-1 (line)]] | alt | 118 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 3.49× (z +20.3) | — |
| [[A498 (line)]] | wt | 128 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 3.79× (z +19.4) | — |
| [[BT-474 (line)]] | alt | 147 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 3.48× (z +14.9) | — |
| [[COLO 205 (line)]] | alt | 152 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +15.6) | — |
| [[LS 180 (line)]] | wt | 125 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +16.9) | — |
| [[NCI-H23 (line)]] | alt | 103 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +22.5) | — |
| [[SW480 (line)]] | alt | 160 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 3.62× (z +20.9) | — |
| [[A-172 (line)]] | wt | 183 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.538× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 182 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.93× (z +16.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.646× (z -9.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[C-33 A (line)]] | alt | 78.1 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.29× (z +13.4) | — |
| [[KATO III (line)]] | alt | 216 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.63× (z +16.7) | — |
| [[LoVo (line)]] | wt | 103 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.94× (z +20.3) | — |
| [[NCI-H2030 (line)]] | alt | 105 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +19.4) | — |
| [[NCI-H2347 (line)]] | alt | 122 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +15.9) | — |
| [[RKO (line)]] | wt | 111 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +16.7) | — |
| [[SHP-77 (line)]] | alt | 162 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.53× (z +17.9) | — |
| [[SW1417 (line)]] | alt | 150 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.57× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.490× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 139 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.12× (z +16.8) | — |
| [[HepG2_C3A (line)]] | wt | 153 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.77× (z +16.8) | — |
| [[HS-578T (line)]] | alt | 121 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.14× (z +14.9) | — |
| [[HT-29 (line)]] | alt | 128 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +21.1) | — |
| [[hTERT-HPNE (line)]] | wt | 128 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.65× (z +14.3) | — |
| [[J82 (line)]] | alt | 70.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +17.0) | — |
| [[NCI-H1792 (line)]] | alt | 124 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.65× (z +13.8) | — |
| [[RPMI-7951 (line)]] | alt | 139 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.53× (z +15.1) | — |
| [[SK-MEL-2 (line)]] | alt | 94.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.52× (z +14.8) | — |
| [[SW 900 (line)]] | alt | 124 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.35× (z +14.7) | — |
| [[C32 (line)]] | wt | 63.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.91× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 208 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.433× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 137 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.52× (z +13.5) | — |
| [[Hs 766T (line)]] | wt | 142 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +14.2) | — |
| [[LOX-IMVI (line)]] | wt | 182 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 134 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.03× (z +14.2) | — |
| [[SNU-423 (line)]] | alt | 167 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +13.5) | — |
| [[SW48 (line)]] | wt | 112 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.68× (z +13.9) | — |
| [[AsPC-1 (line)]] | alt | 200 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.14× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.461× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 98.7 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.90× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 180 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 143 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.65× (z +13.8) | — |
| [[SNU-1 (line)]] | wt | 132 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.9) | — |
| [[CHP-212 (line)]] | wt | 217 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.91× (z +8.9) | — |
| [[NCI-H596 (line)]] | alt | 142 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.106× (z -10.1) |
| [[AN3 CA (line)]] | alt | 217 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 151 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5543), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHNAK2]] | +0.65 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[WASHC4]] | +0.60 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[OPTN]] | +0.59 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[OAZ2]] | +0.55 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[SNX12]] | +0.53 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[ATP6V1C1]] | +0.53 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[SPTAN1]] | +0.53 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[VPS41]] | +0.53 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[VPS26A]] | +0.52 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[VAT1]] | +0.52 | +0.36 / +0.53 | both halves | 9e-05 |  |
| [[STAG2]] | +0.52 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[LAMP2]] | +0.52 | +0.37 / +0.55 | both halves | 8e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BEND3]] | -0.59 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[SCLY]] | -0.56 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[ZNF668]] | -0.55 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[DHRS7B]] | -0.54 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[MYO19]] | -0.54 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[EEF1AKMT4]] | -0.53 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[LRR1]] | -0.52 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[NOP2]] | -0.52 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[MCM9]] | -0.51 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[IL9RP3]] | -0.51 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[RFWD3]] | -0.51 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[TMEM11-DT]] | -0.51 | -0.36 / -0.55 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.484). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (0.2, -33.9); signed map (6.2, -11.0). **Vector** length 112, 36.3% of its response variance represented; |z| ≥ 3 in 1,076 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.0 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.9 | +2.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +3.8 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.5 | +3.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.5 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.0 | +2.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -7.5 | -0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.8 | -3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -6.7 | -3.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.5 | -1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | +0.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -0.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.4 | -0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | kinase D interacting substrate 220 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:8,721,081-8,837,630 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARMS |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Reactome | 11 pathways, smallest: ARMS-mediated activation; Prolonged ERK activation events; Signalling to ERKs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULH0](https://www.uniprot.org/uniprotkb/Q9ULH0) (Kinase D-interacting substrate of 220 kDa):

> Promotes a prolonged MAP-kinase signaling by neurotrophins through activation of a Rap1-dependent mechanism. Provides a docking site for the CRKL-C3G complex, resulting in Rap1-dependent sustained ERK activation. May play an important role in regulating postsynaptic signal transduction through the syntrophin-mediated localization of receptor tyrosine kinases such as EPHA4. In cooperation with SNTA1 can enhance EPHA4-induced JAK/STAT activation. Plays a role in nerve growth factor (NGF)-induced …

**Summary**, from NCBI Gene [57498](https://www.ncbi.nlm.nih.gov/gene/57498):

> This gene encodes a transmembrane protein that is preferentially expressed in the nervous system where it controls neuronal cell survival, differentiation into exons and dendrites, and synaptic plasticity. The encoded protein interacts with membrane receptors, cytosolic signaling components, and cytoskeletal proteins, serving as a scaffold that mediates crosstalk between the neurotrophin pathway and several other intracellular signaling pathways. Aberrant expression of this gene is associated …

**Accessions** — [HGNC:29508](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29508) · Entrez [57498](https://www.ncbi.nlm.nih.gov/gene/57498) · UniProt [Q9ULH0](https://www.uniprot.org/uniprotkb/Q9ULH0) · Ensembl [ENSG00000134313](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134313)

## Data

Gene col 5543: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5543); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5543, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5543]; `tensor/DDL_lfc|DDL_z.npy` [5543]; `embed/gene_vectors.npy` [5543]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5543 or target_col == 5543). Every well: [[KIDINS220 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIDINS220.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
