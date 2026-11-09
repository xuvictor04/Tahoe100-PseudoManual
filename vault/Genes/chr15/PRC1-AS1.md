---
symbol: "PRC1-AS1"
type: "gene"
col: 15134
ensembl_id: "ENSG00000258725"
name: "PRC1 antisense RNA 1"
location: "15q26.1"
module: 39
arm: "+"
pooled_cpm: 6.24
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# PRC1-AS1

*PRC1 antisense RNA 1* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.88× (z +12.4, q 2e-32, up in 33 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.732× (z -4.3, q 0.008, down in 8 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Bendamustine (drug)]] 5 µM in 1 line (NCI-H23 0.0693×); [[Mifepristone (drug)]] 0.05 µM in 1 line (C-33 A 0.0695×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (A-172 0.105×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM15-AS1]] (+0.75, fdr 7e-06), [[BAAT]] (+0.75, fdr 7e-06), [[NPHP3-ACAD11]] (+0.74, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15134.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +12.4 | 2e-32 | 33/43 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +7.7 | 4e-12 | 6/9 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +6.0 | 3e-07 | 13/20 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.49×** | +5.6 | 4e-06 | 14/31 (Hs 766T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.28×** | +4.9 | 1e-04 | 10/47 (SW480, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +4.9 | 1e-04 | 17/42 (HOP62, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.005 | 7/44 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +3.4 | 0.054 | 11/34 (NCI-H1573, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.058 | 11/44 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.060 | 5/40 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.2 | 0.069 | 9/47 (A-172, A549, …) | top dose only |  |
| [[Nafamostat (mesylate) (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.100 | 3/45 (J82, SW48, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.25× | +3.0 | 0.10 | 4/45 (A-172, SW480, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 1.24× | +3.0 | 0.10 | 4/46 (KATO III, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15134.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Bendamustine (drug)]] 5 µM in 1 line (NCI-H23 0.0693×); [[Mifepristone (drug)]] 0.05 µM in 1 line (C-33 A 0.0695×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (A-172 0.105×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.732×** | -4.3 | 0.008 | 8/46 (NCI-H460, PANC-1, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.853× | -3.1 | 0.47 | 6/47 (AsPC-1, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15134. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 5.80 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +8.7) | [[Orlistat (drug)]] 0.05 µM 0.0986× (z -9.1) |
| [[A-172 (line)]] | wt | 7.57 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.105× (z -9.9) |
| [[A498 (line)]] | wt | 5.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 10.7 | 0 | 1 | — | [[Mifepristone (drug)]] 0.05 µM 0.0695× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 6.09 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0837× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 6.98 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0693× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 6.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.117× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 5.06 | 0 | 1 | — | [[Riluzole hydrochloride (drug)]] 0.5 µM 0.0723× (z -8.9) |
| [[SW1417 (line)]] | alt | 5.03 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.103× (z -9.6) |
| [[A-427 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.14 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15134), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM15-AS1]] | +0.75 | +0.63 / +0.73 | both halves | 7e-06 | same gene group |
| [[BAAT]] | +0.75 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[NPHP3-ACAD11]] | +0.74 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[QRICH2]] | +0.72 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[EFCAB8]] | +0.71 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[LINC01030]] | +0.71 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[SLC7A9]] | +0.71 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[FAM184B]] | +0.70 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ARL9]] | +0.70 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.69 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[CCDC62]] | +0.69 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[CNBD2]] | +0.69 | +0.60 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.688). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.8, -14.7); signed map (15.7, 4.0). **Vector** length 55.6, 6.96% of its response variance represented; |z| ≥ 3 in 919 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +1.4 |
|  | [[EX229 (drug)]] 5 µM |  | +1.2 | +1.7 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.5 | -2.9 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Bexarotene (drug)]] 5 µM |  | -1.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | PRC1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q26.1 — chr15:90,966,340-90,988,625 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48587) · Entrez [100507118](https://www.ncbi.nlm.nih.gov/gene/100507118) · Ensembl [ENSG00000258725](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258725)

## Data

Gene col 15134: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15134); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15134, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15134]; `tensor/DDL_lfc|DDL_z.npy` [15134]; `embed/gene_vectors.npy` [15134]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15134 or target_col == 15134). Every well: [[PRC1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRC1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
