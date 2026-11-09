---
symbol: "GOLPH3"
type: "gene"
col: 3457
ensembl_id: "ENSG00000113384"
name: "golgi phosphoprotein 3"
location: "5p13.3"
module: 49
arm: "+"
pooled_cpm: 141.83
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 24
n_dd_up_clean: 4
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# GOLPH3

*golgi phosphoprotein 3* — 5p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.47× (z +8.2, q 2e-13, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.379× (z -20.4, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELP5]] (+0.61, fdr 1e-05), [[MPC1]] (+0.60, fdr 1e-05), [[SLC30A5]] (+0.58, fdr 1e-05); moves opposite to [[APP]] (-0.54, fdr 4e-04), [[PSMD14]] (-0.53, fdr 6e-05), [[DYNC1H1]] (-0.51, fdr 2e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3457.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +8.2 | 2e-13 | 36/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +5.3 | 4e-05 | 26/48 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +5.0 | 1e-04 | 26/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +4.8 | 3e-04 | 25/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +4.3 | 0.002 | 24/47 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.47×** | +4.2 | 0.002 | 27/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3457.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.379×** | -20.4 | 0e+00 | 48/48 (HT-29, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.373×** | -20.0 | 0e+00 | 40/44 (SHP-77, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.512×** | -19.9 | 0e+00 | 47/49 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.407×** | -18.9 | 0e+00 | 48/48 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.451×** | -16.8 | 0e+00 | 48/48 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.455×** | -16.5 | 0e+00 | 45/49 (A-427, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.589×** | -10.3 | 5e-23 | 38/45 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.620×** | -9.7 | 3e-20 | 44/48 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.640×** | -9.0 | 1e-17 | 41/50 (HT-29, HOP62, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.746×** | -8.7 | 1e-16 | 40/48 (A-172, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.662×** | -8.7 | 2e-16 | 41/48 (HT-29, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.804×** | -6.5 | 4e-09 | 30/48 (HS-578T, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.751×** | -6.0 | 8e-08 | 38/48 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.745×** | -6.0 | 1e-07 | 28/47 (HepG2/C3A, HT-29, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.821×** | -5.9 | 2e-07 | 29/48 (HT-29, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.773×** | -5.4 | 2e-06 | 35/48 (HOP62, CFPAC-1, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.778×** | -5.3 | 4e-06 | 28/48 (SNU-423, HOP62, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.798×** | -4.5 | 2e-04 | 29/48 (HOP62, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.808×** | -4.3 | 4e-04 | 24/48 (RKO, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3457. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 181 | 0 | 13 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -23.5) |
| [[HOP62 (line)]] | alt | 154 | 0 | 12 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.283× (z -17.8) |
| [[HT-29 (line)]] | alt | 181 | 0 | 12 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -21.5) |
| [[hTERT-HPNE (line)]] | wt | 131 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.244× (z -13.6) |
| [[SW 900 (line)]] | alt | 248 | 0 | 10 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -16.3) |
| [[CFPAC-1 (line)]] | alt | 162 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -14.1) |
| [[J82 (line)]] | alt | 205 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -18.1) |
| [[NCI-H2347 (line)]] | alt | 223 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -16.4) |
| [[PANC-1 (line)]] | alt | 105 | 2 | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.84× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.407× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.449× (z -11.6) |
| [[A-172 (line)]] | wt | 119 | 0 | 8 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -20.2) |
| [[A498 (line)]] | wt | 210 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -22.7) |
| [[SW480 (line)]] | alt | 116 | 2 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.13× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.373× (z -17.0) |
| [[HEC-1-A (line)]] | alt | 97.0 | 1 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.271× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.463× (z -11.6) |
| [[Hs 766T (line)]] | wt | 168 | 0 | 7 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -14.9) |
| [[LOX-IMVI (line)]] | wt | 110 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.293× (z -14.7) |
| [[NCI-H1792 (line)]] | alt | 188 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.277× (z -15.3) |
| [[Panc 03.27 (line)]] | alt | 140 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.316× (z -15.1) |
| [[SNU-423 (line)]] | alt | 110 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -14.8) |
| [[A549 (line)]] | wt | 128 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.293× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.327× (z -13.7) |
| [[AsPC-1 (line)]] | alt | 148 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -15.8) |
| [[H4 (line)]] | wt | 130 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -11.4) |
| [[LS 180 (line)]] | wt | 128 | 2 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.268× (z -16.0) |
| [[NCI-H1573 (line)]] | alt | 123 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.404× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 107 | 1 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.277× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.379× (z -12.2) |
| [[RPMI-7951 (line)]] | alt | 117 | 0 | 6 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -12.0) |
| [[SHP-77 (line)]] | alt | 210 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0420× (z -40.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -12.7) |
| [[A-427 (line)]] | wt | 138 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -24.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -12.0) |
| [[KATO III (line)]] | alt | 101 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -16.8) |
| [[LoVo (line)]] | wt | 165 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.351× (z -12.7) |
| [[NCI-H2030 (line)]] | alt | 155 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -10.1) |
| [[SW1417 (line)]] | alt | 152 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.331× (z -16.9) |
| [[COLO 205 (line)]] | alt | 143 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -14.4) |
| [[HepG2_C3A (line)]] | wt | 125 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -11.7) |
| [[BT-474 (line)]] | alt | 201 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.333× (z -13.1) |
| [[SW48 (line)]] | wt | 108 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.361× (z -9.4) |
| [[CHP-212 (line)]] | wt | 118 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -9.7) |
| [[HCT15 (line)]] | alt | 134 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 119 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.421× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.465× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 124 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -19.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 86.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 49.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -8.9) |
| [[C-33 A (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -12.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 79.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0889× (z -12.2) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 112 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 144 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3457), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELP5]] | +0.61 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[MPC1]] | +0.60 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[SLC30A5]] | +0.58 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[OSBP]] | +0.57 | +0.61 / +0.57 | both halves | 9e-06 | STRING 461 |
| [[CCDC9]] | +0.56 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[PDXDC2P-NPIPB14P]] | +0.56 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[INAFM1]] | +0.55 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[MYNN]] | +0.54 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[PRPF3]] | +0.53 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[RBM10]] | +0.53 | +0.32 / +0.61 | both halves | 2e-04 |  |
| [[TMEM216]] | +0.53 | +0.38 / +0.53 | both halves | 7e-05 |  |
| [[COG3]] | +0.53 | +0.59 / +0.48 | both halves | 2e-05 | STRING 466 |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APP]] | -0.54 | -0.25 / -0.61 | both halves | 4e-04 |  |
| [[PSMD14]] | -0.53 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[DYNC1H1]] | -0.51 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[GLS]] | -0.50 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[FKBP4]] | -0.50 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[HPRT1]] | -0.50 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[CCT5]] | -0.50 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[GLO1]] | -0.49 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[DST]] | -0.48 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[CAPN2]] | -0.48 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[PSMD2]] | -0.48 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[ASPH]] | -0.48 | -0.34 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GOLPH3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.447). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.9, -39.4); signed map (-52.8, 15.5). **Vector** length 92.3, 30.5% of its response variance represented; |z| ≥ 3 in 1,386 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.2 | +4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.4 | +0.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | +3.2 | -6.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.8 | +0.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.8 | +0.9 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.6 | -0.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.6 | +0.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.5 | +0.4 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.4 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -6.1 | -4.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.4 | -4.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.9 | -6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -8.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -4.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.1 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | golgi phosphoprotein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.3 — chr5:32,124,716-32,174,319 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GPP34, GOPP1, MIDAS, Vps74 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4A6](https://www.uniprot.org/uniprotkb/Q9H4A6) (Golgi phosphoprotein 3):

> Phosphatidylinositol-4-phosphate-binding protein that links Golgi membranes to the cytoskeleton and may participate in the tensile force required for vesicle budding from the Golgi. Thereby, may play a role in Golgi membrane trafficking and could indirectly give its flattened shape to the Golgi apparatus. May also bind to the coatomer to regulate Golgi membrane trafficking. May play a role in anterograde transport from the Golgi to the plasma membrane and regulate secretion. Has also been …

**Summary**, from NCBI Gene [64083](https://www.ncbi.nlm.nih.gov/gene/64083):

> The Golgi complex plays a key role in the sorting and modification of proteins exported from the endoplasmic reticulum. The protein encoded by this gene is a peripheral membrane protein of the Golgi stack and may have a regulatory role in Golgi trafficking. Several alternatively spliced transcript variants of this gene have been described, but the full-length nature of these variants has not been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15452](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15452) · Entrez [64083](https://www.ncbi.nlm.nih.gov/gene/64083) · UniProt [Q9H4A6](https://www.uniprot.org/uniprotkb/Q9H4A6) · Ensembl [ENSG00000113384](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113384)

## Data

Gene col 3457: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3457); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3457, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3457]; `tensor/DDL_lfc|DDL_z.npy` [3457]; `embed/gene_vectors.npy` [3457]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3457 or target_col == 3457). Every well: [[GOLPH3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOLPH3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
