---
symbol: "HMGN4"
type: "gene"
col: 11347
ensembl_id: "ENSG00000182952"
name: "high mobility group nucleosomal binding domain 4"
location: "6p22.2"
module: 94
arm: "+"
pooled_cpm: 29.19
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 6
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# HMGN4

*high mobility group nucleosomal binding domain 4* — 6p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.61× (z +13.5, q 1e-38, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.456× (z -15.7, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF343]] (+0.61, fdr 1e-05), [[NT5C3B]] (+0.59, fdr 1e-05), [[GNPTAB]] (+0.57, fdr 3e-05); moves opposite to [[GLYR1]] (-0.54, fdr 4e-05), [[ACAP3]] (-0.48, fdr 1e-04), [[PI4KA]] (-0.47, fdr 1e-04).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11347.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.61×** | +13.5 | 1e-38 | 39/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.51×** | +8.3 | 3e-14 | 38/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.42×** | +7.0 | 5e-10 | 32/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +6.6 | 6e-09 | 17/37 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.37×** | +6.3 | 4e-08 | 27/47 (PANC-1, SW1417, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.34×** | +5.9 | 4e-07 | 20/43 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +5.6 | 2e-06 | 27/46 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~15% of this change | **1.26×** | +4.6 | 3e-04 | 21/46 (PANC-1, NCI-H2030, …) | all doses, flat | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.26×** | +4.6 | 3e-04 | 19/48 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +4.1 | 0.003 | 11/30 (HS-578T, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.006 | 17/48 (PANC-1, SW480, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.012 | 13/45 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.5 | 0.018 | 7/48 (NCI-H2030, Panc 03.27, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.018 | 8/48 (A-172, NCI-H460, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 5 µM |  | 1.20× | +3.5 | 0.018 | 10/47 (A-427, SNU-423, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.17× | +3.1 | 0.077 | 10/48 (LoVo, LS 180, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.079 | 8/48 (MIA PaCa-2, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.080 | 11/48 (SW 900, MIA PaCa-2, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.082 | 14/48 (SK-MEL-2, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11347.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.456×** | -15.7 | 0e+00 | 44/48 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.569×** | -11.2 | 8e-27 | 36/48 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.571×** | -11.2 | 1e-26 | 44/48 (NCI-H23, J82, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.748×** | -8.2 | 4e-14 | 29/47 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.809×** | -6.0 | 3e-07 | 23/48 (LOX-IMVI, LoVo, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.855× | -4.4 | 0.001 | 20/48 (HOP62, NCI-H661, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.814×** | -4.1 | 0.003 | 15/48 (SW480, HS-578T, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.872× | -3.9 | 0.008 | 15/48 (SW 1271, SHP-77, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.851× | -3.2 | 0.083 | 7/48 (RKO, A-172, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.849× | -3.1 | 0.097 | 18/47 (C32, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11347. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 55.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.308× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 61.8 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.363× (z -10.6) |
| [[SW480 (line)]] | alt | 29.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.391× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 25.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.299× (z -9.2) |
| [[LoVo (line)]] | wt | 30.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.384× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 36.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -11.3) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.485× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 74.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.328× (z -11.5) |
| [[PANC-1 (line)]] | alt | 35.0 | 1 | 1 | [[Selinexor (drug)]] 5 µM 1.81× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.406× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 33.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -9.9) |
| [[A-427 (line)]] | wt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -12.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 25.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.298× (z -9.7) |
| [[C32 (line)]] | wt | 24.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0945× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 25.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.332× (z -10.0) |
| [[HS-578T (line)]] | alt | 29.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -10.6) |
| [[KATO III (line)]] | alt | 24.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.312× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 47.4 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.54× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 18.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.377× (z -8.9) |
| [[RKO (line)]] | wt | 36.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -14.9) |
| [[SHP-77 (line)]] | alt | 24.2 | 0 | 1 | — | [[ULK-101 (drug)]] 0.05 µM 0.249× (z -8.6) |
| [[SNU-423 (line)]] | alt | 29.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.204× (z -12.6) |
| [[A-172 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11347), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF343]] | +0.61 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[NT5C3B]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[GNPTAB]] | +0.57 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[HDDC2]] | +0.56 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[ZNF639]] | +0.55 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[MRPS30]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[NUDT16]] | +0.54 | +0.24 / +0.62 | both halves | 5e-04 |  |
| [[RNF14]] | +0.54 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[TATDN3]] | +0.54 | +0.28 / +0.58 | both halves | 3e-04 |  |
| [[PRDM4]] | +0.53 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[GNA13]] | +0.53 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[ZNF138]] | +0.53 | +0.23 / +0.57 | both halves | 5e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLYR1]] | -0.54 | -0.42 / -0.64 | both halves | 4e-05 |  |
| [[ACAP3]] | -0.48 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[PI4KA]] | -0.47 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[PRKCA]] | -0.47 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[CRELD2]] | -0.46 | -0.19 / -0.56 | ⚠ one half (not replicated) | 8e-04 |  |
| [[STX5]] | -0.44 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[MAPKAPK2]] | -0.44 | -0.20 / -0.52 | ⚠ one half (not replicated) | 8e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises HMGN4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.569). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.2, -10.6); signed map (-33.9, -20.6). **Vector** length 85.2, 17.1% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +13.2 | +13.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +7.9 | +8.3 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +4.7 | +7.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.6 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +1.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.9 | +6.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +3.5 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -3.5 | -15.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.2 | -2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | -11.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +0.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.6 | -0.6 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Darinaparsin (drug)]] 0.5 µM |  | -1.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | high mobility group nucleosomal binding domain 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.2 — chr6:26,538,366-26,546,933 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NHC; previously HMG17L3 |
| Gene groups (HGNC) | Canonical high mobility group |
| Matched by | ensembl_id |

UniProt [O00479](https://www.uniprot.org/uniprotkb/O00479) carries no function annotation.

**Summary**, from NCBI Gene [10473](https://www.ncbi.nlm.nih.gov/gene/10473):

> The protein encoded by this gene, a member of the HMGN protein family, is thought to reduce the compactness of the chromatin fiber in nucleosomes, thereby enhancing transcription from chromatin templates. [provided by RefSeq, Mar 2013]

**Accessions** — [HGNC:4989](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4989) · Entrez [10473](https://www.ncbi.nlm.nih.gov/gene/10473) · UniProt [O00479](https://www.uniprot.org/uniprotkb/O00479) · Ensembl [ENSG00000182952](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182952)

## Data

Gene col 11347: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11347); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11347, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11347]; `tensor/DDL_lfc|DDL_z.npy` [11347]; `embed/gene_vectors.npy` [11347]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11347 or target_col == 11347). Every well: [[HMGN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMGN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
