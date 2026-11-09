---
symbol: "REEP5"
type: "gene"
col: 4991
ensembl_id: "ENSG00000129625"
name: "receptor accessory protein 5"
location: "5q22.2"
module: 214
arm: "+"
pooled_cpm: 69.82
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 10
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/214"]
generated_by: "tahoemap"
---

# REEP5

*receptor accessory protein 5* — 5q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.06× (z +16.2, q 0e+00, up in 44 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 1.36× (z +4.1, q 0.003, up in 21 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.533× (z -19.8, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AMFR]] (+0.61, fdr 1e-05), [[SGPP1]] (+0.57, fdr 5e-05), [[CHPT1]] (+0.55, fdr 3e-05); moves opposite to [[PPP1R10]] (-0.53, fdr 1e-05), [[SMG9]] (-0.52, fdr 3e-05), [[ZNF414]] (-0.48, fdr 9e-05).
> It is in [[Module 214]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4991.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.06×** | +16.2 | 0e+00 | 44/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +15.2 | 0e+00 | 34/41 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +9.6 | 2e-19 | 35/45 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +7.2 | 1e-10 | 36/47 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.35×** | +6.8 | 2e-09 | 33/47 (A-172, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | **1.21×** | +4.2 | 0.002 | 20/47 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.1 | 0.003 | 17/47 (LS 180, NCI-H460, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 0.003 | 21/47 (MIA PaCa-2, HCT15, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 0.003 | 21/47 (SW480, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.20× | +4.1 | 0.003 | 16/47 (NCI-H2347, COLO 205, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.009 | 21/46 (LOX-IMVI, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.020 | 15/46 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.035 | 13/46 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.046 | 8/47 (NCI-H23, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.15× | +3.2 | 0.056 | 11/47 (SW480, LS 180, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.056 | 8/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.070 | 5/47 (CFPAC-1, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4991.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.533×** | -19.8 | 0e+00 | 43/47 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.567×** | -12.6 | 5e-34 | 40/47 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.597×** | -11.5 | 4e-28 | 36/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.628×** | -10.0 | 3e-21 | 36/47 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.674×** | -8.8 | 2e-16 | 35/47 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.774×** | -5.7 | 1e-06 | 24/47 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.805×** | -4.8 | 1e-04 | 21/47 (HS-578T, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.816×** | -4.5 | 5e-04 | 23/47 (C32, HEC-1-A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.676×** | -4.2 | 0.002 | 25/48 (HOP62, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.804×** | -4.0 | 0.004 | 22/47 (SNU-1, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.839× | -3.9 | 0.005 | 18/47 (SNU-1, LoVo, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.851× | -3.4 | 0.028 | 15/47 (LoVo, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4991. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 117 | 2 (2 ⚠) | 6 | [[Dinaciclib (drug)]] 5 µM 2.23× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -20.3) |
| [[SW480 (line)]] | alt | 71.8 | 5 (5 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.30× (z +12.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.423× (z -13.2) |
| [[A-172 (line)]] | wt | 95.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -27.2) |
| [[A498 (line)]] | wt | 92.2 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -16.0) |
| [[A549 (line)]] | wt | 63.1 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 78.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.599× (z -9.6) |
| [[Hs 766T (line)]] | wt | 74.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -15.4) |
| [[LOX-IMVI (line)]] | wt | 73.7 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.26× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -22.9) |
| [[MIA PaCa-2 (line)]] | alt | 67.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.331× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 90.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -9.7) |
| [[HOP62 (line)]] | alt | 77.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -17.6) |
| [[J82 (line)]] | alt | 71.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.22× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -16.2) |
| [[KATO III (line)]] | alt | 51.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +10.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.300× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 46.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.17× (z +11.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 97.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -17.0) |
| [[NCI-H2030 (line)]] | alt | 67.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -16.6) |
| [[NCI-H2347 (line)]] | alt | 133 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.88× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -20.4) |
| [[NCI-H460 (line)]] | wt | 51.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.86× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -13.7) |
| [[Panc 03.27 (line)]] | alt | 96.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +12.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.421× (z -10.4) |
| [[PANC-1 (line)]] | alt | 47.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +14.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -12.0) |
| [[SNU-423 (line)]] | alt | 74.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.36× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -16.8) |
| [[AsPC-1 (line)]] | alt | 62.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -13.8) |
| [[C32 (line)]] | wt | 59.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -12.9) |
| [[RKO (line)]] | wt | 68.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 69.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -11.6) |
| [[SW48 (line)]] | wt | 84.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.368× (z -8.8) |
| [[H4 (line)]] | wt | 71.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -8.8) |
| [[HT-29 (line)]] | alt | 52.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.38× (z +8.8) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 79.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +9.3) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 71.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.472× (z -8.8) |
| [[LS 180 (line)]] | wt | 57.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.447× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 53.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -16.5) |
| [[SNU-1 (line)]] | wt | 61.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -12.1) |
| [[SW 900 (line)]] | alt | 42.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 61.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.45 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 48.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4991), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AMFR]] | +0.61 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[SGPP1]] | +0.57 | +0.72 / +0.39 | both halves | 5e-05 |  |
| [[CHPT1]] | +0.55 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[ZNF398]] | +0.54 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[ABCB10]] | +0.53 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[DUSP22]] | +0.51 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[SNHG22]] | +0.50 | +0.30 / +0.48 | both halves | 2e-04 |  |
| [[SETD7]] | +0.49 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[PCBP4]] | +0.49 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[SVIL-AS1-1]] | +0.49 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[GINM1]] | +0.48 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[CERS2]] | +0.48 | +0.48 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R10]] | -0.53 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[SMG9]] | -0.52 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[ZNF414]] | -0.48 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[HES1]] | -0.48 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[SFR1]] | -0.48 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[FIBP]] | -0.46 | -0.49 / -0.27 | both halves | 3e-04 |  |
| [[IRAG1-AS1]] | -0.46 | -0.58 / -0.27 | both halves | 3e-04 |  |
| [[SNAPIN]] | -0.46 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[ALAS1]] | -0.45 | -0.51 / -0.29 | both halves | 2e-04 |  |
| [[TRA2B]] | -0.45 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[UBR1]] | -0.45 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[EIF4A2]] | -0.44 | -0.35 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises REEP5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises REEP5's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 214]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.497). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-5.5, -0.5); signed map (-40.9, -26.0). **Vector** length 89.9, 22.4% of its response variance represented; |z| ≥ 3 in 814 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.2 | +4.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +7.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | +5.3 | +3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +15.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +2.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.4 | -0.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.8 | -19.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Thymol (drug)]] 5 µM |  | -1.6 | +0.6 |
|  | [[Methotrexate (drug)]] 0.5 µM |  | -1.5 | -1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | receptor accessory protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q22.2 — chr5:112,876,385-112,922,289 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DP1, TB2, D5S346, Yip2e, POB16; previously C5orf18 |
| Gene groups (HGNC) | Receptor accessory proteins |
| Hallmark sets | ADIPOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00765](https://www.uniprot.org/uniprotkb/Q00765) (Receptor expression-enhancing protein 5):

> Plays an essential role in heart function and development by regulating the organization and function of the sarcoplasmic reticulum in cardiomyocytes.

**Summary**, from NCBI Gene [7905](https://www.ncbi.nlm.nih.gov/gene/7905):

> Predicted to be involved in endoplasmic reticulum membrane organization. Located in endoplasmic reticulum tubular network. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30077](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30077) · Entrez [7905](https://www.ncbi.nlm.nih.gov/gene/7905) · UniProt [Q00765](https://www.uniprot.org/uniprotkb/Q00765) · Ensembl [ENSG00000129625](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129625)

## Data

Gene col 4991: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4991); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4991, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4991]; `tensor/DDL_lfc|DDL_z.npy` [4991]; `embed/gene_vectors.npy` [4991]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4991 or target_col == 4991). Every well: [[REEP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/REEP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
