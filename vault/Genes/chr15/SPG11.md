---
symbol: "SPG11"
type: "gene"
col: 2418
ensembl_id: "ENSG00000104133"
name: "SPG11 vesicle trafficking associated, spatacsin"
location: "15q21.1"
module: 28
arm: "+"
pooled_cpm: 122.33
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 25
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# SPG11

*SPG11 vesicle trafficking associated, spatacsin* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.30× (z +8.5, q 1e-14, up in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (NCI-H460 7.70×, hTERT-HPNE 3.47×, NCI-H2030 3.05×, LOX-IMVI 2.47×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 4.55×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 1.69×).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (14 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.562× (z -12.7, q 6e-34, down in 44 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.611× (z -11.3, q 4e-27, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DARS1]] (+0.69, fdr 7e-06), [[TRMT10B]] (+0.69, fdr 7e-06), [[MRPS18B]] (+0.67, fdr 7e-06); moves opposite to [[C1orf216]] (-0.65, fdr 7e-06), [[SDHAP4]] (-0.64, fdr 7e-06), [[ANO7]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2418.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (NCI-H460 7.70×, hTERT-HPNE 3.47×, NCI-H2030 3.05×, LOX-IMVI 2.47×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 4.55×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 1.69×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +8.5 | 1e-14 | 26/48 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.24×** | +4.7 | 9e-04 | 22/48 (NCI-H2347, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.19× | +3.7 | 0.035 | 18/50 (AsPC-1, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +3.6 | 0.040 | 20/47 (LS 180, SW480, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.5 | 0.046 | 17/48 (A-172, COLO 205, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.4 | 0.057 | 3/48 (Hs 766T, AsPC-1, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.30× | +3.1 | 0.13 | 11/50 (AsPC-1, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.12× | +3.1 | 0.13 | 7/48 (SW480, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 19 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2418.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.562×** | -12.7 | 6e-34 | 44/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.558×** | -12.3 | 2e-32 | 39/45 (H4, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.611×** | -11.3 | 4e-27 | 44/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.614×** | -11.2 | 9e-27 | 34/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.622×** | -10.9 | 2e-25 | 41/48 (SW480, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.636×** | -10.3 | 4e-23 | 33/49 (KATO III, COLO 205, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.629×** | -10.2 | 2e-22 | 43/47 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -9.4 | 3e-19 | 34/49 (A549, A498, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.677×** | -8.6 | 6e-16 | 33/44 (Panc 03.27, C-33 A, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.693×** | -8.4 | 2e-15 | 30/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.696×** | -8.3 | 6e-15 | 33/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.520×** | -7.8 | 3e-13 | 29/38 (SK-MEL-2, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.724×** | -7.4 | 6e-12 | 29/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.824×** | -6.2 | 2e-08 | 23/48 (J82, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.766×** | -6.1 | 4e-08 | 31/48 (A-172, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.763×** | -5.8 | 2e-07 | 31/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.618×** | -5.8 | 3e-07 | 28/48 (A-427, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.628×** | -5.6 | 7e-07 | 32/49 (PANC-1, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.832×** | -4.2 | 6e-04 | 21/47 (RPMI-7951, LOX-IMVI, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.883× | -4.0 | 0.001 | 12/49 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.846× | -3.8 | 0.003 | 21/48 (A549, SW 1271, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.820×** | -3.2 | 0.023 | 17/49 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Aprepitant (drug)]] 0.05 µM |  | 0.873× | -3.1 | 0.034 | 15/48 (NCI-H460, SW1417, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.831×** | -3.0 | 0.044 | 17/48 (PANC-1, HEC-1-A, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.871× | -3.0 | 0.048 | 16/47 (SW48, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2418. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 128 | 3 (1 ⚠) | 12 (10 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.70× (z +47.7) | [[Digitoxin (drug)]] 5 µM 0.333× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.541× (z -10.1) |
| [[SW480 (line)]] | alt | 136 | 0 | 15 (11 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.373× (z -16.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.431× (z -14.4) |
| [[LoVo (line)]] | wt | 163 | 0 | 11 (9 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.292× (z -18.7) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.499× (z -11.0) |
| [[PANC-1 (line)]] | alt | 166 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.346× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.471× (z -13.3) |
| [[A-172 (line)]] | wt | 137 | 1 | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.407× (z -13.0) |
| [[HT-29 (line)]] | alt | 155 | 0 | 6 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.129× (z -14.6) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.425× (z -11.7) |
| [[KATO III (line)]] | alt | 185 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.529× (z -9.0) |
| [[LS 180 (line)]] | wt | 130 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +10.4) | [[Digitoxin (drug)]] 5 µM 0.309× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 154 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.283× (z -14.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 71.8 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.9) | [[PH-797804 (drug)]] 5 µM 0.142× (z -12.0) |
| [[COLO 205 (line)]] | alt | 284 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[HCT15 (line)]] | alt | 145 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.157× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.437× (z -8.7) |
| [[J82 (line)]] | alt | 105 | 0 | 5 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.353× (z -13.4) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.634× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 149 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[Panc 03.27 (line)]] | alt | 117 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[RPMI-7951 (line)]] | alt | 175 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +12.5) | [[Dinaciclib (drug)]] 0.05 µM 0.412× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.450× (z -9.4) |
| [[SNU-1 (line)]] | wt | 106 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -9.2) |
| [[SNU-423 (line)]] | alt | 107 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.383× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.456× (z -10.0) |
| [[A549 (line)]] | wt | 105 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -15.7) |
| [[AsPC-1 (line)]] | alt | 108 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.383× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[Hs 766T (line)]] | wt | 133 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.341× (z -12.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 124 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.400× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 104 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +17.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.389× (z -9.7) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.444× (z -8.7) |
| [[RKO (line)]] | wt | 111 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0561× (z -29.5) ⚠ toxic |
| [[A498 (line)]] | wt | 138 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -11.7) |
| [[C32 (line)]] | wt | 90.0 | 0 | 2 (1 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.352× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 133 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.477× (z -9.1) |
| [[H4 (line)]] | wt | 125 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -19.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 92.5 | 0 | 2 (1 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.352× (z -10.0) |
| [[HOP62 (line)]] | alt | 88.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -8.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[hTERT-HPNE (line)]] | wt | 104 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +18.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.348× (z -10.6) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 108 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -13.9) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 116 | 0 | 2 | — | [[Sunitinib (drug)]] 0.05 µM 0.0719× (z -11.3) |
| [[SW48 (line)]] | wt | 99.6 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.292× (z -9.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[BT-474 (line)]] | alt | 69.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.371× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[C-33 A (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -21.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[CHP-212 (line)]] | wt | 138 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0768× (z -16.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 122 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.658× (z -8.9) |
| [[HS-578T (line)]] | alt | 73.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +11.0) | — |
| [[LOX-IMVI (line)]] | wt | 80.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +13.9) | — |
| [[NCI-H596 (line)]] | alt | 121 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.138× (z -8.9) |
| [[SHP-77 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.460× (z -9.2) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0812× (z -17.4) ⚠ toxic |
| [[SW 900 (line)]] | alt | 85.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.389× (z -9.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 118 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.415× (z -9.4) |
| [[AN3 CA (line)]] | alt | 99.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 107 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2418), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DARS1]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[TRMT10B]] | +0.69 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[MRPS18B]] | +0.67 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[CEP350]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[LRRC37A2]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[LINC01473]] | +0.64 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[THAP5]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[BPTF]] | +0.63 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[STX17]] | +0.62 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[TIMM17B]] ⚠ | +0.62 | +0.62 / +0.59 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ZC3H6]] | +0.60 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[CHMP4A]] | +0.60 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[TRIP11]] | +0.60 | +0.68 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1orf216]] | -0.65 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[SDHAP4]] | -0.64 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[ANO7]] | -0.60 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[USP35]] | -0.56 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[ABHD17A]] | -0.56 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[AHSA1]] | -0.56 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[MFSD14B]] | -0.56 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[RNF4]] | -0.56 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[HAGLR]] | -0.56 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[UBE2G1]] | -0.55 | -0.70 / -0.44 | both halves | 3e-05 |  |
| [[SNHG30]] | -0.54 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[KLHL25]] | -0.54 | -0.58 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.608). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-26.1, 7.4); signed map (6.1, -16.7). **Vector** length 100.0, 31.1% of its response variance represented; |z| ≥ 3 in 1,250 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.6 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +9.3 | +2.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.1 | +8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +8.2 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.7 | +2.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.6 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +3.6 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.6 | +0.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -9.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.5 | -6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.2 | -12.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.4 | -11.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.4 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -10.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -0.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -8.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.2 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | SPG11 vesicle trafficking associated, spatacsin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.1 — chr15:44,554,818-44,663,688 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21439; previously KIAA1840, ALS5 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JI7](https://www.uniprot.org/uniprotkb/Q96JI7) (Spatacsin):

> May play a role in neurite plasticity by maintaining cytoskeleton stability and regulating synaptic vesicle transport.

**Summary**, from NCBI Gene [80208](https://www.ncbi.nlm.nih.gov/gene/80208):

> The protein encoded by this gene is a potential transmembrane protein that is phosphorylated upon DNA damage. Defects in this gene are a cause of spastic paraplegia type 11 (SPG11). Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2009]

**Accessions** — [HGNC:11226](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11226) · Entrez [80208](https://www.ncbi.nlm.nih.gov/gene/80208) · UniProt [Q96JI7](https://www.uniprot.org/uniprotkb/Q96JI7) · Ensembl [ENSG00000104133](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104133)

## Data

Gene col 2418: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2418); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2418, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2418]; `tensor/DDL_lfc|DDL_z.npy` [2418]; `embed/gene_vectors.npy` [2418]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2418 or target_col == 2418). Every well: [[SPG11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPG11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
