---
symbol: "ISCU"
type: "gene"
col: 5798
ensembl_id: "ENSG00000136003"
name: "iron-sulfur cluster assembly enzyme"
location: "12q23.3"
module: 62
arm: "+"
pooled_cpm: 26.62
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# ISCU

*iron-sulfur cluster assembly enzyme* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.97× (z +9.4, q 5e-18, up in 41 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.284×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFT20]] (+0.68, fdr 7e-06), [[TP53INP1]] (+0.68, fdr 7e-06), [[RPS27L]] (+0.68, fdr 1e-05); moves opposite to [[DNMT1]] (-0.58, fdr 3e-05), [[NAA15]] (-0.57, fdr 4e-05), [[DHX9]] (-0.57, fdr 3e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5798.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +9.4 | 5e-18 | 41/48 (A549, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.15×** | +8.0 | 5e-13 | 43/46 (LOX-IMVI, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.92×** | +7.1 | 3e-10 | 34/43 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.72×** | +5.9 | 6e-07 | 34/46 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.69×** | +5.5 | 5e-06 | 24/34 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +5.0 | 7e-05 | 26/48 (NCI-H460, LOX-IMVI, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +4.6 | 3e-04 | 29/48 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.1 | 0.003 | 20/48 (NCI-H460, A549, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.40×** | +3.4 | 0.040 | 16/40 (HS-578T, NCI-H2030, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.37×** | +3.4 | 0.040 | 21/48 (J82, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.64×** | +3.3 | 0.048 | 18/46 (NCI-H460, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.2 | 0.055 | 18/47 (SW1417, NCI-H2030, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.055 | 22/47 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.055 | 18/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.60×** | +3.2 | 0.055 | 14/45 (SHP-77, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.60×** | +3.2 | 0.055 | 18/48 (NCI-H2347, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.58×** | +3.1 | 0.068 | 15/48 (SW1417, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5798.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.284×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.717× | -3.6 | 0.18 | 22/48 (A498, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5798. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 41.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 27.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +8.8) | — |
| [[A-172 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5798), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT20]] | +0.68 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[TP53INP1]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[RPS27L]] | +0.68 | +0.55 / +0.74 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[ANKRA2]] | +0.68 | +0.56 / +0.73 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[CDC37L1]] | +0.63 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[YPEL3]] | +0.63 | +0.57 / +0.74 | both halves | 1e-05 |  |
| [[ZFPL1]] | +0.62 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[ATXN3]] | +0.62 | +0.44 / +0.69 | both halves | 3e-05 |  |
| [[COX7A2L]] | +0.62 | +0.68 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[GDF15]] | +0.61 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[RFNG]] | +0.61 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[FDXR]] | +0.61 | +0.51 / +0.64 | both halves | 1e-05 | same gene group; pathway: HALLMARK_P53_PATHWAY; STRING 726 |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNMT1]] | -0.58 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[NAA15]] | -0.57 | -0.41 / -0.65 | both halves | 4e-05 |  |
| [[DHX9]] | -0.57 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[SERBP1]] | -0.56 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[PRKDC]] | -0.55 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[HNRNPA2B1]] | -0.55 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[G3BP1]] | -0.54 | -0.40 / -0.56 | both halves | 5e-05 | pathway: SARS-CoV-2 Infection |
| [[YWHAE]] | -0.54 | -0.50 / -0.59 | both halves | 1e-05 | pathway: SARS-CoV-2 Infection |
| [[CHML]] | -0.54 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[NUP188]] | -0.54 | -0.43 / -0.60 | both halves | 3e-05 | pathway: SARS-CoV-2 Infection |
| [[C1QBP]] | -0.53 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[TAF1B]] | -0.53 | -0.43 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ISCU's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PINCR]] | B | PINCR activity strengthens ISCU's drug response | lines that do not express PINCR (29) vs lines expressing it (19) | the lines without PINCR respond 0.80× as strongly (z diff +0.57); strongest at Mitoxantrone (dihydrochloride) 5 µM: 1.22x vs 1.50x (z diff +1.6) | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[C1QBP]] | C | C1QBP's natural level strengthens ISCU's drug response | C1QBP's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67, reverse -0.22; direction not clear | 0.033 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TP53]] | C | TP53 activity strengthens ISCU's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 0.78× as strongly (z diff +0.69); strongest at Selinexor 5 µM: 1.26x vs 1.66x (z diff +1.8) | 0.907 over the table, 0.084 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.575). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (1.1, -50.5); signed map (-14.1, 5.2). **Vector** length 82.1, 22.1% of its response variance represented; |z| ≥ 3 in 563 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.9 | +3.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.4 | +8.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +2.2 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +2.1 | +0.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | +3.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -3.0 | +5.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.8 | -1.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -2.7 | +3.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | iron-sulfur cluster assembly enzyme |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:108,562,582-108,569,368 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ISU2, hnifU; previously NIFUN |
| Gene groups (HGNC) | Mitochondrial iron-sulfur assembly components |
| Hallmark sets | COAGULATION, P53_PATHWAY, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 11 pathways, smallest: Mitochondrial iron-sulfur cluster biogenesis; Translation of Replicase and Assembly of the Replication Transcription Complex_9694676; Maturation of TCA enzymes and regulation of TCA cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1K1](https://www.uniprot.org/uniprotkb/Q9H1K1) (Iron-sulfur cluster assembly enzyme ISCU):

> [Isoform 1]: Mitochondrial scaffold protein, of the core iron-sulfur cluster (ISC) assembly complex, that provides the structural architecture on which the [2Fe-2S] clusters are assembled. The core iron-sulfur cluster (ISC) assembly complex is involved in the de novo synthesis of a [2Fe-2S] cluster, the first step of the mitochondrial iron-sulfur protein biogenesis. This process is initiated by the cysteine desulfurase complex (NFS1:LYRM4:NDUFAB1) that produces persulfide which is delivered on …

**Summary**, from NCBI Gene [23479](https://www.ncbi.nlm.nih.gov/gene/23479):

> This gene encodes a component of the iron-sulfur (Fe-S) cluster scaffold. Fe-S clusters are cofactors that play a role in the function of a diverse set of enzymes, including those that regulate metabolism, iron homeostasis, and oxidative stress response. Alternative splicing results in transcript variants encoding different protein isoforms that localize either to the cytosol or to the mitochondrion. Mutations in this gene have been found in patients with hereditary myopathy with lactic …

**Accessions** — [HGNC:29882](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29882) · Entrez [23479](https://www.ncbi.nlm.nih.gov/gene/23479) · UniProt [Q9H1K1](https://www.uniprot.org/uniprotkb/Q9H1K1) · Ensembl [ENSG00000136003](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136003)

## Data

Gene col 5798: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5798); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5798, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5798]; `tensor/DDL_lfc|DDL_z.npy` [5798]; `embed/gene_vectors.npy` [5798]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5798 or target_col == 5798). Every well: [[ISCU — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ISCU.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
