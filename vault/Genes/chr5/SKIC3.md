---
symbol: "SKIC3"
type: "gene"
col: 12639
ensembl_id: "ENSG00000198677"
name: "SKI3 subunit of superkiller complex"
location: "5q15"
module: 17
arm: "+"
pooled_cpm: 158.67
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 16
n_dd_up_clean: 8
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# SKIC3

*SKI3 subunit of superkiller complex* — 5q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.57× (z +10.0, q 9e-21, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.550× (z -18.6, q 0e+00, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POT1]] (+0.76, fdr 1e-05), [[PAPSS1]] (+0.73, fdr 7e-06), [[NIPSNAP1]] (+0.72, fdr 7e-06); moves opposite to [[TLNRD1]] (-0.69, fdr 7e-06), [[SPON1-AS1]] (-0.64, fdr 1e-04), [[DDX5]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12639.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +10.0 | 9e-21 | 39/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +9.1 | 4e-17 | 40/48 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +8.0 | 2e-13 | 37/48 (LoVo, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +7.4 | 2e-11 | 32/48 (NCI-H2347, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.33×** | +6.3 | 2e-08 | 30/49 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +5.9 | 4e-07 | 27/44 (SW 900, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +5.0 | 5e-05 | 18/48 (AsPC-1, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +4.8 | 1e-04 | 29/48 (LoVo, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.16× | +4.6 | 2e-04 | 6/48 (C32, CHP-212, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.48×** | +4.5 | 3e-04 | 33/49 (NCI-H460, COLO 205, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.21×** | +4.2 | 0.001 | 24/49 (NCI-H2347, LoVo, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.002 | 28/47 (KATO III, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.18× | +3.6 | 0.014 | 18/48 (H4, RKO, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | 1.17× | +3.4 | 0.023 | 14/48 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.024 | 24/48 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.067 | 7/48 (PANC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.10× | +3.1 | 0.074 | 2/48 (SNU-1, H4) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.15× | +3.0 | 0.099 | 18/49 (HOP62, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12639.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.550×** | -18.6 | 0e+00 | 44/49 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.570×** | -12.4 | 9e-33 | 45/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.573×** | -12.3 | 3e-32 | 41/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.592×** | -11.6 | 1e-28 | 42/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.584×** | -11.4 | 6e-28 | 43/48 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.637×** | -9.9 | 3e-21 | 40/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.762×** | -8.5 | 2e-15 | 41/48 (HS-578T, SNU-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.697×** | -7.9 | 2e-13 | 35/48 (HOP62, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.780×** | -7.7 | 7e-13 | 29/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.724×** | -6.8 | 5e-10 | 36/47 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.735×** | -6.5 | 4e-09 | 34/50 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.747×** | -6.4 | 7e-09 | 37/48 (HOP62, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.752×** | -6.0 | 7e-08 | 29/48 (A498, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.769×** | -5.8 | 3e-07 | 30/48 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **0.824×** | -4.3 | 7e-04 | 25/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12639. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 183 | 0 | 11 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -18.7) |
| [[SW480 (line)]] | alt | 184 | 1 | 7 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.65× (z +8.9) | [[Digitoxin (drug)]] 0.5 µM 0.413× (z -15.6) |
| [[NCI-H460 (line)]] | wt | 177 | 2 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.73× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 1.62× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -20.2) |
| [[A-172 (line)]] | wt | 203 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.432× (z -11.7) |
| [[HS-578T (line)]] | alt | 302 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -11.5) |
| [[LoVo (line)]] | wt | 99.3 | 4 | 2 | [[Panobinostat (drug)]] 5 µM 3.01× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -9.4) |
| [[SHP-77 (line)]] | alt | 166 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.09× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 136 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -11.6) |
| [[RKO (line)]] | wt | 96.6 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +19.3) | [[Digitoxin (drug)]] 0.5 µM 0.378× (z -9.5) |
| [[SW 900 (line)]] | alt | 107 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.96× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -14.1) |
| [[SW48 (line)]] | wt | 148 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.40× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -10.5) |
| [[C32 (line)]] | wt | 186 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -13.5) |
| [[HT-29 (line)]] | alt | 144 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.451× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 145 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -19.2) |
| [[A498 (line)]] | wt | 243 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -11.6) |
| [[A549 (line)]] | wt | 180 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -13.3) |
| [[AsPC-1 (line)]] | alt | 50.0 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 3.09× (z +9.0) | [[Digitoxin (drug)]] 0.5 µM 0.340× (z -8.5) |
| [[HCT15 (line)]] | alt | 181 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 209 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -13.9) |
| [[J82 (line)]] | alt | 136 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 113 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.53× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 124 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 2.11× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -11.9) |
| [[PANC-1 (line)]] | alt | 218 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 1.57× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -16.9) |
| [[SNU-1 (line)]] | wt | 190 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.336× (z -10.4) |
| [[A-427 (line)]] | wt | 115 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +12.6) | — |
| [[BT-474 (line)]] | alt | 72.3 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.303× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 89.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +10.3) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 253 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -14.3) |
| [[Hs 766T (line)]] | wt | 229 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -14.4) |
| [[KATO III (line)]] | alt | 124 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +9.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -11.9) |
| [[NCI-H2030 (line)]] | alt | 122 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -13.8) |
| [[NCI-H23 (line)]] | alt | 116 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 188 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 1.95× (z +15.0) | — |
| [[SK-MEL-2 (line)]] | alt | 169 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -15.6) |
| [[SNU-423 (line)]] | alt | 190 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -9.2) |
| [[SW1417 (line)]] | alt | 104 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.412× (z -10.7) |
| [[AN3 CA (line)]] | alt | 235 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -9.0) |
| [[C-33 A (line)]] | alt | 117 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +8.9) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 227 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -9.5) |
| [[COLO 205 (line)]] | alt | 157 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.52× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 77.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 109 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.374× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 160 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 206 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -15.6) |
| [[SW 1271 (line)]] | alt | 226 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -10.3) |
| [[LS 180 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 371 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12639), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POT1]] | +0.76 | +0.77 / +0.50 | both halves | 1e-05 |  |
| [[PAPSS1]] | +0.73 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[NIPSNAP1]] | +0.72 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[NDRG3]] | +0.71 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[ATP5F1C]] | +0.71 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[MRPS31P4]] | +0.71 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[STX7]] | +0.71 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[ELP1]] | +0.71 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[RNF20]] | +0.70 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[MINDY3]] | +0.70 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[HACE1]] | +0.70 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[LONP2]] | +0.69 | +0.67 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLNRD1]] | -0.69 | -0.65 / -0.69 | both halves | 7e-06 |  |
| [[SPON1-AS1]] | -0.64 | -0.65 / -0.36 | both halves | 1e-04 |  |
| [[DDX5]] | -0.64 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[E2F3]] | -0.63 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[GCNT4]] | -0.63 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[CLCF1]] | -0.63 | -0.50 / -0.68 | both halves | 1e-05 |  |
| [[RBBP6]] | -0.62 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[SATB2]] | -0.62 | -0.60 / -0.36 | both halves | 1e-04 |  |
| [[LINC01829]] | -0.62 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[BAZ1A]] | -0.60 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[LINC01004]] | -0.60 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[SETD1B]] | -0.60 | -0.41 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SKIC3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SYBU]] | B | SYBU activity lowers SKIC3's level | lines that do not express SYBU (18) vs lines expressing it (32) | 1.29× higher at baseline in the lines without SYBU | 0.079 | ⚠ within organs, on part of the lines; also absent: CRIP1, MAP7, CHMP4C |
| [[HLTF]] | B | HLTF activity raises SKIC3's level | lines that do not express HLTF (8) vs lines expressing it (42) | 1.45× lower at baseline in the lines without HLTF | 0.092 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SKIC3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers SKIC3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.778). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-2.2, -7.4); signed map (-32.2, -13.7). **Vector** length 164, 59.3% of its response variance represented; |z| ≥ 3 in 1,363 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Intraflagellar transport* (reactome, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +8.6 | +9.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +8.4 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.3 | +6.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +8.0 | +10.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +7.4 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +7.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +6.7 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.8 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +3.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.7 | -18.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -10.1 | -8.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -9.5 | -11.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -9.5 | -12.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -9.1 | -9.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.9 | -7.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.2 | -2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.2 | -2.5 |
|  | [[Abiraterone acetate (drug)]] 0.05 µM |  | -3.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | SKI3 subunit of superkiller complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q15 — chr5:95,461,755-95,555,050 (-) |
| Ensembl biotype | protein_coding |
| Also known as | THES, SKI3; previously KIAA0372, TTC37 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; SKI complex subunits |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 3 pathways, smallest: mRNA decay by 3' to 5' exoribonuclease; Deadenylation-dependent mRNA decay; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PGP7](https://www.uniprot.org/uniprotkb/Q6PGP7) (Superkiller complex protein 3):

> Component of the SKI complex, a multiprotein complex that assists the RNA-degrading exosome during the mRNA decay and quality-control pathways. The SKI complex catalyzes mRNA extraction from 80S ribosomal complexes in the 3'-5' direction and channels mRNA to the cytosolic exosome for degradation. SKI-mediated extraction of mRNA from stalled ribosomes allow binding of the Pelota-HBS1L complex and subsequent ribosome disassembly by ABCE1 for ribosome recycling. In the nucleus, the SKI complex …

**Summary**, from NCBI Gene [9652](https://www.ncbi.nlm.nih.gov/gene/9652):

> This gene encodes a protein with twenty tetratricopeptide (TPR) repeats. Tetratricopeptide repeat containing motifs are found in a variety of proteins and may mediate protein-protein interactions and chaperone activity. Mutations in this gene are associated with trichohepatoenteric syndrome. [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:23639](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23639) · Entrez [9652](https://www.ncbi.nlm.nih.gov/gene/9652) · UniProt [Q6PGP7](https://www.uniprot.org/uniprotkb/Q6PGP7) · Ensembl [ENSG00000198677](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198677)

## Data

Gene col 12639: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12639); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12639, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12639]; `tensor/DDL_lfc|DDL_z.npy` [12639]; `embed/gene_vectors.npy` [12639]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12639 or target_col == 12639). Every well: [[SKIC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SKIC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
