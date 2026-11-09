---
symbol: "DENND1B"
type: "gene"
col: 13077
ensembl_id: "ENSG00000213047"
name: "DENN domain containing 1B"
location: "1q31.3"
module: 40
arm: "-"
pooled_cpm: 85.69
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 27
n_dd_up_clean: 5
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# DENND1B

*DENN domain containing 1B* — 1q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.38× (z +5.6, q 1e-05, up in 30 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.234× (z -26.1, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TLK1]] (+0.59, fdr 1e-05), [[PLEKHA5]] (+0.59, fdr 1e-05), [[PTPN4]] (+0.57, fdr 3e-05); moves opposite to [[ELK1]] (-0.60, fdr 3e-05), [[SLC35E1]] (-0.53, fdr 4e-05), [[PIH1D1]] (-0.50, fdr 1e-04).
> It sits in the **-** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13077.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +5.6 | 1e-05 | 30/46 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.20× | +4.4 | 0.004 | 18/47 (SW480, Hs 766T, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.007 | 26/46 (SW480, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.024 | 23/47 (C32, HepG2/C3A, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.24×** | +3.7 | 0.024 | 23/49 (SW480, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +3.5 | 0.041 | 14/47 (A-427, CFPAC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.054 | 17/46 (SW480, A-172, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.080 | 19/47 (SW480, MIA PaCa-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13077.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.234×** | -26.1 | 0e+00 | 47/47 (HT-29, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.270×** | -23.6 | 0e+00 | 47/47 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.315×** | -20.8 | 0e+00 | 45/47 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.486×** | -18.3 | 0e+00 | 42/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.500×** | -12.5 | 1e-33 | 35/48 (SHP-77, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.618×** | -12.3 | 2e-32 | 33/47 (NCI-H1573, LoVo, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.499×** | -12.0 | 2e-31 | 30/41 (NCI-H460, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.558×** | -10.5 | 6e-24 | 41/47 (Panc 03.27, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.551×** | -10.3 | 5e-23 | 36/46 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.618×** | -8.3 | 5e-15 | 36/46 (NCI-H460, SNU-423, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.402×** | -8.3 | 5e-15 | 38/48 (MIA PaCa-2, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.645×** | -7.6 | 2e-12 | 34/49 (NCI-H460, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.657×** | -7.5 | 2e-12 | 32/47 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.644×** | -7.3 | 1e-11 | 25/43 (KATO III, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.678×** | -7.0 | 1e-10 | 33/47 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.699×** | -6.4 | 4e-09 | 31/48 (NCI-H2347, A-172, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.503×** | -6.3 | 1e-08 | 32/47 (A498, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.827×** | -4.8 | 4e-05 | 23/47 (BT-474, A-172, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **0.742×** | -3.8 | 0.003 | 25/48 (MIA PaCa-2, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.822×** | -3.4 | 0.016 | 14/48 (HEC-1-A, SW 900, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.699×** | -3.3 | 0.024 | 19/47 (HS-578T, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.883× | -3.2 | 0.033 | 14/47 (HT-29, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13077. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 175 | 0 | 17 (12 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -24.2) |
| [[HT-29 (line)]] | alt | 194 | 0 | 14 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.101× (z -24.4) |
| [[NCI-H1573 (line)]] | alt | 119 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -29.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.262× (z -15.2) |
| [[LoVo (line)]] | wt | 117 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -22.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.170× (z -21.9) |
| [[MIA PaCa-2 (line)]] | alt | 79.0 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.111× (z -21.6) |
| [[NCI-H2347 (line)]] | alt | 160 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.168× (z -20.5) |
| [[CFPAC-1 (line)]] | alt | 67.8 | 4 (2 ⚠) | 5 (1 ⚠) | [[Daptomycin (drug)]] 5 µM 2.55× (z +9.5) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.85× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.291× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 93.3 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.116× (z -23.7) |
| [[BT-474 (line)]] | alt | 277 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.182× (z -19.0) |
| [[KATO III (line)]] | alt | 99.9 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -22.7) |
| [[A498 (line)]] | wt | 52.7 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -19.6) |
| [[LOX-IMVI (line)]] | wt | 77.6 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.249× (z -13.6) |
| [[SNU-423 (line)]] | alt | 82.4 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -17.8) |
| [[SW1417 (line)]] | alt | 99.7 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.177× (z -19.6) |
| [[A-427 (line)]] | wt | 143 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -18.3) |
| [[A549 (line)]] | wt | 87.2 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -17.4) |
| [[AsPC-1 (line)]] | alt | 31.8 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -12.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.216× (z -11.7) |
| [[C32 (line)]] | wt | 61.7 | 0 | 6 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -11.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -11.0) |
| [[COLO 205 (line)]] | alt | 84.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -18.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.275× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 125 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.248× (z -17.5) |
| [[J82 (line)]] | alt | 53.6 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.224× (z -14.7) |
| [[LS 180 (line)]] | wt | 182 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0974× (z -25.9) |
| [[PANC-1 (line)]] | alt | 43.6 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -10.2) |
| [[A-172 (line)]] | wt | 73.7 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +18.7) ⚠ cell-cycle shift, explains ~36% of this change | [[Belinostat (drug)]] 5 µM 0.260× (z -12.2) |
| [[Hs 766T (line)]] | wt | 40.1 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.202× (z -11.3) |
| [[HS-578T (line)]] | alt | 45.6 | 0 | 5 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -12.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.208× (z -12.1) |
| [[NCI-H1792 (line)]] | alt | 62.5 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.171× (z -17.6) |
| [[NCI-H2030 (line)]] | alt | 78.4 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -15.9) |
| [[SW48 (line)]] | wt | 146 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -18.0) |
| [[NCI-H596 (line)]] | alt | 92.5 | 2 (1 ⚠) | 2 | [[Methylthiouracil (drug)]] 0.05 µM 5.17× (z +14.3) | [[Atazanavir (sulfate) (drug)]] 5 µM 0.110× (z -19.4) |
| [[SHP-77 (line)]] | alt | 83.0 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.253× (z -13.6) |
| [[SNU-1 (line)]] | wt | 72.8 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.271× (z -10.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -10.4) |
| [[SW 900 (line)]] | alt | 53.6 | 0 | 4 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.252× (z -11.8) ⚠ transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -10.3) |
| [[SW480 (line)]] | alt | 45.2 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.243× (z -14.4) |
| [[H4 (line)]] | wt | 68.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.232× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 37.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.235× (z -12.1) |
| [[HCT15 (line)]] | alt | 83.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[HOP62 (line)]] | alt | 31.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.332× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 44.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.233× (z -11.4) |
| [[AN3 CA (line)]] | alt | 123 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 69.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.52 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13077), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLK1]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[PLEKHA5]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[PTPN4]] | +0.57 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[PPP4R1]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[LRRFIP2]] | +0.54 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[SMG7]] | +0.54 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[PARD3B]] | +0.54 | +0.32 / +0.57 | both halves | 2e-04 |  |
| [[CAP2]] | +0.53 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[VRK2]] | +0.53 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[ST7]] | +0.52 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[PHACTR2]] | +0.52 | +0.34 / +0.50 | both halves | 1e-04 |  |
| [[STK33]] | +0.51 | +0.35 / +0.43 | both halves | 1e-04 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELK1]] | -0.60 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[SLC35E1]] | -0.53 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[PIH1D1]] | -0.50 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[TRIOBP]] | -0.49 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[POM121]] | -0.49 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[ODF2]] | -0.48 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[SLCO4A1]] | -0.47 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[ARHGAP1]] | -0.47 | -0.44 / -0.37 | both halves | 7e-05 |  |
| [[LINC03009-1]] | -0.47 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[TGFB1]] | -0.47 | -0.29 / -0.48 | both halves | 3e-04 |  |
| [[EPOR]] | -0.47 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[PRSS53]] | -0.47 | -0.40 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DENND1B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers DENND1B's level | compounds that target MAP2K1: 2 of 4 raise it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.8% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **-** arm (projection on the module's main direction -0.307). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-14.8, 13.4); signed map (10.7, -5.3). **Vector** length 90.0, 25.9% of its response variance represented; |z| ≥ 3 in 1,295 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +5.6 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.2 | +5.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.0 | -0.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.9 | +2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.7 | +3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.5 | +1.3 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.6 | -8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -10.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -3.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.6 | -26.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.4 | -20.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -6.3 |
|  | [[Daidzin (drug)]] 5 µM |  | -2.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | DENN domain containing 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q31.3 — chr1:197,504,748-197,775,696 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC27044, FLJ20054; previously FAM31B, C1orf218 |
| Gene groups (HGNC) | DENN domain containing |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P3S1](https://www.uniprot.org/uniprotkb/Q6P3S1) (DENN domain-containing protein 1B):

> Guanine nucleotide exchange factor (GEF) for RAB35 that acts as a regulator of T-cell receptor (TCR) internalization in TH2 cells. Acts by promoting the exchange of GDP to GTP, converting inactive GDP-bound RAB35 into its active GTP-bound form. Plays a role in clathrin-mediated endocytosis. Controls cytokine production in TH2 lymphocytes by controlling the rate of TCR internalization and routing to endosomes: acts by mediating clathrin-mediated endocytosis of TCR via its interaction with the …

**Summary**, from NCBI Gene [163486](https://www.ncbi.nlm.nih.gov/gene/163486):

> Clathrin (see MIM 118955)-mediated endocytosis is a major mechanism for internalization of proteins and lipids. Members of the connecdenn family, such as DENND1B, function as guanine nucleotide exchange factors (GEFs) for the early endosomal small GTPase RAB35 (MIM 604199) and bind to clathrin and clathrin adaptor protein-2 (AP2; see MIM 601024). Thus, connecdenns link RAB35 activation with the clathrin machinery (Marat and McPherson, 2010 [PubMed 20154091]).[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:28404](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28404) · Entrez [163486](https://www.ncbi.nlm.nih.gov/gene/163486) · UniProt [Q6P3S1](https://www.uniprot.org/uniprotkb/Q6P3S1) · Ensembl [ENSG00000213047](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213047)

## Data

Gene col 13077: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13077); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13077, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13077]; `tensor/DDL_lfc|DDL_z.npy` [13077]; `embed/gene_vectors.npy` [13077]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13077 or target_col == 13077). Every well: [[DENND1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DENND1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
