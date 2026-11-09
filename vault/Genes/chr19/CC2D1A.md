---
symbol: "CC2D1A"
type: "gene"
col: 5272
ensembl_id: "ENSG00000132024"
name: "coiled-coil and C2 domain containing 1A"
location: "19p13.12"
module: 30
arm: "+"
pooled_cpm: 25.16
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# CC2D1A

*coiled-coil and C2 domain containing 1A* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 1.53× (z +5.3, q 6e-05, up in 22 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Relugolix (drug)]] 5 µM in 1 line (NCI-H2122 2.24×).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.641× (z -11.0, q 3e-25, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLYWCH1]] (+0.71, fdr 7e-06), [[ABCD4]] (+0.69, fdr 7e-06), [[CRYZL1]] (+0.68, fdr 7e-06); moves opposite to [[TUG1]] (-0.63, fdr 1e-05), [[PURB]] (-0.62, fdr 1e-05), [[C6orf120]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5272.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Relugolix (drug)]] 5 µM in 1 line (NCI-H2122 2.24×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.53×** | +5.3 | 6e-05 | 22/47 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +4.6 | 0.001 | 19/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.33×** | +4.3 | 0.003 | 15/48 (HOP62, SW 1271, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +4.0 | 0.010 | 20/47 (SW480, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.16× | +3.7 | 0.029 | 16/48 (SNU-1, C-33 A, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.6 | 0.033 | 11/41 (BT-474, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.19× | +3.1 | 0.12 | 11/47 (RKO, NCI-H1573, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.28× | +3.1 | 0.12 | 8/48 (A498, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5272.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.641×** | -11.0 | 3e-25 | 33/47 (MIA PaCa-2, HCT15, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.651×** | -10.6 | 1e-23 | 36/48 (Panc 03.27, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.617×** | -8.4 | 7e-15 | 32/47 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.642×** | -7.7 | 1e-12 | 28/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.773×** | -6.3 | 3e-08 | 28/48 (hTERT-HPNE, HEC-1-A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.717×** | -5.8 | 6e-07 | 24/48 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.725×** | -5.4 | 5e-06 | 22/48 (PANC-1, NCI-H1792, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.762×** | -4.5 | 4e-04 | 16/34 (LoVo, SW48, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.614×** | -4.5 | 5e-04 | 23/48 (SW 1271, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.785×** | -4.2 | 0.001 | 19/47 (SW480, NCI-H2030, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.804×** | -3.8 | 0.008 | 18/48 (NCI-H1792, NCI-H460, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.664×** | -3.7 | 0.009 | 16/47 (BT-474, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.806×** | -3.5 | 0.024 | 16/40 (NCI-H1792, Panc 03.27, …) | inconsistent across doses | composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.689×** | -3.4 | 0.028 | 11/47 (SW 1271, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 5 µM |  | 0.880× | -3.1 | 0.069 | 8/48 (Hs 766T, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5272. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 23.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -14.8) |
| [[Panc 03.27 (line)]] | alt | 49.0 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -12.0) |
| [[BT-474 (line)]] | alt | 40.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 24.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 19.2 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.355× (z -9.0) |
| [[AN3 CA (line)]] | alt | 37.3 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0845× (z -10.5) |
| [[C32 (line)]] | wt | 30.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -10.2) |
| [[H4 (line)]] | wt | 20.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.171× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~89% of this change |
| [[HCT15 (line)]] | alt | 55.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.9) |
| [[LoVo (line)]] | wt | 24.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[LS 180 (line)]] | wt | 50.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H2030 (line)]] | alt | 36.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -8.9) |
| [[NCI-H2122 (line)]] | alt | 28.9 | 1 | 0 | [[Relugolix (drug)]] 5 µM 2.24× (z +13.5) | — |
| [[SNU-423 (line)]] | alt | 21.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -8.5) |
| [[SW48 (line)]] | wt | 49.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SW480 (line)]] | alt | 31.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -11.8) |
| [[A-172 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5272), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLYWCH1]] | +0.71 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[ABCD4]] | +0.69 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.68 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[DDRGK1]] | +0.67 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[LIN7B]] | +0.66 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[GTF2H2B]] | +0.61 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[IQSEC2]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[RPP21]] | +0.60 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[ZFP14]] | +0.60 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[UNC45A]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[MRPS5]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[UBE4B]] | +0.60 | +0.62 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUG1]] | -0.63 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[PURB]] | -0.62 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[C6orf120]] | -0.61 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[SLC39A10]] | -0.61 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[YWHAZ]] | -0.58 | -0.35 / -0.65 | both halves | 1e-04 |  |
| [[ERLIN2]] | -0.58 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[RBM12]] | -0.57 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[DR1]] | -0.56 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[CFL1]] | -0.55 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[ZNF655]] | -0.55 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ETS1]] | -0.54 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[PARVA]] | -0.54 | -0.46 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers CC2D1A's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.653). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-0.7, -12.2); signed map (-32.8, -3.5). **Vector** length 88.6, 18.7% of its response variance represented; |z| ≥ 3 in 688 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +4.6 | +4.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | +4.2 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.9 | +5.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.8 | +2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +2.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.5 | -7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -3.9 | -3.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -10.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -6.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -1.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil and C2 domain containing 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:13,906,201-13,930,879 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20241, MRT3, Freud-1, Lgd2, TAPE, Aki-1 |
| Gene groups (HGNC) | C2 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P1N0](https://www.uniprot.org/uniprotkb/Q6P1N0) (Coiled-coil and C2 domain-containing protein 1A):

> Transcription factor that binds specifically to the DRE (dual repressor element) and represses HTR1A gene transcription in neuronal cells. The combination of calcium and ATP specifically inactivates the binding with FRE. May play a role in the altered regulation of HTR1A associated with anxiety and major depression. Mediates HDAC-independent repression of HTR1A promoter in neuronal cell. Performs essential function in controlling functional maturation of synapses (By similarity). Plays distinct …

**Summary**, from NCBI Gene [54862](https://www.ncbi.nlm.nih.gov/gene/54862):

> This gene encodes a transcriptional repressor that binds to a conserved 14-bp 5'-repressor element and regulates expression of the 5-hydroxytryptamine (serotonin) receptor 1A gene in neuronal cells. The DNA binding and transcriptional repressor activities of the protein are inhibited by calcium. A mutation in this gene results in a nonsyndromic form of cognitive disability (MRT3). [provided by RefSeq, Jul 2017]

**Accessions** — [HGNC:30237](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30237) · Entrez [54862](https://www.ncbi.nlm.nih.gov/gene/54862) · UniProt [Q6P1N0](https://www.uniprot.org/uniprotkb/Q6P1N0) · Ensembl [ENSG00000132024](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132024)

## Data

Gene col 5272: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5272); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5272, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5272]; `tensor/DDL_lfc|DDL_z.npy` [5272]; `embed/gene_vectors.npy` [5272]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5272 or target_col == 5272). Every well: [[CC2D1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CC2D1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
