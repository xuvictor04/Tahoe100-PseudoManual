---
symbol: "PLCG1-AS1"
type: "gene"
col: 13545
ensembl_id: "ENSG00000226648"
name: "PLCG1 antisense RNA 1"
location: "20q12"
module: 21
arm: "+"
pooled_cpm: 7.07
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# PLCG1-AS1

*PLCG1 antisense RNA 1* — 20q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.48× (z +16.5, q 0e+00, up in 43 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.816× (z -8.9, q 4e-16, down in 36 of 48 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.0755×, SW480 0.243×); [[Naproxen (drug)]] 0.05 µM in 1 line (A-427 0.0844×); [[Thymol (drug)]] 0.05 µM in 1 line (SW 900 0.0785×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPTE2P6]] (+0.75, fdr 1e-05), [[PAXBP1-AS1]] (+0.74, fdr 1e-05), [[SYNM-AS1]] (+0.72, fdr 7e-06); moves opposite to [[NAA40]] (-0.59, fdr 1e-04).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13545.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.48×** | +16.5 | 0e+00 | 43/43 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.89×** | +13.1 | 6e-37 | 13/14 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.66×** | +12.6 | 3e-34 | 29/32 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.06×** | +8.6 | 1e-15 | 17/22 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +8.1 | 9e-14 | 27/43 (SK-MEL-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +7.8 | 8e-13 | 25/43 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +7.3 | 2e-11 | 26/40 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.67×** | +6.4 | 1e-08 | 26/46 (NCI-H1573, J82, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +5.6 | 1e-06 | 24/48 (PANC-1, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.48×** | +5.1 | 2e-05 | 17/44 (NCI-H1573, LS 180, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +5.0 | 4e-05 | 12/37 (NCI-H460, SHP-77, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +4.7 | 1e-04 | 16/41 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.4 | 6e-04 | 15/45 (SNU-423, LoVo, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.37×** | +4.1 | 0.002 | 11/47 (NCI-H1573, KATO III, …) | rises with dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.72×** | +3.7 | 0.009 | 2/17 (NCI-H1573, SW1417) | top dose only | noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.2 | 0.042 | 8/48 (HEC-1-A, A549, …) | top dose only |  |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.043 | 2/44 (NCI-H460, SNU-423) | inconsistent across doses | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.091 | 3/46 (LoVo, HepG2/C3A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13545.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.0755×, SW480 0.243×); [[Naproxen (drug)]] 0.05 µM in 1 line (A-427 0.0844×); [[Thymol (drug)]] 0.05 µM in 1 line (SW 900 0.0785×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.816×** | -8.9 | 4e-16 | 36/48 (KATO III, RKO, …) | inconsistent across doses |  |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | 0.833× | -3.3 | 0.30 | 6/48 (NCI-H2347, LS 180, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13545. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 8.07 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +12.6) | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.243× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 6.33 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.94× (z +9.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 5.57 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0844× (z -9.9) |
| [[A498 (line)]] | wt | 5.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 7.70 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.5 µM 0.0637× (z -9.3) |
| [[HS-578T (line)]] | alt | 6.23 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.110× (z -9.0) |
| [[J82 (line)]] | alt | 7.12 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.30× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 6.71 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0755× (z -10.4) |
| [[SW 900 (line)]] | alt | 7.16 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.0785× (z -9.6) |
| [[A-172 (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13545), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPTE2P6]] | +0.75 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[PAXBP1-AS1]] | +0.74 | +0.63 / +0.57 | both halves | 1e-05 | same gene group |
| [[SYNM-AS1]] | +0.72 | +0.67 / +0.64 | both halves | 7e-06 | same gene group |
| [[ZNF451-AS1]] | +0.72 | +0.67 / +0.56 | both halves | 1e-05 | same gene group |
| [[CHMP3-AS1]] | +0.71 | +0.67 / +0.58 | both halves | 7e-06 | same gene group |
| [[C2CD5-AS1]] | +0.71 | +0.62 / +0.57 | both halves | 1e-05 | same gene group |
| [[LINC01090]] | +0.71 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[EYS]] | +0.71 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SPEN-AS1]] | +0.70 | +0.55 / +0.56 | both halves | 1e-05 | same gene group |
| [[TTN]] | +0.70 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[SLC27A6]] | +0.69 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[PPP1R9A-AS1]] | +0.69 | +0.62 / +0.52 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA40]] | -0.59 | -0.44 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.698). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.9, 24.9); signed map (32.3, 2.2). **Vector** length 54.2, 6.87% of its response variance represented; |z| ≥ 3 in 936 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +16.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +8.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +4.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.4 | +2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +1.4 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -8.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +1.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | +0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | +0.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.0 | -2.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | PLCG1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20q12 — chr20:41,098,019-41,138,003 (-) |
| Ensembl biotype | lncRNA |
| Also known as | TOP1-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40450](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40450) · Entrez [101927117](https://www.ncbi.nlm.nih.gov/gene/101927117) · Ensembl [ENSG00000226648](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226648)

## Data

Gene col 13545: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13545); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13545, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13545]; `tensor/DDL_lfc|DDL_z.npy` [13545]; `embed/gene_vectors.npy` [13545]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13545 or target_col == 13545). Every well: [[PLCG1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLCG1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
