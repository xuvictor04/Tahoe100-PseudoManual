---
symbol: "GMPR2"
type: "gene"
col: 2047
ensembl_id: "ENSG00000100938"
name: "guanosine monophosphate reductase 2"
location: "14q12"
module: 76
arm: "+"
pooled_cpm: 14.12
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# GMPR2

*guanosine monophosphate reductase 2* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.16× (z +10.5, q 5e-23, up in 20 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.35× (z +5.7, q 2e-06, up in 22 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.605× (z -9.6, q 6e-19, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM59]] (+0.66, fdr 7e-06), [[LYSMD1]] (+0.60, fdr 1e-05), [[ZNF224]] (+0.60, fdr 3e-05); moves opposite to [[CEP83]] (-0.53, fdr 1e-05), [[TAF1B]] (-0.53, fdr 3e-05), [[CFAP161]] (-0.52, fdr 9e-05).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2047.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +10.5 | 5e-23 | 20/26 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.81×** | +8.4 | 2e-14 | 27/36 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.7 | 2e-06 | 22/47 (HS-578T, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +5.2 | 4e-05 | 22/43 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.56×** | +4.1 | 0.006 | 17/43 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.008 | 18/47 (SNU-423, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.34×** | +3.9 | 0.009 | 14/32 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.50×** | +3.6 | 0.019 | 10/43 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.48×** | +3.6 | 0.021 | 11/44 (SK-MEL-2, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2047.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.605×** | -9.6 | 6e-19 | 30/47 (hTERT-HPNE, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.660×** | -5.5 | 9e-06 | 24/47 (NCI-H2347, A-427, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.679×** | -5.4 | 1e-05 | 24/46 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.915× | -4.2 | 0.003 | 4/48 (RPMI-7951, A-172, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.772×** | -3.6 | 0.031 | 13/47 (HEC-1-A, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.782×** | -3.3 | 0.085 | 15/46 (BT-474, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Pemetrexed (drug)]] 0.5 µM |  | 0.803× | -3.1 | 0.16 | 7/47 (SNU-423, Panc 03.27, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2047. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 13.8 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0738× (z -12.2) |
| [[NCI-H2347 (line)]] | alt | 28.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.369× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 16.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -8.9) |
| [[A498 (line)]] | wt | 8.12 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 20.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -9.5) |
| [[COLO 205 (line)]] | alt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -9.4) |
| [[LS 180 (line)]] | wt | 19.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.73× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 13.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.08× (z +11.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2047), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM59]] | +0.66 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[LYSMD1]] | +0.60 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[ZNF224]] | +0.60 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[MKRN1]] | +0.59 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[BABAM1]] | +0.58 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[XAB2]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[CDIPT]] | +0.57 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[LINC00847]] | +0.57 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[TNKS]] | +0.57 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[APH1A]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[TMUB2]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[DNASE2]] | +0.56 | +0.49 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP83]] | -0.53 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[TAF1B]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[CFAP161]] | -0.52 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[SMARCA4]] | -0.49 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[JPH1]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[DUSP7]] | -0.49 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[PFN1]] | -0.48 | -0.49 / -0.27 | both halves | 3e-04 |  |
| [[KCNQ4]] | -0.48 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[XXYLT1]] | -0.48 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[CCND1]] | -0.47 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[CTPS1]] | -0.47 | -0.39 / -0.48 | both halves | 6e-05 | pathway: Metabolism of nucleotides; STRING 406 |
| [[AP1S3]] | -0.47 | -0.41 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.468). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.2, -15.2); signed map (-22.8, 0.2). **Vector** length 53.1, 7.70% of its response variance represented; |z| ≥ 3 in 605 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +5.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +2.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +3.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.2 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +0.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -5.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.0 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -5.5 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | guanosine monophosphate reductase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:24,232,422-24,239,242 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hGMPR-II |
| Gene groups (HGNC) | Guanosine monophosphate reductase family |
| Hallmark sets | DNA_REPAIR |
| Reactome | 3 pathways, smallest: Purine salvage; Nucleotide salvage; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2T1](https://www.uniprot.org/uniprotkb/Q9P2T1) (GMP reductase 2):

> Catalyzes the irreversible NADPH-dependent deamination of GMP to IMP. It functions in the conversion of nucleobase, nucleoside and nucleotide derivatives of G to A nucleotides, and in maintaining the intracellular balance of A and G nucleotides. Plays a role in modulating cellular differentiation.

**Summary**, from NCBI Gene [51292](https://www.ncbi.nlm.nih.gov/gene/51292):

> This gene encodes an enzyme that catalyzes the irreversible and NADPH-dependent reductive deamination of guanosine monophosphate (GMP) to inosine monophosphate (IMP). The protein also functions in the re-utilization of free intracellular bases and purine nucleosides. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2017]

**Accessions** — [HGNC:4377](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4377) · Entrez [51292](https://www.ncbi.nlm.nih.gov/gene/51292) · UniProt [Q9P2T1](https://www.uniprot.org/uniprotkb/Q9P2T1) · Ensembl [ENSG00000100938](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100938)

## Data

Gene col 2047: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2047); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2047, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2047]; `tensor/DDL_lfc|DDL_z.npy` [2047]; `embed/gene_vectors.npy` [2047]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2047 or target_col == 2047). Every well: [[GMPR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GMPR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
