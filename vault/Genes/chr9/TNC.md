---
symbol: "TNC"
type: "gene"
col: 479
ensembl_id: "ENSG00000041982"
name: "tenascin C"
location: "9q33.1"
module: 87
arm: "+"
pooled_cpm: 76.26
n_lines_expressing: 27
n_dd_up: 22
n_dd_down: 25
n_dd_up_clean: 18
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 19
direction_downstream: 10
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# TNC

*tenascin C* — 9q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.50× (z +14.7, q 0e+00, up in 21 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.581× (z -8.7, q 2e-15, down in 21 of 25 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.518× (z -7.5, q 2e-11, down in 21 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLIPR1]] (+0.58, fdr 1e-05), [[KCTD12]] (+0.57, fdr 1e-05), [[DOCK2]] (+0.56, fdr 2e-05); moves opposite to [[AGO4]] (-0.50, fdr 3e-05), [[FHIP2A]] (-0.47, fdr 6e-05), [[ZNF594-DT]] (-0.47, fdr 3e-05).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[SHC4]] → it (grade B ⚠); 10 go from it, the strongest it → [[CHST11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 479.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.50×** | +14.7 | 0e+00 | 21/25 (J82, RKO, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.44×** | +9.7 | 5e-20 | 14/19 (A498, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.09×** | +8.4 | 9e-15 | 19/26 (RKO, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.05×** | +8.2 | 4e-14 | 14/23 (A498, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +8.1 | 5e-14 | 11/20 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.83×** | +6.9 | 7e-10 | 16/25 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **2.83×** | +6.2 | 5e-08 | 15/25 (A498, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.19×** | +4.7 | 2e-04 | 17/26 (NCI-H2347, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | **1.51×** | +4.7 | 2e-04 | 12/26 (LOX-IMVI, COLO 205, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **2.17×** | +4.6 | 2e-04 | 11/25 (A498, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.90×** | +3.8 | 0.007 | 12/25 (A498, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Larotrectinib (drug)]] 0.05 µM |  | **1.39×** | +3.8 | 0.007 | 5/26 (SW 900, LOX-IMVI, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.88×** | +3.7 | 0.008 | 13/25 (AsPC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.008 | 13/25 (RPMI-7951, LOX-IMVI, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.86×** | +3.7 | 0.008 | 10/25 (AsPC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.012 | 14/25 (LOX-IMVI, COLO 205, …) | top dose only | position effect removed |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **1.37×** | +3.6 | 0.013 | 11/25 (NCI-H2347, SNU-423, …) | all doses, flat | position effect removed |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.028 | 6/25 (AsPC-1, CFPAC-1, …) | all doses, flat | position effect removed |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.028 | 11/25 (H4, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 479.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.581×** | -8.7 | 2e-15 | 21/25 (RKO, C32, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **0.518×** | -7.5 | 2e-11 | 21/25 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.575×** | -6.3 | 7e-08 | 17/25 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.619×** | -5.4 | 8e-06 | 19/25 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.663×** | -4.6 | 4e-04 | 16/25 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.675×** | -4.4 | 8e-04 | 20/25 (SW480, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.758×** | -4.4 | 8e-04 | 13/25 (LOX-IMVI, SW 900, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.691×** | -4.2 | 0.002 | 13/25 (SW 900, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.698×** | -4.1 | 0.003 | 14/26 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **0.712×** | -3.8 | 0.007 | 14/25 (J82, HS-578T, …) | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.788×** | -3.8 | 0.007 | 12/25 (BT-474, RPMI-7951, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.718×** | -3.7 | 0.009 | 16/25 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.712×** | -3.7 | 0.010 | 17/23 (C32, H4, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.708×** | -3.6 | 0.012 | 7/25 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.543×** | -3.6 | 0.012 | 14/25 (SK-MEL-2, LOX-IMVI, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **0.803×** | -3.5 | 0.016 | 10/25 (NCI-H1792, COLO 205, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.810×** | -3.4 | 0.025 | 7/25 (BT-474, A498, …) | inconsistent across doses | position effect removed |
| [[Retinoic acid (drug)]] 5 µM |  | **0.816×** | -3.2 | 0.037 | 13/26 (SK-MEL-2, C32, …) | two highest doses |  |
| [[Terfenadine (drug)]] 5 µM |  | **0.817×** | -3.2 | 0.038 | 10/25 (LOX-IMVI, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 479. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 926 | 0 | 16 (6 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.107× (z -19.3) |
| [[SK-MEL-2 (line)]] | alt | 299 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -22.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.189× (z -12.5) |
| [[SW480 (line)]] | alt | 108 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0908× (z -15.2) |
| [[A498 (line)]] | wt | 42.2 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +14.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.81× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 23.2 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.86× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[COLO 205 (line)]] | alt | 89.8 | 3 (1 ⚠) | 0 | [[Daptomycin (drug)]] 0.5 µM 13.2× (z +9.7) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 0.5 µM 11.2× (z +9.1) | — |
| [[J82 (line)]] | alt | 30.5 | 3 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 6.38× (z +15.3) | — |
| [[RKO (line)]] | wt | 27.0 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 6.44× (z +12.6) | [[Selinexor (drug)]] 5 µM 0.151× (z -12.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SHP-77 (line)]] | alt | 24.1 | 3 (1 ⚠) | 0 | [[Daptomycin (drug)]] 5 µM 10.6× (z +9.7) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 5.22× (z +9.6) | — |
| [[H4 (line)]] | wt | 393 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -17.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 31.0 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 5.14× (z +11.3) | — |
| [[hTERT-HPNE (line)]] | wt | 102 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.01× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 287 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.272× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 265 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 310 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.48× (z +8.6) | — |
| [[A-172 (line)]] | wt | 7.34 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.15 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.62 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.74 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.34 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 17.6 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.05 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.46 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.74 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.75 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.84 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 246 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.73 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.73 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.84 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.47 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 98.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.11 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.86 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.53 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.9 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 45.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 479), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLIPR1]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[KCTD12]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[DOCK2]] | +0.56 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[COL15A1]] | +0.55 | +0.47 / +0.55 | both halves | 2e-05 | pathway: Extracellular matrix organization |
| [[DELEC1]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[MIR3681HG]] | +0.54 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[ARNT2]] | +0.54 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[SYTL2]] | +0.54 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[COL19A1]] | +0.54 | +0.48 / +0.53 | both halves | 2e-05 | pathway: Extracellular matrix organization |
| [[AIM2]] | +0.53 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[SETBP1]] | +0.53 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[NYAP2]] | +0.53 | +0.38 / +0.57 | both halves | 7e-05 |  |
| [[PTGS2]] | +0.52 | +0.51 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGO4]] | -0.50 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[FHIP2A]] | -0.47 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[ZNF594-DT]] | -0.47 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[NUDT2]] | -0.46 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[EGFL8]] | -0.45 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[PIK3CA]] | -0.45 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[MALSU1]] | -0.44 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[FBXL20]] | -0.44 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[CNNM2]] | -0.44 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[HINFP]] | -0.43 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[TFDP2]] | -0.43 | -0.37 / -0.47 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 3, C 16. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SHC4]] | B | SHC4 activity raises TNC's level | lines that do not express SHC4 (23) vs lines expressing it (27) | 4.26× lower at baseline in the lines without SHC4 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000250137, AR, GNG2; maybe low, not absent |
| [[MIR3681HG]] | B | MIR3681HG activity raises TNC's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 2.95× lower at baseline in the lines without MIR3681HG | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent |
| [[SHROOM4]] | B | SHROOM4 activity raises TNC's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 3.88× lower at baseline in the lines without SHROOM4 | 0.069 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539 |
| [[NRP2]] | C | NRP2 activity raises TNC's level | lines that do not express NRP2 (24) vs lines expressing it (26) | 5.26× lower at baseline in the lines without NRP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: NLRP1, RFX8, TNFAIP6; co-absent with the target |
| [[MILR1]] | C | MILR1 activity raises TNC's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 4.59× lower at baseline in the lines without MILR1 | 0.008 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1; co-absent with the target |
| [[PLPP4]] | C | PLPP4 activity raises TNC's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 4.78× lower at baseline in the lines without PLPP4 | 0.010 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6; co-absent with the target |
| [[FRMD4A]] | C | FRMD4A activity raises TNC's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 4.83× lower at baseline in the lines without FRMD4A | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |
| [[C1QTNF1]] | C | C1QTNF1 activity raises TNC's level | lines that do not express C1QTNF1 (20) vs lines expressing it (30) | 4.59× lower at baseline in the lines without C1QTNF1 | 0.015 | ⚠ within organs, on part of the lines; also absent: ZNF521, ENSG00000287622, SLC43A3; co-absent with the target |
| [[ITGB3]] | C | ITGB3 activity raises TNC's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 4.09× lower at baseline in the lines without ITGB3 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130; co-absent with the target |
| [[ADAMTS3]] | C | ADAMTS3 activity raises TNC's level | lines that do not express ADAMTS3 (23) vs lines expressing it (27) | 4.53× lower at baseline in the lines without ADAMTS3 | 0.035 | ⚠ within organs, on part of the lines; also absent: ARMCX1, EYA1, ENSG00000232949; co-absent with the target |
| [[FKBP9P1-1]] | C | FKBP9P1-1 activity raises TNC's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 4.25× lower at baseline in the lines without FKBP9P1-1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent; co-absent with the target |
| [[TIMP3]] | C | TIMP3 activity raises TNC's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 3.97× lower at baseline in the lines without TIMP3 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 5, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHST11]] | B | TNC activity raises CHST11's level | lines that do not express TNC (23) vs lines expressing it (27) | 2.97× lower at baseline in the lines without TNC | 0.034 | ⚠ within organs, on part of the lines; also absent: RDUR, RFX8, ENSG00000287622 |
| [[ZNF697]] | B | TNC activity raises ZNF697's level | lines that do not express TNC (23) vs lines expressing it (27) | 2.10× lower at baseline in the lines without TNC | 0.037 | ⚠ within organs, on part of the lines; also absent: RDUR, RFX8, ENSG00000287622 |
| [[CNNM2]] | B | TNC activity lowers CNNM2's level | lines that do not express TNC (23) vs lines expressing it (27) | 1.31× higher at baseline in the lines without TNC | 0.061 | ⚠ within organs, on part of the lines; also absent: RDUR, RFX8, ENSG00000287622 |
| [[ZPLD1]] | B | TNC activity raises ZPLD1's level | lines that do not express TNC (23) vs lines expressing it (27) | 1.75× lower at baseline in the lines without TNC | 0.087 | ⚠ within organs, on part of the lines; also absent: RDUR, RFX8, ENSG00000287622 |
| [[ALK]] | B | TNC activity raises ALK's level | lines that do not express TNC (23) vs lines expressing it (27) | 2.37× lower at baseline in the lines without TNC | 0.089 | ⚠ within organs, on part of the lines; also absent: RDUR, RFX8, ENSG00000287622 |
| [[AIM2]] | C | TNC activity raises AIM2's level | lines that do not express TNC (23) vs lines expressing it (27) | 3.28× lower at baseline in the lines without TNC | 0.013 | ⚠ within organs, on part of the lines; also absent: RDUR, RFX8, ENSG00000287622; co-absent with the target |
| [[KCNQ3]] | C | TNC activity raises KCNQ3's level | lines that do not express TNC (23) vs lines expressing it (27) | 2.71× lower at baseline in the lines without TNC | 0.032 | ⚠ within organs, on part of the lines; also absent: RDUR, RFX8, ENSG00000287622; co-absent with the target |
| [[CTHRC1]] | C | TNC activity raises CTHRC1's level | lines that do not express TNC (23) vs lines expressing it (27) | 2.79× lower at baseline in the lines without TNC | 0.045 | ⚠ within organs, on part of the lines; also absent: RDUR, RFX8, ENSG00000287622; co-absent with the target |
| [[CDK15]] | C | TNC activity raises CDK15's level | lines that do not express TNC (23) vs lines expressing it (27) | 2.12× lower at baseline in the lines without TNC | 0.050 | ⚠ within organs, on part of the lines; also absent: RDUR, RFX8, ENSG00000287622; co-absent with the target |
| [[NRP2]] | C | TNC activity raises NRP2's level | lines that do not express TNC (23) vs lines expressing it (27) | 3.35× lower at baseline in the lines without TNC | 0.088 | ⚠ within organs, on part of the lines; also absent: RDUR, RFX8, ENSG00000287622; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.504). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.2, 18.6); signed map (28.0, 35.8). **Vector** length 106, 33.6% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.5 | +14.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.8 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +6.6 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +1.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.2 | +6.2 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +4.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.9 | +3.8 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -2.5 | -4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.3 | -4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.0 | -8.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -2.0 | -4.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | tenascin C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.1 — chr9:115,019,575-115,118,207 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TN, MGC167029; previously HXB, DFNA56 |
| Gene groups (HGNC) | Tenascins |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 7 pathways, smallest: Syndecan interactions; ECM proteoglycans; Integrin cell surface interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [P24821](https://www.uniprot.org/uniprotkb/P24821) (Tenascin):

> Extracellular matrix protein implicated in guidance of migrating neurons as well as axons during development, synaptic plasticity as well as neuronal regeneration. Promotes neurite outgrowth from cortical neurons grown on a monolayer of astrocytes. Ligand for integrins alpha-8/beta-1, alpha-9/beta-1, alpha-V/beta-3 and alpha-V/beta-6. In tumors, stimulates angiogenesis by elongation, migration and sprouting of endothelial cells.

**Summary**, from NCBI Gene [3371](https://www.ncbi.nlm.nih.gov/gene/3371):

> This gene encodes an extracellular matrix protein with a spatially and temporally restricted tissue distribution. This protein is homohexameric with disulfide-linked subunits, and contains multiple EGF-like and fibronectin type-III domains. It is implicated in guidance of migrating neurons as well as axons during development, synaptic plasticity, and neuronal regeneration. [provided by RefSeq, Jul 2011]

**Accessions** — [HGNC:5318](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5318) · Entrez [3371](https://www.ncbi.nlm.nih.gov/gene/3371) · UniProt [P24821](https://www.uniprot.org/uniprotkb/P24821) · Ensembl [ENSG00000041982](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000041982)

## Data

Gene col 479: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 479); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 479, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 479]; `tensor/DDL_lfc|DDL_z.npy` [479]; `embed/gene_vectors.npy` [479]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 479 or target_col == 479). Every well: [[TNC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
