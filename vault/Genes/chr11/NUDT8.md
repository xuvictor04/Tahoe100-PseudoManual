---
symbol: "NUDT8"
type: "gene"
col: 9545
ensembl_id: "ENSG00000167799"
name: "nudix hydrolase 8"
location: "11q13.2"
module: 24
arm: "+"
pooled_cpm: 2.01
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 6
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# NUDT8

*nudix hydrolase 8* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.84× (z +7.7, q 1e-11, up in 8 of 11 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.359× (z -5.8, q 3e-06, down in 21 of 43 measured lines).
> Its strongest partners by |cos| (72 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 32 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GCHFR]] (+0.70, fdr 1e-05), [[SAC3D1]] (+0.67, fdr 1e-04), [[NDUFA7]] (+0.66, fdr 3e-05); moves opposite to [[UBE2V1]] (-0.60, fdr 3e-04), [[WASH8P]] (-0.52, fdr 2e-04, ⚠ WASH8P in the vector space only through flagged drug-doses), [[LIN7C]] (-0.51, fdr 0.002, ⚠ one half only (not replicated)), [[IL18BP]] (-0.50, fdr 4e-04), [[TARDBP]] (-0.50, fdr 4e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF655]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9545.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **3.84×** | +7.7 | 1e-11 | 8/11 (KATO III, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.81×** | +7.3 | 6e-11 | 0/1 | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.61×** | +5.5 | 8e-06 | 7/11 (KATO III, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.43×** | +4.7 | 4e-04 | 0/4 | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.47× | +3.1 | 0.20 | 8/22 (LoVo, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9545.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.359×** | -5.8 | 3e-06 | 21/43 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.459×** | -4.4 | 0.003 | 18/37 (A-172, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.479×** | -4.2 | 0.005 | 16/32 (Hs 766T, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.515×** | -3.6 | 0.044 | 14/30 (SW1417, NCI-H1573, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.537×** | -3.5 | 0.044 | 8/27 (NCI-H2030, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.556×** | -3.3 | 0.077 | 15/37 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.573× | -3.2 | 0.12 | 12/34 (J82, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.556× | -3.1 | 0.12 | 12/40 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.567× | -3.1 | 0.12 | 13/34 (LS 180, SW1417, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.560× | -3.1 | 0.12 | 7/37 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.685× | -3.0 | 0.12 | 14/27 (NCI-H2030, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.59 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9545. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 4.86 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -10.1) |
| [[LS 180 (line)]] | wt | 3.96 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0426× (z -8.7) |
| [[SW480 (line)]] | alt | 1.20 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0469× (z -8.5) |
| [[A-172 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.791 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.826 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.810 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.301 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.949 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.794 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.681 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.870 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 0.946 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.916 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.861 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.741 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.849 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.881 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.690 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9545), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 24 of them with an alert (⚠; 21 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCHFR]] | +0.70 | +0.53 / +0.68 | both halves | 1e-05 | pathway: Metabolism of vitamins and cofactors |
| [[SAC3D1]] | +0.67 | +0.35 / +0.71 | both halves | 1e-04 |  |
| [[NDUFA7]] | +0.66 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[F12]] | +0.65 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[PAXX]] ⚠ | +0.64 | +0.44 / +0.68 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[OCEL1]] | +0.62 | +0.29 / +0.64 | both halves | 2e-04 |  |
| [[COMTD1]] | +0.60 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[MFSD3]] | +0.59 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[NXT1]] | +0.59 | +0.31 / +0.61 | both halves | 2e-04 |  |
| [[FLVCR1-DT]] | +0.59 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[LAGE3]] | +0.58 | +0.25 / +0.61 | both halves | 4e-04 |  |
| [[ANTKMT]] | +0.58 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[TST]] | +0.57 | +0.40 / +0.63 | both halves | 4e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2V1]] | -0.60 | -0.27 / -0.68 | both halves | 3e-04 |  |
| [[WASH8P]] ⚠ | -0.52 | -0.30 / -0.51 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[LIN7C]] | -0.51 | -0.12 / -0.60 | ⚠ one half (not replicated) | 0.002 |  |
| [[IL18BP]] | -0.50 | -0.25 / -0.52 | both halves | 4e-04 |  |
| [[TARDBP]] | -0.50 | -0.24 / -0.52 | both halves | 4e-04 |  |
| [[CERS2]] | -0.49 | -0.13 / -0.56 | ⚠ one half (not replicated) | 0.002 |  |
| [[STX16]] | -0.49 | -0.19 / -0.58 | ⚠ one half (not replicated) | 9e-04 |  |
| [[KCNIP2]] | -0.48 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[PEX19]] | -0.47 | -0.17 / -0.58 | ⚠ one half (not replicated) | 0.001 |  |
| [[C8orf44-SGK3]] | -0.47 | -0.17 / -0.46 | ⚠ not reproduced | 0.001 |  |
| [[MED28]] | -0.47 | -0.23 / -0.54 | both halves | 5e-04 |  |
| [[LTO1]] | -0.47 | -0.22 / -0.43 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF655]] | B | ZNF655 activity lowers NUDT8's level | lines that do not express ZNF655 (7) vs lines expressing it (43) | 1.89× higher at baseline in the lines without ZNF655 | 0.023 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SRSF12 |
| [[PSMB5]] | B | PSMB5 activity raises NUDT8's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.486). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-45.6, -16.6); signed map (-31.8, 5.4). **Vector** length 44.5, 6.91% of its response variance represented; |z| ≥ 3 in 711 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.1 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | -0.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.6 | +2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.0 | +1.1 |
|  | [[Bendamustine (drug)]] 5 µM |  | +0.9 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +2.1 |
|  | [[Arbutin (drug)]] 5 µM |  | +0.8 | +1.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -5.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.5 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | nudix hydrolase 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:67,627,938-67,629,937 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ41567 |
| Gene groups (HGNC) | Nudix hydrolase family |
| Reactome | 3 pathways, smallest: Vitamin B5 (pantothenate) metabolism; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WV74](https://www.uniprot.org/uniprotkb/Q8WV74) (Mitochondrial coenzyme A diphosphatase NUDT8):

> Acyl-CoA diphosphatase that mediates the hydrolysis of a wide range of CoA and CoA esters yielding 3',5'-ADP and the corresponding 4'-phosphopantetheine derivative as products (By similarity). Hydrolyzes short- and medium-chain acyl-CoAs, exhibiting the highest activity toward free CoA, hexanoyl-CoA, and octanoyl-CoA and the lowest activity against acetyl-CoA (By similarity). Exhibits decapping activity towards dpCoA-capped RNAs in vitro (By similarity).

**Summary**, from NCBI Gene [254552](https://www.ncbi.nlm.nih.gov/gene/254552):

> Predicted to enable coenzyme A diphosphatase activity; magnesium ion binding activity; and manganese ion binding activity. Predicted to be involved in nucleoside phosphate catabolic process. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:8055](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8055) · Entrez [254552](https://www.ncbi.nlm.nih.gov/gene/254552) · UniProt [Q8WV74](https://www.uniprot.org/uniprotkb/Q8WV74) · Ensembl [ENSG00000167799](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167799)

## Data

Gene col 9545: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9545); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9545, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9545]; `tensor/DDL_lfc|DDL_z.npy` [9545]; `embed/gene_vectors.npy` [9545]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9545 or target_col == 9545). Every well: [[NUDT8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDT8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
