---
symbol: "SASS6"
type: "gene"
col: 8023
ensembl_id: "ENSG00000156876"
name: "SAS-6 centriolar assembly protein"
location: "1p21.2"
module: 71
arm: "+"
pooled_cpm: 38.74
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# SASS6

*SAS-6 centriolar assembly protein* — 1p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.71× (z +8.5, q 1e-14, up in 35 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Pasireotide (acetate) (drug)]] 5 µM: 1.16× (z +3.3, q 0.092, up in 8 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (KATO III 3.30×, LS 180 3.76×; ⚠ cell-cycle shift, explains ~28% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (KATO III 3.01×, LoVo 2.84×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A549 2.94×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.595× (z -8.2, q 1e-13, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTBP]] (+0.75, fdr 7e-06), [[LIN9]] (+0.74, fdr 7e-06), [[FANCM]] (+0.72, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF736]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8023.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (KATO III 3.30×, LS 180 3.76×; ⚠ cell-cycle shift, explains ~28% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (KATO III 3.01×, LoVo 2.84×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A549 2.94×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.71×** | +8.5 | 1e-14 | 35/48 (KATO III, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.70×** | +8.3 | 3e-14 | 36/47 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.25×** | +3.5 | 0.091 | 19/48 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.24×** | +3.3 | 0.092 | 11/48 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.092 | 8/48 (HT-29, J82, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.092 | 6/48 (HEC-1-A, NCI-H2030, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.092 | 13/47 (NCI-H1573, HT-29, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +3.2 | 0.10 | 19/48 (RKO, NCI-H1792, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | 1.45× | +3.1 | 0.14 | 13/47 (SW48, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8023.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.595×** | -8.2 | 1e-13 | 33/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.602×** | -7.7 | 4e-12 | 26/39 (NCI-H460, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.680×** | -6.1 | 2e-07 | 27/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.763×** | -6.0 | 2e-07 | 28/48 (SW480, A-172, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.915× | -5.0 | 8e-05 | 5/48 (RKO, COLO 205, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.727×** | -4.4 | 9e-04 | 21/47 (HOP62, HEC-1-A, …) | two highest doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.743×** | -4.3 | 0.001 | 21/43 (C-33 A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.827×** | -4.3 | 0.002 | 20/48 (H4, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.772×** | -4.1 | 0.003 | 21/48 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.783×** | -3.9 | 0.006 | 23/48 (NCI-H2347, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.763×** | -3.8 | 0.008 | 20/44 (SW48, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.789×** | -3.8 | 0.008 | 17/48 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.797×** | -3.6 | 0.014 | 14/48 (NCI-H1573, Panc 03.27, …) | top dose only |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.818×** | -3.2 | 0.060 | 13/48 (SW 1088, PANC-1, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 5 µM |  | **0.821×** | -3.1 | 0.063 | 6/48 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.821×** | -3.1 | 0.063 | 10/48 (RKO, RPMI-7951, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.873× | -3.1 | 0.076 | 13/48 (NCI-H661, Panc 03.27, …) | rises with dose |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **0.827×** | -3.0 | 0.081 | 4/48 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.829×** | -3.0 | 0.086 | 10/48 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.832×** | -2.9 | 0.097 | 11/48 (HOP62, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8023. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 28.0 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.183× (z -16.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.355× (z -10.2) |
| [[A498 (line)]] | wt | 43.2 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.395× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 35.1 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.30× (z +9.4) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2347 (line)]] | alt | 47.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.385× (z -9.7) |
| [[A-172 (line)]] | wt | 29.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -9.8) |
| [[A549 (line)]] | wt | 25.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C-33 A (line)]] | alt | 47.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -11.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 25.7 | 0 | 1 | — | [[Futibatinib (drug)]] 5 µM 0.0518× (z -9.2) |
| [[H4 (line)]] | wt | 38.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -13.5) |
| [[HCT15 (line)]] | alt | 72.3 | 0 | 1 | — | [[IQ 1 (drug)]] 5 µM 0.0771× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 68.0 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0849× (z -15.1) ⚠ toxic |
| [[LoVo (line)]] | wt | 34.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.84× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LS 180 (line)]] | wt | 36.8 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.76× (z +9.2) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H460 (line)]] | wt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -11.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 59.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.354× (z -8.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 72.6 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.122× (z -9.9) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 40.1 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 43.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -10.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 52.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8023), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTBP]] | +0.75 | +0.70 / +0.80 | both halves | 7e-06 |  |
| [[LIN9]] | +0.74 | +0.72 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[FANCM]] | +0.72 | +0.61 / +0.76 | both halves | 7e-06 | STRING 488 |
| [[SLF1]] | +0.71 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[PPIH]] | +0.69 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[CTDSPL2]] | +0.67 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[ZNF684]] | +0.67 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[CEP152]] | +0.66 | +0.61 / +0.73 | both halves | 7e-06 | STRING 975 |
| [[MTF2]] | +0.66 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[C1orf112]] | +0.66 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[OIP5]] | +0.65 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[MIS18BP1]] | +0.65 | +0.70 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF736]] | B | ZNF736 activity raises SASS6's level | lines that do not express ZNF736 (19) vs lines expressing it (31) | 1.27× lower at baseline in the lines without ZNF736 | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000176593, C19orf18, IQCA1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.659). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.8, -49.6); signed map (-43.4, -35.9). **Vector** length 105, 27.8% of its response variance represented; |z| ≥ 3 in 797 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +4.9 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.5 | +0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +0.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.8 | +0.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.6 | +0.9 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.3 | +2.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -6.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.2 | -4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.0 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | -2.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -0.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.3 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | +1.9 |

## What is on record

|  |  |
|---|---|
| Name | SAS-6 centriolar assembly protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.2 — chr1:100,083,563-100,132,955 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761A078, SAS-6, FLJ22097, SAS6 |
| Hallmark sets | MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UVJ0](https://www.uniprot.org/uniprotkb/Q6UVJ0) (Spindle assembly abnormal protein 6 homolog):

> Central scaffolding component of the centrioles ensuring their 9-fold symmetry (By similarity). Required for centrosome biogenesis and duplication: required both for mother-centriole-dependent centriole duplication and deuterosome-dependent centriole amplification in multiciliated cells. Not required for centriole formation in embryonic stem cells but necessary to maintain centriole architecture (By similarity). Required for the recruitment of STIL to the procentriole and for STIL-mediated …

**Summary**, from NCBI Gene [163786](https://www.ncbi.nlm.nih.gov/gene/163786):

> The protein encoded by this gene is a central component of centrioles and is necessary for their duplication and function. Centrioles adopt a cartwheel-shaped structure, with the encoded protein forming the hub and spokes inside a microtubule cylinder. Defects in this gene are a cause of autosomal recessive primary microcephaly. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:25403](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25403) · Entrez [163786](https://www.ncbi.nlm.nih.gov/gene/163786) · UniProt [Q6UVJ0](https://www.uniprot.org/uniprotkb/Q6UVJ0) · Ensembl [ENSG00000156876](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156876)

## Data

Gene col 8023: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8023); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8023, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8023]; `tensor/DDL_lfc|DDL_z.npy` [8023]; `embed/gene_vectors.npy` [8023]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8023 or target_col == 8023). Every well: [[SASS6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SASS6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
