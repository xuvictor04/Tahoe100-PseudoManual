---
symbol: "TMEM135"
type: "gene"
col: 9332
ensembl_id: "ENSG00000166575"
name: "transmembrane protein 135"
location: "11q14.2"
module: 86
arm: "+"
pooled_cpm: 108.49
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 19
n_dd_up_clean: 27
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# TMEM135

*transmembrane protein 135* — 11q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.41× (z +7.8, q 4e-12, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.489× (z -16.1, q 0e+00, down in 48 of 49 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[QPRT]] (+0.61, fdr 1e-05), [[ACSL3]] (+0.60, fdr 1e-05), [[CHIC1]] (+0.53, fdr 3e-05); moves opposite to [[PPP1R26-AS1]] (-0.48, fdr 1e-04), [[MAEA]] (-0.48, fdr 2e-04), [[POLE3]] (-0.47, fdr 3e-04).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GALM]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9332.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +7.8 | 4e-12 | 36/48 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.40×** | +7.6 | 1e-11 | 42/48 (A549, LoVo, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.59×** | +7.1 | 3e-10 | 40/47 (A549, RKO, …) | rises with dose |  |
| [[Berbamine (drug)]] 5 µM |  | **1.32×** | +6.3 | 5e-08 | 32/49 (LoVo, A549, …) | top dose only |  |
| [[Bexarotene (drug)]] 0.5 µM |  | **1.47×** | +6.1 | 1e-07 | 34/48 (SW480, KATO III, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.30×** | +6.0 | 2e-07 | 33/48 (AsPC-1, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.87×** | +5.2 | 1e-05 | 38/49 (MIA PaCa-2, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.38×** | +5.2 | 2e-05 | 38/48 (HT-29, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.36×** | +4.9 | 5e-05 | 25/48 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +4.5 | 5e-04 | 31/48 (J82, RKO, …) | top dose only |  |
| [[Bexarotene (drug)]] 0.05 µM |  | **1.32×** | +4.4 | 6e-04 | 30/48 (SW480, C-33 A, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +4.3 | 7e-04 | 28/49 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Penfluridol (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.002 | 29/47 (A549, A-172, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.60×** | +3.9 | 0.004 | 27/49 (J82, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.004 | 28/48 (A549, NCI-H23, …) | rises with dose | plate-row cell shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.004 | 24/48 (SNU-423, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9332.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.489×** | -16.1 | 0e+00 | 48/49 (NCI-H1792, PANC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.567×** | -8.7 | 1e-15 | 29/44 (Panc 03.27, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.617×** | -7.7 | 2e-12 | 33/49 (A-427, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.643×** | -6.8 | 2e-09 | 31/47 (RKO, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.644×** | -6.8 | 2e-09 | 35/48 (hTERT-HPNE, NCI-H23, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.636×** | -6.7 | 2e-09 | 31/45 (C32, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.651×** | -6.6 | 4e-09 | 34/50 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.757×** | -6.3 | 2e-08 | 41/49 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.664×** | -6.3 | 2e-08 | 40/47 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.676×** | -6.2 | 2e-08 | 38/47 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.685×** | -6.0 | 8e-08 | 33/48 (MIA PaCa-2, HCT15, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **0.696×** | -5.8 | 3e-07 | 32/48 (SW 900, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.706×** | -5.5 | 1e-06 | 36/48 (MIA PaCa-2, SW 1088, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.735×** | -4.9 | 3e-05 | 34/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.735×** | -4.9 | 3e-05 | 36/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.739×** | -4.6 | 1e-04 | 35/48 (MIA PaCa-2, NCI-H2030, …) | rises with dose |  |
| [[Clotrimazole (drug)]] 5 µM |  | **0.832×** | -4.2 | 0.001 | 20/49 (HT-29, MIA PaCa-2, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.698×** | -4.1 | 0.001 | 32/48 (MIA PaCa-2, SW 900, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.635×** | -3.8 | 0.005 | 27/46 (CHP-212, H4, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9332. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 153 | 2 (1 ⚠) | 7 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.52× (z +15.1) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 2.66× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -14.3) |
| [[NCI-H460 (line)]] | wt | 144 | 4 (4 ⚠) | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.98× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -13.7) |
| [[SW480 (line)]] | alt | 124 | 3 | 4 (3 ⚠) | [[Bexarotene (drug)]] 0.5 µM 2.43× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -10.9) |
| [[J82 (line)]] | alt | 69.2 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.17× (z +11.1) | — |
| [[NCI-H1792 (line)]] | alt | 140 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -18.3) |
| [[PANC-1 (line)]] | alt | 163 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -17.0) |
| [[A549 (line)]] | wt | 87.4 | 2 | 1 | [[Cepharanthine (drug)]] 5 µM 2.18× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -11.1) |
| [[COLO 205 (line)]] | alt | 134 | 1 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -9.6) |
| [[HT-29 (line)]] | alt | 142 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 82.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -12.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -10.3) |
| [[LoVo (line)]] | wt | 77.1 | 2 | 1 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 1.95× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 88.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -11.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -8.7) |
| [[SNU-1 (line)]] | wt | 242 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -12.7) |
| [[SW 900 (line)]] | alt | 137 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -11.9) |
| [[SW1417 (line)]] | alt | 67.3 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.10× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -8.7) |
| [[A-427 (line)]] | wt | 189 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -8.5) |
| [[C32 (line)]] | wt | 173 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -14.7) |
| [[Hs 766T (line)]] | wt | 213 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[LOX-IMVI (line)]] | wt | 105 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -14.7) |
| [[LS 180 (line)]] | wt | 169 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 131 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -14.2) |
| [[NCI-H23 (line)]] | alt | 97.8 | 1 | 1 | [[Cepharanthine (drug)]] 5 µM 1.79× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -11.7) |
| [[NCI-H2347 (line)]] | alt | 46.8 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.03× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 68.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0857× (z -21.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[RKO (line)]] | wt | 126 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.239× (z -12.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -11.6) |
| [[SW 1088 (line)]] | alt | 91.4 | 0 | 2 | — | [[Ritonavir (drug)]] 0.5 µM 0.0661× (z -9.9) |
| [[A-172 (line)]] | wt | 52.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -9.4) |
| [[A498 (line)]] | wt | 37.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -9.3) |
| [[AN3 CA (line)]] | alt | 159 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -9.2) |
| [[BT-474 (line)]] | alt | 136 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -10.6) |
| [[H4 (line)]] | wt | 100 | 0 | 1 | — | [[Peretinoin (drug)]] 5 µM 0.321× (z -8.5) |
| [[HCT15 (line)]] | alt | 150 | 0 | 1 | — | [[OTS514 (drug)]] 5 µM 0.137× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 117 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HepG2_C3A (line)]] | wt | 85.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -11.3) |
| [[HS-578T (line)]] | alt | 54.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -9.7) |
| [[KATO III (line)]] | alt | 178 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 54.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 48.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 51.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -9.6) |
| [[SW 1271 (line)]] | alt | 174 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.159× (z -8.8) ⚠ toxic |
| [[SW48 (line)]] | wt | 95.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 137 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 156 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9332), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QPRT]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[ACSL3]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[CHIC1]] | +0.53 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[ME1]] | +0.51 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[MMAB]] | +0.51 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[ERG28]] | +0.51 | +0.62 / +0.36 | both halves | 9e-05 |  |
| [[DENND4C]] | +0.51 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[DHCR7]] | +0.51 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[PRXL2A]] | +0.50 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[SC5D]] | +0.49 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[ECH1]] | +0.49 | +0.36 / +0.50 | both halves | 1e-04 |  |
| [[OLMALINC]] | +0.49 | +0.59 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R26-AS1]] | -0.48 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[MAEA]] | -0.48 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[POLE3]] | -0.47 | -0.27 / -0.51 | both halves | 3e-04 |  |
| [[CRYGS]] | -0.46 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[PIGG]] | -0.46 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[ZNF26]] | -0.46 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[DPY19L3]] | -0.45 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[TRPV1]] | -0.45 | -0.18 / -0.54 | ⚠ one half (not replicated) | 1e-03 |  |
| [[SHPK]] | -0.45 | -0.25 / -0.53 | both halves | 4e-04 |  |
| [[RABGEF1]] | -0.45 | -0.29 / -0.56 | both halves | 2e-04 |  |
| [[TOP3A]] | -0.45 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[DPP9]] | -0.44 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[ZNF710]] | -0.44 | -0.31 / -0.53 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALM]] | B | GALM activity lowers TMEM135's level | lines that do not express GALM (11) vs lines expressing it (39) | 1.51× higher at baseline in the lines without GALM | 0.050 | ⚠ within organs, on part of the lines; also absent: ACOT11, GRIN2D, STAP2; maybe low, not absent |
| [[PIR]] | B | PIR activity raises TMEM135's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.28× lower at baseline in the lines without PIR | 0.091 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.543). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.7, -50.7); signed map (-52.3, 34.1). **Vector** length 129, 43.1% of its response variance represented; |z| ≥ 3 in 1,604 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +7.1 | +7.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +6.9 | +6.0 |
|  | [[Berbamine (drug)]] 5 µM |  | +6.7 | +6.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.5 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +7.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +5.8 | +3.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.0 | -16.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -6.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -6.4 | -6.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -5.9 | -5.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -6.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -5.6 | -6.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -5.1 | -6.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -4.1 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 135 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.2 — chr11:87,037,844-87,328,824 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22104, PMP52 |
| Gene groups (HGNC) | Tim17 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UB9](https://www.uniprot.org/uniprotkb/Q86UB9) (Transmembrane protein 135):

> Involved in mitochondrial metabolism by regulating the balance between mitochondrial fusion and fission. May act as a regulator of mitochondrial fission that promotes DNM1L-dependent fission through activation of DNM1L. May be involved in peroxisome organization.

**Summary**, from NCBI Gene [65084](https://www.ncbi.nlm.nih.gov/gene/65084):

> Predicted to be involved in peroxisome organization. Predicted to act upstream of or within several processes, including regulation of oxidative phosphorylation; response to food; and retinal pigment epithelium development. Predicted to be located in peroxisome. Predicted to be active in peroxisomal membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26167](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26167) · Entrez [65084](https://www.ncbi.nlm.nih.gov/gene/65084) · UniProt [Q86UB9](https://www.uniprot.org/uniprotkb/Q86UB9) · Ensembl [ENSG00000166575](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166575)

## Data

Gene col 9332: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9332); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9332, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9332]; `tensor/DDL_lfc|DDL_z.npy` [9332]; `embed/gene_vectors.npy` [9332]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9332 or target_col == 9332). Every well: [[TMEM135 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM135.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
