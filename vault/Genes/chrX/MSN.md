---
symbol: "MSN"
type: "gene"
col: 7144
ensembl_id: "ENSG00000147065"
name: "moesin"
location: "Xq12"
module: 78
arm: "+"
pooled_cpm: 292.49
n_lines_expressing: 40
n_dd_up: 14
n_dd_down: 32
n_dd_up_clean: 9
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# MSN

*moesin* — Xq12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.40× (z +15.6, q 0e+00, up in 35 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.60× (z +8.4, q 6e-15, up in 35 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.451× (z -20.0, q 0e+00, down in 33 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MACF1]] (+0.72, fdr 7e-06), [[TPM3]] (+0.70, fdr 7e-06), [[ACTN1]] (+0.70, fdr 7e-06); moves opposite to [[SAT2]] (-0.59, fdr 1e-05), [[RAB9A]] (-0.59, fdr 1e-05), [[PPP4R3A]] (-0.59, fdr 2e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CD59]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7144.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.40×** | +15.6 | 0e+00 | 35/39 (A-427, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +14.4 | 2e-44 | 34/36 (C32, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +12.6 | 7e-34 | 34/36 (C-33 A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +8.4 | 6e-15 | 35/38 (Panc 03.27, HEC-1-A, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +8.0 | 2e-13 | 30/38 (SW480, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +7.8 | 5e-13 | 31/38 (HEC-1-A, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.56×** | +7.5 | 4e-12 | 32/38 (HEC-1-A, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.32×** | +4.9 | 6e-05 | 28/37 (SK-MEL-2, PANC-1, …) | all doses, flat | position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.34×** | +4.9 | 7e-05 | 31/38 (SK-MEL-2, NCI-H460, …) | all doses, flat | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.27×** | +4.3 | 8e-04 | 24/38 (SK-MEL-2, PANC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.25×** | +4.0 | 0.004 | 21/37 (SK-MEL-2, PANC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.007 | 21/37 (SK-MEL-2, PANC-1, …) | all doses, flat | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.5 | 0.020 | 10/39 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.021 | 18/38 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Minodronic acid (drug)]] 5 µM |  | **1.43×** | +3.1 | 0.064 | 17/38 (LOX-IMVI, SK-MEL-2, …) | rises with dose | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7144.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.451×** | -20.0 | 0e+00 | 33/38 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.359×** | -18.2 | 0e+00 | 37/38 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.426×** | -15.2 | 0e+00 | 37/38 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.432×** | -14.9 | 0e+00 | 36/38 (SK-MEL-2, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.595×** | -13.1 | 6e-37 | 28/39 (NCI-H1573, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.521×** | -11.6 | 4e-29 | 31/38 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.620×** | -8.5 | 2e-15 | 35/38 (C32, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.616×** | -8.3 | 8e-15 | 29/37 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.688×** | -6.7 | 2e-09 | 31/38 (HT-29, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.719×** | -5.8 | 3e-07 | 27/38 (SK-MEL-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.724×** | -5.7 | 5e-07 | 29/38 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.737×** | -5.1 | 2e-05 | 34/39 (NCI-H460, A-172, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.816×** | -5.1 | 2e-05 | 20/38 (AsPC-1, C32, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.799×** | -4.8 | 6e-05 | 22/38 (AsPC-1, SHP-77, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.769×** | -4.6 | 1e-04 | 23/38 (J82, SHP-77, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Amsacrine (drug)]] 5 µM |  | **0.832×** | -4.6 | 1e-04 | 19/38 (A549, J82, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.812×** | -4.4 | 4e-04 | 20/38 (AsPC-1, SHP-77, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7144. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 357 | 1 | 15 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.33× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -21.9) |
| [[SW480 (line)]] | alt | 299 | 5 (1 ⚠) | 7 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.77× (z +13.7) | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -23.8) |
| [[MIA PaCa-2 (line)]] | alt | 232 | 6 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 2.66× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.22× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -16.8) |
| [[C32 (line)]] | wt | 245 | 5 (4 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 3.38× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.31× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.375× (z -12.8) |
| [[SHP-77 (line)]] | alt | 183 | 2 (2 ⚠) | 8 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.42× (z +14.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -17.5) |
| [[H4 (line)]] | wt | 495 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -20.3) |
| [[NCI-H460 (line)]] | wt | 362 | 2 (2 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +14.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -36.0) |
| [[Panc 03.27 (line)]] | alt | 164 | 7 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.60× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -10.6) |
| [[A549 (line)]] | wt | 457 | 2 (2 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.98× (z +9.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.237× (z -19.5) |
| [[LOX-IMVI (line)]] | wt | 523 | 3 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +14.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -30.1) |
| [[NCI-H1573 (line)]] | alt | 280 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -26.4) |
| [[PANC-1 (line)]] | alt | 315 | 3 (3 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +11.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.346× (z -13.2) |
| [[A-427 (line)]] | wt | 126 | 5 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +15.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.95× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -24.3) |
| [[HOP62 (line)]] | alt | 546 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -16.1) |
| [[HS-578T (line)]] | alt | 358 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +10.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.238× (z -18.9) |
| [[A-172 (line)]] | wt | 395 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +14.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.359× (z -15.6) |
| [[HEC-1-A (line)]] | alt | 116 | 5 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.80× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.34× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.498× (z -8.7) |
| [[HT-29 (line)]] | alt | 289 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -13.2) |
| [[J82 (line)]] | alt | 432 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.233× (z -18.6) |
| [[NCI-H23 (line)]] | alt | 256 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +13.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -29.7) |
| [[RPMI-7951 (line)]] | alt | 547 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -18.5) |
| [[SK-MEL-2 (line)]] | alt | 488 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.260× (z -17.7) |
| [[SNU-423 (line)]] | alt | 666 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +13.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.276× (z -15.8) |
| [[Hs 766T (line)]] | wt | 755 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -15.7) |
| [[LoVo (line)]] | wt | 85.7 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -17.8) |
| [[NCI-H2347 (line)]] | alt | 450 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -14.1) |
| [[SW 900 (line)]] | alt | 192 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +8.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.293× (z -13.2) |
| [[A498 (line)]] | wt | 463 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +13.4) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 103 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 5.34× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -12.3) |
| [[CFPAC-1 (line)]] | alt | 181 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 232 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +11.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -12.9) |
| [[SNU-1 (line)]] | wt | 116 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +11.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 181 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +11.2) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 422 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +9.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.357× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 277 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -23.2) |
| [[SW 1271 (line)]] | alt | 488 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -12.1) |
| [[BT-474 (line)]] | alt | 22.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 30.4 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 23.1 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 25.7 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 24.5 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 22.6 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 70.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 474 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 57.7 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 27.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7144), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MACF1]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 | STRING 534 |
| [[TPM3]] | +0.70 | +0.76 / +0.66 | both halves | 7e-06 | pathway: Signaling by ALK fusions and activated point mutants; STRING 647 |
| [[ACTN1]] | +0.70 | +0.70 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION; STRING 432 |
| [[PSMD2]] | +0.68 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[NES]] | +0.66 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[BCAP31]] | +0.65 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[CDC37]] | +0.64 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[CAPN2]] | +0.63 | +0.60 / +0.66 | both halves | 7e-06 | STRING 562 |
| [[LAMC1]] | +0.63 | +0.60 / +0.70 | both halves | 7e-06 | pathway: L1CAM interactions |
| [[CORO1C]] | +0.63 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[MYH9]] | +0.62 | +0.51 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_APICAL_JUNCTION; STRING 941 |
| [[CAP1]] | +0.62 | +0.65 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |

