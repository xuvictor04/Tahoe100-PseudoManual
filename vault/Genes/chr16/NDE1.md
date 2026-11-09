---
symbol: "NDE1"
type: "gene"
col: 1037
ensembl_id: "ENSG00000072864"
name: "nudE neurodevelopment protein 1"
location: "16p13.11"
module: 22
arm: "+"
pooled_cpm: 90.04
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 44
n_dd_up_clean: 0
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# NDE1

*nudE neurodevelopment protein 1* — 16p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.22× (z +4.7, q 0.001, up in 22 of 48 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~55% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (PANC-1 2.79×, J82 2.79×, A498 1.86×, A549 2.02×, …); [[Harringtonine (drug)]] 5 µM in 4 lines (PANC-1 4.12×, A498 2.53×, A549 2.80×, J82 2.18×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (PANC-1 2.42×).
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (14 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.564× (z -19.0, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HJURP]] (+0.73, fdr 7e-06), [[TROAP]] (+0.72, fdr 7e-06), [[PRR11]] (+0.72, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1037.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (PANC-1 2.79×, J82 2.79×, A498 1.86×, A549 2.02×, …); [[Harringtonine (drug)]] 5 µM in 4 lines (PANC-1 4.12×, A498 2.53×, A549 2.80×, J82 2.18×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (PANC-1 2.42×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.22×** | +4.7 | 0.001 | 22/48 (HT-29, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Tofacitinib (drug)]] 5 µM |  | 1.11× | +3.4 | 0.12 | 7/49 (NCI-H1573, KATO III, …) | top dose only |  |
| [[Pentoxifylline (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.12 | 8/48 (J82, LoVo, …) | two highest doses | position effect removed |
| [[crizotinib (drug)]] 5 µM |  | 1.16× | +3.3 | 0.15 | 11/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Mebendazole (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.16 | 8/48 (HT-29, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 62 in all, 22 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1037.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.564×** | -19.0 | 0e+00 | 44/48 (HS-578T, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.600×** | -11.9 | 2e-30 | 31/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.611×** | -11.5 | 1e-28 | 43/48 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.619×** | -11.2 | 4e-27 | 40/48 (NCI-H460, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.653×** | -10.0 | 2e-21 | 39/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.653×** | -9.6 | 1e-19 | 36/47 (PANC-1, CHP-212, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.667×** | -9.5 | 2e-19 | 32/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.690×** | -8.7 | 3e-16 | 37/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.657×** | -8.6 | 8e-16 | 36/48 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.716×** | -7.8 | 3e-13 | 30/48 (SW480, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.796×** | -7.5 | 2e-12 | 26/48 (AsPC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.805×** | -7.2 | 4e-11 | 27/48 (A-427, HOP62, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.529×** | -6.3 | 2e-08 | 30/48 (SNU-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | **0.759×** | -6.2 | 2e-08 | 22/44 (SW 900, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.769×** | -6.1 | 3e-08 | 28/49 (HepG2/C3A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.775×** | -6.0 | 8e-08 | 27/48 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.548×** | -5.9 | 1e-07 | 29/48 (NCI-H460, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.556×** | -5.8 | 2e-07 | 27/48 (A498, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.776×** | -5.7 | 4e-07 | 23/47 (NCI-H460, HepG2/C3A, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.785×** | -5.6 | 5e-07 | 22/47 (HepG2/C3A, NCI-H460, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.781×** | -5.6 | 8e-07 | 27/48 (HS-578T, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1037. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 114 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.378× (z -12.5) |
| [[PANC-1 (line)]] | alt | 117 | 4 (2 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +21.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.476× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~30% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.618× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 88.2 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -19.0) |
| [[SK-MEL-2 (line)]] | alt | 102 | 0 | 6 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.287× (z -12.5) |
| [[SW 900 (line)]] | alt | 110 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.353× (z -13.3) |
| [[SW480 (line)]] | alt | 89.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -14.3) |
| [[A498 (line)]] | wt | 108 | 2 (1 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.53× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.86× (z +12.2) | [[Selinexor (drug)]] 5 µM 0.578× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 93.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.365× (z -11.2) |
| [[A-427 (line)]] | wt | 84.6 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.445× (z -11.9) |
| [[A549 (line)]] | wt | 105 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.8) | [[Selinexor (drug)]] 5 µM 0.514× (z -10.2) |
| [[J82 (line)]] | alt | 77.7 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +17.6) | [[Selinexor (drug)]] 5 µM 0.554× (z -10.1) |
| [[LoVo (line)]] | wt | 87.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -13.4) |
| [[C32 (line)]] | wt | 99.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 137 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.394× (z -11.1) |
| [[HOP62 (line)]] | alt | 82.1 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.449× (z -11.8) |
| [[Hs 766T (line)]] | wt | 252 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.400× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 54.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.305× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 189 | 0 | 2 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.263× (z -10.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 54.0 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.433× (z -12.1) |
| [[SNU-1 (line)]] | wt | 151 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -16.9) |
| [[A-172 (line)]] | wt | 83.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.537× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 45.7 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.504× (z -9.1) |
| [[CHP-212 (line)]] | wt | 45.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0924× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[H4 (line)]] | wt | 59.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -8.7) |
| [[HCT15 (line)]] | alt | 77.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.310× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 58.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 66.7 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.371× (z -14.2) |
| [[KATO III (line)]] | alt | 73.1 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.547× (z -9.1) |
| [[LS 180 (line)]] | wt | 79.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 68.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -12.5) |
| [[Panc 03.27 (line)]] | alt | 75.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.517× (z -9.8) |
| [[RKO (line)]] | wt | 47.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -12.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 61.7 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.393× (z -11.7) |
| [[SW1417 (line)]] | alt | 81.3 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.548× (z -9.5) |
| [[AN3 CA (line)]] | alt | 94.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 93.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1037), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HJURP]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 | pathway: G2/M Transition |
| [[TROAP]] | +0.72 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[PRR11]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[PTTG1]] | +0.72 | +0.61 / +0.69 | both halves | 7e-06 | pathway: Mitotic Anaphase |
| [[PIMREG]] | +0.71 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[KIF2C]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 620 |
| [[KMT5A]] | +0.71 | +0.57 / +0.74 | both halves | 9e-06 | **novel candidate** |
| [[DLGAP5]] | +0.69 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[GTSE1]] | +0.69 | +0.59 / +0.70 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[KIF18B]] | +0.68 | +0.67 / +0.65 | both halves | 7e-06 | same gene group; STRING 599 |
| [[PIF1]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[TACC3]] | +0.68 | +0.64 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises NDE1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 8.1% of all compounds | 0.042 | ⚠ off-target possible; 4 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.676). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.8, -57.8); signed map (-52.4, -40.5). **Vector** length 139, 44.5% of its response variance represented; |z| ≥ 3 in 1,368 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.54 to 60); *DREAM G2/M down* (control, mean cos +0.61 to 28); *mitotic spindle* (hallmark, mean cos +0.53 to 38).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +0.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.0 | -1.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | -0.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.7 | +0.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | +3.7 | +4.7 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +2.7 | +3.2 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.5 | +2.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.4 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +0.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -11.4 | -19.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -8.2 | -8.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -6.4 | -10.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.3 | -11.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.3 | -6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.1 | -11.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -6.0 | -5.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.4 | -5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.1 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | nudE neurodevelopment protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.11 — chr16:15,643,267-15,734,691 (+) |
| Ensembl biotype | protein_coding |
| Also known as | nudE, FLJ20101, NDE |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Reactome | 30 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXR1](https://www.uniprot.org/uniprotkb/Q9NXR1) (Nuclear distribution protein nudE homolog 1):

> Required for centrosome duplication and formation and function of the mitotic spindle. Essential for the development of the cerebral cortex. May regulate the production of neurons by controlling the orientation of the mitotic spindle during division of cortical neuronal progenitors of the proliferative ventricular zone of the brain. Orientation of the division plane perpendicular to the layers of the cortex gives rise to two proliferative neuronal progenitors whereas parallel orientation of the …

**Summary**, from NCBI Gene [54820](https://www.ncbi.nlm.nih.gov/gene/54820):

> This gene encodes a member of the nuclear distribution E (NudE) family of proteins. The encoded protein is localized at the centrosome and interacts with other centrosome components as part of a multiprotein complex that regulates dynein function. This protein plays an essential role in microtubule organization, mitosis and neuronal migration. Mutations in this gene cause lissencephaly 4, a disorder characterized by lissencephaly, severe brain atrophy, microcephaly, and severe cognitive …

**Accessions** — [HGNC:17619](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17619) · Entrez [54820](https://www.ncbi.nlm.nih.gov/gene/54820) · UniProt [Q9NXR1](https://www.uniprot.org/uniprotkb/Q9NXR1) · Ensembl [ENSG00000072864](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072864)

## Data

Gene col 1037: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1037); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1037, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1037]; `tensor/DDL_lfc|DDL_z.npy` [1037]; `embed/gene_vectors.npy` [1037]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1037 or target_col == 1037). Every well: [[NDE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
