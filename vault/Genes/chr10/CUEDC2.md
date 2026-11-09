---
symbol: "CUEDC2"
type: "gene"
col: 2893
ensembl_id: "ENSG00000107874"
name: "CUE domain containing 2"
location: "10q24.32"
module: 12
arm: "+"
pooled_cpm: 12.31
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 8
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# CUEDC2

*CUE domain containing 2* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.60× (z +9.1, q 6e-17, up in 33 of 38 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1792 7.67×, A-172 3.62×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 6.18×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.573× (z -7.4, q 6e-11, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRHPR]] (+0.61, fdr 1e-05), [[DHX30]] (+0.61, fdr 1e-05), [[COA3]] (+0.61, fdr 1e-05); moves opposite to [[CCNYL1]] (-0.60, fdr 4e-05), [[CALM2]] (-0.50, fdr 7e-05), [[LINC01128]] (-0.50, fdr 1e-04).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2893.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1792 7.67×, A-172 3.62×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 6.18×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.60×** | +9.1 | 6e-17 | 33/38 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.66×** | +8.9 | 1e-16 | 18/22 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +5.0 | 9e-05 | 22/29 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.55×** | +4.2 | 0.004 | 19/41 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.43× | +3.3 | 0.10 | 17/41 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2893.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.573×** | -7.4 | 6e-11 | 35/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.480×** | -6.9 | 1e-09 | 40/47 (SNU-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.545×** | -5.7 | 2e-06 | 34/48 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.568×** | -5.3 | 1e-05 | 27/46 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.601×** | -4.8 | 2e-04 | 27/46 (A-427, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.613×** | -4.6 | 4e-04 | 24/48 (SW48, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.652×** | -4.0 | 0.005 | 20/48 (SK-MEL-2, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.667×** | -3.8 | 0.010 | 20/47 (A-427, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.716× | -3.1 | 0.11 | 16/46 (HepG2/C3A, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2893. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 25.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.62× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -12.1) |
| [[AN3 CA (line)]] | alt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0737× (z -9.0) |
| [[COLO 205 (line)]] | alt | 6.19 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0531× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 8.03 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.18× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.67× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -8.8) |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.103× (z -10.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2893), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRHPR]] | +0.61 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[DHX30]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[COA3]] | +0.61 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[MLST8]] | +0.60 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[NDUFA8]] | +0.60 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[MRPL22]] | +0.60 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[DPH1]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ALKBH3]] | +0.58 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[IRAK1BP1]] | +0.58 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[UCK1]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[TMLHE]] | +0.58 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[NDUFAF5]] | +0.57 | +0.51 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNYL1]] | -0.60 | -0.66 / -0.42 | both halves | 4e-05 |  |
| [[CALM2]] | -0.50 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[LINC01128]] | -0.50 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[SEPTIN10]] | -0.49 | -0.48 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises CUEDC2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.483). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-43.1, -6.6); signed map (-13.2, -22.4). **Vector** length 39.7, 5.55% of its response variance represented; |z| ≥ 3 in 603 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | -0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | -0.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | -0.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.8 | -0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.8 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +1.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +0.9 | +1.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -6.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.5 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.5 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | -0.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.4 | -2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.7 | -1.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.7 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.7 | -0.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | CUE domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:102,423,245-102,432,584 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2491; previously C10orf66 |
| Gene groups (HGNC) | CUE domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H467](https://www.uniprot.org/uniprotkb/Q9H467) (CUE domain-containing protein 2):

> Down-regulates ESR1 protein levels through the ubiquitination-proteasome pathway, regardless of the presence of 17 beta-estradiol. Also involved in 17 beta-estradiol-induced ESR1 degradation. Controls PGR protein levels through a similar mechanism.

**Summary**, from NCBI Gene [79004](https://www.ncbi.nlm.nih.gov/gene/79004):

> Predicted to enable ubiquitin binding activity. Acts upstream of or within negative regulation of cytokine production involved in inflammatory response and negative regulation of macrophage cytokine production. Located in cytosol; nuclear membrane; and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28352](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28352) · Entrez [79004](https://www.ncbi.nlm.nih.gov/gene/79004) · UniProt [Q9H467](https://www.uniprot.org/uniprotkb/Q9H467) · Ensembl [ENSG00000107874](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107874)

## Data

Gene col 2893: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2893); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2893, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2893]; `tensor/DDL_lfc|DDL_z.npy` [2893]; `embed/gene_vectors.npy` [2893]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2893 or target_col == 2893). Every well: [[CUEDC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CUEDC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
