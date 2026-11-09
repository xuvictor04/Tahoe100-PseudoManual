---
symbol: "GOLGA8A"
type: "gene"
col: 10587
ensembl_id: "ENSG00000175265"
name: "golgin A8 family member A"
location: "15q14"
module: 21
arm: "+"
pooled_cpm: 23.21
n_lines_expressing: 46
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# GOLGA8A

*golgin A8 family member A* — 15q14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.01× (z +12.3, q 3e-32, up in 36 of 42 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLGA8B]] (+0.83, fdr 7e-06), [[CCNL2]] (+0.68, fdr 7e-06), [[SGSM2]] (+0.60, fdr 3e-05); moves opposite to [[CBR1]] (-0.52, fdr 4e-05), [[DPM2]] (-0.52, fdr 2e-05), [[MLX]] (-0.50, fdr 5e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10587.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +12.3 | 3e-32 | 36/42 (AsPC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.12×** | +10.3 | 3e-22 | 24/37 (SW480, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +9.9 | 1e-20 | 20/29 (LS 180, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +9.5 | 4e-19 | 25/34 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +7.0 | 3e-10 | 30/42 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +6.4 | 2e-08 | 28/42 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +6.2 | 5e-08 | 24/42 (LS 180, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +4.6 | 3e-04 | 18/44 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 0.003 | 17/42 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.87×** | +4.0 | 0.003 | 15/39 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.007 | 12/43 (HepG2/C3A, A549, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +3.8 | 0.008 | 11/31 (RKO, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.72×** | +3.5 | 0.023 | 8/43 (HEC-1-A, SW1417, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.62×** | +3.1 | 0.079 | 10/41 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10587.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -3.0 | 0.96 | 8/44 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10587. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 13.8 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +9.8) | — |
| [[LS 180 (line)]] | wt | 31.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.56× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 45.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +8.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 41.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 21.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +11.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.05 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.08 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.51 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.19 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10587), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA8B]] | +0.83 | +0.73 / +0.84 | both halves | 7e-06 | same gene group; STRING 543 |
| [[CCNL2]] | +0.68 | +0.61 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[SGSM2]] | +0.60 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[TICAM2-AS1]] | +0.60 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[ARGLU1]] | +0.57 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[C12orf73]] | +0.56 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[HOXB-AS3]] | +0.56 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[RPL41]] | +0.55 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[FAM217A]] | +0.55 | +0.40 / +0.51 | both halves | 4e-05 |  |
| [[LANCL1-AS1]] | +0.53 | +0.47 / +0.39 | both halves | 5e-05 |  |
| [[BCL2L2]] | +0.53 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[PCED1A]] | +0.53 | +0.46 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBR1]] | -0.52 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[DPM2]] | -0.52 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[MLX]] | -0.50 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[TWF2]] | -0.50 | -0.45 / -0.29 | both halves | 3e-04 |  |
| [[H2AX]] | -0.50 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[MINPP1]] | -0.48 | -0.32 / -0.47 | both halves | 2e-04 | same gene group |
| [[SLC39A3]] | -0.48 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[ZNF639]] | -0.47 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[ATP5MC3]] ⚠ | -0.47 | -0.29 / -0.47 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[UBL4A]] | -0.46 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[DLAT]] | -0.46 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[TOMM70]] | -0.46 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[USP14]] | -0.46 | -0.45 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GOLGA8A's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.535). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.3, -25.0); signed map (4.1, -5.2). **Vector** length 66.7, 13.7% of its response variance represented; |z| ≥ 3 in 520 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +12.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +7.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +9.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +4.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.1 | +3.5 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.8 | +3.1 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.8 | +2.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.8 | +2.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.9 | -2.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.2 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.7 | +0.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.7 | -0.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.7 | -2.6 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -2.3 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -1.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | golgin A8 family member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q14 — chr15:34,378,935-34,437,808 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GM88, GOLGIN-67, FAP286, CFAP286 |
| Gene groups (HGNC) | Cilia and flagella associated; MicroRNA protein coding host genes; Golgin A6 and A8 families |
| Matched by | ensembl_id |

**Function**, from UniProt [A7E2F4](https://www.uniprot.org/uniprotkb/A7E2F4) (Golgin subfamily A member 8A):

> May be involved in maintaining Golgi structure.

**Summary**, from NCBI Gene [23015](https://www.ncbi.nlm.nih.gov/gene/23015):

> The Golgi apparatus, which participates in glycosylation and transport of proteins and lipids in the secretory pathway, consists of a series of stacked, flattened membrane sacs referred to as cisternae. Interactions between the Golgi and microtubules are thought to be important for the reorganization of the Golgi after it fragments during mitosis. The golgins constitute a family of proteins which are localized to the Golgi. This gene encodes a golgin which structurally resembles its family …

**Accessions** — [HGNC:31972](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31972) · Entrez [23015](https://www.ncbi.nlm.nih.gov/gene/23015) · UniProt [A7E2F4](https://www.uniprot.org/uniprotkb/A7E2F4) · Ensembl [ENSG00000175265](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175265)

## Data

Gene col 10587: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10587); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10587, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10587]; `tensor/DDL_lfc|DDL_z.npy` [10587]; `embed/gene_vectors.npy` [10587]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10587 or target_col == 10587). Every well: [[GOLGA8A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOLGA8A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
