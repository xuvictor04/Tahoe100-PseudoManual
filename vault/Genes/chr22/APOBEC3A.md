---
symbol: "APOBEC3A"
type: "gene"
col: 4880
ensembl_id: "ENSG00000128383"
name: "apolipoprotein B mRNA editing enzyme catalytic subunit 3A"
location: "22q13.1"
module: 91
arm: "+"
pooled_cpm: 7.6
n_lines_expressing: 44
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# APOBEC3A

*apolipoprotein B mRNA editing enzyme catalytic subunit 3A* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.04× (z +9.2, q 3e-17, up in 22 of 33 measured lines) ⚠ cell-cycle shift, explains ~66% of this change. The strongest without an alert is [[Cytarabine (hydrochloride) (drug)]] 5 µM: 1.58× (z +4.0, q 0.004, up in 10 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.661× (z -3.8, q 0.081, down in 14 of 39 measured lines) ⚠ cell-cycle shift, explains ~96% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (HT-29 0.0526×); [[Selinexor (drug)]] 5 µM in 1 line (A498 0.246×; ⚠ cell-cycle shift, would explain all of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (PANC-1 0.0778×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APOBEC3B]] (+0.68, fdr 7e-06, ⚠ same locus), [[FAM111A]] (+0.62, fdr 7e-06), [[BRCA2]] (+0.61, fdr 7e-06), [[ISG20]] (+0.59, fdr 1e-05); moves opposite to [[RPS7]] (-0.50, fdr 3e-05), [[EIF3CL]] (-0.48, fdr 3e-05), [[URI1]] (-0.47, fdr 3e-05).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[OVOL1]] → it (grade B ⚠); 2 go from it, the strongest it → [[CCT6P3-1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4880.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **2.04×** | +9.2 | 3e-17 | 22/33 (A549, NCI-H2030, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **2.31×** | +7.6 | 8e-12 | 17/23 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.33×** | +7.4 | 3e-11 | 7/11 (SW480, J82, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.21×** | +6.9 | 5e-10 | 27/38 (LoVo, NCI-H1573, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.11×** | +6.8 | 1e-09 | 23/34 (NCI-H2030, A549, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.86×** | +5.6 | 2e-06 | 24/40 (NCI-H1573, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.78×** | +4.8 | 1e-04 | 8/16 (Panc 03.27, J82, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **1.60×** | +4.1 | 0.003 | 14/29 (LoVo, SW1417, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~72% of this change | **1.57×** | +4.1 | 0.003 | 7/28 (CFPAC-1, COLO 205, …) | inconsistent across doses | low cells (technical?) |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.0 | 0.004 | 10/38 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +3.8 | 0.006 | 9/42 (SW480, RKO, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.007 | 15/35 (C32, J82, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.78×** | +3.7 | 0.009 | 10/36 (HCT15, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[5-Fluorouracil (drug)]] 0.5 µM |  | **1.48×** | +3.5 | 0.016 | 8/38 (BT-474, H4, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.022 | 13/41 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.59×** | +3.0 | 0.078 | 6/38 (CFPAC-1, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4880.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (HT-29 0.0526×); [[Selinexor (drug)]] 5 µM in 1 line (A498 0.246×; ⚠ cell-cycle shift, would explain all of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (PANC-1 0.0778×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **0.661×** | -3.8 | 0.081 | 14/39 (H4, A498, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.691× | -3.4 | 0.19 | 12/37 (NCI-H2347, NCI-H1573, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.696× | -3.1 | 0.24 | 14/39 (C32, NCI-H1792, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | 0.697× | -3.1 | 0.24 | 15/38 (KATO III, H4, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.718× | -3.1 | 0.26 | 8/41 (NCI-H2347, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.62 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4880. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.246× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 3.76 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.81× (z +10.2) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[HT-29 (line)]] | alt | 6.78 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0526× (z -10.3) |
| [[PANC-1 (line)]] | alt | 2.07 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0778× (z -8.7) |
| [[A-172 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.760 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4880), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APOBEC3B]] | +0.68 | +0.64 / +0.68 | both halves | 7e-06 | same gene group; pathway: Formation of the Editosome; STRING 939; ⚠ same locus (19.2 kb, same strand: neighbours can correlate without regulation) |
| [[FAM111A]] | +0.62 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[BRCA2]] | +0.61 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ISG20]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[MASTL]] | +0.59 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[REXO5]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[FBXO48]] | +0.57 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[RHNO1]] | +0.55 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[SGO1]] | +0.55 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[THSD8]] ⚠ | +0.54 | +0.59 / +0.54 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ESCO2]] | +0.53 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[SERTAD4]] | +0.53 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[PMAIP1]] | +0.53 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[NFATC2]] | +0.52 | +0.41 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS7]] | -0.50 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[EIF3CL]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[URI1]] | -0.47 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[UBE2F]] | -0.47 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[STRAP]] | -0.47 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[RPS3A]] | -0.47 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[EBPL]] | -0.47 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[PMS2P3]] | -0.46 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[FAR1]] | -0.46 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[DDX54]] | -0.46 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[MRPS35]] | -0.45 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[DCUN1D5]] | -0.45 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OVOL1]] | B | OVOL1 activity raises APOBEC3A's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 2.21× lower at baseline in the lines without OVOL1 | 0.036 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[DAPP1]] | B | DAPP1 activity raises APOBEC3A's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 1.90× lower at baseline in the lines without DAPP1 | 0.093 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCT6P3-1]] | B | APOBEC3A activity raises CCT6P3-1's level | lines that do not express APOBEC3A (6) vs lines expressing it (44) | 1.37× lower at baseline in the lines without APOBEC3A | 0.093 | ⚠ within organs, on part of the lines; also absent: PBX4, CTSV, APOBEC3B; maybe low, not absent |
| [[APOBEC3B]] | C | APOBEC3A activity raises APOBEC3B's level | lines that do not express APOBEC3A (6) vs lines expressing it (44) | 2.09× lower at baseline in the lines without APOBEC3A | 0.068 | ⚠ within organs, on part of the lines; also absent: PBX4, CTSV, APOBEC3B; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.572). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-41.9, -47.8); signed map (-43.9, -48.8). **Vector** length 77.6, 16.9% of its response variance represented; |z| ≥ 3 in 766 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +4.3 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +3.6 | +9.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.0 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +3.0 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | +2.9 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +2.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +3.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | -2.8 | -3.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.4 | -2.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~96% of this change | -2.4 | -3.8 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -0.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | apolipoprotein B mRNA editing enzyme catalytic subunit 3A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:38,952,741-38,963,184 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARP3, PHRBN |
| Gene groups (HGNC) | Apolipoprotein B mRNA editing enzyme catalytic subunits |
| Reactome | 4 pathways, smallest: Formation of the Editosome; mRNA Editing: C to U Conversion; mRNA Editing |
| Matched by | ensembl_id |

