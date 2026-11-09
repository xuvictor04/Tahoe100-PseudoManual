---
symbol: "MSL3P1"
type: "gene"
col: 13393
ensembl_id: "ENSG00000224287"
name: "MSL complex subunit 3B"
location: "2q37.1"
module: 11
arm: "+"
pooled_cpm: 7.62
n_lines_expressing: 44
n_dd_up: 7
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# MSL3P1

*MSL complex subunit 3B* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.13× (z +8.6, q 5e-15, up in 23 of 32 measured lines) ⚠ toxic. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.60× (z +5.6, q 7e-06, up in 20 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.489× (z -11.9, q 6e-30, down in 32 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL9]] (+0.79, fdr 7e-06), [[KBTBD6]] (+0.73, fdr 7e-06), [[GSPT2]] (+0.73, fdr 7e-06); moves opposite to [[ATP11C]] (-0.62, fdr 3e-05), [[PRDM10]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13393.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +8.6 | 5e-15 | 23/32 (HEC-1-A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +5.6 | 7e-06 | 20/41 (NCI-H1792, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +5.2 | 4e-05 | 21/40 (A498, AsPC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.52×** | +5.0 | 1e-04 | 14/31 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +4.8 | 2e-04 | 17/40 (HEC-1-A, A-427, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.38×** | +3.5 | 0.038 | 11/36 (PANC-1, LoVo, …) | all doses, flat | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +3.5 | 0.038 | 5/18 (NCI-H1792, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.31× | +3.2 | 0.12 | 12/41 (NCI-H1573, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13393.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.489×** | -11.9 | 6e-30 | 32/38 (A498, SNU-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.518×** | -7.5 | 3e-11 | 22/36 (LS 180, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.598×** | -6.1 | 3e-07 | 24/42 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.710×** | -5.7 | 2e-06 | 17/41 (SW1417, SNU-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.627×** | -5.5 | 5e-06 | 16/40 (PANC-1, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.692×** | -4.2 | 0.003 | 13/39 (HEC-1-A, A549, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.717×** | -3.9 | 0.008 | 16/40 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.725×** | -3.6 | 0.020 | 14/37 (LS 180, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.731×** | -3.5 | 0.031 | 12/39 (SW 900, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13393. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 20.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -10.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -8.7) |
| [[A498 (line)]] | wt | 11.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 12.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -10.0) |
| [[LoVo (line)]] | wt | 11.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[NCI-H1792 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 30.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -11.5) |
| [[SW480 (line)]] | alt | 6.30 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.200× (z -8.9) |
| [[A-172 (line)]] | wt | 0.667 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.712 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.987 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13393), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL9]] | +0.79 | +0.69 / +0.80 | both halves | 7e-06 |  |
| [[KBTBD6]] | +0.73 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[GSPT2]] | +0.73 | +0.64 / +0.81 | both halves | 7e-06 |  |
| [[MAGEF1]] | +0.72 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[COG2]] | +0.72 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[AGGF1]] | +0.70 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[ZNF22]] | +0.69 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[ZNF23]] | +0.68 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[REXO4]] | +0.66 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[RP9]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[KAT14]] | +0.65 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[ZNF45]] | +0.65 | +0.48 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP11C]] | -0.62 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[PRDM10]] | -0.59 | -0.49 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MSL3P1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CYP2R1]] | C | CYP2R1 activity raises MSL3P1's level | lines that do not express CYP2R1 (3) vs lines expressing it (47) | 3.47× lower at baseline in the lines without CYP2R1 | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: PIM2, CDCA7, NMRAL1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.523). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-30.3, -1.1); signed map (-0.8, -22.7). **Vector** length 61.3, 10.8% of its response variance represented; |z| ≥ 3 in 641 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.6 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +8.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +0.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -11.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -1.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.8 | -1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | MSL complex subunit 3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:233,866,129-233,868,230 (-) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Also known as | ; previously MSL3L2, MSL3P1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P0C860](https://www.uniprot.org/uniprotkb/P0C860) (MSL complex subunit 3B):

> Probable non-catalytic component of the MSL histone acetyltransferase complex, a multiprotein complex that mediates the majority of histone H4 acetylation at 'Lys-16' (H4K16ac), an epigenetic mark that prevents chromatin compaction.

**Summary**, from NCBI Gene [151507](https://www.ncbi.nlm.nih.gov/gene/151507):

> Predicted to be involved in DNA-templated transcription; chromatin organization; and regulation of DNA-templated transcription. Predicted to be located in nucleus. Predicted to be part of MSL complex and NuA4 histone acetyltransferase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17837](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17837) · Entrez [151507](https://www.ncbi.nlm.nih.gov/gene/151507) · UniProt [P0C860](https://www.uniprot.org/uniprotkb/P0C860) · Ensembl [ENSG00000224287](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224287)

## Data

Gene col 13393: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13393); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13393, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13393]; `tensor/DDL_lfc|DDL_z.npy` [13393]; `embed/gene_vectors.npy` [13393]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13393 or target_col == 13393). Every well: [[MSL3P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSL3P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
