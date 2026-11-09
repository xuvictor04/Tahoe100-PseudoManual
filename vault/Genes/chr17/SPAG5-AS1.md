---
symbol: "SPAG5-AS1"
type: "gene"
col: 13599
ensembl_id: "ENSG00000227543"
name: "SPAG5 antisense RNA 1"
location: "17q11.2"
module: 21
arm: "+"
pooled_cpm: 5.83
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# SPAG5-AS1

*SPAG5 antisense RNA 1* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.96× (z +23.8, q 0e+00, up in 38 of 39 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Temsirolimus (drug)]] 0.5 µM in 1 line (SW1417 0.0650×); [[Elagolix sodium (drug)]] 0.05 µM in 1 line (Hs 766T 0.0667×); [[Pimozide (drug)]] 0.5 µM in 1 line (HT-29 0.0912×; ⚠ transcription drop); [[Flumatinib (mesylate) (drug)]] 0.05 µM in 1 line (Panc 03.27 0.0605×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP34-DT]] (+0.75, fdr 7e-06), [[LMNB1-DT]] (+0.73, fdr 7e-06), [[MYH11]] (+0.73, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[VWA1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13599.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.96×** | +23.8 | 0e+00 | 38/39 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.40×** | +15.1 | 0e+00 | 30/40 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.79×** | +12.5 | 1e-33 | 22/27 (SW 900, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.49×** | +10.7 | 2e-24 | 8/10 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.34×** | +9.6 | 1e-19 | 15/18 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +6.8 | 9e-10 | 19/39 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +4.8 | 1e-04 | 15/38 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +4.5 | 5e-04 | 12/44 (NCI-H2347, SW1417, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.2 | 0.002 | 13/38 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.003 | 11/44 (A-172, RKO, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.052 | 10/45 (CFPAC-1, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.074 | 8/47 (KATO III, PANC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13599.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Temsirolimus (drug)]] 0.5 µM in 1 line (SW1417 0.0650×); [[Elagolix sodium (drug)]] 0.05 µM in 1 line (Hs 766T 0.0667×); [[Pimozide (drug)]] 0.5 µM in 1 line (HT-29 0.0912×; ⚠ transcription drop); [[Flumatinib (mesylate) (drug)]] 0.05 µM in 1 line (Panc 03.27 0.0605×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -4.3 | 0.012 | 9/48 (NCI-H1792, NCI-H2030, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.764× | -3.3 | 0.27 | 2/48 (COLO 205, RPMI-7951) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.780× | -3.0 | 0.43 | 8/46 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13599. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 7.57 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +10.4) | — |
| [[HOP62 (line)]] | alt | 8.42 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.38× (z +15.0) | — |
| [[NCI-H1573 (line)]] | alt | 7.65 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +10.1) | — |
| [[A498 (line)]] | wt | 4.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +10.7) | — |
| [[A549 (line)]] | wt | 5.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 4.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +10.6) | — |
| [[Hs 766T (line)]] | wt | 4.94 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.05 µM 0.0667× (z -9.1) |
| [[HT-29 (line)]] | alt | 4.64 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0912× (z -9.0) ⚠ transcription drop |
| [[KATO III (line)]] | alt | 5.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.35× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 8.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 11.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +12.5) | — |
| [[Panc 03.27 (line)]] | alt | 4.19 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 0.05 µM 0.0605× (z -8.9) |
| [[PANC-1 (line)]] | alt | 5.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +11.5) | — |
| [[SHP-77 (line)]] | alt | 5.86 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0790× (z -8.8) |
| [[SW1417 (line)]] | alt | 5.60 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0650× (z -9.1) |
| [[SW480 (line)]] | alt | 4.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +11.0) | — |
| [[A-427 (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13599), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP34-DT]] | +0.75 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[LMNB1-DT]] | +0.73 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[MYH11]] | +0.73 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[PKD2L2]] | +0.71 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[LINC02608]] | +0.71 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[LCA5L]] | +0.68 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[AADACL2-AS1]] | +0.67 | +0.41 / +0.68 | both halves | 4e-05 | same gene group |
| [[PSMD14-DT]] | +0.66 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[HRG-AS1]] | +0.66 | +0.46 / +0.66 | both halves | 3e-05 | same gene group |
| [[DNAJC9-AS1-1]] | +0.65 | +0.48 / +0.62 | both halves | 2e-05 | same gene group |
| [[CTDSPL2-DT]] | +0.65 | +0.54 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VWA1]] | B | VWA1 activity lowers SPAG5-AS1's level | lines that do not express VWA1 (10) vs lines expressing it (40) | 1.14× higher at baseline in the lines without VWA1 | 0.024 | ⚠ within organs, on part of the lines; also absent: ATAD3C, KLC3, GPRC5C |
| [[LINC02934]] | B | LINC02934 activity lowers SPAG5-AS1's level | lines that do not express LINC02934 (8) vs lines expressing it (42) | 1.04× higher at baseline in the lines without LINC02934 | 0.025 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SPAG5-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[RABGEF1P3]] | B | RABGEF1P3 activity raises SPAG5-AS1's level | lines that do not express RABGEF1P3 (5) vs lines expressing it (45) | 1.26× lower at baseline in the lines without RABGEF1P3 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC2A1, PHLDA2, SHB; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.668). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.4, 24.9); signed map (31.3, 3.7). **Vector** length 63.9, 9.77% of its response variance represented; |z| ≥ 3 in 843 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +23.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +9.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +15.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +2.2 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +2.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.9 | +3.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -2.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | SPAG5 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q11.2 — chr17:28,598,790-28,617,377 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41140](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41140) · Entrez [100506436](https://www.ncbi.nlm.nih.gov/gene/100506436) · Ensembl [ENSG00000227543](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227543)

## Data

Gene col 13599: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13599); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13599, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13599]; `tensor/DDL_lfc|DDL_z.npy` [13599]; `embed/gene_vectors.npy` [13599]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13599 or target_col == 13599). Every well: [[SPAG5-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPAG5-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
