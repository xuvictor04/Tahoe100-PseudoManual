---
symbol: "IRAK1BP1"
type: "gene"
col: 7077
ensembl_id: "ENSG00000146243"
name: "interleukin 1 receptor associated kinase 1 binding protein 1"
location: "6q14.1"
module: 17
arm: "+"
pooled_cpm: 16.62
n_lines_expressing: 48
n_dd_up: 22
n_dd_down: 16
n_dd_up_clean: 18
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# IRAK1BP1

*interleukin 1 receptor associated kinase 1 binding protein 1* — 6q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.57× (z +9.4, q 5e-18, up in 32 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.436× (z -12.2, q 2e-31, down in 34 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAAF4]] (+0.70, fdr 7e-06), [[NDUFAF5]] (+0.69, fdr 7e-06), [[ALKBH8]] (+0.68, fdr 7e-06); moves opposite to [[TRPV1]] (-0.61, fdr 8e-05), [[LINC01128]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PRKCA]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Lapatinib ditosylate (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7077.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.57×** | +9.4 | 5e-18 | 32/46 (RKO, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.82×** | +8.8 | 4e-16 | 33/45 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.75×** | +8.2 | 4e-14 | 29/45 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.66×** | +7.5 | 1e-11 | 34/45 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +7.2 | 7e-11 | 29/45 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +7.0 | 2e-10 | 30/45 (HEC-1-A, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +5.6 | 2e-06 | 18/40 (SW48, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.40×** | +5.0 | 4e-05 | 20/45 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.87×** | +4.8 | 8e-05 | 18/46 (HEC-1-A, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +4.5 | 4e-04 | 17/46 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +4.5 | 4e-04 | 14/27 (A498, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.34×** | +4.4 | 6e-04 | 17/45 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.005 | 16/45 (NCI-H23, SW480, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.014 | 12/45 (NCI-H460, HCT15, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.020 | 8/45 (SW480, BT-474, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.022 | 4/45 (NCI-H23, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.022 | 16/45 (HEC-1-A, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.030 | 14/45 (HEC-1-A, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7077.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.436×** | -12.2 | 2e-31 | 34/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.526×** | -9.4 | 1e-18 | 34/45 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.536×** | -9.2 | 1e-17 | 35/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.659×** | -8.7 | 7e-16 | 30/45 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.611×** | -7.2 | 5e-11 | 27/45 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.697×** | -5.3 | 1e-05 | 17/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.785×** | -5.0 | 4e-05 | 22/46 (SK-MEL-2, PANC-1, …) | rises with dose | composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.719×** | -4.8 | 9e-05 | 18/45 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.748×** | -4.3 | 0.001 | 17/45 (SW480, C32, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.748×** | -4.2 | 0.001 | 15/45 (H4, RPMI-7951, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.588×** | -4.1 | 0.002 | 14/44 (RPMI-7951, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.783×** | -3.6 | 0.017 | 20/43 (NCI-H460, C32, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.779×** | -3.5 | 0.019 | 12/43 (SHP-77, RKO, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.794×** | -3.4 | 0.030 | 18/45 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.800×** | -3.3 | 0.040 | 10/46 (J82, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.746×** | -3.1 | 0.078 | 8/46 (PANC-1, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7077. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 17.1 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -11.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.303× (z -10.2) |
| [[SW480 (line)]] | alt | 25.0 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.166× (z -16.2) |
| [[NCI-H23 (line)]] | alt | 48.6 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -11.0) |
| [[PANC-1 (line)]] | alt | 15.5 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.245× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 25.2 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.225× (z -10.1) |
| [[AN3 CA (line)]] | alt | 51.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0851× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Decitabine (drug)]] 0.5 µM 0.153× (z -8.6) |
| [[C32 (line)]] | wt | 15.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -8.7) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.192× (z -8.6) |
| [[RKO (line)]] | wt | 25.3 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0710× (z -15.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.164× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 20.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -14.9) ⚠ cell-cycle shift, explains ~64% of this change |
| [[HOP62 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -9.7) ⚠ cell-cycle shift, explains ~64% of this change |
| [[HT-29 (line)]] | alt | 5.21 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0814× (z -9.3) ⚠ transcription drop |
| [[LoVo (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -8.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 18.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 138 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0896× (z -9.6) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 51.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.302× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[SW 900 (line)]] | alt | 9.39 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.121× (z -8.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7077), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF4]] | +0.70 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[NDUFAF5]] | +0.69 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ALKBH8]] | +0.68 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[SLC25A12]] | +0.68 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[TTC5]] | +0.68 | +0.54 / +0.73 | both halves | 1e-05 |  |
| [[BBS5]] | +0.67 | +0.51 / +0.73 | both halves | 1e-05 |  |
| [[EHMT2]] | +0.66 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[MRPL19]] | +0.65 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[IFTAP]] | +0.65 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[MRPS31P4]] | +0.65 | +0.38 / +0.72 | both halves | 6e-05 |  |
| [[MRPL16]] | +0.65 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[ESD]] | +0.65 | +0.52 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRPV1]] | -0.61 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[LINC01128]] | -0.54 | -0.48 / -0.57 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKCA]] | B | PRKCA activity lowers IRAK1BP1's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 2.57× higher at baseline in the lines without PRKCA | 0.014 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[PKIG]] | B | PKIG activity raises IRAK1BP1's level | lines that do not express PKIG (6) vs lines expressing it (44) | 2.42× lower at baseline in the lines without PKIG | 0.044 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1 |
| [[SLC5A4-AS1]] | B | SLC5A4-AS1 activity raises IRAK1BP1's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 1.73× lower at baseline in the lines without SLC5A4-AS1 | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |
| [[TBC1D19]] | C | TBC1D19 activity raises IRAK1BP1's level | lines that do not express TBC1D19 (4) vs lines expressing it (46) | 2.89× lower at baseline in the lines without TBC1D19 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | C | IRAK1BP1's natural level lowers the cells' numbers under Lapatinib ditosylate 0.5 µM (makes them more sensitive) | IRAK1BP1's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.63 | 0.440 over the table, 0.072 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.737). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-24.3, -1.8); signed map (-23.6, -14.2). **Vector** length 81.2, 16.5% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.9 | +9.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +0.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.7 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +7.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | -0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +4.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.4 | +5.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +4.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -8.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -2.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -1.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.4 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -4.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.4 | -4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 1 receptor associated kinase 1 binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.1 — chr6:78,867,551-78,946,440 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AIP70, SIMPL |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VVH5](https://www.uniprot.org/uniprotkb/Q5VVH5) (Interleukin-1 receptor-associated kinase 1-binding protein 1):

> Component of the IRAK1-dependent TNFRSF1A signaling pathway that leads to NF-kappa-B activation and is required for cell survival. Acts by enhancing RELA transcriptional activity (By similarity).

**Summary**, from NCBI Gene [134728](https://www.ncbi.nlm.nih.gov/gene/134728):

> Predicted to enable signaling adaptor activity. Predicted to be involved in positive regulation of canonical NF-kappaB signal transduction. Predicted to be located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17368](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17368) · Entrez [134728](https://www.ncbi.nlm.nih.gov/gene/134728) · UniProt [Q5VVH5](https://www.uniprot.org/uniprotkb/Q5VVH5) · Ensembl [ENSG00000146243](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146243)

## Data

Gene col 7077: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7077); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7077, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7077]; `tensor/DDL_lfc|DDL_z.npy` [7077]; `embed/gene_vectors.npy` [7077]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7077 or target_col == 7077). Every well: [[IRAK1BP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IRAK1BP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
