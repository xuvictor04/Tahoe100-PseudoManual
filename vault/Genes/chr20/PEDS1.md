---
symbol: "PEDS1"
type: "gene"
col: 14250
ensembl_id: "ENSG00000240849"
name: "plasmanylethanolamine desaturase 1"
location: "20q13.13"
module: 85
arm: "+"
pooled_cpm: 51.81
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 16
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# PEDS1

*plasmanylethanolamine desaturase 1* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.53× (z +19.7, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.609× (z -14.1, q 2e-42, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YIF1B]] (+0.77, fdr 1e-05), [[AHDC1]] (+0.74, fdr 7e-06), [[SLC27A1]] (+0.73, fdr 1e-05); moves opposite to [[WARS2-AS1]] (-0.67, fdr 1e-04), [[GABPB2]] (-0.67, fdr 5e-05), [[GNG12-AS1]] (-0.67, fdr 4e-05).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14250.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.53×** | +19.7 | 0e+00 | 46/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.46×** | +19.2 | 0e+00 | 47/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.32×** | +17.9 | 0e+00 | 45/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.90×** | +12.7 | 5e-35 | 44/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +12.2 | 4e-32 | 43/48 (SW480, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +9.4 | 5e-19 | 39/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.94×** | +7.3 | 2e-11 | 38/48 (HOP62, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +6.8 | 7e-10 | 33/48 (MIA PaCa-2, BT-474, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.22×** | +4.1 | 0.002 | 22/47 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.21×** | +4.0 | 0.004 | 19/47 (C-33 A, MIA PaCa-2, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.20×** | +3.9 | 0.005 | 18/49 (NCI-H23, NCI-H1573, …) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.015 | 12/47 (RPMI-7951, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.5 | 0.022 | 12/44 (NCI-H23, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.14× | +3.3 | 0.042 | 19/49 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.3 | 0.042 | 11/42 (HS-578T, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.17× | +3.2 | 0.050 | 15/47 (NCI-H23, LOX-IMVI, …) | two highest doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.16× | +3.0 | 0.077 | 8/49 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14250.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.609×** | -14.1 | 2e-42 | 33/48 (Hs 766T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.576×** | -11.7 | 2e-29 | 38/47 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.613×** | -10.0 | 2e-21 | 33/48 (Hs 766T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.712×** | -9.7 | 3e-20 | 34/47 (Hs 766T, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.616×** | -9.5 | 2e-19 | 31/43 (C-33 A, LS 180, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.647×** | -9.3 | 2e-18 | 32/48 (AsPC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.673×** | -8.1 | 4e-14 | 29/48 (C32, Hs 766T, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.690×** | -7.9 | 2e-13 | 30/48 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.694×** | -7.5 | 5e-12 | 25/39 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.785×** | -7.2 | 2e-11 | 24/48 (HOP62, Hs 766T, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.758×** | -5.7 | 7e-07 | 24/49 (Hs 766T, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.826×** | -5.5 | 2e-06 | 22/48 (HT-29, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.774×** | -5.5 | 2e-06 | 26/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.794×** | -4.9 | 3e-05 | 21/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.817×** | -4.0 | 0.003 | 20/47 (SW48, hTERT-HPNE, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.716×** | -3.7 | 0.006 | 20/49 (Hs 766T, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.852× | -3.3 | 0.033 | 10/48 (C32, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14250. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 259 | 0 | 17 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -23.6) |
| [[HOP62 (line)]] | alt | 49.5 | 5 | 5 | [[Belinostat (drug)]] 5 µM 3.22× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -14.9) |
| [[A-172 (line)]] | wt | 34.3 | 1 | 6 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.99× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -16.3) |
| [[C32 (line)]] | wt | 67.8 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -13.7) |
| [[SW480 (line)]] | alt | 51.9 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.68× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.120× (z -25.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 59.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.34× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.300× (z -13.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 98.5 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.92× (z +12.6) | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -12.5) |
| [[LoVo (line)]] | wt | 23.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.03× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.174× (z -15.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 35.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.85× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.180× (z -14.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 34.0 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 36.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.37× (z +13.1) | — |
| [[SNU-423 (line)]] | alt | 45.3 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.99× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -14.1) |
| [[A498 (line)]] | wt | 77.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -18.4) |
| [[A549 (line)]] | wt | 38.9 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.356× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 49.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -9.7) |
| [[BT-474 (line)]] | alt | 70.0 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.07× (z +8.7) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.431× (z -10.1) |
| [[HS-578T (line)]] | alt | 48.3 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.79× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -13.8) |
| [[LOX-IMVI (line)]] | wt | 25.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.52× (z +11.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 32.8 | 3 | 0 | [[Belinostat (drug)]] 5 µM 4.07× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 48.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.208× (z -13.6) |
| [[NCI-H1792 (line)]] | alt | 56.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -14.0) |
| [[Panc 03.27 (line)]] | alt | 52.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.98× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 41.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -15.1) |
| [[RKO (line)]] | wt | 25.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.04× (z +11.3) | — |
| [[SW1417 (line)]] | alt | 71.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.42× (z +10.7) | — |
| [[C-33 A (line)]] | alt | 109 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.56× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.0854× (z -20.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 47.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.25× (z +10.7) | — |
| [[HCT15 (line)]] | alt | 36.8 | 1 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.70× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.0997× (z -14.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 29.2 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.42× (z +8.9) | — |
| [[KATO III (line)]] | alt | 43.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.91× (z +10.2) | — |
| [[SW 1271 (line)]] | alt | 54.0 | 0 | 2 | — | [[Doxycycline (monohydrate) (drug)]] 0.05 µM 0.0632× (z -9.2) |
| [[SW 900 (line)]] | alt | 34.8 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.228× (z -11.4) |
| [[AN3 CA (line)]] | alt | 46.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.136× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 54.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 84.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 46.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -9.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 50.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 38.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -15.3) |
| [[SNU-1 (line)]] | wt | 42.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -9.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14250), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YIF1B]] | +0.77 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[AHDC1]] | +0.74 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[SLC27A1]] | +0.73 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[GNAI2]] | +0.73 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[MAST3]] | +0.72 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[RIMS3]] | +0.71 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[PDZD7]] | +0.70 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[CFD]] | +0.70 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[SLC9A6]] | +0.70 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[PCMT1]] | +0.69 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[SNTA1]] | +0.69 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[ANKRD27]] | +0.69 | +0.64 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WARS2-AS1]] | -0.67 | -0.61 / -0.35 | both halves | 1e-04 |  |
| [[GABPB2]] | -0.67 | -0.64 / -0.39 | both halves | 5e-05 |  |
| [[GNG12-AS1]] | -0.67 | -0.67 / -0.41 | both halves | 4e-05 |  |
| [[ERCC6L2]] | -0.67 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[PSME3IP1]] | -0.67 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[NIPAL2]] | -0.66 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[INO80D]] | -0.66 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[KRR1]] | -0.65 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[ST7L]] | -0.65 | -0.62 / -0.36 | both halves | 1e-04 |  |
| [[PBLD]] | -0.64 | -0.55 / -0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[TASOR]] | -0.64 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[RXYLT1]] | -0.64 | -0.63 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[MCPH1]] | -0.64 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[UTP20]] | -0.63 | -0.60 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PEDS1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.820). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (5.9, -2.0); signed map (-28.5, 20.0). **Vector** length 132, 38.4% of its response variance represented; |z| ≥ 3 in 1,318 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +9.4 | +19.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +8.9 | +12.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.6 | +17.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +8.4 | +19.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +12.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +6.0 | +7.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.7 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.8 | +3.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.9 | -10.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.7 | -9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.0 | -14.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.9 | -11.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.9 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -5.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.2 | -3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -4.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | plasmanylethanolamine desaturase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.13 — chr20:50,118,254-50,153,734 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Kua; previously TMEM189 |
| Gene groups (HGNC) | Oxygenases |
| Matched by | ensembl_id |

