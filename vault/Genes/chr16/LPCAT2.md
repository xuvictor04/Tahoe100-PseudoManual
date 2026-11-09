---
symbol: "LPCAT2"
type: "gene"
col: 1492
ensembl_id: "ENSG00000087253"
name: "lysophosphatidylcholine acyltransferase 2"
location: "16q12.2"
module: 88
arm: "-"
pooled_cpm: 49.49
n_lines_expressing: 41
n_dd_up: 11
n_dd_down: 15
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 7
direction_downstream: 4
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# LPCAT2

*lysophosphatidylcholine acyltransferase 2* — 16q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.76× (z +18.6, q 0e+00, up in 33 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.601× (z -11.4, q 3e-27, down in 28 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGSM1]] (+0.70, fdr 1e-05), [[FCHO1]] (+0.64, fdr 4e-05), [[UBA6]] (+0.62, fdr 9e-05); moves opposite to [[EFCAB2]] (-0.67, fdr 1e-05), [[INO80D]] (-0.65, fdr 2e-05), [[ZNF689]] (-0.65, fdr 1e-05).
> It sits in the **-** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SH3GL3]] → it (grade B ⚠); 4 go from it, the strongest it → [[GUCY1B1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1492.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.76×** | +18.6 | 0e+00 | 33/39 (KATO III, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.12×** | +17.5 | 0e+00 | 31/39 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.07×** | +16.9 | 0e+00 | 35/39 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.00×** | +16.1 | 0e+00 | 32/39 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.85×** | +14.4 | 1e-44 | 35/39 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.82×** | +14.0 | 1e-42 | 33/39 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +10.0 | 8e-22 | 21/38 (NCI-H1792, HS-578T, …) | two highest doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +9.0 | 2e-17 | 26/39 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.92×** | +7.9 | 1e-13 | 27/39 (NCI-H2030, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +7.4 | 6e-12 | 16/30 (A498, HS-578T, …) | two highest doses | cell-cycle shift (explains ~6% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.17× | +5.3 | 6e-06 | 17/39 (RKO, HOP62, …) | rises with dose | low cells (technical?) |
| [[Rifaximin (drug)]] 5 µM |  | **1.21×** | +4.3 | 8e-04 | 10/39 (NCI-H2030, NCI-H1573, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.19× | +4.0 | 0.003 | 13/39 (SK-MEL-2, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.16× | +3.5 | 0.019 | 9/39 (RKO, A-172, …) | rises with dose |  |
| [[Rifaximin (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.019 | 6/39 (SNU-423, A-427, …) | rises with dose | position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.025 | 9/39 (SW 900, Panc 03.27, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.11× | +3.4 | 0.025 | 4/39 (RPMI-7951, hTERT-HPNE, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | 1.15× | +3.4 | 0.025 | 9/39 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.09× | +3.0 | 0.089 | 3/40 (SNU-423, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1492.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.601×** | -11.4 | 3e-27 | 28/39 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.623×** | -11.0 | 1e-25 | 27/39 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.724×** | -10.6 | 5e-24 | 25/39 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.695×** | -8.4 | 5e-15 | 24/39 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.708×** | -8.0 | 1e-13 | 21/39 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -6.3 | 3e-08 | 1/40 (SW 1271) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.767×** | -6.1 | 7e-08 | 20/39 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.782×** | -5.7 | 8e-07 | 18/39 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~11% of this change | **0.805×** | -5.0 | 3e-05 | 18/37 (SW480, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **0.673×** | -4.8 | 9e-05 | 16/38 (SW480, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.864× | -4.8 | 9e-05 | 13/39 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.824×** | -4.5 | 4e-04 | 16/39 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.696×** | -4.4 | 5e-04 | 15/40 (LS 180, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | **0.828×** | -4.2 | 0.001 | 14/38 (PANC-1, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.722×** | -3.9 | 0.003 | 16/38 (KATO III, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.840× | -3.9 | 0.004 | 15/39 (SK-MEL-2, HEC-1-A, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | 0.847× | -3.8 | 0.004 | 15/39 (HOP62, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.842× | -3.8 | 0.006 | 13/38 (SW480, A-172, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.746×** | -3.6 | 0.010 | 10/37 (C-33 A, HCT15, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1492. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 39.8 | 6 | 1 | [[Belinostat (drug)]] 5 µM 3.36× (z +11.2) | [[Harringtonine (drug)]] 5 µM 0.376× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 29.6 | 6 | 1 | [[Tucidinostat (drug)]] 5 µM 2.27× (z +11.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.380× (z -9.7) |
| [[LS 180 (line)]] | wt | 49.0 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 2.28× (z +11.4) | — |
| [[NCI-H23 (line)]] | alt | 32.7 | 2 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.79× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -22.0) |
| [[A498 (line)]] | wt | 21.9 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.19× (z +12.8) | — |
| [[KATO III (line)]] | alt | 52.7 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 2.25× (z +12.0) | — |
| [[NCI-H1792 (line)]] | alt | 40.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.91× (z +13.7) | — |
| [[SW 900 (line)]] | alt | 50.8 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 2.10× (z +9.6) | — |
| [[A-427 (line)]] | wt | 41.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -23.6) |
| [[HS-578T (line)]] | alt | 58.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.71× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.291× (z -11.4) |
| [[LoVo (line)]] | wt | 47.9 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.334× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 74.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 125 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.48× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 13.1 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 3.01× (z +10.9) | — |
| [[RKO (line)]] | wt | 43.9 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.319× (z -9.4) |
| [[SW1417 (line)]] | alt | 93.7 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 1.91× (z +10.2) | — |
| [[A-172 (line)]] | wt | 105 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.214× (z -10.4) |
| [[J82 (line)]] | alt | 22.9 | 2 | 0 | [[Belinostat (drug)]] 5 µM 3.81× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 93.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -14.0) |
| [[A549 (line)]] | wt | 25.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.51× (z +9.3) | — |
| [[CHP-212 (line)]] | wt | 33.8 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.0932× (z -8.5) |
| [[HCT15 (line)]] | alt | 49.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 35.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.426× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 65.4 | 0 | 1 | — | [[vincristine (drug)]] 5 µM 0.0678× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 181 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 73.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -16.1) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 73.5 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 5 µM 0.0754× (z -8.7) |
| [[SW48 (line)]] | wt | 16.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 68.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.386× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~11% of this change |
| [[AN3 CA (line)]] | alt | 7.56 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.68 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.39 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 78.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.15 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.23 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.19 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1492), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGSM1]] | +0.70 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[FCHO1]] | +0.64 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[UBA6]] | +0.62 | +0.64 / +0.36 | both halves | 9e-05 |  |
| [[SEPTIN6]] | +0.62 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[CALB2]] | +0.62 | +0.65 / +0.54 | both halves | 1e-05 | same gene group |
| [[AZIN2]] | +0.62 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[GALNT12]] | +0.61 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[INPP5F]] | +0.61 | +0.54 / +0.42 | both halves | 4e-05 | pathway: Phospholipid metabolism |
| [[WASF3]] | +0.61 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[RIMS3]] | +0.61 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[SH3GL3]] | +0.61 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[TMOD2]] | +0.60 | +0.40 / +0.51 | both halves | 5e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB2]] | -0.67 | -0.60 / -0.55 | both halves | 1e-05 | same gene group |
| [[INO80D]] | -0.65 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[ZNF689]] | -0.65 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[MCPH1]] | -0.65 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[ZFX]] | -0.64 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[ARFGAP2]] | -0.64 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[PEF1]] | -0.63 | -0.53 / -0.53 | both halves | 1e-05 | same gene group |
| [[ZNF747]] | -0.62 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[FIZ1]] | -0.62 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[WDR33]] | -0.62 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[CREBBP]] | -0.61 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[CFLAR]] | -0.60 | -0.54 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SH3GL3]] | B | SH3GL3 activity raises LPCAT2's level | lines that do not express SH3GL3 (21) vs lines expressing it (29) | 1.47× lower at baseline in the lines without SH3GL3 | 0.027 | ⚠ within organs, on part of the lines; also absent: S1PR3, SPANXA2-OT1, SALL1 |
| [[TRIM9]] | B | TRIM9 activity raises LPCAT2's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 1.91× lower at baseline in the lines without TRIM9 | 0.068 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1 |
| [[GUCY1B1]] | B | GUCY1B1 activity raises LPCAT2's level | lines that do not express GUCY1B1 (25) vs lines expressing it (25) | 1.76× lower at baseline in the lines without GUCY1B1 | 0.075 | ⚠ within organs, on part of the lines; also absent: FAP, STAC, SALL1 |
| [[ANOS1]] | B | ANOS1 activity raises LPCAT2's level | lines that do not express ANOS1 (31) vs lines expressing it (19) | 1.34× lower at baseline in the lines without ANOS1 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000268119, ZYG11A, KRT7 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers LPCAT2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers LPCAT2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DYNLT3]] | C | DYNLT3 activity raises LPCAT2's level | lines that do not express DYNLT3 (4) vs lines expressing it (46) | 4.97× lower at baseline in the lines without DYNLT3 | 0.036 | ⚠ few lines (4 vs 46); across organs; also absent: PLEKHA5, LRRCC1, RGL1 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GUCY1B1]] | B | LPCAT2 activity raises GUCY1B1's level | lines that do not express LPCAT2 (9) vs lines expressing it (41) | 2.06× lower at baseline in the lines without LPCAT2 | 0.038 | ⚠ within organs, on part of the lines; also absent: E2F7, PARD3B |
| [[PIK3CD]] | B | LPCAT2 activity raises PIK3CD's level | lines that do not express LPCAT2 (9) vs lines expressing it (41) | 1.32× lower at baseline in the lines without LPCAT2 | 0.056 | ⚠ within organs, on part of the lines; also absent: E2F7, PARD3B |
| [[CYRIA]] | B | LPCAT2 activity raises CYRIA's level | lines that do not express LPCAT2 (9) vs lines expressing it (41) | 2.17× lower at baseline in the lines without LPCAT2 | 0.069 | ⚠ within organs, on part of the lines; also absent: E2F7, PARD3B |
| [[PLCG2]] | B | LPCAT2 activity strengthens PLCG2's drug response | lines that do not express LPCAT2 (7) vs lines expressing it (31) | the lines without LPCAT2 respond 0.70× as strongly (z diff +1.01); strongest at Tucidinostat 5 µM: 1.21x vs 1.86x (z diff +2.8) | 0.096 | ⚠ within organs, on part of the lines; also absent: E2F7, PARD3B; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **-** arm (projection on the module's main direction -0.628). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (3.4, 8.1); signed map (-21.0, 30.3). **Vector** length 107, 25.2% of its response variance represented; |z| ≥ 3 in 1,191 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.4 | +18.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.9 | +14.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.2 | +14.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.5 | +16.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +10.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.0 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.7 | +4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +2.0 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.9 | -8.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.9 | -11.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.7 | -11.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.4 | -10.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -2.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.2 | -4.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.1 | -4.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | lysophosphatidylcholine acyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.2 — chr16:55,509,072-55,586,666 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20481, AGPAT11, LysoPAFAT, LPLAT9; previously AYTL1 |
| Gene groups (HGNC) | 1-acylglycerol-3-phosphate O-acyltransferases; EF-hand domain containing; Lysophospholipid acyltransferases |
| Reactome | 4 pathways, smallest: Acyl chain remodelling of PC; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L5N7](https://www.uniprot.org/uniprotkb/Q7L5N7) (Lysophosphatidylcholine acyltransferase 2):

> Exhibits both acyltransferase and acetyltransferase activities. Catalyzes the conversion of lysophosphatidylcholine (1-acyl-sn-glycero-3-phosphocholine or LPC) into phosphatidylcholine (1,2-diacyl-sn-glycero-3-phosphocholine or PC). Catalyzes the conversion 1-acyl-sn-glycerol-3-phosphate (lysophosphatidic acid or LPA) into 1,2-diacyl-sn-glycerol-3-phosphate (phosphatidic acid or PA) by incorporating an acyl moiety at the sn-2 position of the glycerol backbone. Involved in platelet-activating …

**Summary**, from NCBI Gene [54947](https://www.ncbi.nlm.nih.gov/gene/54947):

> This gene encodes a member of the lysophospholipid acyltransferase family. The encoded enzyme may function in two ways: to catalyze the biosynthesis of platelet-activating factor (1-O-alkyl-2-acetyl-sn-glycero-3-phosphocholine) from 1-O-alkyl-sn-glycero-3-phosphocholine, and to catalyze the synthesis of glycerophospholipid precursors from arachidonyl-CoA and lysophosphatidylcholine. The encoded protein may function in membrane biogenesis and production of platelet-activating factor in …

**Accessions** — [HGNC:26032](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26032) · Entrez [54947](https://www.ncbi.nlm.nih.gov/gene/54947) · UniProt [Q7L5N7](https://www.uniprot.org/uniprotkb/Q7L5N7) · Ensembl [ENSG00000087253](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087253)

## Data

Gene col 1492: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1492); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1492, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1492]; `tensor/DDL_lfc|DDL_z.npy` [1492]; `embed/gene_vectors.npy` [1492]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1492 or target_col == 1492). Every well: [[LPCAT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LPCAT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
