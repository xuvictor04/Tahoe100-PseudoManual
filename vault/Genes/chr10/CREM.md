---
symbol: "CREM"
type: "gene"
col: 1756
ensembl_id: "ENSG00000095794"
name: "cAMP responsive element modulator"
location: "10p11.21"
module: 57
arm: "-"
pooled_cpm: 53.76
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 8
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# CREM

*cAMP responsive element modulator* — 10p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.85× (z +14.5, q 1e-44, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.443× (z -10.0, q 9e-21, down in 34 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALS2]] (+0.67, fdr 1e-05), [[MAFG]] (+0.61, fdr 1e-05), [[MRPL45P2]] (+0.60, fdr 2e-05); moves opposite to [[CYB5A]] (-0.59, fdr 3e-05), [[ANXA11]] (-0.57, fdr 2e-05), [[ELP1]] (-0.56, fdr 3e-05).
> It sits in the **-** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC00944]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1756.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.85×** | +14.5 | 1e-44 | 34/47 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.84×** | +13.5 | 4e-39 | 33/48 (BT-474, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.74×** | +12.9 | 5e-36 | 36/48 (BT-474, HEC-1-A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +11.8 | 4e-30 | 40/48 (LoVo, A-427, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +11.6 | 3e-29 | 35/47 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +9.6 | 6e-20 | 32/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +9.0 | 1e-17 | 26/48 (CFPAC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +8.9 | 5e-17 | 28/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +8.5 | 1e-15 | 30/48 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +8.0 | 9e-14 | 34/48 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +7.5 | 4e-12 | 29/47 (HepG2/C3A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +7.0 | 1e-10 | 25/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +5.8 | 2e-07 | 27/47 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.28×** | +5.7 | 4e-07 | 22/48 (SNU-1, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +5.4 | 3e-06 | 24/47 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +4.9 | 4e-05 | 21/48 (HepG2/C3A, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.33×** | +4.8 | 5e-05 | 16/49 (SW480, LS 180, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1756.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.443×** | -10.0 | 9e-21 | 34/49 (A549, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.692×** | -8.3 | 3e-14 | 34/47 (NCI-H1573, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.734×** | -7.3 | 7e-11 | 28/48 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.755×** | -6.1 | 1e-07 | 23/44 (SHP-77, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.628×** | -5.7 | 1e-06 | 23/48 (A-427, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **0.795×** | -5.4 | 6e-06 | 22/47 (HT-29, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.800×** | -5.3 | 1e-05 | 23/48 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.823×** | -4.6 | 3e-04 | 19/48 (A-427, NCI-H460, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.837× | -4.2 | 0.002 | 14/47 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.842× | -4.0 | 0.003 | 14/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | 0.847× | -3.9 | 0.005 | 23/47 (BT-474, A-427, …) | all doses, flat | composition shift |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.850× | -3.8 | 0.007 | 18/47 (H4, A549, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.860× | -3.5 | 0.017 | 15/47 (C-33 A, RKO, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.902× | -3.4 | 0.025 | 10/48 (CHP-212, AN3 CA, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | 0.869× | -3.1 | 0.067 | 7/48 (HOP62, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1756. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 38.4 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.51× (z +11.1) | — |
| [[LoVo (line)]] | wt | 27.4 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.39× (z +21.8) | — |
| [[SW480 (line)]] | alt | 29.9 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +15.9) | [[Dinaciclib (drug)]] 0.05 µM 0.417× (z -9.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 124 | 1 | 4 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.49× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.321× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 53.9 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.96× (z +13.8) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 41.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.9) | — |
| [[NCI-H460 (line)]] | wt | 152 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.418× (z -9.9) |
| [[BT-474 (line)]] | alt | 57.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.94× (z +13.8) | — |
| [[KATO III (line)]] | alt | 38.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.90× (z +11.5) | — |
| [[SW48 (line)]] | wt | 45.3 | 0 | 3 (2 ⚠) | — | [[Torkinib (drug)]] 5 µM 0.0509× (z -10.2) ⚠ toxic · without an alert: [[Bendamustine (drug)]] 5 µM 0.214× (z -9.7) |
| [[C-33 A (line)]] | alt | 105 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.129× (z -9.2) |
| [[HOP62 (line)]] | alt | 46.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.57× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 28.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +8.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.337× (z -8.7) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 101 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.394× (z -11.6) |
| [[SW1417 (line)]] | alt | 45.5 | 1 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.65× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.427× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[A549 (line)]] | wt | 73.4 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.181× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 39.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 21.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +12.2) | — |
| [[COLO 205 (line)]] | alt | 21.7 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.91× (z +8.5) | — |
| [[H4 (line)]] | wt | 41.4 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.227× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 62.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.86× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 32.0 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.15× (z +9.1) | — |
| [[J82 (line)]] | alt | 33.2 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.14× (z +9.9) ⚠ cell-cycle shift, explains ~75% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 52.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 68.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.6) | — |
| [[NCI-H23 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[RKO (line)]] | wt | 72.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +11.7) | — |
| [[SK-MEL-2 (line)]] | alt | 68.1 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.34× (z +8.5) | — |
| [[A498 (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 164 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 81.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1756), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALS2]] | +0.67 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[MAFG]] | +0.61 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[MRPL45P2]] | +0.60 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[RHBDD3]] | +0.60 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[SPAG5-AS1]] | +0.59 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[COA6]] | +0.58 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[HSCB]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[ZDHHC1]] | +0.56 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[ZCCHC10]] | +0.55 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[USP34-DT]] | +0.55 | +0.45 / +0.40 | both halves | 4e-05 |  |
| [[ZC3HC1]] | +0.54 | +0.55 / +0.36 | both halves | 1e-04 |  |
| [[CCDC117]] | +0.54 | +0.46 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB5A]] | -0.59 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[ANXA11]] | -0.57 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[ELP1]] | -0.56 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[SKP2]] | -0.56 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[SLC35A3]] | -0.56 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[PODXL2]] | -0.55 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[TRAM2]] | -0.55 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[CS]] | -0.55 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[TTLL12]] | -0.54 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[GTPBP3]] | -0.53 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[FAM120A]] | -0.53 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[COLGALT1]] | -0.53 | -0.46 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00944]] | B | LINC00944 activity lowers CREM's level | lines that do not express LINC00944 (20) vs lines expressing it (30) | 1.54× higher at baseline in the lines without LINC00944 | 0.078 | ⚠ within organs, on part of the lines; also absent: RDUR, ENSG00000289600, LINC02405 |
| [[TOP2A]] | B | TOP2A activity lowers CREM's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises CREM's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC02608]] | C | LINC02608 activity strengthens CREM's drug response | lines that do not express LINC02608 (4) vs lines expressing it (45) | the lines without LINC02608 respond 0.71× as strongly (z diff +1.44); strongest at Ixazomib citrate 0.5 µM: 0.91x vs 1.83x (z diff +6.2) | 0.041 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GNA14; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **-** arm (projection on the module's main direction -0.498). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-16.3, 12.2); signed map (0.4, -5.2). **Vector** length 120, 31.1% of its response variance represented; |z| ≥ 3 in 1,294 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.3 | +13.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +8.2 | +11.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.9 | +14.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.5 | +12.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.3 | +11.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +3.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.6 | +4.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -6.9 | -4.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.9 | -7.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.6 | -10.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.4 | -5.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.0 | -5.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.9 | -2.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.9 | -4.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | cAMP responsive element modulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p11.21 — chr10:35,126,791-35,212,958 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hCREM-2 |
| Gene groups (HGNC) | CREB1 transcription factor family |
| Reactome | 2 pathways, smallest: Phosphorylated BMAL1:CLOCK (ARNTL:CLOCK) activates expression of core clock genes; Circadian clock |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03060](https://www.uniprot.org/uniprotkb/Q03060) (cAMP-responsive element modulator):

> Transcriptional regulator that binds the cAMP response element (CRE), a sequence present in many viral and cellular promoters. Isoforms are either transcriptional activators or repressors. Plays a role in spermatogenesis and is involved in spermatid maturation.; [Isoform 6]: May play a role in the regulation of the circadian clock: acts as a transcriptional repressor of the core circadian component PER1 by directly binding to cAMP response elements in its promoter.

**Summary**, from NCBI Gene [1390](https://www.ncbi.nlm.nih.gov/gene/1390):

> This gene encodes a bZIP transcription factor that binds to the cAMP responsive element found in many viral and cellular promoters. It is an important component of cAMP-mediated signal transduction during the spermatogenetic cycle, as well as other complex processes. Alternative promoter and translation initiation site usage allows this gene to exert spatial and temporal specificity to cAMP responsiveness. Multiple alternatively spliced transcript variants encoding several different isoforms …

**Accessions** — [HGNC:2352](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2352) · Entrez [1390](https://www.ncbi.nlm.nih.gov/gene/1390) · UniProt [Q03060](https://www.uniprot.org/uniprotkb/Q03060) · Ensembl [ENSG00000095794](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095794)

## Data

Gene col 1756: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1756); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1756, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1756]; `tensor/DDL_lfc|DDL_z.npy` [1756]; `embed/gene_vectors.npy` [1756]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1756 or target_col == 1756). Every well: [[CREM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CREM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
