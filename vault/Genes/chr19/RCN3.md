---
symbol: "RCN3"
type: "gene"
col: 6632
ensembl_id: "ENSG00000142552"
name: "reticulocalbin 3"
location: "19q13.33"
module: 56
arm: "+"
pooled_cpm: 6.15
n_lines_expressing: 39
n_dd_up: 5
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# RCN3

*reticulocalbin 3* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.95× (z +7.0, q 1e-09, up in 3 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.78× (z +6.3, q 9e-08, up in 16 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.374× (z -10.3, q 3e-22, down in 24 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB3A]] (+0.63, fdr 2e-05), [[DDB1]] (+0.63, fdr 1e-05), [[AMPD2]] (+0.63, fdr 1e-05); moves opposite to [[ENOX2]] (-0.59, fdr 6e-05), [[ATE1]] (-0.55, fdr 1e-04), [[JADE3]] (-0.54, fdr 7e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[GPR173]] → it (grade B ⚠); 6 go from it, the strongest it → [[CFAP45]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6632.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +7.0 | 1e-09 | 3/9 (NCI-H2347, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.78×** | +6.3 | 9e-08 | 16/37 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.71×** | +5.8 | 1e-06 | 17/37 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.012 | 8/31 (HEC-1-A, A549, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.016 | 12/37 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Posaconazole (drug)]] 5 µM |  | 1.34× | +3.0 | 0.23 | 2/37 (HT-29, AsPC-1) | top dose only | plate-row cell shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6632.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.374×** | -10.3 | 3e-22 | 24/35 (SW 900, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.452×** | -8.7 | 1e-15 | 21/37 (NCI-H1792, SW 900, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.542×** | -6.7 | 3e-09 | 18/37 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.544×** | -6.6 | 3e-09 | 20/30 (SW 900, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.544×** | -6.6 | 3e-09 | 20/37 (H4, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.610×** | -5.4 | 6e-06 | 21/35 (NCI-H1792, H4, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.617×** | -5.1 | 3e-05 | 11/30 (SW 900, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.672×** | -4.4 | 9e-04 | 13/37 (NCI-H1792, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.718×** | -3.6 | 0.017 | 6/37 (C32, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.719×** | -3.6 | 0.017 | 16/29 (SW 900, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.723×** | -3.5 | 0.020 | 13/37 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.810×** | -3.3 | 0.052 | 6/37 (HS-578T, HEC-1-A, …) | top dose only | position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.749×** | -3.2 | 0.068 | 5/35 (AN3 CA, NCI-H1792, …) | inconsistent across doses |  |
| [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM |  | **0.757×** | -3.0 | 0.094 | 6/34 (NCI-H23, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6632. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 31.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -11.9) |
| [[SW 900 (line)]] | alt | 13.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0372× (z -14.0) |
| [[CFPAC-1 (line)]] | alt | 8.86 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.100× (z -10.1) |
| [[SW480 (line)]] | alt | 4.88 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.47× (z +10.0) | — |
| [[C32 (line)]] | wt | 3.71 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.64× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 8.39 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0351× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 3.38 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0826× (z -8.6) |
| [[A-172 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.584 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.990 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.717 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.719 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.15 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6632), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB3A]] | +0.63 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[DDB1]] | +0.63 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[AMPD2]] | +0.63 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[PDXDC2P]] | +0.63 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[MPND]] | +0.62 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[SEC13]] | +0.62 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[COPA]] | +0.61 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[PDXDC1]] | +0.61 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[CCDC9]] | +0.61 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[POFUT2]] | +0.61 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[TMEM39A]] | +0.61 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[COPG1]] | +0.60 | +0.57 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENOX2]] | -0.59 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[ATE1]] | -0.55 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[JADE3]] | -0.54 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[ITPA]] | -0.54 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[NUTM2B-AS1]] | -0.52 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[BMPR1B]] | -0.52 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[DPY19L1P1]] | -0.52 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[TCF12]] | -0.51 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[MED13]] | -0.51 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[SLC25A13]] | -0.51 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[USP25]] | -0.51 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[ARID1B]] | -0.51 | -0.39 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR173]] | B | GPR173 activity raises RCN3's level | lines that do not express GPR173 (30) vs lines expressing it (20) | 2.15× lower at baseline in the lines without GPR173 | 0.031 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2 |
| [[HDAC6]] | B | HDAC6 activity lowers RCN3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TCEA3]] | B | TCEA3 activity raises RCN3's level | lines that do not express TCEA3 (14) vs lines expressing it (36) | 2.01× lower at baseline in the lines without TCEA3 | 0.091 | ⚠ within organs, on part of the lines; also absent: ZNF43, ENSG00000267383, ZNF681; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFAP45]] | B | RCN3 activity lowers CFAP45's level | lines that do not express RCN3 (11) vs lines expressing it (39) | 1.70× higher at baseline in the lines without RCN3 | 0.028 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[GOLGA2]] | B | RCN3 activity lowers GOLGA2's level | lines that do not express RCN3 (11) vs lines expressing it (39) | 1.53× higher at baseline in the lines without RCN3 | 0.050 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[RUFY3]] | B | RCN3 activity raises RUFY3's level | lines that do not express RCN3 (11) vs lines expressing it (39) | 1.51× lower at baseline in the lines without RCN3 | 0.059 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[RAP1GAP]] | B | RCN3 activity raises RAP1GAP's level | lines that do not express RCN3 (11) vs lines expressing it (39) | 1.71× lower at baseline in the lines without RCN3 | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ZNF404]] | B | RCN3 activity lowers ZNF404's level | lines that do not express RCN3 (11) vs lines expressing it (39) | 1.29× higher at baseline in the lines without RCN3 | 0.082 | ⚠ within organs, on part of the lines; maybe low, not absent |
| cells under [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM | B | RCN3 activity raises the cells' numbers under Diammonium Glycyrrhizinate 0.5 µM (protects the cells) | lines that do not express RCN3 (11) vs lines expressing it (37) | the lines without RCN3: 0.87× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.610). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.9, -31.2); signed map (-51.9, 6.3). **Vector** length 56.0, 8.50% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antigen Presentation: Folding, assembly and peptide loading of class I MHC* (reactome, mean cos +0.54 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.6 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.3 | +0.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.3 | +6.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +0.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +0.4 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.2 | +1.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -8.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -5.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -6.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.3 | -10.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.3 | -6.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -1.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | reticulocalbin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,528,003-49,546,962 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RLP49 |
| Gene groups (HGNC) | CREC family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96D15](https://www.uniprot.org/uniprotkb/Q96D15) (Reticulocalbin-3):

> Probable molecular chaperone assisting protein biosynthesis and transport in the endoplasmic reticulum. Required for the proper biosynthesis and transport of pulmonary surfactant-associated protein A/SP-A, pulmonary surfactant-associated protein D/SP-D and the lipid transporter ABCA3 (By similarity). By regulating both the proper expression and the degradation through the endoplasmic reticulum-associated protein degradation pathway of these proteins plays a crucial role in pulmonary surfactant …

**Summary**, from NCBI Gene [57333](https://www.ncbi.nlm.nih.gov/gene/57333):

> Enables calcium ion binding activity. Involved in several processes, including collagen biosynthetic process; positive regulation of peptidase activity; and regulation of phosphatidylinositol 3-kinase/protein kinase B signal transduction. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21145](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21145) · Entrez [57333](https://www.ncbi.nlm.nih.gov/gene/57333) · UniProt [Q96D15](https://www.uniprot.org/uniprotkb/Q96D15) · Ensembl [ENSG00000142552](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142552)

## Data

Gene col 6632: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6632); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6632, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6632]; `tensor/DDL_lfc|DDL_z.npy` [6632]; `embed/gene_vectors.npy` [6632]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6632 or target_col == 6632). Every well: [[RCN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RCN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
