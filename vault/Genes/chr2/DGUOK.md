---
symbol: "DGUOK"
type: "gene"
col: 3606
ensembl_id: "ENSG00000114956"
name: "deoxyguanosine kinase"
location: "2p13.1"
module: 7
arm: "+"
pooled_cpm: 56.97
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# DGUOK

*deoxyguanosine kinase* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.68× (z +7.3, q 1e-10, up in 29 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.621× (z -12.7, q 2e-34, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TADA3]] (+0.67, fdr 7e-06), [[LINC00467]] (+0.61, fdr 1e-05), [[PYM1]] (+0.60, fdr 1e-05); moves opposite to [[HSPA1B]] (-0.58, fdr 2e-05), [[KIF1B]] (-0.55, fdr 1e-05), [[TKT]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3606.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +7.3 | 1e-10 | 29/49 (A498, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +7.2 | 1e-10 | 1/49 (SW 1088) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +6.0 | 3e-07 | 25/47 (NCI-H460, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.19× | +5.9 | 4e-07 | 21/48 (SW480, J82, …) | rises with dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.37×** | +4.4 | 0.001 | 18/48 (LS 180, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~5% of this change | 1.17× | +3.9 | 0.008 | 14/47 (HepG2/C3A, CFPAC-1, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.16× | +3.9 | 0.008 | 11/48 (Panc 03.27, Hs 766T, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.10× | +3.7 | 0.018 | 5/48 (NCI-H2030, HepG2/C3A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.14× | +3.6 | 0.022 | 18/49 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.14× | +3.5 | 0.022 | 11/48 (RKO, AsPC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.14× | +3.4 | 0.034 | 8/48 (A-427, SK-MEL-2, …) | rises with dose |  |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 1.14× | +3.4 | 0.034 | 11/48 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.14× | +3.3 | 0.043 | 15/47 (SW480, H4, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.13× | +3.1 | 0.067 | 10/48 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3606.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.621×** | -12.7 | 2e-34 | 40/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.703×** | -9.4 | 1e-18 | 37/48 (C32, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.701×** | -9.1 | 1e-17 | 36/47 (SNU-423, SHP-77, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.607×** | -7.0 | 4e-10 | 27/45 (SK-MEL-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | **0.776×** | -6.8 | 1e-09 | 26/48 (PANC-1, KATO III, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.774×** | -6.5 | 1e-08 | 25/48 (SNU-423, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.835× | -4.8 | 1e-04 | 18/48 (NCI-H1573, A-427, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.855× | -4.2 | 0.002 | 16/48 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.807×** | -4.1 | 0.003 | 14/48 (NCI-H460, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.885× | -3.2 | 0.089 | 6/48 (A549, NCI-H2030, …) | top dose only | plate-row cell shift |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | 0.883× | -3.1 | 0.100 | 11/47 (AsPC-1, SNU-423, …) | inconsistent across doses |  |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | 0.888× | -3.1 | 0.100 | 10/48 (SNU-1, A-427, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.888× | -3.1 | 0.100 | 11/47 (NCI-H1573, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3606. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 119 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0947× (z -27.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[NCI-H460 (line)]] | wt | 56.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.492× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.510× (z -8.8) |
| [[PANC-1 (line)]] | alt | 81.4 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.433× (z -10.4) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.473× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 56.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1573 (line)]] | alt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.397× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[NCI-H23 (line)]] | alt | 105 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 62.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.02× (z +12.2) | — |
| [[A549 (line)]] | wt | 86.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.378× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[AN3 CA (line)]] | alt | 44.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.123× (z -10.4) ⚠ toxic |
| [[C32 (line)]] | wt | 38.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.358× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 48.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.388× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[SHP-77 (line)]] | alt | 61.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.309× (z -11.1) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 53.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -9.4) ⚠ cell-cycle shift, explains ~9% of this change |
| [[SNU-423 (line)]] | alt | 38.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.181× (z -14.0) ⚠ toxic |
| [[A-172 (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 63.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 64.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 55.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3606), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TADA3]] | +0.67 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[LINC00467]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[PYM1]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[MDM4]] | +0.60 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[SDHC]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ZDHHC4]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[MYSM1]] | +0.57 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[PPP3CB]] | +0.56 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[TJAP1]] | +0.56 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[ZNF26]] | +0.56 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[ZNF561]] | +0.55 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[SEC23B]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPA1B]] | -0.58 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[KIF1B]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[TKT]] | -0.54 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[DCUN1D4]] | -0.52 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[STRN]] | -0.52 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[MCU]] | -0.52 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[HACD3]] | -0.52 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[BLMH]] | -0.50 | -0.57 / -0.31 | both halves | 2e-04 |  |
| [[HSPA1A]] | -0.50 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[LRRFIP2]] | -0.50 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[HSF2]] | -0.50 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[CAMK2G]] | -0.49 | -0.54 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises DGUOK's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.320). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-29.1, 16.5); signed map (4.5, -24.6). **Vector** length 104, 23.5% of its response variance represented; |z| ≥ 3 in 862 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.2 | +7.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +5.4 | +5.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~5% of this change | +4.3 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +4.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.3 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +3.5 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.1 | +3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +3.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -7.1 | -12.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.7 | -9.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.8 | -9.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.1 | -6.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.8 | -7.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.6 | -4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | deoxyguanosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:73,926,826-73,958,961 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dGK |
| Gene groups (HGNC) | Deoxyribonucleoside kinases |
| Hallmark sets | DNA_REPAIR |
| Reactome | 3 pathways, smallest: Purine salvage; Nucleotide salvage; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16854](https://www.uniprot.org/uniprotkb/Q16854) (Deoxyguanosine kinase, mitochondrial):

> Phosphorylates deoxyguanosine and deoxyadenosine in the mitochondrial matrix, with the highest efficiency for deoxyguanosine. In non-replicating cells, where cytosolic dNTP synthesis is down-regulated, mtDNA synthesis depends solely on DGUOK and TK2. Phosphorylates certain nucleoside analogs (By similarity). Widely used as target of antiviral and chemotherapeutic agents.

**Summary**, from NCBI Gene [1716](https://www.ncbi.nlm.nih.gov/gene/1716):

> In mammalian cells, the phosphorylation of purine deoxyribonucleosides is mediated predominantly by two deoxyribonucleoside kinases, cytosolic deoxycytidine kinase and mitochondrial deoxyguanosine kinase. The protein encoded by this gene is responsible for phosphorylation of purine deoxyribonucleosides in the mitochondrial matrix. In addition, this protein phosphorylates several purine deoxyribonucleoside analogs used in the treatment of lymphoproliferative disorders, and this phosphorylation …

**Accessions** — [HGNC:2858](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2858) · Entrez [1716](https://www.ncbi.nlm.nih.gov/gene/1716) · UniProt [Q16854](https://www.uniprot.org/uniprotkb/Q16854) · Ensembl [ENSG00000114956](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114956)

## Data

Gene col 3606: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3606); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3606, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3606]; `tensor/DDL_lfc|DDL_z.npy` [3606]; `embed/gene_vectors.npy` [3606]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3606 or target_col == 3606). Every well: [[DGUOK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DGUOK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