**Function**, from UniProt [P31941](https://www.uniprot.org/uniprotkb/P31941) (DNA dC->dU-editing enzyme APOBEC-3A):

> DNA deaminase (cytidine deaminase) with restriction activity against viruses, foreign DNA and mobility of retrotransposons. Exhibits antiviral activity against adeno-associated virus (AAV) and human T-cell leukemia virus type 1 (HTLV-1) and may inhibit the mobility of LTR and non-LTR retrotransposons. Selectively targets single-stranded DNA and can deaminate both methylcytosine and cytosine in foreign DNA. Can induce somatic hypermutation in the nuclear and mitochondrial DNA. May also play a …

**Summary**, from NCBI Gene [200315](https://www.ncbi.nlm.nih.gov/gene/200315):

> This gene is a member of the cytidine deaminase gene family. It is one of seven related genes or pseudogenes found in a cluster, thought to result from gene duplication, on chromosome 22. Members of the cluster encode proteins that are structurally and functionally related to the C to U RNA-editing cytidine deaminase APOBEC1. The protein encoded by this gene lacks the zinc binding activity of other family members. The protein plays a role in immunity, by restricting transmission of foreign DNA …

**Accessions** — [HGNC:17343](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17343) · Entrez [200315](https://www.ncbi.nlm.nih.gov/gene/200315) · UniProt [P31941](https://www.uniprot.org/uniprotkb/P31941) · Ensembl [ENSG00000128383](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128383)

## Data

Gene col 4880: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4880); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4880, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4880]; `tensor/DDL_lfc|DDL_z.npy` [4880]; `embed/gene_vectors.npy` [4880]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4880 or target_col == 4880). Every well: [[APOBEC3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APOBEC3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
