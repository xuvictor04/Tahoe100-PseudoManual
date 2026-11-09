---
symbol: "SCML1"
type: "gene"
col: 521
ensembl_id: "ENSG00000047634"
name: "Scm polycomb group protein like 1"
location: "Xp22.13"
module: 170
arm: "-"
pooled_cpm: 40.14
n_lines_expressing: 47
n_dd_up: 30
n_dd_down: 7
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/170"]
generated_by: "tahoemap"
---

# SCML1

*Scm polycomb group protein like 1* — Xp22.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.22× (z +19.0, q 0e+00, up in 38 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.772× (z -4.2, q 0.013, down in 21 of 45 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Ponatinib (drug)]] 0.5 µM: 0.796× (z -3.9, q 0.029, down in 18 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHTF2]] (+0.56, fdr 2e-05), [[ELOVL5]] (+0.51, fdr 3e-05), [[EML4]] (+0.50, fdr 3e-05); moves opposite to [[ABRAXAS2]] (-0.56, fdr 5e-05), [[NSMCE3]] (-0.49, fdr 7e-04), [[SLC7A6OS]] (-0.48, fdr 3e-05).
> It sits in the **-** arm of [[Module 170]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RADX]] → it (grade B ⚠); 2 go from it, the strongest it → [[TTC4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 23 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 521.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.22×** | +19.0 | 0e+00 | 38/44 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.37×** | +14.5 | 3e-45 | 42/45 (NCI-H460, SW1417, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.07×** | +12.3 | 2e-32 | 42/45 (NCI-H460, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +11.7 | 2e-29 | 31/44 (A-172, J82, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.97×** | +11.4 | 4e-28 | 38/45 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +11.3 | 1e-27 | 38/43 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.88×** | +10.7 | 1e-24 | 35/43 (A-172, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.88×** | +10.7 | 1e-24 | 41/45 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.81×** | +10.0 | 2e-21 | 32/45 (A-172, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.74×** | +9.3 | 9e-19 | 38/45 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.80×** | +9.2 | 2e-18 | 29/39 (A-427, LS 180, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **1.70×** | +8.9 | 3e-17 | 33/44 (NCI-H1573, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **1.70×** | +8.5 | 5e-16 | 29/36 (NCI-H1573, Panc 03.27, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +7.9 | 8e-14 | 27/44 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.55×** | +7.4 | 5e-12 | 28/45 (A-172, LoVo, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +6.1 | 3e-08 | 25/45 (NCI-H460, A-172, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.93×** | +5.8 | 2e-07 | 27/45 (NCI-H460, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.78×** | +5.1 | 9e-06 | 24/46 (Panc 03.27, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Berbamine (drug)]] 5 µM |  | 1.19× | +4.1 | 8e-04 | 16/46 (KATO III, C-33 A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.002 | 19/45 (C32, SK-MEL-2, …) | two highest doses |  |
| [[EX229 (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.029 | 12/45 (NCI-H460, KATO III, …) | inconsistent across doses |  |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.045 | 3/45 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.052 | 7/45 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.05 µM |  | 1.19× | +2.9 | 0.057 | 6/45 (J82, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.14× | +2.9 | 0.059 | 7/45 (J82, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 521.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.772×** | -4.2 | 0.013 | 21/45 (SW480, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.796×** | -3.9 | 0.029 | 18/45 (AsPC-1, J82, …) | two highest doses | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | 0.834× | -3.6 | 0.042 | 17/45 (SW480, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.810×** | -3.6 | 0.042 | 15/44 (SW480, A-172, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.812×** | -3.6 | 0.042 | 17/44 (HT-29, Hs 766T, …) | two highest doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **0.819×** | -3.4 | 0.063 | 13/45 (A-172, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.854× | -3.3 | 0.063 | 11/45 (SW480, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.869× | -3.3 | 0.063 | 13/45 (SW480, RKO, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.825×** | -3.3 | 0.063 | 18/45 (H4, Hs 766T, …) | two highest doses |  |
| [[Neratinib (drug)]] 5 µM |  | **0.830×** | -3.2 | 0.084 | 12/45 (A-427, SW 900, …) | top dose only | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.834× | -3.1 | 0.10 | 12/45 (LoVo, A498, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.883× | -3.0 | 0.11 | 18/45 (SW480, COLO 205, …) | rises with dose |  |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | 0.838× | -3.0 | 0.11 | 7/45 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 521. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.8 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +12.5) | — |
| [[A-172 (line)]] | wt | 59.4 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +18.3) | — |
| [[LoVo (line)]] | wt | 24.3 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +12.6) | — |
| [[A549 (line)]] | wt | 22.6 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 29.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.16× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.4) | — |
| [[NCI-H2347 (line)]] | alt | 17.3 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +14.4) | — |
| [[SW1417 (line)]] | alt | 56.2 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 37.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +12.2) | — |
| [[KATO III (line)]] | alt | 41.2 | 3 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.97× (z +9.8) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[Panc 03.27 (line)]] | alt | 35.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +12.4) | — |
| [[SW480 (line)]] | alt | 117 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | [[Bortezomib (drug)]] 0.05 µM 0.495× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 22.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +9.5) | — |
| [[COLO 205 (line)]] | alt | 55.5 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.86× (z +9.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.23× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 16.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +14.0) | — |
| [[Hs 766T (line)]] | wt | 48.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +14.0) | — |
| [[J82 (line)]] | alt | 57.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +15.0) | — |
| [[LS 180 (line)]] | wt | 46.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +11.7) | — |
| [[SNU-423 (line)]] | alt | 71.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +16.6) | — |
| [[A498 (line)]] | wt | 42.6 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.566× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 30.6 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.311× (z -8.7) |
| [[HCT15 (line)]] | alt | 33.7 | 0 | 1 | — | [[Belumosudil (mesylate) (drug)]] 5 µM 0.0656× (z -9.5) |
| [[HS-578T (line)]] | alt | 30.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 35.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +9.8) | — |
| [[hTERT-HPNE (line)]] | wt | 28.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 15.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.24× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[PANC-1 (line)]] | alt | 25.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 49.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +11.5) | — |
| [[SHP-77 (line)]] | alt | 43.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 27.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +11.9) | — |
| [[A-427 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.71 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.42 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 521), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*36 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHTF2]] | +0.56 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[ELOVL5]] | +0.51 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[EML4]] | +0.50 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[ARL5B]] | +0.49 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[CDK4]] | +0.49 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[RRM2]] | +0.48 | +0.36 / +0.48 | both halves | 1e-04 |  |
| [[EZH2]] | +0.47 | +0.49 / +0.49 | both halves | 2e-05 |  |
| [[RBBP7]] | +0.47 | +0.37 / +0.47 | both halves | 8e-05 |  |
| [[SNRPA]] | +0.47 | +0.34 / +0.41 | both halves | 1e-04 |  |
| [[TPP2]] | +0.46 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[ETV1]] | +0.46 | +0.43 / +0.41 | both halves | 4e-05 |  |
| [[MSH2]] | +0.46 | +0.32 / +0.43 | both halves | 2e-04 |  |

## Genes that move opposite

*64 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABRAXAS2]] | -0.56 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[NSMCE3]] | -0.49 | -0.21 / -0.46 | both halves | 7e-04 |  |
| [[SLC7A6OS]] | -0.48 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[TEFM]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[CCDC59]] | -0.48 | -0.32 / -0.50 | both halves | 1e-04 |  |
| [[OTUD7B]] | -0.48 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[ALKBH3]] | -0.48 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[SNW1]] | -0.47 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[RPP38]] | -0.47 | -0.22 / -0.49 | both halves | 6e-04 |  |
| [[TIMM22]] | -0.47 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[DPF2]] | -0.47 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[BRAP]] | -0.46 | -0.40 / -0.42 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RADX]] | B | RADX activity raises SCML1's level | lines that do not express RADX (14) vs lines expressing it (36) | 1.48× lower at baseline in the lines without RADX | 0.075 | ⚠ within organs, on part of the lines; also absent: RNF128 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTC4]] | C | SCML1 activity lowers TTC4's level | lines that do not express SCML1 (3) vs lines expressing it (47) | 1.66× higher at baseline in the lines without SCML1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: LHFPL2, SESTD1, HIPK2; its own permutation p |
| [[NCAPG2]] | C | SCML1 activity lowers NCAPG2's level | lines that do not express SCML1 (3) vs lines expressing it (47) | 1.58× higher at baseline in the lines without SCML1 | 0.065 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: LHFPL2, SESTD1, HIPK2 |

