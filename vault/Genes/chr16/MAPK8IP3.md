---
symbol: "MAPK8IP3"
type: "gene"
col: 6250
ensembl_id: "ENSG00000138834"
name: "mitogen-activated protein kinase 8 interacting protein 3"
location: "16p13.3"
module: 3
arm: "+"
pooled_cpm: 64.59
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# MAPK8IP3

*mitogen-activated protein kinase 8 interacting protein 3* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.83× (z +12.1, q 7e-31, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.656× (z -7.8, q 4e-12, down in 31 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.820× (z -5.6, q 3e-06, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIGA2]] (+0.61, fdr 3e-05), [[ATG4B]] (+0.60, fdr 2e-05), [[GNAI2]] (+0.59, fdr 2e-05); moves opposite to [[PHACTR2]] (-0.54, fdr 3e-05), [[SETMAR]] (-0.54, fdr 7e-05), [[PPP2CA]] (-0.53, fdr 6e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HS6ST2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6250.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.83×** | +12.1 | 7e-31 | 42/48 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.68×** | +10.4 | 1e-22 | 39/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +9.3 | 3e-18 | 40/48 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +9.2 | 4e-18 | 26/48 (HepG2/C3A, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.90×** | +6.7 | 2e-09 | 31/48 (PANC-1, MIA PaCa-2, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.59×** | +4.8 | 1e-04 | 23/49 (SW480, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +4.1 | 0.004 | 21/48 (A-172, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.008 | 22/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.6 | 0.023 | 20/48 (PANC-1, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.041 | 21/48 (A498, A-172, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.052 | 18/48 (SW48, SHP-77, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.069 | 19/47 (SW480, LoVo, …) | inconsistent across doses |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.098 | 13/49 (J82, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6250.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.656×** | -7.8 | 4e-12 | 31/45 (Panc 03.27, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.683×** | -7.3 | 7e-11 | 25/42 (SHP-77, KATO III, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.713×** | -6.7 | 3e-09 | 27/49 (A549, A-172, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.705×** | -6.7 | 3e-09 | 26/47 (AsPC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.820×** | -5.6 | 3e-06 | 25/48 (Panc 03.27, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.778×** | -4.9 | 8e-05 | 23/48 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.867× | -4.0 | 0.005 | 17/48 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.812×** | -4.0 | 0.005 | 19/49 (A-172, RPMI-7951, …) | top dose only | position effect removed |
| [[Berbamine (drug)]] 0.05 µM |  | **0.826×** | -3.8 | 0.009 | 18/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.827×** | -3.8 | 0.009 | 20/49 (HOP62, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.714×** | -3.5 | 0.022 | 20/48 (PANC-1, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.719×** | -3.4 | 0.028 | 15/48 (PANC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 0.846× | -3.3 | 0.037 | 15/48 (HOP62, H4, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.889× | -3.3 | 0.037 | 10/48 (CFPAC-1, SHP-77, …) | top dose only | position effect removed |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.848× | -3.3 | 0.038 | 11/49 (HOP62, LS 180, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.743×** | -3.1 | 0.059 | 13/48 (CFPAC-1, AsPC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6250. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 105 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.301× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.555× (z -9.4) |
| [[A-427 (line)]] | wt | 42.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 87.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.194× (z -13.8) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[LoVo (line)]] | wt | 41.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.63× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 38.6 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.91× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 49.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0631× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.475× (z -9.4) |
| [[PANC-1 (line)]] | alt | 86.6 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.354× (z -13.0) ⚠ unreliable plate only · without an alert: [[Selinexor (drug)]] 5 µM 0.609× (z -8.9) |
| [[A549 (line)]] | wt | 76.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H1792 (line)]] | alt | 74.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 36.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.6) | — |
| [[RKO (line)]] | wt | 59.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -13.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 54.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.161× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[AsPC-1 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.373× (z -10.1) ⚠ toxic |
| [[C-33 A (line)]] | alt | 67.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -16.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 55.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.401× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[CFPAC-1 (line)]] | alt | 78.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.344× (z -9.6) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 78.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 97.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.376× (z -9.4) ⚠ toxic |
| [[KATO III (line)]] | alt | 49.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 61.8 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.478× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 39.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.449× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 71.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -9.5) ⚠ cell-cycle shift, explains ~49% of this change |
| [[SW480 (line)]] | alt | 70.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +8.6) | — |
| [[A498 (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 102 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 68.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 71.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 81.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 57.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6250), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIGA2]] | +0.61 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[ATG4B]] | +0.60 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[GNAI2]] | +0.59 | +0.49 / +0.46 | both halves | 2e-05 | same gene group |
| [[SH3GL1]] | +0.58 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[ACAP3]] | +0.57 | +0.37 / +0.49 | both halves | 8e-05 | same gene group |
| [[TSC2]] | +0.57 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[RAB40C]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[ZER1]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[PPP1R13L]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[MRNIP]] | +0.56 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[PIP5K1C]] | +0.55 | +0.49 / +0.38 | both halves | 6e-05 |  |
| [[BAIAP3]] | +0.55 | +0.52 / +0.29 | both halves | 3e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHACTR2]] | -0.54 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[SETMAR]] | -0.54 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[PPP2CA]] | -0.53 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[TRMT11]] | -0.53 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[HDDC2]] | -0.53 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[STEAP2]] | -0.51 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[SLC35G1]] | -0.51 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[OGFRL1]] | -0.51 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[EPM2A]] | -0.50 | -0.48 / -0.21 | both halves | 6e-04 |  |
| [[RNASEH2B]] | -0.50 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[B3GALNT1]] | -0.50 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[RWDD2B]] | -0.50 | -0.40 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HS6ST2]] | B | HS6ST2 activity lowers MAPK8IP3's level | lines that do not express HS6ST2 (28) vs lines expressing it (22) | 1.23× higher at baseline in the lines without HS6ST2 | 0.012 | ⚠ within organs, on part of the lines; also absent: VIPR2, CACNB2, ENSG00000257883 |
| [[AFAP1-AS1]] | B | AFAP1-AS1 activity raises MAPK8IP3's level | lines that do not express AFAP1-AS1 (33) vs lines expressing it (17) | 1.17× lower at baseline in the lines without AFAP1-AS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: AGR2, GABRP, LINC01610 |
| [[HDAC6]] | B | HDAC6 activity lowers MAPK8IP3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.505). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (4.9, -0.6); signed map (-29.0, 13.8). **Vector** length 104, 26.1% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.8 | +10.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +12.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.5 | +2.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.4 | +9.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.4 | +4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +6.7 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +2.4 | +2.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.3 | +1.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.1 | +2.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.3 | -5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.9 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -4.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.5 | -4.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.1 | -6.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.2 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.0 | -3.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.7 | -2.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.5 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase 8 interacting protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,706,166-1,770,351 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1066, JSAP1, JIP3, syd |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPT6](https://www.uniprot.org/uniprotkb/Q9UPT6) (C-Jun-amino-terminal kinase-interacting protein 3):

> The JNK-interacting protein (JIP) group of scaffold proteins selectively mediates JNK signaling by aggregating specific components of the MAPK cascade to form a functional JNK signaling module. May function as a regulator of vesicle transport, through interactions with the JNK-signaling components and motor proteins (By similarity). Promotes neuronal axon elongation in a kinesin- and JNK-dependent manner. Activates cofilin at axon tips via local activation of JNK, thereby regulating filopodial …

**Summary**, from NCBI Gene [23162](https://www.ncbi.nlm.nih.gov/gene/23162):

> The protein encoded by this gene shares similarity with the product of Drosophila syd gene, required for the functional interaction of kinesin I with axonal cargo. Studies of the similar gene in mouse suggested that this protein may interact with, and regulate the activity of numerous protein kinases of the JNK signaling pathway, and thus function as a scaffold protein in neuronal cells. The C. elegans counterpart of this gene is found to regulate synaptic vesicle transport possibly by …

**Accessions** — [HGNC:6884](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6884) · Entrez [23162](https://www.ncbi.nlm.nih.gov/gene/23162) · UniProt [Q9UPT6](https://www.uniprot.org/uniprotkb/Q9UPT6) · Ensembl [ENSG00000138834](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138834)

## Data

Gene col 6250: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6250); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6250, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6250]; `tensor/DDL_lfc|DDL_z.npy` [6250]; `embed/gene_vectors.npy` [6250]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6250 or target_col == 6250). Every well: [[MAPK8IP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPK8IP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
