---
symbol: "EMC1"
type: "gene"
col: 4812
ensembl_id: "ENSG00000127463"
name: "ER membrane protein complex subunit 1"
location: "1p36.13"
module: 127
arm: "+"
pooled_cpm: 36.02
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# EMC1

*ER membrane protein complex subunit 1* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.51× (z +14.2, q 8e-43, up in 41 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.95× (z +8.7, q 5e-16, up in 44 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Brimonidine (drug)]] 0.5 µM in 1 line (NCI-H661 0.0666×); [[Homoharringtonine (drug)]] 5 µM in 1 line (H4 0.360×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGT]] (+0.77, fdr 7e-06), [[RPSA]] (+0.75, fdr 7e-06), [[FKBP9]] (+0.74, fdr 7e-06); moves opposite to [[SMIM26]] (-0.72, fdr 1e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[UBE2B]] (-0.71, fdr 7e-06), [[RPL36AL]] (-0.70, fdr 1e-05, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[EIF1B]] (-0.69, fdr 1e-05), [[NKAP]] (-0.68, fdr 1e-05).
> It is in [[Module 127]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4812.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.51×** | +14.2 | 8e-43 | 41/46 (HOP62, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +13.8 | 7e-41 | 35/39 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +11.0 | 5e-26 | 36/42 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.95×** | +8.7 | 5e-16 | 44/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.67×** | +7.9 | 4e-13 | 39/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.37×** | +6.9 | 4e-10 | 38/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +6.8 | 1e-09 | 31/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.47×** | +5.9 | 2e-07 | 35/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +5.3 | 8e-06 | 28/48 (NCI-H1573, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.38×** | +4.9 | 5e-05 | 28/48 (COLO 205, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.3 | 8e-04 | 27/48 (HOP62, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.32×** | +4.3 | 8e-04 | 27/47 (NCI-H1573, NCI-H2030, …) | two highest doses | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.3 | 8e-04 | 18/33 (SNU-423, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.68×** | +4.2 | 0.001 | 24/48 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.55×** | +3.5 | 0.017 | 18/48 (Hs 766T, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.019 | 17/48 (NCI-H1792, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.50×** | +3.3 | 0.034 | 18/48 (NCI-H1792, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.49×** | +3.2 | 0.039 | 15/46 (Hs 766T, NCI-H1792, …) | rises with dose | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4812.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Brimonidine (drug)]] 0.5 µM in 1 line (NCI-H661 0.0666×); [[Homoharringtonine (drug)]] 5 µM in 1 line (H4 0.360×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rapamycin (drug)]] 0.5 µM |  | 0.801× | -3.4 | 0.25 | 15/48 (COLO 205, MIA PaCa-2, …) | all doses, flat | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.808× | -3.3 | 0.25 | 19/48 (NCI-H23, A498, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.814× | -3.1 | 0.25 | 16/48 (HOP62, BT-474, …) | rises with dose | position effect removed |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | 0.823× | -3.0 | 0.25 | 16/48 (SW 1088, KATO III, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.824× | -3.0 | 0.25 | 14/48 (LS 180, H4, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.872× | -3.0 | 0.25 | 13/48 (LS 180, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4812. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 65.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 36.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A549 (line)]] | wt | 21.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.08× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 58.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LS 180 (line)]] | wt | 29.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +10.0) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 39.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.06× (z +8.9) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 60.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 24.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.98× (z +10.3) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 25.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[CFPAC-1 (line)]] | alt | 39.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[H4 (line)]] | wt | 62.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 23.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LoVo (line)]] | wt | 19.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.47× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 27.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.39× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 33.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2030 (line)]] | alt | 38.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.39× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 52.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.12× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 79.5 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0666× (z -12.1) |
| [[SK-MEL-2 (line)]] | alt | 38.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SNU-1 (line)]] | wt | 37.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SNU-423 (line)]] | alt | 29.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW480 (line)]] | alt | 29.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.40× (z +9.1) | — |
| [[A-427 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4812), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGT]] | +0.77 | +0.67 / +0.78 | both halves | 7e-06 |  |
| [[RPSA]] | +0.75 | +0.66 / +0.75 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |
| [[FKBP9]] | +0.74 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[PRPF8]] | +0.73 | +0.61 / +0.78 | both halves | 7e-06 | STRING 415 |
| [[PPT1]] | +0.73 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[UGGT1]] | +0.73 | +0.68 / +0.73 | both halves | 7e-06 | STRING 470 |
| [[ATP13A1]] | +0.72 | +0.55 / +0.78 | both halves | 1e-05 |  |
| [[CHID1]] | +0.72 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[LAMP1]] | +0.72 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[NCSTN]] | +0.71 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[BPNT2]] | +0.71 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[EFTUD2]] | +0.71 | +0.60 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM26]] ⚠ | -0.72 | -0.55 / -0.74 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[UBE2B]] | -0.71 | -0.63 / -0.76 | both halves | 7e-06 |  |
| [[RPL36AL]] ⚠ | -0.70 | -0.51 / -0.76 | both halves | 1e-05 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; ⚠ in the vector space only through flagged drug-doses |
| [[EIF1B]] | -0.69 | -0.54 / -0.82 | both halves | 1e-05 |  |
| [[NACA4P]] ⚠ | -0.68 | -0.54 / -0.71 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NKAP]] | -0.68 | -0.53 / -0.71 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | -0.67 | -0.58 / -0.71 | both halves | 7e-06 |  |
| [[MSX1]] | -0.67 | -0.50 / -0.74 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.66 | -0.55 / -0.71 | both halves | 1e-05 |  |
| [[SNHG32]] | -0.66 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[SNHG6]] | -0.65 | -0.65 / -0.66 | both halves | 7e-06 |  |
| [[GABARAPL2]] | -0.64 | -0.49 / -0.75 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.63 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[BTG1]] | -0.63 | -0.42 / -0.70 | both halves | 4e-05 |  |
| [[SNHG7]] | -0.63 | -0.51 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-24.9, -23.5); signed map (-22.1, -37.0). **Vector** length 114, 29.8% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.4 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.9 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +8.9 | +14.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.5 | +7.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +8.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +6.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.8 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +4.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.5 | +2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +3.2 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | +0.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +0.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | +1.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.8 | -3.0 |
|  | [[Adagrasib (drug)]] 5 µM |  | -2.7 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ER membrane protein complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:19,215,660-19,251,552 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0090 |
| Gene groups (HGNC) | ER membrane protein complex subunits |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N766](https://www.uniprot.org/uniprotkb/Q8N766) (ER membrane protein complex subunit 1):

> Part of the endoplasmic reticulum membrane protein complex (EMC) that enables the energy-independent insertion into endoplasmic reticulum membranes of newly synthesized membrane proteins. Preferentially accommodates proteins with transmembrane domains that are weakly hydrophobic or contain destabilizing features such as charged and aromatic residues. Involved in the cotranslational insertion of multi-pass membrane proteins in which stop-transfer membrane-anchor sequences become ER membrane …

**Summary**, from NCBI Gene [23065](https://www.ncbi.nlm.nih.gov/gene/23065):

> This gene encodes a single-pass type I transmembrane protein, which is a subunit of the endoplasmic reticulum membrane protein complex (EMC). Multiple alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2012]

**Accessions** — [HGNC:28957](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28957) · Entrez [23065](https://www.ncbi.nlm.nih.gov/gene/23065) · UniProt [Q8N766](https://www.uniprot.org/uniprotkb/Q8N766) · Ensembl [ENSG00000127463](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127463)

## Data

Gene col 4812: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4812); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4812, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4812]; `tensor/DDL_lfc|DDL_z.npy` [4812]; `embed/gene_vectors.npy` [4812]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4812 or target_col == 4812). Every well: [[EMC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EMC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
