---
symbol: "PCDH1"
type: "gene"
col: 7980
ensembl_id: "ENSG00000156453"
name: "protocadherin 1"
location: "5q31.3"
module: 31
arm: "+"
pooled_cpm: 27.29
n_lines_expressing: 30
n_dd_up: 12
n_dd_down: 29
n_dd_up_clean: 8
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 52
direction_downstream: 105
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# PCDH1

*protocadherin 1* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.47× (z +7.1, q 5e-10, up in 11 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.492× (z -13.1, q 3e-36, down in 23 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JUP]] (+0.68, fdr 7e-06), [[HS3ST1]] (+0.66, fdr 7e-06), [[CAPG]] (+0.64, fdr 7e-06); moves opposite to [[ST3GAL3]] (-0.50, fdr 3e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 52 arrows point to it, the strongest [[PROSER2]] → it (grade B ⚠); 105 go from it, the strongest it → [[KIAA1522]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7980.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +7.1 | 5e-10 | 11/28 (A-172, HEC-1-A, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 0.05 µM |  | **1.65×** | +6.6 | 1e-08 | 13/28 (SW1417, SW480, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +6.2 | 1e-07 | 10/27 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.37×** | +5.9 | 5e-07 | 12/28 (HT-29, A-427, …) | all doses, flat | low cells (technical?) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.43×** | +4.8 | 2e-04 | 16/27 (SW1417, SW480, …) | top dose only | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.84×** | +4.2 | 0.003 | 14/25 (Hs 766T, COLO 205, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.38×** | +4.1 | 0.003 | 8/25 (CFPAC-1, NCI-H1573, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.6 | 0.023 | 0/28 | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.026 | 7/25 (NCI-H1573, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.036 | 10/27 (LoVo, CFPAC-1, …) | two highest doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.29×** | +3.4 | 0.036 | 6/27 (A-427, LS 180, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.28×** | +3.2 | 0.057 | 9/25 (SK-MEL-2, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.26×** | +3.1 | 0.092 | 3/26 (A-172, J82, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7980.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.492×** | -13.1 | 3e-36 | 23/27 (MIA PaCa-2, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.527×** | -8.3 | 2e-14 | 19/27 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.541×** | -7.7 | 3e-12 | 20/26 (SK-MEL-2, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.680×** | -7.1 | 2e-10 | 19/27 (Hs 766T, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.598×** | -6.7 | 3e-09 | 15/27 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.611×** | -6.4 | 1e-08 | 18/27 (Hs 766T, KATO III, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.613×** | -6.4 | 2e-08 | 19/25 (LoVo, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.654×** | -5.5 | 3e-06 | 18/26 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.672×** | -5.2 | 2e-05 | 17/27 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.665×** | -5.1 | 2e-05 | 18/27 (KATO III, Hs 766T, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.669×** | -5.0 | 3e-05 | 16/24 (Hs 766T, Panc 03.27, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.688×** | -4.8 | 6e-05 | 16/28 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.692×** | -4.8 | 8e-05 | 16/27 (LS 180, SW1417, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.707×** | -4.5 | 3e-04 | 17/27 (Hs 766T, KATO III, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.734×** | -4.0 | 0.002 | 16/27 (AsPC-1, KATO III, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.567×** | -3.9 | 0.004 | 16/26 (Panc 03.27, COLO 205, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.576×** | -3.7 | 0.005 | 10/26 (KATO III, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.597×** | -3.5 | 0.012 | 14/25 (KATO III, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.826×** | -3.5 | 0.013 | 14/28 (MIA PaCa-2, Hs 766T, …) | top dose only | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.784×** | -3.1 | 0.040 | 11/27 (HepG2/C3A, SW 1271, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.714×** | -3.1 | 0.042 | 11/28 (LoVo, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Trimetrexate (drug)]] 5 µM |  | 0.843× | -3.1 | 0.042 | 9/27 (HT-29, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.637×** | -3.1 | 0.047 | 9/27 (Panc 03.27, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.791×** | -3.0 | 0.052 | 10/27 (A-172, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7980. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 99.7 | 0 | 11 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0981× (z -23.3) |
| [[KATO III (line)]] | alt | 106 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -20.1) |
| [[AsPC-1 (line)]] | alt | 69.2 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -15.3) |
| [[Hs 766T (line)]] | wt | 191 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -24.5) |
| [[Panc 03.27 (line)]] | alt | 124 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -19.3) |
| [[COLO 205 (line)]] | alt | 54.9 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -13.4) |
| [[HT-29 (line)]] | alt | 46.1 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.192× (z -11.8) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -9.9) |
| [[LoVo (line)]] | wt | 39.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -15.4) |
| [[SW1417 (line)]] | alt | 79.6 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.256× (z -14.9) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 64.1 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -18.9) |
| [[SK-MEL-2 (line)]] | alt | 25.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0972× (z -20.6) |
| [[C32 (line)]] | wt | 25.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.208× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.349× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 21.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.186× (z -11.0) |
| [[LS 180 (line)]] | wt | 35.2 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.270× (z -9.7) ⚠ cell-cycle shift, explains ~54% of this change |
| [[BT-474 (line)]] | alt | 16.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 25.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -9.0) |
| [[SW480 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.299× (z -8.7) ⚠ cell-cycle shift, explains ~68% of this change |
| [[A-172 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.43 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.37 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.24 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.66 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7980), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUP]] | +0.68 | +0.61 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |
| [[HS3ST1]] | +0.66 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[CAPG]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[CRYBG2]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[C1orf116]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[SEMA3B]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[ITGB4]] | +0.60 | +0.69 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_APICAL_JUNCTION; STRING 472 |
| [[TRIP10]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[PTK6]] | +0.59 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[MUC3A]] | +0.59 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[KIAA0040]] | +0.59 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[GJB3]] | +0.59 | +0.59 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST3GAL3]] | -0.50 | -0.58 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*52 arrows, 52 of them with an alert ⚠; grade A 0, B 20, C 32. Shown: the 12 strongest; 40 more arrows (40 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PROSER2]] | B | PROSER2 activity raises PCDH1's level | lines that do not express PROSER2 (14) vs lines expressing it (36) | 3.17× lower at baseline in the lines without PROSER2 | 0.002 | ⚠ within organs, on part of the lines; also absent: BIK, EPS8L2, SERPINB9P1; maybe low, not absent |
| [[TINAGL1]] | B | TINAGL1 activity raises PCDH1's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 3.28× lower at baseline in the lines without TINAGL1 | 0.010 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[VSIR]] | B | VSIR activity raises PCDH1's level | lines that do not express VSIR (14) vs lines expressing it (36) | 3.35× lower at baseline in the lines without VSIR | 0.020 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |
| [[SEMA3B]] | B | SEMA3B activity raises PCDH1's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.36× lower at baseline in the lines without SEMA3B | 0.020 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[LPAR5]] | B | LPAR5 activity raises PCDH1's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 3.01× lower at baseline in the lines without LPAR5 | 0.024 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[SH3TC1]] | B | SH3TC1 activity raises PCDH1's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 2.66× lower at baseline in the lines without SH3TC1 | 0.034 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[TOP2A]] | B | TOP2A activity raises PCDH1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TTC9]] | B | TTC9 activity raises PCDH1's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 2.14× lower at baseline in the lines without TTC9 | 0.038 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |
| [[UNC13D]] | B | UNC13D activity raises PCDH1's level | lines that do not express UNC13D (14) vs lines expressing it (36) | 2.73× lower at baseline in the lines without UNC13D | 0.048 | ⚠ within organs, on part of the lines; also absent: PRAG1, CDS1, VAMP5; maybe low, not absent |
| [[KRT19]] | B | KRT19 activity raises PCDH1's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 3.21× lower at baseline in the lines without KRT19 | 0.051 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |
| [[NECTIN1]] | B | NECTIN1 activity raises PCDH1's level | lines that do not express NECTIN1 (8) vs lines expressing it (42) | 2.30× lower at baseline in the lines without NECTIN1 | 0.056 | ⚠ within organs, on part of the lines; also absent: PRR5; maybe low, not absent |
| [[GPRC5A]] | B | GPRC5A activity raises PCDH1's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 2.88× lower at baseline in the lines without GPRC5A | 0.057 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |

### Downstream of this gene

*105 arrows, 105 of them with an alert ⚠; grade A 0, B 79, C 26. Shown: the 12 strongest; 93 more arrows (93 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA1522]] | B | PCDH1 activity raises KIAA1522's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.90× lower at baseline in the lines without PCDH1 | 8e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[CRYBG2]] | B | PCDH1 activity raises CRYBG2's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 3.09× lower at baseline in the lines without PCDH1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[LPAR5]] | B | PCDH1 activity raises LPAR5's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.40× lower at baseline in the lines without PCDH1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[CORO2A]] | B | PCDH1 activity raises CORO2A's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.39× lower at baseline in the lines without PCDH1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[ARHGAP27]] | B | PCDH1 activity raises ARHGAP27's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.36× lower at baseline in the lines without PCDH1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[ARHGEF16]] | B | PCDH1 activity raises ARHGEF16's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.39× lower at baseline in the lines without PCDH1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[MFSD6]] | B | PCDH1 activity raises MFSD6's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 1.88× lower at baseline in the lines without PCDH1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[JUP]] | B | PCDH1 activity raises JUP's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 3.24× lower at baseline in the lines without PCDH1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[UNC13D]] | B | PCDH1 activity raises UNC13D's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.98× lower at baseline in the lines without PCDH1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[EPB41L1]] | B | PCDH1 activity raises EPB41L1's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.50× lower at baseline in the lines without PCDH1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[TJP2]] | B | PCDH1 activity raises TJP2's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.84× lower at baseline in the lines without PCDH1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[PARD6B]] | B | PCDH1 activity raises PARD6B's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.31× lower at baseline in the lines without PCDH1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.740). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.0, 55.6); signed map (-1.6, 38.8). **Vector** length 84.2, 23.8% of its response variance represented; |z| ≥ 3 in 749 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +4.6 | +5.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.9 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +7.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +2.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.3 | +3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | -0.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.0 | +4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.3 | -3.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.9 | -3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -3.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | protocadherin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:141,853,090-141,879,246 (-) |
| Ensembl biotype | protein_coding |
| Also known as | pc42 |
| Gene groups (HGNC) | Non-clustered protocadherins |
| Hallmark sets | APICAL_JUNCTION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08174](https://www.uniprot.org/uniprotkb/Q08174) (Protocadherin-1):

> May be involved in cell-cell interaction processes and in cell adhesion.

**Summary**, from NCBI Gene [5097](https://www.ncbi.nlm.nih.gov/gene/5097):

> This gene belongs to the protocadherin subfamily within the cadherin superfamily. The encoded protein is a membrane protein found at cell-cell boundaries. It is involved in neural cell adhesion, suggesting a possible role in neuronal development. The protein includes an extracelllular region, containing 7 cadherin-like domains, a transmembrane region and a C-terminal cytoplasmic region. Cells expressing the protein showed cell aggregation activity. Alternative splicing occurs in this gene. …

**Accessions** — [HGNC:8655](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8655) · Entrez [5097](https://www.ncbi.nlm.nih.gov/gene/5097) · UniProt [Q08174](https://www.uniprot.org/uniprotkb/Q08174) · Ensembl [ENSG00000156453](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156453)

## Data

Gene col 7980: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7980); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7980, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7980]; `tensor/DDL_lfc|DDL_z.npy` [7980]; `embed/gene_vectors.npy` [7980]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7980 or target_col == 7980). Every well: [[PCDH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCDH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
