---
symbol: "TICAM1"
type: "gene"
col: 4829
ensembl_id: "ENSG00000127666"
name: "TIR domain containing adaptor molecule 1"
location: "19p13.3"
module: 31
arm: "+"
pooled_cpm: 30.05
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 28
n_dd_up_clean: 2
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 25
direction_downstream: 1
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# TICAM1

*TIR domain containing adaptor molecule 1* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 1.57× (z +6.3, q 1e-07, up in 22 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.20× (z +6.2, q 1e-07, up in 29 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HOP62 2.87×, HS-578T 2.45×; ⚠ cell-cycle shift, explains ~26% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 3.12×; ⚠ cell-cycle shift, explains ~4% of this change); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (NCI-H460 3.12×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (HOP62 4.56×).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.368× (z -21.2, q 0e+00, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITPKC]] (+0.63, fdr 1e-05), [[SBNO2]] (+0.61, fdr 1e-05), [[FBXO46]] (+0.56, fdr 1e-05); moves opposite to [[TDP1]] (-0.53, fdr 4e-05), [[PGM1]] (-0.51, fdr 1e-04), [[NUP133]] (-0.51, fdr 5e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[SH2D3A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[RFFL]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4829.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HOP62 2.87×, HS-578T 2.45×; ⚠ cell-cycle shift, explains ~26% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 3.12×; ⚠ cell-cycle shift, explains ~4% of this change); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (NCI-H460 3.12×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (HOP62 4.56×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +6.3 | 1e-07 | 22/37 (HS-578T, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.20×** | +6.2 | 1e-07 | 29/49 (NCI-H2030, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.21×** | +4.2 | 0.006 | 19/47 (HOP62, HS-578T, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.011 | 19/47 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | 1.49× | +3.2 | 0.15 | 12/45 (HEC-1-A, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | 1.49× | +3.2 | 0.15 | 16/45 (HEC-1-A, SW1417, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4829.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.368×** | -21.2 | 0e+00 | 41/46 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.353×** | -15.6 | 0e+00 | 43/48 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.416×** | -13.2 | 3e-37 | 39/48 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.445×** | -11.7 | 2e-29 | 37/48 (A-172, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.472×** | -11.3 | 2e-27 | 35/47 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.467×** | -11.0 | 4e-26 | 40/47 (Panc 03.27, A-172, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.828×** | -10.1 | 5e-22 | 26/49 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.513×** | -9.6 | 5e-20 | 26/33 (NCI-H2347, BT-474, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.689×** | -7.9 | 2e-13 | 32/48 (CFPAC-1, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.649×** | -6.5 | 5e-09 | 24/42 (NCI-H2347, CFPAC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.681×** | -5.7 | 5e-07 | 25/48 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.710×** | -5.1 | 1e-05 | 29/48 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.711×** | -5.1 | 2e-05 | 24/47 (HT-29, Panc 03.27, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM |  | **0.790×** | -4.9 | 3e-05 | 23/48 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.726×** | -4.8 | 7e-05 | 22/47 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[NG25 (drug)]] 5 µM |  | **0.549×** | -4.7 | 9e-05 | 25/44 (Panc 03.27, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.597×** | -4.0 | 0.002 | 19/49 (LoVo, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.792×** | -3.5 | 0.016 | 16/49 (HOP62, A549, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.802×** | -3.3 | 0.030 | 8/48 (HEC-1-A, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4829. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 83.1 | 0 | 10 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -20.7) |
| [[CFPAC-1 (line)]] | alt | 51.7 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -21.0) |
| [[HEC-1-A (line)]] | alt | 56.0 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -18.8) |
| [[HT-29 (line)]] | alt | 38.4 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -17.6) |
| [[LoVo (line)]] | wt | 54.0 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -19.8) |
| [[NCI-H460 (line)]] | wt | 26.3 | 4 (4 ⚠) | 2 | [[Harringtonine (drug)]] 0.5 µM 3.12× (z +9.7) ⚠ cell-cycle shift, explains ~4% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -17.3) |
| [[SW1417 (line)]] | alt | 45.9 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -16.8) |
| [[AsPC-1 (line)]] | alt | 67.7 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -16.2) |
| [[NCI-H1573 (line)]] | alt | 55.8 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -13.6) |
| [[LS 180 (line)]] | wt | 23.6 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 25.2 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0934× (z -22.7) |
| [[NCI-H2347 (line)]] | alt | 54.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0692× (z -21.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -16.9) |
| [[SW480 (line)]] | alt | 14.4 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.196× (z -10.8) |
| [[A-172 (line)]] | wt | 44.8 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -16.0) |
| [[KATO III (line)]] | alt | 16.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.138× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 49.4 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.255× (z -11.5) |
| [[SW48 (line)]] | wt | 41.3 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -13.0) |
| [[A-427 (line)]] | wt | 27.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.266× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.280× (z -8.7) |
| [[A498 (line)]] | wt | 37.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[BT-474 (line)]] | alt | 24.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0879× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -9.8) |
| [[COLO 205 (line)]] | alt | 43.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -10.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HOP62 (line)]] | alt | 10.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +9.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.56× (z +8.9) | — |
| [[A549 (line)]] | wt | 17.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -12.3) |
| [[C-33 A (line)]] | alt | 11.2 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0587× (z -10.3) |
| [[Hs 766T (line)]] | wt | 31.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0891× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HS-578T (line)]] | alt | 24.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +8.6) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[RPMI-7951 (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SK-MEL-2 (line)]] | alt | 22.4 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -8.5) |
| [[SNU-423 (line)]] | alt | 18.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -10.3) |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.150× (z -9.0) |
| [[AN3 CA (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4829), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITPKC]] | +0.63 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[SBNO2]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[FBXO46]] | +0.56 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[OLFM2]] | +0.56 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[STX11]] | +0.56 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[RDH13]] | +0.56 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[ARHGAP27]] | +0.55 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CTTNBP2NL]] | +0.55 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[CRYBG2]] | +0.53 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[RBMXL1]] | +0.52 | +0.36 / +0.56 | both halves | 9e-05 |  |
| [[TRAF4]] | +0.52 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[ABTB2]] | +0.52 | +0.45 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TDP1]] | -0.53 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[PGM1]] | -0.51 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[NUP133]] | -0.51 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[WHAMMP1]] | -0.49 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[SNX13]] | -0.49 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[LEPR]] | -0.47 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[TMED10]] | -0.46 | -0.35 / -0.36 | both halves | 1e-04 | STRING 492 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 25, C 0. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SH2D3A]] | B | SH2D3A activity raises TICAM1's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 1.95× lower at baseline in the lines without SH2D3A | 0.002 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[MISP]] | B | MISP activity raises TICAM1's level | lines that do not express MISP (23) vs lines expressing it (27) | 2.00× lower at baseline in the lines without MISP | 0.003 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[C1orf116]] | B | C1orf116 activity raises TICAM1's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 2.00× lower at baseline in the lines without C1orf116 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[FSD1]] | B | FSD1 activity lowers TICAM1's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 2.02× higher at baseline in the lines without FSD1 | 0.010 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[INAVA]] | B | INAVA activity raises TICAM1's level | lines that do not express INAVA (29) vs lines expressing it (21) | 1.86× lower at baseline in the lines without INAVA | 0.013 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[CRYBG2]] | B | CRYBG2 activity strengthens TICAM1's drug response | lines that do not express CRYBG2 (23) vs lines expressing it (26) | the lines without CRYBG2 respond 0.67× as strongly (z diff +2.00); strongest at Dinaciclib 5 µM: 0.53x vs 0.31x (z diff +3.4) | 0.020 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1; target measured in part of the lines; artifact flags |
| [[SLC52A3]] | B | SLC52A3 activity raises TICAM1's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 1.85× lower at baseline in the lines without SLC52A3 | 0.021 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[TOP2A]] | B | TOP2A activity raises TICAM1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[C1orf116]] | B | C1orf116 activity strengthens TICAM1's drug response | lines that do not express C1orf116 (31) vs lines expressing it (18) | the lines without C1orf116 respond 0.57× as strongly (z diff +2.67); strongest at Dinaciclib 5 µM: 0.63x vs 0.22x (z diff +5.7) | 0.041 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; target measured in part of the lines; artifact flags |
| [[PTK6]] | B | PTK6 activity raises TICAM1's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 1.81× lower at baseline in the lines without PTK6 | 0.043 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |
| [[SH2D3A]] | B | SH2D3A activity strengthens TICAM1's drug response | lines that do not express SH2D3A (24) vs lines expressing it (25) | the lines without SH2D3A respond 0.59× as strongly (z diff +2.21); strongest at Dinaciclib 5 µM: 0.55x vs 0.31x (z diff +4.1) | 0.045 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3; target measured in part of the lines; artifact flags |
| [[TMEM40]] | B | TMEM40 activity strengthens TICAM1's drug response | lines that do not express TMEM40 (24) vs lines expressing it (25) | the lines without TMEM40 respond 0.70× as strongly (z diff +1.53); strongest at Dinaciclib 0.5 µM: 0.80x vs 0.52x (z diff +3.1) | 0.050 | ⚠ within organs, on part of the lines; also absent: LRG1, LRRN1, WNT7A; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RFFL]] | C | TICAM1's natural level strengthens RFFL's drug response | TICAM1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.13; direction not clear | 0.036 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.582). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.4, 7.1); signed map (7.9, 32.8). **Vector** length 102, 26.0% of its response variance represented; |z| ≥ 3 in 1,124 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.9 | +3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.6 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.2 | -1.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.8 | +6.2 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.3 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | -0.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.1 | +2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.8 | +1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +0.3 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -11.0 |
|  | [[NG25 (drug)]] 5 µM |  | -5.0 | -4.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -11.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.9 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -3.9 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -7.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -5.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.1 | -0.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | TIR domain containing adaptor molecule 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:4,815,932-4,831,712 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRIF, TICAM-1, MGC35334, PRVTIRB |
| Gene groups (HGNC) | TIR domain containing |
| Reactome | 31 pathways, smallest: TRAF3 deficiency - HSE; TLR3-mediated TICAM1-dependent programmed cell death; TRIF-mediated programmed cell death |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUC6](https://www.uniprot.org/uniprotkb/Q8IUC6) (TIR domain-containing adapter molecule 1):

> Involved in innate immunity against invading pathogens. Adapter used by TLR3, TLR4 (through TICAM2) and TLR5 to mediate NF-kappa-B and interferon-regulatory factor (IRF) activation, and to induce programmed cell death, such as apoptosis and necroptosis. Ligand binding to these receptors results in TICAM1/TRIF recruitment through its TIR domain. Distinct protein-interaction motifs allow recruitment of the effector proteins TBK1, TRAF6, RIPK1 and RIPK3, which in turn, lead to the activation of …

**Summary**, from NCBI Gene [148022](https://www.ncbi.nlm.nih.gov/gene/148022):

> This gene encodes an adaptor protein containing a Toll/interleukin-1 receptor (TIR) homology domain, which is an intracellular signaling domain that mediates protein-protein interactions between the Toll-like receptors (TLRs) and signal-transduction components. This protein is involved in native immunity against invading pathogens. It specifically interacts with toll-like receptor 3, but not with other TLRs, and this association mediates dsRNA induction of interferon-beta through activation of …

**Accessions** — [HGNC:18348](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18348) · Entrez [148022](https://www.ncbi.nlm.nih.gov/gene/148022) · UniProt [Q8IUC6](https://www.uniprot.org/uniprotkb/Q8IUC6) · Ensembl [ENSG00000127666](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127666)

## Data

Gene col 4829: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4829); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4829, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4829]; `tensor/DDL_lfc|DDL_z.npy` [4829]; `embed/gene_vectors.npy` [4829]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4829 or target_col == 4829). Every well: [[TICAM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TICAM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
