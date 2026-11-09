---
symbol: "SPTBN1-AS2"
type: "gene"
col: 14162
ensembl_id: "ENSG00000238018"
name: "SPTBN1 antisense RNA 2"
location: "2p16.2"
module: 21
arm: "+"
pooled_cpm: 6.99
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# SPTBN1-AS2

*SPTBN1 antisense RNA 2* — 2p16.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.87× (z +11.8, q 1e-29, up in 26 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.29× (z +4.0, q 0.007, up in 12 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.875× (z -5.4, q 5e-05, down in 19 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Larotrectinib (drug)]] 5 µM: 0.786× (z -3.8, q 0.027, down in 11 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.194×, KATO III 0.310×; ⚠ cell-cycle shift, would explain all of this change); [[Ferulic acid (drug)]] 0.5 µM in 1 line (HCT15 0.0556×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (RPMI-7951 0.0688×); [[Voriconazole (drug)]] 0.5 µM in 1 line (BT-474 0.0578×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TICAM2-AS1]] (+0.79, fdr 7e-06), [[CNGB3]] (+0.78, fdr 7e-06), [[C12orf40]] (+0.75, fdr 7e-06); moves opposite to [[TXLNA]] (-0.57, fdr 4e-05), [[NANP]] (-0.53, fdr 6e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14162.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.87×** | +11.8 | 1e-29 | 26/30 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.68×** | +10.6 | 5e-24 | 12/13 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.30×** | +8.1 | 8e-14 | 19/22 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.64×** | +5.5 | 4e-06 | 19/38 (AsPC-1, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.007 | 12/42 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.035 | 12/38 (A-172, C32, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +3.5 | 0.044 | 14/43 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.3 | 0.064 | 9/37 (LoVo, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.51×** | +3.3 | 0.064 | 7/45 (MIA PaCa-2, HOP62, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.095 | 4/45 (NCI-H2030, NCI-H23, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14162.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.194×, KATO III 0.310×; ⚠ cell-cycle shift, would explain all of this change); [[Ferulic acid (drug)]] 0.5 µM in 1 line (HCT15 0.0556×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (RPMI-7951 0.0688×); [[Voriconazole (drug)]] 0.5 µM in 1 line (BT-474 0.0578×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.875× | -5.4 | 5e-05 | 19/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.712×** | -3.8 | 0.027 | 13/47 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | **0.786×** | -3.8 | 0.027 | 11/46 (CFPAC-1, SW480, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14162. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 4.89 | 0 | 1 | — | [[Voriconazole (drug)]] 0.5 µM 0.0578× (z -9.2) |
| [[HCT15 (line)]] | alt | 7.10 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.5 µM 0.0556× (z -10.2) |
| [[KATO III (line)]] | alt | 9.50 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 8.60 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +9.0) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 7.76 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0688× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 6.72 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 6.38 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 8.85 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14162), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TICAM2-AS1]] | +0.79 | +0.71 / +0.79 | both halves | 7e-06 | same gene group |
| [[CNGB3]] | +0.78 | +0.62 / +0.81 | both halves | 7e-06 |  |
| [[C12orf40]] | +0.75 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[FLJ40194]] | +0.73 | +0.52 / +0.75 | both halves | 1e-05 |  |
| [[MAL2-AS1]] | +0.73 | +0.59 / +0.76 | both halves | 7e-06 | same gene group |
| [[HSPA2-AS1]] | +0.73 | +0.65 / +0.75 | both halves | 7e-06 | same gene group |
| [[FAM217A]] | +0.73 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[ZRANB2-AS1]] | +0.73 | +0.60 / +0.75 | both halves | 7e-06 | same gene group |
| [[EFCAB14-AS1]] | +0.72 | +0.73 / +0.72 | both halves | 7e-06 | same gene group |
| [[DSG2-AS1]] | +0.72 | +0.52 / +0.77 | both halves | 1e-05 | same gene group |
| [[RN7SL1]] | +0.72 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[LRRC37A16P]] | +0.72 | +0.59 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXLNA]] | -0.57 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[NANP]] | -0.53 | -0.39 / -0.56 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.771). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.5, 28.0); signed map (34.0, 4.9). **Vector** length 41.0, 4.28% of its response variance represented; |z| ≥ 3 in 742 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.3 | +1.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.3 | +1.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -2.1 | -3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -5.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -0.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -1.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.0 | -0.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | SPTBN1 antisense RNA 2 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2p16.2 — chr2:54,661,011-54,680,045 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40563](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40563) · Entrez [123706536](https://www.ncbi.nlm.nih.gov/gene/123706536) · Ensembl [ENSG00000238018](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000238018)

## Data

Gene col 14162: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14162); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14162, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14162]; `tensor/DDL_lfc|DDL_z.npy` [14162]; `embed/gene_vectors.npy` [14162]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14162 or target_col == 14162). Every well: [[SPTBN1-AS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPTBN1-AS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
