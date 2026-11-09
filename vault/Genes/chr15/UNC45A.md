---
symbol: "UNC45A"
type: "gene"
col: 6431
ensembl_id: "ENSG00000140553"
name: "unc-45 myosin chaperone A"
location: "15q26.1"
module: 30
arm: "+"
pooled_cpm: 29.73
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# UNC45A

*unc-45 myosin chaperone A* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.84× (z +8.5, q 2e-14, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.604× (z -9.9, q 3e-20, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBCB]] (+0.79, fdr 7e-06), [[DPY30]] (+0.76, fdr 7e-06), [[MGST3]] (+0.76, fdr 7e-06); moves opposite to [[CYREN]] (-0.66, fdr 3e-05), [[ST7L]] (-0.66, fdr 2e-05), [[LEKR1]] (-0.66, fdr 3e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TENM3-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6431.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.84×** | +8.5 | 2e-14 | 39/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.73×** | +7.6 | 8e-12 | 36/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +6.0 | 4e-07 | 37/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.77×** | +5.6 | 3e-06 | 37/48 (HEC-1-A, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +5.4 | 9e-06 | 36/48 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +5.2 | 2e-05 | 3/48 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +5.0 | 4e-05 | 30/48 (HOP62, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.59×** | +4.6 | 4e-04 | 28/48 (HT-29, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +4.0 | 0.004 | 22/48 (HOP62, A-427, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.023 | 21/47 (SW480, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.028 | 21/48 (HOP62, Hs 766T, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +3.4 | 0.028 | 20/47 (SHP-77, RKO, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.28×** | +3.4 | 0.029 | 20/46 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | **1.27×** | +3.3 | 0.044 | 22/42 (PANC-1, A-427, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | **1.27×** | +3.1 | 0.066 | 14/36 (SW480, AsPC-1, …) | rises with dose | composition shift |
| [[Thymol (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.072 | 12/47 (hTERT-HPNE, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6431.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.604×** | -9.9 | 3e-20 | 35/47 (H4, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.619×** | -5.2 | 5e-05 | 32/47 (NCI-H2347, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.704×** | -4.7 | 6e-04 | 26/48 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -3.1 | 0.30 | 19/48 (HOP62, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6431. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 36.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.455× (z -10.2) |
| [[SNU-1 (line)]] | wt | 28.4 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0818× (z -12.0) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.264× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 32.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -10.8) |
| [[H4 (line)]] | wt | 34.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0919× (z -18.9) |
| [[HCT15 (line)]] | alt | 45.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -9.1) |
| [[HS-578T (line)]] | alt | 26.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 28.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -12.2) |
| [[NCI-H23 (line)]] | alt | 23.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 35.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -9.4) |
| [[PANC-1 (line)]] | alt | 26.9 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.38× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 29.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -8.7) |
| [[SW48 (line)]] | wt | 48.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[A-172 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 26.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6431), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCB]] | +0.79 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[DPY30]] | +0.76 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[MGST3]] | +0.76 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[FBXO44]] | +0.75 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[SNX1]] | +0.72 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[MKRN2]] | +0.71 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[FLYWCH2]] | +0.71 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.71 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[MRGBP]] | +0.71 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[SHARPIN]] | +0.70 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[SLC9A6]] | +0.70 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[ATPAF2]] | +0.70 | +0.73 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYREN]] | -0.66 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[ST7L]] | -0.66 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[LEKR1]] | -0.66 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[ARAP2]] | -0.66 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.65 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[PSMD6-AS1]] | -0.63 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | -0.62 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[TASOR]] | -0.62 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[ZC3H4]] | -0.61 | -0.57 / -0.39 | both halves | 6e-05 | same gene group |
| [[TUG1]] | -0.61 | -0.55 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TENM3-AS1]] | B | TENM3-AS1 activity weakens UNC45A's drug response | lines that do not express TENM3-AS1 (19) vs lines expressing it (29) | the lines without TENM3-AS1 respond 1.16× as strongly (z diff -0.37); strongest at Panobinostat 5 µM: 2.08x vs 1.65x (z diff -1.4) | 0.080 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[HACE1]] | C | HACE1 activity raises UNC45A's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 1.38× lower at baseline in the lines without HACE1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.859). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (0.7, -5.5); signed map (-34.6, -3.5). **Vector** length 99.2, 26.4% of its response variance represented; |z| ≥ 3 in 649 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.5 | +7.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.3 | +5.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.1 | +8.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.9 | +6.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.8 | +5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.6 | +5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.5 | +4.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +3.4 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.1 | +3.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.8 | +3.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.5 | -9.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.3 | -5.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | -3.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | unc-45 myosin chaperone A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:90,930,180-90,954,093 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SMAP-1, GC-UNC45 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3U1](https://www.uniprot.org/uniprotkb/Q9H3U1) (Protein unc-45 homolog A):

> Acts as a co-chaperone for HSP90. Prevents the stimulation of HSP90AB1 ATPase activity by AHSA1. Positive factor in promoting PGR function in the cell. May be necessary for proper folding of myosin (Potential). Necessary for normal cell proliferation. Necessary for normal myotube formation and myosin accumulation during muscle cell development. May play a role in erythropoiesis in stroma cells in the spleen (By similarity).

**Summary**, from NCBI Gene [55898](https://www.ncbi.nlm.nih.gov/gene/55898):

> This gene encodes a regulatory component of the progesterone receptor/heat shock protein 90 chaperoning complex, which functions in the assembly and folding of the progesterone receptor. The encoded protein is thought to be essential for normal cell proliferation, and for the accumulation of myosin during development of muscle cells. [provided by RefSeq, Sep 2018]

**Accessions** — [HGNC:30594](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30594) · Entrez [55898](https://www.ncbi.nlm.nih.gov/gene/55898) · UniProt [Q9H3U1](https://www.uniprot.org/uniprotkb/Q9H3U1) · Ensembl [ENSG00000140553](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140553)

## Data

Gene col 6431: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6431); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6431, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6431]; `tensor/DDL_lfc|DDL_z.npy` [6431]; `embed/gene_vectors.npy` [6431]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6431 or target_col == 6431). Every well: [[UNC45A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UNC45A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
