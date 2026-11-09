---
symbol: "INKA2"
type: "gene"
col: 12475
ensembl_id: "ENSG00000197852"
name: "inka box actin regulator 2"
location: "1p13.2"
module: 62
arm: "+"
pooled_cpm: 5.71
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# INKA2

*inka box actin regulator 2* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.02× (z +22.8, q 0e+00, up in 40 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Simotinib (drug)]] 5 µM in 1 line (A498 0.0889×; ⚠ toxic); [[Tadalafil (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0857×); [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.103×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.110×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF423]] (+0.74, fdr 7e-06), [[SPATA18]] (+0.69, fdr 7e-06), [[GRIN2C]] (+0.69, fdr 7e-06).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12475.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.02×** | +22.8 | 0e+00 | 40/43 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.16×** | +11.2 | 9e-27 | 19/28 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.65×** | +10.4 | 6e-23 | 24/41 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +9.7 | 7e-20 | 19/41 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +9.5 | 2e-19 | 5/11 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.89×** | +9.2 | 2e-18 | 29/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +9.1 | 6e-18 | 27/42 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +7.7 | 1e-12 | 24/45 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +7.6 | 2e-12 | 22/47 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +7.3 | 2e-11 | 7/17 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +7.0 | 1e-10 | 19/40 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +6.5 | 3e-09 | 9/31 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.32×** | +5.6 | 7e-07 | 10/47 (H4, LoVo, …) | top dose only | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +5.6 | 7e-07 | 12/45 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.6 | 9e-07 | 18/47 (SW48, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +5.5 | 1e-06 | 13/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +5.1 | 9e-06 | 14/45 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +4.5 | 2e-04 | 10/46 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.18× | +3.4 | 0.019 | 8/47 (RKO, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.020 | 11/43 (SW48, J82, …) | rises with dose | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12475.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Simotinib (drug)]] 5 µM in 1 line (A498 0.0889×; ⚠ toxic); [[Tadalafil (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0857×); [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.103×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.110×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Arbutin (drug)]] 5 µM |  | 0.779× | -3.5 | 0.23 | 5/45 (Hs 766T, SW480, …) | top dose only |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.800× | -3.2 | 0.46 | 2/46 (NCI-H2347, C-33 A) | rises with dose | plate-row cell shift |
| [[Mebendazole (drug)]] 5 µM |  | 0.808× | -3.0 | 0.49 | 4/46 (SW 1088, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12475. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 4.11 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.81× (z +13.5) | — |
| [[A498 (line)]] | wt | 4.48 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.02× (z +14.0) | [[Simotinib (drug)]] 5 µM 0.0889× (z -11.1) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.17× (z +8.9) | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.110× (z -8.5) |
| [[A549 (line)]] | wt | 4.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.09× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 3.33 | 0 | 1 | — | [[Tadalafil (drug)]] 0.05 µM 0.0857× (z -8.9) |
| [[LoVo (line)]] | wt | 11.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +11.5) | — |
| [[LOX-IMVI (line)]] | wt | 3.76 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0906× (z -8.5) |
| [[LS 180 (line)]] | wt | 6.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 4.16 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.103× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 8.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +8.7) | — |
| [[RKO (line)]] | wt | 7.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.66× (z +11.3) | — |
| [[SW480 (line)]] | alt | 6.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +11.2) | — |
| [[A-172 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12475), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF423]] | +0.74 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[SPATA18]] | +0.69 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[GRIN2C]] | +0.69 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[DNAI3]] | +0.68 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.68 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[TYMSOS]] | +0.66 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[MIR3659HG]] | +0.65 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[ACTA2]] | +0.65 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[ZNF561-AS1]] | +0.65 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[ZNF451-AS1]] | +0.64 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[SPATA21]] | +0.63 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[PINCR]] | +0.63 | +0.50 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers INKA2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PINCR]] | B | PINCR activity strengthens INKA2's drug response | lines that do not express PINCR (29) vs lines expressing it (19) | the lines without PINCR respond 0.78× as strongly (z diff +0.44); strongest at Idarubicin (hydrochloride) 5 µM: 2.30x vs 4.28x (z diff +3.3) | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[GRIN2C]] | B | GRIN2C activity raises INKA2's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 1.28× lower at baseline in the lines without GRIN2C | 0.088 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[EDA2R]] | B | EDA2R activity raises INKA2's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.08× lower at baseline in the lines without EDA2R | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.739). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.6, 36.9); signed map (43.5, -23.3). **Vector** length 50.6, 5.86% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *p53 targets up* (control, mean cos +0.51 to 26); *apoptosis* (hallmark, mean cos +0.54 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +22.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +9.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.4 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +5.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.4 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +3.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -1.5 | +7.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.2 | +7.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +1.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.0 | +9.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -3.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | +0.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -0.8 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | inka box actin regulator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:111,680,630-111,755,824 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31105; previously C1orf183, FAM212B |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NTI7](https://www.uniprot.org/uniprotkb/Q9NTI7) (PAK4-inhibitor INKA2):

> Inhibitor of the serine/threonine-protein kinase PAK4. Acts by binding PAK4 in a substrate-like manner, inhibiting the protein kinase activity.

**Summary**, from NCBI Gene [55924](https://www.ncbi.nlm.nih.gov/gene/55924):

> Enables protein kinase binding activity. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28045](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28045) · Entrez [55924](https://www.ncbi.nlm.nih.gov/gene/55924) · UniProt [Q9NTI7](https://www.uniprot.org/uniprotkb/Q9NTI7) · Ensembl [ENSG00000197852](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197852)

## Data

Gene col 12475: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12475); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12475, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12475]; `tensor/DDL_lfc|DDL_z.npy` [12475]; `embed/gene_vectors.npy` [12475]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12475 or target_col == 12475). Every well: [[INKA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INKA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
