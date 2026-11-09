---
symbol: "SLC27A4"
type: "gene"
col: 9421
ensembl_id: "ENSG00000167114"
name: "solute carrier family 27 member 4"
location: "9q34.11"
module: 2
arm: "+"
pooled_cpm: 12.0
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 6
n_dd_up_clean: 16
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# SLC27A4

*solute carrier family 27 member 4* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (18 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.38× (z +13.7, q 8e-40, up in 41 of 47 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.73× (z +12.3, q 3e-32, up in 34 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.724× (z -7.2, q 3e-10, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOXK2]] (+0.67, fdr 7e-06), [[SGPP1]] (+0.67, fdr 7e-06), [[CORO7]] (+0.66, fdr 7e-06); moves opposite to [[NDUFA5]] (-0.66, fdr 7e-06), [[RBM7]] (-0.63, fdr 1e-05), [[BDH2]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BHLHE41]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SVIL-AS1-1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9421.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.38×** | +13.7 | 8e-40 | 41/47 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +12.3 | 3e-32 | 34/45 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.14×** | +12.0 | 7e-31 | 37/47 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.12×** | +11.9 | 2e-30 | 39/47 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.79×** | +9.2 | 6e-18 | 34/47 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +8.5 | 2e-15 | 29/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +7.7 | 8e-13 | 29/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.67×** | +6.9 | 3e-10 | 27/40 (SW480, LoVo, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.63×** | +6.6 | 3e-09 | 25/45 (A498, NCI-H460, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.31×** | +6.0 | 9e-08 | 20/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.42×** | +5.5 | 2e-06 | 18/47 (LS 180, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +5.4 | 3e-06 | 20/47 (SW480, SW48, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.40×** | +5.3 | 5e-06 | 19/44 (HEC-1-A, SW1417, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.37×** | +5.0 | 3e-05 | 13/45 (A549, NCI-H2030, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.33×** | +4.5 | 2e-04 | 17/47 (KATO III, NCI-H23, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +4.5 | 2e-04 | 7/47 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +3.9 | 0.002 | 10/47 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.011 | 11/47 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.011 | 11/47 (A549, J82, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.012 | 7/47 (NCI-H460, SW480, …) | rises with dose |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.027 | 8/47 (A549, HEC-1-A, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.051 | 8/47 (A498, NCI-H460, …) | top dose only |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.21×** | +2.9 | 0.057 | 5/45 (LoVo, Panc 03.27, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9421.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.724×** | -7.2 | 3e-10 | 25/47 (SK-MEL-2, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.733×** | -7.0 | 9e-10 | 29/46 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.456×** | -6.5 | 1e-08 | 25/47 (RKO, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.770×** | -3.5 | 0.057 | 11/45 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.806×** | -3.4 | 0.068 | 14/44 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.784×** | -3.3 | 0.093 | 14/46 (SK-MEL-2, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.680× | -3.2 | 0.11 | 11/42 (SW48, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9421. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 24.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -13.0) |
| [[J82 (line)]] | alt | 20.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -8.7) |
| [[A-172 (line)]] | wt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -14.1) |
| [[A498 (line)]] | wt | 11.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +11.3) | — |
| [[A549 (line)]] | wt | 11.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 11.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +9.4) | — |
| [[RKO (line)]] | wt | 27.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -12.1) |
| [[SHP-77 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[A-427 (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9421), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXK2]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[SGPP1]] | +0.67 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[CORO7]] | +0.66 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[TSPAN17]] | +0.66 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[LIMK1]] | +0.65 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[TPST2]] | +0.64 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[CSNK1E]] | +0.64 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[TMEM184B]] | +0.63 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[DNAJC5]] | +0.63 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[PACC1]] | +0.62 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[CBL]] | +0.62 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[HMOX2]] | +0.62 | +0.53 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA5]] | -0.66 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[RBM7]] | -0.63 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[BDH2]] | -0.62 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[SF3B1]] | -0.61 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[ZNF608]] | -0.60 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[DZIP3]] | -0.60 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[COPS5]] | -0.60 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[CLK4]] | -0.60 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[MED12]] | -0.59 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[FUNDC1]] | -0.59 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[BCLAF1]] | -0.59 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[CCDC25]] | -0.58 | -0.56 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BHLHE41]] | B | BHLHE41 activity lowers SLC27A4's level | lines that do not express BHLHE41 (19) vs lines expressing it (31) | 1.35× higher at baseline in the lines without BHLHE41 | 0.018 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SVIL-AS1-1]] | C | SLC27A4's natural level strengthens SVIL-AS1-1's drug response | SLC27A4's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse -0.16; direction not clear | 0.091 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.492). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-5.2, -0.4); signed map (-44.0, -5.9). **Vector** length 85.2, 16.6% of its response variance represented; |z| ≥ 3 in 1,036 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | +3.6 | +6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +12.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.4 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +8.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +6.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.5 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.5 | +5.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.5 | -7.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -5.0 | -3.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.8 | -6.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.5 | -7.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -3.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.0 | -2.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.8 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 27 member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,340,527-128,361,470 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FATP4, ACSVL4, FATP-4 |
| Gene groups (HGNC) | Acyl-CoA synthetase family; Solute carrier family 27 |
| Reactome | 6 pathways, smallest: Transport of fatty acids; Transport of vitamins, nucleosides, and related molecules; SLC transporter disorders |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P1M0](https://www.uniprot.org/uniprotkb/Q6P1M0) (Long-chain fatty acid transport protein 4):

> Mediates the levels of long-chain fatty acids (LCFA) in the cell by facilitating their transport across cell membranes. Appears to be the principal fatty acid transporter in small intestinal enterocytes. Also functions as an acyl-CoA ligase catalyzing the ATP-dependent formation of fatty acyl-CoA using LCFA and very-long-chain fatty acids (VLCFA) as substrates, which prevents fatty acid efflux from cells and might drive more fatty acid uptake. Plays a role in the formation of the epidermal …

**Summary**, from NCBI Gene [10999](https://www.ncbi.nlm.nih.gov/gene/10999):

> This gene encodes a member of a family of fatty acid transport proteins, which are involved in translocation of long-chain fatty acids cross the plasma membrane. This protein is expressed at high levels on the apical side of mature enterocytes in the small intestine, and appears to be the principal fatty acid transporter in enterocytes. Clinical studies suggest this gene as a candidate gene for the insulin resistance syndrome. Mutations in this gene have been associated with ichthyosis …

**Accessions** — [HGNC:10998](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10998) · Entrez [10999](https://www.ncbi.nlm.nih.gov/gene/10999) · UniProt [Q6P1M0](https://www.uniprot.org/uniprotkb/Q6P1M0) · Ensembl [ENSG00000167114](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167114)

## Data

Gene col 9421: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9421); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9421, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9421]; `tensor/DDL_lfc|DDL_z.npy` [9421]; `embed/gene_vectors.npy` [9421]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9421 or target_col == 9421). Every well: [[SLC27A4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC27A4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
