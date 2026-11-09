---
symbol: "CCDC142"
type: "gene"
col: 5736
ensembl_id: "ENSG00000135637"
name: "coiled-coil domain containing 142"
location: "2p13.1"
module: 118
arm: "+"
pooled_cpm: 15.75
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# CCDC142

*coiled-coil domain containing 142* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.50× (z +7.1, q 5e-10, up in 34 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 0.361×, A-427 0.393×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (SNU-423 0.203×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (HCT15 0.185×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJC30]] (+0.69, fdr 1e-05), [[COA6]] (+0.64, fdr 3e-05), [[ATP6V0E1]] (+0.62, fdr 9e-06); moves opposite to [[SSRP1]] (-0.62, fdr 1e-05), [[DNAJC10]] (-0.61, fdr 2e-05), [[TRAP1]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 118]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5736.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +7.1 | 5e-10 | 34/47 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.62×** | +6.0 | 4e-07 | 21/38 (NCI-H1792, A498, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.6 | 9e-04 | 23/48 (A498, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +4.4 | 0.001 | 15/32 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +4.4 | 0.001 | 20/43 (HS-578T, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.2 | 0.002 | 21/47 (NCI-H23, SW1417, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.0 | 0.006 | 0/48 | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.022 | 15/47 (SW48, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.22×** | +3.5 | 0.027 | 15/48 (CFPAC-1, RKO, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.3 | 0.062 | 10/30 (NCI-H460, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.074 | 14/46 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.47×** | +3.2 | 0.074 | 12/44 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.076 | 10/44 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 0.361×, A-427 0.393×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (SNU-423 0.203×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (HCT15 0.185×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5736. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 15.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 26.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 20.1 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.185× (z -8.9) |
| [[SNU-423 (line)]] | alt | 13.2 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.203× (z -9.2) |
| [[A498 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5736), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC30]] | +0.69 | +0.49 / +0.72 | both halves | 1e-05 |  |
| [[COA6]] | +0.64 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[ATP6V0E1]] | +0.62 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[SMIM27]] | +0.61 | +0.39 / +0.62 | both halves | 6e-05 |  |
| [[KBTBD4]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[TEFM]] | +0.60 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[SUPT7L]] | +0.60 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[PCF11-AS1]] | +0.59 | +0.38 / +0.49 | both halves | 7e-05 |  |
| [[C1orf56]] | +0.59 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[VAMP8]] | +0.59 | +0.33 / +0.59 | both halves | 1e-04 |  |
| [[EAPP]] | +0.59 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[SYNRG]] | +0.59 | +0.44 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSRP1]] | -0.62 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[DNAJC10]] | -0.61 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[TRAP1]] | -0.56 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[SSX2IP]] | -0.56 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[CDCA7L]] | -0.55 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[GGCT]] | -0.52 | -0.52 / -0.37 | both halves | 9e-05 |  |
| [[COTL1]] | -0.51 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[HTATSF1]] | -0.51 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[PHF6]] | -0.50 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[CEP83]] | -0.50 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[NIN]] | -0.50 | -0.36 / -0.42 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.733). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-46.4, 9.1); signed map (-5.6, -4.7). **Vector** length 53.3, 8.21% of its response variance represented; |z| ≥ 3 in 546 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +4.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.7 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +3.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.5 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -0.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | +0.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 142 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:74,471,986-74,483,408 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14397 |
| Matched by | ensembl_id |

UniProt [Q17RM4](https://www.uniprot.org/uniprotkb/Q17RM4) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25889](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25889) · Entrez [84865](https://www.ncbi.nlm.nih.gov/gene/84865) · UniProt [Q17RM4](https://www.uniprot.org/uniprotkb/Q17RM4) · Ensembl [ENSG00000135637](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135637)

## Data

Gene col 5736: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5736); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5736, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5736]; `tensor/DDL_lfc|DDL_z.npy` [5736]; `embed/gene_vectors.npy` [5736]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5736 or target_col == 5736). Every well: [[CCDC142 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC142.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
