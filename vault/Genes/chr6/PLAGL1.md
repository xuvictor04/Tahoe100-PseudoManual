---
symbol: "PLAGL1"
type: "gene"
col: 3993
ensembl_id: "ENSG00000118495"
name: "PLAG1 like zinc finger 1"
location: "6q24.2"
module: 23
arm: "+"
pooled_cpm: 38.86
n_lines_expressing: 28
n_dd_up: 20
n_dd_down: 24
n_dd_up_clean: 16
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 7
direction_downstream: 9
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# PLAGL1

*PLAG1 like zinc finger 1* — 6q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.52× (z +11.6, q 1e-28, up in 15 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.252× (z -26.9, q 0e+00, down in 24 of 26 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JAM2]] (+0.66, fdr 1e-05), [[KMO]] (+0.65, fdr 1e-05), [[TRPC1]] (+0.65, fdr 1e-05); moves opposite to [[BCR]] (-0.58, fdr 3e-05), [[PPM1F]] (-0.57, fdr 6e-05), [[FOXK1]] (-0.56, fdr 1e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[IRAG2]] → it (grade B ⚠); 9 go from it, the strongest it → [[RBMS3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3993.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +11.6 | 1e-28 | 15/26 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +11.1 | 3e-26 | 13/26 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.47×** | +7.2 | 1e-10 | 14/25 (NCI-H460, A-172, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.46×** | +7.1 | 1e-10 | 20/25 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +6.3 | 4e-08 | 11/26 (SW480, RKO, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.34×** | +6.1 | 7e-08 | 13/26 (NCI-H460, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.38×** | +6.1 | 7e-08 | 15/26 (NCI-H460, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.30×** | +6.1 | 8e-08 | 13/26 (NCI-H460, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.35×** | +5.9 | 2e-07 | 18/25 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.34×** | +5.7 | 5e-07 | 8/26 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.31×** | +5.2 | 1e-05 | 13/26 (NCI-H460, A-172, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.19× | +4.5 | 3e-04 | 12/26 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +4.4 | 4e-04 | 12/26 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.16× | +4.1 | 0.002 | 8/26 (SW480, H4, …) | inconsistent across doses | low cells (technical?) |
| [[RMC-6236 (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.007 | 14/26 (NCI-H460, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.7 | 0.007 | 5/26 (C-33 A, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.009 | 3/26 (A-427, LoVo, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.20×** | +3.6 | 0.010 | 11/26 (RKO, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3993.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.252×** | -26.9 | 0e+00 | 24/26 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.319×** | -22.3 | 0e+00 | 25/26 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.369×** | -19.5 | 0e+00 | 23/26 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.489×** | -14.0 | 3e-42 | 22/23 (A-172, SW480, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.553×** | -11.6 | 5e-29 | 22/25 (SW480, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.545×** | -11.4 | 3e-28 | 20/24 (NCI-H460, HCT15, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.330×** | -11.3 | 8e-28 | 21/27 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.670×** | -7.8 | 3e-13 | 20/25 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.483×** | -7.4 | 7e-12 | 17/26 (SW480, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.671×** | -7.2 | 3e-11 | 21/26 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.694×** | -7.2 | 4e-11 | 17/26 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.706×** | -6.8 | 4e-10 | 19/25 (HCT15, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.686×** | -6.8 | 4e-10 | 17/22 (hTERT-HPNE, RPMI-7951, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **0.697×** | -6.8 | 5e-10 | 16/21 (NCI-H1792, SW 900, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.711×** | -6.7 | 9e-10 | 15/26 (SW480, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.527×** | -6.6 | 2e-09 | 19/26 (NCI-H1792, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.721×** | -6.1 | 5e-08 | 17/26 (LOX-IMVI, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.788×** | -4.7 | 9e-05 | 18/26 (HCT15, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | **0.824×** | -3.5 | 0.012 | 5/26 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.839× | -3.4 | 0.013 | 15/26 (H4, RPMI-7951, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.833×** | -3.4 | 0.013 | 8/26 (NCI-H661, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3993. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 77.9 | 2 | 15 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.0885× (z -33.2) |
| [[H4 (line)]] | wt | 173 | 0 | 14 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0947× (z -22.4) |
| [[NCI-H1792 (line)]] | alt | 133 | 0 | 13 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0620× (z -29.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.106× (z -24.8) |
| [[NCI-H460 (line)]] | wt | 68.9 | 5 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.221× (z -16.8) |
| [[RKO (line)]] | wt | 101 | 4 (1 ⚠) | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +14.8) | [[Belinostat (drug)]] 5 µM 0.0896× (z -22.6) |
| [[HCT15 (line)]] | alt | 218 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0590× (z -28.1) |
| [[HOP62 (line)]] | alt | 168 | 1 | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +17.2) | [[Panobinostat (drug)]] 5 µM 0.0750× (z -26.8) |
| [[hTERT-HPNE (line)]] | wt | 143 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.112× (z -20.5) |
| [[RPMI-7951 (line)]] | alt | 90.9 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.157× (z -16.2) |
| [[LOX-IMVI (line)]] | wt | 54.8 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -18.4) |
| [[SW 900 (line)]] | alt | 78.6 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.0520× (z -27.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.257× (z -13.3) |
| [[A-172 (line)]] | wt | 39.4 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0393× (z -26.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.282× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 52.0 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +11.7) | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -18.0) |
| [[LoVo (line)]] | wt | 13.8 | 1 (1 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +14.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.235× (z -9.5) |
| [[A549 (line)]] | wt | 36.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.130× (z -16.8) |
| [[Hs 766T (line)]] | wt | 38.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.114× (z -15.8) |
| [[CHP-212 (line)]] | wt | 110 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.126× (z -10.0) |
| [[SNU-423 (line)]] | alt | 14.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.0834× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[A498 (line)]] | wt | 45.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.351× (z -9.2) |
| [[C-33 A (line)]] | alt | 12.6 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.109× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 16.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.140× (z -8.8) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 64.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.212× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[A-427 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.15 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.18 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.76 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.48 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.27 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 9.44 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.33 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.30 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 13.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3993), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JAM2]] | +0.66 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[KMO]] | +0.65 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[TRPC1]] | +0.65 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[FLRT2]] | +0.63 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[FAM200A]] | +0.60 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[ZEB2]] | +0.60 | +0.49 / +0.61 | both halves | 1e-05 | same gene group |
| [[PBDC1]] | +0.60 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[IL32]] | +0.58 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[MYPN]] | +0.57 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[ZNF181]] | +0.56 | +0.52 / +0.36 | both halves | 9e-05 | same gene group |
| [[FILIP1L]] | +0.55 | +0.60 / +0.40 | both halves | 4e-05 |  |
| [[THAP2]] | +0.55 | +0.53 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCR]] | -0.58 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[PPM1F]] | -0.57 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[FOXK1]] | -0.56 | -0.62 / -0.35 | both halves | 1e-04 |  |
| [[COPG2]] | -0.54 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[MBOAT1]] | -0.54 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[LRRC20]] | -0.54 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[RALGPS1]] | -0.53 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[TBC1D24]] | -0.53 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[VPS26B]] | -0.53 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[AP3M2]] | -0.52 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[NUDT21]] | -0.51 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[MAPK9]] | -0.51 | -0.44 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRAG2]] | B | IRAG2 activity raises PLAGL1's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 2.75× lower at baseline in the lines without IRAG2 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411 |
| [[FLRT2]] | B | FLRT2 activity raises PLAGL1's level | lines that do not express FLRT2 (29) vs lines expressing it (21) | 2.97× lower at baseline in the lines without FLRT2 | 0.060 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2 |
| [[MAP2K1]] | B | MAP2K1 activity lowers PLAGL1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[DNAH11]] | B | DNAH11 activity raises PLAGL1's level | lines that do not express DNAH11 (23) vs lines expressing it (27) | 2.41× lower at baseline in the lines without DNAH11 | 0.086 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1 |
| [[PTGFR]] | C | PTGFR activity raises PLAGL1's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 3.27× lower at baseline in the lines without PTGFR | 0.033 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX; co-absent with the target |
| [[ZEB2]] | C | ZEB2 activity raises PLAGL1's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 2.92× lower at baseline in the lines without ZEB2 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16; co-absent with the target |
| [[OR9Q1]] | C | OR9Q1 activity raises PLAGL1's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 3.01× lower at baseline in the lines without OR9Q1 | 0.053 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBMS3]] | B | PLAGL1 activity raises RBMS3's level | lines that do not express PLAGL1 (22) vs lines expressing it (28) | 1.94× lower at baseline in the lines without PLAGL1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, GJA1, SOX5 |
| [[GPR176]] | B | PLAGL1 activity raises GPR176's level | lines that do not express PLAGL1 (22) vs lines expressing it (28) | 2.75× lower at baseline in the lines without PLAGL1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, GJA1, SOX5 |
| [[RALGPS1]] | B | PLAGL1 activity lowers RALGPS1's level | lines that do not express PLAGL1 (22) vs lines expressing it (28) | 1.69× higher at baseline in the lines without PLAGL1 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, GJA1, SOX5 |
| [[APH1B]] | B | PLAGL1 activity raises APH1B's level | lines that do not express PLAGL1 (22) vs lines expressing it (28) | 1.92× lower at baseline in the lines without PLAGL1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, GJA1, SOX5 |
| [[ZEB2]] | C | PLAGL1 activity raises ZEB2's level | lines that do not express PLAGL1 (22) vs lines expressing it (28) | 3.58× lower at baseline in the lines without PLAGL1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, GJA1, SOX5; co-absent with the target |
| [[ABI3BP]] | C | PLAGL1 activity raises ABI3BP's level | lines that do not express PLAGL1 (22) vs lines expressing it (28) | 1.95× lower at baseline in the lines without PLAGL1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, GJA1, SOX5; co-absent with the target |
| [[ZFY]] | C | PLAGL1 activity raises ZFY's level | lines that do not express PLAGL1 (22) vs lines expressing it (28) | 2.87× lower at baseline in the lines without PLAGL1 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, GJA1, SOX5; co-absent with the target |
| [[OR9Q1]] | C | PLAGL1 activity raises OR9Q1's level | lines that do not express PLAGL1 (22) vs lines expressing it (28) | 1.96× lower at baseline in the lines without PLAGL1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, GJA1, SOX5; co-absent with the target |
| [[PTGFR]] | C | PLAGL1 activity raises PTGFR's level | lines that do not express PLAGL1 (22) vs lines expressing it (28) | 2.50× lower at baseline in the lines without PLAGL1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, GJA1, SOX5; co-absent with the target |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.489). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (35.6, 19.0); signed map (45.0, 14.8). **Vector** length 91.9, 25.0% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.0 | +11.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.1 | +11.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.7 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.9 | +3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.6 | +6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.4 | +7.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +7.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.3 | +6.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.6 | -26.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.3 | -19.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.3 | -11.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.1 | -7.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.7 | -22.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -6.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -7.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | PLAG1 like zinc finger 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.2 — chr6:143,940,300-144,064,599 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZAC, LOT1 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 3 pathways, smallest: TP53 regulates transcription of additional cell cycle genes whose exact role in the p53 pathway remain uncertain; TP53 Regulates Transcription of Cell Cycle Genes; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UM63](https://www.uniprot.org/uniprotkb/Q9UM63) (Zinc finger protein PLAGL1):

> Acts as a transcriptional activator. Involved in the transcriptional regulation of type 1 receptor for pituitary adenylate cyclase-activating polypeptide.

**Summary**, from NCBI Gene [5325](https://www.ncbi.nlm.nih.gov/gene/5325):

> This gene encodes a C2H2 zinc finger protein that functions as a suppressor of cell growth. This gene is often deleted or methylated and silenced in cancer cells. In addition, overexpression of this gene during fetal development is thought to be the causal factor for transient neonatal diabetes mellitus (TNDM). Alternative splicing and the use of alternative promoters results in multiple transcript variants encoding two different protein isoforms. The P1 downstream promoter of this gene is …

**Accessions** — [HGNC:9046](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9046) · Entrez [5325](https://www.ncbi.nlm.nih.gov/gene/5325) · UniProt [Q9UM63](https://www.uniprot.org/uniprotkb/Q9UM63) · Ensembl [ENSG00000118495](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118495)

## Data

Gene col 3993: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3993); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3993, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3993]; `tensor/DDL_lfc|DDL_z.npy` [3993]; `embed/gene_vectors.npy` [3993]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3993 or target_col == 3993). Every well: [[PLAGL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLAGL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
