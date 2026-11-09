---
symbol: "CREB3L2"
type: "gene"
col: 11249
ensembl_id: "ENSG00000182158"
name: "cAMP responsive element binding protein 3 like 2"
location: "7q33"
module: 56
arm: "+"
pooled_cpm: 115.39
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 20
n_dd_up_clean: 7
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# CREB3L2

*cAMP responsive element binding protein 3 like 2* — 7q33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 1.40× (z +5.8, q 2e-06, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.536× (z -10.2, q 1e-21, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRRC1]] (+0.66, fdr 1e-05), [[SEC24D]] (+0.65, fdr 9e-06), [[SSR1]] (+0.65, fdr 7e-06); moves opposite to [[GABPB1]] (-0.53, fdr 8e-05), [[NUTM2B-AS1]] (-0.53, fdr 6e-05), [[LARS2]] (-0.50, fdr 3e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11249.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +5.8 | 2e-06 | 28/48 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.40×** | +5.8 | 2e-06 | 27/48 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.7 | 4e-04 | 22/48 (HT-29, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.27×** | +4.1 | 0.006 | 22/48 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.017 | 19/49 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.046 | 17/48 (C32, SW480, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.052 | 22/48 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.1 | 0.14 | 21/48 (PANC-1, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11249.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.536×** | -10.2 | 1e-21 | 43/48 (hTERT-HPNE, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.561×** | -10.0 | 3e-21 | 44/48 (COLO 205, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.564×** | -9.9 | 6e-21 | 39/48 (COLO 205, BT-474, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.572×** | -9.7 | 5e-20 | 43/48 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.610×** | -8.6 | 1e-15 | 37/48 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.742×** | -7.3 | 2e-11 | 31/48 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.659×** | -7.2 | 4e-11 | 37/48 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.480×** | -6.6 | 2e-09 | 31/45 (hTERT-HPNE, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.801×** | -5.4 | 3e-06 | 33/48 (SNU-1, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.732×** | -5.4 | 4e-06 | 26/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.741×** | -5.2 | 1e-05 | 27/48 (BT-474, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.740×** | -5.0 | 2e-05 | 22/47 (H4, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.761×** | -4.7 | 9e-05 | 26/49 (H4, LoVo, …) | inconsistent across doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.764×** | -4.5 | 3e-04 | 24/47 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.793×** | -3.7 | 0.008 | 24/45 (SHP-77, SNU-1, …) | inconsistent across doses | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.816×** | -3.5 | 0.014 | 20/48 (LoVo, H4, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.816×** | -3.5 | 0.014 | 21/48 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.821×** | -3.4 | 0.019 | 21/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.822×** | -3.4 | 0.019 | 19/48 (RPMI-7951, HS-578T, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.822×** | -3.3 | 0.029 | 17/47 (BT-474, J82, …) | rises with dose |  |
| [[Thymol (drug)]] 5 µM |  | 0.877× | -3.2 | 0.034 | 17/48 (NCI-H23, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.842× | -3.0 | 0.070 | 18/48 (NCI-H2347, SW 900, …) | inconsistent across doses |  |
| [[Acetohexamide (drug)]] 5 µM |  | 0.887× | -2.9 | 0.076 | 6/48 (HT-29, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11249. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 262 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -22.1) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -13.2) |
| [[LoVo (line)]] | wt | 128 | 0 | 7 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.297× (z -12.8) ⚠ toxic; cell-cycle shift, explains ~29% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.315× (z -12.0) |
| [[H4 (line)]] | wt | 213 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.291× (z -11.5) |
| [[HOP62 (line)]] | alt | 195 | 0 | 6 (3 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.367× (z -11.8) |
| [[SW480 (line)]] | alt | 63.4 | 2 (2 ⚠) | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +9.8) ⚠ cell-cycle shift, explains ~19% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.314× (z -11.7) |
| [[A549 (line)]] | wt | 115 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -12.2) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.369× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 63.4 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.53× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -18.0) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.344× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 225 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -19.7) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.267× (z -13.1) |
| [[BT-474 (line)]] | alt | 92.6 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.205× (z -12.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.270× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 343 | 0 | 4 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.291× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 172 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -20.1) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.212× (z -13.3) |
| [[PANC-1 (line)]] | alt | 33.2 | 3 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.30× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -10.3) ⚠ cell-cycle shift, explains ~49% of this change |
| [[RKO (line)]] | wt | 97.0 | 3 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.38× (z +9.7) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.18× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[C32 (line)]] | wt | 109 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.44× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 104 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -11.0) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.343× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 58.5 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.312× (z -11.4) |
| [[SW 900 (line)]] | alt | 167 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -12.3) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.325× (z -11.1) |
| [[A-172 (line)]] | wt | 80.7 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.371× (z -9.2) ⚠ cell-cycle shift, explains ~97% of this change |
| [[KATO III (line)]] | alt | 117 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 133 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.320× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 79.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.353× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 92.5 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.97× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 118 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.294× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[A-427 (line)]] | wt | 41.3 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.137× (z -8.7) ⚠ toxic |
| [[A498 (line)]] | wt | 324 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.659× (z -8.5) ⚠ cell-cycle shift, explains ~49% of this change |
| [[AsPC-1 (line)]] | alt | 80.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.400× (z -9.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 159 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.240× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 36.4 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.93× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 41.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +10.0) ⚠ cell-cycle shift, explains ~19% of this change | — |
| [[RPMI-7951 (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -9.6) ⚠ cell-cycle shift, explains ~49% of this change |
| [[SHP-77 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.359× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SW1417 (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.336× (z -9.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 127 | 1 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 3.39× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 76.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 104 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 208 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 228 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11249), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRRC1]] | +0.66 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[SEC24D]] | +0.65 | +0.67 / +0.57 | both halves | 9e-06 | STRING 748 |
| [[SSR1]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 | pathway: Unfolded Protein Response (UPR) |
| [[GORASP2]] | +0.63 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[GBF1]] | +0.63 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[TTC3]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[MANF]] | +0.62 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[OSTC]] | +0.61 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[PJA2]] | +0.61 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[TMEM39A]] | +0.61 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[FBXO16]] | +0.60 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[COG6]] | +0.60 | +0.62 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABPB1]] | -0.53 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[NUTM2B-AS1]] | -0.53 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[LARS2]] | -0.50 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[TTC27]] | -0.50 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[ZNF124]] | -0.49 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[PHF14]] | -0.49 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[MRPL45P2]] | -0.49 | -0.48 / -0.37 | both halves | 9e-05 |  |
| [[E2F3]] | -0.49 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[RBM19]] | -0.49 | -0.52 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers CREB3L2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers CREB3L2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.616). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.2, -33.1); signed map (-53.6, 11.1). **Vector** length 126, 38.3% of its response variance represented; |z| ≥ 3 in 1,334 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ER to Golgi Anterograde Transport* (reactome, mean cos +0.53 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.53 to 16); *COPI-dependent Golgi-to-ER retrograde traffic* (reactome, mean cos +0.53 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | +8.0 | -4.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.4 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +5.4 | -3.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.0 | +5.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +3.0 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +0.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -7.3 | -10.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.6 | -10.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.6 | -9.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.2 | -3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.8 | -3.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.8 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | cAMP responsive element binding protein 3 like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q33 — chr7:137,874,979-138,002,086 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BBF2H7, TCAG_1951439 |
| Gene groups (HGNC) | CREB3 transcription factor family |
| Reactome | 4 pathways, smallest: CREB3 factors activate genes; Unfolded Protein Response (UPR); Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q70SY1](https://www.uniprot.org/uniprotkb/Q70SY1) (Cyclic AMP-responsive element-binding protein 3-like protein 2):

> Transcription factor involved in unfolded protein response (UPR). In the absence of endoplasmic reticulum (ER) stress, inserted into ER membranes, with N-terminal DNA-binding and transcription activation domains oriented toward the cytosolic face of the membrane. In response to ER stress, transported to the Golgi, where it is cleaved in a site-specific manner by resident proteases S1P/MBTPS1 and S2P/MBTPS2. The released N-terminal cytosolic domain is translocated to the nucleus to effect …

**Summary**, from NCBI Gene [64764](https://www.ncbi.nlm.nih.gov/gene/64764):

> This gene encodes a member of the oasis bZIP transcription factor family. Members of this family can dimerize but form homodimers only. The encoded protein is a transcriptional activator. Translocations between this gene on chromosome 7 and the gene fused in sarcoma on chromosome 16 can be found in some tumors. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:23720](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23720) · Entrez [64764](https://www.ncbi.nlm.nih.gov/gene/64764) · UniProt [Q70SY1](https://www.uniprot.org/uniprotkb/Q70SY1) · Ensembl [ENSG00000182158](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182158)

## Data

Gene col 11249: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11249); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11249, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11249]; `tensor/DDL_lfc|DDL_z.npy` [11249]; `embed/gene_vectors.npy` [11249]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11249 or target_col == 11249). Every well: [[CREB3L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CREB3L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
