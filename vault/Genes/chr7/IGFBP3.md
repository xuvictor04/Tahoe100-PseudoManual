---
symbol: "IGFBP3"
type: "gene"
col: 7111
ensembl_id: "ENSG00000146674"
name: "insulin like growth factor binding protein 3"
location: "7p12.3"
module: 13
arm: "+"
pooled_cpm: 617.81
n_lines_expressing: 30
n_dd_up: 0
n_dd_down: 78
n_dd_up_clean: 0
n_dd_down_clean: 63
in_vector_space: true
direction_upstream: 14
direction_downstream: 24
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# IGFBP3

*insulin like growth factor binding protein 3* — 7p12.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Trametinib (drug)]] 0.5 µM in 1 line (HEC-1-A 2.18×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (Panc 03.27 2.76×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 78 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.105× (z -32.9, q 0e+00, down in 27 of 28 measured lines) ⚠ position correction uncertain. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.106× (z -22.3, q 0e+00, down in 28 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LOXL2]] (+0.73, fdr 7e-06), [[SETBP1]] (+0.60, fdr 7e-06), [[MAF]] (+0.59, fdr 1e-05); moves opposite to [[STXBP5]] (-0.54, fdr 4e-05), [[LTBR]] (-0.54, fdr 4e-05), [[FOXC2]] (-0.51, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[SMOX]] → it (grade B ⚠); 24 go from it, the strongest it → [[LUCAT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7111.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Trametinib (drug)]] 0.5 µM in 1 line (HEC-1-A 2.18×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (Panc 03.27 2.76×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rimonabant (drug)]] 0.5 µM |  | 1.37× | +3.3 | 0.32 | 20/28 (AsPC-1, A498, …) | inconsistent across doses | position effect removed |
| [[Rifaximin (drug)]] 0.5 µM |  | 1.34× | +3.0 | 0.32 | 19/28 (SW 900, A498, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 79 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 78 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7111.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | **0.105×** | -32.9 | 0e+00 | 27/28 (H4, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.106×** | -22.3 | 0e+00 | 28/28 (H4, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ position correction uncertain | **0.175×** | -18.0 | 0e+00 | 27/28 (H4, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.334×** | -15.9 | 0e+00 | 26/29 (NCI-H1792, SNU-423, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.237×** | -14.8 | 0e+00 | 28/28 (SW48, A-172, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.292×** | -12.6 | 1e-34 | 28/28 (NCI-H1792, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.317×** | -11.8 | 3e-30 | 28/28 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.320×** | -11.3 | 1e-27 | 26/28 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.335×** | -11.2 | 2e-27 | 28/28 (A-172, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.329×** | -11.0 | 2e-26 | 27/27 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.350×** | -10.8 | 2e-25 | 27/28 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.353×** | -10.7 | 4e-25 | 25/28 (SNU-423, H4, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.362×** | -10.4 | 8e-24 | 26/28 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.362×** | -9.9 | 3e-21 | 28/28 (H4, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~3% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.393×** | -9.6 | 3e-20 | 26/28 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.428×** | -8.7 | 1e-16 | 23/28 (HOP62, NCI-H1573, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.436×** | -8.5 | 6e-16 | 27/28 (COLO 205, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.565×** | -8.3 | 4e-15 | 22/28 (J82, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.449×** | -8.2 | 6e-15 | 23/28 (NCI-H1573, A498, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.580×** | -7.9 | 8e-14 | 23/28 (A498, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.485×** | -7.4 | 3e-12 | 26/28 (NCI-H460, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.71 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7111. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 574 | 0 | 44 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0990× (z -25.6) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.0371× (z -24.8) |
| [[H4 (line)]] | wt | 2,494 | 0 | 37 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0102× (z -50.9) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.0139× (z -32.2) |
| [[NCI-H1573 (line)]] | alt | 487 | 0 | 32 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0730× (z -31.3) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.0558× (z -23.5) |
| [[A498 (line)]] | wt | 1,449 | 0 | 27 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -21.5) ⚠ position correction uncertain · without an alert: [[Triamcinolone (drug)]] 0.5 µM 0.115× (z -18.9) |
| [[NCI-H1792 (line)]] | alt | 789 | 0 | 27 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0397× (z -35.9) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.0190× (z -29.9) |
| [[HS-578T (line)]] | alt | 4,956 | 0 | 23 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0333× (z -34.8) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.0512× (z -20.7) |
| [[NCI-H460 (line)]] | wt | 774 | 0 | 23 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -26.0) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.0416× (z -24.8) |
| [[C32 (line)]] | wt | 1,275 | 0 | 22 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0460× (z -28.8) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.0280× (z -22.7) |
| [[SNU-423 (line)]] | alt | 755 | 0 | 22 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0367× (z -36.2) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.0441× (z -23.2) |
| [[A-172 (line)]] | wt | 1,794 | 0 | 21 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0304× (z -33.1) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.0246× (z -23.9) |
| [[NCI-H2347 (line)]] | alt | 719 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0961× (z -23.9) ⚠ position correction uncertain · without an alert: [[Belinostat (drug)]] 5 µM 0.155× (z -13.4) |
| [[SK-MEL-2 (line)]] | alt | 367 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0747× (z -24.1) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.0467× (z -19.3) |
| [[COLO 205 (line)]] | alt | 237 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -15.6) ⚠ position correction uncertain · without an alert: [[Belinostat (drug)]] 5 µM 0.131× (z -13.3) |
| [[J82 (line)]] | alt | 1,400 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0825× (z -25.2) ⚠ position correction uncertain · without an alert: [[Selinexor (drug)]] 5 µM 0.222× (z -15.2) |
| [[A549 (line)]] | wt | 1,212 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0635× (z -26.3) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.0603× (z -18.2) |
| [[CFPAC-1 (line)]] | alt | 1,364 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -23.2) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -17.0) |
| [[SW480 (line)]] | alt | 172 | 0 | 10 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0701× (z -18.4) |
| [[HEC-1-A (line)]] | alt | 621 | 1 | 8 (4 ⚠) | [[Trametinib (drug)]] 0.5 µM 2.18× (z +8.7) | [[Harringtonine (drug)]] 5 µM 0.0719× (z -23.2) |
| [[RPMI-7951 (line)]] | alt | 392 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -17.8) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -15.5) |
| [[SW 900 (line)]] | alt | 195 | 0 | 9 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.160× (z -11.8) |
| [[SW48 (line)]] | wt | 359 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0865× (z -19.5) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.0367× (z -17.9) |
| [[SW 1271 (line)]] | alt | 873 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0840× (z -17.3) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.122× (z -14.6) |
| [[AsPC-1 (line)]] | alt | 1,574 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -27.5) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.108× (z -19.3) |
| [[NCI-H2030 (line)]] | alt | 558 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0742× (z -25.9) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.149× (z -12.9) |
| [[CHP-212 (line)]] | wt | 257 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -12.8) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.132× (z -9.1) |
| [[SW 1088 (line)]] | alt | 3,207 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0435× (z -21.2) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.0271× (z -16.6) |
| [[LOX-IMVI (line)]] | wt | 161 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -15.4) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.103× (z -14.2) |
| [[Panc 03.27 (line)]] | alt | 333 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 28.3 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 88.8 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 55.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 50.2 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 51.1 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 153 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 60.8 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 46.3 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 86.5 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 36.0 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 77.3 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 60.0 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 546 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 47.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 417 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.0 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 75.0 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 40.1 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 32.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 77.5 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 50.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7111), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LOXL2]] | +0.73 | +0.70 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 551 |
| [[SETBP1]] | +0.60 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[MAF]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[GJA1]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[PTGS2]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP; STRING 602 |
| [[LINC01411]] | +0.59 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[ADAM19]] | +0.57 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[COL15A1]] | +0.56 | +0.48 / +0.54 | both halves | 2e-05 | pathway: HALLMARK_MYOGENESIS |
| [[AIM2]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[CRLF2]] | +0.56 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[NAV1]] | +0.56 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[NDNF]] | +0.56 | +0.49 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STXBP5]] | -0.54 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[LTBR]] | -0.54 | -0.40 / -0.46 | both halves | 4e-05 |  |
| [[FOXC2]] | -0.51 | -0.47 / -0.46 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[SLC25A13]] | -0.50 | -0.52 / -0.45 | both halves | 3e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[MT1M]] | -0.50 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[FGD4]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[HSPBAP1]] | -0.48 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ARMC8]] | -0.47 | -0.51 / -0.43 | both halves | 4e-05 |  |
| [[MAOA]] | -0.47 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[CCND3]] | -0.46 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[TAF8]] | -0.46 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[RIPOR2]] | -0.45 | -0.48 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 5, C 9. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMOX]] | B | SMOX activity raises IGFBP3's level | lines that do not express SMOX (6) vs lines expressing it (44) | 6.71× lower at baseline in the lines without SMOX | 0.010 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[ADAM19]] | B | ADAM19 activity raises IGFBP3's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 4.25× lower at baseline in the lines without ADAM19 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[LTBR]] | B | LTBR activity raises IGFBP3's level | lines that do not express LTBR (8) vs lines expressing it (42) | 1.73× lower at baseline in the lines without LTBR | 0.075 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |
| [[NHS]] | B | NHS activity raises IGFBP3's level | lines that do not express NHS (17) vs lines expressing it (33) | 3.73× lower at baseline in the lines without NHS | 0.095 | ⚠ within organs, on part of the lines; also absent: ANKRD29, WNT7B, ABCC3 |
| [[FOXC2]] | B | FOXC2 activity raises IGFBP3's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 3.88× lower at baseline in the lines without FOXC2 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT |
| [[MAF]] | C | MAF activity raises IGFBP3's level | lines that do not express MAF (27) vs lines expressing it (23) | 7.50× lower at baseline in the lines without MAF | 0.007 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1; co-absent with the target |
| [[ADAMTS9-AS2]] | C | ADAMTS9-AS2 activity raises IGFBP3's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 4.49× lower at baseline in the lines without ADAMTS9-AS2 | 0.031 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2; co-absent with the target |
| [[CRLF2]] | C | CRLF2 activity raises IGFBP3's level | lines that do not express CRLF2 (35) vs lines expressing it (15) | 4.39× lower at baseline in the lines without CRLF2 | 0.039 | ⚠ within organs, on part of the lines; also absent: PAK3, RSPO3, FENDRR; co-absent with the target |
| [[PTHLH]] | C | PTHLH activity raises IGFBP3's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 4.96× lower at baseline in the lines without PTHLH | 0.052 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1; co-absent with the target |
| [[STAC]] | C | STAC activity raises IGFBP3's level | lines that do not express STAC (25) vs lines expressing it (25) | 5.51× lower at baseline in the lines without STAC | 0.062 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11; co-absent with the target |
| [[ADAM12]] | C | ADAM12 activity raises IGFBP3's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 6.61× lower at baseline in the lines without ADAM12 | 0.063 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1; co-absent with the target |
| [[CFAP20DC]] | C | CFAP20DC activity raises IGFBP3's level | lines that do not express CFAP20DC (16) vs lines expressing it (34) | 4.35× lower at baseline in the lines without CFAP20DC | 0.065 | ⚠ within organs, on part of the lines; also absent: RGS17, CHST11, WDR17; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 13, C 11. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LUCAT1]] | B | IGFBP3 activity raises LUCAT1's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 3.11× lower at baseline in the lines without IGFBP3 | 0.010 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF |
| [[FAM107B]] | B | IGFBP3 activity raises FAM107B's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 2.21× lower at baseline in the lines without IGFBP3 | 0.028 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF |
| [[MANCR]] | B | IGFBP3 activity raises MANCR's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 2.38× lower at baseline in the lines without IGFBP3 | 0.038 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF |
| [[IL1RAP]] | B | IGFBP3 activity raises IL1RAP's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 2.53× lower at baseline in the lines without IGFBP3 | 0.040 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF |
| [[SMOX]] | B | IGFBP3 activity raises SMOX's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 2.07× lower at baseline in the lines without IGFBP3 | 0.046 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF |
| [[LTBR]] | B | IGFBP3 activity raises LTBR's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 1.19× lower at baseline in the lines without IGFBP3 | 0.067 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF |
| [[RARA]] | B | IGFBP3 activity raises RARA's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 1.92× lower at baseline in the lines without IGFBP3 | 0.067 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF |
| [[UBA6]] | B | IGFBP3 activity raises UBA6's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 1.33× lower at baseline in the lines without IGFBP3 | 0.071 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF |
| [[KRT7]] | B | IGFBP3 activity raises KRT7's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 2.19× lower at baseline in the lines without IGFBP3 | 0.078 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF |
| [[HSPBAP1]] | B | IGFBP3 activity lowers HSPBAP1's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 1.23× higher at baseline in the lines without IGFBP3 | 0.088 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF |
| [[LARP1]] | B | IGFBP3 activity lowers LARP1's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 1.25× higher at baseline in the lines without IGFBP3 | 0.089 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF |
| cells under [[Niclosamide (olamine) (drug)]] 5 µM | B | IGFBP3 activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express IGFBP3 (20) vs lines expressing it (28) | the lines without IGFBP3: 0.73× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.544). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.3, 17.8); signed map (21.6, 51.6). **Vector** length 124, 44.1% of its response variance represented; |z| ≥ 3 in 1,887 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | -15.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.3 | +0.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.0 | -11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.9 | -1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.9 | +0.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.8 | +0.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | -0.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | +0.1 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -6.4 | -7.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -6.4 | -4.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -6.2 | -5.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -6.1 | -8.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -6.0 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | insulin like growth factor binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p12.3 — chr7:45,912,245-45,921,874 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IBP3, BP-53 |
| Gene groups (HGNC) | Insulin like growth factor binding proteins |
| Hallmark sets | MYOGENESIS, KRAS_SIGNALING_UP, GLYCOLYSIS, HYPOXIA, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 5 pathways, smallest: TP53 Regulates Transcription of Death Receptors and Ligands; TP53 Regulates Transcription of Cell Death Genes; Post-translational protein phosphorylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P17936](https://www.uniprot.org/uniprotkb/P17936) (Insulin-like growth factor-binding protein 3):

> Multifunctional protein that plays a critical role in regulating the availability of IGFs such as IGF1 and IGF2 to their receptors and thereby regulates IGF-mediated cellular processes including proliferation, differentiation, and apoptosis in a cell-type specific manner. Also exhibits IGF-independent antiproliferative and apoptotic effects mediated by its receptor TMEM219/IGFBP-3R. Inhibits the positive effect of humanin on insulin sensitivity. Promotes testicular germ cell apoptosis. Acts via …

**Summary**, from NCBI Gene [3486](https://www.ncbi.nlm.nih.gov/gene/3486):

> This gene is a member of the insulin-like growth factor binding protein (IGFBP) family and encodes a protein with an IGFBP domain and a thyroglobulin type-I domain. The protein forms a ternary complex with insulin-like growth factor acid-labile subunit (IGFALS) and either insulin-like growth factor (IGF) I or II. In this form, it circulates in the plasma, prolonging the half-life of IGFs and altering their interaction with cell surface receptors. Alternate transcriptional splice variants, …

**Accessions** — [HGNC:5472](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5472) · Entrez [3486](https://www.ncbi.nlm.nih.gov/gene/3486) · UniProt [P17936](https://www.uniprot.org/uniprotkb/P17936) · Ensembl [ENSG00000146674](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146674)

## Data

Gene col 7111: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7111); `tables/drug_effects.parquet` (81 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7111, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7111]; `tensor/DDL_lfc|DDL_z.npy` [7111]; `embed/gene_vectors.npy` [7111]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7111 or target_col == 7111). Every well: [[IGFBP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGFBP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
