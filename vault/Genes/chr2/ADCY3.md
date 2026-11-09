---
symbol: "ADCY3"
type: "gene"
col: 6110
ensembl_id: "ENSG00000138031"
name: "adenylate cyclase 3"
location: "2p23.3"
module: 18
arm: "+"
pooled_cpm: 23.75
n_lines_expressing: 45
n_dd_up: 20
n_dd_down: 15
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 17
direction_downstream: 46
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# ADCY3

*adenylate cyclase 3* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.88× (z +17.5, q 0e+00, up in 36 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.438× (z -22.9, q 0e+00, down in 37 of 43 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.458× (z -14.7, q 0e+00, down in 28 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BEND3]] (+0.78, fdr 7e-06), [[UCK2]] (+0.75, fdr 7e-06), [[MACROD1]] (+0.74, fdr 7e-06); moves opposite to [[DNAL4]] (-0.58, fdr 2e-05), [[ASB8]] (-0.57, fdr 1e-05), [[MAP3K13]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[NCS1]] → it (grade B ⚠); 46 go from it, the strongest it → [[B4GALT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6110.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +17.5 | 0e+00 | 36/42 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.66×** | +10.0 | 5e-21 | 29/42 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.55×** | +8.3 | 1e-14 | 23/40 (SW480, SHP-77, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.49×** | +7.5 | 9e-12 | 19/30 (Panc 03.27, C32, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +7.2 | 9e-11 | 22/42 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.42×** | +6.8 | 7e-10 | 20/42 (NCI-H460, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.40×** | +6.7 | 2e-09 | 21/42 (SW480, HCT15, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.29×** | +4.8 | 1e-04 | 16/41 (SW480, A498, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.24×** | +4.3 | 1e-03 | 11/42 (NCI-H460, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.27×** | +4.3 | 1e-03 | 14/39 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.24×** | +4.3 | 1e-03 | 19/41 (SNU-423, C32, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.24×** | +4.1 | 0.002 | 12/43 (NCI-H460, RPMI-7951, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +4.0 | 0.003 | 9/39 (NCI-H1573, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.004 | 10/41 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +3.8 | 0.006 | 11/42 (AsPC-1, LoVo, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.031 | 8/41 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | 1.18× | +3.2 | 0.040 | 6/42 (A498, NCI-H460, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.059 | 7/42 (A498, NCI-H460, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +3.0 | 0.068 | 12/42 (NCI-H460, CFPAC-1, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.068 | 7/42 (A498, NCI-H460, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.070 | 8/40 (NCI-H460, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.071 | 7/42 (A498, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | 1.17× | +2.9 | 0.083 | 8/42 (AsPC-1, NCI-H460, …) | rises with dose | position effect removed |
| [[vincristine (drug)]] 5 µM |  | **1.33×** | +2.9 | 0.083 | 2/39 (NCI-H460, NCI-H1573) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6110.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.438×** | -22.9 | 0e+00 | 37/43 (NCI-H2030, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.458×** | -14.7 | 0e+00 | 28/43 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.604×** | -9.9 | 8e-21 | 25/43 (A-427, RKO, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.434×** | -8.6 | 1e-15 | 27/43 (A-427, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.711×** | -6.7 | 2e-09 | 23/43 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.740×** | -5.9 | 3e-07 | 23/43 (SW48, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.754×** | -5.5 | 3e-06 | 22/43 (SW48, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.790×** | -4.5 | 6e-04 | 14/42 (NCI-H23, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.815×** | -4.4 | 7e-04 | 11/43 (SW480, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.809×** | -4.2 | 0.002 | 13/42 (SW1417, LoVo, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.842× | -4.0 | 0.003 | 16/43 (SW480, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.678×** | -4.0 | 0.003 | 10/39 (RKO, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.942× | -3.9 | 0.004 | 4/43 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.686×** | -3.9 | 0.004 | 13/42 (A-427, A498, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.833×** | -3.8 | 0.005 | 15/43 (SW480, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.766×** | -3.7 | 0.007 | 8/41 (LS 180, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.852× | -3.6 | 0.009 | 14/43 (SW480, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.835× | -3.5 | 0.012 | 12/42 (SNU-423, A498, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.855× | -3.1 | 0.054 | 5/43 (A-427, HT-29, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.856× | -3.1 | 0.055 | 12/42 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6110. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 67.8 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.130× (z -19.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.204× (z -14.5) |
| [[A-427 (line)]] | wt | 64.1 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0688× (z -28.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.164× (z -18.5) |
| [[NCI-H460 (line)]] | wt | 24.1 | 3 (2 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +14.5) | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -15.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.343× (z -9.4) |
| [[SNU-1 (line)]] | wt | 43.3 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0718× (z -15.0) ⚠ toxic; cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -9.2) |
| [[SW48 (line)]] | wt | 80.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -13.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.235× (z -11.2) |
| [[LoVo (line)]] | wt | 27.4 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -13.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.337× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 31.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -15.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.286× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 35.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -18.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.221× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 42.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -16.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.214× (z -13.1) |
| [[PANC-1 (line)]] | alt | 24.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -19.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.396× (z -9.0) |
| [[SW480 (line)]] | alt | 40.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +13.2) | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -12.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 27.7 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.233× (z -11.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A498 (line)]] | wt | 35.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -13.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A549 (line)]] | wt | 35.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -9.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[J82 (line)]] | alt | 26.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -12.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.369× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 24.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.77× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Harringtonine (drug)]] 5 µM 0.259× (z -8.9) |
| [[SHP-77 (line)]] | alt | 26.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.230× (z -9.8) |
| [[AN3 CA (line)]] | alt | 51.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -9.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[BT-474 (line)]] | alt | 8.27 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0347× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 64.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.339× (z -8.5) |
| [[LS 180 (line)]] | wt | 9.66 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -8.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H1573 (line)]] | alt | 7.96 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -9.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 10.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 38.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -20.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SK-MEL-2 (line)]] | alt | 28.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.240× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.37 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.66 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 26.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6110), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BEND3]] | +0.78 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[UCK2]] | +0.75 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[MACROD1]] | +0.74 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[GART]] | +0.73 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[ANKRD13B]] | +0.71 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[TMTC4]] | +0.70 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[SLC25A15]] | +0.69 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[CMTM4]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[ADAT2]] | +0.68 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[LETM1]] | +0.68 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[TCOF1]] | +0.67 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[TYRO3]] | +0.66 | +0.65 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAL4]] | -0.58 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[ASB8]] | -0.57 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[MAP3K13]] | -0.56 | -0.63 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 12, C 5. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCS1]] | B | NCS1 activity raises ADCY3's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 2.88× lower at baseline in the lines without NCS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[MSI1]] | B | MSI1 activity raises ADCY3's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.08× lower at baseline in the lines without MSI1 | 0.020 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[BRSK2]] | B | BRSK2 activity raises ADCY3's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 2.74× lower at baseline in the lines without BRSK2 | 0.029 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[DLX1]] | B | DLX1 activity raises ADCY3's level | lines that do not express DLX1 (13) vs lines expressing it (37) | 2.09× lower at baseline in the lines without DLX1 | 0.038 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1 |
| [[NT5M]] | B | NT5M activity raises ADCY3's level | lines that do not express NT5M (7) vs lines expressing it (43) | 2.47× lower at baseline in the lines without NT5M | 0.042 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[MAF]] | B | MAF activity lowers ADCY3's level | lines that do not express MAF (27) vs lines expressing it (23) | 1.49× higher at baseline in the lines without MAF | 0.060 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |
| [[MAP2K1]] | B | MAP2K1 activity raises ADCY3's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GBX2-AS1]] | B | GBX2-AS1 activity raises ADCY3's level | lines that do not express GBX2-AS1 (13) vs lines expressing it (37) | 1.79× lower at baseline in the lines without GBX2-AS1 | 0.072 | ⚠ within organs, on part of the lines; also absent: ANTXR1, KCNK13, TTC7B |
| [[FGD1]] | B | FGD1 activity raises ADCY3's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 1.70× lower at baseline in the lines without FGD1 | 0.075 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |
| [[MAF]] | B | MAF activity weakens ADCY3's drug response | lines that do not express MAF (24) vs lines expressing it (19) | the lines without MAF respond 1.06× as strongly (z diff -0.44); strongest at Homoharringtonine 0.5 µM: 0.39x vs 0.78x (z diff -3.7) | 0.083 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1; target measured in part of the lines; both ways; artifact flags |
| [[GALNT14]] | B | GALNT14 activity lowers ADCY3's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.30× higher at baseline in the lines without GALNT14 | 0.086 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[MEX3A]] | B | MEX3A activity raises ADCY3's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 2.69× lower at baseline in the lines without MEX3A | 0.098 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |

### Downstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 46, C 0. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B4GALT2]] | B | ADCY3 activity raises B4GALT2's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.45× lower at baseline in the lines without ADCY3 | 0.004 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[MAPK12]] | B | ADCY3 activity raises MAPK12's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.83× lower at baseline in the lines without ADCY3 | 0.006 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[LYRM4]] | B | ADCY3 activity raises LYRM4's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.54× lower at baseline in the lines without ADCY3 | 0.007 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[ABCC5]] | B | ADCY3 activity raises ABCC5's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 2.00× lower at baseline in the lines without ADCY3 | 0.010 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[STIM1]] | B | ADCY3 activity raises STIM1's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.48× lower at baseline in the lines without ADCY3 | 0.014 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[PUS7]] | B | ADCY3 activity raises PUS7's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without ADCY3 | 0.015 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[USP45]] | B | ADCY3 activity raises USP45's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.27× lower at baseline in the lines without ADCY3 | 0.019 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[CLN6]] | B | ADCY3 activity raises CLN6's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.20× lower at baseline in the lines without ADCY3 | 0.019 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[ANKRD13B]] | B | ADCY3 activity raises ANKRD13B's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.83× lower at baseline in the lines without ADCY3 | 0.020 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[MDN1]] | B | ADCY3 activity raises MDN1's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.32× lower at baseline in the lines without ADCY3 | 0.022 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[XPO5]] | B | ADCY3 activity raises XPO5's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.44× lower at baseline in the lines without ADCY3 | 0.024 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[GATD1]] | B | ADCY3 activity raises GATD1's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.49× lower at baseline in the lines without ADCY3 | 0.025 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.847). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-8.3, -36.9); signed map (-2.8, -53.4). **Vector** length 119, 30.9% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +17.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.6 | +10.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +5.4 | +6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | +4.8 | +8.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +4.8 | +6.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +3.9 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -6.0 | -22.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.8 | -9.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.5 | -14.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.0 | -8.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.8 | -4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.1 | -3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -4.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.8 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | adenylate cyclase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:24,819,169-24,920,237 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AC3 |
| Gene groups (HGNC) | Adenylate cyclases |
| Reactome | 44 pathways, smallest: Adenylate cyclase activating pathway; Adenylate cyclase inhibitory pathway; Olfactory Signaling Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [O60266](https://www.uniprot.org/uniprotkb/O60266) (Adenylate cyclase type 3):

> Catalyzes the formation of the signaling molecule cAMP in response to G protein signaling. Participates in signaling cascades triggered by odorant receptors via its function in cAMP biosynthesis: specifically activated by G alpha protein GNAL/G(olf) in olfactory epithelium (By similarity). Mediates signaling cascades in primary cilia: specifically activated by G alpha protein GNAS/G(s) in primary cilia. Plays a role in regulating food intake and body fat accumulation in the paraventricular …

**Summary**, from NCBI Gene [109](https://www.ncbi.nlm.nih.gov/gene/109):

> This gene encodes adenylyl cyclase 3 which is a membrane-associated enzyme and catalyzes the formation of the secondary messenger cyclic adenosine monophosphate (cAMP). This protein appears to be widely expressed in various human tissues and may be involved in a number of physiological and pathophysiological metabolic processes. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:234](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:234) · Entrez [109](https://www.ncbi.nlm.nih.gov/gene/109) · UniProt [O60266](https://www.uniprot.org/uniprotkb/O60266) · Ensembl [ENSG00000138031](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138031)

## Data

Gene col 6110: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6110); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6110, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6110]; `tensor/DDL_lfc|DDL_z.npy` [6110]; `embed/gene_vectors.npy` [6110]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6110 or target_col == 6110). Every well: [[ADCY3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADCY3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
