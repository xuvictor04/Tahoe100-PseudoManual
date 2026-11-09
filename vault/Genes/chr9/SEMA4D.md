---
symbol: "SEMA4D"
type: "gene"
col: 11945
ensembl_id: "ENSG00000187764"
name: "semaphorin 4D"
location: "9q22.2"
module: 115
arm: "+"
pooled_cpm: 25.37
n_lines_expressing: 43
n_dd_up: 8
n_dd_down: 17
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# SEMA4D

*semaphorin 4D* — 9q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.26× (z +7.4, q 1e-10, up in 22 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.577× (z -12.2, q 3e-31, down in 25 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTK7]] (+0.66, fdr 1e-05), [[ARHGEF16]] (+0.65, fdr 1e-05), [[UNC5A]] (+0.64, fdr 1e-05); moves opposite to [[RO60]] (-0.50, fdr 1e-04), [[ANKRD17-DT]] (-0.49, fdr 3e-04), [[DNAI4]] (-0.49, fdr 1e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[P2RY2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11945.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +7.4 | 1e-10 | 22/41 (PANC-1, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +4.9 | 2e-04 | 16/38 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.22×** | +4.5 | 0.001 | 7/37 (LS 180, Hs 766T, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.22×** | +4.4 | 0.001 | 16/40 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.20×** | +4.1 | 0.005 | 9/40 (HEC-1-A, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.19× | +3.9 | 0.009 | 13/40 (PANC-1, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **1.39×** | +3.8 | 0.011 | 8/34 (HEC-1-A, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.013 | 7/38 (COLO 205, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.26×** | +3.7 | 0.015 | 9/37 (LoVo, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.19× | +3.6 | 0.017 | 13/39 (HEC-1-A, J82, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.17× | +3.5 | 0.020 | 13/41 (SW480, hTERT-HPNE, …) | all doses, stronger at high dose | position effect removed |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.18× | +3.5 | 0.022 | 7/40 (C-33 A, SW480, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.030 | 11/40 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.17× | +3.4 | 0.030 | 4/38 (J82, SNU-423, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.079 | 8/37 (NCI-H460, SNU-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11945.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.577×** | -12.2 | 3e-31 | 25/40 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.599×** | -11.3 | 3e-27 | 25/36 (RKO, LoVo, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.642×** | -9.4 | 8e-19 | 23/40 (NCI-H2030, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.656×** | -9.3 | 2e-18 | 27/39 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.659×** | -9.2 | 4e-18 | 27/41 (COLO 205, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.672×** | -8.8 | 1e-16 | 23/40 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.653×** | -8.7 | 3e-16 | 21/31 (J82, HT-29, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.708×** | -7.3 | 2e-11 | 18/26 (LS 180, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.710×** | -7.3 | 2e-11 | 19/40 (NCI-H2347, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.721×** | -7.2 | 3e-11 | 23/39 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.795×** | -7.2 | 4e-11 | 18/39 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.724×** | -6.8 | 4e-10 | 19/37 (CFPAC-1, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.731×** | -6.7 | 1e-09 | 18/36 (COLO 205, LS 180, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.835× | -5.6 | 8e-07 | 15/41 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.776×** | -5.4 | 3e-06 | 18/39 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.757×** | -3.2 | 0.040 | 10/35 (NCI-H460, A549, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.762×** | -3.1 | 0.052 | 8/38 (COLO 205, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11945. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 108 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.177× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -13.1) |
| [[HEC-1-A (line)]] | alt | 75.7 | 4 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +22.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.31× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -21.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 33.0 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.350× (z -11.4) |
| [[SW1417 (line)]] | alt | 58.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -18.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -13.1) |
| [[HT-29 (line)]] | alt | 49.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -9.2) |
| [[LS 180 (line)]] | wt | 42.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0942× (z -22.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.250× (z -13.8) |
| [[Panc 03.27 (line)]] | alt | 45.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.362× (z -8.7) |
| [[RKO (line)]] | wt | 49.2 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.304× (z -10.2) |
| [[SW480 (line)]] | alt | 26.5 | 1 (1 ⚠) | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.21× (z +8.7) ⚠ cell-cycle shift, explains ~12% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.402× (z -10.0) |
| [[A-172 (line)]] | wt | 30.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.19× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 31.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -12.3) |
| [[J82 (line)]] | alt | 60.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0876× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -12.9) |
| [[MIA PaCa-2 (line)]] | alt | 24.1 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.56× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.204× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 29.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -13.3) |
| [[A-427 (line)]] | wt | 21.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.232× (z -10.4) |
| [[HOP62 (line)]] | alt | 16.7 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -9.0) |
| [[KATO III (line)]] | alt | 41.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.285× (z -10.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 55.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -13.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 23.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.303× (z -8.7) |
| [[AN3 CA (line)]] | alt | 44.0 | 0 | 1 | — | [[Bicalutamide (drug)]] 0.5 µM 0.140× (z -8.7) |
| [[BT-474 (line)]] | alt | 35.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -9.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 42.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.290× (z -9.1) |
| [[H4 (line)]] | wt | 11.8 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.124× (z -8.5) |
| [[HCT15 (line)]] | alt | 40.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -10.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 6.92 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.37× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 14.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.206× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 11.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.316× (z -8.6) |
| [[PANC-1 (line)]] | alt | 6.41 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +15.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-1 (line)]] | wt | 28.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -10.2) |
| [[SNU-423 (line)]] | alt | 8.15 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.68× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.12 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11945), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTK7]] | +0.66 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[ARHGEF16]] | +0.65 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[UNC5A]] | +0.64 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[ARHGEF10L]] | +0.62 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[RASAL1]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[DNMT3B]] | +0.61 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[EDA]] | +0.58 | +0.33 / +0.61 | both halves | 1e-04 |  |
| [[SLC45A4]] | +0.58 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[CORO2A]] | +0.58 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[CRYBG2]] | +0.57 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[NGEF]] | +0.57 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[ARHGAP44]] | +0.57 | +0.47 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RO60]] | -0.50 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[ANKRD17-DT]] | -0.49 | -0.46 / -0.26 | both halves | 3e-04 |  |
| [[DNAI4]] | -0.49 | -0.34 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P2RY2]] | B | P2RY2 activity strengthens SEMA4D's drug response | lines that do not express P2RY2 (22) vs lines expressing it (19) | the lines without P2RY2 respond 0.36× as strongly (z diff +2.72); strongest at Dinaciclib 5 µM: 0.91x vs 0.37x (z diff +5.9) | 0.047 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223; target measured in part of the lines; artifact flags |
| [[VAV1]] | B | VAV1 activity raises SEMA4D's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 2.00× lower at baseline in the lines without VAV1 | 0.047 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |
| [[LRP4]] | B | LRP4 activity weakens SEMA4D's drug response | lines that do not express LRP4 (14) vs lines expressing it (27) | the lines without LRP4 respond 1.56× as strongly (z diff -1.42); strongest at Dinaciclib 0.05 µM: 0.41x vs 0.80x (z diff -4.5) | 0.058 | ⚠ within organs, on part of the lines; target measured in part of the lines; artifact flags |
| [[SULT2B1]] | B | SULT2B1 activity strengthens SEMA4D's drug response | lines that do not express SULT2B1 (22) vs lines expressing it (19) | the lines without SULT2B1 respond 0.42× as strongly (z diff +2.58); strongest at Dinaciclib 5 µM: 0.92x vs 0.33x (z diff +7.1) | 0.060 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CRYBG2]] | B | CRYBG2 activity strengthens SEMA4D's drug response | lines that do not express CRYBG2 (19) vs lines expressing it (22) | the lines without CRYBG2 respond 0.42× as strongly (z diff +2.38); strongest at Dinaciclib 5 µM: 0.87x vs 0.36x (z diff +6.2) | 0.066 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1; target measured in part of the lines; artifact flags |
| [[IL17RE]] | B | IL17RE activity strengthens SEMA4D's drug response | lines that do not express IL17RE (8) vs lines expressing it (33) | the lines without IL17RE respond 0.50× as strongly (z diff +2.08); strongest at Dinaciclib 5 µM: 1.06x vs 0.43x (z diff +5.7) | 0.068 | ⚠ within organs, on part of the lines; also absent: MCF2L; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[B3GNT7]] | B | B3GNT7 activity raises SEMA4D's level | lines that do not express B3GNT7 (31) vs lines expressing it (19) | 1.25× lower at baseline in the lines without B3GNT7 | 0.071 | ⚠ within organs, on part of the lines; also absent: KRT23, PROM1, HSD17B2 |
| [[TTC9]] | B | TTC9 activity raises SEMA4D's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 2.61× lower at baseline in the lines without TTC9 | 0.089 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |
| [[PCDH1]] | B | PCDH1 activity strengthens SEMA4D's drug response | lines that do not express PCDH1 (17) vs lines expressing it (24) | the lines without PCDH1 respond 0.52× as strongly (z diff +1.95); strongest at Dinaciclib 5 µM: 0.74x vs 0.43x (z diff +4.4) | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29; target measured in part of the lines; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers SEMA4D's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises SEMA4D's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LRRC20]] | C | LRRC20 activity raises SEMA4D's level | lines that do not express LRRC20 (5) vs lines expressing it (45) | 5.13× lower at baseline in the lines without LRRC20 | 0.057 | ⚠ within organs, on part of the lines; also absent: MCM2, MCM10, SEMA4D; maybe low, not absent; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.685). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.1, 47.0); signed map (-21.9, 35.8). **Vector** length 90.0, 18.7% of its response variance represented; |z| ≥ 3 in 931 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +4.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | +3.9 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.6 | +4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +3.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +2.6 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -7.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.8 | -9.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -3.6 | -4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.3 | -7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -5.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | semaphorin 4D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.2 — chr9:89,360,787-89,498,130 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD100, coll-4, FLJ39737; previously SEMAJ, C9orf164 |
| Gene groups (HGNC) | CD molecules; Immunoglobulin like domain containing; Semaphorins |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 7 pathways, smallest: Sema4D mediated inhibition of cell attachment and migration; Other semaphorin interactions; Sema4D induced cell migration and growth-cone collapse |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92854](https://www.uniprot.org/uniprotkb/Q92854) (Semaphorin-4D):

> Cell surface receptor for PLXNB1 and PLXNB2 that plays an important role in cell-cell signaling. Regulates GABAergic synapse development (By similarity). Promotes the development of inhibitory synapses in a PLXNB1-dependent manner (By similarity). Modulates the complexity and arborization of developing neurites in hippocampal neurons by activating PLXNB1 and interaction with PLXNB1 mediates activation of RHOA. Promotes the migration of cerebellar granule cells. Plays a role in the immune …

**Summary**, from NCBI Gene [10507](https://www.ncbi.nlm.nih.gov/gene/10507):

> Enables identical protein binding activity; semaphorin receptor binding activity; and transmembrane signaling receptor activity. Involved in several processes, including ossification involved in bone maturation; positive regulation of phosphatidylinositol 3-kinase/protein kinase B signal transduction; and regulation of neuron projection development. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10732](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10732) · Entrez [10507](https://www.ncbi.nlm.nih.gov/gene/10507) · UniProt [Q92854](https://www.uniprot.org/uniprotkb/Q92854) · Ensembl [ENSG00000187764](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187764)

## Data

Gene col 11945: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11945); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11945, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11945]; `tensor/DDL_lfc|DDL_z.npy` [11945]; `embed/gene_vectors.npy` [11945]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11945 or target_col == 11945). Every well: [[SEMA4D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEMA4D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
