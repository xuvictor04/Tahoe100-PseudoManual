---
symbol: "GNGT1"
type: "gene"
col: 4843
ensembl_id: "ENSG00000127928"
name: "G protein subunit gamma transducin 1"
location: "7q21.3"
module: 117
arm: "+"
pooled_cpm: 101.22
n_lines_expressing: 20
n_dd_up: 29
n_dd_down: 10
n_dd_up_clean: 23
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 6
direction_downstream: 13
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# GNGT1

*G protein subunit gamma transducin 1* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.74× (z +16.6, q 0e+00, up in 2 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.83× (z +14.1, q 1e-42, up in 12 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.636× (z -7.4, q 5e-11, down in 18 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALOX12P2-1]] (+0.68, fdr 1e-05), [[LRP1B]] (+0.68, fdr 1e-05), [[CLIC2]] (+0.67, fdr 1e-05); moves opposite to [[ZMYND19]] (-0.62, fdr 1e-05), [[ODF2]] (-0.61, fdr 1e-05), [[FBH1]] (-0.59, fdr 2e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SLC44A5]] → it (grade B ⚠); 13 go from it, the strongest it → [[BANK1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4843.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.74×** | +16.6 | 0e+00 | 2/19 (AsPC-1, SW480) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.69×** | +15.1 | 0e+00 | 9/18 (LoVo, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +14.1 | 1e-42 | 12/18 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +11.8 | 4e-30 | 0/19 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.89×** | +9.9 | 4e-21 | 18/18 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +8.9 | 7e-17 | 2/18 (LS 180, AsPC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.68×** | +8.6 | 9e-16 | 18/18 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +8.0 | 9e-14 | 16/18 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +7.1 | 6e-11 | 16/18 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.8 | 4e-07 | 0/20 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +5.2 | 1e-05 | 10/18 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.52×** | +4.8 | 8e-05 | 11/19 (KATO III, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.5 | 2e-04 | 3/18 (J82, RPMI-7951, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +4.5 | 2e-04 | 17/18 (AsPC-1, SW480, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +4.5 | 2e-04 | 15/18 (J82, LS 180, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.31×** | +4.5 | 3e-04 | 0/19 | rises with dose | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.30×** | +4.2 | 9e-04 | 0/19 | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.44×** | +4.1 | 0.001 | 0/18 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4843.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.636×** | -7.4 | 5e-11 | 18/18 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.699×** | -5.9 | 1e-06 | 17/18 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.737×** | -5.0 | 9e-05 | 16/18 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -4.6 | 7e-04 | 0/20 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.792×** | -3.9 | 0.013 | 16/18 (KATO III, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.795×** | -3.8 | 0.015 | 2/18 (NCI-H1792, NCI-H460) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.801×** | -3.6 | 0.021 | 4/18 (NCI-H1792, SHP-77, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **0.668×** | -3.5 | 0.036 | 13/19 (HT-29, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.803×** | -3.3 | 0.052 | 0/18 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.826×** | -3.2 | 0.090 | 8/18 (KATO III, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.827×** | -3.1 | 0.090 | 6/18 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4843. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 253 | 7 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +18.2) | [[Panobinostat (drug)]] 0.5 µM 0.184× (z -17.5) |
| [[KATO III (line)]] | alt | 200 | 4 | 8 (5 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.17× (z +15.6) | [[Panobinostat (drug)]] 0.5 µM 0.144× (z -21.3) |
| [[MIA PaCa-2 (line)]] | alt | 498 | 1 | 10 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.171× (z -16.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.223× (z -13.8) |
| [[A498 (line)]] | wt | 191 | 6 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -11.0) |
| [[LoVo (line)]] | wt | 125 | 5 (1 ⚠) | 5 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.95× (z +13.2) | [[Panobinostat (drug)]] 5 µM 0.229× (z -15.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.230× (z -14.9) |
| [[NCI-H460 (line)]] | wt | 399 | 2 | 6 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.80× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -21.9) |
| [[HT-29 (line)]] | alt | 335 | 0 | 7 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.128× (z -20.4) |
| [[LS 180 (line)]] | wt | 119 | 3 | 4 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.73× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.193× (z -16.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.223× (z -15.1) |
| [[SHP-77 (line)]] | alt | 235 | 3 | 4 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.64× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.192× (z -16.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.211× (z -15.2) |
| [[J82 (line)]] | alt | 50.3 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +15.6) | — |
| [[NCI-H1792 (line)]] | alt | 397 | 3 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.69× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.48× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -16.3) |
| [[A-427 (line)]] | wt | 81.9 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.51× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.301× (z -10.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.308× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 198 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -11.4) |
| [[SW480 (line)]] | alt | 59.0 | 2 | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.01× (z +9.7) | [[Belinostat (drug)]] 5 µM 0.209× (z -13.7) |
| [[AsPC-1 (line)]] | alt | 83.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +16.6) | [[Panobinostat (drug)]] 5 µM 0.292× (z -9.3) ⚠ cell-cycle shift, explains ~39% of this change |
| [[LOX-IMVI (line)]] | wt | 68.0 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.230× (z -12.0) |
| [[SW 900 (line)]] | alt | 181 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -12.1) |
| [[A549 (line)]] | wt | 13.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 20.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 15.8 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.5 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 12.5 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.6 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.8 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 17.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.7 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.9 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 9.50 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.5 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 22.0 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 13.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4843), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALOX12P2-1]] | +0.68 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[LRP1B]] | +0.68 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[CLIC2]] | +0.67 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[CAPS2]] | +0.67 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[BBOX1-AS1]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[AKR1C3]] | +0.63 | +0.55 / +0.55 | both halves | 1e-05 | pathway: Sensory Perception |
| [[LINC02428]] | +0.63 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ZSCAN31]] | +0.62 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[PSMA4]] | +0.62 | +0.65 / +0.45 | both halves | 3e-05 | pathway: Beta-catenin independent WNT signaling |
| [[IGSF1]] | +0.62 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[BHMT2]] | +0.61 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[JAKMIP3]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND19]] | -0.62 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[ODF2]] | -0.61 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[FBH1]] | -0.59 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[SOCS7]] | -0.58 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[PIGF]] | -0.57 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[SMARCD2]] | -0.56 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[ANKRD13D]] | -0.56 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ERI1]] | -0.56 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[RECQL]] | -0.55 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[TMEM104]] | -0.55 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[SFXN2]] | -0.55 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[DPY19L3]] | -0.55 | -0.59 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A5]] | B | SLC44A5 activity raises GNGT1's level | lines that do not express SLC44A5 (17) vs lines expressing it (33) | 2.01× lower at baseline in the lines without SLC44A5 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000289609; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises GNGT1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MIR4307HG]] | C | MIR4307HG activity raises GNGT1's level | lines that do not express MIR4307HG (35) vs lines expressing it (15) | 3.88× lower at baseline in the lines without MIR4307HG | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000258081, MAGEB2, LINC02438; co-absent with the target |
| [[IGSF1]] | C | IGSF1 activity raises GNGT1's level | lines that do not express IGSF1 (33) vs lines expressing it (17) | 2.98× lower at baseline in the lines without IGSF1 | 0.024 | ⚠ within organs, on part of the lines; also absent: LINC01885, ZNF208, ENSG00000233358; co-absent with the target |
| [[LINC01611]] | C | LINC01611 activity raises GNGT1's level | lines that do not express LINC01611 (34) vs lines expressing it (16) | 3.08× lower at baseline in the lines without LINC01611 | 0.032 | ⚠ within organs, on part of the lines; also absent: CDH13, ENSG00000248973, LINC02377; co-absent with the target |
| [[GLDN]] | C | GLDN activity raises GNGT1's level | lines that do not express GLDN (25) vs lines expressing it (25) | 2.55× lower at baseline in the lines without GLDN | 0.064 | ⚠ within organs, on part of the lines; also absent: MIR4713HG, MT1G, ENSG00000255595; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 9, C 4. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BANK1]] | B | GNGT1 activity raises BANK1's level | lines that do not express GNGT1 (30) vs lines expressing it (20) | 1.99× lower at baseline in the lines without GNGT1 | 0.013 | ⚠ within organs, on part of the lines; also absent: SLC25A24P1, REG4, CACNA2D3 |
| [[SLC44A5]] | B | GNGT1 activity raises SLC44A5's level | lines that do not express GNGT1 (30) vs lines expressing it (20) | 1.89× lower at baseline in the lines without GNGT1 | 0.028 | ⚠ within organs, on part of the lines; also absent: SLC25A24P1, REG4, CACNA2D3 |
| [[LINC02542]] | B | GNGT1 activity raises LINC02542's level | lines that do not express GNGT1 (30) vs lines expressing it (20) | 1.62× lower at baseline in the lines without GNGT1 | 0.031 | ⚠ within organs, on part of the lines; also absent: SLC25A24P1, REG4, CACNA2D3 |
| [[RIPK2-DT]] | B | GNGT1 activity lowers RIPK2-DT's level | lines that do not express GNGT1 (30) vs lines expressing it (20) | 1.33× higher at baseline in the lines without GNGT1 | 0.038 | ⚠ within organs, on part of the lines; also absent: SLC25A24P1, REG4, CACNA2D3 |
| [[DIP2C-AS1]] | B | GNGT1 activity raises DIP2C-AS1's level | lines that do not express GNGT1 (30) vs lines expressing it (20) | 1.43× lower at baseline in the lines without GNGT1 | 0.045 | ⚠ within organs, on part of the lines; also absent: SLC25A24P1, REG4, CACNA2D3 |
| [[LINC00355]] | B | GNGT1 activity raises LINC00355's level | lines that do not express GNGT1 (30) vs lines expressing it (20) | 1.72× lower at baseline in the lines without GNGT1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SLC25A24P1, REG4, CACNA2D3 |
| [[DGCR2]] | B | GNGT1 activity strengthens DGCR2's drug response | lines that do not express GNGT1 (30) vs lines expressing it (19) | the lines without GNGT1 respond 0.88× as strongly (z diff +0.14); strongest at Belinostat 5 µM: 1.37x vs 1.68x (z diff +1.8) | 0.075 | ⚠ within organs, on part of the lines; also absent: SLC25A24P1, REG4, CACNA2D3; target measured in part of the lines; artifact flags |
| [[CASC9]] | B | GNGT1 activity raises CASC9's level | lines that do not express GNGT1 (30) vs lines expressing it (20) | 2.16× lower at baseline in the lines without GNGT1 | 0.079 | ⚠ within organs, on part of the lines; also absent: SLC25A24P1, REG4, CACNA2D3 |
| [[NRG4]] | B | GNGT1 activity raises NRG4's level | lines that do not express GNGT1 (30) vs lines expressing it (20) | 1.64× lower at baseline in the lines without GNGT1 | 0.099 | ⚠ within organs, on part of the lines; also absent: SLC25A24P1, REG4, CACNA2D3 |
| [[IGSF1]] | C | GNGT1 activity raises IGSF1's level | lines that do not express GNGT1 (30) vs lines expressing it (20) | 3.08× lower at baseline in the lines without GNGT1 | 0.008 | ⚠ within organs, on part of the lines; also absent: SLC25A24P1, REG4, CACNA2D3; co-absent with the target |
| [[GLDN]] | C | GNGT1 activity raises GLDN's level | lines that do not express GNGT1 (30) vs lines expressing it (20) | 2.35× lower at baseline in the lines without GNGT1 | 0.027 | ⚠ within organs, on part of the lines; also absent: SLC25A24P1, REG4, CACNA2D3; co-absent with the target |
| [[RASSF6]] | C | GNGT1 activity raises RASSF6's level | lines that do not express GNGT1 (30) vs lines expressing it (20) | 2.33× lower at baseline in the lines without GNGT1 | 0.034 | ⚠ within organs, on part of the lines; also absent: SLC25A24P1, REG4, CACNA2D3; co-absent with the target |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.686). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-6.4, 48.1); signed map (50.4, -8.2). **Vector** length 83.9, 25.6% of its response variance represented; |z| ≥ 3 in 724 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Synthesis of bile acids and bile salts via 27-hydroxycholesterol* (reactome, mean cos +0.51 to 3); *Synthesis of bile acids and bile salts via 24-hydroxycholesterol* (reactome, mean cos +0.51 to 3); *Synthesis of bile acids and bile salts via 7alpha-hydroxycholesterol* (reactome, mean cos +0.51 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.3 | +14.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.0 | +9.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.9 | +8.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.7 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +16.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +4.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.6 | -7.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.5 | -5.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -3.3 | -3.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.7 | -3.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.5 | -0.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -3.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.2 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.9 | -1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit gamma transducin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.3 — chr7:93,591,573-93,911,265 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GNG1 |
| Gene groups (HGNC) | G protein subunits gamma |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 70 pathways, smallest: Activation of the phototransduction cascade; G beta:gamma signalling through BTK; Prostacyclin signalling through prostacyclin receptor |
| Matched by | ensembl_id |

