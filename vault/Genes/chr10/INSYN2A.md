---
symbol: "INSYN2A"
type: "gene"
col: 12065
ensembl_id: "ENSG00000188916"
name: "inhibitory synaptic factor 2A"
location: "10q26.2"
module: 62
arm: "+"
pooled_cpm: 2.97
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# INSYN2A

*inhibitory synaptic factor 2A* — 10q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.56× (z +9.6, q 7e-19, up in 3 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.33× (z +4.3, q 0.002, up in 10 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.688× (z -3.9, q 0.048, down in 13 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Vilanterol (drug)]] 0.05 µM in 1 line (A498 0.0671×); [[Hesperidin (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0602×); [[Ixazomib citrate (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0779×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EVI2B]] (+0.67, fdr 1e-05), [[DNAI3]] (+0.66, fdr 3e-05), [[A2ML1-AS1]] (+0.64, fdr 1e-05); moves opposite to [[MPP1]] (-0.51, fdr 1e-04), [[CS]] (-0.50, fdr 7e-05), [[TUBB]] (-0.50, fdr 3e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12065.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.56×** | +9.6 | 7e-19 | 3/4 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.04×** | +7.5 | 1e-11 | 6/16 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.92×** | +6.4 | 3e-08 | 1/9 (NCI-H1792) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.3 | 0.002 | 10/35 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.010 | 6/35 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.9 | 0.010 | 3/23 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +3.8 | 0.012 | 3/18 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.5 | 0.030 | 4/30 (A498, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.4 | 0.037 | 4/13 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.041 | 5/43 (HS-578T, A549, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.79×** | +3.2 | 0.068 | 1/5 (A549) | top dose only | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.2 | 0.069 | 4/36 (RKO, HCT15, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.074 | 4/42 (C32, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12065.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Vilanterol (drug)]] 0.05 µM in 1 line (A498 0.0671×); [[Hesperidin (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0602×); [[Ixazomib citrate (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0779×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.688×** | -3.9 | 0.048 | 13/45 (A549, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.700×** | -3.7 | 0.050 | 9/45 (SNU-423, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -3.6 | 0.072 | 10/47 (NCI-H1792, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12065. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 4.99 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.85× (z +14.1) | — |
| [[A498 (line)]] | wt | 2.76 | 0 | 2 | — | [[Vilanterol (drug)]] 0.05 µM 0.0671× (z -10.5) |
| [[A549 (line)]] | wt | 7.82 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.98× (z +12.0) | — |
| [[LOX-IMVI (line)]] | wt | 2.97 | 0 | 1 | — | [[Hesperidin (drug)]] 0.5 µM 0.0602× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 2.46 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.05 µM 0.0779× (z -8.5) |
| [[A-172 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12065), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EVI2B]] | +0.67 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[DNAI3]] | +0.66 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[A2ML1-AS1]] | +0.64 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[SORCS3]] | +0.63 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[ZNF423]] | +0.63 | +0.29 / +0.66 | both halves | 3e-04 |  |
| [[ST7-AS2]] | +0.61 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[INKA2]] | +0.61 | +0.29 / +0.54 | both halves | 2e-04 |  |
| [[CFAP58]] | +0.61 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[TMLHE-AS1]] | +0.61 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[GAS6-AS1]] | +0.60 | +0.37 / +0.63 | both halves | 9e-05 |  |
| [[ACTA2]] | +0.60 | +0.39 / +0.48 | both halves | 6e-05 |  |
| [[TNFRSF10A]] | +0.59 | +0.40 / +0.58 | both halves | 4e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPP1]] | -0.51 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[CS]] | -0.50 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[TUBB]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[SSX2IP]] | -0.50 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[PHF6]] | -0.49 | -0.38 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises INSYN2A's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.6, 37.0); signed map (43.8, -23.2). **Vector** length 39.7, 3.71% of its response variance represented; |z| ≥ 3 in 1,016 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.4 | +0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +1.1 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -1.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | inhibitory synaptic factor 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.2 — chr10:127,135,426-127,196,591 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ45557; previously C10orf141, FAM196A, INSYN2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZSG2](https://www.uniprot.org/uniprotkb/Q6ZSG2) (Inhibitory synaptic factor 2A):

> Component of the protein machinery at the inhibitory synapses, probably acting as a scaffold. Inhibitory synapses dampen neuronal activity through postsynaptic hyperpolarization. This synaptic inhibition is fundamental for the functioning of the central nervous system, shaping and orchestrating the flow of information through neuronal networks to generate a precise neural code.

**Summary**, from NCBI Gene [642938](https://www.ncbi.nlm.nih.gov/gene/642938):

> Predicted to be involved in inhibitory postsynaptic potential. Predicted to be active in GABA-ergic synapse and postsynaptic density. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:33859](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33859) · Entrez [642938](https://www.ncbi.nlm.nih.gov/gene/642938) · UniProt [Q6ZSG2](https://www.uniprot.org/uniprotkb/Q6ZSG2) · Ensembl [ENSG00000188916](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188916)

## Data

Gene col 12065: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12065); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12065, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12065]; `tensor/DDL_lfc|DDL_z.npy` [12065]; `embed/gene_vectors.npy` [12065]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12065 or target_col == 12065). Every well: [[INSYN2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INSYN2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
