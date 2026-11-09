---
symbol: "PTPN23"
type: "gene"
col: 1145
ensembl_id: "ENSG00000076201"
name: "protein tyrosine phosphatase non-receptor type 23"
location: "3p21.31"
module: 107
arm: "+"
pooled_cpm: 28.9
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 12
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# PTPN23

*protein tyrosine phosphatase non-receptor type 23* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.64× (z +8.2, q 2e-13, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.656× (z -6.8, q 7e-09, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC47]] (+0.64, fdr 8e-06), [[BRMS1]] (+0.62, fdr 2e-05), [[ZNF408]] (+0.61, fdr 2e-05); moves opposite to [[COX7B]] (-0.47, fdr 3e-05), [[PEAK1]] (-0.46, fdr 5e-05).
> It is in [[Module 107]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Binimetinib (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1145.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.64×** | +8.2 | 2e-13 | 42/48 (SW480, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +6.8 | 3e-09 | 35/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.10×** | +6.2 | 8e-08 | 30/47 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +6.2 | 1e-07 | 31/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +4.7 | 3e-04 | 26/48 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +3.9 | 0.008 | 12/48 (SNU-423, SW1417, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.074 | 16/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.091 | 16/48 (PANC-1, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1145.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.656×** | -6.8 | 7e-09 | 34/48 (A-172, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~10% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.776×** | -5.6 | 7e-06 | 31/48 (SNU-423, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.728×** | -5.1 | 6e-05 | 25/48 (A498, RPMI-7951, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.763×** | -4.4 | 0.002 | 26/48 (CHP-212, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.618×** | -4.0 | 0.004 | 16/48 (LoVo, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.762×** | -4.0 | 0.004 | 21/41 (LoVo, SK-MEL-2, …) | inconsistent across doses | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.778×** | -4.0 | 0.004 | 21/48 (J82, A498, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.793×** | -3.7 | 0.013 | 14/48 (A-427, Panc 03.27, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.798×** | -3.6 | 0.017 | 18/48 (A498, A-172, …) | all doses, flat | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **0.800×** | -3.6 | 0.018 | 18/44 (C-33 A, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.795×** | -3.6 | 0.020 | 20/48 (A-427, RPMI-7951, …) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.809×** | -3.4 | 0.030 | 14/47 (KATO III, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1145. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 31.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[PANC-1 (line)]] | alt | 23.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +9.1) | — |
| [[SW480 (line)]] | alt | 33.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.46× (z +8.9) | — |
| [[A-427 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1145), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC47]] | +0.64 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[BRMS1]] | +0.62 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[ZNF408]] | +0.61 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[XAB2]] | +0.60 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[ANAPC2]] | +0.59 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[BLOC1S3]] | +0.59 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[SF3A2]] | +0.58 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[TRMT2A]] | +0.57 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[TBL3]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[ZNF142]] | +0.57 | +0.48 / +0.47 | both halves | 2e-05 | STRING 440 |
| [[RANBP3]] | +0.57 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[TOP3B]] | +0.56 | +0.56 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX7B]] | -0.47 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[PEAK1]] | -0.46 | -0.39 / -0.47 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers PTPN23's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Binimetinib (drug)]] 0.05 µM | C | PTPN23's natural level lowers the cells' numbers under Binimetinib 0.05 µM (makes them more sensitive) | PTPN23's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64 | 0.390 over the table, 0.093 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.672). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.9, -3.3); signed map (-10.7, -25.9). **Vector** length 73.0, 13.6% of its response variance represented; |z| ≥ 3 in 792 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.7 | -1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.3 | +0.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.0 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.8 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +6.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +0.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.0 | +0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | -0.2 |
| fall | [[Tucidinostat (drug)]] 0.5 µM |  | -3.6 | -4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -5.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.8 | -6.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -1.5 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.9 | -0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -4.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase non-receptor type 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:47,381,011-47,413,435 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564F0923, KIAA1471, HD-PTP |
| Gene groups (HGNC) | Protein tyrosine phosphatases non-receptor type |
| Reactome | 4 pathways, smallest: Interleukin-37 signaling; Interleukin-1 family signaling; Signaling by Interleukins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3S7](https://www.uniprot.org/uniprotkb/Q9H3S7) (Tyrosine-protein phosphatase non-receptor type 23):

> Plays a role in sorting of endocytic ubiquitinated cargos into multivesicular bodies (MVBs) via its interaction with the ESCRT-I complex (endosomal sorting complex required for transport I), and possibly also other ESCRT complexes. May act as a negative regulator of Ras-mediated mitogenic activity. Plays a role in ciliogenesis.

**Summary**, from NCBI Gene [25930](https://www.ncbi.nlm.nih.gov/gene/25930):

> This gene encodes a member of the non-receptor type protein-tyrosine phosphatase family. The encoded protein may be involved in the regulation of small nuclear ribonucleo protein assembly and pre-mRNA splicing by modifying the survival motor neuron (SMN) complex. The encoded protein additionally plays a role in ciliogenesis and is part of endosomal sorting complex required for transport (ESCRT) pathways. This gene may serve a tumor suppressor function. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:14406](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14406) · Entrez [25930](https://www.ncbi.nlm.nih.gov/gene/25930) · UniProt [Q9H3S7](https://www.uniprot.org/uniprotkb/Q9H3S7) · Ensembl [ENSG00000076201](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076201)

## Data

Gene col 1145: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1145); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1145, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1145]; `tensor/DDL_lfc|DDL_z.npy` [1145]; `embed/gene_vectors.npy` [1145]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1145 or target_col == 1145). Every well: [[PTPN23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPN23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
