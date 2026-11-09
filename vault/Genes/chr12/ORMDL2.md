---
symbol: "ORMDL2"
type: "gene"
col: 4425
ensembl_id: "ENSG00000123353"
name: "ORMDL sphingolipid biosynthesis regulator 2"
location: "12q13.2"
module: 184
arm: "+"
pooled_cpm: 9.88
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 10
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/184"]
generated_by: "tahoemap"
---

# ORMDL2

*ORMDL sphingolipid biosynthesis regulator 2* — 12q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.07× (z +11.9, q 6e-30, up in 38 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.403× (z -5.3, q 7e-05, down in 26 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RUBCN]] (+0.67, fdr 7e-06), [[ULBP2]] (+0.65, fdr 3e-05), [[ELOVL1]] (+0.64, fdr 7e-06); moves opposite to [[RBM26]] (-0.58, fdr 1e-05), [[SSRP1]] (-0.58, fdr 4e-05), [[ILF3]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 184]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SFN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4425.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +11.9 | 6e-30 | 38/43 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +7.1 | 3e-10 | 32/42 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.0 | 2e-07 | 24/48 (NCI-H2030, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.68×** | +6.0 | 2e-07 | 31/47 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.58×** | +5.3 | 1e-05 | 23/47 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.55×** | +5.1 | 3e-05 | 23/47 (SW480, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.54×** | +5.0 | 4e-05 | 19/32 (Panc 03.27, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.56×** | +5.0 | 4e-05 | 10/19 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +4.6 | 2e-04 | 18/42 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.4 | 5e-04 | 19/43 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +4.4 | 7e-04 | 19/45 (LoVo, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.2 | 0.001 | 13/33 (AsPC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.43×** | +3.8 | 0.005 | 8/25 (NCI-H2030, A498, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.008 | 17/45 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +3.6 | 0.010 | 7/25 (A549, LOX-IMVI, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.030 | 10/48 (SHP-77, NCI-H2347, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.041 | 13/48 (SW1417, MIA PaCa-2, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.081 | 3/45 (CFPAC-1, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4425.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.403×** | -5.3 | 7e-05 | 26/44 (LoVo, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.753×** | -4.6 | 0.001 | 21/41 (HS-578T, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.698×** | -4.1 | 0.006 | 14/47 (A-427, PANC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.515×** | -3.9 | 0.016 | 15/41 (A-427, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.792×** | -3.8 | 0.016 | 15/47 (SNU-1, HT-29, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 0.05 µM |  | **0.742×** | -3.4 | 0.054 | 14/47 (C-33 A, SW1417, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.747×** | -3.4 | 0.063 | 7/48 (A-427, COLO 205, …) | all doses, flat |  |
| [[Minodronic acid (drug)]] 0.05 µM |  | **0.740×** | -3.3 | 0.067 | 9/48 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.741×** | -3.3 | 0.067 | 14/43 (BT-474, Panc 03.27, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.573×** | -3.2 | 0.067 | 15/40 (MIA PaCa-2, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Methotrexate (drug)]] 0.05 µM |  | 0.766× | -3.1 | 0.11 | 9/44 (H4, SNU-1, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4425. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[HS-578T (line)]] | alt | 9.22 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -10.1) |
| [[HT-29 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[MIA PaCa-2 (line)]] | alt | 4.98 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0612× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 7.06 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0720× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 6.35 | 0 | 1 | — | [[Penfluridol (drug)]] 0.5 µM 0.0724× (z -10.4) |
| [[SW480 (line)]] | alt | 9.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +10.1) | — |
| [[A-172 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.26 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4425), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RUBCN]] | +0.67 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ULBP2]] | +0.65 | +0.46 / +0.67 | both halves | 3e-05 |  |
| [[ELOVL1]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[TPTEP2-CSNK1E]] | +0.63 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[WDR44]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[RHOC]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[PLIN3]] | +0.60 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[SLC27A4]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[DNASE1L1]] | +0.59 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[GLTP]] | +0.59 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[TSPAN17]] | +0.58 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[PINK1]] | +0.58 | +0.49 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM26]] | -0.58 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[SSRP1]] | -0.58 | -0.41 / -0.67 | both halves | 4e-05 |  |
| [[ILF3]] | -0.55 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[PRPF4B]] | -0.55 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[C2CD5]] | -0.54 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[SRSF10]] | -0.54 | -0.31 / -0.61 | both halves | 2e-04 |  |
| [[HNRNPD]] | -0.54 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[FUBP1]] | -0.53 | -0.36 / -0.58 | both halves | 9e-05 |  |
| [[MATR3]] | -0.53 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[BACE1-AS]] | -0.53 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[EWSR1]] | -0.52 | -0.37 / -0.57 | both halves | 9e-05 |  |
| [[SORL1]] | -0.52 | -0.53 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SFN]] | B | SFN activity raises ORMDL2's level | lines that do not express SFN (20) vs lines expressing it (30) | 1.61× lower at baseline in the lines without SFN | 0.008 | ⚠ within organs, on part of the lines; also absent: KRT18, ESRP2, SH2D3A |
| [[TOP2A]] | B | TOP2A activity lowers ORMDL2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[APC]] | C | APC activity weakens ORMDL2's drug response | recorded loss-of-function mutation of APC in 7 lines vs 38 not recorded | the APC-altered lines respond 1.71× as strongly (z diff -1.27); strongest at Panobinostat 5 µM: 2.26x vs 1.44x (z diff -2.7) | 0.047 | ⚠ tissue-confounded; across organs; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 184]]; 20 genes; this gene is in the **+** arm (projection on the module's main direction 0.724). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (15.1, -1.1); signed map (-16.0, 18.4). **Vector** length 65.4, 11.8% of its response variance represented; |z| ≥ 3 in 688 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +11.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +6.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +1.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.9 | +2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.9 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | -4.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.6 | -5.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -3.3 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ORMDL sphingolipid biosynthesis regulator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.2 — chr12:55,818,041-55,821,879 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC160, adoplin-2, MST095, MSTP095 |
| Gene groups (HGNC) | ORMDL sphingolipid biosynthesis regulators |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53FV1](https://www.uniprot.org/uniprotkb/Q53FV1) (ORM1-like protein 2):

> Plays an essential role in the homeostatic regulation of sphingolipid de novo biosynthesis by modulating the activity of the serine palmitoyltransferase (SPT) in response to ceramide levels. When complexed to SPT, the binding of ceramides to its N-terminus stabilizes a conformation that block SPT substrate entry, hence preventing SPT catalytic activity. Through this mechanism, maintains ceramide levels at sufficient concentrations for the production of complex sphingolipids, but which prevents …

**Summary**, from NCBI Gene [29095](https://www.ncbi.nlm.nih.gov/gene/29095):

> Involved in ceramide metabolic process. Acts upstream of or within negative regulation of ceramide biosynthetic process. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16037](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16037) · Entrez [29095](https://www.ncbi.nlm.nih.gov/gene/29095) · UniProt [Q53FV1](https://www.uniprot.org/uniprotkb/Q53FV1) · Ensembl [ENSG00000123353](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123353)

## Data

Gene col 4425: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4425); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4425, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4425]; `tensor/DDL_lfc|DDL_z.npy` [4425]; `embed/gene_vectors.npy` [4425]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4425 or target_col == 4425). Every well: [[ORMDL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ORMDL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
