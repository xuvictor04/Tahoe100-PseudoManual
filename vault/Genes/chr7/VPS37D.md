---
symbol: "VPS37D"
type: "gene"
col: 10718
ensembl_id: "ENSG00000176428"
name: "VPS37D subunit of ESCRT-I"
location: "7q11.23"
module: 30
arm: "+"
pooled_cpm: 3.14
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# VPS37D

*VPS37D subunit of ESCRT-I* — 7q11.23

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.615× (z -3.8, q 0.083, down in 14 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-172 0.108×, NCI-H460 0.0712×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2347 0.248×, C32 0.178×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2347 0.0972×; ⚠ toxic; transcription drop); [[Bexarotene (drug)]] 0.05 µM in 1 line (LS 180 0.0490×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMBR1L]] (+0.74, fdr 7e-06), [[LIN7B]] (+0.70, fdr 7e-06), [[CGRRF1]] (+0.70, fdr 1e-05); moves opposite to [[XRCC5]] (-0.72, fdr 1e-05), [[PSME3]] (-0.70, fdr 7e-06), [[EIF2S1]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 030]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10718.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.86× | +3.5 | 0.18 | 9/26 (NCI-H1792, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 1.36× | +3.4 | 0.18 | 7/43 (A-172, NCI-H2030, …) | top dose only | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.80× | +3.3 | 0.18 | 6/33 (MIA PaCa-2, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.50× | +3.2 | 0.20 | 7/45 (C-33 A, BT-474, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.48× | +3.1 | 0.25 | 7/20 (A-172, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10718.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-172 0.108×, NCI-H460 0.0712×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2347 0.248×, C32 0.178×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2347 0.0972×; ⚠ toxic; transcription drop); [[Bexarotene (drug)]] 0.05 µM in 1 line (LS 180 0.0490×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.615×** | -3.8 | 0.083 | 14/36 (A-172, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.647× | -3.4 | 0.19 | 9/45 (CHP-212, NCI-H2347, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.658× | -3.3 | 0.21 | 12/44 (J82, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.753× | -3.1 | 0.25 | 17/46 (SW1417, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10718. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 4.84 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0972× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.248× (z -8.5) |
| [[A-172 (line)]] | wt | 7.04 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -9.8) |
| [[C32 (line)]] | wt | 7.08 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 5.92 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[LS 180 (line)]] | wt | 2.77 | 0 | 1 | — | [[Bexarotene (drug)]] 0.05 µM 0.0490× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 2.35 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0712× (z -9.7) |
| [[A-427 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10718), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMBR1L]] | +0.74 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[LIN7B]] | +0.70 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[CGRRF1]] | +0.70 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[DENND6B]] | +0.69 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[MALSU1]] | +0.68 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[KBTBD3]] | +0.68 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[PRKAB2]] | +0.67 | +0.67 / +0.59 | both halves | 7e-06 | pathway: Autophagy |
| [[UNC119]] | +0.67 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[RAB40C]] | +0.67 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[PLCD1]] | +0.67 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[TMEM185A]] | +0.67 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[RNF113A]] | +0.67 | +0.46 / +0.70 | both halves | 2e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XRCC5]] | -0.72 | -0.56 / -0.73 | both halves | 1e-05 | pathway: HIV Infection |
| [[PSME3]] | -0.70 | -0.59 / -0.72 | both halves | 7e-06 |  |
| [[EIF2S1]] | -0.69 | -0.60 / -0.78 | both halves | 7e-06 |  |
| [[ABCE1]] | -0.68 | -0.58 / -0.68 | both halves | 8e-06 |  |
| [[EIF4G1]] | -0.66 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[HNRNPAB]] | -0.66 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[GNL3L]] | -0.66 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[RBM12]] | -0.66 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[SSU72]] | -0.65 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[NUP188]] | -0.64 | -0.50 / -0.71 | both halves | 1e-05 | pathway: HCMV Infection |
| [[ANAPC7]] | -0.64 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[PRMT3]] | -0.63 | -0.63 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.702). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.0, -10.4); signed map (-26.1, -6.5). **Vector** length 60.7, 9.75% of its response variance represented; |z| ≥ 3 in 738 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +2.4 | +3.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +3.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +1.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +3.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.5 | -0.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.4 | -0.6 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.4 | -1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | VPS37D subunit of ESCRT-I |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:73,667,831-73,672,112 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC35352; previously WBSCR24 |
| Gene groups (HGNC) | ESCRT-I |
| Hallmark sets | DNA_REPAIR |
| Reactome | 15 pathways, smallest: Membrane binding and targetting of GAG proteins; Synthesis And Processing Of GAG, GAGPOL Polyproteins; Assembly Of The HIV Virion |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86XT2](https://www.uniprot.org/uniprotkb/Q86XT2) (Vacuolar protein sorting-associated protein 37D):

> Component of the ESCRT-I complex, a regulator of vesicular trafficking process. Required for the sorting of endocytic ubiquitinated cargos into multivesicular bodies. May be involved in cell growth and differentiation.

**Summary**, from NCBI Gene [155382](https://www.ncbi.nlm.nih.gov/gene/155382):

> Predicted to be involved in protein targeting to membrane; protein targeting to vacuole; and ubiquitin-dependent protein catabolic process via the multivesicular body sorting pathway. Located in extracellular exosome. Part of ESCRT I complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18287](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18287) · Entrez [155382](https://www.ncbi.nlm.nih.gov/gene/155382) · UniProt [Q86XT2](https://www.uniprot.org/uniprotkb/Q86XT2) · Ensembl [ENSG00000176428](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176428)

## Data

Gene col 10718: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10718); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10718, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10718]; `tensor/DDL_lfc|DDL_z.npy` [10718]; `embed/gene_vectors.npy` [10718]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10718 or target_col == 10718). Every well: [[VPS37D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS37D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
