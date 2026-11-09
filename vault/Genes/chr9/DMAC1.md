---
symbol: "DMAC1"
type: "gene"
col: 5957
ensembl_id: "ENSG00000137038"
name: "distal membrane arm assembly component 1"
location: "9p24.1"
module: 11
arm: "+"
pooled_cpm: 11.86
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 11
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# DMAC1

*distal membrane arm assembly component 1* — 9p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.38× (z +5.7, q 6e-06, up in 33 of 38 measured lines) ⚠ toxic. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A549 7.89×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.397× (z -6.3, q 2e-07, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL57]] (+0.73, fdr 1e-05), [[ZNF330]] (+0.68, fdr 1e-05), [[GTF2H5]] (+0.67, fdr 1e-05); moves opposite to [[NUCB1]] (-0.60, fdr 2e-05), [[UFD1]] (-0.59, fdr 1e-05), [[SUDS3]] (-0.57, fdr 4e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NUDT11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5957.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A549 7.89×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.38×** | +5.7 | 6e-06 | 33/38 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.29×** | +5.5 | 1e-05 | 20/22 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.16×** | +5.3 | 3e-05 | 23/34 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.65×** | +3.4 | 0.083 | 23/42 (CFPAC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | 1.63× | +3.1 | 0.23 | 13/28 (HT-29, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Arbutin (drug)]] 5 µM |  | 1.58× | +3.0 | 0.23 | 19/45 (A498, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5957.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.397×** | -6.3 | 2e-07 | 38/46 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.458×** | -5.3 | 3e-05 | 34/45 (SNU-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.465×** | -5.2 | 4e-05 | 29/45 (LoVo, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.441×** | -4.6 | 5e-04 | 30/44 (SW480, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.639×** | -4.3 | 0.002 | 30/45 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.552×** | -4.0 | 0.005 | 27/46 (LS 180, KATO III, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.559×** | -3.9 | 0.006 | 28/45 (HEC-1-A, LS 180, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.584×** | -3.6 | 0.019 | 24/45 (HepG2/C3A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.598×** | -3.5 | 0.030 | 23/46 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.383×** | -3.4 | 0.036 | 20/45 (NCI-H1573, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.387×** | -3.4 | 0.037 | 24/45 (RKO, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5957. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 13.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.89× (z +8.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 19.4 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.180× (z -8.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[LS 180 (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.119× (z -9.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SNU-1 (line)]] | wt | 10.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0568× (z -9.1) |
| [[A-172 (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5957), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 9 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL57]] | +0.73 | +0.57 / +0.79 | both halves | 1e-05 |  |
| [[ZNF330]] | +0.68 | +0.56 / +0.77 | both halves | 1e-05 |  |
| [[GTF2H5]] | +0.67 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[WDR75]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[MRPL15]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[PET117]] | +0.64 | +0.40 / +0.74 | both halves | 5e-05 | same gene group; pathway: Aerobic respiration and respiratory electron transport |
| [[MTLN]] ⚠ | +0.63 | +0.41 / +0.73 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF593]] | +0.63 | +0.41 / +0.74 | both halves | 4e-05 |  |
| [[DNPH1]] | +0.63 | +0.39 / +0.73 | both halves | 6e-05 |  |
| [[MPLKIP]] | +0.62 | +0.44 / +0.76 | both halves | 3e-05 |  |
| [[GEMIN6]] | +0.61 | +0.43 / +0.68 | both halves | 3e-05 |  |
| [[MFSD3]] | +0.61 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[BRIX1]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUCB1]] | -0.60 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[UFD1]] | -0.59 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[SUDS3]] | -0.57 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[MAN2B2]] | -0.56 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[STX16]] | -0.55 | -0.30 / -0.68 | both halves | 2e-04 |  |
| [[MAPK9]] | -0.54 | -0.37 / -0.59 | both halves | 8e-05 |  |
| [[IL18BP]] | -0.53 | -0.27 / -0.61 | both halves | 3e-04 |  |
| [[KCNIP2]] | -0.53 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[MTCH1]] | -0.52 | -0.62 / -0.36 | both halves | 1e-04 |  |
| [[ABCB8]] | -0.52 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[DVL3]] | -0.52 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[ACADVL]] | -0.52 | -0.34 / -0.58 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUDT11]] | B | NUDT11 activity raises DMAC1's level | lines that do not express NUDT11 (24) vs lines expressing it (26) | 1.07× lower at baseline in the lines without NUDT11 | 0.005 | ⚠ within organs, on part of the lines; also absent: RNF182, ADAMTS10, NPTX1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.476). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-47.5, -10.0); signed map (-13.9, -8.5). **Vector** length 58.5, 12.7% of its response variance represented; |z| ≥ 3 in 611 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +5.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +0.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +1.0 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.1 | +2.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.0 | +1.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.6 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -3.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.1 | -4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.6 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -2.1 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -1.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -3.4 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | distal membrane arm assembly component 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.1 — chr9:7,796,500-7,888,380 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4730; previously C9orf123, TMEM261 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GE9](https://www.uniprot.org/uniprotkb/Q96GE9) (Distal membrane-arm assembly complex protein 1):

> Required for the assembly of the mitochondrial NADH:ubiquinone oxidoreductase complex (complex I). Involved in the assembly of the distal region of complex I.

**Summary**, from NCBI Gene [90871](https://www.ncbi.nlm.nih.gov/gene/90871):

> Involved in mitochondrial respiratory chain complex I assembly. Located in mitochondrial inner membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30536](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30536) · Entrez [90871](https://www.ncbi.nlm.nih.gov/gene/90871) · UniProt [Q96GE9](https://www.uniprot.org/uniprotkb/Q96GE9) · Ensembl [ENSG00000137038](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137038)

## Data

Gene col 5957: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5957); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5957, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5957]; `tensor/DDL_lfc|DDL_z.npy` [5957]; `embed/gene_vectors.npy` [5957]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5957 or target_col == 5957). Every well: [[DMAC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DMAC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