## Where it sits

- **Module**: [[Module 170]]; 24 genes; this gene is in the **-** arm (projection on the module's main direction -0.505). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-35.2, -38.6); signed map (-30.5, -46.8). **Vector** length 88.5, 22.4% of its response variance represented; |z| ≥ 3 in 1,213 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +4.2 | +10.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.2 | +9.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.7 | +2.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.7 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +2.6 | +9.2 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.5 | +4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +5.8 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.6 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.8 | -2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.0 | -1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.9 | -3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.8 | -2.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.5 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | Scm polycomb group protein like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.13 — chrX:17,737,449-17,754,988 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sterile alpha motif domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UN30](https://www.uniprot.org/uniprotkb/Q9UN30) (Sex comb on midleg-like protein 1):

> Putative Polycomb group (PcG) protein. PcG proteins act by forming multiprotein complexes, which are required to maintain the transcriptionally repressive state of homeotic genes throughout development. May be involved in spermatogenesis during sexual maturation (By similarity).

**Summary**, from NCBI Gene [6322](https://www.ncbi.nlm.nih.gov/gene/6322):

> Predicted to enable chromatin binding activity and histone binding activity. Predicted to be involved in negative regulation of DNA-templated transcription. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10580](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10580) · Entrez [6322](https://www.ncbi.nlm.nih.gov/gene/6322) · UniProt [Q9UN30](https://www.uniprot.org/uniprotkb/Q9UN30) · Ensembl [ENSG00000047634](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000047634)

## Data

Gene col 521: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 521); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 521, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 521]; `tensor/DDL_lfc|DDL_z.npy` [521]; `embed/gene_vectors.npy` [521]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 521 or target_col == 521). Every well: [[SCML1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCML1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
