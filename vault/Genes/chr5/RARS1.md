---
symbol: "RARS1"
type: "gene"
col: 3486
ensembl_id: "ENSG00000113643"
name: "arginyl-tRNA synthetase 1"
location: "5q34"
module: 49
arm: "+"
pooled_cpm: 167.65
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# RARS1

*arginyl-tRNA synthetase 1* — 5q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.75× (z +13.1, q 2e-36, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.563× (z -13.5, q 1e-38, down in 46 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.606× (z -11.8, q 1e-29, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACBD3]] (+0.76, fdr 7e-06), [[MED8]] (+0.76, fdr 1e-05), [[GORASP2]] (+0.75, fdr 7e-06); moves opposite to [[PSPC1]] (-0.60, fdr 5e-05), [[ATE1]] (-0.59, fdr 3e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC00595]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3486.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.75×** | +13.1 | 2e-36 | 43/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +12.3 | 4e-32 | 43/48 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +10.2 | 5e-22 | 40/48 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +7.1 | 1e-10 | 30/48 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +7.0 | 4e-10 | 29/48 (LOX-IMVI, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +4.9 | 8e-05 | 24/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +4.8 | 1e-04 | 26/48 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.45×** | +4.6 | 4e-04 | 27/48 (LOX-IMVI, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.15× | +4.3 | 9e-04 | 8/49 (NCI-H1792, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +4.0 | 0.003 | 19/48 (LOX-IMVI, SK-MEL-2, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.003 | 21/49 (A-172, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.005 | 23/48 (NCI-H460, SW 900, …) | two highest doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.7 | 0.010 | 18/49 (HS-578T, LS 180, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | 1.16× | +3.1 | 0.073 | 10/48 (NCI-H460, A549, …) | inconsistent across doses | position effect removed |
| [[EX229 (drug)]] 0.5 µM |  | **1.20×** | +3.1 | 0.077 | 16/49 (MIA PaCa-2, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.084 | 15/48 (SW480, LOX-IMVI, …) | two highest doses | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.085 | 9/48 (A498, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3486.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.563×** | -13.5 | 1e-38 | 46/48 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.594×** | -12.2 | 6e-32 | 41/49 (RKO, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.606×** | -11.8 | 1e-29 | 42/48 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.621×** | -10.7 | 8e-25 | 32/44 (CFPAC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.671×** | -9.4 | 7e-19 | 38/48 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.707×** | -8.1 | 4e-14 | 38/48 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.690×** | -8.1 | 6e-14 | 31/45 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.782×** | -5.6 | 2e-06 | 30/48 (A498, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -5.4 | 5e-06 | 19/49 (hTERT-HPNE, A498, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.799×** | -5.1 | 2e-05 | 26/47 (A498, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.943× | -5.0 | 3e-05 | 0/50 | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.853× | -3.7 | 0.009 | 20/48 (H4, HCT15, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.851× | -3.7 | 0.011 | 18/48 (hTERT-HPNE, LoVo, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.864× | -3.2 | 0.060 | 11/49 (NCI-H1573, SW1417, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~5% of this change | 0.864× | -3.2 | 0.060 | 18/48 (SW 1271, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | 0.876× | -3.1 | 0.063 | 15/48 (NCI-H1573, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3486. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 163 | 3 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.39× (z +14.7) | [[Digitoxin (drug)]] 5 µM 0.415× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.453× (z -13.3) |
| [[A498 (line)]] | wt | 243 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -14.5) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.593× (z -9.0) |
| [[H4 (line)]] | wt | 288 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.226× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.253× (z -12.7) |
| [[KATO III (line)]] | alt | 182 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.505× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 153 | 2 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.86× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.525× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.548× (z -9.0) |
| [[HOP62 (line)]] | alt | 176 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.361× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.369× (z -14.9) |
| [[hTERT-HPNE (line)]] | wt | 232 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.426× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 134 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.29× (z +13.0) | — |
| [[NCI-H2347 (line)]] | alt | 194 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.462× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.485× (z -11.1) |
| [[A-172 (line)]] | wt | 137 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.16× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.474× (z -11.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 167 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.97× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.367× (z -13.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 132 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.04× (z +9.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.407× (z -11.5) |
| [[BT-474 (line)]] | alt | 88.0 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -16.8) |
| [[CFPAC-1 (line)]] | alt | 154 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.360× (z -14.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 140 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.24× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.472× (z -9.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 115 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.11× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.473× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 114 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.94× (z +11.3) | [[Digitoxin (drug)]] 5 µM 0.434× (z -8.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 235 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.409× (z -12.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 129 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.92× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.442× (z -10.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 136 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.01× (z +8.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.427× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 164 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.53× (z +12.4) | — |
| [[NCI-H1792 (line)]] | alt | 143 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.429× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.475× (z -8.7) |
| [[RKO (line)]] | wt | 162 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.95× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -22.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 184 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 136 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.64× (z +13.7) | — |
| [[SW 900 (line)]] | alt | 157 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.431× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.455× (z -10.0) |
| [[SW1417 (line)]] | alt | 189 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.332× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.379× (z -14.8) |
| [[C-33 A (line)]] | alt | 108 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.36× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 148 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.19× (z +11.6) | — |
| [[Hs 766T (line)]] | wt | 184 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.500× (z -8.7) |
| [[LoVo (line)]] | wt | 220 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.10× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.471× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 161 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.411× (z -11.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 246 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.84× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.455× (z -11.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 159 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -8.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 282 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.334× (z -9.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 121 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.93× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 154 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -17.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 179 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.538× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 172 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.452× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 310 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -10.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 222 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -8.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 196 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 144 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 154 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3486), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACBD3]] | +0.76 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[MED8]] | +0.76 | +0.77 / +0.52 | both halves | 1e-05 |  |
| [[GORASP2]] | +0.75 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[PDIA5]] | +0.75 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[ZNF526]] | +0.74 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[COPB1]] | +0.73 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[COG3]] | +0.73 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[GOLGA5]] | +0.73 | +0.79 / +0.62 | both halves | 7e-06 |  |
| [[SRP54]] | +0.72 | +0.70 / +0.65 | both halves | 7e-06 | STRING 444 |
| [[RINT1]] | +0.72 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[SSR2]] | +0.72 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[COG6]] | +0.72 | +0.67 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSPC1]] | -0.60 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[ATE1]] | -0.59 | -0.53 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00595]] | B | LINC00595 activity raises RARS1's level | lines that do not express LINC00595 (9) vs lines expressing it (41) | 1.20× lower at baseline in the lines without LINC00595 | 0.087 | ⚠ within organs, on part of the lines; also absent: SUSD4, EBF4, SLC17A7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.804). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.7, -33.2); signed map (-52.0, 10.9). **Vector** length 153, 52.8% of its response variance represented; |z| ≥ 3 in 1,131 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *XBP1(S) activates chaperone genes* (reactome, mean cos +0.51 to 8); *IRE1alpha activates chaperones* (reactome, mean cos +0.51 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.6 | +13.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.3 | +10.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +5.0 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +7.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.9 | +12.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +4.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.7 | +3.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.1 | +2.7 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.6 | -13.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -8.6 | -11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.4 | -8.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -8.3 | -9.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -7.7 | -8.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.4 | -3.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -4.0 | -3.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.9 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | arginyl-tRNA synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q34 — chr5:168,486,451-168,519,301 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DALRD1; previously RARS |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class I |
| Hallmark sets | ALLOGRAFT_REJECTION, GLYCOLYSIS |
| Reactome | 7 pathways, smallest: Cytosolic tRNA aminoacylation; tRNA Aminoacylation; Transcriptional and post-translational regulation of MITF-M expression and activity |
| Matched by | ensembl_id |

**Function**, from UniProt [P54136](https://www.uniprot.org/uniprotkb/P54136) (Arginine--tRNA ligase, cytoplasmic):

> Forms part of a macromolecular complex that catalyzes the attachment of specific amino acids to cognate tRNAs during protein synthesis. Modulates the secretion of AIMP1 and may be involved in generation of the inflammatory cytokine EMAP2 from AIMP1.

**Summary**, from NCBI Gene [5917](https://www.ncbi.nlm.nih.gov/gene/5917):

> Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Arginyl-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9870](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9870) · Entrez [5917](https://www.ncbi.nlm.nih.gov/gene/5917) · UniProt [P54136](https://www.uniprot.org/uniprotkb/P54136) · Ensembl [ENSG00000113643](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113643)

## Data

Gene col 3486: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3486); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3486, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3486]; `tensor/DDL_lfc|DDL_z.npy` [3486]; `embed/gene_vectors.npy` [3486]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3486 or target_col == 3486). Every well: [[RARS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RARS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
