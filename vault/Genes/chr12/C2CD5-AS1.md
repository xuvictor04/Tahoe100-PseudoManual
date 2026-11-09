---
symbol: "C2CD5-AS1"
type: "gene"
col: 14671
ensembl_id: "ENSG00000250166"
name: "C2CD5 antisense RNA 1"
location: "12p12.1"
module: 21
arm: "+"
pooled_cpm: 4.89
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# C2CD5-AS1

*C2CD5 antisense RNA 1* — 12p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.57× (z +15.5, q 0e+00, up in 38 of 42 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (NCI-H460 0.117×); [[Sunitinib (drug)]] 0.5 µM in 1 line (HT-29 0.0586×); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (A-427 0.0936×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHMP3-AS1]] (+0.88, fdr 7e-06), [[CTDSPL2-DT]] (+0.84, fdr 7e-06), [[ST7-AS2]] (+0.84, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14671.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.57×** | +15.5 | 0e+00 | 38/42 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.02×** | +12.8 | 6e-35 | 20/25 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.47×** | +9.7 | 7e-20 | 8/13 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +9.3 | 1e-18 | 8/9 (HOP62, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.72×** | +6.3 | 3e-08 | 24/44 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.59×** | +5.4 | 7e-06 | 12/33 (NCI-H2347, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +4.9 | 9e-05 | 10/40 (HCT15, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +4.8 | 9e-05 | 11/39 (A-172, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.007 | 9/36 (C32, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.2 | 0.072 | 4/32 (Panc 03.27, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.0 | 0.13 | 12/47 (SW480, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14671.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (NCI-H460 0.117×); [[Sunitinib (drug)]] 0.5 µM in 1 line (HT-29 0.0586×); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (A-427 0.0936×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.868× | -5.9 | 3e-06 | 20/48 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.750× | -3.3 | 0.25 | 10/46 (SNU-1, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14671. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 5.16 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0936× (z -9.1) |
| [[A549 (line)]] | wt | 5.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 4.69 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.50× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 4.51 | 0 | 1 | — | [[Sunitinib (drug)]] 0.5 µM 0.0586× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 4.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.54× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 7.01 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0901× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 4.30 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.117× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 4.97 | 0 | 1 | — | [[Resveratrol (drug)]] 0.5 µM 0.0693× (z -8.7) |
| [[SW480 (line)]] | alt | 7.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +12.9) | — |
| [[A-172 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14671), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP3-AS1]] | +0.88 | +0.72 / +0.85 | both halves | 7e-06 | same gene group |
| [[CTDSPL2-DT]] | +0.84 | +0.72 / +0.81 | both halves | 7e-06 |  |
| [[ST7-AS2]] | +0.84 | +0.72 / +0.83 | both halves | 7e-06 | same gene group |
| [[SPATA21]] | +0.84 | +0.70 / +0.81 | both halves | 7e-06 |  |
| [[TICAM2-AS1]] | +0.84 | +0.74 / +0.82 | both halves | 7e-06 | same gene group |
| [[ZRANB2-AS1]] | +0.83 | +0.80 / +0.78 | both halves | 7e-06 | same gene group |
| [[HSPA2-AS1]] | +0.83 | +0.78 / +0.77 | both halves | 7e-06 | same gene group |
| [[UBOX5-AS1]] | +0.83 | +0.63 / +0.80 | both halves | 7e-06 | same gene group |
| [[ZNF451-AS1]] | +0.83 | +0.74 / +0.74 | both halves | 7e-06 | same gene group |
| [[HRG-AS1]] | +0.83 | +0.73 / +0.80 | both halves | 7e-06 | same gene group |
| [[GEMIN7-AS1]] | +0.82 | +0.68 / +0.82 | both halves | 7e-06 | same gene group |
| [[LANCL1-AS1]] | +0.82 | +0.81 / +0.73 | both halves | 7e-06 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers C2CD5-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HOXD11]] | B | HOXD11 activity raises C2CD5-AS1's level | lines that do not express HOXD11 (36) vs lines expressing it (14) | 1.09× lower at baseline in the lines without HOXD11 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HOXD10, TMEM52B, OLR1 |
| [[CLVS1]] | C | CLVS1's natural level weakens C2CD5-AS1's drug response | CLVS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.71, reverse +0.22; direction clear | 0.009 | ⚠ tissue can mimic it; precision caveat |
| [[PTPRT]] | C | PTPRT's natural level weakens C2CD5-AS1's drug response | PTPRT's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.69, reverse +0.22; direction clear | 0.015 | ⚠ tissue can mimic it; precision caveat |
| [[CCDC39]] | C | CCDC39's natural level weakens C2CD5-AS1's drug response | CCDC39's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68, reverse +0.06; direction not clear | 0.023 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[CNTNAP5]] | C | CNTNAP5's natural level weakens C2CD5-AS1's drug response | CNTNAP5's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.67, reverse +0.04; direction clear | 0.026 | ⚠ tissue can mimic it; precision caveat |
| [[GRM7]] | C | GRM7's natural level weakens C2CD5-AS1's drug response | GRM7's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.63, reverse +0.12; direction clear | 0.069 | ⚠ tissue can mimic it; precision caveat |
| [[CHRM5]] | C | CHRM5's natural level weakens C2CD5-AS1's drug response | CHRM5's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.12; direction clear | 0.090 | ⚠ tissue can mimic it; precision caveat |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.927). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.1, 27.1); signed map (33.4, 4.7). **Vector** length 50.4, 6.07% of its response variance represented; |z| ≥ 3 in 864 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +15.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +12.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.3 | +1.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -1.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -5.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -0.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.0 | -0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | C2CD5 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12p12.1 — chr12:22,409,237-22,618,868 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55961](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55961) · Entrez [105369692](https://www.ncbi.nlm.nih.gov/gene/105369692) · Ensembl [ENSG00000250166](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250166)

## Data

Gene col 14671: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14671); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14671, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14671]; `tensor/DDL_lfc|DDL_z.npy` [14671]; `embed/gene_vectors.npy` [14671]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14671 or target_col == 14671). Every well: [[C2CD5-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C2CD5-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
