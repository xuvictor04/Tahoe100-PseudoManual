---
symbol: "IRS1"
type: "gene"
col: 9744
ensembl_id: "ENSG00000169047"
name: "insulin receptor substrate 1"
location: "2q36.3"
module: 1
arm: "+"
pooled_cpm: 35.55
n_lines_expressing: 44
n_dd_up: 16
n_dd_down: 22
n_dd_up_clean: 16
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# IRS1

*insulin receptor substrate 1* — 2q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.82× (z +7.5, q 2e-11, up in 25 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.398× (z -11.7, q 1e-28, down in 32 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAT1]] (+0.66, fdr 7e-06), [[RRS1]] (+0.61, fdr 8e-06), [[ADO]] (+0.61, fdr 1e-05); moves opposite to [[GPR107]] (-0.60, fdr 1e-05), [[KCTD7]] (-0.57, fdr 1e-05), [[TMEM50B]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SDHAP3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZNF462]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, none with an alert; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9744.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +7.5 | 2e-11 | 25/42 (A-172, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +5.6 | 6e-06 | 21/42 (A-172, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +5.2 | 3e-05 | 22/42 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.19×** | +5.2 | 3e-05 | 21/42 (NCI-H460, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.003 | 15/42 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.39×** | +4.1 | 0.003 | 21/42 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.007 | 17/42 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.008 | 15/42 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.009 | 15/42 (NCI-H1573, Panc 03.27, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **1.33×** | +3.6 | 0.016 | 14/42 (MIA PaCa-2, CHP-212, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.023 | 7/42 (NCI-H1573, SW 900, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **1.32×** | +3.5 | 0.024 | 11/42 (NCI-H1573, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.37×** | +3.5 | 0.024 | 12/41 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.077 | 8/42 (NCI-H1573, CFPAC-1, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.077 | 8/42 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9744.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.398×** | -11.7 | 1e-28 | 32/42 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.552×** | -7.5 | 2e-11 | 30/42 (LoVo, C-33 A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.565×** | -7.2 | 9e-11 | 26/42 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.553×** | -7.1 | 2e-10 | 28/42 (LoVo, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -6.4 | 2e-08 | 28/42 (MIA PaCa-2, LoVo, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.604×** | -6.4 | 2e-08 | 28/40 (BT-474, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.629×** | -5.9 | 4e-07 | 25/42 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.637×** | -5.7 | 8e-07 | 29/42 (LoVo, C-33 A, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.664×** | -5.2 | 1e-05 | 24/42 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.674×** | -4.8 | 9e-05 | 23/42 (SNU-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.701×** | -4.3 | 8e-04 | 20/40 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.753×** | -3.6 | 0.015 | 17/42 (NCI-H2030, BT-474, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.582×** | -3.6 | 0.015 | 16/41 (RPMI-7951, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM |  | **0.826×** | -3.4 | 0.025 | 13/42 (HT-29, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.762×** | -3.3 | 0.035 | 15/40 (HEC-1-A, SNU-423, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.779×** | -3.2 | 0.055 | 16/41 (NCI-H1573, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9744. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 59.1 | 0 | 27 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0836× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 0.5 µM 0.0918× (z -13.5) |
| [[LoVo (line)]] | wt | 81.9 | 0 | 16 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0864× (z -23.0) |
| [[SNU-1 (line)]] | wt | 193 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -15.8) |
| [[C-33 A (line)]] | alt | 99.0 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.155× (z -14.5) |
| [[CHP-212 (line)]] | wt | 135 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -13.0) |
| [[SW48 (line)]] | wt | 117 | 2 | 5 | [[Homoharringtonine (drug)]] 0.5 µM 4.06× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.0891× (z -16.1) |
| [[LS 180 (line)]] | wt | 41.5 | 0 | 6 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 24.9 | 3 | 3 | [[TAK-901 (drug)]] 5 µM 13.9× (z +10.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -13.6) |
| [[MIA PaCa-2 (line)]] | alt | 121 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -20.5) |
| [[A-172 (line)]] | wt | 8.98 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.80× (z +11.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 9.79× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 98.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.240× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 43.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.217× (z -10.2) |
| [[PANC-1 (line)]] | alt | 30.5 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.304× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.342× (z -9.5) |
| [[SW1417 (line)]] | alt | 46.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 59.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.136× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 23.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.189× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.193× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 38.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -10.5) |
| [[HCT15 (line)]] | alt | 39.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -9.0) |
| [[Hs 766T (line)]] | wt | 26.0 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0472× (z -12.6) |
| [[HT-29 (line)]] | alt | 42.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.245× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 10.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0936× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0317× (z -14.5) |
| [[A-427 (line)]] | wt | 5.05 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.41 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.25 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.97 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.82 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.04 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9744), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAT1]] | +0.66 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[RRS1]] | +0.61 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[ADO]] | +0.61 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[MYC]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN; STRING 667 |
| [[BYSL]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[MGA]] | +0.58 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[COA7]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[FJX1]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[HNRNPF]] | +0.57 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[SF3B3]] | +0.56 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[CSTF2T]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[GOPC]] | +0.55 | +0.59 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR107]] | -0.60 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[KCTD7]] | -0.57 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[TMEM50B]] | -0.57 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[RARS2]] | -0.56 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[RAB6A]] | -0.56 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[MAX]] | -0.55 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[CBFA2T2]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[DPM1]] | -0.55 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[ULK1]] | -0.54 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[GET1-SH3BGR]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[HSPB11]] | -0.54 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[GET1]] | -0.53 | -0.53 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SDHAP3]] | B | SDHAP3 activity raises IRS1's level | lines that do not express SDHAP3 (8) vs lines expressing it (42) | 2.45× lower at baseline in the lines without SDHAP3 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000291079, PHKA1, C1orf115 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF462]] | B | IRS1 activity raises ZNF462's level | lines that do not express IRS1 (6) vs lines expressing it (44) | 1.04× lower at baseline in the lines without IRS1 | 0.036 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.527). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-17.2, -38.0); signed map (3.3, -40.6). **Vector** length 119, 32.8% of its response variance represented; |z| ≥ 3 in 1,104 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.5 | +7.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.3 | +5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.3 | +5.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.1 | +5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.0 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.7 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.2 | +4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +3.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -6.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.0 | -7.1 |
|  | [[Artesunate (drug)]] 5 µM |  | -2.7 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.7 | -7.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -2.5 | -3.0 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -2.3 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -5.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.1 | -0.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | insulin receptor substrate 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.3 — chr2:226,731,312-226,799,820 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HIRS-1 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Insulin receptor substrate family |
| Hallmark sets | UV_RESPONSE_DN, APICAL_JUNCTION |
| Reactome | 39 pathways, smallest: IRS activation; Activated NTRK3 signals through PI3K; SOS-mediated signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [P35568](https://www.uniprot.org/uniprotkb/P35568) (Insulin receptor substrate 1):

> Signaling adapter protein that participates in the signal transduction from two prominent receptor tyrosine kinases, insulin receptor/INSR and insulin-like growth factor I receptor/IGF1R. Plays therefore an important role in development, growth, glucose homeostasis as well as lipid metabolism. Upon phosphorylation by the insulin receptor, functions as a signaling scaffold that propagates insulin action through binding to SH2 domain-containing proteins including the p85 regulatory subunit of …

**Summary**, from NCBI Gene [3667](https://www.ncbi.nlm.nih.gov/gene/3667):

> This gene encodes a protein which is phosphorylated by insulin receptor tyrosine kinase. Mutations in this gene are associated with type II diabetes and susceptibility to insulin resistance. [provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:6125](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6125) · Entrez [3667](https://www.ncbi.nlm.nih.gov/gene/3667) · UniProt [P35568](https://www.uniprot.org/uniprotkb/P35568) · Ensembl [ENSG00000169047](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169047)

## Data

Gene col 9744: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9744); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9744, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9744]; `tensor/DDL_lfc|DDL_z.npy` [9744]; `embed/gene_vectors.npy` [9744]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9744 or target_col == 9744). Every well: [[IRS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IRS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
