---
symbol: "CDKN2D"
type: "gene"
col: 4970
ensembl_id: "ENSG00000129355"
name: "cyclin dependent kinase inhibitor 2D"
location: "19p13.2"
module: 3
arm: "+"
pooled_cpm: 9.49
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CDKN2D

*cyclin dependent kinase inhibitor 2D* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.77× (z +8.2, q 1e-13, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.482× (z -4.3, q 0.008, down in 29 of 44 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.330× (z -3.6, q 0.060, down in 24 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 1 line (SK-MEL-2 0.0330×); [[Selinexor (drug)]] 5 µM in 1 line (C32 0.196×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WIPF2]] (+0.76, fdr 7e-06), [[FAM89B]] (+0.75, fdr 7e-06), [[SIGIRR]] (+0.73, fdr 1e-05); moves opposite to [[TMX3]] (-0.71, fdr 7e-06), [[ABCF2]] (-0.71, fdr 7e-06), [[NAA50]] (-0.70, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ABCC2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4970.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.77×** | +8.2 | 1e-13 | 45/47 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.45×** | +7.7 | 5e-12 | 44/47 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.91×** | +6.6 | 7e-09 | 43/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.02×** | +4.4 | 0.002 | 34/47 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | **1.93×** | +4.1 | 0.005 | 28/42 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.81×** | +3.7 | 0.022 | 27/43 (LoVo, SNU-423, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.48×** | +3.5 | 0.043 | 19/43 (LoVo, A-427, …) | top dose only | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +3.4 | 0.043 | 17/37 (NCI-H2030, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +3.1 | 0.14 | 13/48 (NCI-H2347, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4970.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 1 line (SK-MEL-2 0.0330×); [[Selinexor (drug)]] 5 µM in 1 line (C32 0.196×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.482×** | -4.3 | 0.008 | 29/44 (A-172, H4, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.510×** | -4.2 | 0.008 | 28/47 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.330×** | -3.6 | 0.060 | 24/43 (A-172, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.357× | -3.3 | 0.12 | 21/42 (LS 180, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.595× | -3.2 | 0.14 | 22/47 (A-172, HS-578T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.86 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4970. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.196× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 14.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0330× (z -13.4) |
| [[A-172 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.26 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4970), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WIPF2]] | +0.76 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[FAM89B]] | +0.75 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[SIGIRR]] | +0.73 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[CARHSP1]] | +0.73 | +0.43 / +0.71 | both halves | 3e-05 |  |
| [[TMEM191A-1]] | +0.72 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[GPX4]] | +0.72 | +0.59 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_REACTIVE_OXYGEN_SPECIES_PATHWAY |
| [[ARID3A]] | +0.72 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[LGALS1]] | +0.71 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[RRAS]] | +0.71 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[LIN7B]] | +0.70 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[MINDY2]] | +0.70 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[RNF114]] | +0.70 | +0.48 / +0.64 | both halves | 2e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMX3]] | -0.71 | -0.65 / -0.76 | both halves | 7e-06 |  |
| [[ABCF2]] | -0.71 | -0.65 / -0.69 | both halves | 7e-06 |  |
| [[NAA50]] | -0.70 | -0.57 / -0.72 | both halves | 1e-05 |  |
| [[UTP20]] | -0.69 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[PSME3]] | -0.68 | -0.61 / -0.66 | both halves | 7e-06 |  |
| [[VPS52]] | -0.68 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[RCN1]] | -0.68 | -0.42 / -0.67 | both halves | 4e-05 |  |
| [[ZNF300]] | -0.67 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[DARS2]] | -0.67 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[ILF3]] | -0.67 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[CCT7]] | -0.66 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[EPM2A]] | -0.66 | -0.50 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCC2]] | B | ABCC2 activity lowers CDKN2D's level | lines that do not express ABCC2 (22) vs lines expressing it (28) | 1.29× higher at baseline in the lines without ABCC2 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, NR0B1, DNAJC12; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers CDKN2D's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PIM2]] | C | PIM2 activity lowers CDKN2D's level | lines that do not express PIM2 (3) vs lines expressing it (47) | 2.26× higher at baseline in the lines without PIM2 | 0.026 | ⚠ few lines (3 vs 47); across organs; also absent: JMJD8, CHD7, CYP2R1; maybe low, not absent |
| [[FUCA2]] | C | FUCA2 activity raises CDKN2D's level | lines that do not express FUCA2 (3) vs lines expressing it (47) | 1.95× lower at baseline in the lines without FUCA2 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPX1, AIFM2, SP100; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.723). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-22.7, -29.4); signed map (-28.2, 15.6). **Vector** length 103, 30.9% of its response variance represented; |z| ≥ 3 in 697 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.2 | +6.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.2 | +8.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.0 | +7.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.6 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +2.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.5 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.5 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.8 | +2.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.1 | -2.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.5 | -0.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.3 | -4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.1 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | +0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase inhibitor 2D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,566,460-10,569,059 (-) |
| Ensembl biotype | protein_coding |
| Also known as | INK4D, p19 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Cyclin dependent kinase inhibitor 2 family |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY |
| Reactome | 11 pathways, smallest: Oncogene Induced Senescence; Cyclin D associated events in G1; G1 Phase |
| Matched by | ensembl_id |

**Function**, from UniProt [P55273](https://www.uniprot.org/uniprotkb/P55273) (Cyclin-dependent kinase 4 inhibitor D):

> Interacts strongly with CDK4 and CDK6 and inhibits them.

**Summary**, from NCBI Gene [1032](https://www.ncbi.nlm.nih.gov/gene/1032):

> The protein encoded by this gene is a member of the INK4 family of cyclin-dependent kinase inhibitors. This protein has been shown to form a stable complex with CDK4 or CDK6, and prevent the activation of the CDK kinases, thus function as a cell growth regulator that controls cell cycle G1 progression. The abundance of the transcript of this gene was found to oscillate in a cell-cycle dependent manner with the lowest expression at mid G1 and a maximal expression during S phase. The negative …

**Accessions** — [HGNC:1790](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1790) · Entrez [1032](https://www.ncbi.nlm.nih.gov/gene/1032) · UniProt [P55273](https://www.uniprot.org/uniprotkb/P55273) · Ensembl [ENSG00000129355](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129355)

## Data

Gene col 4970: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4970); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4970, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4970]; `tensor/DDL_lfc|DDL_z.npy` [4970]; `embed/gene_vectors.npy` [4970]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4970 or target_col == 4970). Every well: [[CDKN2D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDKN2D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
