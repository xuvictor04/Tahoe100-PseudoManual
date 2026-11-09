---
symbol: "SEC31B"
type: "gene"
col: 1133
ensembl_id: "ENSG00000075826"
name: "SEC31 homolog B, COPII component"
location: "10q24.31"
module: 105
arm: "+"
pooled_cpm: 15.96
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 11
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# SEC31B

*SEC31 homolog B, COPII component* — 10q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.96× (z +10.5, q 4e-23, up in 26 of 42 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.74× (z +9.0, q 8e-17, up in 30 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.583× (z -8.4, q 2e-14, down in 25 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHRS13]] (+0.68, fdr 7e-06), [[FNTB]] (+0.68, fdr 1e-05), [[CRYBB2P1-1]] (+0.63, fdr 9e-06); moves opposite to [[TJP1]] (-0.50, fdr 4e-05), [[SH3D19]] (-0.47, fdr 3e-05), [[RABGAP1L]] (-0.47, fdr 1e-04).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GPR155]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1133.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +10.5 | 4e-23 | 26/42 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +9.0 | 8e-17 | 30/46 (HOP62, NCI-H23, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.67×** | +8.3 | 2e-14 | 35/47 (A-172, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +6.5 | 1e-08 | 17/46 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +5.9 | 3e-07 | 21/47 (A498, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.40×** | +5.5 | 3e-06 | 18/46 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +5.5 | 4e-06 | 18/45 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +5.2 | 2e-05 | 13/46 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.25×** | +5.1 | 2e-05 | 14/47 (HEC-1-A, C32, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +4.9 | 6e-05 | 21/46 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Afatinib (drug)]] 5 µM |  | **1.30×** | +4.4 | 5e-04 | 12/47 (SW480, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.30×** | +4.3 | 9e-04 | 8/45 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +4.1 | 0.002 | 16/46 (Panc 03.27, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.1 | 0.002 | 15/47 (NCI-H2030, NCI-H2347, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.18× | +3.8 | 0.005 | 7/47 (BT-474, LS 180, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.012 | 7/46 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.022 | 10/43 (A-172, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.079 | 5/46 (NCI-H23, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1133.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.583×** | -8.4 | 2e-14 | 25/46 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.657×** | -6.8 | 3e-09 | 21/39 (C32, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.698×** | -5.8 | 1e-06 | 19/46 (C32, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.698×** | -5.8 | 1e-06 | 21/43 (C32, SNU-423, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.759×** | -4.5 | 9e-04 | 17/46 (hTERT-HPNE, RPMI-7951, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.765×** | -4.4 | 0.001 | 19/46 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.797×** | -3.7 | 0.017 | 15/46 (C32, SNU-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.791×** | -3.7 | 0.017 | 7/25 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.857× | -3.5 | 0.025 | 21/46 (C32, CFPAC-1, …) | all doses, flat | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.801×** | -3.5 | 0.031 | 17/45 (C32, NCI-H1792, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.743×** | -3.4 | 0.031 | 10/44 (HCT15, H4, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.871× | -3.2 | 0.074 | 3/47 (PANC-1, KATO III, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.826×** | -3.1 | 0.083 | 8/47 (NCI-H1573, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1133. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 107 | 0 | 16 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0490× (z -25.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.261× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 11.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.04× (z +9.4) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 21.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0587× (z -14.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 14.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -10.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -9.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 41.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -14.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 8.45 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.121× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Torkinib (drug)]] 5 µM 0.0735× (z -8.6) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.346× (z -9.9) ⚠ transcription drop; cell-cycle shift, explains ~53% of this change |
| [[SHP-77 (line)]] | alt | 10.5 | 0 | 1 | — | [[9-ING-41 (drug)]] 0.5 µM 0.0782× (z -8.6) |
| [[SNU-1 (line)]] | wt | 26.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.127× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~93% of this change |
| [[SNU-423 (line)]] | alt | 22.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.00 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1133), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHRS13]] | +0.68 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[FNTB]] | +0.68 | +0.76 / +0.55 | both halves | 1e-05 |  |
| [[CRYBB2P1-1]] | +0.63 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[POM121C]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[EFCAB3P1]] | +0.62 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[TRMU]] | +0.58 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[POM121]] | +0.57 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[TMEM14B]] | +0.57 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[PMS2CL]] | +0.57 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[ATPAF2]] | +0.56 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[TRIT1]] | +0.55 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[SAP30-DT]] | +0.55 | +0.61 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TJP1]] | -0.50 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[SH3D19]] | -0.47 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[RABGAP1L]] | -0.47 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[RFFL]] | -0.46 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[PPM1L]] | -0.44 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[JADE3]] | -0.44 | -0.45 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR155]] | B | GPR155 activity raises SEC31B's level | lines that do not express GPR155 (6) vs lines expressing it (44) | 2.06× lower at baseline in the lines without GPR155 | 0.015 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PKIG, TBC1D19; maybe low, not absent |
| [[C4orf47]] | C | C4orf47 activity raises SEC31B's level | lines that do not express C4orf47 (3) vs lines expressing it (47) | 2.11× lower at baseline in the lines without C4orf47 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.674). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.4, -20.4); signed map (-40.1, 22.1). **Vector** length 95.8, 20.4% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.4 | +9.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.9 | +10.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.7 | +8.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +3.6 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +3.0 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +5.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +5.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +1.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.4 | -8.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.8 | -5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.8 | -3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.8 | -5.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -4.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.7 | -3.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | SEC31 homolog B, COPII component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.31 — chr10:100,486,646-100,519,864 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SEC31B-1, DKFZP434M183; previously SEC31L2 |
| Gene groups (HGNC) | WD repeat domain containing; Coat protein complex II |
| Reactome | 6 pathways, smallest: COPII-mediated vesicle transport; ER to Golgi Anterograde Transport; Transport to the Golgi and subsequent modification |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQW1](https://www.uniprot.org/uniprotkb/Q9NQW1) (Protein transport protein Sec31B):

> As a component of the coat protein complex II (COPII), may function in vesicle budding and cargo export from the endoplasmic reticulum.

**Summary**, from NCBI Gene [25956](https://www.ncbi.nlm.nih.gov/gene/25956):

> This gene encodes a protein of unknown function. The protein has moderate similarity to rat VAP1 protein which is an endosomal membrane-associated protein, containing a putative Ca2+/calmodulin-dependent kinase II phosphorylation site. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:23197](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23197) · Entrez [25956](https://www.ncbi.nlm.nih.gov/gene/25956) · UniProt [Q9NQW1](https://www.uniprot.org/uniprotkb/Q9NQW1) · Ensembl [ENSG00000075826](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075826)

## Data

Gene col 1133: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1133); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1133, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1133]; `tensor/DDL_lfc|DDL_z.npy` [1133]; `embed/gene_vectors.npy` [1133]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1133 or target_col == 1133). Every well: [[SEC31B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC31B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
