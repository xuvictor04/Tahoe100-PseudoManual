---
symbol: "RECQL5"
type: "gene"
col: 2952
ensembl_id: "ENSG00000108469"
name: "RecQ like helicase 5"
location: "17q25"
module: 23
arm: "+"
pooled_cpm: 24.73
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 23
n_dd_up_clean: 4
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# RECQL5

*RecQ like helicase 5* — 17q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.91× (z +17.6, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.429× (z -16.2, q 0e+00, down in 39 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.456× (z -15.1, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM39]] (+0.75, fdr 7e-06), [[ACAD9]] (+0.73, fdr 7e-06), [[SNIP1]] (+0.70, fdr 1e-05); moves opposite to [[SOAT1]] (-0.67, fdr 7e-06), [[BTBD3]] (-0.62, fdr 7e-06), [[SLC23A2]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2952.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +17.6 | 0e+00 | 46/48 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +8.4 | 9e-15 | 30/47 (SNU-423, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +6.0 | 3e-07 | 23/48 (Panc 03.27, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +5.6 | 2e-06 | 23/47 (LoVo, Panc 03.27, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.17× | +4.2 | 0.003 | 11/48 (J82, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.16× | +4.0 | 0.006 | 8/48 (NCI-H460, H4, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.18× | +3.1 | 0.14 | 11/48 (AsPC-1, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.16 | 12/48 (HOP62, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2952.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.429×** | -16.2 | 0e+00 | 39/46 (hTERT-HPNE, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.427×** | -15.7 | 0e+00 | 37/44 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.456×** | -15.1 | 0e+00 | 42/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.482×** | -14.0 | 3e-42 | 30/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.657×** | -11.4 | 7e-28 | 45/48 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.558×** | -11.2 | 6e-27 | 34/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.577×** | -10.5 | 6e-24 | 29/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.604×** | -9.3 | 1e-18 | 24/35 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.646×** | -8.4 | 3e-15 | 29/47 (H4, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.660×** | -7.9 | 1e-13 | 31/48 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.687×** | -6.6 | 2e-09 | 20/38 (KATO III, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.717×** | -6.3 | 1e-08 | 22/47 (A549, HEC-1-A, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.725×** | -6.2 | 3e-08 | 28/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.757×** | -5.1 | 1e-05 | 20/47 (NCI-H1792, H4, …) | two highest doses | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.766×** | -5.1 | 1e-05 | 19/48 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.785×** | -4.6 | 1e-04 | 18/47 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.854× | -4.2 | 8e-04 | 15/48 (LoVo, CHP-212, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.739×** | -4.1 | 0.001 | 17/45 (HCT15, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.697×** | -3.6 | 0.008 | 11/48 (AsPC-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cilostazol (drug)]] 0.05 µM |  | **0.828×** | -3.3 | 0.022 | 8/47 (NCI-H1792, BT-474, …) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 5 µM |  | 0.887× | -3.2 | 0.030 | 7/48 (HepG2/C3A, RKO, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.738×** | -3.0 | 0.052 | 9/46 (A549, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2952. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 38.7 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.191× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.243× (z -14.1) |
| [[SW480 (line)]] | alt | 26.3 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +10.1) | [[Digitoxin (drug)]] 0.5 µM 0.300× (z -13.0) |
| [[H4 (line)]] | wt | 32.6 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.105× (z -12.1) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.162× (z -10.1) |
| [[HOP62 (line)]] | alt | 23.7 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +10.8) | [[Digitoxin (drug)]] 5 µM 0.258× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.352× (z -9.1) |
| [[KATO III (line)]] | alt | 42.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.271× (z -12.1) |
| [[LoVo (line)]] | wt | 23.5 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.135× (z -16.2) ⚠ toxic · without an alert: [[Tucidinostat (drug)]] 5 µM 0.455× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 27.5 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.237× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.238× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 18.1 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.340× (z -9.5) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.367× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 22.7 | 0 | 4 (3 ⚠) | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0437× (z -16.6) |
| [[Hs 766T (line)]] | wt | 23.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[TAK-733 (drug)]] 5 µM 0.0673× (z -8.6) |
| [[J82 (line)]] | alt | 21.9 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.273× (z -9.9) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.339× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 34.1 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.247× (z -10.0) ⚠ toxic |
| [[SW1417 (line)]] | alt | 22.5 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +9.7) | [[Lonafarnib (drug)]] 5 µM 0.0820× (z -9.3) ⚠ toxic |
| [[A-427 (line)]] | wt | 29.8 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.152× (z -15.3) ⚠ toxic · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -8.8) |
| [[A498 (line)]] | wt | 32.1 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.264× (z -11.3) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 47.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -9.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 30.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.211× (z -9.4) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 18.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.174× (z -11.0) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 20.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.244× (z -10.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 33.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 27.3 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.15× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -12.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 24.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 21.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 28.6 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.127× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 25.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +10.1) | — |
| [[HepG2_C3A (line)]] | wt | 20.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -11.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 22.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0352× (z -18.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 16.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.246× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 35.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.303× (z -9.6) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 14.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +8.5) | — |
| [[RKO (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.193× (z -8.9) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 17.3 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0534× (z -13.3) |
| [[AN3 CA (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2952), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM39]] | +0.75 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[ACAD9]] | +0.73 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[SNIP1]] | +0.70 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[PIGG]] | +0.69 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[NMNAT1]] | +0.69 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[LRRC41]] | +0.66 | +0.32 / +0.69 | both halves | 1e-04 |  |
| [[KIAA0753]] | +0.65 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[IKZF4]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[FOXRED1]] | +0.62 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[GLE1]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[SLC9A5]] | +0.61 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[DUS2]] | +0.61 | +0.46 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOAT1]] | -0.67 | -0.63 / -0.61 | both halves | 7e-06 |  |
| [[BTBD3]] | -0.62 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[SLC23A2]] | -0.62 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[TRAK1]] | -0.62 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[HMGN3]] | -0.61 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[ANOS1]] | -0.61 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[TMOD2]] | -0.58 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[EFR3A]] | -0.58 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[ALDH3A2]] | -0.58 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[ATP8A1]] | -0.57 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[CXADR]] | -0.57 | -0.34 / -0.63 | both halves | 1e-04 |  |
| [[PAFAH1B3]] | -0.57 | -0.58 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RECQL5's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PLPP2]] | B | PLPP2 activity raises RECQL5's level | lines that do not express PLPP2 (8) vs lines expressing it (42) | 1.16× lower at baseline in the lines without PLPP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: MAP3K21, C3orf52, REPS2 |
| [[TRIM58]] | B | TRIM58 activity raises RECQL5's level | lines that do not express TRIM58 (31) vs lines expressing it (19) | 1.18× lower at baseline in the lines without TRIM58 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000235749, MME, FGF20 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.434). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-6.0, 18.4); signed map (7.6, 0.9). **Vector** length 95.4, 22.1% of its response variance represented; |z| ≥ 3 in 1,138 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +17.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +5.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +3.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.2 | +4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.5 | +1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +1.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -11.3 | -11.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -8.5 | -7.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.4 | -5.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.7 | -15.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.5 | -3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | +0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | RecQ like helicase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25 — chr17:75,626,845-75,667,189 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RecQ5, FLJ90603 |
| Gene groups (HGNC) | RecQ like helicases |
| Matched by | ensembl_id |

