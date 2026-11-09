---
symbol: "KPNA1"
type: "gene"
col: 3519
ensembl_id: "ENSG00000114030"
name: "karyopherin subunit alpha 1"
location: "3q21.1"
module: 4
arm: "+"
pooled_cpm: 129.37
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 6
n_dd_up_clean: 18
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# KPNA1

*karyopherin subunit alpha 1* — 3q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.84× (z +15.4, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.785× (z -6.1, q 5e-07, down in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~23% of this change. The strongest without an alert is [[Filgotinib (drug)]] 0.05 µM: 0.808× (z -3.8, q 0.029, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP4R1]] (+0.70, fdr 1e-05), [[AGFG1]] (+0.70, fdr 7e-06), [[EIF4E]] (+0.63, fdr 7e-06); moves opposite to [[TXNL4B]] (-0.61, fdr 1e-05), [[SPTY2D1]] (-0.58, fdr 1e-05), [[INTS6L]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3519.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.84×** | +15.4 | 0e+00 | 44/48 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.29×** | +14.8 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +14.1 | 1e-42 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.45×** | +14.0 | 4e-42 | 48/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.14×** | +13.1 | 6e-37 | 45/47 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.74×** | +12.3 | 5e-33 | 47/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.98×** | +12.2 | 2e-32 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.80×** | +10.5 | 4e-24 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.84×** | +10.5 | 4e-24 | 44/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.71×** | +9.6 | 7e-20 | 45/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.62×** | +8.7 | 2e-16 | 43/48 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +7.6 | 2e-12 | 39/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +6.9 | 3e-10 | 32/48 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.46×** | +6.8 | 4e-10 | 37/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.45×** | +6.6 | 1e-09 | 36/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +6.0 | 9e-08 | 34/48 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +4.4 | 3e-04 | 27/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3519.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.785×** | -6.1 | 5e-07 | 33/48 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.808×** | -3.8 | 0.029 | 22/48 (RPMI-7951, J82, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | **0.809×** | -3.8 | 0.029 | 19/48 (RPMI-7951, NCI-H1792, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.825×** | -3.4 | 0.081 | 21/49 (HOP62, H4, …) | all doses, stronger at high dose |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.827×** | -3.4 | 0.081 | 20/48 (RPMI-7951, C32, …) | inconsistent across doses |  |
| [[Simotinib (drug)]] 0.05 µM |  | **0.813×** | -3.3 | 0.093 | 22/48 (COLO 205, RKO, …) | inconsistent across doses |  |
| [[Ranolazine (drug)]] 0.05 µM |  | 0.838× | -3.2 | 0.12 | 18/48 (LS 180, SW 1271, …) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | 0.839× | -3.1 | 0.13 | 15/48 (AsPC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.841× | -3.1 | 0.13 | 22/48 (BT-474, HOP62, …) | all doses, stronger at high dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.845× | -3.0 | 0.14 | 20/48 (NCI-H1792, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3519. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 111 | 12 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +14.3) | — |
| [[PANC-1 (line)]] | alt | 132 | 12 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +17.3) | — |
| [[SW480 (line)]] | alt | 114 | 11 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +18.5) | — |
| [[HOP62 (line)]] | alt | 110 | 8 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.86× (z +11.9) | — |
| [[LoVo (line)]] | wt | 118 | 8 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.71× (z +13.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.81× (z +12.1) | — |
| [[NCI-H23 (line)]] | alt | 185 | 7 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 173 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.72× (z +11.9) | — |
| [[NCI-H1792 (line)]] | alt | 87.2 | 7 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.45× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 3.64× (z +11.8) | — |
| [[COLO 205 (line)]] | alt | 89.4 | 6 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.85× (z +12.3) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 13.3× (z +11.0) | — |
| [[H4 (line)]] | wt | 102 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.97× (z +10.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 123 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 101 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 114 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.01× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +12.0) | — |
| [[SW 900 (line)]] | alt | 104 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.18× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +11.2) | — |
| [[AsPC-1 (line)]] | alt | 81.7 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.4) | [[Selinexor (drug)]] 5 µM 0.515× (z -8.8) ⚠ cell-cycle shift, explains ~23% of this change |
| [[SK-MEL-2 (line)]] | alt | 156 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.26× (z +9.6) | — |
| [[A-427 (line)]] | wt | 204 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.19× (z +12.8) | — |
| [[A549 (line)]] | wt | 126 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +16.8) | — |
| [[HEC-1-A (line)]] | alt | 162 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.1) | — |
| [[J82 (line)]] | alt | 188 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.20× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 110 | 3 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.85× (z +9.6) | — |
| [[A-172 (line)]] | wt | 107 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.14× (z +8.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.67× (z +8.6) | — |
| [[A498 (line)]] | wt | 148 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +14.7) | — |
| [[C-33 A (line)]] | alt | 125 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 78.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +14.7) | — |
| [[HT-29 (line)]] | alt | 125 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.07× (z +10.4) | — |
| [[KATO III (line)]] | alt | 96.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.8) | — |
| [[NCI-H2347 (line)]] | alt | 160 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 210 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.40× (z +10.4) | — |
| [[RKO (line)]] | wt | 184 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.61× (z +10.4) | — |
| [[RPMI-7951 (line)]] | alt | 147 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 146 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.14× (z +9.5) | — |
| [[SW 1088 (line)]] | alt | 88.8 | 0 | 2 | — | [[Tolmetin (drug)]] 5 µM 0.0854× (z -9.0) |
| [[SW48 (line)]] | wt | 148 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.30× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 140 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +8.9) | — |
| [[C32 (line)]] | wt | 117 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 8.58× (z +10.3) | — |
| [[HCT15 (line)]] | alt | 82.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 62.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 119 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 68.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +8.6) | — |
| [[SW 1271 (line)]] | alt | 171 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 202 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.06× (z +8.7) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 102 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 165 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 77.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 141 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3519), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP4R1]] | +0.70 | +0.56 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[AGFG1]] | +0.70 | +0.61 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[EIF4E]] | +0.63 | +0.71 / +0.64 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[AAGAB]] | +0.59 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[NDUFS6]] | +0.59 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[EXT2]] | +0.57 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[KAT6A]] | +0.57 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[SMAD2]] | +0.56 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[LRRFIP2]] | +0.56 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[VAPA]] | +0.55 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[KLHL2]] | +0.54 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[THAP12]] | +0.54 | +0.52 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNL4B]] | -0.61 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[SPTY2D1]] | -0.58 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[INTS6L]] | -0.58 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[NOSIP]] | -0.56 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[JMJD6]] | -0.56 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[GTF2B]] | -0.54 | -0.54 / -0.49 | both halves | 1e-05 | pathway: HIV Infection |
| [[FAM53C]] | -0.54 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[TOB2]] | -0.53 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[USP8]] | -0.53 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[POLR2A]] | -0.53 | -0.55 / -0.47 | both halves | 2e-05 | pathway: HIV Infection |
| [[ARF4]] | -0.52 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[BLZF1]] | -0.52 | -0.50 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.398). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-8.9, -29.3); signed map (-21.2, -53.3). **Vector** length 90.3, 32.9% of its response variance represented; |z| ≥ 3 in 1,339 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.6 | +0.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.5 | -1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.3 | -2.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.9 | +13.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.6 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.0 | +0.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.9 | +0.8 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | +2.6 | +2.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -6.3 | -6.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -5.1 | -3.1 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.3 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | +0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.7 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -0.4 |
|  | [[EX229 (drug)]] 0.05 µM |  | -2.9 | -0.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.8 | +0.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.7 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | karyopherin subunit alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.1 — chr3:122,421,902-122,514,945 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SRP1, RCH2, NPI-1, IPOA5 |
| Gene groups (HGNC) | Armadillo repeat containing; Importins |
| Reactome | 31 pathways, smallest: Integration of provirus; Suppression of phagosomal maturation; Apoptosis induced DNA fragmentation |
| Matched by | ensembl_id |

