---
symbol: "RBM15-AS1"
type: "gene"
col: 13617
ensembl_id: "ENSG00000227963"
name: "RBM15 antisense RNA 1"
location: "1p13.3"
module: 26
arm: "+"
pooled_cpm: 2.38
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# RBM15-AS1

*RBM15 antisense RNA 1* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.65× (z +27.6, q 0e+00, up in 32 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.613× (z -5.5, q 2e-05, down in 11 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYLK4]] (+0.71, fdr 4e-05), [[SAXO1]] (+0.71, fdr 1e-05), [[SIAH2-AS1]] (+0.70, fdr 1e-05); moves opposite to [[METTL5]] (-0.60, fdr 1e-04), [[COMMD2]] (-0.58, fdr 9e-05), [[ZNF30]] (-0.56, fdr 6e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13617.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.65×** | +27.6 | 0e+00 | 32/32 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.78×** | +17.7 | 0e+00 | 10/12 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.01×** | +17.5 | 0e+00 | 1/2 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.12×** | +12.0 | 4e-31 | 20/33 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.97×** | +11.4 | 7e-28 | 3/4 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.96×** | +10.7 | 8e-25 | 16/44 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +8.7 | 2e-16 | 6/12 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.02×** | +7.9 | 2e-13 | 22/39 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +7.6 | 2e-12 | 9/31 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +6.4 | 1e-08 | 8/25 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.38×** | +3.7 | 0.012 | 3/46 (KATO III, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.37×** | +3.6 | 0.016 | 4/10 (NCI-H2030, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.33×** | +3.2 | 0.052 | 4/42 (Hs 766T, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13617.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.613×** | -5.5 | 2e-05 | 11/43 (A549, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.706×** | -3.8 | 0.047 | 8/39 (LoVo, AsPC-1, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM |  | **0.722×** | -3.7 | 0.048 | 4/44 (AN3 CA, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.737×** | -3.4 | 0.085 | 7/41 (SK-MEL-2, H4, …) | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 0.802× | -3.3 | 0.10 | 6/44 (SNU-1, AN3 CA, …) | inconsistent across doses |  |
| [[Zileuton (drug)]] 0.05 µM |  | 0.765× | -3.0 | 0.23 | 9/43 (LS 180, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13617. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 2.49 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.81× (z +9.2) | [[Tazarotene (drug)]] 0.5 µM 0.0670× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 2.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.84× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 3.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.90× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 2.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.13× (z +10.4) | — |
| [[SW480 (line)]] | alt | 4.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +10.5) | — |
| [[A-172 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13617), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYLK4]] | +0.71 | +0.42 / +0.73 | both halves | 4e-05 |  |
| [[SAXO1]] | +0.71 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[SIAH2-AS1]] | +0.70 | +0.54 / +0.62 | both halves | 1e-05 | same gene group |
| [[PIPOX]] | +0.68 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[NRL]] | +0.66 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[CCNT2-AS1]] | +0.66 | +0.56 / +0.60 | both halves | 1e-05 | same gene group |
| [[DDX19A-DT]] | +0.66 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[DRAIC]] | +0.65 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[CPEB2-DT]] | +0.65 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[TTC41P]] | +0.64 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[C2orf49-DT]] | +0.64 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ALG1L9P]] | +0.64 | +0.47 / +0.64 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL5]] | -0.60 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[COMMD2]] | -0.58 | -0.37 / -0.45 | both halves | 9e-05 |  |
| [[ZNF30]] | -0.56 | -0.22 / -0.46 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RBM15-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[OPRD1]] | B | OPRD1 activity raises RBM15-AS1's level | lines that do not express OPRD1 (28) vs lines expressing it (22) | 1.27× lower at baseline in the lines without OPRD1 | 0.021 | ⚠ within organs, on part of the lines; also absent: PHYHIPL, GPC3, RAB3C; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.635). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (11.8, 19.6); signed map (26.0, -2.1). **Vector** length 45.6, 4.99% of its response variance represented; |z| ≥ 3 in 1,118 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +27.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +17.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +11.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +17.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +10.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | -0.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.2 | +0.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.0 | +0.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.2 | -5.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +0.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +0.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | +0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -3.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -0.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | RBM15 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p13.3 — chr1:110,286,375-110,339,171 (-) |
| Ensembl biotype | lncRNA |
| Also known as | AS-RBM15 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53636](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53636) · Entrez [440600](https://www.ncbi.nlm.nih.gov/gene/440600) · Ensembl [ENSG00000227963](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227963)

## Data

Gene col 13617: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13617); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13617, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13617]; `tensor/DDL_lfc|DDL_z.npy` [13617]; `embed/gene_vectors.npy` [13617]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13617 or target_col == 13617). Every well: [[RBM15-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM15-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
