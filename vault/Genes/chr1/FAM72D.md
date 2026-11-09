---
symbol: "FAM72D"
type: "gene"
col: 13274
ensembl_id: "ENSG00000215784"
name: "RUMY family member 4"
location: "1q21.1"
module: 22
arm: "+"
pooled_cpm: 6.99
n_lines_expressing: 47
n_dd_up: 31
n_dd_down: 17
n_dd_up_clean: 14
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 39
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# FAM72D

*RUMY family member 4* — 1q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.97× (z +14.1, q 3e-42, up in 28 of 38 measured lines) ⚠ cell-cycle shift, explains ~89% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.56× (z +12.2, q 1e-31, up in 30 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.620× (z -6.3, q 2e-07, down in 24 of 43 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Cytarabine (hydrochloride) (drug)]] 0.05 µM: 0.617× (z -4.1, q 0.002, down in 14 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM72A]] (+0.91, fdr 7e-06), [[SGO2]] (+0.90, fdr 7e-06), [[FAM72B]] (+0.88, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); 39 go from it, the strongest it → [[NDC80]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 17 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13274.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **2.97×** | +14.1 | 3e-42 | 28/38 (PANC-1, NCI-H2030, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.56×** | +12.2 | 1e-31 | 30/35 (LOX-IMVI, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **2.08×** | +6.7 | 3e-09 | 20/35 (C-33 A, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~85% of this change | **2.08×** | +6.7 | 3e-09 | 17/28 (SHP-77, PANC-1, …) | all doses, flat | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.83×** | +5.5 | 4e-06 | 21/42 (KATO III, A549, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.83×** | +5.5 | 4e-06 | 22/44 (KATO III, NCI-H2347, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.79×** | +5.3 | 8e-06 | 20/44 (KATO III, SW480, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.50×** | +5.3 | 1e-05 | 21/43 (NCI-H1573, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.76×** | +5.0 | 4e-05 | 20/42 (PANC-1, A-427, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.70×** | +4.8 | 8e-05 | 15/40 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.68×** | +4.7 | 1e-04 | 18/44 (SW480, PANC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +4.6 | 2e-04 | 16/44 (SW480, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.63×** | +4.5 | 3e-04 | 11/41 (HOP62, SW 900, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.58×** | +4.1 | 0.001 | 13/36 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | **1.58×** | +4.0 | 0.002 | 2/11 (NCI-H2030, PANC-1) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.010 | 11/44 (A-172, KATO III, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.019 | 5/40 (J82, H4, …) | rises with dose | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.032 | 8/43 (HEC-1-A, NCI-H460, …) | rises with dose | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.62×** | +3.1 | 0.039 | 6/34 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.39×** | +3.0 | 0.061 | 9/43 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[AZD1390 (drug)]] 0.05 µM |  | **1.40×** | +2.9 | 0.088 | 6/42 (SW1417, A549, …) | inconsistent across doses | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.82×** | +2.9 | 0.088 | 3/32 (NCI-H460, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Gefitinib (drug)]] 5 µM |  | **1.37×** | +2.8 | 0.092 | 6/44 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | **1.25×** | +2.8 | 0.094 | 6/43 (RPMI-7951, J82, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **1.54×** | +2.8 | 0.094 | 9/43 (NCI-H460, HOP62, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13274.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.620×** | -6.3 | 2e-07 | 24/43 (A-427, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.507×** | -5.9 | 9e-07 | 23/40 (BT-474, HT-29, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.526×** | -5.7 | 2e-06 | 21/39 (HT-29, A-172, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.543×** | -5.6 | 2e-06 | 24/44 (SHP-77, SNU-1, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.558×** | -5.4 | 8e-06 | 23/41 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.592×** | -4.9 | 1e-04 | 20/44 (SHP-77, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.619×** | -4.4 | 8e-04 | 19/44 (LS 180, SHP-77, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.617×** | -4.1 | 0.002 | 14/43 (NCI-H1573, SW48, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.756×** | -3.7 | 0.014 | 15/44 (LoVo, KATO III, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.673×** | -3.7 | 0.014 | 13/44 (NCI-H460, A-427, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.472×** | -3.6 | 0.015 | 16/40 (PANC-1, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.689×** | -3.5 | 0.026 | 19/42 (HT-29, HOP62, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.771×** | -3.4 | 0.027 | 21/43 (A549, PANC-1, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.682×** | -3.3 | 0.033 | 12/44 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.700×** | -3.2 | 0.054 | 10/39 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.793×** | -3.1 | 0.080 | 10/44 (SW 900, RPMI-7951, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.793×** | -3.0 | 0.100 | 11/43 (NCI-H23, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +1.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13274. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.44 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.249× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 14.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +12.9) ⚠ cell-cycle shift, explains ~89% of this change | [[Bortezomib (drug)]] 5 µM 0.0660× (z -9.4) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.203× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 8.72 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +9.4) ⚠ cell-cycle shift, explains ~89% of this change | — |
| [[LOX-IMVI (line)]] | wt | 5.33 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.76× (z +9.4) ⚠ cell-cycle shift, explains ~89% of this change | — |
| [[NCI-H2030 (line)]] | alt | 6.59 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.00× (z +11.8) ⚠ cell-cycle shift, explains ~89% of this change | — |
| [[Panc 03.27 (line)]] | alt | 5.11 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0649× (z -8.9) |
| [[SNU-423 (line)]] | alt | 3.79 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.48× (z +8.9) ⚠ cell-cycle shift, explains ~89% of this change | — |
| [[A-172 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.863 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13274), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM72A]] | +0.91 | +0.83 / +0.92 | both halves | 7e-06 | STRING 478 |
| [[SGO2]] | +0.90 | +0.87 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[FAM72B]] | +0.88 | +0.85 / +0.88 | both halves | 7e-06 | STRING 640 |
| [[DLGAP5]] | +0.87 | +0.86 / +0.87 | both halves | 7e-06 | STRING 449 |
| [[PIF1]] | +0.87 | +0.80 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[PTTG1]] | +0.86 | +0.84 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[CDCA8]] | +0.85 | +0.80 / +0.86 | both halves | 7e-06 | STRING 443 |
| [[CDKN3]] | +0.85 | +0.84 / +0.87 | both halves | 7e-06 |  |
| [[CENPE]] | +0.85 | +0.88 / +0.83 | both halves | 7e-06 |  |
| [[AURKA]] | +0.84 | +0.83 / +0.89 | both halves | 7e-06 |  |
| [[KIF18A]] | +0.84 | +0.83 / +0.82 | both halves | 7e-06 |  |
| [[CKAP2]] | +0.84 | +0.84 / +0.83 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises FAM72D's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.10× lower at baseline in the lines without PIMREG | 0.068 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises FAM72D's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.77× lower at baseline in the lines without NDC80 | 0.053 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent; co-absent with the target |
| [[CDC20]] | C | CDC20 activity raises FAM72D's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.37× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[CDCA3]] | C | CDCA3 activity raises FAM72D's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 2.82× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target |
| [[AURKB]] | C | AURKB activity raises FAM72D's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.23× lower at baseline in the lines without AURKB | 0.086 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 0, C 39. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDC80]] | C | FAM72D activity raises NDC80's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 3.50× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; co-absent with the target; its own permutation p |
| [[KIF18B]] | C | FAM72D activity raises KIF18B's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 3.27× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[GTSE1]] | C | FAM72D activity raises GTSE1's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.86× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[CDCA3]] | C | FAM72D activity raises CDCA3's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.86× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; co-absent with the target; its own permutation p |
| [[CENPF]] | C | FAM72D activity raises CENPF's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.83× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[KIF15]] | C | FAM72D activity raises KIF15's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.81× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[NCAPD2]] | C | FAM72D activity raises NCAPD2's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.57× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[PIF1]] | C | FAM72D activity raises PIF1's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.55× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[BUB1]] | C | FAM72D activity raises BUB1's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.45× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[SPAG5]] | C | FAM72D activity raises SPAG5's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.38× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[TROAP]] | C | FAM72D activity raises TROAP's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.37× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[TTK]] | C | FAM72D activity raises TTK's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.32× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.842). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.8, -57.6); signed map (-51.3, -41.9). **Vector** length 97.8, 23.8% of its response variance represented; |z| ≥ 3 in 1,018 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.66 to 60); *DREAM G2/M down* (control, mean cos +0.79 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.62 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +6.3 | +14.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +12.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~85% of this change | +3.4 | +6.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~69% of this change | +3.2 | +4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +2.9 | +5.5 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.8 | +3.4 |
|  | [[Peretinoin (drug)]] 0.05 µM |  | +1.8 | +2.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.8 | +3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.6 | +2.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.3 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.8 | -3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -4.4 | -4.4 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -4.1 | -5.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~78% of this change | -3.9 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -1.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.9 | -3.4 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -2.8 | -4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | RUMY family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.1 — chr1:145,095,974-145,112,696 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously FAM72D |
| Matched by | ensembl_id |

UniProt [Q6L9T8](https://www.uniprot.org/uniprotkb/Q6L9T8) carries no function annotation.

**Summary**, from NCBI Gene [728833](https://www.ncbi.nlm.nih.gov/gene/728833):

> Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:33593](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33593) · Entrez [728833](https://www.ncbi.nlm.nih.gov/gene/728833) · UniProt [Q6L9T8](https://www.uniprot.org/uniprotkb/Q6L9T8) · Ensembl [ENSG00000215784](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215784)

## Data

Gene col 13274: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13274); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13274, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13274]; `tensor/DDL_lfc|DDL_z.npy` [13274]; `embed/gene_vectors.npy` [13274]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13274 or target_col == 13274). Every well: [[FAM72D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM72D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
