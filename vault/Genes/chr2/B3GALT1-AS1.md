---
symbol: "B3GALT1-AS1"
type: "gene"
col: 14011
ensembl_id: "ENSG00000235335"
name: "B3GALT1 antisense RNA 1"
location: "2q24.3"
module: 39
arm: "+"
pooled_cpm: 2.83
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# B3GALT1-AS1

*B3GALT1 antisense RNA 1* — 2q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 5.47× (z +15.0, q 0e+00, up in 5 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.53× (z +12.5, q 1e-33, up in 22 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 0.406× (z -4.5, q 0.002, down in 11 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMO7DN]] (+0.67, fdr 1e-05), [[ALDH8A1]] (+0.67, fdr 1e-05), [[FNDC7]] (+0.66, fdr 1e-05); moves opposite to [[TMEM254]] (-0.54, fdr 3e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FER1L6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14011.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.47×** | +15.0 | 0e+00 | 5/6 (LoVo, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.53×** | +12.5 | 1e-33 | 22/33 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.72×** | +9.1 | 2e-17 | 1/2 (HepG2/C3A) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.44×** | +8.5 | 2e-15 | 7/13 (AsPC-1, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +7.8 | 6e-13 | 17/32 (Panc 03.27, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +6.2 | 7e-08 | 9/31 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.75×** | +5.3 | 8e-06 | 14/45 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.004 | 9/41 (NCI-H460, A-427, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.048 | 12/37 (A-172, SNU-423, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.42×** | +3.1 | 0.088 | 12/39 (A-172, AsPC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +3.1 | 0.088 | 2/24 (SW480, SNU-423) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | 1.40× | +3.1 | 0.10 | 3/40 (LoVo, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14011.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.406×** | -4.5 | 0.002 | 11/26 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.719×** | -4.5 | 0.002 | 10/41 (HEC-1-A, HCT15, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.654×** | -4.1 | 0.009 | 11/41 (C32, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.477×** | -3.7 | 0.029 | 13/36 (LOX-IMVI, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.691×** | -3.5 | 0.044 | 12/42 (HepG2/C3A, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.720× | -3.2 | 0.15 | 16/42 (HepG2/C3A, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14011. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 14.6 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0393× (z -11.2) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0434× (z -10.8) |
| [[COLO 205 (line)]] | alt | 10.1 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0539× (z -9.4) |
| [[LoVo (line)]] | wt | 9.84 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 10.4× (z +8.6) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.110× (z -8.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 2.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.89× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 5.70 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0927× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~6% of this change |
| [[LOX-IMVI (line)]] | wt | 5.11 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0868× (z -8.7) |
| [[SW 900 (line)]] | alt | 9.16 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0782× (z -10.7) ⚠ cell-cycle shift, explains ~76% of this change |
| [[A-172 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.816 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.828 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.893 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.791 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.774 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14011), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMO7DN]] | +0.67 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[ALDH8A1]] | +0.67 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[FNDC7]] | +0.66 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[PPP1R36]] | +0.65 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[SLC2A9]] | +0.65 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[IMPA1P1]] | +0.65 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[OIT3]] | +0.64 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[NUP210L]] | +0.64 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[CORIN]] | +0.64 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[SH2D4B]] | +0.64 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[TMEM236]] | +0.64 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[C19orf38]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM254]] | -0.54 | -0.44 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FER1L6]] | B | FER1L6 activity raises B3GALT1-AS1's level | lines that do not express FER1L6 (7) vs lines expressing it (43) | 1.98× lower at baseline in the lines without FER1L6 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers B3GALT1-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.661). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.0, -14.5); signed map (17.6, 10.0). **Vector** length 57.7, 7.52% of its response variance represented; |z| ≥ 3 in 1,238 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +15.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +3.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +5.3 |
| fall | [[NG25 (drug)]] 5 µM |  | -2.2 | -4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -4.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | B3GALT1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q24.3 — chr2:167,814,757-167,941,180 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40089](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40089) · Entrez [105616981](https://www.ncbi.nlm.nih.gov/gene/105616981) · Ensembl [ENSG00000235335](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235335)

## Data

Gene col 14011: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14011); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14011, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14011]; `tensor/DDL_lfc|DDL_z.npy` [14011]; `embed/gene_vectors.npy` [14011]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14011 or target_col == 14011). Every well: [[B3GALT1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B3GALT1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
