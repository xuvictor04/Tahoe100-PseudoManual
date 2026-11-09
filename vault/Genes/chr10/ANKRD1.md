---
symbol: "ANKRD1"
type: "gene"
col: 7304
ensembl_id: "ENSG00000148677"
name: "ankyrin repeat domain 1"
location: "10q23.31"
module: 120
arm: "+"
pooled_cpm: 37.54
n_lines_expressing: 20
n_dd_up: 47
n_dd_down: 3
n_dd_up_clean: 31
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# ANKRD1

*ankyrin repeat domain 1* — 10q23.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 47 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.85× (z +15.4, q 0e+00, up in 13 of 18 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 7.99× (z +14.4, q 3e-44, up in 15 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.513× (z -4.6, q 0.002, down in 13 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (SW480 0.128×, HepG2/C3A 0.207×, SW1417 0.258×, C-33 A 0.138×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 3 lines (J82 0.180×, Hs 766T 0.150×, SW1417 0.244×; ⚠ cell-cycle shift, explains ~80% of this change); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SW480 0.0608×); [[Cobimetinib (drug)]] 5 µM in 1 line (SW480 0.119×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCN1]] (+0.64, fdr 1e-05), [[DLC1]] (+0.59, fdr 2e-05), [[MYC]] (+0.57, fdr 2e-05); moves opposite to [[HOXA3]] (-0.49, fdr 3e-05), [[USF1]] (-0.48, fdr 5e-05), [[GNAS]] (-0.48, fdr 4e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC01186]] → it (grade B ⚠); 3 go from it, the strongest it → [[LINC01186]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 47 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7304.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **4.85×** | +15.4 | 0e+00 | 13/18 (A-172, CFPAC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **7.99×** | +14.4 | 3e-44 | 15/18 (A-172, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.81×** | +9.2 | 5e-18 | 13/18 (CFPAC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **3.57×** | +8.8 | 2e-16 | 9/17 (Panc 03.27, SW 900, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.44×** | +8.5 | 2e-15 | 9/18 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **2.21×** | +7.8 | 8e-13 | 15/18 (SK-MEL-2, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **3.16×** | +7.6 | 2e-12 | 14/18 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **3.00×** | +7.6 | 2e-12 | 11/18 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **2.84×** | +6.9 | 2e-10 | 17/18 (A-172, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.94×** | +6.9 | 3e-10 | 10/17 (Panc 03.27, SNU-423, …) | all doses, flat | composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **4.18×** | +6.7 | 1e-09 | 17/17 (SW 900, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.56×** | +6.5 | 4e-09 | 9/18 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **2.61×** | +6.4 | 7e-09 | 14/18 (NCI-H460, SK-MEL-2, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **2.47×** | +6.3 | 2e-08 | 14/18 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.41×** | +6.1 | 4e-08 | 10/18 (A-172, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **2.23×** | +5.6 | 9e-07 | 16/18 (SW 900, A-172, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 5 µM |  | **4.20×** | +5.2 | 6e-06 | 13/16 (SK-MEL-2, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **2.11×** | +5.2 | 6e-06 | 13/18 (A-172, SNU-423, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.11×** | +5.2 | 6e-06 | 11/18 (A-172, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belumosudil (drug)]] 5 µM |  | **2.11×** | +5.0 | 2e-05 | 5/18 (SK-MEL-2, SNU-423, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +4.8 | 4e-05 | 8/18 (SK-MEL-2, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.89×** | +4.4 | 2e-04 | 12/18 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7304.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (SW480 0.128×, HepG2/C3A 0.207×, SW1417 0.258×, C-33 A 0.138×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 3 lines (J82 0.180×, Hs 766T 0.150×, SW1417 0.244×; ⚠ cell-cycle shift, explains ~80% of this change); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SW480 0.0608×); [[Cobimetinib (drug)]] 5 µM in 1 line (SW480 0.119×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.513×** | -4.6 | 0.002 | 13/18 (J82, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.644×** | -4.3 | 0.005 | 11/18 (J82, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.587×** | -3.7 | 0.044 | 10/18 (CFPAC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Pentagastrin (drug)]] 5 µM |  | 0.727× | -3.1 | 0.25 | 9/18 (hTERT-HPNE, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7304. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 88.6 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.1× (z +13.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 27.9× (z +11.8) | — |
| [[SW480 (line)]] | alt | 98.5 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0608× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 46.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 23.2× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 209 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +13.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 9.34× (z +12.3) | — |
| [[NCI-H460 (line)]] | wt | 10.4 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 23.5× (z +10.4) | — |
| [[SK-MEL-2 (line)]] | alt | 280 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 14.3× (z +10.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 8.72× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 42.8 | 3 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 15.6× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 45.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +10.1) ⚠ cell-cycle shift, explains ~30% of this change | [[Selinexor (drug)]] 5 µM 0.150× (z -9.9) ⚠ cell-cycle shift, explains ~80% of this change |
| [[J82 (line)]] | alt | 78.5 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.180× (z -10.6) ⚠ cell-cycle shift, explains ~80% of this change |
| [[SNU-423 (line)]] | alt | 170 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.63× (z +11.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 19.8× (z +11.2) | — |
| [[SW 900 (line)]] | alt | 37.2 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 33.0× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 40.3 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.244× (z -9.2) ⚠ cell-cycle shift, explains ~80% of this change |
| [[C-33 A (line)]] | alt | 72.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 350 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 2.95 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.24 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.07 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.99 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.35 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.93 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.83 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.45 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.13 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.04 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.93 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.31 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.40 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.30 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.84 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.25 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7304), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCN1]] | +0.64 | +0.53 / +0.61 | both halves | 1e-05 | STRING 772 |
| [[DLC1]] | +0.59 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[MYC]] | +0.57 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[WWC1]] | +0.57 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[IGF2BP2]] | +0.57 | +0.39 / +0.58 | both halves | 6e-05 |  |
| [[MIR4435-2HG]] | +0.56 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[SRGAP1]] | +0.55 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[CYTOR]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[STARD13]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[LINC00707]] | +0.52 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[RASAL2]] | +0.51 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[PTPRN2]] | +0.51 | +0.44 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA3]] | -0.49 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[USF1]] | -0.48 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[GNAS]] | -0.48 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[TMEM94]] | -0.48 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[FAM76B]] | -0.46 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[VDAC1P8]] | -0.45 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[HDAC6]] | -0.45 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[MED24]] | -0.44 | -0.38 / -0.32 | both halves | 2e-04 | pathway: PPARA activates gene expression |
| [[EPHX1]] | -0.44 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[GLE1]] | -0.43 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[MFSD8]] | -0.43 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[SUOX]] | -0.42 | -0.21 / -0.43 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01186]] | B | LINC01186 activity raises ANKRD1's level | lines that do not express LINC01186 (12) vs lines expressing it (38) | 3.51× lower at baseline in the lines without LINC01186 | 0.058 | ⚠ within organs, on part of the lines; also absent: LINC01836, STXBP2, EEPD1 |
| [[TSPAN2]] | B | TSPAN2 activity raises ANKRD1's level | lines that do not express TSPAN2 (19) vs lines expressing it (31) | 2.21× lower at baseline in the lines without TSPAN2 | 0.096 | ⚠ within organs, on part of the lines; also absent: SAA1, STK32A, IFI44L |
| [[SHISA9]] | C | SHISA9 activity raises ANKRD1's level | lines that do not express SHISA9 (38) vs lines expressing it (12) | 2.25× lower at baseline in the lines without SHISA9 | 0.050 | ⚠ within organs, on part of the lines; also absent: LHFPL3-AS1, S100A1, LINC01456; maybe low, not absent; co-absent with the target |
| [[ST6GALNAC5]] | C | ST6GALNAC5 activity raises ANKRD1's level | lines that do not express ST6GALNAC5 (31) vs lines expressing it (19) | 1.99× lower at baseline in the lines without ST6GALNAC5 | 0.084 | ⚠ within organs, on part of the lines; also absent: TRBC2, ENPP5, KCNH8; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01186]] | B | ANKRD1 activity raises LINC01186's level | lines that do not express ANKRD1 (30) vs lines expressing it (20) | 1.69× lower at baseline in the lines without ANKRD1 | 0.041 | ⚠ within organs, on part of the lines; also absent: CAVIN2-AS1, WNT7A, NPPB |
| [[MIR4435-2HG]] | B | ANKRD1 activity raises MIR4435-2HG's level | lines that do not express ANKRD1 (30) vs lines expressing it (20) | 1.40× lower at baseline in the lines without ANKRD1 | 0.088 | ⚠ within organs, on part of the lines; also absent: CAVIN2-AS1, WNT7A, NPPB |
| [[SHISA9]] | C | ANKRD1 activity raises SHISA9's level | lines that do not express ANKRD1 (30) vs lines expressing it (20) | 1.61× lower at baseline in the lines without ANKRD1 | 0.005 | ⚠ within organs, on part of the lines; also absent: CAVIN2-AS1, WNT7A, NPPB; co-absent with the target |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.647). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.7, 11.8); signed map (13.6, 40.8). **Vector** length 65.1, 17.9% of its response variance represented; |z| ≥ 3 in 684 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.0 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +3.1 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.8 | +9.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.8 | +6.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +4.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.5 | +5.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | -2.1 | -4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.8 | -1.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.6 | -2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.3 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.2 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.31 — chr10:90,912,096-90,921,087 (-) |
| Ensembl biotype | protein_coding |
| Also known as | C-193, ALRP, CARP, CVARP, MCARP |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Reactome | 3 pathways, smallest: PPARA activates gene expression; Regulation of lipid metabolism by PPARalpha; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15327](https://www.uniprot.org/uniprotkb/Q15327) (Ankyrin repeat domain-containing protein 1):

> May play an important role in endothelial cell activation. May act as a nuclear transcription factor that negatively regulates the expression of cardiac genes. Induction seems to be correlated with apoptotic cell death in hepatoma cells.

**Summary**, from NCBI Gene [27063](https://www.ncbi.nlm.nih.gov/gene/27063):

> The protein encoded by this gene is localized to the nucleus of endothelial cells and is induced by IL-1 and TNF-alpha stimulation. Studies in rat cardiomyocytes suggest that this gene functions as a transcription factor. Interactions between this protein and the sarcomeric proteins myopalladin and titin suggest that it may also be involved in the myofibrillar stretch-sensor system. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15819](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15819) · Entrez [27063](https://www.ncbi.nlm.nih.gov/gene/27063) · UniProt [Q15327](https://www.uniprot.org/uniprotkb/Q15327) · Ensembl [ENSG00000148677](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148677)

## Data

Gene col 7304: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7304); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7304, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7304]; `tensor/DDL_lfc|DDL_z.npy` [7304]; `embed/gene_vectors.npy` [7304]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7304 or target_col == 7304). Every well: [[ANKRD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
