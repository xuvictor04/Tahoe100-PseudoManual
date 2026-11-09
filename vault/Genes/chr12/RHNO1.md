---
symbol: "RHNO1"
type: "gene"
col: 10161
ensembl_id: "ENSG00000171792"
name: "RAD9-HUS1-RAD1 interacting nuclear orphan 1"
location: "12p13.33"
module: 91
arm: "+"
pooled_cpm: 8.49
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# RHNO1

*RAD9-HUS1-RAD1 interacting nuclear orphan 1* — 12p13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.63× (z +9.2, q 2e-17, up in 24 of 30 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.52× (z +5.7, q 2e-06, up in 23 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.255× (z -6.8, q 5e-09, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM111A]] (+0.71, fdr 7e-06), [[ZNF681]] (+0.66, fdr 1e-05), [[BRCA2]] (+0.66, fdr 7e-06); moves opposite to [[TMEM120B]] (-0.60, fdr 4e-05), [[TOMM20]] (-0.59, fdr 1e-05), [[RPL23A]] (-0.57, fdr 3e-05).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10161.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.63×** | +9.2 | 2e-17 | 24/30 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.44×** | +8.2 | 6e-14 | 10/14 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.02×** | +6.5 | 2e-08 | 31/46 (NCI-H2030, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.83×** | +5.8 | 1e-06 | 19/36 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.7 | 2e-06 | 23/45 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.79×** | +5.6 | 3e-06 | 28/46 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.46×** | +5.1 | 2e-05 | 17/44 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.68×** | +4.6 | 4e-04 | 11/24 (NCI-H2347, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.51×** | +3.9 | 0.005 | 15/43 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Trifluridine (drug)]] 0.5 µM |  | **1.49×** | +3.8 | 0.007 | 12/45 (SW480, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.013 | 17/43 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.6 | 0.015 | 14/35 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.40×** | +3.2 | 0.052 | 10/48 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.052 | 11/42 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.052 | 9/46 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.092 | 11/47 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.098 | 8/47 (NCI-H23, HEC-1-A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10161.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.255×** | -6.8 | 5e-09 | 29/45 (Panc 03.27, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.347×** | -5.3 | 3e-05 | 26/42 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.763×** | -3.7 | 0.046 | 21/48 (KATO III, NCI-H661, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.678×** | -3.5 | 0.062 | 17/47 (Panc 03.27, LOX-IMVI, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.784× | -3.3 | 0.11 | 10/47 (SNU-1, NCI-H2030, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.723× | -3.1 | 0.18 | 16/47 (SNU-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10161. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 29.6 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0558× (z -9.2) |
| [[HS-578T (line)]] | alt | 4.37 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0653× (z -9.0) ⚠ transcription drop |
| [[NCI-H2030 (line)]] | alt | 9.77 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.112× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 15.0 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0265× (z -10.0) |
| [[PANC-1 (line)]] | alt | 8.43 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0552× (z -8.9) |
| [[SNU-423 (line)]] | alt | 5.27 | 0 | 1 | — | [[Menadione (drug)]] 0.5 µM 0.0931× (z -8.7) |
| [[A-172 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10161), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM111A]] | +0.71 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[ZNF681]] | +0.66 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[BRCA2]] | +0.66 | +0.66 / +0.62 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 572 |
| [[MSANTD7]] | +0.66 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ZNF318]] | +0.65 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[ESPL1]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[PHF19]] | +0.64 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[HASPIN]] | +0.63 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[DCLRE1A]] | +0.62 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[REXO5]] | +0.62 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[GEN1]] | +0.62 | +0.63 / +0.51 | both halves | 1e-05 | pathway: DNA Double-Strand Break Repair |
| [[APOBEC3B]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM120B]] | -0.60 | -0.69 / -0.41 | both halves | 4e-05 |  |
| [[TOMM20]] | -0.59 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[RPL23A]] | -0.57 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[TMEM41B]] | -0.55 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[STRAP]] | -0.55 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[EIF3CL]] | -0.55 | -0.67 / -0.28 | both halves | 3e-04 |  |
| [[SDHB]] | -0.55 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[UQCRH]] | -0.55 | -0.60 / -0.36 | both halves | 1e-04 |  |
| [[COX6C]] | -0.55 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[ANKRD27]] | -0.54 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[NME2]] | -0.54 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[MYPOP]] | -0.54 | -0.56 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RHNO1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.668). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-43.9, -44.0); signed map (4.6, -32.9). **Vector** length 72.4, 13.3% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Resolution of D-loop Structures through Holliday Junction Intermediates* (reactome, mean cos +0.59 to 4); *Resolution of D-Loop Structures* (reactome, mean cos +0.59 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +5.8 | +6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | +5.3 | +5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +5.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | +4.1 | +5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +1.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.9 | +3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.8 | +0.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.9 | -6.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.2 | -3.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -3.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | RAD9-HUS1-RAD1 interacting nuclear orphan 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.33 — chr12:2,876,258-2,889,524 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HKMT1188, MGC13204, RHINO; previously C12orf32 |
| Reactome | 20 pathways, smallest: Impaired BRCA2 binding to RAD51; HDR through Single Strand Annealing (SSA); Presynaptic phase of homologous DNA pairing and strand exchange |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSD3](https://www.uniprot.org/uniprotkb/Q9BSD3) (RAD9, HUS1, RAD1-interacting nuclear orphan protein 1):

> Involved in microhomology-mediated end-joining (MMEJ) DNA repair by promoting recruitment of polymerase theta (POLQ) to DNA damage sites during mitosis. MMEJ is an alternative non-homologous end-joining (NHEJ) machinery that takes place during mitosis to repair double-strand breaks in DNA that originate in S-phase. Accumulates in M-phase; following phosphorylation by PLK1, interacts with POLQ, enabling its recruitment to double-strand breaks for subsequent repair. Also involved in the DNA …

**Summary**, from NCBI Gene [83695](https://www.ncbi.nlm.nih.gov/gene/83695):

> Enables chromatin-protein adaptor activity. Involved in several processes, including DNA repair; cellular response to radiation; and regulation of cell cycle process. Located in chromosome and nucleus. Is active in chromatin and site of double-strand break. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28206](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28206) · Entrez [83695](https://www.ncbi.nlm.nih.gov/gene/83695) · UniProt [Q9BSD3](https://www.uniprot.org/uniprotkb/Q9BSD3) · Ensembl [ENSG00000171792](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171792)

## Data

Gene col 10161: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10161); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10161, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10161]; `tensor/DDL_lfc|DDL_z.npy` [10161]; `embed/gene_vectors.npy` [10161]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10161 or target_col == 10161). Every well: [[RHNO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHNO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
