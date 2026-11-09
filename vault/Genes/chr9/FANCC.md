---
symbol: "FANCC"
type: "gene"
col: 8140
ensembl_id: "ENSG00000158169"
name: "FA complementation group C"
location: "9q22.32"
module: 6
arm: "+"
pooled_cpm: 79.61
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# FANCC

*FA complementation group C* — 9q22.32

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.469× (z -23.6, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FANCA]] (+0.72, fdr 7e-06), [[MELK]] (+0.71, fdr 7e-06), [[MYO19]] (+0.71, fdr 7e-06); moves opposite to [[CHMP4B]] (-0.58, fdr 9e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8140.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.9 | 0.051 | 14/47 (A549, Panc 03.27, …) | inconsistent across doses |  |
| [[Irinotecan (drug)]] 0.5 µM |  | 1.24× | +3.4 | 0.22 | 9/48 (SW480, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brimonidine (drug)]] 5 µM |  | 1.15× | +3.2 | 0.27 | 7/48 (LS 180, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8140.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.469×** | -23.6 | 0e+00 | 42/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.493×** | -15.0 | 0e+00 | 44/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.525×** | -14.2 | 2e-43 | 41/48 (H4, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.593×** | -10.6 | 3e-24 | 28/45 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.613×** | -10.4 | 4e-23 | 29/44 (A-427, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.629×** | -10.2 | 2e-22 | 38/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.638×** | -9.9 | 4e-21 | 30/49 (SHP-77, J82, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.425×** | -9.9 | 4e-21 | 44/49 (MIA PaCa-2, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.470×** | -8.7 | 2e-16 | 32/48 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.718×** | -7.3 | 2e-11 | 31/48 (SW480, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.732×** | -6.8 | 4e-10 | 31/48 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.744×** | -6.5 | 4e-09 | 30/48 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.754×** | -6.2 | 2e-08 | 24/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **0.761×** | -6.0 | 8e-08 | 29/48 (SW 1271, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **0.766×** | -5.9 | 2e-07 | 28/48 (NCI-H2030, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.753×** | -5.8 | 3e-07 | 28/48 (HEC-1-A, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.771×** | -5.7 | 4e-07 | 26/48 (BT-474, H4, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.847× | -5.1 | 8e-06 | 13/49 (KATO III, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.793×** | -5.1 | 1e-05 | 25/48 (NCI-H2030, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8140. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 85.3 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -26.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.266× (z -17.6) |
| [[HEC-1-A (line)]] | alt | 147 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -17.2) |
| [[MIA PaCa-2 (line)]] | alt | 86.5 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -27.9) |
| [[NCI-H23 (line)]] | alt | 136 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0972× (z -27.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.505× (z -11.8) |
| [[A-427 (line)]] | wt | 106 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0898× (z -30.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.567× (z -10.4) |
| [[A498 (line)]] | wt | 128 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -24.7) |
| [[HS-578T (line)]] | alt | 53.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -13.0) |
| [[NCI-H2030 (line)]] | alt | 77.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -12.8) |
| [[PANC-1 (line)]] | alt | 91.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.487× (z -11.8) |
| [[SNU-1 (line)]] | wt | 126 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -15.6) |
| [[SW480 (line)]] | alt | 110 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -15.0) |
| [[A-172 (line)]] | wt | 73.7 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.226× (z -14.8) |
| [[HOP62 (line)]] | alt | 65.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -18.3) |
| [[J82 (line)]] | alt | 139 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 0.5 µM 0.530× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 78.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -16.2) |
| [[NCI-H1573 (line)]] | alt | 44.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -16.4) |
| [[SW48 (line)]] | wt | 106 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -13.2) |
| [[A549 (line)]] | wt | 91.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.353× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.416× (z -11.1) |
| [[C-33 A (line)]] | alt | 146 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -14.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 55.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -20.6) |
| [[RPMI-7951 (line)]] | alt | 43.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -12.2) |
| [[SK-MEL-2 (line)]] | alt | 85.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.451× (z -11.5) |
| [[C32 (line)]] | wt | 59.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.305× (z -10.7) |
| [[COLO 205 (line)]] | alt | 45.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -11.6) |
| [[H4 (line)]] | wt | 62.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0226× (z -27.6) |
| [[HCT15 (line)]] | alt | 108 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.512× (z -8.7) |
| [[LS 180 (line)]] | wt | 77.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -19.8) |
| [[SHP-77 (line)]] | alt | 102 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -18.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 68.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -13.2) |
| [[SW1417 (line)]] | alt | 93.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 43.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -12.3) |
| [[CHP-212 (line)]] | wt | 48.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.117× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 49.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -12.1) |
| [[HT-29 (line)]] | alt | 80.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -12.1) |
| [[KATO III (line)]] | alt | 68.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 48.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.362× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 42.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -14.0) |
| [[SW 1271 (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0840× (z -12.2) ⚠ transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 39.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -9.4) |
| [[AN3 CA (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8140), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANCA]] | +0.72 | +0.76 / +0.73 | both halves | 7e-06 | same gene group; pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 999 |
| [[MELK]] | +0.71 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[MYO19]] | +0.71 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[POLE2]] | +0.70 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[CDC7]] | +0.70 | +0.74 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[WDR76]] | +0.68 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[MIR924HG]] | +0.68 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[DNA2]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 | STRING 508 |
| [[MMS22L]] | +0.67 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[DSCC1]] | +0.66 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[DTL]] | +0.66 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[ZNF367]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP4B]] | -0.58 | -0.62 / -0.57 | both halves | 9e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises FANCC's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.81× lower at baseline in the lines without E2F2 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[NT5M]] | B | NT5M activity raises FANCC's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.75× lower at baseline in the lines without NT5M | 0.013 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[NT5M]] | B | NT5M activity strengthens FANCC's drug response | lines that do not express NT5M (7) vs lines expressing it (42) | the lines without NT5M respond 0.58× as strongly (z diff +2.42); strongest at Dinaciclib 0.5 µM: 1.15x vs 0.62x (z diff +5.7) | 0.033 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG; target measured in part of the lines; artifact flags |
| [[GBX2-AS1]] | B | GBX2-AS1 activity raises FANCC's level | lines that do not express GBX2-AS1 (13) vs lines expressing it (37) | 1.35× lower at baseline in the lines without GBX2-AS1 | 0.090 | ⚠ within organs, on part of the lines; also absent: ANTXR1, KCNK13, TTC7B |
| [[CENPP]] | C | CENPP activity raises FANCC's level | lines that do not express CENPP (4) vs lines expressing it (46) | 2.25× lower at baseline in the lines without CENPP | 0.023 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises FANCC's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.97× lower at baseline in the lines without DSCC1 | 0.030 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.671). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-31.8, -47.0); signed map (-35.6, -44.3). **Vector** length 109, 31.5% of its response variance represented; |z| ≥ 3 in 1,107 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.53 to 28); *DNA Replication* (reactome, mean cos +0.53 to 40); *E2F G1/S* (control, mean cos +0.52 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.1 | +1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.0 | +1.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +5.2 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +4.9 | -3.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +1.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +0.1 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +2.1 | +3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +0.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +0.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -14.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | -4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.4 | -23.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.3 | -3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.1 | -10.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -8.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.3 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -5.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | FA complementation group C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.32 — chr9:95,099,054-95,426,796 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FAC, FA3; previously FACC |
| Gene groups (HGNC) | FA complementation groups; FA core complex |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 8 pathways, smallest: Fanconi Anemia Pathway; TP53 Regulates Transcription of DNA Repair Genes; PKR-mediated signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00597](https://www.uniprot.org/uniprotkb/Q00597) (Fanconi anemia group C protein):

> DNA repair protein that may operate in a postreplication repair or a cell cycle checkpoint function. May be implicated in interstrand DNA cross-link repair and in the maintenance of normal chromosome stability. Upon IFNG induction, may facilitate STAT1 activation by recruiting STAT1 to IFNGR1.

**Summary**, from NCBI Gene [2176](https://www.ncbi.nlm.nih.gov/gene/2176):

> The Fanconi anemia complementation group (FANC) currently includes FANCA, FANCB, FANCC, FANCD1 (also called BRCA2), FANCD2, FANCE, FANCF, FANCG, FANCI, FANCJ (also called BRIP1), FANCL, FANCM and FANCN (also called PALB2). The previously defined group FANCH is the same as FANCA. Fanconi anemia is a genetically heterogeneous recessive disorder characterized by cytogenetic instability, hypersensitivity to DNA crosslinking agents, increased chromosomal breakage, and defective DNA repair. The …

**Accessions** — [HGNC:3584](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3584) · Entrez [2176](https://www.ncbi.nlm.nih.gov/gene/2176) · UniProt [Q00597](https://www.uniprot.org/uniprotkb/Q00597) · Ensembl [ENSG00000158169](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158169)

## Data

Gene col 8140: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8140); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8140, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8140]; `tensor/DDL_lfc|DDL_z.npy` [8140]; `embed/gene_vectors.npy` [8140]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8140 or target_col == 8140). Every well: [[FANCC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FANCC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
