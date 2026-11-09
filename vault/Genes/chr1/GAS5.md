---
symbol: "GAS5"
type: "gene"
col: 13980
ensembl_id: "ENSG00000234741"
name: "growth arrest specific 5"
location: "1q25.1"
module: 131
arm: "+"
pooled_cpm: 178.74
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# GAS5

*growth arrest specific 5* — 1q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 2.39× (z +4.5, q 0.002, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.370×; ⚠ cell-cycle shift, would explain all of this change); [[Tadalafil (drug)]] 5 µM in 1 line (SW 1088 0.0676×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFAS1]] (+0.85, fdr 7e-06), [[RPS23]] (+0.81, fdr 7e-06), [[SNHG8]] (+0.80, fdr 7e-06); moves opposite to [[TARDBP]] (-0.66, fdr 3e-05), [[RAB1B]] (-0.64, fdr 1e-05), [[SRP9]] (-0.62, fdr 1e-05).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13980.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.39×** | +4.5 | 0.002 | 47/48 (SW480, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.85×** | +4.5 | 0.002 | 44/48 (KATO III, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.79×** | +4.2 | 0.004 | 42/48 (PANC-1, SW 1271, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.1 | 0.007 | 30/49 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.69×** | +3.8 | 0.015 | 42/48 (HT-29, KATO III, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.68×** | +3.8 | 0.015 | 40/48 (CFPAC-1, SW 900, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.05×** | +3.7 | 0.016 | 44/48 (SW480, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.71×** | +3.7 | 0.016 | 40/48 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.02×** | +3.6 | 0.017 | 44/47 (LoVo, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.3 | 0.043 | 30/47 (SW 900, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +3.3 | 0.043 | 4/50 (AsPC-1, PANC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.3 | 0.043 | 34/47 (COLO 205, SNU-423, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.86×** | +3.2 | 0.055 | 40/48 (LoVo, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.85×** | +3.2 | 0.060 | 43/49 (AsPC-1, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.80×** | +3.0 | 0.090 | 39/48 (RPMI-7951, SW 900, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.370×; ⚠ cell-cycle shift, would explain all of this change); [[Tadalafil (drug)]] 5 µM in 1 line (SW 1088 0.0676×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13980. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 252 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 245 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +8.8) | — |
| [[SW 1088 (line)]] | alt | 93.4 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0676× (z -8.5) |
| [[A-172 (line)]] | wt | 96.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 333 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 167 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 174 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 152 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 207 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 150 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 127 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 127 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 102 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 146 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 97.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 362 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 235 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 187 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 94.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 314 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 228 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 216 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 91.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 225 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 174 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13980), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 20 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFAS1]] | +0.85 | +0.79 / +0.89 | both halves | 7e-06 | same gene group |
| [[RPS23]] | +0.81 | +0.70 / +0.87 | both halves | 7e-06 |  |
| [[SNHG8]] | +0.80 | +0.71 / +0.85 | both halves | 7e-06 | same gene group |
| [[EPB41L4A-AS1]] | +0.79 | +0.70 / +0.82 | both halves | 7e-06 | same gene group |
| [[RPS15]] ⚠ | +0.79 | +0.66 / +0.86 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG7]] | +0.79 | +0.70 / +0.82 | both halves | 7e-06 | same gene group |
| [[RPS13]] ⚠ | +0.78 | +0.63 / +0.85 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36A]] | +0.76 | +0.61 / +0.83 | both halves | 7e-06 |  |
| [[SNHG6]] | +0.75 | +0.66 / +0.80 | both halves | 7e-06 | same gene group |
| [[RPL8]] ⚠ | +0.75 | +0.65 / +0.80 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL7A]] | +0.75 | +0.58 / +0.85 | both halves | 7e-06 |  |
| [[RPL15]] | +0.75 | +0.58 / +0.82 | both halves | 8e-06 |  |
| [[SNHG25]] | +0.75 | +0.61 / +0.82 | both halves | 7e-06 | same gene group |
| [[RPS10]] | +0.74 | +0.60 / +0.84 | both halves | 7e-06 |  |
| [[RPL24]] | +0.73 | +0.59 / +0.79 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TARDBP]] | -0.66 | -0.45 / -0.72 | both halves | 3e-05 |  |
| [[RAB1B]] | -0.64 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[SRP9]] | -0.62 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[GPAA1]] | -0.62 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[POGLUT3]] | -0.61 | -0.48 / -0.66 | both halves | 2e-05 |  |
| [[CBX5]] | -0.61 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[TGOLN2]] | -0.61 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[HMGN1]] | -0.60 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[DR1]] | -0.59 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[NCBP1]] | -0.59 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[HNRNPUL1]] | -0.57 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[TMX1]] | -0.57 | -0.50 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.750). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-40.6, -28.6); signed map (-62.9, -3.2). **Vector** length 130, 58.4% of its response variance represented; |z| ≥ 3 in 676 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Termination* (reactome, mean cos +0.71 to 20); *Peptide chain elongation* (reactome, mean cos +0.72 to 19); *PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA* (reactome, mean cos +0.72 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +5.5 | +4.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.6 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +1.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +4.3 | +2.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +3.9 | +2.3 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +3.5 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +1.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.2 | +1.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.2 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.9 | +0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | -0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | +0.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.9 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.8 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | growth arrest specific 5 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q25.1 — chr1:173,858,559-173,868,882 (-) |
| Ensembl biotype | lncRNA |
| Also known as | SNHG2, NCRNA00030 |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes; Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [60674](https://www.ncbi.nlm.nih.gov/gene/60674):

> This gene produces a spliced long non-coding RNA and is a member of the 5' terminal oligo-pyrimidine class of genes. It is a small nucleolar RNA host gene, containing multiple C/D box snoRNA genes in its introns. Part of the secondary RNA structure of the encoded transcript mimics glucocorticoid response element (GRE) which means it can bind to the DNA binding domain of the glucocorticoid receptor (nuclear receptor subfamily 3, group C, member 1). This action blocks the glucocorticoid receptor …

**Accessions** — [HGNC:16355](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16355) · Entrez [60674](https://www.ncbi.nlm.nih.gov/gene/60674) · Ensembl [ENSG00000234741](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234741)

## Data

Gene col 13980: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13980); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13980, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13980]; `tensor/DDL_lfc|DDL_z.npy` [13980]; `embed/gene_vectors.npy` [13980]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13980 or target_col == 13980). Every well: [[GAS5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAS5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
