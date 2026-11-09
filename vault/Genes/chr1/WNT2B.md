---
symbol: "WNT2B"
type: "gene"
col: 5527
ensembl_id: "ENSG00000134245"
name: "Wnt family member 2B"
location: "1p13.2"
module: 38
arm: "+"
pooled_cpm: 66.37
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 39
n_dd_up_clean: 0
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# WNT2B

*Wnt family member 2B* — 1p13.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 3.03×; ⚠ cell-cycle shift, explains ~28% of this change).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (9 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.345× (z -10.9, q 7e-25, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BLZF2P]] (+0.73, fdr 7e-06), [[LINC02798]] (+0.72, fdr 7e-06), [[TTLL3]] (+0.70, fdr 7e-06); moves opposite to [[TRUB1]] (-0.64, fdr 1e-05), [[NELFCD]] (-0.62, fdr 7e-06), [[TRAPPC11]] (-0.58, fdr 1e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MFNG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5527.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 3.03×; ⚠ cell-cycle shift, explains ~28% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PF-06260933 (drug)]] 5 µM |  | 1.76× | +3.1 | 0.44 | 25/48 (HT-29, SNU-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.22× | +3.0 | 0.44 | 20/48 (SHP-77, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5527.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.345×** | -10.9 | 7e-25 | 40/48 (Panc 03.27, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.380×** | -10.3 | 2e-22 | 35/48 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.385×** | -9.8 | 3e-20 | 39/47 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.407×** | -9.6 | 2e-19 | 39/48 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.445×** | -8.6 | 8e-16 | 39/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.234×** | -8.1 | 6e-14 | 47/49 (LoVo, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.272×** | -7.3 | 3e-11 | 34/48 (RKO, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.507×** | -7.2 | 3e-11 | 33/47 (Panc 03.27, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.634×** | -6.9 | 5e-10 | 29/48 (HT-29, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.552×** | -6.3 | 1e-08 | 34/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.574×** | -5.9 | 2e-07 | 35/48 (NCI-H1792, RKO, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.354×** | -5.8 | 3e-07 | 42/47 (RKO, NCI-H23, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.585×** | -5.5 | 2e-06 | 25/41 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.620×** | -5.1 | 1e-05 | 30/49 (HT-29, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.622×** | -5.0 | 2e-05 | 29/48 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Anethole trithione (drug)]] 5 µM |  | **0.716×** | -5.0 | 2e-05 | 39/48 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.730×** | -4.7 | 7e-05 | 31/48 (RKO, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.653×** | -4.4 | 4e-04 | 26/49 (HEC-1-A, SNU-1, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.655×** | -4.3 | 4e-04 | 31/48 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.670×** | -4.3 | 6e-04 | 28/48 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.773×** | -3.9 | 0.003 | 28/48 (RKO, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5527. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 178 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -22.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.116× (z -16.0) |
| [[HT-29 (line)]] | alt | 184 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -25.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.196× (z -13.4) |
| [[LoVo (line)]] | wt | 107 | 0 | 9 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.136× (z -17.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -15.4) |
| [[COLO 205 (line)]] | alt | 131 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -19.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.157× (z -14.7) |
| [[LS 180 (line)]] | wt | 52.9 | 0 | 8 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.126× (z -13.0) |
| [[AsPC-1 (line)]] | alt | 98.0 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -21.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.124× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 82.8 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.126× (z -16.3) |
| [[NCI-H23 (line)]] | alt | 183 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 57.2 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.245× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 90.8 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.141× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 122 | 0 | 6 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0681× (z -10.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 75.3 | 0 | 6 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.186× (z -13.0) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.250× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 62.0 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0487× (z -18.5) |
| [[PANC-1 (line)]] | alt | 44.0 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.167× (z -14.1) |
| [[H4 (line)]] | wt | 67.0 | 0 | 4 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0653× (z -15.0) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.127× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 178 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.224× (z -9.0) |
| [[KATO III (line)]] | alt | 44.4 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.166× (z -12.1) |
| [[SW480 (line)]] | alt | 30.5 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.155× (z -15.3) |
| [[A549 (line)]] | wt | 40.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -12.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.182× (z -10.1) |
| [[BT-474 (line)]] | alt | 36.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -10.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.183× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 67.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -15.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.211× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 91.7 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.217× (z -10.6) |
| [[A498 (line)]] | wt | 42.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -11.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.204× (z -10.3) |
| [[C-33 A (line)]] | alt | 81.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -9.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 100 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[J82 (line)]] | alt | 51.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 37.3 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.119× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 91.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +11.5) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 5 µM 0.203× (z -11.2) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 71.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0561× (z -9.8) |
| [[A-427 (line)]] | wt | 34.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.222× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 54.2 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.263× (z -9.6) |
| [[SNU-423 (line)]] | alt | 38.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.185× (z -9.4) |
| [[SW 900 (line)]] | alt | 45.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.156× (z -11.2) ⚠ toxic |
| [[SW1417 (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -11.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5527), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLZF2P]] | +0.73 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[LINC02798]] | +0.72 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[TTLL3]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[C11orf91]] | +0.70 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[UCKL1-AS1]] | +0.70 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[LINC01588]] | +0.70 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[POU2F2]] | +0.69 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[CDKL4]] | +0.67 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[UBE2F-SCLY]] | +0.66 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[SLC22A14]] | +0.66 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[SLC22A13]] | +0.66 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[ATP8B5P-1]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRUB1]] | -0.64 | -0.53 / -0.73 | both halves | 1e-05 |  |
| [[NELFCD]] | -0.62 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[TRAPPC11]] | -0.58 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[KCTD3]] | -0.57 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[XPO1]] | -0.57 | -0.60 / -0.54 | both halves | 1e-05 | pathway: Signaling by WNT |
| [[FBXO7]] | -0.56 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[TM7SF3]] | -0.56 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[MRS2]] | -0.55 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[UBA5]] | -0.54 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[CFAP418]] | -0.54 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MFNG]] | B | MFNG activity lowers WNT2B's level | lines that do not express MFNG (12) vs lines expressing it (38) | 1.53× higher at baseline in the lines without MFNG | 0.062 | ⚠ within organs, on part of the lines; also absent: CARD10, EPS8L2, KRT8 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.673). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.3, -19.9); signed map (15.1, 14.5). **Vector** length 138, 49.7% of its response variance represented; |z| ≥ 3 in 1,389 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.5 | +1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.4 | +2.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.5 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.5 | +0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.4 | +3.1 |
| fall | [[Radotinib (drug)]] 5 µM |  | -6.6 | -3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.6 | -1.3 |
|  | [[NG25 (drug)]] 5 µM |  | -6.2 | -5.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.8 | -4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.5 | -4.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -5.0 | -3.7 |
|  | [[Afatinib (drug)]] 5 µM |  | -4.7 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | Wnt family member 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:112,466,541-112,530,165 (+) |
| Ensembl biotype | protein_coding |
| Also known as | XWNT2; previously WNT13 |
| Gene groups (HGNC) | Wnt family |
| Reactome | 5 pathways, smallest: WNT ligand biogenesis and trafficking; Class B/2 (Secretin family receptors); GPCR ligand binding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q93097](https://www.uniprot.org/uniprotkb/Q93097) (Protein Wnt-2b):

> Ligand for members of the frizzled family of seven transmembrane receptors. Functions in the canonical Wnt/beta-catenin signaling pathway. Plays a redundant role in embryonic lung development.

**Summary**, from NCBI Gene [7482](https://www.ncbi.nlm.nih.gov/gene/7482):

> This gene encodes a member of the wingless-type MMTV integration site (WNT) family of highly conserved, secreted signaling factors. WNT family members function in a variety of developmental processes including regulation of cell growth and differentiation and are characterized by a WNT-core domain. This gene may play a role in human development as well as carcinogenesis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2014]

**Accessions** — [HGNC:12781](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12781) · Entrez [7482](https://www.ncbi.nlm.nih.gov/gene/7482) · UniProt [Q93097](https://www.uniprot.org/uniprotkb/Q93097) · Ensembl [ENSG00000134245](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134245)

## Data

Gene col 5527: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5527); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5527, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5527]; `tensor/DDL_lfc|DDL_z.npy` [5527]; `embed/gene_vectors.npy` [5527]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5527 or target_col == 5527). Every well: [[WNT2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WNT2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
