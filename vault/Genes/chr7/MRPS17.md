---
symbol: "MRPS17"
type: "gene"
col: 14211
ensembl_id: "ENSG00000239789"
name: "mitochondrial ribosomal protein S17"
location: "7p11.2"
module: 1
arm: "+"
pooled_cpm: 2.42
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# MRPS17

*mitochondrial ribosomal protein S17* — 7p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.26× (z +9.5, q 1e-18, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 2.77× (z +8.5, q 4e-15, up in 30 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Allantoin (drug)]] 0.5 µM: 0.630× (z -3.9, q 0.047, down in 10 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0695×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRS1]] (+0.71, fdr 7e-06), [[CCDC137]] (+0.68, fdr 7e-06), [[LBHD1]] (+0.66, fdr 7e-06); moves opposite to [[LAPTM4A]] (-0.58, fdr 1e-05), [[TMED4]] (-0.57, fdr 1e-05), [[ATP6AP2]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14211.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.26×** | +9.5 | 1e-18 | 2/2 (A498, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.77×** | +8.5 | 4e-15 | 30/43 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.94×** | +5.5 | 7e-06 | 13/30 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +5.4 | 1e-05 | 6/10 (KATO III, PANC-1, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.98×** | +5.3 | 1e-05 | 9/23 (LoVo, HEC-1-A, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.98×** | +5.3 | 1e-05 | 2/3 (A498, SW480) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.92×** | +5.2 | 1e-05 | 15/42 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.75×** | +4.6 | 2e-04 | 10/45 (SW480, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.69×** | +4.4 | 7e-04 | 4/12 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +4.2 | 0.001 | 7/19 (PANC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.62×** | +4.0 | 0.003 | 12/42 (PANC-1, LoVo, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.41×** | +4.0 | 0.003 | 9/32 (KATO III, AsPC-1, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.011 | 5/33 (A498, A549, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.014 | 0/43 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.48×** | +3.3 | 0.039 | 7/45 (SW 900, SW48, …) | rises with dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.041 | 7/36 (NCI-H1792, HS-578T, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **2.04×** | +3.1 | 0.058 | 2/34 (SW480, PANC-1) | top dose only | noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.44×** | +3.1 | 0.060 | 4/32 (SHP-77, SW1417, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14211.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0695×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Allantoin (drug)]] 0.5 µM |  | **0.630×** | -3.9 | 0.047 | 10/36 (SHP-77, MIA PaCa-2, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14211. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 2.50 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0695× (z -9.1) |
| [[A-172 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.943 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14211), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRS1]] | +0.71 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[CCDC137]] | +0.68 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[LBHD1]] | +0.66 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[NIFK]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[GPATCH4]] | +0.63 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[NIP7]] | +0.62 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[NOP14]] | +0.62 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[MRM3]] | +0.62 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[BRIX1]] | +0.61 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[PWP2]] | +0.61 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[MRPL15]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 915 |
| [[ZNF146]] | +0.61 | +0.51 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAPTM4A]] | -0.58 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[TMED4]] | -0.57 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[ATP6AP2]] | -0.56 | -0.46 / -0.62 | both halves | 3e-05 |  |
| [[TM9SF2]] | -0.55 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[CD99]] | -0.55 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[RCN2]] | -0.54 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[RTN3]] | -0.54 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[CTSD]] | -0.53 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[PCYOX1]] | -0.53 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[PHTF2]] | -0.53 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[TMBIM6]] | -0.53 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[GRN]] | -0.51 | -0.42 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.566). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-45.7, -9.9); signed map (-2.8, -20.9). **Vector** length 35.3, 3.29% of its response variance represented; |z| ≥ 3 in 919 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.2 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +5.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.1 | +3.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +2.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.0 | +2.0 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.8 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.2 | +0.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -1.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -0.9 | -0.2 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -0.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p11.2 — chr7:55,951,877-55,956,500 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC011, RPMS17, MRP-S17, uS17m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Small subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9Y2R5](https://www.uniprot.org/uniprotkb/Q9Y2R5) carries no function annotation.

**Summary**, from NCBI Gene [51373](https://www.ncbi.nlm.nih.gov/gene/51373):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14047](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14047) · Entrez [51373](https://www.ncbi.nlm.nih.gov/gene/51373) · UniProt [Q9Y2R5](https://www.uniprot.org/uniprotkb/Q9Y2R5) · Ensembl [ENSG00000239789](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000239789)

## Data

Gene col 14211: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14211); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14211, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14211]; `tensor/DDL_lfc|DDL_z.npy` [14211]; `embed/gene_vectors.npy` [14211]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14211 or target_col == 14211). Every well: [[MRPS17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
