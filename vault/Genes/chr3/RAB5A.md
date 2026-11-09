---
symbol: "RAB5A"
type: "gene"
col: 6895
ensembl_id: "ENSG00000144566"
name: "RAB5A, member RAS oncogene family"
location: "3p24.3"
module: 41
arm: "+"
pooled_cpm: 175.4
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 28
n_dd_up_clean: 5
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# RAB5A

*RAB5A, member RAS oncogene family* — 3p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.81× (z +5.4, q 5e-05, up in 37 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.488× (z -12.4, q 2e-32, down in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.499× (z -12.0, q 2e-30, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARF4]] (+0.79, fdr 7e-06), [[COQ10B]] (+0.79, fdr 7e-06), [[STX5]] (+0.77, fdr 7e-06); moves opposite to [[RPE]] (-0.64, fdr 1e-05), [[VMA21]] (-0.63, fdr 7e-06), [[DHX9]] (-0.62, fdr 7e-06).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KCNK6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6895.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +5.4 | 5e-05 | 37/49 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.012 | 30/48 (SNU-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.48×** | +3.5 | 0.064 | 29/48 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.48×** | +3.5 | 0.064 | 30/48 (RPMI-7951, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.090 | 25/48 (SNU-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.20× | +3.2 | 0.15 | 23/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6895.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.488×** | -12.4 | 2e-32 | 45/48 (AsPC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.499×** | -12.0 | 2e-30 | 45/48 (HT-29, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.546×** | -10.4 | 4e-23 | 43/48 (AsPC-1, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.604×** | -8.4 | 9e-15 | 33/44 (SW48, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.736×** | -7.4 | 1e-11 | 33/49 (A549, NCI-H1792, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.672×** | -6.6 | 5e-09 | 42/48 (A549, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.689×** | -6.4 | 1e-08 | 38/49 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.776×** | -6.1 | 7e-08 | 31/48 (AsPC-1, NCI-H1792, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.707×** | -6.0 | 1e-07 | 40/48 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.724×** | -5.6 | 2e-06 | 43/48 (LOX-IMVI, AsPC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.709×** | -5.5 | 2e-06 | 31/45 (LoVo, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.806×** | -5.2 | 9e-06 | 31/48 (A-172, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.747×** | -5.0 | 2e-05 | 35/48 (HT-29, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.760×** | -4.5 | 2e-04 | 33/48 (HEC-1-A, hTERT-HPNE, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.607×** | -4.5 | 3e-04 | 32/48 (AsPC-1, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.807×** | -3.7 | 0.007 | 24/48 (NCI-H2347, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.809×** | -3.7 | 0.008 | 30/48 (NCI-H2030, AsPC-1, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.865× | -3.5 | 0.013 | 15/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.812×** | -3.5 | 0.015 | 24/48 (SW 900, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.682×** | -3.4 | 0.015 | 28/48 (AsPC-1, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.690×** | -3.3 | 0.021 | 20/48 (AsPC-1, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.820×** | -3.3 | 0.027 | 23/48 (HS-578T, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.832×** | -3.2 | 0.033 | 22/47 (HepG2/C3A, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6895. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 176 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.352× (z -12.8) |
| [[NCI-H1792 (line)]] | alt | 266 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -11.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.365× (z -10.0) |
| [[A549 (line)]] | wt | 226 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -15.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.391× (z -11.8) |
| [[LoVo (line)]] | wt | 210 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.391× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[RPMI-7951 (line)]] | alt | 273 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.434× (z -10.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.457× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 234 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.309× (z -15.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.409× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 135 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.400× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 222 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.487× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.552× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 197 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.294× (z -12.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.342× (z -11.3) |
| [[NCI-H2347 (line)]] | alt | 226 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.463× (z -11.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.472× (z -10.9) |
| [[Panc 03.27 (line)]] | alt | 192 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.334× (z -14.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.453× (z -10.3) |
| [[SW 900 (line)]] | alt | 175 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.337× (z -12.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.397× (z -10.4) |
| [[SW1417 (line)]] | alt | 273 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.450× (z -12.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.475× (z -11.7) |
| [[HOP62 (line)]] | alt | 233 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.390× (z -10.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.438× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 168 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.398× (z -11.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1573 (line)]] | alt | 165 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.326× (z -12.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.407× (z -10.0) |
| [[Hs 766T (line)]] | wt | 174 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.370× (z -11.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.441× (z -9.1) |
| [[BT-474 (line)]] | alt | 158 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.457× (z -9.1) |
| [[CHP-212 (line)]] | wt | 159 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HepG2_C3A (line)]] | wt | 128 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.446× (z -8.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 206 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.451× (z -11.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 174 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[LS 180 (line)]] | wt | 229 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[MIA PaCa-2 (line)]] | alt | 120 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.4) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[NCI-H2030 (line)]] | alt | 166 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.411× (z -10.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 125 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.0) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[NCI-H596 (line)]] | alt | 180 | 0 | 1 | — | [[Irinotecan (drug)]] 5 µM 0.0776× (z -9.5) |
| [[SNU-1 (line)]] | wt | 135 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +8.6) | — |
| [[SW48 (line)]] | wt | 189 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW480 (line)]] | alt | 162 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.484× (z -9.0) |
| [[A-172 (line)]] | wt | 171 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 130 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 86.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 172 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 266 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6895), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARF4]] | +0.79 | +0.81 / +0.78 | both halves | 7e-06 | STRING 476 |
| [[COQ10B]] | +0.79 | +0.77 / +0.76 | both halves | 7e-06 |  |
| [[STX5]] | +0.77 | +0.72 / +0.82 | both halves | 7e-06 | STRING 486 |
| [[FAM177A1]] | +0.75 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[OSBP]] | +0.75 | +0.80 / +0.69 | both halves | 7e-06 |  |
| [[TINCR]] | +0.74 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[SPTY2D1]] | +0.73 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[PHKG1]] | +0.71 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[SRP54]] | +0.70 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[TBC1D23]] | +0.70 | +0.72 / +0.65 | both halves | 7e-06 | STRING 537 |
| [[SEC31A]] | +0.68 | +0.75 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION |
| [[ACBD3]] | +0.68 | +0.75 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPE]] | -0.64 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[VMA21]] | -0.63 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[DHX9]] | -0.62 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[TMEM33]] | -0.62 | -0.64 / -0.57 | both halves | 8e-06 |  |
| [[CAPRIN1]] | -0.61 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[PPP2R1B]] | -0.61 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[CCT5]] | -0.60 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[FAM98B]] | -0.60 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[GOT2]] | -0.59 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[ELAC2]] | -0.59 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[AGPS]] | -0.58 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[ATIC]] | -0.58 | -0.58 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNK6]] | B | KCNK6 activity raises RAB5A's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 1.39× lower at baseline in the lines without KCNK6 | 0.008 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.752). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (10.2, -37.7); signed map (-49.4, 14.7). **Vector** length 111, 40.2% of its response variance represented; |z| ≥ 3 in 1,129 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Intra-Golgi and retrograde Golgi-to-ER traffic* (reactome, mean cos +0.54 to 12); *Asparagine N-linked glycosylation* (reactome, mean cos +0.56 to 12); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.63 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | -2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.3 | -7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.0 | +3.5 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.8 | +1.8 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.7 | +1.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.3 | -6.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.7 | -6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.5 | -3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.7 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -3.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.5 | -3.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | RAB5A, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.3 — chr3:19,947,097-19,985,175 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RAB5 |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 21 pathways, smallest: Prevention of phagosomal-lysosomal fusion; Suppression of phagosomal maturation; Response of Mtb to phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [P20339](https://www.uniprot.org/uniprotkb/P20339) (Ras-related protein Rab-5A):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. RAB5A is required for the fusion of plasma membranes and early endosomes and involved in early endocytic trafficking. …

**Summary**, from NCBI Gene [5868](https://www.ncbi.nlm.nih.gov/gene/5868):

> Enables G protein activity; GDP binding activity; and GTP binding activity. Involved in several processes, including amyloid-beta clearance by transcytosis; early endosome to late endosome transport; and regulation of exocytosis. Located in several cellular components, including cytoplasmic side of early endosome membrane; somatodendritic compartment; and terminal bouton. Is active in early endosome membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9783](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9783) · Entrez [5868](https://www.ncbi.nlm.nih.gov/gene/5868) · UniProt [P20339](https://www.uniprot.org/uniprotkb/P20339) · Ensembl [ENSG00000144566](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144566)

## Data

Gene col 6895: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6895); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6895, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6895]; `tensor/DDL_lfc|DDL_z.npy` [6895]; `embed/gene_vectors.npy` [6895]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6895 or target_col == 6895). Every well: [[RAB5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
