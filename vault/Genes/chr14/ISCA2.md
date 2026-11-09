---
symbol: "ISCA2"
type: "gene"
col: 9202
ensembl_id: "ENSG00000165898"
name: "iron-sulfur cluster assembly 2"
location: "14q24.3"
module: 24
arm: "+"
pooled_cpm: 5.49
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 6
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# ISCA2

*iron-sulfur cluster assembly 2* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.90× (z +5.8, q 4e-06, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.475× (z -6.7, q 2e-08, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPATCH11]] (+0.76, fdr 9e-06), [[TRAPPC5]] (+0.71, fdr 2e-05), [[POLR2J]] (+0.70, fdr 3e-05, ⚠ POLR2J in the vector space only through flagged drug-doses), [[NDUFA8]] (+0.70, fdr 1e-05); moves opposite to [[GTF3C2-AS2]] (-0.70, fdr 2e-05), [[MSTO1]] (-0.67, fdr 3e-04), [[CROCC]] (-0.65, fdr 1e-03, ⚠ one half only (not replicated)), [[C2orf88]] (-0.64, fdr 6e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9202.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +5.8 | 4e-06 | 30/47 (CFPAC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.72×** | +4.9 | 3e-04 | 22/47 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +4.7 | 5e-04 | 17/47 (RKO, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +4.4 | 0.002 | 5/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.62×** | +4.3 | 0.002 | 17/40 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.57×** | +4.0 | 0.005 | 16/34 (SW1417, HOP62, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9202.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.475×** | -6.7 | 2e-08 | 27/46 (HepG2/C3A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.603×** | -4.5 | 0.002 | 19/47 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.711×** | -4.3 | 0.003 | 17/40 (A498, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.402×** | -4.2 | 0.004 | 18/43 (NCI-H2347, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.647×** | -3.9 | 0.012 | 13/47 (SW 900, NCI-H23, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.665×** | -3.6 | 0.025 | 17/40 (SW 900, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.511× | -3.1 | 0.17 | 13/39 (Panc 03.27, J82, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.712× | -3.0 | 0.17 | 15/46 (KATO III, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9202. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 4.99 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0392× (z -9.9) |
| [[HOP62 (line)]] | alt | 4.59 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0440× (z -11.8) |
| [[A-172 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9202), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 14 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH11]] | +0.76 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[TRAPPC5]] | +0.71 | +0.46 / +0.71 | both halves | 2e-05 |  |
| [[POLR2J]] ⚠ | +0.70 | +0.44 / +0.68 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NDUFA8]] | +0.70 | +0.56 / +0.67 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[ASB8]] | +0.69 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[COA3]] | +0.68 | +0.54 / +0.75 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[TUBG2]] | +0.68 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[SNAPIN]] | +0.67 | +0.39 / +0.71 | both halves | 5e-05 |  |
| [[PITPNA-AS1]] | +0.67 | +0.37 / +0.65 | both halves | 7e-05 |  |
| [[C18orf21]] | +0.67 | +0.43 / +0.76 | both halves | 3e-05 |  |
| [[DCTN3]] | +0.66 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[MRPL43]] | +0.65 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[ZNF22]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF3C2-AS2]] | -0.70 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[MSTO1]] | -0.67 | -0.29 / -0.55 | both halves | 3e-04 |  |
| [[CROCC]] | -0.65 | -0.18 / -0.58 | ⚠ one half (not replicated) | 1e-03 |  |
| [[C2orf88]] | -0.64 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[RCC1]] | -0.63 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[GLIPR1-AS1]] | -0.62 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[CCDC200]] | -0.62 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[U2AF2]] | -0.62 | -0.15 / -0.60 | ⚠ one half (not replicated) | 0.001 |  |
| [[PSMD6-AS1]] | -0.62 | -0.19 / -0.56 | ⚠ one half (not replicated) | 8e-04 |  |
| [[UBQLN4]] | -0.62 | -0.34 / -0.59 | both halves | 1e-04 |  |
| [[BHLHE40-AS1]] | -0.61 | -0.44 / -0.40 | both halves | 4e-05 |  |
| [[SNHG22]] | -0.61 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[CCDC62]] | -0.61 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[LY6G5B]] | -0.61 | -0.24 / -0.67 | both halves | 5e-04 |  |
| [[SRSF1]] | -0.61 | -0.25 / -0.62 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ISCA2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.510). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-42.9, -6.8); signed map (-18.1, -7.9). **Vector** length 52.8, 7.79% of its response variance represented; |z| ≥ 3 in 705 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +2.5 | +4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.5 | +5.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.0 | +4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +1.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +1.9 | +4.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +0.9 | +2.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.9 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.9 | -0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.9 | +1.5 |
|  | [[Thymol (drug)]] 5 µM |  | +0.8 | +2.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.9 | +1.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -2.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.4 | +0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -0.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.0 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | iron-sulfur cluster assembly 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:74,493,756-74,497,106 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ISA2; previously HBLD1 |
| Gene groups (HGNC) | Mitochondrial iron-sulfur assembly components |
| Reactome | 4 pathways, smallest: Mitochondrial iron-sulfur cluster biogenesis; Maturation of TCA enzymes and regulation of TCA cycle; Citric acid cycle (TCA cycle) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86U28](https://www.uniprot.org/uniprotkb/Q86U28) (Iron-sulfur cluster assembly 2 homolog, mitochondrial):

> Involved in the maturation of mitochondrial 4Fe-4S proteins functioning late in the iron-sulfur cluster assembly pathway. May be involved in the binding of an intermediate of Fe/S cluster assembly.

**Summary**, from NCBI Gene [122961](https://www.ncbi.nlm.nih.gov/gene/122961):

> The protein encoded by this gene is an A-type iron-sulfur cluster (ISC) protein found in mitochondria. The encoded protein appears to be involved in the maturation of mitochondrial iron-sulfur proteins. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:19857](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19857) · Entrez [122961](https://www.ncbi.nlm.nih.gov/gene/122961) · UniProt [Q86U28](https://www.uniprot.org/uniprotkb/Q86U28) · Ensembl [ENSG00000165898](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165898)

## Data

Gene col 9202: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9202); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9202, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9202]; `tensor/DDL_lfc|DDL_z.npy` [9202]; `embed/gene_vectors.npy` [9202]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9202 or target_col == 9202). Every well: [[ISCA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ISCA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
