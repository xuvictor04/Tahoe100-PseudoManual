---
symbol: "DMXL2"
type: "gene"
col: 2414
ensembl_id: "ENSG00000104093"
name: "Dmx like 2"
location: "15q21.2"
module: 28
arm: "+"
pooled_cpm: 89.31
n_lines_expressing: 47
n_dd_up: 5
n_dd_down: 22
n_dd_up_clean: 5
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# DMXL2

*Dmx like 2* — 15q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.33× (z +5.6, q 1e-05, up in 26 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (13 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.503× (z -9.3, q 1e-17, down in 39 of 44 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.674× (z -5.5, q 3e-06, down in 36 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHF21A]] (+0.56, fdr 1e-05), [[TIFA]] (+0.56, fdr 1e-05), [[GTF3A]] (+0.56, fdr 3e-05, ⚠ GTF3A in the vector space only through flagged drug-doses), [[CYB5A]] (+0.55, fdr 1e-05); moves opposite to [[MEF2B]] (-0.55, fdr 3e-05), [[ZNF394]] (-0.54, fdr 1e-04), [[KCTD13]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DYNC2H1]] → it (grade B ⚠); 3 go from it, the strongest it → [[DYNC2H1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2414.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +5.6 | 1e-05 | 26/45 (PANC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +5.1 | 1e-04 | 27/45 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +4.7 | 5e-04 | 29/45 (NCI-H2347, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +4.2 | 0.003 | 31/46 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.65×** | +3.7 | 0.028 | 27/46 (AsPC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.25× | +3.0 | 0.22 | 20/45 (J82, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2414.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.503×** | -9.3 | 1e-17 | 39/44 (HT-29, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.525×** | -8.4 | 2e-14 | 37/42 (NCI-H1792, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.543×** | -8.2 | 4e-14 | 33/41 (NCI-H23, CHP-212, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.567×** | -8.0 | 2e-13 | 38/46 (LoVo, A549, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.602×** | -7.1 | 1e-10 | 36/45 (SW48, NCI-H1792, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.673×** | -5.6 | 3e-06 | 31/45 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.674×** | -5.5 | 3e-06 | 36/45 (SW480, SNU-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.697×** | -5.1 | 3e-05 | 31/45 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.705×** | -4.9 | 6e-05 | 37/44 (HT-29, SW 900, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.721×** | -4.6 | 2e-04 | 27/45 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.807×** | -4.3 | 0.001 | 26/46 (A549, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.741×** | -4.2 | 0.001 | 26/45 (NCI-H1573, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.741×** | -4.2 | 0.001 | 32/45 (NCI-H460, Panc 03.27, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **0.743×** | -4.2 | 0.001 | 28/45 (HS-578T, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.592×** | -3.9 | 0.004 | 25/42 (Hs 766T, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.748×** | -3.8 | 0.006 | 30/45 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.770×** | -3.7 | 0.008 | 25/45 (Panc 03.27, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.766×** | -3.6 | 0.010 | 25/44 (Panc 03.27, HT-29, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.838× | -3.5 | 0.013 | 16/46 (Panc 03.27, SW 900, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.858× | -3.0 | 0.060 | 17/45 (SNU-1, A-172, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.679×** | -3.0 | 0.060 | 18/45 (A498, NCI-H460, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2414. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 92.7 | 0 | 9 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.166× (z -18.4) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.534× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 95.1 | 1 | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -12.9) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SW480 (line)]] | alt | 62.9 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.308× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.431× (z -9.2) |
| [[A549 (line)]] | wt | 188 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -11.4) |
| [[LoVo (line)]] | wt | 122 | 1 | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.53× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H1792 (line)]] | alt | 146 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.229× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.356× (z -13.4) |
| [[COLO 205 (line)]] | alt | 85.2 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -9.7) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.451× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 140 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.589× (z -9.0) |
| [[Hs 766T (line)]] | wt | 67.9 | 0 | 3 (3 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0517× (z -13.5) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 98.8 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.303× (z -10.5) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 86.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 101 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A498 (line)]] | wt | 77.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[C-33 A (line)]] | alt | 144 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[CHP-212 (line)]] | wt | 98.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0955× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Thymol (drug)]] 0.5 µM 0.169× (z -10.1) |
| [[HCT15 (line)]] | alt | 172 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HT-29 (line)]] | alt | 151 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.199× (z -13.8) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 92.6 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.343× (z -10.3) ⚠ toxic |
| [[NCI-H596 (line)]] | alt | 87.5 | 1 (1 ⚠) | 1 | [[Pentoxifylline (drug)]] 0.05 µM 3.18× (z +11.0) ⚠ transcription drop | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.325× (z -10.8) |
| [[PANC-1 (line)]] | alt | 134 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +19.4) | — |
| [[RKO (line)]] | wt | 116 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[RPMI-7951 (line)]] | alt | 131 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.233× (z -12.6) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SNU-1 (line)]] | wt | 141 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.455× (z -9.8) |
| [[SW48 (line)]] | wt | 97.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +11.2) | [[Digitoxin (drug)]] 5 µM 0.158× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[BT-474 (line)]] | alt | 45.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +10.0) | — |
| [[J82 (line)]] | alt | 65.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +11.8) | — |
| [[NCI-H2347 (line)]] | alt | 46.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +15.6) | — |
| [[Panc 03.27 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -11.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 68.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SW 900 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.309× (z -10.3) ⚠ toxic |
| [[SW1417 (line)]] | alt | 95.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.361× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 65.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 118 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 69.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 85.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.6 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 75.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.42 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.23 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 84.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2414), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF21A]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[TIFA]] | +0.56 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[GTF3A]] ⚠ | +0.56 | +0.54 / +0.45 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CYB5A]] | +0.55 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[COMMD8]] | +0.55 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[CLCN3]] | +0.53 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[AGL]] | +0.52 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[MDH1]] | +0.52 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[AMOT]] | +0.52 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[LGALSL]] | +0.51 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[NBN]] | +0.51 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[CAND1]] | +0.51 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[LCOR]] | +0.51 | +0.41 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEF2B]] | -0.55 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[ZNF394]] | -0.54 | -0.36 / -0.59 | both halves | 1e-04 |  |
| [[KCTD13]] | -0.53 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[GATD1-DT]] | -0.52 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[AXIN1]] | -0.51 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[PPP1R26-AS1]] | -0.51 | -0.36 / -0.61 | both halves | 9e-05 |  |
| [[ZKSCAN2-DT]] | -0.51 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[ARPC5L]] | -0.51 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[ZNF778]] | -0.50 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[TMEM11-DT]] | -0.50 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[ERVK13-1]] | -0.50 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[RABGEF1]] | -0.50 | -0.44 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYNC2H1]] | B | DYNC2H1 activity raises DMXL2's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 2.76× lower at baseline in the lines without DYNC2H1 | 0.081 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYNC2H1]] | C | DMXL2 activity raises DYNC2H1's level | lines that do not express DMXL2 (3) vs lines expressing it (47) | 5.83× lower at baseline in the lines without DMXL2 | 0.060 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: PPP2R3A, CCDC102A, ENSG00000250264 |
| [[ZNF586]] | C | DMXL2 activity raises ZNF586's level | lines that do not express DMXL2 (3) vs lines expressing it (47) | 2.28× lower at baseline in the lines without DMXL2 | 0.071 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: PPP2R3A, CCDC102A, ENSG00000250264 |
| [[HLTF]] | C | DMXL2 activity raises HLTF's level | lines that do not express DMXL2 (3) vs lines expressing it (47) | 4.79× lower at baseline in the lines without DMXL2 | 0.090 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: PPP2R3A, CCDC102A, ENSG00000250264 |

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.457). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.1, -1.9); signed map (6.3, -36.5). **Vector** length 94.8, 28.4% of its response variance represented; |z| ≥ 3 in 1,096 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.0 | +5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | -1.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +4.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.0 | +1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.5 | -0.2 |
|  | [[EX229 (drug)]] 0.05 µM |  | +2.4 | +0.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.3 | -9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.7 | -5.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.2 | -0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | Dmx like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.2 — chr15:51,447,711-51,622,833 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RC3, KIAA0856, DFNA71 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDJ6](https://www.uniprot.org/uniprotkb/Q8TDJ6) (DmX-like protein 2):

> May serve as a scaffold protein for MADD and RAB3GA on synaptic vesicles. Plays a role in the brain as a key controller of neuronal and endocrine homeostatic processes (By similarity).

**Summary**, from NCBI Gene [23312](https://www.ncbi.nlm.nih.gov/gene/23312):

> This gene encodes a protein with 12 WD domains. Proteins with WD domains are involved in many functions including participation in signal transduction pathways. Participation of the encoded protein in regulation of the Notch signaling pathway has been demonstrated in vitro using several human cell lines (PMID:20810660). A gene encoding a similar protein is located on chromosome 5. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug …

**Accessions** — [HGNC:2938](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2938) · Entrez [23312](https://www.ncbi.nlm.nih.gov/gene/23312) · UniProt [Q8TDJ6](https://www.uniprot.org/uniprotkb/Q8TDJ6) · Ensembl [ENSG00000104093](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104093)

## Data

Gene col 2414: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2414); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2414, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2414]; `tensor/DDL_lfc|DDL_z.npy` [2414]; `embed/gene_vectors.npy` [2414]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2414 or target_col == 2414). Every well: [[DMXL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DMXL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