## Genes that move opposite

*33 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAT2]] | -0.59 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[RAB9A]] | -0.59 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[PPP4R3A]] | -0.59 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[C15orf61]] ⚠ | -0.58 | -0.41 / -0.72 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[HOXA5]] | -0.57 | -0.41 / -0.65 | both halves | 4e-05 |  |
| [[COIL]] | -0.57 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[RCHY1]] | -0.57 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[POLR1H]] | -0.57 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[DPM3]] | -0.56 | -0.29 / -0.68 | both halves | 2e-04 |  |
| [[SCAF11]] | -0.55 | -0.65 / -0.36 | both halves | 1e-04 |  |
| [[SCAMP3]] | -0.55 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[ZNF330]] | -0.55 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[RANGRF]] | -0.55 | -0.36 / -0.54 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD59]] | B | CD59 activity raises MSN's level | lines that do not express CD59 (7) vs lines expressing it (43) | 2.22× lower at baseline in the lines without CD59 | 0.099 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.710). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.6, 10.1); signed map (-8.1, 38.2). **Vector** length 136, 49.7% of its response variance represented; |z| ≥ 3 in 1,476 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.0 | +8.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.3 | +8.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.0 | +7.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.7 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.1 | +12.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | -1.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.4 | +2.9 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +3.2 | +2.3 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.3 | -2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.2 | -8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -20.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.6 | -6.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -11.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.2 | -4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.1 | -4.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.9 | -5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.6 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | moesin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq12 — chrX:65,588,377-65,741,931 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | FERM domain containing |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 16 pathways, smallest: Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation; Interleukin-12 signaling; Recycling pathway of L1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P26038](https://www.uniprot.org/uniprotkb/P26038) (Moesin):

> Ezrin-radixin-moesin (ERM) family protein that connects the actin cytoskeleton to the plasma membrane and thereby regulates the structure and function of specific domains of the cell cortex. Tethers actin filaments by oscillating between a resting and an activated state providing transient interactions between moesin and the actin cytoskeleton. Once phosphorylated on its C-terminal threonine, moesin is activated leading to interaction with F-actin and cytoskeletal rearrangement. These …

**Summary**, from NCBI Gene [4478](https://www.ncbi.nlm.nih.gov/gene/4478):

> Moesin (for membrane-organizing extension spike protein) is a member of the ERM family which includes ezrin and radixin. ERM proteins appear to function as cross-linkers between plasma membranes and actin-based cytoskeletons. Moesin is localized to filopodia and other membranous protrusions that are important for cell-cell recognition and signaling and for cell movement. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7373](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7373) · Entrez [4478](https://www.ncbi.nlm.nih.gov/gene/4478) · UniProt [P26038](https://www.uniprot.org/uniprotkb/P26038) · Ensembl [ENSG00000147065](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147065)

## Data

Gene col 7144: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7144); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7144, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7144]; `tensor/DDL_lfc|DDL_z.npy` [7144]; `embed/gene_vectors.npy` [7144]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7144 or target_col == 7144). Every well: [[MSN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
