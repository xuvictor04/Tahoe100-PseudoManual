---
symbol: "ANKRD16"
type: "gene"
col: 5564
ensembl_id: "ENSG00000134461"
name: "ankyrin repeat domain 16"
location: "10p15.1"
module: 15
arm: "+"
pooled_cpm: 13.64
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 15
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ANKRD16

*ankyrin repeat domain 16* — 10p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.08× (z +24.6, q 0e+00, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.409× (z -13.4, q 5e-38, down in 34 of 46 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC12A9]] (+0.64, fdr 2e-05), [[BCL7A]] (+0.63, fdr 3e-05), [[DEXI]] (+0.61, fdr 1e-04); moves opposite to [[ARAF]] (-0.57, fdr 2e-05), [[TFE3]] (-0.56, fdr 1e-04), [[GRIPAP1]] (-0.56, fdr 6e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FAM216A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5564.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.08×** | +24.6 | 0e+00 | 43/46 (LoVo, A549, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +12.7 | 2e-34 | 37/46 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.06×** | +11.1 | 1e-26 | 33/47 (CFPAC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.89×** | +9.8 | 1e-20 | 34/47 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +9.3 | 1e-18 | 31/46 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.74×** | +8.6 | 1e-15 | 36/47 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +7.3 | 2e-11 | 24/40 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.50×** | +6.2 | 3e-08 | 26/47 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +5.9 | 2e-07 | 20/47 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.45×** | +5.7 | 7e-07 | 22/47 (A549, NCI-H2030, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +5.3 | 5e-06 | 21/45 (A-172, SW1417, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.78×** | +4.7 | 1e-04 | 9/48 (CFPAC-1, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.007 | 4/47 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +3.8 | 0.007 | 9/48 (LOX-IMVI, J82, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.19× | +3.7 | 0.009 | 11/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.0 | 0.089 | 11/48 (A549, SW1417, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5564.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.409×** | -13.4 | 5e-38 | 34/46 (A-427, SNU-1, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.476×** | -11.5 | 3e-28 | 36/47 (RKO, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.576×** | -8.6 | 2e-15 | 30/46 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.596×** | -8.0 | 1e-13 | 28/46 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.695×** | -8.0 | 1e-13 | 26/47 (SK-MEL-2, C-33 A, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.664×** | -6.4 | 2e-08 | 23/47 (C32, A-427, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.690×** | -5.8 | 5e-07 | 21/47 (HEC-1-A, C-33 A, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.690×** | -5.8 | 5e-07 | 26/46 (SNU-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.692×** | -5.7 | 6e-07 | 18/46 (A-427, HT-29, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.686×** | -5.6 | 1e-06 | 23/42 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.744×** | -4.6 | 2e-04 | 15/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.764×** | -4.2 | 0.001 | 17/46 (A-427, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.788×** | -3.6 | 0.015 | 12/24 (J82, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.797×** | -3.6 | 0.015 | 20/39 (SNU-423, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Aprepitant (drug)]] 0.05 µM |  | **0.817×** | -3.2 | 0.059 | 5/47 (SW48, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5564. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 17.1 | 3 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +13.1) | [[Harringtonine (drug)]] 5 µM 0.252× (z -10.8) |
| [[LS 180 (line)]] | wt | 12.9 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -11.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 20.1 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +11.5) | [[Harringtonine (drug)]] 5 µM 0.123× (z -11.6) |
| [[SNU-1 (line)]] | wt | 38.9 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.112× (z -12.5) |
| [[A-427 (line)]] | wt | 16.6 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0605× (z -16.8) |
| [[PANC-1 (line)]] | alt | 10.5 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.229× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.270× (z -9.7) |
| [[SW480 (line)]] | alt | 16.5 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +8.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.340× (z -8.8) |
| [[A-172 (line)]] | wt | 24.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -9.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 11.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.79× (z +13.5) | — |
| [[C-33 A (line)]] | alt | 42.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -9.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.277× (z -8.6) |
| [[HOP62 (line)]] | alt | 14.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +11.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 26.8 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.261× (z -9.3) |
| [[A549 (line)]] | wt | 11.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.63× (z +14.0) | — |
| [[C32 (line)]] | wt | 8.70 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0586× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 8.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 21.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.124× (z -8.6) ⚠ toxic |
| [[HT-29 (line)]] | alt | 6.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.51× (z +11.2) | — |
| [[hTERT-HPNE (line)]] | wt | 11.2 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0904× (z -9.4) |
| [[J82 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -13.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 12.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +14.4) | — |
| [[LOX-IMVI (line)]] | wt | 11.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +10.4) | — |
| [[NCI-H1792 (line)]] | alt | 18.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 17.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +11.8) | — |
| [[RPMI-7951 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.128× (z -10.4) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -11.8) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SNU-423 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0418× (z -19.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 8.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.35× (z +9.8) | — |
| [[SW48 (line)]] | wt | 25.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.70 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5564), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC12A9]] | +0.64 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[BCL7A]] | +0.63 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[DEXI]] | +0.61 | +0.35 / +0.68 | both halves | 1e-04 |  |
| [[EIF4ENIF1]] | +0.61 | +0.39 / +0.68 | both halves | 5e-05 |  |
| [[MZT2A]] | +0.60 | +0.32 / +0.64 | both halves | 1e-04 |  |
| [[EEF2K]] | +0.60 | +0.41 / +0.69 | both halves | 4e-05 |  |
| [[RILPL1]] | +0.60 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[ZNF248]] | +0.58 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[PRRT3-AS1]] | +0.58 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[GATD1-DT]] | +0.58 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[POM121]] | +0.56 | +0.25 / +0.59 | both halves | 4e-04 |  |
| [[POM121C]] | +0.55 | +0.29 / +0.57 | both halves | 3e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARAF]] | -0.57 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[TFE3]] | -0.56 | -0.35 / -0.61 | both halves | 1e-04 |  |
| [[GRIPAP1]] | -0.56 | -0.22 / -0.64 | both halves | 6e-04 |  |
| [[BCL7B]] | -0.55 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[GMFB]] | -0.53 | -0.21 / -0.64 | both halves | 6e-04 |  |
| [[HUS1]] | -0.52 | -0.20 / -0.58 | ⚠ one half (not replicated) | 8e-04 |  |
| [[EFR3A]] | -0.50 | -0.28 / -0.56 | both halves | 3e-04 |  |
| [[CSRP1]] | -0.50 | -0.28 / -0.60 | both halves | 3e-04 |  |
| [[OCRL]] | -0.50 | -0.28 / -0.53 | both halves | 3e-04 |  |
| [[ZNF548]] | -0.49 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[AFF4]] | -0.49 | -0.33 / -0.60 | both halves | 1e-04 |  |
| [[MBD6]] | -0.49 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[CREB3]] | -0.48 | -0.35 / -0.51 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM216A]] | B | FAM216A activity raises ANKRD16's level | lines that do not express FAM216A (7) vs lines expressing it (43) | 1.77× lower at baseline in the lines without FAM216A | 0.036 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ANKRD16's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TMEM38A]] | C | TMEM38A's natural level weakens ANKRD16's drug response | TMEM38A's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.63, reverse -0.06; direction not clear | 0.079 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.511). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-10.1, -2.5); signed map (-40.6, 1.4). **Vector** length 78.2, 15.5% of its response variance represented; |z| ≥ 3 in 1,089 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +24.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +12.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +9.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | -2.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.4 | +1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[EX229 (drug)]] 5 µM |  | +1.7 | +0.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.5 | +5.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.5 | +0.4 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.0 | -3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.9 | -3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | +0.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.1 | -13.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -5.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.7 | -0.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.7 | -2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.1 — chr10:5,861,616-5,889,906 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434N1511 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P6B7](https://www.uniprot.org/uniprotkb/Q6P6B7) (Ankyrin repeat domain-containing protein 16):

> Required to prevent the misactivation of serine (Ser) with tRNA(Ala) by promoting the hydrolysis of Ser-mischarged tRNA(Ala), thereby playing a role in translational fidelity. Binds directly to the catalytic domain of AARS/AlaRS and captures Ser that is misactivated by AARS/AlaRS, preventing the charging of Ser adenylates to tRNA(Ala) and precluding Ser misincorporation in nascent peptides.

**Summary**, from NCBI Gene [54522](https://www.ncbi.nlm.nih.gov/gene/54522):

> Predicted to be involved in tRNA modification. Predicted to be located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23471](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23471) · Entrez [54522](https://www.ncbi.nlm.nih.gov/gene/54522) · UniProt [Q6P6B7](https://www.uniprot.org/uniprotkb/Q6P6B7) · Ensembl [ENSG00000134461](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134461)

## Data

Gene col 5564: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5564); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5564, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5564]; `tensor/DDL_lfc|DDL_z.npy` [5564]; `embed/gene_vectors.npy` [5564]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5564 or target_col == 5564). Every well: [[ANKRD16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
