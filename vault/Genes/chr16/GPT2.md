---
symbol: "GPT2"
type: "gene"
col: 9237
ensembl_id: "ENSG00000166123"
name: "glutamic--pyruvic transaminase 2"
location: "16q11.2"
module: 63
arm: "+"
pooled_cpm: 45.46
n_lines_expressing: 48
n_dd_up: 27
n_dd_down: 39
n_dd_up_clean: 25
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# GPT2

*glutamic--pyruvic transaminase 2* — 16q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.92× (z +10.3, q 4e-22, up in 41 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Artesunate (drug)]] 5 µM: 1.48× (z +8.3, q 4e-14, up in 37 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.160× (z -38.8, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GARS1]] (+0.79, fdr 7e-06), [[EIF4EBP1]] (+0.76, fdr 7e-06), [[CARS1]] (+0.76, fdr 7e-06); moves opposite to [[PNRC2]] (-0.57, fdr 2e-05), [[C11orf58]] (-0.54, fdr 1e-04).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9237.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.92×** | +10.3 | 4e-22 | 41/46 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | **1.48×** | +8.3 | 4e-14 | 37/46 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +6.6 | 6e-09 | 26/46 (SW480, A-172, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.50×** | +6.4 | 3e-08 | 32/46 (SHP-77, SW480, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **2.13×** | +6.2 | 5e-08 | 34/44 (NCI-H2030, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.47×** | +6.1 | 1e-07 | 30/46 (NCI-H2030, SHP-77, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.90×** | +5.3 | 9e-06 | 28/46 (NCI-H2030, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.37×** | +4.9 | 6e-05 | 26/46 (Hs 766T, SW480, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.36×** | +4.9 | 6e-05 | 24/46 (SNU-1, HCT15, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.24×** | +4.8 | 1e-04 | 24/46 (NCI-H2030, SW480, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.74×** | +4.6 | 2e-04 | 24/45 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | **1.31×** | +4.3 | 9e-04 | 18/46 (NCI-H2030, AsPC-1, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.003 | 19/47 (SNU-1, Hs 766T, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.42×** | +4.0 | 0.003 | 14/44 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.60×** | +3.9 | 0.004 | 20/46 (NCI-H2030, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.60×** | +3.9 | 0.004 | 19/44 (NCI-H2030, NCI-H460, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9237.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.160×** | -38.8 | 0e+00 | 45/46 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.162×** | -27.6 | 0e+00 | 44/46 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.263×** | -21.1 | 0e+00 | 43/46 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.418×** | -13.8 | 7e-41 | 38/46 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.536×** | -13.2 | 8e-38 | 36/46 (A-172, C32, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.492×** | -11.2 | 5e-27 | 40/46 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.517×** | -10.4 | 2e-23 | 33/44 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.530×** | -9.6 | 5e-20 | 28/44 (HepG2/C3A, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.558×** | -9.2 | 2e-18 | 36/46 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.571×** | -8.8 | 6e-17 | 36/46 (A-172, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.603×** | -8.0 | 8e-14 | 32/46 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.714×** | -7.3 | 2e-11 | 33/46 (HS-578T, HepG2/C3A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.625×** | -6.9 | 3e-10 | 28/41 (AN3 CA, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.636×** | -6.9 | 3e-10 | 25/37 (PANC-1, H4, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.663×** | -6.2 | 2e-08 | 27/44 (J82, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.695×** | -5.7 | 4e-07 | 26/46 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[AZD-8055 (drug)]] 5 µM |  | **0.548×** | -5.0 | 2e-05 | 24/46 (HS-578T, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.733×** | -4.7 | 7e-05 | 23/46 (C32, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.05 µM |  | **0.732×** | -4.6 | 1e-04 | 21/46 (Hs 766T, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9237. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 38.5 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0811× (z -33.8) |
| [[KATO III (line)]] | alt | 75.5 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -25.5) |
| [[NCI-H460 (line)]] | wt | 30.4 | 1 (1 ⚠) | 9 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.68× (z +9.8) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -18.5) |
| [[LoVo (line)]] | wt | 69.1 | 0 | 9 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0559× (z -24.4) |
| [[A-172 (line)]] | wt | 59.0 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -23.7) |
| [[C32 (line)]] | wt | 64.5 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0478× (z -33.8) |
| [[J82 (line)]] | alt | 59.5 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0564× (z -40.5) |
| [[SW1417 (line)]] | alt | 33.0 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -21.7) |
| [[A498 (line)]] | wt | 78.3 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -20.0) |
| [[HepG2_C3A (line)]] | wt | 150 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -24.2) |
| [[HT-29 (line)]] | alt | 68.4 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0860× (z -30.6) |
| [[SNU-1 (line)]] | wt | 99.3 | 2 | 5 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 3.76× (z +12.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.0693× (z -18.2) |
| [[CFPAC-1 (line)]] | alt | 35.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -20.1) |
| [[H4 (line)]] | wt | 76.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -20.5) |
| [[HS-578T (line)]] | alt | 57.5 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.0927× (z -25.3) |
| [[LS 180 (line)]] | wt | 53.3 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -18.5) |
| [[MIA PaCa-2 (line)]] | alt | 106 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0590× (z -20.6) |
| [[RKO (line)]] | wt | 55.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -17.1) |
| [[SW48 (line)]] | wt | 81.6 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -17.0) |
| [[AsPC-1 (line)]] | alt | 24.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0904× (z -18.1) |
| [[SK-MEL-2 (line)]] | alt | 57.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0469× (z -26.2) |
| [[AN3 CA (line)]] | alt | 73.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -13.6) |
| [[NCI-H2030 (line)]] | alt | 26.1 | 1 (1 ⚠) | 3 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.02× (z +10.1) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -21.5) |
| [[HCT15 (line)]] | alt | 83.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -11.7) |
| [[Hs 766T (line)]] | wt | 43.2 | 1 | 2 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.88× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -18.8) |
| [[NCI-H1792 (line)]] | alt | 30.5 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0679× (z -18.3) |
| [[NCI-H23 (line)]] | alt | 20.8 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.110× (z -12.9) |
| [[NCI-H2347 (line)]] | alt | 18.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -15.4) |
| [[RPMI-7951 (line)]] | alt | 44.9 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0918× (z -16.2) |
| [[A-427 (line)]] | wt | 21.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0344× (z -22.5) |
| [[C-33 A (line)]] | alt | 57.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.353× (z -10.7) |
| [[SNU-423 (line)]] | alt | 32.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -13.0) |
| [[SW 900 (line)]] | alt | 19.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -14.8) |
| [[SW480 (line)]] | alt | 50.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -18.4) |
| [[A549 (line)]] | wt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 24.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -9.4) |
| [[HOP62 (line)]] | alt | 53.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0950× (z -25.7) |
| [[NCI-H1573 (line)]] | alt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 16.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -13.3) |
| [[BT-474 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9237), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GARS1]] | +0.79 | +0.80 / +0.78 | both halves | 7e-06 |  |
| [[EIF4EBP1]] | +0.76 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[CARS1]] | +0.76 | +0.69 / +0.81 | both halves | 7e-06 |  |
| [[GOT1]] | +0.74 | +0.70 / +0.70 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives; STRING 984 |
| [[LONP1]] | +0.73 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[ASNS]] | +0.73 | +0.70 / +0.72 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives; STRING 610 |
| [[SESN2]] | +0.73 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[SARS1]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives |
| [[UBE2Q2P2]] | +0.72 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[PHGDH]] | +0.72 | +0.71 / +0.71 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives; STRING 714 |
| [[CHAC1]] | +0.71 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[XPOT]] | +0.70 | +0.71 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNRC2]] | -0.57 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[C11orf58]] | -0.54 | -0.54 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity raises GPT2's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 6.4% of all compounds | 0.041 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises GPT2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.758). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.0, 49.0); signed map (-13.6, 25.6). **Vector** length 147, 49.2% of its response variance represented; |z| ≥ 3 in 1,478 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.66 to 16); *mTORC1 signaling* (hallmark, mean cos +0.58 to 20); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.67 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.9 | +10.3 |
|  | [[Artesunate (drug)]] 5 µM |  | +7.4 | +8.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.0 | +1.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.7 | -0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.7 | +6.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +6.4 | +5.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +5.7 | +6.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.3 | +6.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +5.2 | +4.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -10.9 | -13.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.2 | -27.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -6.6 | -8.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.2 | -13.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.2 | -21.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -4.9 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -5.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -4.3 | -3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.0 | -4.1 |
|  | [[AZD-8055 (drug)]] 5 µM |  | -3.8 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | glutamic--pyruvic transaminase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q11.2 — chr16:46,884,362-46,931,289 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ALT2 |
| Gene groups (HGNC) | Glutamic--pyruvic transaminase family |
| Reactome | 1 pathways, smallest: Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TD30](https://www.uniprot.org/uniprotkb/Q8TD30) (Alanine aminotransferase 2):

> Catalyzes the reversible transamination between alanine and 2-oxoglutarate to form pyruvate and glutamate.

**Summary**, from NCBI Gene [84706](https://www.ncbi.nlm.nih.gov/gene/84706):

> This gene encodes a mitochondrial alanine transaminase, a pyridoxal enzyme that catalyzes the reversible transamination between alanine and 2-oxoglutarate to generate pyruvate and glutamate. Alanine transaminases play roles in gluconeogenesis and amino acid metabolism in many tissues including skeletal muscle, kidney, and liver. Activating transcription factor 4 upregulates this gene under metabolic stress conditions in hepatocyte cell lines. A loss of function mutation in this gene has been …

**Accessions** — [HGNC:18062](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18062) · Entrez [84706](https://www.ncbi.nlm.nih.gov/gene/84706) · UniProt [Q8TD30](https://www.uniprot.org/uniprotkb/Q8TD30) · Ensembl [ENSG00000166123](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166123)

## Data

Gene col 9237: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9237); `tables/drug_effects.parquet` (73 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9237, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9237]; `tensor/DDL_lfc|DDL_z.npy` [9237]; `embed/gene_vectors.npy` [9237]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9237 or target_col == 9237). Every well: [[GPT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
