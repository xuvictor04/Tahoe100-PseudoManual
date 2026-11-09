---
symbol: "HOTAIRM1"
type: "gene"
col: 13902
ensembl_id: "ENSG00000233429"
name: "HOXA transcript antisense RNA, myeloid-specific 1"
location: "7p15.2"
module: 4
arm: "-"
pooled_cpm: 15.58
n_lines_expressing: 36
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# HOTAIRM1

*HOXA transcript antisense RNA, myeloid-specific 1* — 7p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.79× (z +7.6, q 2e-11, up in 27 of 29 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.97× (z +7.4, q 5e-11, up in 26 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Folic acid (drug)]] 5 µM: 0.696× (z -3.9, q 0.056, down in 20 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW 900 0.136×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNHG9]] (+0.72, fdr 7e-06), [[TERF2IP]] (+0.67, fdr 7e-06), [[MRPL33]] (+0.66, fdr 7e-06); moves opposite to [[LRPPRC]] (-0.68, fdr 7e-06), [[PRKDC]] (-0.68, fdr 7e-06), [[EFTUD2]] (-0.66, fdr 7e-06).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[TGOLN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13902.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.79×** | +7.6 | 2e-11 | 27/29 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +7.4 | 5e-11 | 26/31 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.43×** | +6.8 | 2e-09 | 27/32 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.30×** | +6.4 | 2e-08 | 24/33 (HCT15, A-427, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.74×** | +6.0 | 2e-07 | 23/32 (LoVo, SW1417, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.73×** | +4.2 | 0.002 | 17/30 (H4, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.68×** | +3.9 | 0.009 | 17/33 (LoVo, SW1417, …) | rises with dose | composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.4 | 0.041 | 16/33 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.4 | 0.042 | 16/30 (LoVo, A-172, …) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.83×** | +3.3 | 0.049 | 15/31 (A498, HS-578T, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.82×** | +3.3 | 0.049 | 18/29 (A-427, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +3.3 | 0.049 | 17/31 (SW480, A-427, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.54×** | +3.2 | 0.056 | 17/28 (PANC-1, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.50×** | +3.1 | 0.072 | 11/25 (PANC-1, SW480, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13902.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW 900 0.136×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Folic acid (drug)]] 5 µM |  | **0.696×** | -3.9 | 0.056 | 20/34 (SW480, SNU-423, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.754× | -3.0 | 0.67 | 16/34 (A498, SW 1271, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13902. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 14.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +10.0) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[PANC-1 (line)]] | alt | 25.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 30.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 43.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.57× (z +8.8) ⚠ toxic | — |
| [[SW480 (line)]] | alt | 17.6 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.14× (z +10.0) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13902), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 8 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG9]] | +0.72 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[TERF2IP]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[MRPL33]] | +0.66 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[GABARAPL2]] | +0.65 | +0.57 / +0.71 | both halves | 8e-06 |  |
| [[COX17]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ACAP1]] | +0.62 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[CCDC126]] | +0.62 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[DCTN6-DT]] | +0.62 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[SNHG19]] | +0.62 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[ZMYM5]] | +0.62 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[PURA]] | +0.61 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[EIF1B]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRPPRC]] | -0.68 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[PRKDC]] | -0.68 | -0.65 / -0.68 | both halves | 7e-06 |  |
| [[EFTUD2]] | -0.66 | -0.65 / -0.67 | both halves | 7e-06 |  |
| [[NUP155]] | -0.65 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[EIF2S1]] | -0.65 | -0.51 / -0.70 | both halves | 1e-05 |  |
| [[CCT7]] | -0.64 | -0.54 / -0.72 | both halves | 1e-05 |  |
| [[XRCC5]] | -0.64 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[XRCC6]] | -0.63 | -0.57 / -0.66 | both halves | 9e-06 |  |
| [[MTHFD1]] | -0.63 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[FANCG]] | -0.61 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[API5]] | -0.61 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[SMU1]] | -0.60 | -0.61 / -0.62 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGOLN2]] | B | HOTAIRM1 activity raises TGOLN2's level | lines that do not express HOTAIRM1 (14) vs lines expressing it (36) | 1.31× lower at baseline in the lines without HOTAIRM1 | 0.052 | ⚠ within organs, on part of the lines; also absent: GXYLT2, HOXA5, SOBP |
| [[SLC30A4]] | B | HOTAIRM1 activity raises SLC30A4's level | lines that do not express HOTAIRM1 (14) vs lines expressing it (36) | 1.25× lower at baseline in the lines without HOTAIRM1 | 0.052 | ⚠ within organs, on part of the lines; also absent: GXYLT2, HOXA5, SOBP |
| [[RNF19A]] | B | HOTAIRM1 activity lowers RNF19A's level | lines that do not express HOTAIRM1 (14) vs lines expressing it (36) | 1.40× higher at baseline in the lines without HOTAIRM1 | 0.072 | ⚠ within organs, on part of the lines; also absent: GXYLT2, HOXA5, SOBP |
| [[ACAP1]] | B | HOTAIRM1 activity raises ACAP1's level | lines that do not express HOTAIRM1 (14) vs lines expressing it (36) | 1.42× lower at baseline in the lines without HOTAIRM1 | 0.074 | ⚠ within organs, on part of the lines; also absent: GXYLT2, HOXA5, SOBP |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.612). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-30.6, -31.9); signed map (-6.9, 5.0). **Vector** length 72.3, 19.7% of its response variance represented; |z| ≥ 3 in 511 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +4.0 | +6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +6.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +6.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +0.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +2.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -0.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.9 | -2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | HOXA transcript antisense RNA, myeloid-specific 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7p15.2 — chr7:27,095,647-27,100,265 (+) |
| Ensembl biotype | lncRNA |
| Also known as | HOXA-AS1, NCRNA00179, HOXA1-AS1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100506311](https://www.ncbi.nlm.nih.gov/gene/100506311):

> This non-coding locus is located in the HOX gene cluster. Transcription of this locus is induced by retinoic acid, and transcripts likely function in regulation of myelopoiesis through transcriptional activation of several genes in the HOXA cluster, in addition to several beta-2 integrins. [provided by RefSeq, Jan 2013]

**Accessions** — [HGNC:37117](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37117) · Entrez [100506311](https://www.ncbi.nlm.nih.gov/gene/100506311) · Ensembl [ENSG00000233429](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233429)

## Data

Gene col 13902: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13902); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13902, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13902]; `tensor/DDL_lfc|DDL_z.npy` [13902]; `embed/gene_vectors.npy` [13902]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13902 or target_col == 13902). Every well: [[HOTAIRM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOTAIRM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
