---
symbol: "INPP5A"
type: "gene"
col: 889
ensembl_id: "ENSG00000068383"
name: "inositol polyphosphate-5-phosphatase A"
location: "10q26.3"
module: 136
arm: "+"
pooled_cpm: 64.69
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# INPP5A

*inositol polyphosphate-5-phosphatase A* — 10q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.72× (z +14.0, q 1e-41, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.451× (z -9.1, q 5e-17, down in 38 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.703× (z -4.9, q 1e-04, down in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (Hs 766T 0.0201×, AN3 CA 0.0969×, LOX-IMVI 0.215×, LoVo 0.276×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (LS 180 0.203×, LOX-IMVI 0.244×, HEC-1-A 0.279×, H4 0.145×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.293×, NCI-H23 0.403×); [[Methylthiouracil (drug)]] 0.05 µM in 1 line (NCI-H596 0.171×); [[Harringtonine (drug)]] 0.5 µM in 1 line (C32 0.326×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL25]] (+0.66, fdr 7e-06), [[TMEM184B]] (+0.65, fdr 1e-05), [[MYO9B]] (+0.62, fdr 3e-05); moves opposite to [[MTPAP]] (-0.65, fdr 1e-05), [[AASDHPPT]] (-0.65, fdr 7e-06), [[GOPC]] (-0.61, fdr 1e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[UNC5B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 889.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.72×** | +14.0 | 1e-41 | 47/48 (KATO III, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.22×** | +11.2 | 2e-26 | 45/48 (SW1417, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.02×** | +9.8 | 1e-20 | 45/48 (KATO III, SW1417, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.9 | 8e-10 | 29/49 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +5.5 | 4e-06 | 31/48 (KATO III, A498, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.43×** | +4.9 | 7e-05 | 34/48 (KATO III, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.005 | 23/48 (COLO 205, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +3.7 | 0.013 | 25/44 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.027 | 23/48 (COLO 205, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +3.2 | 0.078 | 18/49 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 889.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (Hs 766T 0.0201×, AN3 CA 0.0969×, LOX-IMVI 0.215×, LoVo 0.276×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (LS 180 0.203×, LOX-IMVI 0.244×, HEC-1-A 0.279×, H4 0.145×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.293×, NCI-H23 0.403×); [[Methylthiouracil (drug)]] 0.05 µM in 1 line (NCI-H596 0.171×); [[Harringtonine (drug)]] 0.5 µM in 1 line (C32 0.326×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.451×** | -9.1 | 5e-17 | 38/42 (Hs 766T, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.534×** | -8.8 | 5e-16 | 39/48 (LS 180, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.517×** | -8.5 | 3e-15 | 37/45 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.703×** | -4.9 | 1e-04 | 33/48 (C32, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.679×** | -4.4 | 0.001 | 30/47 (C32, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.837× | -3.5 | 0.039 | 18/48 (NCI-H661, hTERT-HPNE, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | 0.655× | -3.1 | 0.16 | 17/49 (SNU-423, Panc 03.27, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 889. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 63.3 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.03× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -10.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 78.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.97× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 56.8 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +15.2) | — |
| [[SW1417 (line)]] | alt | 64.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.81× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -13.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 79.3 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.00× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -14.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 128 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0201× (z -24.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 66.5 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.276× (z -11.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 95.6 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -13.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 59.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.42× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -8.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 58.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.32× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.314× (z -9.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 54.3 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.230× (z -10.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 47.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -15.2) |
| [[A498 (line)]] | wt | 27.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +15.6) | — |
| [[A549 (line)]] | wt | 41.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.96× (z +11.7) | — |
| [[AsPC-1 (line)]] | alt | 107 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -10.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 60.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +11.6) | — |
| [[HEC-1-A (line)]] | alt | 60.0 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.74× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -12.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 86.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 56.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.56× (z +12.0) | — |
| [[PANC-1 (line)]] | alt | 110 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.44× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.342× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 49.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +12.0) | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -9.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 55.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.97× (z +12.2) | — |
| [[AN3 CA (line)]] | alt | 98.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0969× (z -11.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 65.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -10.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 89.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.326× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 64.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.63× (z +8.6) | — |
| [[H4 (line)]] | wt | 74.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -12.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 89.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.85× (z +10.2) | — |
| [[HOP62 (line)]] | alt | 89.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -9.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 25.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.84× (z +10.7) | — |
| [[NCI-H23 (line)]] | alt | 35.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 31.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +8.5) | — |
| [[NCI-H596 (line)]] | alt | 70.8 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.171× (z -15.7) |
| [[SK-MEL-2 (line)]] | alt | 47.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -8.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 63.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -10.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 61.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 108 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 889), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL25]] | +0.66 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[TMEM184B]] | +0.65 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[MYO9B]] | +0.62 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[SEMA3F]] | +0.61 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[TSPAN9]] | +0.61 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[PLCB3]] | +0.60 | +0.59 / +0.50 | both halves | 1e-05 | pathway: Inositol phosphate metabolism; STRING 918 |
| [[PKD1]] | +0.60 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[MBOAT7]] | +0.60 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[CTNNBIP1]] | +0.59 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[PIP5K1C]] | +0.59 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[KDM4B]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[GNAI2]] | +0.59 | +0.56 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTPAP]] | -0.65 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[AASDHPPT]] | -0.65 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[GOPC]] | -0.61 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[MRRF]] | -0.60 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[POLR3C]] | -0.60 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[TRMT13]] | -0.59 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[ZNF260]] | -0.59 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[SENP1]] | -0.59 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[CHURC1]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[ZNF594]] | -0.58 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[BCDIN3D]] | -0.57 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[ZNF140]] | -0.57 | -0.43 / -0.61 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UNC5B]] | B | UNC5B activity raises INPP5A's level | lines that do not express UNC5B (6) vs lines expressing it (44) | 1.20× lower at baseline in the lines without UNC5B | 0.079 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.2, 5.9); signed map (-24.2, 21.2). **Vector** length 90.4, 23.6% of its response variance represented; |z| ≥ 3 in 1,030 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.5 | +14.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.9 | +11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +6.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.1 | +9.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.9 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.2 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | -2.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -4.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -2.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | +0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | +0.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.9 | -1.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | inositol polyphosphate-5-phosphatase A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.3 — chr10:132,537,787-132,783,480 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 5PTASE |
| Gene groups (HGNC) | Phosphoinositide phosphatases |
| Reactome | 2 pathways, smallest: Synthesis of IP2, IP, and Ins in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14642](https://www.uniprot.org/uniprotkb/Q14642) (Inositol polyphosphate-5-phosphatase A):

> Phosphatase that specifically hydrolyzes the 5-phosphate of inositol 1,4,5-trisphosphate to inositol 1,4-bisphosphate, and inositol 1,3,4,5-tetrasphosphate to inositol 1,3,4-trisphosphate. Plays a crucial role in the survival of cerebellar Purkinje cells (By similarity).

**Summary**, from NCBI Gene [3632](https://www.ncbi.nlm.nih.gov/gene/3632):

> The protein encoded by this gene is a membrane-associated type I inositol 1,4,5-trisphosphate (InsP3) 5-phosphatase. InsP3 5-phosphatases hydrolyze Ins(1,4,5)P3, which mobilizes intracellular calcium and acts as a second messenger mediating cell responses to various stimulation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6076](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6076) · Entrez [3632](https://www.ncbi.nlm.nih.gov/gene/3632) · UniProt [Q14642](https://www.uniprot.org/uniprotkb/Q14642) · Ensembl [ENSG00000068383](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068383)

## Data

Gene col 889: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 889); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 889, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 889]; `tensor/DDL_lfc|DDL_z.npy` [889]; `embed/gene_vectors.npy` [889]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 889 or target_col == 889). Every well: [[INPP5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INPP5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
