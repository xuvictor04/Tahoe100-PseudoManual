---
symbol: "PCBP1-AS1"
type: "gene"
col: 11056
ensembl_id: "ENSG00000179818"
name: "PCBP1 antisense RNA 1"
location: "2p13.3"
module: 83
arm: "+"
pooled_cpm: 58.92
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 19
n_dd_up_clean: 11
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# PCBP1-AS1

*PCBP1 antisense RNA 1* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.59× (z +21.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.383× (z -15.2, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM15-AS1]] (+0.87, fdr 7e-06), [[CCT6B]] (+0.81, fdr 1e-05), [[PBLD]] (+0.81, fdr 5e-05); moves opposite to [[MAST3]] (-0.73, fdr 1e-04), [[TSPAN33]] (-0.72, fdr 3e-05), [[PAFAH1B3]] (-0.72, fdr 1e-04).
> It sits in the **+** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11056.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.59×** | +21.2 | 0e+00 | 47/48 (MIA PaCa-2, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +9.2 | 7e-18 | 30/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +7.1 | 3e-10 | 30/48 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +6.8 | 1e-09 | 34/48 (SW1417, Hs 766T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +6.0 | 2e-07 | 31/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.9 | 3e-07 | 27/50 (MIA PaCa-2, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.56×** | +3.7 | 0.018 | 19/48 (RKO, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.018 | 25/48 (SW480, SNU-423, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.022 | 18/48 (CFPAC-1, A-172, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.036 | 18/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.092 | 13/48 (C32, SW48, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11056.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.383×** | -15.2 | 0e+00 | 47/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.412×** | -14.0 | 3e-42 | 46/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.448×** | -12.7 | 1e-34 | 45/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.507×** | -10.7 | 1e-24 | 41/48 (C-33 A, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.600×** | -8.1 | 8e-14 | 40/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.616×** | -7.7 | 2e-12 | 36/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.670×** | -6.3 | 2e-08 | 33/48 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.673×** | -6.0 | 1e-07 | 33/47 (HepG2/C3A, NCI-H23, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.709×** | -5.5 | 3e-06 | 31/48 (PANC-1, H4, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.730×** | -5.0 | 3e-05 | 28/48 (PANC-1, SK-MEL-2, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.733×** | -4.9 | 5e-05 | 26/48 (C-33 A, H4, …) | all doses, stronger at high dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.591×** | -4.3 | 6e-04 | 24/48 (NCI-H23, C32, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.769×** | -4.2 | 0.001 | 23/48 (RPMI-7951, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.608×** | -4.1 | 0.002 | 24/49 (HepG2/C3A, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.855× | -3.5 | 0.016 | 15/48 (C32, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.862× | -3.3 | 0.029 | 19/48 (SW48, NCI-H23, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.871× | -3.1 | 0.057 | 14/49 (CFPAC-1, SNU-1, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.690×** | -3.1 | 0.061 | 17/48 (RKO, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11056. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 159 | 1 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.101× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.169× (z -17.8) |
| [[PANC-1 (line)]] | alt | 60.5 | 1 | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +14.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.328× (z -12.3) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.377× (z -10.8) |
| [[C-33 A (line)]] | alt | 186 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0829× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.230× (z -12.6) |
| [[LoVo (line)]] | wt | 100 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +14.3) | [[Panobinostat (drug)]] 5 µM 0.188× (z -16.7) |
| [[NCI-H2030 (line)]] | alt | 118 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.4) | [[Belinostat (drug)]] 5 µM 0.216× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 43.2 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +18.5) | [[Digitoxin (drug)]] 5 µM 0.368× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.373× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 90.0 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +10.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.327× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.352× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 102 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.6) | [[Belinostat (drug)]] 5 µM 0.341× (z -10.5) |
| [[SNU-1 (line)]] | wt | 186 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -12.8) |
| [[SW480 (line)]] | alt | 70.3 | 2 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +15.1) | [[Panobinostat (drug)]] 5 µM 0.329× (z -12.7) |
| [[A-427 (line)]] | wt | 103 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.318× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 30.0 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +16.1) | [[Digitoxin (drug)]] 5 µM 0.270× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.341× (z -8.5) |
| [[COLO 205 (line)]] | alt | 82.4 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +10.5) | [[Belinostat (drug)]] 5 µM 0.244× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 129 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.217× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 49.2 | 2 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.345× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 37.2 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +20.7) | [[Panobinostat (drug)]] 5 µM 0.308× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 68.5 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +10.0) | [[Belinostat (drug)]] 5 µM 0.159× (z -13.7) |
| [[SK-MEL-2 (line)]] | alt | 66.0 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.192× (z -13.9) |
| [[Hs 766T (line)]] | wt | 23.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.53× (z +19.3) | — |
| [[LS 180 (line)]] | wt | 42.9 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +14.3) | [[Panobinostat (drug)]] 0.5 µM 0.360× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 29.9 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.269× (z -9.1) |
| [[SW1417 (line)]] | alt | 37.3 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +17.2) | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -9.0) |
| [[SW48 (line)]] | wt | 83.9 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.146× (z -12.5) |
| [[A549 (line)]] | wt | 40.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.316× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[C32 (line)]] | wt | 62.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.357× (z -8.8) |
| [[HCT15 (line)]] | alt | 48.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +13.9) | — |
| [[HOP62 (line)]] | alt | 36.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +14.1) | — |
| [[RKO (line)]] | wt | 53.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.299× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 73.9 | 0 | 1 | — | [[Malotilate (drug)]] 0.05 µM 0.134× (z -10.4) |
| [[BT-474 (line)]] | alt | 20.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.84× (z +15.9) | — |
| [[CFPAC-1 (line)]] | alt | 43.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +15.2) | — |
| [[HEC-1-A (line)]] | alt | 42.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +13.2) | — |
| [[HS-578T (line)]] | alt | 30.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +11.7) | — |
| [[HT-29 (line)]] | alt | 27.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +12.9) | — |
| [[hTERT-HPNE (line)]] | wt | 36.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +9.2) | — |
| [[KATO III (line)]] | alt | 31.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +13.9) | — |
| [[NCI-H2347 (line)]] | alt | 21.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +14.4) | — |
| [[SHP-77 (line)]] | alt | 70.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.385× (z -8.7) |
| [[SNU-423 (line)]] | alt | 32.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +12.7) | — |
| [[SW 900 (line)]] | alt | 39.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +11.5) | — |
| [[A-172 (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11056), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM15-AS1]] | +0.87 | +0.85 / +0.66 | both halves | 7e-06 | same gene group |
| [[CCT6B]] | +0.81 | +0.81 / +0.49 | both halves | 1e-05 |  |
| [[PBLD]] | +0.81 | +0.76 / +0.40 | both halves | 5e-05 |  |
| [[MPDU1]] | +0.79 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[ZCWPW1]] | +0.79 | +0.77 / +0.42 | both halves | 4e-05 |  |
| [[UBE2D3-AS1]] | +0.79 | +0.78 / +0.47 | both halves | 2e-05 | same gene group |
| [[MSH4]] | +0.77 | +0.82 / +0.35 | both halves | 1e-04 |  |
| [[C2orf49-DT]] | +0.77 | +0.75 / +0.45 | both halves | 3e-05 |  |
| [[MZF1-AS1]] | +0.77 | +0.77 / +0.31 | both halves | 2e-04 | same gene group |
| [[ACTR3-AS1]] | +0.77 | +0.75 / +0.45 | both halves | 3e-05 | same gene group |
| [[MFF-DT]] | +0.76 | +0.67 / +0.29 | both halves | 2e-04 |  |
| [[LINC01004]] | +0.76 | +0.72 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST3]] | -0.73 | -0.64 / -0.33 | both halves | 1e-04 |  |
| [[TSPAN33]] | -0.72 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[PAFAH1B3]] | -0.72 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[YIF1B]] | -0.72 | -0.62 / -0.18 | ⚠ one half (not replicated) | 0.001 |  |
| [[SERAC1]] | -0.70 | -0.66 / -0.40 | both halves | 5e-05 |  |
| [[TUBG2]] | -0.69 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[WRAP73]] | -0.68 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[TMEM256]] | -0.68 | -0.56 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PCBP1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.887). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (8.7, 9.8); signed map (21.8, -3.8). **Vector** length 130, 40.6% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +14.1 | +21.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.4 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.2 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +9.1 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.2 | +3.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.2 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.7 | +3.0 |
| fall | [[Belinostat (drug)]] 5 µM |  | -10.9 | -15.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -10.0 | -14.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -8.9 | -12.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -7.5 | -6.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.2 | -8.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.8 | -4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.6 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -3.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.5 | -2.0 |
|  | [[Cyclosporin A (drug)]] 5 µM |  | -2.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | PCBP1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2p13.3 — chr2:69,960,104-70,103,220 (-) |
| Ensembl biotype | lncRNA |
| Also known as | Linc-GALH |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:42948](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42948) · Entrez [400960](https://www.ncbi.nlm.nih.gov/gene/400960) · Ensembl [ENSG00000179818](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179818)

## Data

Gene col 11056: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11056); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11056, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11056]; `tensor/DDL_lfc|DDL_z.npy` [11056]; `embed/gene_vectors.npy` [11056]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11056 or target_col == 11056). Every well: [[PCBP1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCBP1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
