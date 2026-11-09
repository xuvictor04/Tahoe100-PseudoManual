---
symbol: "COMT"
type: "gene"
col: 1719
ensembl_id: "ENSG00000093010"
name: "catechol-O-methyltransferase"
location: "22q11.21"
module: 5
arm: "+"
pooled_cpm: 30.99
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 23
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# COMT

*catechol-O-methyltransferase* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.93× (z +12.7, q 5e-34, up in 26 of 35 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HepG2/C3A 6.04×, NCI-H1573 3.81×, HS-578T 2.64×, LoVo 2.78×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (HepG2/C3A 9.27×, PANC-1 2.36×, HS-578T 2.83×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HepG2/C3A 6.09×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.278× (z -25.5, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRRF]] (+0.65, fdr 5e-05), [[PEX26]] (+0.65, fdr 2e-05), [[TMEM138]] (+0.65, fdr 1e-05); moves opposite to [[ANKRD37]] (-0.61, fdr 4e-05), [[ING1]] (-0.61, fdr 2e-05), [[NDRG1]] (-0.59, fdr 6e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF254]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1719.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HepG2/C3A 6.04×, NCI-H1573 3.81×, HS-578T 2.64×, LoVo 2.78×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (HepG2/C3A 9.27×, PANC-1 2.36×, HS-578T 2.83×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HepG2/C3A 6.09×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +12.7 | 5e-34 | 26/35 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +10.1 | 2e-21 | 34/44 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.34×** | +5.4 | 1e-05 | 20/39 (HepG2/C3A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +3.2 | 0.18 | 4/47 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.29 | 11/47 (A549, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1719.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.278×** | -25.5 | 0e+00 | 47/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.295×** | -24.3 | 0e+00 | 47/47 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.309×** | -23.4 | 0e+00 | 44/47 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.550×** | -16.8 | 0e+00 | 38/47 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.564×** | -16.1 | 0e+00 | 38/46 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.520×** | -12.6 | 4e-34 | 43/47 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.710×** | -9.6 | 6e-20 | 35/47 (PANC-1, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.620×** | -9.5 | 2e-19 | 35/46 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.646×** | -8.3 | 5e-15 | 30/47 (Panc 03.27, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.673×** | -7.6 | 2e-12 | 25/47 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.706×** | -6.9 | 3e-10 | 32/47 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.709×** | -6.8 | 4e-10 | 29/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.716×** | -6.6 | 1e-09 | 24/45 (SHP-77, SW480, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.535×** | -6.5 | 3e-09 | 29/47 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.737×** | -6.0 | 6e-08 | 26/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.757×** | -5.5 | 1e-06 | 24/47 (CHP-212, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.609×** | -5.2 | 9e-06 | 24/47 (KATO III, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.817×** | -4.0 | 0.002 | 15/46 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.841× | -3.4 | 0.015 | 16/47 (SW48, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1719. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 23.0 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +9.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.186× (z -15.3) |
| [[Panc 03.27 (line)]] | alt | 39.3 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.196× (z -13.6) |
| [[PANC-1 (line)]] | alt | 25.7 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.36× (z +9.7) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.229× (z -17.3) |
| [[RKO (line)]] | wt | 42.6 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.126× (z -18.1) |
| [[MIA PaCa-2 (line)]] | alt | 56.7 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.115× (z -20.8) |
| [[NCI-H460 (line)]] | wt | 24.8 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -14.7) |
| [[HEC-1-A (line)]] | alt | 49.0 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.292× (z -13.9) |
| [[HS-578T (line)]] | alt | 59.3 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +9.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.247× (z -13.5) |
| [[SNU-1 (line)]] | wt | 51.7 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.173× (z -12.1) |
| [[SW1417 (line)]] | alt | 30.9 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -13.7) |
| [[SW480 (line)]] | alt | 28.3 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -19.0) |
| [[C-33 A (line)]] | alt | 41.7 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -15.8) |
| [[C32 (line)]] | wt | 25.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -22.7) |
| [[H4 (line)]] | wt | 32.3 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.110× (z -12.9) |
| [[HOP62 (line)]] | alt | 29.5 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.182× (z -15.4) |
| [[HT-29 (line)]] | alt | 48.8 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 26.2 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -12.9) |
| [[SK-MEL-2 (line)]] | alt | 59.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.233× (z -13.7) |
| [[SNU-423 (line)]] | alt | 33.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -16.2) |
| [[A498 (line)]] | wt | 42.4 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -21.9) |
| [[HepG2_C3A (line)]] | wt | 31.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.27× (z +12.7) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 29.9 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.136× (z -11.7) |
| [[A-172 (line)]] | wt | 29.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.183× (z -14.4) |
| [[A-427 (line)]] | wt | 19.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.185× (z -11.9) |
| [[A549 (line)]] | wt | 24.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.253× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 27.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.342× (z -10.0) |
| [[KATO III (line)]] | alt | 25.5 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.283× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 24.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.246× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 25.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.277× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 30.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 15.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -9.6) |
| [[BT-474 (line)]] | alt | 31.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.297× (z -8.8) |
| [[COLO 205 (line)]] | alt | 24.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -10.6) |
| [[HCT15 (line)]] | alt | 33.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -11.7) |
| [[hTERT-HPNE (line)]] | wt | 33.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.235× (z -9.1) |
| [[LS 180 (line)]] | wt | 25.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.306× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 36.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 32.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.334× (z -8.8) |
| [[SHP-77 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.108× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~54% of this change |
| [[AN3 CA (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1719), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRRF]] | +0.65 | +0.39 / +0.63 | both halves | 5e-05 |  |
| [[PEX26]] | +0.65 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[TMEM138]] | +0.65 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[TXNRD2]] | +0.65 | +0.39 / +0.69 | both halves | 5e-05 | STRING 806; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[NUP42]] | +0.63 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[ITPA]] | +0.62 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[MAPKAPK5]] | +0.60 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[QTRT1]] | +0.59 | +0.33 / +0.54 | both halves | 1e-04 |  |
| [[METAP1D]] | +0.58 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[LINC00665]] | +0.56 | +0.39 / +0.44 | both halves | 5e-05 |  |
| [[NAA25]] | +0.56 | +0.55 / +0.55 | both halves | 1e-05 | same gene group |
| [[MDM4]] | +0.56 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[NOL9]] | +0.56 | +0.43 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD37]] | -0.61 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[ING1]] | -0.61 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[NDRG1]] | -0.59 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[TNFRSF11A]] | -0.56 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[CIB1]] | -0.56 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[TRPT1]] | -0.55 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[RNASE4]] | -0.55 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[UBA6]] | -0.53 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[CALM1]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 | pathway: Neuronal System |
| [[CXCR4]] | -0.53 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[DNAAF3]] | -0.53 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[CASTOR1]] | -0.53 | -0.40 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF254]] | B | ZNF254 activity raises COMT's level | lines that do not express ZNF254 (6) vs lines expressing it (44) | 1.27× lower at baseline in the lines without ZNF254 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000283201, ZNF571, ZNF613 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.460). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-17.1, -30.7); signed map (-8.3, -42.3). **Vector** length 68.2, 13.3% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.9 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +2.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +1.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -9.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.0 | -12.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.4 | -5.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.3 | -23.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.2 | -16.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -1.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.8 | -1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -0.2 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | catechol-O-methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:19,941,371-19,969,975 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MicroRNA protein coding host genes; 7BS small molecule methyltransferases; Small molecule methyltransferases |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 9 pathways, smallest: Neurotransmitter clearance; Methylation; Phase II - Conjugation of compounds |
| Matched by | ensembl_id |