**Function**, from UniProt [P52294](https://www.uniprot.org/uniprotkb/P52294) (Importin subunit alpha-5):

> Functions in nuclear protein import as an adapter protein for nuclear receptor KPNB1. Binds specifically and directly to substrates containing either a simple or bipartite NLS motif. Docking of the importin/substrate complex to the nuclear pore complex (NPC) is mediated by KPNB1 through binding to nucleoporin FxFG repeats and the complex is subsequently translocated through the pore by an energy requiring, Ran-dependent mechanism. At the nucleoplasmic side of the NPC, Ran binds to importin-beta …

**Summary**, from NCBI Gene [3836](https://www.ncbi.nlm.nih.gov/gene/3836):

> The transport of molecules between the nucleus and the cytoplasm in eukaryotic cells is mediated by the nuclear pore complex (NPC), which consists of 60-100 proteins. Small molecules (up to 70 kD) can pass through the nuclear pore by nonselective diffusion while larger molecules are transported by an active process. The protein encoded by this gene belongs to the importin alpha family, and is involved in nuclear protein import. This protein interacts with the recombination activating gene 1 …

**Accessions** — [HGNC:6394](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6394) · Entrez [3836](https://www.ncbi.nlm.nih.gov/gene/3836) · UniProt [P52294](https://www.uniprot.org/uniprotkb/P52294) · Ensembl [ENSG00000114030](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114030)

## Data

Gene col 3519: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3519); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3519, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3519]; `tensor/DDL_lfc|DDL_z.npy` [3519]; `embed/gene_vectors.npy` [3519]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3519 or target_col == 3519). Every well: [[KPNA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KPNA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
