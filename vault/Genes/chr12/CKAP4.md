---
symbol: "CKAP4"
type: "gene"
col: 5801
ensembl_id: "ENSG00000136026"
name: "cytoskeleton associated protein 4"
location: "12q23.3"
module: 42
arm: "+"
pooled_cpm: 59.0
n_lines_expressing: 46
n_dd_up: 4
n_dd_down: 23
n_dd_up_clean: 0
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# CKAP4

*cytoskeleton associated protein 4* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.28× (z +8.7, q 1e-15, up in 31 of 35 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 5 lines (A549 6.19×, SNU-423 5.06×, PANC-1 3.40×, LoVo 3.13×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-423 5.44×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-423 4.29×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.333× (z -17.0, q 0e+00, down in 42 of 44 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDIA3]] (+0.58, fdr 1e-05), [[TXNDC15]] (+0.55, fdr 2e-05), [[SDF4]] (+0.53, fdr 2e-05); moves opposite to [[PCMTD2]] (-0.49, fdr 4e-05), [[BAIAP3]] (-0.49, fdr 1e-04), [[VPS8]] (-0.47, fdr 1e-04).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NOXA1]] → it (grade B ⚠); 3 go from it, the strongest it → [[PDIA3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5801.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 5 lines (A549 6.19×, SNU-423 5.06×, PANC-1 3.40×, LoVo 3.13×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-423 5.44×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-423 4.29×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +8.7 | 1e-15 | 31/35 (A549, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +8.4 | 1e-14 | 34/41 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.43×** | +4.0 | 0.008 | 23/43 (HCT15, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +4.0 | 0.008 | 22/39 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.22× | +3.1 | 0.17 | 21/44 (SNU-423, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 5 µM |  | 1.33× | +3.1 | 0.17 | 24/44 (HepG2/C3A, HT-29, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | 1.33× | +3.1 | 0.17 | 17/44 (SNU-423, LoVo, …) | top dose only |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.21× | +3.0 | 0.18 | 18/44 (A-427, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5801.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.333×** | -17.0 | 0e+00 | 42/44 (A-172, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.245×** | -15.4 | 0e+00 | 44/44 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.252×** | -15.1 | 0e+00 | 43/44 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.284×** | -13.8 | 7e-41 | 43/44 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.442×** | -8.9 | 5e-17 | 35/44 (HS-578T, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.462×** | -8.1 | 5e-14 | 37/44 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.512×** | -7.3 | 2e-11 | 35/44 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.512×** | -7.3 | 2e-11 | 40/44 (NCI-H2030, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.537×** | -6.8 | 8e-10 | 37/44 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.565×** | -6.2 | 3e-08 | 30/44 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.594×** | -5.7 | 7e-07 | 33/44 (HepG2/C3A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.656×** | -4.4 | 5e-04 | 27/44 (HepG2/C3A, A498, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.481×** | -4.2 | 0.001 | 28/44 (A498, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.685×** | -4.1 | 0.002 | 27/44 (SW48, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.775×** | -3.9 | 0.004 | 26/44 (LoVo, KATO III, …) | rises with dose | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.520×** | -3.7 | 0.007 | 25/44 (A-427, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5801. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 80.8 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -18.9) |
| [[A-172 (line)]] | wt | 198 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -25.2) |
| [[A498 (line)]] | wt | 205 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 2.66× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -18.2) |
| [[HS-578T (line)]] | alt | 120 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -18.5) |
| [[A549 (line)]] | wt | 34.4 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 6.19× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -17.0) |
| [[C32 (line)]] | wt | 49.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 155 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -11.6) |
| [[LoVo (line)]] | wt | 55.4 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +9.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.0788× (z -21.2) |
| [[RKO (line)]] | wt | 33.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -18.5) |
| [[COLO 205 (line)]] | alt | 37.1 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.114× (z -12.1) |
| [[H4 (line)]] | wt | 175 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -13.0) |
| [[HCT15 (line)]] | alt | 44.0 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 122 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.221× (z -11.6) |
| [[HOP62 (line)]] | alt | 75.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -15.4) |
| [[Hs 766T (line)]] | wt | 35.1 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.152× (z -12.9) |
| [[J82 (line)]] | alt | 62.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -14.6) |
| [[LOX-IMVI (line)]] | wt | 54.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -19.2) |
| [[NCI-H1573 (line)]] | alt | 63.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -13.7) |
| [[NCI-H1792 (line)]] | alt | 63.7 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.144× (z -14.1) |
| [[RPMI-7951 (line)]] | alt | 68.5 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.199× (z -11.1) |
| [[A-427 (line)]] | wt | 32.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -11.3) |
| [[AN3 CA (line)]] | alt | 57.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 37.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -10.2) |
| [[HT-29 (line)]] | alt | 23.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.144× (z -11.9) |
| [[KATO III (line)]] | alt | 41.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0805× (z -19.3) |
| [[LS 180 (line)]] | wt | 32.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.124× (z -13.5) |
| [[MIA PaCa-2 (line)]] | alt | 25.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 56.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -19.0) |
| [[NCI-H23 (line)]] | alt | 33.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0849× (z -22.4) |
| [[NCI-H2347 (line)]] | alt | 57.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -11.7) |
| [[SNU-423 (line)]] | alt | 64.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.06× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 72.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.130× (z -16.5) |
| [[BT-474 (line)]] | alt | 36.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.250× (z -9.1) |
| [[SNU-1 (line)]] | wt | 27.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -9.7) |
| [[C-33 A (line)]] | alt | 50.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -9.1) |
| [[PANC-1 (line)]] | alt | 46.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.40× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 17.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -9.6) |
| [[SW48 (line)]] | wt | 31.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -11.2) |
| [[AsPC-1 (line)]] | alt | 9.58 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 56.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5801), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDIA3]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[TXNDC15]] | +0.55 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[SDF4]] | +0.53 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[GPX8]] | +0.53 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[SERPINH1]] | +0.53 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[P3H3]] | +0.51 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[COPB2]] | +0.50 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[ZNF75D]] | +0.50 | +0.36 / +0.52 | both halves | 9e-05 |  |
| [[B4GALNT1]] | +0.50 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[SLC6A9]] | +0.49 | +0.37 / +0.44 | both halves | 8e-05 |  |
| [[CNPY2]] | +0.49 | +0.39 / +0.45 | both halves | 5e-05 |  |
| [[SLC39A7]] | +0.49 | +0.37 / +0.50 | both halves | 7e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCMTD2]] | -0.49 | -0.40 / -0.48 | both halves | 4e-05 |  |
| [[BAIAP3]] | -0.49 | -0.32 / -0.41 | both halves | 1e-04 |  |
| [[VPS8]] | -0.47 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[NUDT14]] | -0.45 | -0.33 / -0.32 | both halves | 2e-04 |  |
| [[HIF1AN]] | -0.43 | -0.25 / -0.37 | both halves | 4e-04 |  |
| [[CBX7]] | -0.43 | -0.39 / -0.23 | both halves | 5e-04 |  |
| [[GGA1]] | -0.43 | -0.17 / -0.29 | ⚠ not reproduced | 0.001 |  |
| [[UBBP4-1]] | -0.42 | -0.31 / -0.32 | both halves | 2e-04 |  |
| [[RBFA]] | -0.42 | -0.22 / -0.37 | both halves | 6e-04 |  |
| [[MCTP1]] | -0.42 | -0.29 / -0.41 | both halves | 2e-04 |  |
| [[R3HDM4]] | -0.41 | -0.25 / -0.35 | both halves | 4e-04 |  |
| [[TPPP]] | -0.41 | -0.26 / -0.41 | both halves | 4e-04 |  |
| [[NKD2]] | -0.41 | -0.29 / -0.39 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOXA1]] | B | NOXA1 activity lowers CKAP4's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 2.28× higher at baseline in the lines without NOXA1 | 0.057 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDIA3]] | C | CKAP4 activity raises PDIA3's level | lines that do not express CKAP4 (4) vs lines expressing it (46) | 1.55× lower at baseline in the lines without CKAP4 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CAMKK1; maybe low, not absent; its own permutation p |
| [[HYOU1]] | C | CKAP4 activity raises HYOU1's level | lines that do not express CKAP4 (4) vs lines expressing it (46) | 1.38× lower at baseline in the lines without CKAP4 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CAMKK1; maybe low, not absent; its own permutation p |
| [[PDIA6]] | C | CKAP4 activity raises PDIA6's level | lines that do not express CKAP4 (4) vs lines expressing it (46) | 1.52× lower at baseline in the lines without CKAP4 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CAMKK1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.389). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.2, -9.0); signed map (-29.5, -23.0). **Vector** length 82.1, 23.8% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +2.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +1.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.6 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | -2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +0.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.2 | +1.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.1 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -2.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.7 | -5.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.7 | -15.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.6 | -0.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.6 | -15.4 |
|  | [[4EGI-1 (drug)]] 5 µM |  | -2.3 | -0.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.8 | -0.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | cytoskeleton associated protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:106,237,881-106,304,279 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P63, CLIMP-63, CLIMP63, ERGIC-63 |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 10 pathways, smallest: Surfactant metabolism; RND2 GTPase cycle; RND3 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07065](https://www.uniprot.org/uniprotkb/Q07065) (Cytoskeleton-associated protein 4):

> Mediates the anchoring of the endoplasmic reticulum to microtubules.; High-affinity epithelial cell surface receptor for the FZD8-related low molecular weight sialoglycopeptide APF/antiproliferative factor. Mediates the APF antiproliferative signaling within cells.

**Summary**, from NCBI Gene [10970](https://www.ncbi.nlm.nih.gov/gene/10970):

> Enables RNA binding activity. Located in lipid droplet and rough endoplasmic reticulum. Biomarker of hepatocellular carcinoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16991](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16991) · Entrez [10970](https://www.ncbi.nlm.nih.gov/gene/10970) · UniProt [Q07065](https://www.uniprot.org/uniprotkb/Q07065) · Ensembl [ENSG00000136026](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136026)

## Data

Gene col 5801: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5801); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5801, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5801]; `tensor/DDL_lfc|DDL_z.npy` [5801]; `embed/gene_vectors.npy` [5801]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5801 or target_col == 5801). Every well: [[CKAP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CKAP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
