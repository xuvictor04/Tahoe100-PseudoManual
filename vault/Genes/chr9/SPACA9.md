---
symbol: "SPACA9"
type: "gene"
col: 9171
ensembl_id: "ENSG00000165698"
name: "sperm acrosome associated 9"
location: "9q34.13"
module: 130
arm: "+"
pooled_cpm: 2.76
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# SPACA9

*sperm acrosome associated 9* — 9q34.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.36× (z +9.7, q 2e-19, up in 5 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bimiralisib (drug)]] 0.5 µM: 1.95× (z +4.0, q 0.008, up in 9 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.495× (z -5.9, q 2e-06, down in 20 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM254]] (+0.67, fdr 7e-06), [[AKAP1-DT]] (+0.67, fdr 7e-06), [[CLN8-AS1]] (+0.66, fdr 7e-06); moves opposite to [[CCT6A]] (-0.57, fdr 2e-05), [[LRP8]] (-0.56, fdr 1e-05), [[NOLC1]] (-0.54, fdr 4e-05).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GIHCG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9171.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.36×** | +9.7 | 2e-19 | 5/6 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.16×** | +6.4 | 4e-08 | 8/17 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +5.7 | 2e-06 | 3/9 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.79×** | +4.8 | 2e-04 | 7/17 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.95×** | +4.0 | 0.008 | 9/27 (Hs 766T, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.6 | 0.027 | 10/32 (PANC-1, SW1417, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.83×** | +3.6 | 0.027 | 4/15 (A498, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.52×** | +3.5 | 0.038 | 8/38 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.078 | 4/44 (SW480, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.72×** | +3.2 | 0.079 | 2/25 (A498, RKO) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.68× | +3.1 | 0.11 | 6/26 (SW480, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9171.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.495×** | -5.9 | 2e-06 | 20/42 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.548×** | -5.0 | 1e-04 | 17/40 (A-427, A-172, …) | all doses, flat | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.576×** | -4.6 | 7e-04 | 18/46 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.649×** | -3.6 | 0.043 | 15/41 (NCI-H460, hTERT-HPNE, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.678× | -3.3 | 0.13 | 9/40 (SW1417, HT-29, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.682× | -3.2 | 0.13 | 13/45 (Hs 766T, NCI-H460, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9171. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 2.75 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0393× (z -13.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.767 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.684 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9171), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM254]] | +0.67 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[AKAP1-DT]] | +0.67 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[CLN8-AS1]] | +0.66 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[HEIH]] | +0.65 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[TP53TG1]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[PIGP]] | +0.63 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[DNAJC27]] | +0.63 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[RRAGC]] | +0.63 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[YY1AP1]] | +0.62 | +0.61 / +0.39 | both halves | 6e-05 |  |
| [[NUDT14]] | +0.61 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[RAB9A]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[VAMP2]] | +0.61 | +0.68 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT6A]] | -0.57 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[LRP8]] | -0.56 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[NOLC1]] | -0.54 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[ASAP2]] | -0.53 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[RRM2]] | -0.53 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[MACROH2A1]] | -0.53 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[TPM3]] | -0.52 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[TCOF1]] | -0.52 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[SNRPA]] | -0.52 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[TMEM181]] | -0.52 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[SLC4A7]] | -0.52 | -0.39 / -0.58 | both halves | 6e-05 |  |
| [[ACOT7]] | -0.51 | -0.49 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GIHCG]] | B | GIHCG activity raises SPACA9's level | lines that do not express GIHCG (9) vs lines expressing it (41) | 1.49× lower at baseline in the lines without GIHCG | 0.049 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, LIX1L, HLTF; maybe low, not absent |
| [[SHISA4]] | C | SHISA4 activity raises SPACA9's level | lines that do not express SHISA4 (3) vs lines expressing it (47) | 1.83× lower at baseline in the lines without SHISA4 | 0.043 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: PPP2R3A, CCDC102A, ENSG00000250264 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-41.8, -17.1); signed map (-8.7, 0.9). **Vector** length 38.1, 4.21% of its response variance represented; |z| ≥ 3 in 792 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +5.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.7 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.3 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -1.9 | -3.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.4 | -5.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -3.3 |
|  | [[Pimozide (drug)]] 5 µM |  | -1.0 | -0.9 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.0 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -0.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | sperm acrosome associated 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.13 — chr9:132,878,027-132,890,201 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Mast; previously C9orf9 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96E40](https://www.uniprot.org/uniprotkb/Q96E40) (Sperm acrosome-associated protein 9):

> Microtubule inner protein (MIP) that maintains the structural integrity of manchette microtubules during spermiogenesis (By similarity). Part of the dynein-decorated doublet microtubules (DMTs) of multiciliated respiratory cells and the distal singlet microtubules of monoflagellated spermatozoa. Forms an extensive interaction network cross-linking the lumen of axonemal doublet microtubules (By similarity).

**Summary**, from NCBI Gene [11092](https://www.ncbi.nlm.nih.gov/gene/11092):

> Enables microtubule binding activity. Involved in axoneme assembly. Located in axonemal microtubule; cytosol; and sperm end piece. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:1367](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1367) · Entrez [11092](https://www.ncbi.nlm.nih.gov/gene/11092) · UniProt [Q96E40](https://www.uniprot.org/uniprotkb/Q96E40) · Ensembl [ENSG00000165698](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165698)

## Data

Gene col 9171: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9171); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9171, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9171]; `tensor/DDL_lfc|DDL_z.npy` [9171]; `embed/gene_vectors.npy` [9171]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9171 or target_col == 9171). Every well: [[SPACA9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPACA9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
