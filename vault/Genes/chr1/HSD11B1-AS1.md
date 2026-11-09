---
symbol: "HSD11B1-AS1"
type: "gene"
col: 13601
ensembl_id: "ENSG00000227591"
name: "HSD11B1 antisense RNA 1"
location: "1q32.2"
module: 75
arm: "+"
pooled_cpm: 2.71
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# HSD11B1-AS1

*HSD11B1 antisense RNA 1* — 1q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.67× (z +19.7, q 0e+00, up in 27 of 28 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (RKO 0.132×); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.171×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.0896×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC8C-DT]] (+0.77, fdr 7e-06), [[NPHS1]] (+0.75, fdr 7e-06), [[THSD7B]] (+0.73, fdr 7e-06).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[IL32]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13601.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.67×** | +19.7 | 0e+00 | 27/28 (A498, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.49×** | +16.0 | 0e+00 | 25/32 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.65×** | +8.8 | 3e-16 | 7/14 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.73×** | +8.7 | 4e-16 | 2/5 (HOP62, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.35×** | +7.7 | 1e-12 | 22/33 (LoVo, Panc 03.27, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +7.6 | 3e-12 | 24/42 (A498, Hs 766T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.46×** | +7.3 | 3e-11 | 5/6 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.14×** | +6.9 | 4e-10 | 12/31 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +6.0 | 1e-07 | 9/29 (LS 180, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +6.0 | 1e-07 | 8/16 (NCI-H2347, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.76×** | +5.1 | 2e-05 | 10/40 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +5.0 | 2e-05 | 4/42 (Panc 03.27, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +4.7 | 1e-04 | 12/33 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +4.7 | 1e-04 | 11/25 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +4.6 | 2e-04 | 4/21 (NCI-H2347, A498, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.009 | 6/41 (A498, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.066 | 8/44 (C32, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +3.0 | 0.066 | 9/29 (A549, MIA PaCa-2, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.40×** | +3.0 | 0.066 | 3/36 (BT-474, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (RKO 0.132×); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.171×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.0896×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13601. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 13.5 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.132× (z -11.3) |
| [[A498 (line)]] | wt | 4.71 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.0989× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 6.77 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 5.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.27× (z +8.9) | — |
| [[LoVo (line)]] | wt | 1.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.8× (z +13.6) | — |
| [[Panc 03.27 (line)]] | alt | 9.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +9.7) | — |
| [[A-172 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.999 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.988 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.798 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.859 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.954 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.867 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13601), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC8C-DT]] | +0.77 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[NPHS1]] | +0.75 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[THSD7B]] | +0.73 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[CCDC73]] | +0.73 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[RBMS3-AS3]] | +0.72 | +0.72 / +0.61 | both halves | 7e-06 | same gene group |
| [[COL28A1]] | +0.72 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.72 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[FEZ1]] | +0.71 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[XKR4]] | +0.71 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.71 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[UPK2]] | +0.70 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[GRIA4]] | +0.70 | +0.61 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL32]] | B | IL32 activity raises HSD11B1-AS1's level | lines that do not express IL32 (18) vs lines expressing it (32) | 1.65× lower at baseline in the lines without IL32 | 0.006 | ⚠ within organs, on part of the lines; also absent: PODXL, APOL1, F3 |
| [[ENKUR]] | B | ENKUR activity raises HSD11B1-AS1's level | lines that do not express ENKUR (20) vs lines expressing it (30) | 1.54× lower at baseline in the lines without ENKUR | 0.018 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers HSD11B1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02605]] | B | LINC02605 activity raises HSD11B1-AS1's level | lines that do not express LINC02605 (15) vs lines expressing it (35) | 1.56× lower at baseline in the lines without LINC02605 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000285744, FAR2, ENSG00000285517 |
| [[EDIL3-DT]] | B | EDIL3-DT activity raises HSD11B1-AS1's level | lines that do not express EDIL3-DT (25) vs lines expressing it (25) | 1.33× lower at baseline in the lines without EDIL3-DT | 0.096 | ⚠ within organs, on part of the lines; also absent: EDIL3, NALCN, DTNA |
| [[CD40]] | B | CD40 activity raises HSD11B1-AS1's level | lines that do not express CD40 (22) vs lines expressing it (28) | 1.50× lower at baseline in the lines without CD40 | 0.097 | ⚠ within organs, on part of the lines; also absent: ZNF528-AS1, TNFRSF9, TMEM156 |
| [[TTN]] | C | TTN's natural level weakens HSD11B1-AS1's drug response | TTN's natural level across 38 lines (lineage-adjusted; a glimpse) | r -0.72, reverse -0.47; direction clear | 0.063 | ⚠ tissue can mimic it; precision caveat |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.773). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.9, 23.4); signed map (37.7, 10.3). **Vector** length 51.8, 7.11% of its response variance represented; |z| ≥ 3 in 966 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +19.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +16.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +1.7 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +1.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -0.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.3 | -0.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | HSD11B1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q32.2 — chr1:209,661,356-209,724,125 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54053](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54053) · Entrez [101930114](https://www.ncbi.nlm.nih.gov/gene/101930114) · Ensembl [ENSG00000227591](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227591)

## Data

Gene col 13601: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13601); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13601, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13601]; `tensor/DDL_lfc|DDL_z.npy` [13601]; `embed/gene_vectors.npy` [13601]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13601 or target_col == 13601). Every well: [[HSD11B1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSD11B1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
