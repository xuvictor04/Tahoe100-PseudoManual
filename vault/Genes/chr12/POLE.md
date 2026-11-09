---
symbol: "POLE"
type: "gene"
col: 10789
ensembl_id: "ENSG00000177084"
name: "DNA polymerase epsilon, catalytic subunit"
location: "12q24.33"
module: 6
arm: "+"
pooled_cpm: 46.18
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 17
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 9
direction_downstream: 1
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# POLE

*DNA polymerase epsilon, catalytic subunit* — 12q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (19 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.74× (z +8.1, q 5e-13, up in 29 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H1792 10.5×, NCI-H1573 4.60×, HS-578T 3.59×, LoVo 2.71×, …; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.629× (z -7.0, q 1e-09, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FANCA]] (+0.91, fdr 7e-06), [[MYBL2]] (+0.90, fdr 7e-06), [[CDC45]] (+0.88, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PSPC1]] (grade A ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 19 with an alert ⚠; shown: the 15 strongest. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10789.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H1792 10.5×, NCI-H1573 4.60×, HS-578T 3.59×, LoVo 2.71×, …; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **1.74×** | +8.1 | 5e-13 | 29/41 (CFPAC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.55×** | +6.6 | 1e-08 | 31/48 (A549, LoVo, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.52×** | +6.3 | 5e-08 | 33/48 (PANC-1, SHP-77, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.43×** | +5.4 | 9e-06 | 31/48 (SHP-77, PANC-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.41×** | +5.1 | 3e-05 | 28/47 (A549, SHP-77, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.40×** | +5.1 | 3e-05 | 28/47 (PANC-1, SHP-77, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.40×** | +5.1 | 3e-05 | 26/48 (A549, LoVo, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.39×** | +5.0 | 4e-05 | 27/47 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.39×** | +4.7 | 1e-04 | 23/47 (PANC-1, SNU-423, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +4.6 | 3e-04 | 26/48 (NCI-H460, LoVo, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.35×** | +4.4 | 7e-04 | 24/48 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.33×** | +4.3 | 9e-04 | 23/47 (H4, NCI-H460, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **1.34×** | +4.3 | 9e-04 | 21/47 (SNU-1, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.34×** | +4.1 | 0.002 | 20/44 (RPMI-7951, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.20×** | +3.9 | 0.003 | 18/48 (A549, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10789.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM |  | **0.629×** | -7.0 | 1e-09 | 31/48 (SW 1271, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.750×** | -6.2 | 2e-07 | 27/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.667×** | -6.1 | 2e-07 | 31/48 (A-427, HEC-1-A, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.699×** | -5.4 | 8e-06 | 28/48 (HOP62, SW480, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.778×** | -5.4 | 8e-06 | 28/48 (SW480, SNU-423, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.755×** | -4.1 | 0.004 | 22/47 (SK-MEL-2, HEC-1-A, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.766×** | -4.0 | 0.004 | 20/48 (A-427, HEC-1-A, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 5 µM |  | **0.611×** | -3.9 | 0.007 | 21/47 (HEC-1-A, A-427, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.763×** | -3.9 | 0.007 | 23/48 (A-427, H4, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.710×** | -3.7 | 0.012 | 15/48 (A-172, A498, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.796×** | -3.6 | 0.013 | 18/48 (A-427, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.781×** | -3.6 | 0.013 | 19/47 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.05 µM |  | **0.778×** | -3.6 | 0.013 | 15/48 (HEC-1-A, A-427, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.822×** | -3.5 | 0.016 | 21/48 (SK-MEL-2, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | 0.849× | -3.5 | 0.016 | 16/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.794×** | -3.5 | 0.017 | 17/49 (SK-MEL-2, HEC-1-A, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 0.857× | -3.3 | 0.030 | 13/48 (KATO III, SW 900, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.808×** | -3.2 | 0.037 | 15/47 (RKO, SW480, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.843× | -3.0 | 0.080 | 14/48 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.75 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10789. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 84.3 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.136× (z -16.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 0.219× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 99.2 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -13.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SK-MEL-2 (line)]] | alt | 74.9 | 0 | 4 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.174× (z -12.4) |
| [[A498 (line)]] | wt | 33.4 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.418× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 67.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 42.9 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.305× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 76.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0774× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 17.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HS-578T (line)]] | alt | 20.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 41.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LOX-IMVI (line)]] | wt | 39.5 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.410× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 24.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +17.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1792 (line)]] | alt | 21.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +20.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 91.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.337× (z -9.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[RKO (line)]] | wt | 61.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.283× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 58.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10789), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANCA]] | +0.91 | +0.91 / +0.91 | both halves | 7e-06 | STRING 567 |
| [[MYBL2]] | +0.90 | +0.90 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[CDC45]] | +0.88 | +0.87 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 995 |
| [[MCM8]] | +0.87 | +0.82 / +0.88 | both halves | 7e-06 | pathway: Activation of the pre-replicative complex; STRING 819 |
| [[WDR76]] | +0.87 | +0.86 / +0.85 | both halves | 7e-06 |  |
| [[CHAF1A]] | +0.87 | +0.87 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 514 |
| [[CENPK]] | +0.87 | +0.85 / +0.87 | both halves | 7e-06 |  |
| [[XRCC2]] | +0.86 | +0.84 / +0.87 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 616 |
| [[TONSL]] | +0.86 | +0.84 / +0.85 | both halves | 7e-06 | STRING 464 |
| [[RAD51]] | +0.86 | +0.86 / +0.84 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 828 |
| [[MCM5]] | +0.86 | +0.84 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 997 |
| [[NCAPG2]] | +0.85 | +0.86 / +0.86 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises POLE's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.02× lower at baseline in the lines without E2F2 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises POLE's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.21× lower at baseline in the lines without E2F8 | 0.026 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises POLE's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[TERT]] | B | TERT activity raises POLE's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.47× lower at baseline in the lines without TERT | 0.056 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[CDC25A]] | B | CDC25A activity raises POLE's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.04× lower at baseline in the lines without CDC25A | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises POLE's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.99× lower at baseline in the lines without TCF19 | 0.094 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity strengthens POLE's drug response | lines that do not express E2F2 (13) vs lines expressing it (35) | the lines without E2F2 respond 0.88× as strongly (z diff +0.40); strongest at Homoharringtonine 0.5 µM: 0.99x vs 0.51x (z diff +4.2) | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[DSCC1]] | C | DSCC1 activity raises POLE's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.21× lower at baseline in the lines without DSCC1 | 0.027 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[ZNF367]] | C | ZNF367 activity raises POLE's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 2.04× lower at baseline in the lines without ZNF367 | 0.0998 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 1, B 0, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSPC1]] | A | the direction of POLE's effect on PSPC1's drug response is not inferred (the mechanism is not recorded) | recorded alteration (mechanism not recorded) of POLE in 8 lines vs 41 not recorded | the POLE-altered lines respond 0.60× as strongly (z diff +1.86); strongest at Digitoxin 5 µM: 1.46x vs 2.24x (z diff +3.1) | 0.009 | ⚠ within organs, on part of the lines; mechanism partly not recorded; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.896). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.4, -44.0); signed map (-37.2, -45.8). **Vector** length 146, 47.3% of its response variance represented; |z| ≥ 3 in 1,194 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.72 to 28); *E2F G1/S* (control, mean cos +0.72 to 23); *Cell Cycle Checkpoints* (reactome, mean cos +0.72 to 45).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | +6.0 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.5 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +4.5 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.4 | +4.1 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +3.0 | +2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.7 | +2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +2.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.5 | +2.1 |
|  | [[Methotrexate (drug)]] 5 µM |  | +2.5 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -7.2 | -6.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.6 | -6.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -6.0 | -7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.7 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.5 | -4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.4 | -4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.2 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.0 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | DNA polymerase epsilon, catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:132,623,753-132,687,376 (-) |
| Ensembl biotype | protein_coding |
| Also known as | POLE1 |
| Gene groups (HGNC) | DNA polymerases |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 30 pathways, smallest: DNA replication initiation; PCNA-Dependent Long Patch Base Excision Repair; Gap-filling DNA repair synthesis and ligation in GG-NER |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07864](https://www.uniprot.org/uniprotkb/Q07864) (DNA polymerase epsilon catalytic subunit A):

> Catalytic component of the DNA polymerase epsilon complex. Participates in chromosomal DNA replication (By similarity). Required during synthesis of the leading DNA strands at the replication fork, binds at/or near replication origins and moves along DNA with the replication fork (By similarity). Has 3'-5' proofreading exonuclease activity that corrects errors arising during DNA replication (By similarity). Involved in DNA synthesis during DNA repair. Along with DNA polymerase POLD1 and DNA …

**Summary**, from NCBI Gene [5426](https://www.ncbi.nlm.nih.gov/gene/5426):

> This gene encodes the catalytic subunit of DNA polymerase epsilon. The enzyme is involved in DNA repair and chromosomal DNA replication. Mutations in this gene have been associated with colorectal cancer 12 and facial dysmorphism, immunodeficiency, livedo, and short stature. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:9177](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9177) · Entrez [5426](https://www.ncbi.nlm.nih.gov/gene/5426) · UniProt [Q07864](https://www.uniprot.org/uniprotkb/Q07864) · Ensembl [ENSG00000177084](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177084)

## Data

Gene col 10789: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10789); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10789, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10789]; `tensor/DDL_lfc|DDL_z.npy` [10789]; `embed/gene_vectors.npy` [10789]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10789 or target_col == 10789). Every well: [[POLE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