**Function**, from UniProt [P63211](https://www.uniprot.org/uniprotkb/P63211) (Guanine nucleotide-binding protein G(T) subunit gamma-T1):

> Gamma subunit of the heterotrimeric guanine nucleotide-binding protein (G proteins) that forms complexes with alpha and gamma subunits and participates in signal transduction downstream of G protein-coupled receptors (GPCRs) (By similarity). The beta-gamma dimer stabilizes the GDP-bound inactive alpha subunit by limiting spontaneous GDP dissociation. Upon GPCR activation, facilitates receptor-catalyzed GDP release and GTP binding on the alpha subunit (By similarity). Following GPCR activation, …

**Summary**, from NCBI Gene [2792](https://www.ncbi.nlm.nih.gov/gene/2792):

> This gene encodes the gamma subunit of transducin, a guanine nucleotide-binding protein (G protein) that is found in rod outer segments. Transducin, also known as GMPase, mediates the activation of a cyclic GTP-specific (guanosine monophosphate) phosphodiesterase by rhodopsin. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:4411](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4411) · Entrez [2792](https://www.ncbi.nlm.nih.gov/gene/2792) · UniProt [P63211](https://www.uniprot.org/uniprotkb/P63211) · Ensembl [ENSG00000127928](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127928)

## Data

Gene col 4843: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4843); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4843, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4843]; `tensor/DDL_lfc|DDL_z.npy` [4843]; `embed/gene_vectors.npy` [4843]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4843 or target_col == 4843). Every well: [[GNGT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNGT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
