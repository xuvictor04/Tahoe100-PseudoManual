---
symbol: "SVBP"
type: "gene"
col: 10871
ensembl_id: "ENSG00000177868"
name: "small vasohibin binding protein"
location: "1p34.2"
module: 24
arm: "+"
pooled_cpm: 6.85
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# SVBP

*small vasohibin binding protein* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.59× (z +9.6, q 6e-19, up in 25 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +7.5, q 8e-12, up in 34 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ferulic acid (drug)]] 0.5 µM in 1 line (A-172 0.0536×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (C-33 A 0.0555×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (C-33 A 0.0753×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARF5]] (+0.66, fdr 1e-05), [[NDUFA2]] (+0.65, fdr 1e-05), [[ADGRL3-AS1]] (+0.64, fdr 1e-05); moves opposite to [[GNL3L]] (-0.54, fdr 3e-05), [[LAS1L]] (-0.53, fdr 3e-05), [[RAD51D]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10871.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.59×** | +9.6 | 6e-19 | 25/29 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.33×** | +8.2 | 9e-14 | 9/13 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +7.5 | 8e-12 | 34/43 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.73×** | +5.5 | 5e-06 | 22/38 (HT-29, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +5.1 | 3e-05 | 10/18 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.013 | 14/43 (NCI-H23, PANC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.6 | 0.028 | 14/35 (CFPAC-1, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.36× | +3.1 | 0.15 | 9/43 (NCI-H23, LS 180, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.35× | +3.0 | 0.16 | 5/46 (RPMI-7951, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10871.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ferulic acid (drug)]] 0.5 µM in 1 line (A-172 0.0536×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (C-33 A 0.0555×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (C-33 A 0.0753×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.703× | -3.5 | 0.10 | 16/41 (NCI-H1573, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.688× | -3.5 | 0.10 | 7/46 (NCI-H2030, HCT15, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.694× | -3.5 | 0.10 | 12/44 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.722× | -3.1 | 0.24 | 11/45 (A498, HT-29, …) | top dose only |  |
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | 0.808× | -3.0 | 0.28 | 8/47 (CFPAC-1, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10871. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 9.47 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0555× (z -10.7) |
| [[A-172 (line)]] | wt | 4.40 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.5 µM 0.0536× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 6.36 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0860× (z -8.7) |
| [[A-427 (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10871), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARF5]] | +0.66 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[NDUFA2]] | +0.65 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ADGRL3-AS1]] | +0.64 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[DNAJC4]] | +0.60 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[MORC3]] | +0.60 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[TRIM52-AS1]] | +0.60 | +0.39 / +0.64 | both halves | 6e-05 |  |
| [[PPP1R2]] | +0.60 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[SNHG9]] | +0.59 | +0.38 / +0.64 | both halves | 7e-05 |  |
| [[SMIM27]] | +0.59 | +0.35 / +0.67 | both halves | 1e-04 |  |
| [[RABAC1]] | +0.58 | +0.37 / +0.62 | both halves | 8e-05 |  |
| [[DCTN6-DT]] | +0.58 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[FGFR1OP2]] | +0.58 | +0.45 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNL3L]] | -0.54 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[LAS1L]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[RAD51D]] | -0.53 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[SRSF10]] | -0.53 | -0.33 / -0.61 | both halves | 1e-04 |  |
| [[RRP15]] | -0.51 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[FARSB]] | -0.51 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[ABCE1]] | -0.51 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[ACSF3]] | -0.50 | -0.40 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.570). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-41.3, -24.1); signed map (-32.8, 11.5). **Vector** length 45.6, 5.83% of its response variance represented; |z| ≥ 3 in 661 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +9.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +3.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +2.6 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | +1.1 | +1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +3.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.0 | -0.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.1 | -3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -3.5 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.0 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -1.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | small vasohibin binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:42,807,052-42,817,397 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC45441; previously CCDC23 |
| Reactome | 1 pathways, smallest: Carboxyterminal post-translational modifications of tubulin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N300](https://www.uniprot.org/uniprotkb/Q8N300) (Small vasohibin-binding protein):

> Enhances the tyrosine carboxypeptidase activity of VASH1 and VASH2, thereby promoting the removal of the C-terminal tyrosine residue of alpha-tubulin. This activity is critical for spindle function and accurate chromosome segregation during mitosis since microtubule detyrosination regulates mitotic spindle length and postioning. Also required to enhance the solubility and secretion of VASH1 and VASH2. Plays a role in axon and excitatory synapse formation.

**Summary**, from NCBI Gene [374969](https://www.ncbi.nlm.nih.gov/gene/374969):

> Enables microtubule binding activity and peptidase activator activity. Involved in axon development; proteolysis; and regulation of metallopeptidase activity. Acts upstream of or within negative regulation of endothelial cell migration; negative regulation of protein ubiquitination; and protein secretion. Located in apical part of cell. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29204](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29204) · Entrez [374969](https://www.ncbi.nlm.nih.gov/gene/374969) · UniProt [Q8N300](https://www.uniprot.org/uniprotkb/Q8N300) · Ensembl [ENSG00000177868](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177868)

## Data

Gene col 10871: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10871); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10871, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10871]; `tensor/DDL_lfc|DDL_z.npy` [10871]; `embed/gene_vectors.npy` [10871]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10871 or target_col == 10871). Every well: [[SVBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SVBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
