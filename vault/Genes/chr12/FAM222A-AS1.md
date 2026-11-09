---
symbol: "FAM222A-AS1"
type: "gene"
col: 14952
ensembl_id: "ENSG00000255650"
name: "FAM222A antisense RNA 1"
location: "12q24.11"
module: 33
arm: "+"
pooled_cpm: 3.18
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# FAM222A-AS1

*FAM222A antisense RNA 1* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.77× (z +9.7, q 3e-19, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.34× (z +8.4, q 1e-14, up in 22 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Epirubicin (hydrochloride) (drug)]] 0.5 µM: 0.664× (z -4.1, q 0.020, down in 13 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR3H]] (+0.61, fdr 1e-05), [[TMEM241]] (+0.60, fdr 3e-04), [[NLE1]] (+0.59, fdr 3e-05); moves opposite to [[BMPR2]] (-0.53, fdr 1e-05), [[LRRC57]] (-0.51, fdr 1e-04), [[TMEM59]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FAM78B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14952.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.77×** | +9.7 | 3e-19 | 1/3 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.34×** | +8.4 | 1e-14 | 22/41 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.19×** | +7.7 | 2e-12 | 18/40 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.21×** | +7.2 | 8e-11 | 3/5 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.06×** | +7.1 | 1e-10 | 6/14 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +5.6 | 2e-06 | 15/41 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.61×** | +4.7 | 2e-04 | 15/42 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +4.3 | 0.001 | 12/37 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +4.1 | 0.002 | 5/42 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.007 | 9/29 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.32×** | +3.8 | 0.007 | 8/26 (A-172, HOP62, …) | top dose only | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **2.08×** | +3.8 | 0.008 | 10/20 (SW1417, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.48×** | +3.7 | 0.010 | 6/16 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.44×** | +3.6 | 0.013 | 9/40 (NCI-H2347, PANC-1, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.90×** | +3.3 | 0.034 | 10/18 (SW1417, KATO III, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14952.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.664×** | -4.1 | 0.020 | 13/41 (HEC-1-A, SW1417, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.674×** | -3.9 | 0.020 | 12/30 (RKO, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.676×** | -3.9 | 0.020 | 14/41 (SW48, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Neratinib (drug)]] 0.5 µM |  | **0.681×** | -3.8 | 0.020 | 5/40 (AsPC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Cyclosporin A (drug)]] 5 µM |  | **0.697×** | -3.6 | 0.039 | 8/41 (C-33 A, J82, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.701×** | -3.5 | 0.041 | 11/38 (Hs 766T, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.719×** | -3.3 | 0.087 | 15/43 (RKO, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.703×** | -3.2 | 0.089 | 6/42 (A-427, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14952. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 21.5 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -12.9) |
| [[RKO (line)]] | wt | 15.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0680× (z -11.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0648× (z -10.8) |
| [[Hs 766T (line)]] | wt | 3.75 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0326× (z -10.0) |
| [[LoVo (line)]] | wt | 9.13 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0734× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 1.49 | 0 | 1 | — | [[Macitentan (drug)]] 5 µM 0.0686× (z -8.7) |
| [[SW480 (line)]] | alt | 6.67 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -10.5) |
| [[A-172 (line)]] | wt | 0.797 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.847 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.623 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.844 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.864 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.878 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.975 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.850 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.826 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14952), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR3H]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[TMEM241]] | +0.60 | +0.29 / +0.69 | both halves | 3e-04 |  |
| [[NLE1]] | +0.59 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[RRP7BP]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[LINC01357]] | +0.58 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[PALD1]] | +0.58 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[PRR5]] | +0.58 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[PRR5-ARHGAP8]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[DCAF4]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[LINC01399]] | +0.57 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[LINC01237]] | +0.57 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[PIWIL1]] | +0.57 | +0.54 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMPR2]] | -0.53 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[LRRC57]] | -0.51 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[TMEM59]] | -0.51 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[SMIM14]] | -0.50 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[SOS2]] | -0.47 | -0.43 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM78B]] | B | FAM78B activity raises FAM222A-AS1's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.39× lower at baseline in the lines without FAM78B | 0.073 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[GARNL3]] | C | GARNL3 activity raises FAM222A-AS1's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 1.60× lower at baseline in the lines without GARNL3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.594). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (0.1, 44.9); signed map (-1.3, 27.5). **Vector** length 58.6, 8.73% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +5.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +3.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.4 | +8.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.3 | +4.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +3.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | +1.0 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.7 | +0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.0 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | +0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.3 | -1.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | FAM222A antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q24.11 — chr12:109,734,166-109,773,508 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28223](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28223) · Entrez [84983](https://www.ncbi.nlm.nih.gov/gene/84983) · Ensembl [ENSG00000255650](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255650)

## Data

Gene col 14952: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14952); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14952, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14952]; `tensor/DDL_lfc|DDL_z.npy` [14952]; `embed/gene_vectors.npy` [14952]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14952 or target_col == 14952). Every well: [[FAM222A-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM222A-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
