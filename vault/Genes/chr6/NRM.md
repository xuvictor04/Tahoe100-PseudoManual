---
symbol: "NRM"
type: "gene"
col: 6008
ensembl_id: "ENSG00000137404"
name: "nurim"
location: "6p21.33"
module: 67
arm: "+"
pooled_cpm: 2.59
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# NRM

*nurim* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.30× (z +11.8, q 2e-29, up in 8 of 8 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Cobimetinib (drug)]] 0.05 µM: 1.49× (z +3.1, q 0.086, up in 5 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.595× (z -4.1, q 0.021, down in 18 of 41 measured lines) ⚠ cell-cycle shift, explains ~40% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 0.5 µM in 1 line (A-427 0.0516×; ⚠ cell-cycle shift, explains ~93% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TK1]] (+0.66, fdr 7e-06), [[NUDT1]] (+0.66, fdr 7e-06), [[GGH]] (+0.64, fdr 1e-05); moves opposite to [[ZC3H8]] (-0.54, fdr 2e-04), [[ZNF600]] (-0.53, fdr 9e-05), [[DNAJC2]] (-0.52, fdr 5e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 11 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6008.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **4.30×** | +11.8 | 2e-29 | 8/8 (A498, J82, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **3.92×** | +11.5 | 4e-28 | 12/13 (A498, J82, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.04×** | +8.7 | 9e-16 | 6/8 (J82, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.31×** | +7.8 | 6e-13 | 28/48 (HOP62, J82, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.95×** | +5.6 | 2e-06 | 20/44 (KATO III, BT-474, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.97×** | +5.5 | 4e-06 | 13/23 (A498, PANC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.91×** | +5.5 | 4e-06 | 6/15 (KATO III, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.85×** | +5.2 | 2e-05 | 15/44 (SW480, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.72×** | +4.6 | 3e-04 | 14/46 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.3 | 0.001 | 3/14 (NCI-H2347, J82, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.40×** | +4.0 | 0.003 | 9/31 (NCI-H2347, C32, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.49×** | +3.1 | 0.086 | 5/29 (NCI-H2030, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6008.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 0.5 µM in 1 line (A-427 0.0516×; ⚠ cell-cycle shift, explains ~93% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.595×** | -4.1 | 0.021 | 18/41 (HOP62, BT-474, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.675× | -3.3 | 0.28 | 8/42 (LS 180, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6008. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 2.87 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0516× (z -9.4) ⚠ cell-cycle shift, explains ~93% of this change |
| [[A-172 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.748 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.982 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.69 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6008), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TK1]] | +0.66 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[NUDT1]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[GGH]] | +0.64 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[STIL]] | +0.63 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[UBE2T]] | +0.63 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[RNASEH2A]] | +0.62 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[NCAPG2]] | +0.62 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[GINS2]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ZDHHC12]] | +0.62 | +0.64 / +0.40 | both halves | 5e-05 |  |
| [[TTK]] | +0.62 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[NCAPH]] | +0.61 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[H2AZ2]] | +0.60 | +0.66 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H8]] | -0.54 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[ZNF600]] | -0.53 | -0.49 / -0.37 | both halves | 9e-05 |  |
| [[DNAJC2]] | -0.52 | -0.54 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises NRM's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.40× lower at baseline in the lines without PIMREG | 0.016 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises NRM's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.34× lower at baseline in the lines without TCF19 | 0.023 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises NRM's level | lines that do not express AURKB (4) vs lines expressing it (46) | 1.45× lower at baseline in the lines without AURKB | 0.029 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[E2F1]] | C | E2F1 activity raises NRM's level | lines that do not express E2F1 (3) vs lines expressing it (47) | 1.60× lower at baseline in the lines without E2F1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p |
| [[DIAPH3]], [[MELK]], [[TK1]] | C | DIAPH3, MELK, TK1 activity raises NRM's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 1.47× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[PKMYT1]] | C | PKMYT1 activity raises NRM's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 1.44× lower at baseline in the lines without PKMYT1 | 0.084 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-31.4, -50.8); signed map (-42.7, -38.8). **Vector** length 45.2, 5.40% of its response variance represented; |z| ≥ 3 in 873 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.56 to 12); *G2/M checkpoint* (hallmark, mean cos +0.53 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +3.1 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +3.0 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +2.6 | +8.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | +2.6 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.0 | +2.6 |
|  | [[Flutamide (drug)]] 5 µM |  | +0.9 | +1.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +0.9 | +2.3 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.4 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~93% of this change | -1.8 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | nurim |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:30,688,047-30,691,420 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NRM29 |
| Gene groups (HGNC) | Membrane-bound methyltransferase family |
| Matched by | ensembl_id |

UniProt [Q8IXM6](https://www.uniprot.org/uniprotkb/Q8IXM6) carries no function annotation.

**Summary**, from NCBI Gene [11270](https://www.ncbi.nlm.nih.gov/gene/11270):

> The protein encoded by this gene contains transmembrane domains and resides within the inner nuclear membrane, where it is tightly associated with the nucleus. This protein shares homology with isoprenylcysteine carboxymethyltransferase enzymes. Alternative splicing results in multiple transcript variants that encode different protein isoforms. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:8003](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8003) · Entrez [11270](https://www.ncbi.nlm.nih.gov/gene/11270) · UniProt [Q8IXM6](https://www.uniprot.org/uniprotkb/Q8IXM6) · Ensembl [ENSG00000137404](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137404)

## Data

Gene col 6008: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6008); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6008, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6008]; `tensor/DDL_lfc|DDL_z.npy` [6008]; `embed/gene_vectors.npy` [6008]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6008 or target_col == 6008). Every well: [[NRM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
