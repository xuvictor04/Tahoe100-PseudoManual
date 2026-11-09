---
symbol: "GPX1"
type: "gene"
col: 13897
ensembl_id: "ENSG00000233276"
name: "glutathione peroxidase 1"
location: "3p21.31"
module: 62
arm: "+"
pooled_cpm: 37.72
n_lines_expressing: 46
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 1
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# GPX1

*glutathione peroxidase 1* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.10× (z +9.4, q 3e-18, up in 40 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.10× (z +7.0, q 4e-10, up in 39 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (PANC-1 0.132×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.157×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SESN1]] (+0.65, fdr 1e-05), [[PPM1D]] (+0.64, fdr 3e-05), [[CST3]] (+0.63, fdr 3e-05); moves opposite to [[LMCD1-AS1]] (-0.53, fdr 7e-05), [[SUDS3]] (-0.53, fdr 1e-05), [[NUDC]] (-0.51, fdr 9e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[TP53INP1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13897.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **4.10×** | +9.4 | 3e-18 | 40/40 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **3.37×** | +7.8 | 2e-12 | 33/36 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.97×** | +7.0 | 4e-10 | 41/41 (LS 180, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +7.0 | 4e-10 | 39/43 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.60×** | +6.1 | 1e-07 | 40/44 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +5.4 | 6e-06 | 40/43 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.30×** | +5.1 | 2e-05 | 34/37 (LoVo, HT-29, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.71×** | +5.0 | 4e-05 | 37/44 (A549, A-172, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.98×** | +4.5 | 4e-04 | 37/42 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.74×** | +3.7 | 0.013 | 29/43 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **1.65×** | +3.3 | 0.043 | 28/43 (SW480, LoVo, …) | top dose only | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.40×** | +3.1 | 0.084 | 30/44 (A-427, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13897.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (PANC-1 0.132×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.157×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.608× | -3.1 | 0.64 | 22/44 (LS 180, HT-29, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.594× | -3.0 | 0.64 | 24/44 (SK-MEL-2, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13897. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 51.5 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +10.1) | — |
| [[NCI-H460 (line)]] | wt | 26.2 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +9.9) | — |
| [[A-172 (line)]] | wt | 38.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +11.9) | — |
| [[LoVo (line)]] | wt | 22.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.14× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[RKO (line)]] | wt | 38.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.67× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +8.7) | — |
| [[A-427 (line)]] | wt | 77.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -15.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 27.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.36× (z +10.9) | — |
| [[C32 (line)]] | wt | 12.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 37.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.48× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HT-29 (line)]] | alt | 28.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.19× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H1792 (line)]] | alt | 30.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.73× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[PANC-1 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.132× (z -16.4) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 38.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.09× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[A498 (line)]] | wt | 66.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.80 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13897), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SESN1]] | +0.65 | +0.49 / +0.64 | both halves | 1e-05 | pathway: Cellular response to chemical stress |
| [[PPM1D]] | +0.64 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[CST3]] | +0.63 | +0.44 / +0.71 | both halves | 3e-05 |  |
| [[FAS]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_APOPTOSIS |
| [[DDB2]] | +0.61 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[ACTA2]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[S100A13]] | +0.60 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[ANKRA2]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[FDXR]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_APOPTOSIS |
| [[TAF3]] | +0.59 | +0.38 / +0.63 | both halves | 6e-05 |  |
| [[POLH]] | +0.58 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[GRIN2C]] | +0.58 | +0.54 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMCD1-AS1]] | -0.53 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[SUDS3]] | -0.53 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[NUDC]] | -0.51 | -0.37 / -0.55 | both halves | 9e-05 |  |
| [[FLNC]] | -0.51 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[USP14]] | -0.47 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[EP400]] | -0.47 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[MAP1B]] | -0.46 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[PTGES3]] | -0.46 | -0.40 / -0.50 | both halves | 5e-05 | pathway: Arachidonate metabolism |
| [[CCT3]] | -0.46 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[STIP1]] | -0.45 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[SLC19A1]] | -0.45 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[CCT2]] | -0.45 | -0.22 / -0.48 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GPX1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PINCR]] | B | PINCR activity strengthens GPX1's drug response | lines that do not express PINCR (25) vs lines expressing it (19) | the lines without PINCR respond 0.77× as strongly (z diff +1.11); strongest at Idarubicin (hydrochloride) 0.5 µM: 1.53x vs 2.70x (z diff +2.1) | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[PLCL2]] | B | PLCL2 activity raises GPX1's level | lines that do not express PLCL2 (12) vs lines expressing it (38) | 1.67× lower at baseline in the lines without PLCL2 | 0.096 | ⚠ within organs, on part of the lines |
| [[MDM2]] | C | MDM2's natural level strengthens GPX1's drug response | MDM2's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.68, reverse -0.07; direction not clear | 0.051 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[FDXR]] | C | FDXR's natural level strengthens GPX1's drug response | FDXR's natural level across 38 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.09; direction not clear | 0.062 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[DDB2]] | C | DDB2's natural level strengthens GPX1's drug response | DDB2's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.08; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TP53]] | C | TP53 activity strengthens GPX1's drug response | recorded loss-of-function mutation of TP53 in 27 lines vs 17 not recorded | the TP53-altered lines respond 0.75× as strongly (z diff +1.27); strongest at Idarubicin (hydrochloride) 0.5 µM: 1.51x vs 2.97x (z diff +2.5) | 0.138 over the table, 0.004 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53INP1]] | C | GPX1 activity raises TP53INP1's level | lines that do not express GPX1 (4) vs lines expressing it (46) | 2.22× lower at baseline in the lines without GPX1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FUCA2; its own permutation p |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.659). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.7, 36.2); signed map (41.6, -25.2). **Vector** length 80.3, 27.6% of its response variance represented; |z| ≥ 3 in 698 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +5.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +5.1 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +5.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +7.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.0 | -0.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.6 | -0.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.5 | +1.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.0 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -2.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -0.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.3 | -0.8 |
|  | [[EX229 (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.9 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | glutathione peroxidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,357,174-49,358,605 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Selenoproteins; Glutathione peroxidase family |
| Hallmark sets | APOPTOSIS |
| Reactome | 10 pathways, smallest: Synthesis of 12-eicosatetraenoic acid derivatives; Synthesis of 15-eicosatetraenoic acid derivatives; Synthesis of 5-eicosatetraenoic acids |
| Matched by | ensembl_id |

**Function**, from UniProt [P07203](https://www.uniprot.org/uniprotkb/P07203) (Glutathione peroxidase 1):

> Catalyzes the reduction of hydroperoxides in a glutathione-dependent manner thus regulating cellular redox homeostasis. Can reduce small soluble hydroperoxides such as H2O2, cumene hydroperoxide and tert-butyl hydroperoxide, as well as several fatty acid-derived hydroperoxides. In platelets catalyzes the reduction of 12-hydroperoxyeicosatetraenoic acid, the primary product of the arachidonate 12-lipoxygenase pathway.

**Summary**, from NCBI Gene [2876](https://www.ncbi.nlm.nih.gov/gene/2876):

> The protein encoded by this gene belongs to the glutathione peroxidase family, members of which catalyze the reduction of organic hydroperoxides and hydrogen peroxide (H2O2) by glutathione, and thereby protect cells against oxidative damage. Other studies indicate that H2O2 is also essential for growth-factor mediated signal transduction, mitochondrial function, and maintenance of thiol redox-balance; therefore, by limiting H2O2 accumulation, glutathione peroxidases are also involved in …

**Accessions** — [HGNC:4553](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4553) · Entrez [2876](https://www.ncbi.nlm.nih.gov/gene/2876) · UniProt [P07203](https://www.uniprot.org/uniprotkb/P07203) · Ensembl [ENSG00000233276](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233276)

## Data

Gene col 13897: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13897); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13897, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13897]; `tensor/DDL_lfc|DDL_z.npy` [13897]; `embed/gene_vectors.npy` [13897]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13897 or target_col == 13897). Every well: [[GPX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
