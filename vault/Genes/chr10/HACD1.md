---
symbol: "HACD1"
type: "gene"
col: 9220
ensembl_id: "ENSG00000165996"
name: "3-hydroxyacyl-CoA dehydratase 1"
location: "10p12.33"
module: 124
arm: "+"
pooled_cpm: 15.88
n_lines_expressing: 45
n_dd_up: 21
n_dd_down: 6
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# HACD1

*3-hydroxyacyl-CoA dehydratase 1* — 10p12.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.73× (z +10.8, q 3e-24, up in 26 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.558× (z -8.2, q 2e-13, down in 22 of 42 measured lines).
> Its strongest partners by |cos| (69 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 31 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GYG1]] (+0.69, fdr 1e-05), [[LGALSL-DT]] (+0.68, fdr 3e-05), [[ZBTB8A]] (+0.67, fdr 3e-05); moves opposite to [[GNAI3]] (-0.59, fdr 4e-04), [[AMPD2]] (-0.57, fdr 1e-04), [[POGLUT2]] (-0.56, fdr 0.001, ⚠ one half only (not replicated)), [[RAB3A]] (-0.56, fdr 5e-04).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 2 go from it, the strongest it → [[DNAJC21]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9220.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +10.8 | 3e-24 | 26/41 (LoVo, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +9.3 | 3e-18 | 20/33 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +9.3 | 4e-18 | 22/42 (RPMI-7951, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +8.9 | 1e-16 | 25/40 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +7.4 | 1e-11 | 14/21 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +5.8 | 6e-07 | 17/29 (RPMI-7951, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +5.4 | 6e-06 | 21/41 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.4 | 6e-06 | 22/40 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +5.2 | 1e-05 | 20/43 (C-33 A, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.5 | 4e-04 | 14/42 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +4.3 | 9e-04 | 16/35 (AsPC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +4.2 | 0.001 | 18/42 (NCI-H460, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.007 | 10/42 (J82, RKO, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.009 | 13/42 (RPMI-7951, A498, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.009 | 12/43 (A-172, RPMI-7951, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.010 | 9/42 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.020 | 12/42 (SNU-423, A-427, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.3 | 0.035 | 15/43 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.047 | 9/42 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9220.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.558×** | -8.2 | 2e-13 | 22/42 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.355×** | -7.6 | 1e-11 | 23/39 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.391×** | -6.9 | 1e-09 | 26/43 (LoVo, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.637×** | -6.3 | 4e-08 | 24/42 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.695×** | -5.1 | 4e-05 | 21/42 (J82, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.748×** | -4.1 | 0.004 | 19/41 (LOX-IMVI, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 0.799× | -3.1 | 0.13 | 8/43 (RPMI-7951, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9220. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 35.5 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.292× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.373× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 32.3 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.0625× (z -11.6) |
| [[A-427 (line)]] | wt | 34.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.288× (z -9.0) |
| [[A549 (line)]] | wt | 22.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.80× (z +8.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 20.7 | 0 | 1 | — | [[Bexarotene (drug)]] 0.05 µM 0.0584× (z -9.3) |
| [[HOP62 (line)]] | alt | 13.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +8.6) | — |
| [[J82 (line)]] | alt | 44.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.313× (z -10.4) |
| [[LoVo (line)]] | wt | 17.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 4.50 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0657× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 18.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 4.83 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0749× (z -9.2) |
| [[SW480 (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.0) | — |
| [[A-172 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.62 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9220), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 28 of them with an alert (⚠; 28 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GYG1]] | +0.69 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[LGALSL-DT]] | +0.68 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[ZBTB8A]] | +0.67 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[TMEM192]] | +0.67 | +0.71 / +0.43 | both halves | 3e-05 |  |
| [[UBXN2A]] | +0.66 | +0.71 / +0.34 | both halves | 1e-04 |  |
| [[ITPA]] | +0.65 | +0.64 / +0.34 | both halves | 1e-04 |  |
| [[SPTY2D1OS]] | +0.64 | +0.69 / +0.36 | both halves | 1e-04 |  |
| [[ST7L]] | +0.64 | +0.66 / +0.24 | both halves | 5e-04 |  |
| [[RXYLT1]] | +0.64 | +0.68 / +0.35 | both halves | 1e-04 |  |
| [[ANKRD18A]] | +0.64 | +0.55 / +0.36 | both halves | 1e-04 |  |
| [[PPP1R12A-AS2]] | +0.62 | +0.64 / +0.33 | both halves | 1e-04 |  |
| [[ZC3H7B]] | +0.62 | +0.60 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAI3]] | -0.59 | -0.59 / -0.26 | both halves | 4e-04 |  |
| [[AMPD2]] | -0.57 | -0.64 / -0.33 | both halves | 1e-04 |  |
| [[POGLUT2]] | -0.56 | -0.57 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[RAB3A]] | -0.56 | -0.43 / -0.23 | both halves | 5e-04 |  |
| [[ELP1]] | -0.55 | -0.53 / -0.21 | both halves | 6e-04 |  |
| [[CTNNBL1]] | -0.55 | -0.56 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[SIPA1]] | -0.55 | -0.51 / -0.12 | ⚠ one half (not replicated) | 0.002 |  |
| [[ALDOA]] | -0.54 | -0.50 / -0.29 | both halves | 3e-04 |  |
| [[POT1]] | -0.54 | -0.58 / -0.25 | both halves | 4e-04 |  |
| [[SEC24C]] | -0.54 | -0.65 / -0.28 | both halves | 3e-04 |  |
| [[ESS2]] | -0.54 | -0.40 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises HACD1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FGF2]] | B | FGF2 activity raises HACD1's level | lines that do not express FGF2 (16) vs lines expressing it (34) | 2.06× lower at baseline in the lines without FGF2 | 0.083 | ⚠ within organs, on part of the lines; also absent: F2R, EML1, DPY19L2 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAJC21]] | B | HACD1 activity raises DNAJC21's level | lines that do not express HACD1 (5) vs lines expressing it (45) | 1.76× lower at baseline in the lines without HACD1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CLSTN3, CDR2L, PIM1; its own permutation p |
| [[ZBTB8A]] | B | HACD1 activity raises ZBTB8A's level | lines that do not express HACD1 (5) vs lines expressing it (45) | 1.35× lower at baseline in the lines without HACD1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CLSTN3, CDR2L, PIM1; its own permutation p |

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.684). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-1.1, 10.3); signed map (22.5, -20.3). **Vector** length 88.2, 19.1% of its response variance represented; |z| ≥ 3 in 803 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +9.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +8.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.9 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +7.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +3.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +3.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.4 | -8.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.1 | -5.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.5 | -6.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -7.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.5 | -6.9 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.5 | -0.9 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Malotilate (drug)]] 0.05 µM |  | -1.3 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | 3-hydroxyacyl-CoA dehydratase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.33 — chr10:17,589,032-17,617,374 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CAP; previously PTPLA |
| Gene groups (HGNC) | 3-hydroxyacyl-CoA dehydratase family |
| Reactome | 4 pathways, smallest: Synthesis of very long-chain fatty acyl-CoAs; Fatty acyl-CoA biosynthesis; Fatty acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [B0YJ81](https://www.uniprot.org/uniprotkb/B0YJ81) (Very-long-chain):

> [Isoform 1]: Catalyzes the third of the four reactions of the long-chain fatty acids elongation cycle. This endoplasmic reticulum-bound enzymatic process, allows the addition of two carbons to the chain of long- and very long-chain fatty acids/VLCFAs per cycle. This enzyme catalyzes the dehydration of the 3-hydroxyacyl-CoA intermediate into trans-2,3-enoyl-CoA, within each cycle of fatty acid elongation. Thereby, it participates in the production of VLCFAs of different chain lengths that are …

**Summary**, from NCBI Gene [9200](https://www.ncbi.nlm.nih.gov/gene/9200):

> The protein encoded by this gene contains a characteristic catalytic motif of the protein tyrosine phosphatases (PTPs) family. The PTP motif of this protein has the highly conserved arginine residue replaced by a proline residue; thus it may represent a distinct class of PTPs. Members of the PTP family are known to be signaling molecules that regulate a variety of cellular processes. This gene was preferentially expressed in both adult and fetal heart. A much lower expression level was detected …

**Accessions** — [HGNC:9639](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9639) · Entrez [9200](https://www.ncbi.nlm.nih.gov/gene/9200) · UniProt [B0YJ81](https://www.uniprot.org/uniprotkb/B0YJ81) · Ensembl [ENSG00000165996](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165996)

## Data

Gene col 9220: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9220); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9220, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9220]; `tensor/DDL_lfc|DDL_z.npy` [9220]; `embed/gene_vectors.npy` [9220]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9220 or target_col == 9220). Every well: [[HACD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HACD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
