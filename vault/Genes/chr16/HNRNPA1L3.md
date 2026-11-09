---
symbol: "HNRNPA1L3"
type: "gene"
col: 13405
ensembl_id: "ENSG00000224578"
name: "heterogeneous nuclear ribonucleoprotein A1 like 3"
location: "16q12.1"
module: 20
arm: "+"
pooled_cpm: 6.36
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# HNRNPA1L3

*heterogeneous nuclear ribonucleoprotein A1 like 3* — 16q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.64× (z +14.8, q 0e+00, up in 26 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.31× (z +4.4, q 0.001, up in 18 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.771× (z -10.5, q 6e-23, down in 39 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Trimetrexate (drug)]] 0.5 µM: 0.661× (z -4.7, q 6e-04, down in 17 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EEF1A1P5]] (+0.75, fdr 7e-06), [[EEF1A1]] (+0.73, fdr 7e-06), [[HNRNPA1]] (+0.72, fdr 7e-06); moves opposite to [[PIAS4]] (-0.58, fdr 1e-05), [[MRPS18C]] (-0.56, fdr 6e-05), [[LRRC8E]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13405.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.64×** | +14.8 | 0e+00 | 26/27 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.18×** | +12.7 | 1e-34 | 15/15 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.15×** | +11.5 | 2e-28 | 18/20 (LoVo, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +5.0 | 6e-05 | 17/34 (NCI-H1792, J82, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.4 | 0.001 | 18/40 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.92×** | +3.9 | 0.009 | 3/15 (SNU-423, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **1.40×** | +3.8 | 0.011 | 8/35 (LoVo, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.042 | 12/44 (NCI-H2030, A-172, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.71×** | +3.2 | 0.079 | 5/41 (KATO III, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13405.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.771×** | -10.5 | 6e-23 | 39/48 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Trimetrexate (drug)]] 0.5 µM |  | **0.661×** | -4.7 | 6e-04 | 17/44 (hTERT-HPNE, SW480, …) | two highest doses | position effect removed |
| [[Ferulic acid (drug)]] 0.5 µM |  | **0.671×** | -4.6 | 9e-04 | 13/45 (HS-578T, J82, …) | two highest doses | low cells (technical?); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **0.727×** | -3.6 | 0.038 | 14/41 (KATO III, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.653×** | -3.5 | 0.055 | 12/35 (CFPAC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.815×** | -3.3 | 0.074 | 12/47 (Panc 03.27, SHP-77, …) | top dose only |  |
| [[Bergenin (drug)]] 0.5 µM |  | **0.751×** | -3.3 | 0.074 | 13/44 (SHP-77, HOP62, …) | inconsistent across doses | position effect removed |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **0.751×** | -3.3 | 0.074 | 8/41 (RKO, PANC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.762× | -3.1 | 0.12 | 13/46 (SW1417, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13405. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 7.98 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.21× (z +10.1) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 4.16 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.301× (z -8.7) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SW480 (line)]] | alt | 10.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.41× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13405), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEF1A1P5]] | +0.75 | +0.64 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[EEF1A1]] | +0.73 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[HNRNPA1]] | +0.72 | +0.78 / +0.72 | both halves | 7e-06 | STRING 801 |
| [[EIF4H]] | +0.70 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[NONO]] | +0.67 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[IPO5]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[PAPOLA]] | +0.65 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[RPL4]] | +0.65 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[RPL3]] | +0.64 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[CRTAP]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[TWF1]] | +0.62 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[TOP2B]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIAS4]] | -0.58 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[MRPS18C]] | -0.56 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[LRRC8E]] | -0.55 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[CROCCP2-1]] | -0.54 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[ISG20L2]] | -0.54 | -0.39 / -0.57 | both halves | 6e-05 |  |
| [[TMEM70]] | -0.53 | -0.30 / -0.55 | both halves | 2e-04 |  |
| [[TIMM29]] | -0.53 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[ADPRS]] | -0.53 | -0.36 / -0.57 | both halves | 1e-04 |  |
| [[TRAPPC2B]] | -0.53 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[SDHAF1]] | -0.53 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[RPP14]] | -0.52 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[CHKB]] | -0.52 | -0.56 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.614). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-29.8, -25.1); signed map (-22.0, -34.0). **Vector** length 53.1, 6.72% of its response variance represented; |z| ≥ 3 in 846 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cap-dependent Translation Initiation* (reactome, mean cos +0.52 to 12); *Eukaryotic Translation Initiation* (reactome, mean cos +0.52 to 12); *L13a-mediated translational silencing of Ceruloplasmin expression* (reactome, mean cos +0.55 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.9 | +14.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +11.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +4.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | -0.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +3.0 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -3.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.5 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | +0.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -10.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.3 | +0.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -0.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | heterogeneous nuclear ribonucleoprotein A1 like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.1 — chr16:51,553,436-51,647,132 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HNRNPA1P48 |
| Matched by | ensembl_id |

UniProt [A0A2R8Y4L2](https://www.uniprot.org/uniprotkb/A0A2R8Y4L2) carries no function annotation.

**Summary**, from NCBI Gene [642659](https://www.ncbi.nlm.nih.gov/gene/642659):

> Predicted to enable mRNA 3'-UTR binding activity. Predicted to be involved in mRNA splicing, via spliceosome. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:48778](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48778) · Entrez [642659](https://www.ncbi.nlm.nih.gov/gene/642659) · UniProt [A0A2R8Y4L2](https://www.uniprot.org/uniprotkb/A0A2R8Y4L2) · Ensembl [ENSG00000224578](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224578)

## Data

Gene col 13405: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13405); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13405, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13405]; `tensor/DDL_lfc|DDL_z.npy` [13405]; `embed/gene_vectors.npy` [13405]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13405 or target_col == 13405). Every well: [[HNRNPA1L3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNRNPA1L3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
