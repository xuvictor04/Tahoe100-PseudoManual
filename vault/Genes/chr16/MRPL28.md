---
symbol: "MRPL28"
type: "gene"
col: 1461
ensembl_id: "ENSG00000086504"
name: "mitochondrial ribosomal protein L28"
location: "16p13.3"
module: 16
arm: "+"
pooled_cpm: 7.87
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# MRPL28

*mitochondrial ribosomal protein L28* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.71× (z +8.8, q 1e-15, up in 25 of 31 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.57× (z +4.0, q 0.009, up in 21 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.573× (z -6.9, q 2e-09, down in 27 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 0.05 µM in 1 line (NCI-H23 0.0603×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.189×); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (NCI-H23 0.0846×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POP4]] (+0.65, fdr 1e-05), [[HSD17B10]] (+0.59, fdr 4e-05, ⚠ HSD17B10 in the vector space only through flagged drug-doses), [[RANBP6]] (+0.56, fdr 4e-05), [[PIGQ]] (+0.55, fdr 3e-05); moves opposite to [[NAP1L1]] (-0.56, fdr 4e-05), [[EEF1B2]] (-0.55, fdr 3e-05), [[RPL21]] (-0.53, fdr 2e-05, ⚠ RPL21 in the vector space only through flagged drug-doses), [[CD247]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1461.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.71×** | +8.8 | 1e-15 | 25/31 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.38×** | +7.3 | 7e-11 | 15/17 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.90×** | +5.2 | 4e-05 | 16/22 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.79×** | +5.1 | 5e-05 | 23/38 (KATO III, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +4.0 | 0.009 | 21/46 (SNU-423, AsPC-1, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.085 | 14/46 (LoVo, HCT15, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.50×** | +3.3 | 0.085 | 15/42 (NCI-H23, A-172, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1461.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 0.05 µM in 1 line (NCI-H23 0.0603×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.189×); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (NCI-H23 0.0846×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.573×** | -6.9 | 2e-09 | 27/42 (NCI-H1792, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.716×** | -4.1 | 0.009 | 27/41 (KATO III, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.706× | -3.1 | 0.42 | 13/45 (C32, HOP62, …) | two highest doses | cell-cycle shift (explains ~12% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1461. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 4.94 | 0 | 2 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0603× (z -9.6) |
| [[A498 (line)]] | wt | 11.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.71× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1792 (line)]] | alt | 7.31 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 7.12 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1461), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POP4]] | +0.65 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[HSD17B10]] ⚠ | +0.59 | +0.42 / +0.58 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RANBP6]] | +0.56 | +0.40 / +0.50 | both halves | 4e-05 |  |
| [[PIGQ]] | +0.55 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[GPS1]] | +0.55 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[SLC35A4]] | +0.54 | +0.33 / +0.70 | both halves | 1e-04 |  |
| [[SLC39A3]] | +0.54 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[MRPS18A]] | +0.54 | +0.49 / +0.50 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 977 |
| [[GPKOW]] | +0.54 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[BCKDK]] | +0.54 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[MSRB1]] | +0.54 | +0.37 / +0.46 | both halves | 8e-05 |  |
| [[MRPL35]] | +0.53 | +0.38 / +0.56 | both halves | 6e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 938 |
| [[PDHB]] | +0.53 | +0.52 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAP1L1]] | -0.56 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[EEF1B2]] | -0.55 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[RPL21]] ⚠ | -0.53 | -0.52 / -0.48 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CD247]] | -0.52 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[RPL23A]] | -0.51 | -0.37 / -0.60 | both halves | 8e-05 |  |
| [[KPNB1-DT]] | -0.51 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[RPS6]] ⚠ | -0.51 | -0.55 / -0.51 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LINC02976]] | -0.50 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[DDX59-AS1]] | -0.50 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[EOGT-DT]] | -0.49 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[KLF3-AS1]] | -0.48 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[RPL22]] | -0.48 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[RPS24]] | -0.48 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[GAS5]] | -0.47 | -0.63 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.425). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-52.1, -13.7); signed map (-17.8, -27.6). **Vector** length 47.5, 6.57% of its response variance represented; |z| ≥ 3 in 657 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.0 | +4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +2.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | -0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +1.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.2 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -6.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -1.5 | -3.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.3 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.2 | -2.5 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L28 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:366,969-371,289 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p15, bL28m; previously MAAT1 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q13084](https://www.uniprot.org/uniprotkb/Q13084) carries no function annotation.

**Summary**, from NCBI Gene [10573](https://www.ncbi.nlm.nih.gov/gene/10573):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14484](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14484) · Entrez [10573](https://www.ncbi.nlm.nih.gov/gene/10573) · UniProt [Q13084](https://www.uniprot.org/uniprotkb/Q13084) · Ensembl [ENSG00000086504](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086504)

## Data

Gene col 1461: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1461); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1461, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1461]; `tensor/DDL_lfc|DDL_z.npy` [1461]; `embed/gene_vectors.npy` [1461]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1461 or target_col == 1461). Every well: [[MRPL28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
