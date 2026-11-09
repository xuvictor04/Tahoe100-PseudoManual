---
symbol: "KCNK15-AS1"
type: "gene"
col: 14409
ensembl_id: "ENSG00000244558"
name: "KCNK15 and WISP2 antisense RNA 1"
location: "20q13.12"
module: 57
arm: "+"
pooled_cpm: 3.15
n_lines_expressing: 45
n_dd_up: 33
n_dd_down: 23
n_dd_up_clean: 26
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# KCNK15-AS1

*KCNK15 and WISP2 antisense RNA 1* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 4.37× (z +13.7, q 7e-40, up in 35 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.244× (z -13.1, q 2e-36, down in 30 of 41 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.326× (z -10.4, q 4e-23, down in 28 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RASAL1]] (+0.60, fdr 4e-05), [[MAP2K6]] (+0.60, fdr 1e-05), [[SLC5A4-AS1]] (+0.59, fdr 2e-05); moves opposite to [[ZFYVE16]] (-0.55, fdr 7e-05), [[CASP3]] (-0.52, fdr 6e-05), [[ERCC6L2]] (-0.51, fdr 3e-04).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[RASGEF1A]] → it (grade B ⚠); 6 go from it, the strongest it → [[IFT172]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14409.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **4.37×** | +13.7 | 7e-40 | 35/40 (BT-474, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.35×** | +13.6 | 7e-40 | 35/40 (BT-474, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.15×** | +10.0 | 2e-21 | 26/39 (KATO III, BT-474, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **2.16×** | +7.1 | 1e-10 | 21/39 (SW480, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.13×** | +7.0 | 2e-10 | 14/29 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.12×** | +7.0 | 3e-10 | 22/40 (SHP-77, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.62×** | +6.3 | 2e-08 | 7/39 (NCI-H2030, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +5.8 | 5e-07 | 0/5 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | **1.49×** | +5.3 | 9e-06 | 13/37 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.73×** | +5.1 | 2e-05 | 13/40 (SK-MEL-2, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +5.0 | 4e-05 | 0/4 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.49×** | +4.9 | 6e-05 | 8/39 (SW480, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.71×** | +4.8 | 8e-05 | 10/27 (A498, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.60×** | +4.7 | 1e-04 | 10/39 (NCI-H23, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.65×** | +4.7 | 1e-04 | 14/34 (SK-MEL-2, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.43×** | +4.6 | 1e-04 | 7/38 (SK-MEL-2, SW480, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.67×** | +4.6 | 2e-04 | 10/31 (NCI-H23, A549, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.66×** | +4.4 | 3e-04 | 7/32 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.55×** | +4.1 | 0.001 | 11/35 (SK-MEL-2, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14409.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.244×** | -13.1 | 2e-36 | 30/41 (SW480, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.423×** | -11.3 | 3e-27 | 22/27 (A498, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.326×** | -10.4 | 4e-23 | 28/36 (SW480, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.422×** | -8.0 | 2e-13 | 19/25 (A498, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.458×** | -7.3 | 4e-11 | 26/37 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.445×** | -7.2 | 4e-11 | 19/34 (A498, NCI-H2030, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.495×** | -6.5 | 4e-09 | 17/40 (SNU-1, SW48, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.495×** | -6.5 | 4e-09 | 22/33 (SW480, SNU-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.565×** | -5.3 | 7e-06 | 18/36 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.573×** | -5.2 | 1e-05 | 17/21 (SW480, HEC-1-A, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.581×** | -5.0 | 2e-05 | 11/30 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.585×** | -5.0 | 3e-05 | 19/39 (A498, SW480, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.639×** | -4.2 | 0.001 | 12/36 (NCI-H2030, SW480, …) | two highest doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.646×** | -4.1 | 0.002 | 11/31 (A498, PANC-1, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.654×** | -3.9 | 0.003 | 10/40 (LOX-IMVI, SNU-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.674×** | -3.7 | 0.008 | 14/36 (SNU-1, A549, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.774×** | -3.4 | 0.023 | 14/38 (C32, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -3.2 | 0.045 | 10/28 (HEC-1-A, NCI-H23, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.789×** | -3.1 | 0.047 | 12/23 (SK-MEL-2, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.715×** | -3.1 | 0.047 | 9/22 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Thymol (drug)]] 5 µM |  | **0.794×** | -3.0 | 0.060 | 3/35 (SK-MEL-2, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.70 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14409. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 9.92 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0494× (z -21.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SW480 (line)]] | alt | 7.50 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0170× (z -20.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.117× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 5.09 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0270× (z -15.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0637× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 9.25 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0254× (z -16.8) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H1573 (line)]] | alt | 3.41 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0483× (z -8.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 9.27 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -12.1) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -8.6) |
| [[A549 (line)]] | wt | 2.24 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0976× (z -8.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[BT-474 (line)]] | alt | 3.98 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0913× (z -8.6) ⚠ cell-cycle shift, explains ~57% of this change |
| [[CFPAC-1 (line)]] | alt | 2.53 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0261× (z -9.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 3.85 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -9.2) ⚠ cell-cycle shift, explains ~57% of this change |
| [[PANC-1 (line)]] | alt | 2.86 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0980× (z -13.4) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A-172 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.444 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.953 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.795 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.882 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.671 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.816 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.903 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.928 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14409), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASAL1]] | +0.60 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[MAP2K6]] | +0.60 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[SLC5A4-AS1]] | +0.59 | +0.48 / +0.68 | both halves | 2e-05 | same gene group |
| [[GALM]] | +0.58 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[TMC3-AS1]] | +0.58 | +0.42 / +0.69 | both halves | 4e-05 | same gene group |
| [[DOC2A]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[EPHX2]] | +0.57 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[PRSS16]] | +0.57 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[PECR]] | +0.56 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[ACACB]] | +0.55 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[FBXL16]] | +0.55 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[TTLL1]] | +0.54 | +0.52 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFYVE16]] | -0.55 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[CASP3]] | -0.52 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[ERCC6L2]] | -0.51 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[DDX5]] | -0.50 | -0.29 / -0.55 | both halves | 2e-04 |  |
| [[SATB2]] | -0.50 | -0.29 / -0.47 | both halves | 3e-04 |  |
| [[CYREN]] | -0.50 | -0.30 / -0.35 | both halves | 2e-04 |  |
| [[ZBED5]] | -0.49 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[JADE3]] | -0.49 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[CSRNP2]] | -0.49 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[IGF2BP3]] | -0.48 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[MSRA]] | -0.48 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[UBE3B]] | -0.48 | -0.28 / -0.44 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASGEF1A]] | B | RASGEF1A activity raises KCNK15-AS1's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 1.48× lower at baseline in the lines without RASGEF1A | 0.025 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |
| [[RASGEF1A]] | B | RASGEF1A activity strengthens KCNK15-AS1's drug response | lines that do not express RASGEF1A (21) vs lines expressing it (20) | the lines without RASGEF1A respond 0.70× as strongly (z diff +1.17); strongest at Homoharringtonine 5 µM: 0.37x vs 0.15x (z diff +4.3) | 0.039 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB; target measured in part of the lines; artifact flags |
| [[LINC00173]] | B | LINC00173 activity raises KCNK15-AS1's level | lines that do not express LINC00173 (18) vs lines expressing it (32) | 1.28× lower at baseline in the lines without LINC00173 | 0.071 | ⚠ within organs, on part of the lines; also absent: GBX1, RAB3C, NOVA2 |
| [[MAP2K1]] | B | MAP2K1 activity lowers KCNK15-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFT172]] | B | KCNK15-AS1 activity raises IFT172's level | lines that do not express KCNK15-AS1 (5) vs lines expressing it (45) | 1.89× lower at baseline in the lines without KCNK15-AS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: DNAI1, FBXO15, ENSG00000132832; maybe low, not absent |
| [[ARMCX6]] | B | KCNK15-AS1 activity raises ARMCX6's level | lines that do not express KCNK15-AS1 (5) vs lines expressing it (45) | 1.52× lower at baseline in the lines without KCNK15-AS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: DNAI1, FBXO15, ENSG00000132832; maybe low, not absent |
| [[TTLL1]] | B | KCNK15-AS1 activity raises TTLL1's level | lines that do not express KCNK15-AS1 (5) vs lines expressing it (45) | 1.44× lower at baseline in the lines without KCNK15-AS1 | 0.088 | ⚠ within organs, on part of the lines; also absent: DNAI1, FBXO15, ENSG00000132832; maybe low, not absent |
| [[HMGN3]] | B | KCNK15-AS1 activity raises HMGN3's level | lines that do not express KCNK15-AS1 (5) vs lines expressing it (45) | 2.09× lower at baseline in the lines without KCNK15-AS1 | 0.091 | ⚠ within organs, on part of the lines; also absent: DNAI1, FBXO15, ENSG00000132832; maybe low, not absent |
| [[PREPL]] | B | KCNK15-AS1 activity raises PREPL's level | lines that do not express KCNK15-AS1 (5) vs lines expressing it (45) | 1.47× lower at baseline in the lines without KCNK15-AS1 | 0.097 | ⚠ within organs, on part of the lines; also absent: DNAI1, FBXO15, ENSG00000132832; maybe low, not absent |
| [[MYPOP]] | B | KCNK15-AS1 activity raises MYPOP's level | lines that do not express KCNK15-AS1 (5) vs lines expressing it (45) | 1.40× lower at baseline in the lines without KCNK15-AS1 | 0.098 | ⚠ within organs, on part of the lines; also absent: DNAI1, FBXO15, ENSG00000132832; maybe low, not absent |

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.495). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-1.6, 33.6); signed map (42.2, -9.1). **Vector** length 58.9, 9.62% of its response variance represented; |z| ≥ 3 in 1,119 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +10.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +5.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.1 | +13.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | +13.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +3.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | +4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +5.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -3.0 | -7.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.3 | -5.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -10.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.1 | -8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -1.7 | -11.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -5.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | KCNK15 and WISP2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20q13.12 — chr20:44,694,892-44,746,021 (-) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-445H22.4; previously LINC01260 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49901](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49901) · Entrez [106144538](https://www.ncbi.nlm.nih.gov/gene/106144538) · Ensembl [ENSG00000244558](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244558)

## Data

Gene col 14409: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14409); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14409, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14409]; `tensor/DDL_lfc|DDL_z.npy` [14409]; `embed/gene_vectors.npy` [14409]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14409 or target_col == 14409). Every well: [[KCNK15-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNK15-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
