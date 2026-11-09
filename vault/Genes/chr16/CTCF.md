---
symbol: "CTCF"
type: "gene"
col: 2296
ensembl_id: "ENSG00000102974"
name: "CCCTC-binding factor"
location: "16q22.1"
module: 7
arm: "+"
pooled_cpm: 77.5
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# CTCF

*CCCTC-binding factor* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.21× (z +13.6, q 4e-39, up in 37 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.447× (z -26.4, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGF29]] (+0.61, fdr 2e-05), [[GMEB1]] (+0.60, fdr 1e-05), [[UQCRFS1]] (+0.60, fdr 1e-04); moves opposite to [[MALAT1]] (-0.54, fdr 1e-04), [[PEA15]] (-0.50, fdr 2e-05), [[SPAG9]] (-0.49, fdr 3e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2296.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.21×** | +13.6 | 4e-39 | 37/49 (SW480, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.84×** | +10.5 | 3e-23 | 34/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.15× | +4.6 | 9e-04 | 12/48 (LS 180, CFPAC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.15× | +4.5 | 9e-04 | 17/48 (LS 180, SNU-423, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.9 | 0.013 | 13/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Resveratrol (drug)]] 5 µM |  | 1.08× | +3.8 | 0.014 | 0/49 | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.11× | +3.4 | 0.057 | 8/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.057 | 12/49 (A498, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2296.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.447×** | -26.4 | 0e+00 | 47/48 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.497×** | -22.9 | 0e+00 | 46/48 (C-33 A, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.497×** | -22.9 | 0e+00 | 48/48 (BT-474, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.547×** | -19.0 | 0e+00 | 41/44 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.572×** | -18.3 | 0e+00 | 41/49 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.575×** | -16.7 | 0e+00 | 34/45 (SW48, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.665×** | -13.3 | 1e-38 | 44/48 (SW48, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.724×** | -10.6 | 3e-24 | 35/48 (NCI-H2030, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.844× | -7.8 | 3e-13 | 22/48 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.805×** | -7.1 | 7e-11 | 23/48 (NCI-H2347, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.805×** | -6.9 | 3e-10 | 28/49 (H4, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.669×** | -6.9 | 3e-10 | 31/49 (NCI-H2347, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.812×** | -6.5 | 3e-09 | 26/50 (SW48, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.879× | -5.9 | 1e-07 | 17/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.849× | -5.1 | 1e-05 | 13/48 (A549, KATO III, …) | rises with dose |  |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | 0.890× | -3.7 | 0.007 | 14/48 (COLO 205, SW 1271, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.930× | -3.4 | 0.021 | 2/48 (SW 1088, H4) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.903× | -3.3 | 0.022 | 5/48 (A-427, SW480, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.906× | -3.1 | 0.045 | 3/49 (SW 900, HOP62, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.908× | -3.1 | 0.045 | 13/48 (A-427, NCI-H661, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2296. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 93.4 | 6 (4 ⚠) | 6 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 5.16× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.395× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 139 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.390× (z -13.0) |
| [[HEC-1-A (line)]] | alt | 95.8 | 2 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.98× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.415× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 90.1 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.478× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 81.1 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.436× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.534× (z -10.4) |
| [[SW48 (line)]] | wt | 123 | 2 | 6 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.40× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.336× (z -11.2) |
| [[SW480 (line)]] | alt | 113 | 2 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.72× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.343× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.465× (z -13.0) |
| [[NCI-H2347 (line)]] | alt | 64.6 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.346× (z -17.0) |
| [[C-33 A (line)]] | alt | 132 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.15× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.276× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.309× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 82.6 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.338× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.391× (z -13.6) |
| [[C32 (line)]] | wt | 68.6 | 1 | 4 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.95× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.404× (z -10.5) |
| [[COLO 205 (line)]] | alt | 65.4 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.01× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.344× (z -10.5) |
| [[KATO III (line)]] | alt | 82.6 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.414× (z -12.3) |
| [[LoVo (line)]] | wt | 80.5 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.466× (z -11.8) |
| [[A-427 (line)]] | wt | 90.0 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.431× (z -10.4) |
| [[AN3 CA (line)]] | alt | 139 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -12.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 57.2 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.393× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 86.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.288× (z -13.2) |
| [[MIA PaCa-2 (line)]] | alt | 63.3 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.373× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 78.1 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.49× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.440× (z -9.7) |
| [[PANC-1 (line)]] | alt | 56.6 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.458× (z -12.9) |
| [[SK-MEL-2 (line)]] | alt | 65.7 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.404× (z -9.9) |
| [[A498 (line)]] | wt | 62.4 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.459× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 61.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.316× (z -12.4) |
| [[SW1417 (line)]] | alt | 83.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.427× (z -11.4) |
| [[A-172 (line)]] | wt | 58.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.386× (z -11.5) |
| [[BT-474 (line)]] | alt | 80.6 | 1 | 1 | [[TAK-901 (drug)]] 0.05 µM 2.58× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -14.7) |
| [[HOP62 (line)]] | alt | 75.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.435× (z -10.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 52.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.382× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.453× (z -9.0) |
| [[HT-29 (line)]] | alt | 74.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.397× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 87.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.465× (z -9.2) |
| [[A549 (line)]] | wt | 70.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.366× (z -12.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 66.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.272× (z -9.6) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 72.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.479× (z -10.2) |
| [[NCI-H596 (line)]] | alt | 79.4 | 0 | 1 | — | [[Oxaprozin (drug)]] 5 µM 0.131× (z -9.5) |
| [[RKO (line)]] | wt | 72.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -8.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 94.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.435× (z -9.5) |
| [[SNU-423 (line)]] | alt | 54.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.400× (z -9.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 57.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.416× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 87.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 97.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 93.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2296), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGF29]] | +0.61 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[GMEB1]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[UQCRFS1]] | +0.60 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[PATZ1]] | +0.60 | +0.52 / +0.54 | both halves | 1e-05 | same gene group |
| [[ZNF689]] | +0.60 | +0.34 / +0.62 | both halves | 1e-04 | same gene group |
| [[ASH2L]] | +0.59 | +0.46 / +0.61 | both halves | 3e-05 | pathway: Activation of HOX genes during differentiation; STRING 625 |
| [[MRM2]] | +0.59 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[AKAP8]] | +0.59 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[MCRS1]] | +0.58 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[SRSF4]] | +0.57 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[TOE1]] | +0.57 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[LIN9]] | +0.56 | +0.44 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MALAT1]] | -0.54 | -0.33 / -0.58 | both halves | 1e-04 |  |
| [[PEA15]] | -0.50 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[SPAG9]] | -0.49 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[PRKCI]] | -0.48 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[NEAT1]] | -0.48 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[NBEAL1]] | -0.47 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[TALAM1]] | -0.47 | -0.25 / -0.54 | both halves | 4e-04 |  |
| [[UFM1]] | -0.47 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[VAMP7]] | -0.47 | -0.17 / -0.49 | ⚠ not reproduced | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CTCF's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises CTCF's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.452). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-50.4, -0.2); signed map (-5.5, -17.7). **Vector** length 107, 28.4% of its response variance represented; |z| ≥ 3 in 1,192 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.6 | -0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +7.0 | +2.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.4 | +13.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.1 | +10.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.4 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +0.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +0.6 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.6 | +2.6 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.3 | -16.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.1 | -18.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.8 | -19.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -7.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.1 | -13.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.2 | -3.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -2.2 | -0.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | CCCTC-binding factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,562,467-67,639,177 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FAP108, CFAP108 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Cilia and flagella associated |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 6 pathways, smallest: CHD6, CHD7, CHD8, CHD9 subfamily; Activation of HOX genes during differentiation; Activation of anterior HOX genes in hindbrain development during early embryogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P49711](https://www.uniprot.org/uniprotkb/P49711) (Transcriptional repressor CTCF):

> Chromatin binding factor that binds to DNA sequence specific sites and regulates the 3D structure of chromatin. Binds together strands of DNA, thus forming chromatin loops, and anchors DNA to cellular structures, such as the nuclear lamina. Defines the boundaries between active and heterochromatic DNA via binding to chromatin insulators, thereby preventing interaction between promoter and nearby enhancers and silencers. Participates in the allele-specific gene expression at the imprinted …

**Summary**, from NCBI Gene [10664](https://www.ncbi.nlm.nih.gov/gene/10664):

> This gene is a member of the BORIS + CTCF gene family and encodes a transcriptional regulator protein with 11 highly conserved zinc finger (ZF) domains. This nuclear protein is able to use different combinations of the ZF domains to bind different DNA target sequences and proteins. Depending upon the context of the site, the protein can bind a histone acetyltransferase (HAT)-containing complex and function as a transcriptional activator or bind a histone deacetylase (HDAC)-containing complex …

**Accessions** — [HGNC:13723](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13723) · Entrez [10664](https://www.ncbi.nlm.nih.gov/gene/10664) · UniProt [P49711](https://www.uniprot.org/uniprotkb/P49711) · Ensembl [ENSG00000102974](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102974)

## Data

Gene col 2296: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2296); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2296, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2296]; `tensor/DDL_lfc|DDL_z.npy` [2296]; `embed/gene_vectors.npy` [2296]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2296 or target_col == 2296). Every well: [[CTCF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTCF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