**Function**, from UniProt [A5PLL7](https://www.uniprot.org/uniprotkb/A5PLL7) (Plasmanylethanolamine desaturase 1):

> Plasmanylethanolamine desaturase involved in plasmalogen biogenesis in the endoplasmic reticulum membrane. Plasmalogens are glycerophospholipids with a hydrocarbon chain linked by a vinyl ether bond at the glycerol sn-1 position, and are involved in antioxidative and signaling mechanisms.

**Summary**, from NCBI Gene [387521](https://www.ncbi.nlm.nih.gov/gene/387521):

> Co-transcription of this gene and the neighboring downstream gene (ubiquitin-conjugating enzyme E2 variant 1) generates a rare read-through transcript, which encodes a fusion protein comprised of sequence sharing identity with each individual gene product. The protein encoded by this individual gene lacks a UEV1 domain but includes three transmembrane regions. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2009]

**Accessions** — [HGNC:16735](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16735) · Entrez [387521](https://www.ncbi.nlm.nih.gov/gene/387521) · UniProt [A5PLL7](https://www.uniprot.org/uniprotkb/A5PLL7) · Ensembl [ENSG00000240849](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240849)

## Data

Gene col 14250: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14250); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14250, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14250]; `tensor/DDL_lfc|DDL_z.npy` [14250]; `embed/gene_vectors.npy` [14250]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14250 or target_col == 14250). Every well: [[PEDS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEDS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