**Function**, from UniProt [O94762](https://www.uniprot.org/uniprotkb/O94762) (ATP-dependent DNA helicase Q5):

> DNA helicase that plays an important role in DNA replication, transcription and repair. Probably unwinds DNA in a 3'-5' direction (Probable). Binds to the RNA polymerase II subunit POLR2A during transcription elongation and suppresses transcription-associated genomic instability. Also associates with POLR1A and enforces the stability of ribosomal DNA arrays. Plays an important role in mitotic chromosome separation after cross-over events and cell cycle progress. Mechanistically, removes RAD51 …

**Summary**, from NCBI Gene [9400](https://www.ncbi.nlm.nih.gov/gene/9400):

> The protein encoded by this gene is a helicase that is important for genome stability. The encoded protein also prevents aberrant homologous recombination by displacing RAD51 from ssDNA. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2011]

**Accessions** — [HGNC:9950](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9950) · Entrez [9400](https://www.ncbi.nlm.nih.gov/gene/9400) · UniProt [O94762](https://www.uniprot.org/uniprotkb/O94762) · Ensembl [ENSG00000108469](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108469)

## Data

Gene col 2952: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2952); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2952, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2952]; `tensor/DDL_lfc|DDL_z.npy` [2952]; `embed/gene_vectors.npy` [2952]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2952 or target_col == 2952). Every well: [[RECQL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RECQL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