**Function**, from UniProt [P21964](https://www.uniprot.org/uniprotkb/P21964) (Catechol O-methyltransferase):

> Catalyzes the O-methylation, and thereby the inactivation, of catecholamine neurotransmitters and catechol hormones. Also shortens the biological half-lives of certain neuroactive drugs, like L-DOPA, alpha-methyl DOPA and isoproterenol.

**Summary**, from NCBI Gene [1312](https://www.ncbi.nlm.nih.gov/gene/1312):

> Catechol-O-methyltransferase catalyzes the transfer of a methyl group from S-adenosylmethionine to catecholamines, including the neurotransmitters dopamine, epinephrine, and norepinephrine. This O-methylation results in one of the major degradative pathways of the catecholamine transmitters. In addition to its role in the metabolism of endogenous substances, COMT is important in the metabolism of catechol drugs used in the treatment of hypertension, asthma, and Parkinson disease. COMT is found …

**Accessions** — [HGNC:2228](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2228) · Entrez [1312](https://www.ncbi.nlm.nih.gov/gene/1312) · UniProt [P21964](https://www.uniprot.org/uniprotkb/P21964) · Ensembl [ENSG00000093010](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000093010)

## Data

Gene col 1719: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1719); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1719, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1719]; `tensor/DDL_lfc|DDL_z.npy` [1719]; `embed/gene_vectors.npy` [1719]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1719 or target_col == 1719). Every well: [[COMT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COMT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
