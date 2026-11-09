---
symbol: "TAF5"
type: "gene"
col: 7319
ensembl_id: "ENSG00000148835"
name: "TATA-box binding protein associated factor 5"
location: "10q24.33"
module: 16
arm: "-"
pooled_cpm: 12.21
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# TAF5

*TATA-box binding protein associated factor 5* — 10q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.19× (z +14.2, q 1e-42, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.542× (z -7.8, q 4e-12, down in 23 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.798× (z -4.0, q 0.008, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SNU-423 0.0540×, A-172 0.128×, NCI-H460 0.183×, KATO III 0.159×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H2030 0.0507×, A498 0.103×, SHP-77 0.114×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (HS-578T 0.103×; ⚠ toxic; transcription drop); [[Bendamustine (drug)]] 5 µM in 1 line (BT-474 0.0762×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (Hs 766T 0.109×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NARF]] (+0.70, fdr 7e-06), [[MAP3K3]] (+0.66, fdr 3e-05), [[NDUFA2]] (+0.66, fdr 1e-04); moves opposite to [[ZNF655]] (-0.65, fdr 1e-05), [[GDAP1]] (-0.64, fdr 7e-06), [[DST]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 12 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7319.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +14.2 | 1e-42 | 44/46 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.27×** | +10.5 | 4e-23 | 34/46 (LS 180, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.22×** | +10.2 | 6e-22 | 42/47 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.16×** | +9.8 | 1e-20 | 41/47 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.06×** | +9.2 | 3e-18 | 37/47 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.00×** | +8.8 | 1e-16 | 37/47 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.83×** | +7.4 | 1e-11 | 33/46 (SW48, Panc 03.27, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.62×** | +6.2 | 4e-08 | 27/46 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +6.2 | 4e-08 | 24/48 (SNU-423, Hs 766T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.63×** | +6.0 | 1e-07 | 27/46 (A-427, LS 180, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.51×** | +5.3 | 7e-06 | 26/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.2 | 8e-06 | 23/42 (HEC-1-A, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.39×** | +4.2 | 0.001 | 19/46 (SW48, RKO, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.39×** | +4.2 | 0.001 | 13/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.19× | +3.2 | 0.051 | 12/48 (SW1417, NCI-H460, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.051 | 14/47 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7319.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SNU-423 0.0540×, A-172 0.128×, NCI-H460 0.183×, KATO III 0.159×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H2030 0.0507×, A498 0.103×, SHP-77 0.114×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (HS-578T 0.103×; ⚠ toxic; transcription drop); [[Bendamustine (drug)]] 5 µM in 1 line (BT-474 0.0762×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (Hs 766T 0.109×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.542×** | -7.8 | 4e-12 | 23/38 (SNU-423, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.660×** | -5.1 | 1e-04 | 11/23 (HS-578T, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.699×** | -4.2 | 0.005 | 15/31 (NCI-H2030, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.798×** | -4.0 | 0.008 | 18/48 (A-427, MIA PaCa-2, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.764×** | -3.4 | 0.073 | 16/45 (RPMI-7951, H4, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.830×** | -3.3 | 0.079 | 17/48 (KATO III, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.784× | -3.1 | 0.17 | 4/48 (SW 900, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7319. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 10.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -11.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 8.74 | 0 | 2 (1 ⚠) | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.109× (z -9.4) |
| [[LS 180 (line)]] | wt | 7.94 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.17× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H460 (line)]] | wt | 11.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -11.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 13.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +10.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.7) | — |
| [[A498 (line)]] | wt | 19.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -16.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 9.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.97× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 9.12 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0762× (z -10.4) |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -10.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 9.33 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0507× (z -17.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 17.1 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.00× (z +9.8) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SHP-77 (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -12.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 8.81 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0540× (z -13.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7319), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NARF]] | +0.70 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[MAP3K3]] | +0.66 | +0.44 / +0.74 | both halves | 3e-05 |  |
| [[NDUFA2]] | +0.66 | +0.33 / +0.69 | both halves | 1e-04 |  |
| [[DDT]] | +0.65 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[SRGAP2D]] | +0.63 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[CDC25C]] | +0.63 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[GMCL1]] | +0.63 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[KMT5C]] | +0.63 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[RHEBL1]] | +0.63 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[ZNF684]] | +0.63 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[EEF1AKMT4]] | +0.62 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[ANKRD13D]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF655]] | -0.65 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[GDAP1]] | -0.64 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[DST]] | -0.63 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[ANKEF1]] | -0.63 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[ZMYM4]] | -0.63 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[FKTN]] | -0.63 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[AFF4]] | -0.62 | -0.31 / -0.76 | both halves | 2e-04 | pathway: Affinity selection of immunoglobulins |
| [[PTPN11]] | -0.61 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[GMFB]] | -0.61 | -0.36 / -0.62 | both halves | 1e-04 |  |
| [[ZNF260]] | -0.61 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[ZNF780A]] | -0.60 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[TRIM44]] | -0.60 | -0.53 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TAF5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KRT80]] | B | KRT80 activity lowers TAF5's level | lines that do not express KRT80 (22) vs lines expressing it (28) | 1.19× higher at baseline in the lines without KRT80 | 0.094 | ⚠ within organs, on part of the lines; also absent: C19orf33, EPS8L2, SPNS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.583). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-8.8, -28.4); signed map (-39.4, 9.6). **Vector** length 76.3, 14.3% of its response variance represented; |z| ≥ 3 in 948 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +14.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.7 | +7.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.8 | +6.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +2.2 | +10.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.8 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +0.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.1 | +3.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +1.2 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +0.9 | +1.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +0.9 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.8 | -4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.5 | -7.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -2.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | TATA-box binding protein associated factor 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.33 — chr10:103,367,966-103,389,065 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TAFII100; previously TAF2D |
| Gene groups (HGNC) | WD repeat domain containing; General transcription factor IID complex subunits |
| Reactome | 20 pathways, smallest: HIV Transcription Initiation; RNA Polymerase II HIV Promoter Escape; RNA Polymerase II Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15542](https://www.uniprot.org/uniprotkb/Q15542) (Transcription initiation factor TFIID subunit 5):

> The TFIID basal transcription factor complex plays a major role in the initiation of RNA polymerase II (Pol II)-dependent transcription. TFIID recognizes and binds promoters with or without a TATA box via its subunit TBP, a TATA-box-binding protein, and promotes assembly of the pre-initiation complex (PIC). The TFIID complex consists of TBP and TBP-associated factors (TAFs), including TAF1, TAF2, TAF3, TAF4, TAF5, TAF6, TAF7, TAF8, TAF9, TAF10, TAF11, TAF12 and TAF13. The TFIID complex …

**Summary**, from NCBI Gene [6877](https://www.ncbi.nlm.nih.gov/gene/6877):

> Initiation of transcription by RNA polymerase II requires the activities of more than 70 polypeptides. The protein that coordinates these activities is transcription factor IID (TFIID), which binds to the core promoter to position the polymerase properly, serves as the scaffold for assembly of the remainder of the transcription complex, and acts as a channel for regulatory signals. TFIID is composed of the TATA-binding protein (TBP) and a group of evolutionarily conserved proteins known as …

**Accessions** — [HGNC:11539](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11539) · Entrez [6877](https://www.ncbi.nlm.nih.gov/gene/6877) · UniProt [Q15542](https://www.uniprot.org/uniprotkb/Q15542) · Ensembl [ENSG00000148835](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148835)

## Data

Gene col 7319: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7319); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7319, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7319]; `tensor/DDL_lfc|DDL_z.npy` [7319]; `embed/gene_vectors.npy` [7319]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7319 or target_col == 7319). Every well: [[TAF5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAF5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
