---
symbol: "LRRN3"
type: "gene"
col: 10341
ensembl_id: "ENSG00000173114"
name: "leucine rich repeat neuronal 3"
location: "7q31.1"
module: 90
arm: "+"
pooled_cpm: 2.39
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# LRRN3

*leucine rich repeat neuronal 3* — 7q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.87× (z +10.4, q 2e-22, up in 4 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.53× (z +5.9, q 5e-07, up in 12 of 32 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H661 0.158×); [[Resveratrol (drug)]] 0.05 µM in 1 line (PANC-1 0.0749×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBMS3-AS3]] (+0.78, fdr 7e-06), [[LRRC4C]] (+0.73, fdr 7e-06), [[SPATC1]] (+0.72, fdr 1e-05).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[BRCA2]] → it (grade B ⚠); 2 go from it, the strongest it → [[LRRC4C]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10341.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.87×** | +10.4 | 2e-22 | 4/9 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.63×** | +9.2 | 1e-17 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.53×** | +8.4 | 6e-15 | 1/2 (HS-578T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +5.9 | 5e-07 | 12/32 (hTERT-HPNE, HS-578T, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.75×** | +5.5 | 4e-06 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.1 | 3e-05 | 8/28 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +4.5 | 6e-04 | 3/18 (hTERT-HPNE, PANC-1, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.04×** | +3.7 | 0.018 | 0/1 | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.02×** | +3.6 | 0.020 | 0/2 | top dose only | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.65×** | +3.5 | 0.026 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ornidazole (drug)]] 5 µM | ⚠ unreliable plate only | **1.42×** | +3.5 | 0.028 | 1/46 (NCI-H661) | top dose only | position effect removed |
| [[Elagolix sodium (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.028 | 2/33 (NCI-H661, CHP-212) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.032 | 5/33 (LOX-IMVI, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +3.3 | 0.037 | 0/1 | rises with dose | noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.046 | 3/26 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mifepristone (drug)]] 0.05 µM |  | **1.42×** | +3.2 | 0.048 | 1/32 (LOX-IMVI) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.076 | 8/40 (HS-578T, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10341.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H661 0.158×); [[Resveratrol (drug)]] 0.05 µM in 1 line (PANC-1 0.0749×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.916× | -3.1 | 0.74 | 13/47 (SW1417, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10341. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H661 (line)]] | alt | 218 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -11.4) |
| [[PANC-1 (line)]] | alt | 1.42 | 0 | 1 | — | [[Resveratrol (drug)]] 0.05 µM 0.0749× (z -8.8) |
| [[A-172 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10341), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBMS3-AS3]] | +0.78 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.73 | +0.66 / +0.64 | both halves | 7e-06 | same gene group |
| [[SPATC1]] | +0.72 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[CNTNAP4]] | +0.72 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[ARHGAP15]] | +0.72 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[PPP1R9A-AS1]] | +0.71 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[CNTNAP5]] | +0.70 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[GRIA4]] | +0.70 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[KIF6]] | +0.69 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[ARL14EP-DT]] | +0.69 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.68 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[CNTN5]] | +0.68 | +0.67 / +0.59 | both halves | 7e-06 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BRCA2]] | B | BRCA2 activity strengthens LRRN3's drug response | recorded loss-of-function mutation of BRCA2 in 6 lines vs 30 not recorded | the BRCA2-altered lines respond the other way (z diff +1.87); strongest at Dinaciclib 0.5 µM: 0.31x vs 2.22x (z diff +6.4) | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TGFBR2, WNK2, ACVR2A; target measured in part of the lines; artifact flags |
| [[LINC02240]] | B | LINC02240 activity raises LRRN3's level | lines that do not express LINC02240 (35) vs lines expressing it (15) | 2.08× lower at baseline in the lines without LINC02240 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02941, CHL1, EDNRB; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC4C]] | C | LRRN3's natural level weakens LRRC4C's drug response | LRRN3's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.67, reverse -0.33; direction clear | 0.032 | ⚠ tissue can mimic it; precision caveat |
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | C | LRRN3's natural level lowers the cells' numbers under Lapatinib ditosylate 0.5 µM (makes them more sensitive) | LRRN3's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.61 | 0.446 over the table, 0.075 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.705). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.9, 27.3); signed map (34.8, 13.2). **Vector** length 30.9, 2.28% of its response variance represented; |z| ≥ 3 in 1,104 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +10.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | -0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +1.4 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.0 | +1.5 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -3.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -0.8 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.9 | -1.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -0.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.8 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat neuronal 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.1 — chr7:111,091,006-111,125,454 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NLRR3, FLJ11129, FIGLER5 |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing |
| Matched by | ensembl_id |

UniProt [Q9H3W5](https://www.uniprot.org/uniprotkb/Q9H3W5) carries no function annotation.

**Summary**, from NCBI Gene [54674](https://www.ncbi.nlm.nih.gov/gene/54674):

> Predicted to enable signaling receptor activity. Predicted to act upstream of or within positive regulation of synapse assembly. Predicted to be located in membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17200](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17200) · Entrez [54674](https://www.ncbi.nlm.nih.gov/gene/54674) · UniProt [Q9H3W5](https://www.uniprot.org/uniprotkb/Q9H3W5) · Ensembl [ENSG00000173114](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173114)

## Data

Gene col 10341: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10341); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10341, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10341]; `tensor/DDL_lfc|DDL_z.npy` [10341]; `embed/gene_vectors.npy` [10341]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10341 or target_col == 10341). Every well: [[LRRN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
