---
symbol: "B4GALT2"
type: "gene"
col: 3905
ensembl_id: "ENSG00000117411"
name: "beta-1,4-galactosyltransferase 2"
location: "1p34.1"
module: 36
arm: "+"
pooled_cpm: 13.44
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# B4GALT2

*beta-1,4-galactosyltransferase 2* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.71× (z +10.6, q 1e-23, up in 32 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 1.90× (z +4.0, q 0.007, up in 18 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.412× (z -13.5, q 1e-38, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRM]] (+0.76, fdr 7e-06), [[VKORC1L1]] (+0.70, fdr 7e-06), [[TIMM23B]] (+0.67, fdr 7e-06); moves opposite to [[SDCBP]] (-0.56, fdr 1e-05), [[MED29]] (-0.52, fdr 2e-05), [[BROX]] (-0.51, fdr 5e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADCY3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3905.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.71×** | +10.6 | 1e-23 | 32/36 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.63×** | +9.9 | 8e-21 | 19/23 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +8.1 | 1e-13 | 25/29 (Panc 03.27, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.52×** | +4.4 | 0.001 | 22/42 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **1.90×** | +4.0 | 0.007 | 18/43 (MIA PaCa-2, NCI-H460, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.41×** | +3.7 | 0.023 | 20/47 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.039 | 12/46 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.74×** | +3.5 | 0.039 | 10/47 (KATO III, HT-29, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.056 | 10/44 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.69×** | +3.3 | 0.056 | 11/42 (SHP-77, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.083 | 12/46 (HT-29, J82, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.64×** | +3.1 | 0.089 | 6/45 (SNU-423, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3905.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.412×** | -13.5 | 1e-38 | 39/47 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.532×** | -6.5 | 1e-08 | 29/47 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.546×** | -6.5 | 1e-08 | 29/48 (LoVo, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.559×** | -6.3 | 6e-08 | 28/48 (A498, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.570×** | -6.0 | 2e-07 | 26/47 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.636×** | -4.9 | 1e-04 | 25/47 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.729×** | -4.8 | 1e-04 | 24/48 (H4, MIA PaCa-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.735×** | -4.7 | 2e-04 | 21/47 (J82, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.772×** | -3.9 | 0.005 | 20/46 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.718×** | -3.6 | 0.020 | 20/45 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.726×** | -3.2 | 0.072 | 11/48 (A498, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3905. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 18.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -8.5) |
| [[A-427 (line)]] | wt | 17.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.164× (z -10.4) |
| [[J82 (line)]] | alt | 18.9 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.213× (z -14.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.264× (z -12.3) |
| [[LOX-IMVI (line)]] | wt | 12.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -11.4) |
| [[MIA PaCa-2 (line)]] | alt | 17.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 10.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.38× (z +9.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 14.5 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -9.4) |
| [[BT-474 (line)]] | alt | 4.99 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0977× (z -10.4) |
| [[C-33 A (line)]] | alt | 19.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 17.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -11.7) |
| [[HOP62 (line)]] | alt | 16.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -15.3) |
| [[hTERT-HPNE (line)]] | wt | 19.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -8.8) |
| [[LoVo (line)]] | wt | 11.3 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.209× (z -8.9) |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 10.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -12.1) |
| [[SNU-1 (line)]] | wt | 18.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -10.0) |
| [[SW1417 (line)]] | alt | 8.87 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -9.2) |
| [[SW480 (line)]] | alt | 9.43 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -9.1) |
| [[A-172 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3905), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRM]] | +0.76 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[VKORC1L1]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[TIMM23B]] | +0.67 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ATAD3B]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[ATAD3A]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[HIRA]] | +0.62 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[TRIM27]] | +0.62 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[ZMYND19]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[NDUFAF2]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[NT5DC2]] | +0.60 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[SIMC1]] | +0.60 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[TIMM23]] | +0.60 | +0.52 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDCBP]] | -0.56 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[MED29]] | -0.52 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[BROX]] | -0.51 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[ZNF436]] | -0.51 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[THAP9]] | -0.50 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ARMT1]] | -0.50 | -0.45 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY3]] | B | ADCY3 activity raises B4GALT2's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.45× lower at baseline in the lines without ADCY3 | 0.004 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[ANKRD13B]] | C | ANKRD13B activity raises B4GALT2's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 1.91× lower at baseline in the lines without ANKRD13B | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.639). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-5.2, -28.7); signed map (-45.6, -18.6). **Vector** length 68.4, 13.6% of its response variance represented; |z| ≥ 3 in 753 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.9 | +2.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | -0.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +9.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.2 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +1.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.9 | -6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.6 | -13.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.3 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | beta-1,4-galactosyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:43,978,943-43,991,170 (+) |
| Ensembl biotype | protein_coding |
| Also known as | beta4Gal-T2 |
| Gene groups (HGNC) | Beta 4-glycosyltransferases |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 8 pathways, smallest: N-Glycan antennae elongation; Keratan sulfate biosynthesis; N-glycan antennae elongation in the medial/trans-Golgi |
| Matched by | ensembl_id |

**Function**, from UniProt [O60909](https://www.uniprot.org/uniprotkb/O60909) (Beta-1,4-galactosyltransferase 2):

> Responsible for the synthesis of complex-type N-linked oligosaccharides in many glycoproteins as well as the carbohydrate moieties of glycolipids. Can produce lactose.

**Summary**, from NCBI Gene [8704](https://www.ncbi.nlm.nih.gov/gene/8704):

> This gene is one of seven beta-1,4-galactosyltransferase (beta4GalT) genes. They encode type II membrane-bound glycoproteins that appear to have exclusive specificity for the donor substrate UDP-galactose; all transfer galactose in a beta1,4 linkage to similar acceptor sugars: GlcNAc, Glc, and Xyl. Each beta4GalT has a distinct function in the biosynthesis of different glycoconjugates and saccharide structures. As type II membrane proteins, they have an N-terminal hydrophobic signal sequence …

**Accessions** — [HGNC:925](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:925) · Entrez [8704](https://www.ncbi.nlm.nih.gov/gene/8704) · UniProt [O60909](https://www.uniprot.org/uniprotkb/O60909) · Ensembl [ENSG00000117411](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117411)

## Data

Gene col 3905: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3905); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3905, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3905]; `tensor/DDL_lfc|DDL_z.npy` [3905]; `embed/gene_vectors.npy` [3905]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3905 or target_col == 3905). Every well: [[B4GALT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B4GALT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
