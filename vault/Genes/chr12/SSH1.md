---
symbol: "SSH1"
type: "gene"
col: 1396
ensembl_id: "ENSG00000084112"
name: "slingshot protein phosphatase 1"
location: "12q24.11"
module: 84
arm: "+"
pooled_cpm: 121.06
n_lines_expressing: 48
n_dd_up: 0
n_dd_down: 24
n_dd_up_clean: 0
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# SSH1

*slingshot protein phosphatase 1* — 12q24.11

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 7 lines (NCI-H460 9.53×, RPMI-7951 11.6×, A549 8.47×, A498 5.60×, …; ⚠ cell-cycle shift, explains ~30% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HEC-1-A 2.08×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A498 2.19×); [[Auranofin (drug)]] 5 µM in 1 line (AsPC-1 2.76×).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.460× (z -23.0, q 0e+00, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPAS2]] (+0.59, fdr 9e-06), [[PHC2]] (+0.56, fdr 1e-05), [[UBASH3B]] (+0.51, fdr 3e-05); moves opposite to [[OCLN]] (-0.51, fdr 2e-04), [[TOX3]] (-0.50, fdr 3e-05), [[CD2AP]] (-0.49, fdr 4e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[ITGB3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1396.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 7 lines (NCI-H460 9.53×, RPMI-7951 11.6×, A549 8.47×, A498 5.60×, …; ⚠ cell-cycle shift, explains ~30% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HEC-1-A 2.08×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A498 2.19×); [[Auranofin (drug)]] 5 µM in 1 line (AsPC-1 2.76×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.82 | 17/46 (NCI-H460, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1396.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.460×** | -23.0 | 0e+00 | 42/46 (SK-MEL-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.537×** | -18.4 | 0e+00 | 38/47 (A549, SNU-423, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.524×** | -13.5 | 2e-39 | 39/46 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.576×** | -11.5 | 1e-28 | 37/46 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.576×** | -11.1 | 2e-26 | 33/46 (SK-MEL-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.595×** | -10.4 | 1e-23 | 26/43 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.608×** | -10.4 | 2e-23 | 32/47 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.615×** | -10.2 | 2e-22 | 36/46 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.631×** | -9.6 | 4e-20 | 34/46 (HOP62, SW 1271, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.665×** | -8.5 | 8e-16 | 37/46 (C32, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.662×** | -8.3 | 5e-15 | 32/45 (RKO, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.693×** | -7.6 | 1e-12 | 34/46 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.694×** | -7.6 | 1e-12 | 30/46 (LS 180, HOP62, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.691×** | -7.1 | 4e-11 | 28/44 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.716×** | -6.7 | 7e-10 | 28/48 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -5.6 | 7e-07 | 27/46 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.634×** | -5.0 | 2e-05 | 26/46 (RPMI-7951, A498, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.638×** | -4.9 | 3e-05 | 23/46 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.670×** | -4.4 | 3e-04 | 22/45 (A498, C32, …) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.826×** | -4.0 | 0.002 | 20/46 (C32, HEC-1-A, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1396. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 371 | 0 | 14 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -18.0) |
| [[HOP62 (line)]] | alt | 181 | 0 | 13 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -17.2) |
| [[SW 900 (line)]] | alt | 286 | 0 | 12 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0886× (z -18.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.282× (z -14.3) |
| [[MIA PaCa-2 (line)]] | alt | 145 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -25.8) |
| [[NCI-H460 (line)]] | wt | 123 | 1 (1 ⚠) | 10 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 9.53× (z +15.8) ⚠ cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -17.9) |
| [[PANC-1 (line)]] | alt | 224 | 1 (1 ⚠) | 9 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.24× (z +9.7) ⚠ cell-cycle shift, explains ~30% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -15.7) |
| [[RPMI-7951 (line)]] | alt | 251 | 1 (1 ⚠) | 9 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.6× (z +12.4) ⚠ cell-cycle shift, explains ~30% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -16.1) |
| [[SK-MEL-2 (line)]] | alt | 270 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -29.3) |
| [[A549 (line)]] | wt | 279 | 1 (1 ⚠) | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.47× (z +11.2) ⚠ cell-cycle shift, explains ~30% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -22.6) |
| [[HEC-1-A (line)]] | alt | 81.6 | 2 (1 ⚠) | 6 | [[Ixazomib citrate (drug)]] 0.5 µM 2.08× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -18.7) |
| [[A-172 (line)]] | wt | 99.7 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -15.9) |
| [[A498 (line)]] | wt | 160 | 2 (1 ⚠) | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.60× (z +10.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.19× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -15.3) |
| [[LoVo (line)]] | wt | 62.0 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -20.0) |
| [[SNU-1 (line)]] | wt | 86.6 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -12.2) |
| [[SW480 (line)]] | alt | 51.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -15.8) |
| [[NCI-H2030 (line)]] | alt | 163 | 1 (1 ⚠) | 4 | [[TAK-901 (drug)]] 5 µM 6.56× (z +9.1) ⚠ cell-cycle shift, explains ~30% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 102 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -16.4) |
| [[RKO (line)]] | wt | 105 | 0 | 5 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0685× (z -24.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.340× (z -14.4) |
| [[LS 180 (line)]] | wt | 53.9 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.344× (z -11.8) |
| [[NCI-H2347 (line)]] | alt | 119 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -17.8) |
| [[H4 (line)]] | wt | 130 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -9.2) |
| [[HCT15 (line)]] | alt | 106 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -11.8) |
| [[Hs 766T (line)]] | wt | 142 | 1 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.30× (z +9.4) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 5 µM 0.301× (z -12.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 183 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -13.6) |
| [[J82 (line)]] | alt | 109 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -15.2) |
| [[NCI-H1573 (line)]] | alt | 46.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -14.5) |
| [[SNU-423 (line)]] | alt | 155 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -27.1) |
| [[A-427 (line)]] | wt | 55.2 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.174× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 96.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -11.9) |
| [[HS-578T (line)]] | alt | 96.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -10.1) |
| [[KATO III (line)]] | alt | 38.6 | 1 (1 ⚠) | 1 | [[Bortezomib (drug)]] 0.05 µM 2.48× (z +8.6) ⚠ cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 79.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -13.3) |
| [[NCI-H1792 (line)]] | alt | 151 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -16.2) |
| [[Panc 03.27 (line)]] | alt | 61.8 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.478× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.512× (z -8.8) |
| [[AN3 CA (line)]] | alt | 63.7 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.186× (z -9.3) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 60.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.76× (z +8.8) | — |
| [[CHP-212 (line)]] | wt | 171 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -13.7) |
| [[HepG2_C3A (line)]] | wt | 52.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -9.8) |
| [[HT-29 (line)]] | alt | 39.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -8.9) |
| [[SHP-77 (line)]] | alt | 93.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -9.1) |
| [[SW 1271 (line)]] | alt | 198 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.115× (z -11.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 56.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -11.3) |
| [[BT-474 (line)]] | alt | 29.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 56.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1396), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPAS2]] | +0.59 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[PHC2]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 | same gene group |
| [[UBASH3B]] | +0.51 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[MIR100HG]] | +0.50 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[DGKG]] | +0.50 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[RASA3]] | +0.49 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[WWTR1]] | +0.49 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[STX1A]] | +0.48 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[SH3RF3]] | +0.48 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[OAF]] | +0.48 | +0.42 / +0.40 | both halves | 5e-05 |  |
| [[SPRY4]] | +0.47 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[SHC3]] | +0.47 | +0.48 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OCLN]] | -0.51 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[TOX3]] | -0.50 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[CD2AP]] | -0.49 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[KLF3-AS1]] | -0.48 | -0.50 / -0.36 | both halves | 9e-05 |  |
| [[POF1B]] | -0.48 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[MFSD6]] | -0.48 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[STX19]] | -0.47 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[ERBB2]] | -0.46 | -0.39 / -0.37 | both halves | 7e-05 | same gene group |
| [[MGAM2]] | -0.45 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[C4BPB]] | -0.44 | -0.28 / -0.48 | both halves | 3e-04 |  |
| [[FAM151B-DT]] | -0.44 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[ANXA4]] | -0.44 | -0.44 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB3]] | B | ITGB3 activity raises SSH1's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 2.13× lower at baseline in the lines without ITGB3 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[COL13A1]] | B | COL13A1 activity raises SSH1's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 2.06× lower at baseline in the lines without COL13A1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[NAV2]] | B | NAV2 activity raises SSH1's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 1.90× lower at baseline in the lines without NAV2 | 0.022 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1 |
| [[ARHGEF38]] | B | ARHGEF38 activity lowers SSH1's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 2.20× higher at baseline in the lines without ARHGEF38 | 0.022 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[MIR100HG]] | B | MIR100HG activity raises SSH1's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 2.16× lower at baseline in the lines without MIR100HG | 0.023 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[ROR1]] | B | ROR1 activity raises SSH1's level | lines that do not express ROR1 (14) vs lines expressing it (36) | 1.66× lower at baseline in the lines without ROR1 | 0.026 | ⚠ within organs, on part of the lines |
| [[LINC02253]] | B | LINC02253 activity lowers SSH1's level | lines that do not express LINC02253 (35) vs lines expressing it (15) | 1.80× higher at baseline in the lines without LINC02253 | 0.032 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02058, ENSG00000289349 |
| [[FAM20C]] | B | FAM20C activity raises SSH1's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 1.73× lower at baseline in the lines without FAM20C | 0.047 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1 |
| [[POF1B]] | B | POF1B activity lowers SSH1's level | lines that do not express POF1B (34) vs lines expressing it (16) | 1.91× higher at baseline in the lines without POF1B | 0.050 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31 |
| [[TMC4]] | B | TMC4 activity lowers SSH1's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 1.77× higher at baseline in the lines without TMC4 | 0.059 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[SH3RF3]] | B | SH3RF3 activity raises SSH1's level | lines that do not express SH3RF3 (14) vs lines expressing it (36) | 1.48× lower at baseline in the lines without SH3RF3 | 0.067 | ⚠ within organs, on part of the lines; also absent: DCLK2, OSBPL6, FHL1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.530). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.7, 5.1); signed map (6.8, 48.9). **Vector** length 91.8, 23.9% of its response variance represented; |z| ≥ 3 in 1,397 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.8 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.7 | +1.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | +4.5 | +2.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | +2.8 | -3.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.3 | -8.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +0.7 |
|  | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM |  | +1.4 | +2.6 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | +1.3 | +1.3 |
|  | [[Olanzapine (drug)]] 5 µM |  | +1.3 | +1.6 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.9 | -10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.4 | -10.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.4 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.1 | -7.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.7 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.3 | -2.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.3 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.1 | -3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.0 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | slingshot protein phosphatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:108,778,191-108,857,590 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1298, SSH1L |
| Gene groups (HGNC) | Slingshot protein phosphatases; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WYL5](https://www.uniprot.org/uniprotkb/Q8WYL5) (Protein phosphatase Slingshot homolog 1):

> Protein phosphatase which regulates actin filament dynamics. Dephosphorylates and activates the actin binding/depolymerizing factor cofilin, which subsequently binds to actin filaments and stimulates their disassembly. Inhibitory phosphorylation of cofilin is mediated by LIMK1, which may also be dephosphorylated and inactivated by this protein.

**Summary**, from NCBI Gene [54434](https://www.ncbi.nlm.nih.gov/gene/54434):

> The protein encoded by this gene belongs to the slingshot homolog (SSH) family of phosphatases, which regulate actin filament dynamics. The SSH proteins dephosphorylate and activate the actin binding/depolymerizing factor cofilin, which subsequently binds to actin filaments and stimulates their disassembly. Cofilin is inactivated by kinases such as LIM domain kinase-1 (LIMK1), which may also be dephosphorylated and inactivated by SSH proteins. The SSH family thus appears to play a role in actin …

**Accessions** — [HGNC:30579](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30579) · Entrez [54434](https://www.ncbi.nlm.nih.gov/gene/54434) · UniProt [Q8WYL5](https://www.uniprot.org/uniprotkb/Q8WYL5) · Ensembl [ENSG00000084112](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084112)

## Data

Gene col 1396: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1396); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1396, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1396]; `tensor/DDL_lfc|DDL_z.npy` [1396]; `embed/gene_vectors.npy` [1396]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1396 or target_col == 1396). Every well: [[SSH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SSH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
