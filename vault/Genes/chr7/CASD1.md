---
symbol: "CASD1"
type: "gene"
col: 4855
ensembl_id: "ENSG00000127995"
name: "CAS1 domain sialic acid O acetyltransferase 1"
location: "7q21.3"
module: 46
arm: "+"
pooled_cpm: 42.55
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 30
n_dd_up_clean: 6
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# CASD1

*CAS1 domain sialic acid O acetyltransferase 1* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM: 1.46× (z +5.7, q 6e-06, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.189× (z -25.3, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DECR1]] (+0.72, fdr 1e-05), [[HFE]] (+0.69, fdr 2e-05), [[EFCAB2]] (+0.68, fdr 7e-05); moves opposite to [[CARMIL2]] (-0.68, fdr 1e-05), [[KIF21B]] (-0.66, fdr 5e-05), [[ANKRD27]] (-0.66, fdr 5e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4855.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +5.7 | 6e-06 | 35/47 (SNU-423, C32, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +5.3 | 3e-05 | 27/47 (LS 180, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +5.2 | 3e-05 | 31/47 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.029 | 19/46 (AsPC-1, A549, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.090 | 15/47 (HOP62, NCI-H1573, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.090 | 17/47 (SW1417, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.18× | +3.2 | 0.11 | 16/47 (HOP62, NCI-H2030, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.2 | 0.11 | 15/47 (A498, Panc 03.27, …) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.23× | +3.1 | 0.13 | 12/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4855.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.189×** | -25.3 | 0e+00 | 47/47 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.198×** | -24.6 | 0e+00 | 47/47 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.207×** | -23.9 | 0e+00 | 47/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.382×** | -14.6 | 0e+00 | 46/47 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.419×** | -13.2 | 1e-37 | 45/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.612×** | -7.5 | 8e-12 | 36/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.652×** | -6.5 | 7e-09 | 33/47 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.637×** | -6.5 | 7e-09 | 38/47 (C32, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.645×** | -6.4 | 9e-09 | 30/46 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.681×** | -5.8 | 3e-07 | 25/46 (C32, SNU-1, …) | all doses, flat | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.488×** | -5.7 | 6e-07 | 34/47 (NCI-H1792, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.685×** | -5.5 | 1e-06 | 29/45 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.736×** | -4.7 | 1e-04 | 28/47 (SW 900, C32, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.728×** | -4.6 | 1e-04 | 27/47 (RKO, NCI-H1792, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.773×** | -4.6 | 2e-04 | 28/47 (SW480, C32, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | **0.742×** | -4.5 | 2e-04 | 32/47 (A-172, SW 1271, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.568×** | -4.5 | 2e-04 | 26/48 (MIA PaCa-2, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.748×** | -4.4 | 3e-04 | 26/47 (HT-29, SW 1088, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4855. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.9 | 0 | 10 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.147× (z -18.3) |
| [[NCI-H1792 (line)]] | alt | 64.1 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -21.2) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.111× (z -18.0) |
| [[C32 (line)]] | wt | 148 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -14.5) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.195× (z -13.8) |
| [[RKO (line)]] | wt | 59.6 | 0 | 8 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.128× (z -17.7) |
| [[MIA PaCa-2 (line)]] | alt | 53.4 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.109× (z -18.8) |
| [[AN3 CA (line)]] | alt | 84.5 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0950× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.118× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 49.9 | 0 | 6 | — | [[Belinostat (drug)]] 5 µM 0.108× (z -17.1) |
| [[SW480 (line)]] | alt | 51.3 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.116× (z -24.7) |
| [[HepG2_C3A (line)]] | wt | 64.1 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.118× (z -15.8) |
| [[LS 180 (line)]] | wt | 45.9 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -18.9) |
| [[SNU-1 (line)]] | wt | 110 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.242× (z -12.1) |
| [[SW 900 (line)]] | alt | 53.3 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.179× (z -13.6) |
| [[SW1417 (line)]] | alt | 50.5 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.142× (z -19.0) |
| [[A498 (line)]] | wt | 37.8 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -14.1) |
| [[CFPAC-1 (line)]] | alt | 37.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -11.9) |
| [[H4 (line)]] | wt | 42.4 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0589× (z -18.4) |
| [[HEC-1-A (line)]] | alt | 64.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.216× (z -17.2) |
| [[J82 (line)]] | alt | 30.6 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.171× (z -13.5) |
| [[LoVo (line)]] | wt | 35.0 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.153× (z -17.1) |
| [[LOX-IMVI (line)]] | wt | 31.6 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.149× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 44.9 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.191× (z -15.7) |
| [[NCI-H2030 (line)]] | alt | 51.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.235× (z -12.5) |
| [[PANC-1 (line)]] | alt | 25.2 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.204× (z -14.4) |
| [[RPMI-7951 (line)]] | alt | 34.7 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.180× (z -11.0) |
| [[SHP-77 (line)]] | alt | 44.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -13.2) |
| [[SNU-423 (line)]] | alt | 31.0 | 0 | 4 | — | [[Belinostat (drug)]] 0.5 µM 0.116× (z -15.8) |
| [[A-172 (line)]] | wt | 27.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -11.2) |
| [[A549 (line)]] | wt | 48.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -16.1) |
| [[AsPC-1 (line)]] | alt | 34.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.186× (z -13.2) |
| [[C-33 A (line)]] | alt | 60.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.189× (z -11.9) |
| [[COLO 205 (line)]] | alt | 25.5 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.163× (z -10.1) |
| [[HOP62 (line)]] | alt | 37.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -15.6) |
| [[Hs 766T (line)]] | wt | 18.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.189× (z -10.2) |
| [[HS-578T (line)]] | alt | 33.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.100× (z -15.9) |
| [[HT-29 (line)]] | alt | 28.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -12.9) |
| [[NCI-H2347 (line)]] | alt | 51.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -15.5) |
| [[Panc 03.27 (line)]] | alt | 20.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 34.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -11.7) |
| [[SW48 (line)]] | wt | 43.6 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0399× (z -20.4) |
| [[HCT15 (line)]] | alt | 47.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.177× (z -11.6) |
| [[BT-474 (line)]] | alt | 47.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.301× (z -9.1) |
| [[SW 1271 (line)]] | alt | 38.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0521× (z -8.5) |
| [[A-427 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 66.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4855), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DECR1]] | +0.72 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[HFE]] | +0.69 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[EFCAB2]] | +0.68 | +0.52 / +0.38 | both halves | 7e-05 |  |
| [[ZNF532]] | +0.67 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[NFYC]] | +0.67 | +0.58 / +0.32 | both halves | 2e-04 |  |
| [[UNK]] | +0.66 | +0.57 / +0.35 | both halves | 1e-04 |  |
| [[TRAF3IP2-AS1]] | +0.66 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[TMEM35B]] | +0.65 | +0.50 / +0.36 | both halves | 1e-04 |  |
| [[CFAP418]] | +0.65 | +0.54 / +0.32 | both halves | 2e-04 |  |
| [[ACOT2]] | +0.65 | +0.58 / +0.38 | both halves | 6e-05 |  |
| [[FBXW4]] | +0.65 | +0.60 / +0.36 | both halves | 1e-04 |  |
| [[CRPPA]] | +0.65 | +0.47 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CARMIL2]] | -0.68 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[KIF21B]] | -0.66 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[ANKRD27]] | -0.66 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[RBAK-RBAKDN]] | -0.65 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ST6GALNAC6]] | -0.65 | -0.52 / -0.44 | both halves | 3e-05 | STRING 423 |
| [[LPCAT1]] | -0.63 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[SPTLC2]] | -0.63 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[ST6GALNAC6-1]] | -0.63 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[TNK2]] | -0.60 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[GNAI3]] | -0.60 | -0.47 / -0.26 | both halves | 3e-04 |  |
| [[TMEM184B]] | -0.60 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[KCTD21]] | -0.60 | -0.38 / -0.49 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CASD1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.706). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (0.0, 11.5); signed map (25.2, -21.5). **Vector** length 98.6, 26.7% of its response variance represented; |z| ≥ 3 in 1,142 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.1 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | -0.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | +0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +5.0 | +5.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +1.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.4 | +0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +0.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +3.7 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -7.3 | -14.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.3 | -13.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.8 | -24.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.3 | -25.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.1 | -23.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.0 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.4 | -4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -7.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.0 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | CAS1 domain sialic acid O acetyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.3 — chr7:94,509,219-94,557,019 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21213, FLJ21879, C7orf12, Cas1 |
| Gene groups (HGNC) | Acyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PB1](https://www.uniprot.org/uniprotkb/Q96PB1) (N-acetylneuraminate):

> Key enzyme in the biosynthesis of O-acetylated (O-Ac) sialoglycans such as gangliosides O-AcGD3 and O-AcGD2, which affect various processes such as cell-cell interactions, host-pathogen recognition. Catalyzes the transfer of an acetyl group from a donor, the acetyl-coenzyme-A molecule (acetyl-CoA), to the C7/8/9 OH-position of a sialic acid residue. The primary site of O-acetyl group transfer on sialic acid seems to depend on cell type and can be C7, from which the O-acetyl group could …

**Summary**, from NCBI Gene [64921](https://www.ncbi.nlm.nih.gov/gene/64921):

> Enables N-acetylneuraminate 9-O-acetyltransferase activity. Involved in carbohydrate metabolic process. Located in Golgi membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16014](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16014) · Entrez [64921](https://www.ncbi.nlm.nih.gov/gene/64921) · UniProt [Q96PB1](https://www.uniprot.org/uniprotkb/Q96PB1) · Ensembl [ENSG00000127995](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127995)

## Data

Gene col 4855: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4855); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4855, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4855]; `tensor/DDL_lfc|DDL_z.npy` [4855]; `embed/gene_vectors.npy` [4855]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4855 or target_col == 4855). Every well: [[CASD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
