---
symbol: "MAGEF1"
type: "gene"
col: 10817
ensembl_id: "ENSG00000177383"
name: "MAGE family member F1"
location: "3q27.1"
module: 11
arm: "+"
pooled_cpm: 14.25
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# MAGEF1

*MAGE family member F1* — 3q27.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.62× (z +4.7, q 0.001, up in 24 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.393× (z -9.2, q 3e-17, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSL3P1]] (+0.72, fdr 7e-06), [[BLOC1S4]] (+0.69, fdr 9e-06), [[ABCF1]] (+0.67, fdr 7e-06); moves opposite to [[NPHP3-ACAD11]] (-0.56, fdr 3e-05), [[PRDM2]] (-0.56, fdr 3e-05), [[FAM229A]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10817.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.62×** | +4.7 | 0.001 | 24/45 (LS 180, KATO III, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.33×** | +3.9 | 0.026 | 25/47 (HEC-1-A, SW 1271, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.059 | 23/47 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.42×** | +3.4 | 0.086 | 17/46 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | 1.40× | +3.3 | 0.10 | 14/40 (SW1417, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | 1.25× | +3.1 | 0.17 | 22/47 (HOP62, MIA PaCa-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | 1.39× | +3.1 | 0.17 | 6/22 (A-427, SW1417, …) | top dose only | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.38× | +3.0 | 0.17 | 16/41 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.36× | +3.0 | 0.17 | 12/46 (MIA PaCa-2, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10817.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.393×** | -9.2 | 3e-17 | 35/46 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.494×** | -6.9 | 1e-09 | 35/46 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.515×** | -6.5 | 1e-08 | 31/46 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.634×** | -6.3 | 4e-08 | 26/45 (LoVo, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.527×** | -5.9 | 3e-07 | 27/47 (NCI-H1573, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.559×** | -5.7 | 1e-06 | 28/46 (HT-29, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.564×** | -5.6 | 2e-06 | 25/45 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.670×** | -5.5 | 2e-06 | 27/45 (SK-MEL-2, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.581×** | -5.3 | 7e-06 | 28/46 (KATO III, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.453×** | -4.1 | 0.003 | 20/32 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.549× | -3.1 | 0.11 | 13/45 (SNU-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10817. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 22.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 15.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -11.8) |
| [[SW480 (line)]] | alt | 24.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -10.1) |
| [[A-172 (line)]] | wt | 23.0 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0689× (z -8.6) ⚠ toxic |
| [[BT-474 (line)]] | alt | 12.6 | 0 | 1 | — | [[Budesonide (drug)]] 0.05 µM 0.0865× (z -10.2) |
| [[C-33 A (line)]] | alt | 21.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 8.58 | 0 | 1 | — | [[Flutamide (drug)]] 0.05 µM 0.0470× (z -10.0) |
| [[HT-29 (line)]] | alt | 9.20 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.148× (z -8.6) |
| [[KATO III (line)]] | alt | 40.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 20.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.207× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 4.96 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -9.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 9.74 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0610× (z -9.2) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 20.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -17.3) |
| [[SW48 (line)]] | wt | 15.6 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0807× (z -9.2) |
| [[A-427 (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10817), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSL3P1]] | +0.72 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[BLOC1S4]] | +0.69 | +0.57 / +0.75 | both halves | 9e-06 |  |
| [[ABCF1]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[MRPL57]] | +0.66 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[AGGF1]] | +0.65 | +0.51 / +0.74 | both halves | 1e-05 |  |
| [[NDUFA8]] | +0.65 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[KLHL9]] | +0.64 | +0.46 / +0.69 | both halves | 2e-05 |  |
| [[PPP4R2]] | +0.64 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[MRFAP1L1]] | +0.63 | +0.52 / +0.78 | both halves | 1e-05 |  |
| [[GSPT2]] | +0.63 | +0.47 / +0.75 | both halves | 2e-05 |  |
| [[CENPB]] | +0.61 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[CEBPZ]] | +0.61 | +0.46 / +0.74 | both halves | 2e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPHP3-ACAD11]] | -0.56 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[PRDM2]] | -0.56 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[FAM229A]] | -0.52 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[KIAA1191]] | -0.52 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[CSDE1]] | -0.51 | -0.32 / -0.58 | both halves | 2e-04 |  |
| [[AP2B1]] | -0.51 | -0.42 / -0.55 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers MAGEF1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[PSMB5]] | B | PSMB5 activity raises MAGEF1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.521). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-42.8, -0.2); signed map (-2.5, -21.6). **Vector** length 77.3, 16.8% of its response variance represented; |z| ≥ 3 in 741 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +4.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | -0.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.0 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +3.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | -0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.2 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | -4.4 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.4 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.2 | +0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.0 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -5.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.1 | -1.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -3.1 |
|  | [[Pentagastrin (drug)]] 5 µM |  | -1.0 | -2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | MAGE family member F1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.1 — chr3:184,710,364-184,712,064 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MAGE family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAY2](https://www.uniprot.org/uniprotkb/Q9HAY2) (Melanoma-associated antigen F1):

> Enhances ubiquitin ligase activity of RING-type zinc finger-containing E3 ubiquitin ligases. Proposed to act through recruitment and/or stabilization of the E2 ubiquitin-conjugating enzyme at the E3:substrate complex. MAGEF1-NSMCE1 ubiquitin ligase complex promotes proteasomal degradation of MMS19, a key component of the cytosolic iron-sulfur protein assembly (CIA) machinery. Down-regulation of MMS19 impairs the activity of several DNA repair and metabolism enzymes such as ERCC2/XPD, FANCJ, …

**Summary**, from NCBI Gene [64110](https://www.ncbi.nlm.nih.gov/gene/64110):

> This intronless gene encodes a member of the MAGE superfamily. It is ubiquitously expressed in normal tissues and in tumor cells. This gene includes a microsatellite repeat in the coding region. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:29639](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29639) · Entrez [64110](https://www.ncbi.nlm.nih.gov/gene/64110) · UniProt [Q9HAY2](https://www.uniprot.org/uniprotkb/Q9HAY2) · Ensembl [ENSG00000177383](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177383)

## Data

Gene col 10817: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10817); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10817, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10817]; `tensor/DDL_lfc|DDL_z.npy` [10817]; `embed/gene_vectors.npy` [10817]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10817 or target_col == 10817). Every well: [[MAGEF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAGEF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
