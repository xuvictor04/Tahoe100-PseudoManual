---
symbol: "VOPP1"
type: "gene"
col: 7859
ensembl_id: "ENSG00000154978"
name: "VOPP1 WW domain binding protein"
location: "7p11.2"
module: 11
arm: "-"
pooled_cpm: 175.64
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# VOPP1

*VOPP1 WW domain binding protein* — 7p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.63× (z +16.2, q 0e+00, up in 31 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.19× (z +8.1, q 9e-14, up in 19 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.291× (z -57.5, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAK1]] (+0.60, fdr 8e-06), [[C12orf75]] (+0.54, fdr 1e-05), [[MGAT4A]] (+0.52, fdr 1e-05); moves opposite to [[SDE2]] (-0.54, fdr 2e-05), [[TBCC]] (-0.53, fdr 4e-05), [[ATRIP]] (-0.52, fdr 3e-05).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MGAT4A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7859.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +16.2 | 0e+00 | 31/47 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +10.6 | 9e-24 | 25/42 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +8.1 | 9e-14 | 19/46 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.27×** | +7.8 | 1e-12 | 27/47 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.24×** | +6.5 | 8e-09 | 21/43 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +5.3 | 1e-05 | 19/46 (NCI-H1573, C32, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.16× | +5.0 | 4e-05 | 16/46 (AsPC-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.17× | +4.9 | 6e-05 | 17/45 (NCI-H1573, NCI-H2347, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.11× | +4.9 | 7e-05 | 8/46 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.15× | +4.7 | 1e-04 | 16/46 (NCI-H1573, SNU-423, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +4.5 | 4e-04 | 11/47 (Panc 03.27, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.14× | +4.5 | 4e-04 | 12/45 (SNU-423, NCI-H2347, …) | rises with dose |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | 1.13× | +3.8 | 0.006 | 7/45 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.12× | +3.6 | 0.011 | 14/45 (C32, SNU-423, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.012 | 13/47 (NCI-H1573, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 1.11× | +3.4 | 0.022 | 9/46 (NCI-H1792, BT-474, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.032 | 13/46 (NCI-H2347, RPMI-7951, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.037 | 14/44 (NCI-H2347, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.10× | +3.2 | 0.038 | 6/46 (RKO, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.10× | +3.1 | 0.055 | 13/46 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.07× | +3.0 | 0.065 | 3/47 (Panc 03.27, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7859.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.291×** | -57.5 | 0e+00 | 45/46 (COLO 205, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.415×** | -29.0 | 0e+00 | 39/46 (Panc 03.27, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.544×** | -19.3 | 0e+00 | 35/46 (COLO 205, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.711×** | -15.9 | 0e+00 | 36/47 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.685×** | -12.5 | 2e-33 | 35/46 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.696×** | -12.0 | 6e-31 | 34/46 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.744×** | -9.7 | 2e-20 | 32/46 (Panc 03.27, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.818×** | -9.3 | 8e-19 | 22/46 (AsPC-1, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -7.6 | 2e-12 | 0/48 | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.806×** | -7.1 | 8e-11 | 25/46 (SW480, LOX-IMVI, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.674×** | -6.8 | 6e-10 | 25/47 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.816×** | -6.7 | 1e-09 | 23/46 (Panc 03.27, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.820×** | -6.3 | 2e-08 | 21/46 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.830×** | -6.1 | 3e-08 | 22/46 (A-427, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.822×** | -6.1 | 4e-08 | 23/46 (SW480, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.868× | -4.6 | 1e-04 | 19/46 (SW1417, LOX-IMVI, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.870× | -4.6 | 1e-04 | 15/46 (LOX-IMVI, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.864× | -4.4 | 2e-04 | 13/45 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.786×** | -4.1 | 9e-04 | 16/46 (LS 180, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7859. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 251 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -39.6) |
| [[COLO 205 (line)]] | alt | 385 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0963× (z -47.0) |
| [[Panc 03.27 (line)]] | alt | 229 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -44.1) |
| [[SW480 (line)]] | alt | 451 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -27.7) |
| [[SW1417 (line)]] | alt | 296 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -36.3) |
| [[A-427 (line)]] | wt | 182 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -19.7) |
| [[NCI-H1573 (line)]] | alt | 606 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -32.2) |
| [[A-172 (line)]] | wt | 331 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -30.5) |
| [[A498 (line)]] | wt | 200 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +15.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -25.9) |
| [[AsPC-1 (line)]] | alt | 168 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -35.3) |
| [[BT-474 (line)]] | alt | 137 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -27.0) |
| [[C32 (line)]] | wt | 117 | 1 | 4 | [[TAK-901 (drug)]] 0.05 µM 2.12× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -28.3) |
| [[CFPAC-1 (line)]] | alt | 91.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -21.5) |
| [[HEC-1-A (line)]] | alt | 215 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -30.8) |
| [[HOP62 (line)]] | alt | 101 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 1.82× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -28.1) |
| [[HT-29 (line)]] | alt | 189 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -33.8) |
| [[KATO III (line)]] | alt | 195 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -32.2) |
| [[LoVo (line)]] | wt | 84.0 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +13.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -33.3) |
| [[NCI-H1792 (line)]] | alt | 187 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.42× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -28.4) |
| [[PANC-1 (line)]] | alt | 132 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -39.0) |
| [[SW 900 (line)]] | alt | 133 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -32.8) |
| [[A549 (line)]] | wt | 94.3 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.25× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -22.4) |
| [[Hs 766T (line)]] | wt | 147 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -31.0) |
| [[HS-578T (line)]] | alt | 99.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -17.1) |
| [[NCI-H2347 (line)]] | alt | 140 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -15.5) |
| [[RKO (line)]] | wt | 170 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -18.2) |
| [[J82 (line)]] | alt | 120 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -21.7) |
| [[LS 180 (line)]] | wt | 152 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -27.4) |
| [[MIA PaCa-2 (line)]] | alt | 69.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -14.1) |
| [[NCI-H2030 (line)]] | alt | 56.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 2.59× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -17.3) |
| [[RPMI-7951 (line)]] | alt | 132 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -16.0) |
| [[SNU-423 (line)]] | alt | 124 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +13.4) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 191 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -22.8) |
| [[AN3 CA (line)]] | alt | 147 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -15.8) |
| [[H4 (line)]] | wt | 188 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -17.1) |
| [[HCT15 (line)]] | alt | 78.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 146 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -13.7) |
| [[hTERT-HPNE (line)]] | wt | 99.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -15.3) |
| [[SW 1088 (line)]] | alt | 152 | 0 | 2 | — | [[Sildenafil (drug)]] 0.05 µM 0.0679× (z -11.1) |
| [[CHP-212 (line)]] | wt | 68.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 105 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -15.2) |
| [[SNU-1 (line)]] | wt | 134 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -16.4) |
| [[C-33 A (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 40.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.3 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 140 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7859), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAK1]] | +0.60 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[C12orf75]] | +0.54 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[MGAT4A]] | +0.52 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[COBL]] | +0.52 | +0.39 / +0.53 | both halves | 5e-05 |  |
| [[MAPK9]] | +0.50 | +0.37 / +0.49 | both halves | 9e-05 |  |
| [[OSBPL3]] | +0.50 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[LAPTM4B]] | +0.49 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[RALGPS1]] | +0.49 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[CACNG4]] | +0.48 | +0.28 / +0.50 | both halves | 3e-04 |  |
| [[ENTREP2]] | +0.48 | +0.28 / +0.46 | both halves | 3e-04 |  |
| [[PTK7]] | +0.48 | +0.54 / +0.36 | both halves | 1e-04 |  |
| [[RAPGEF5]] | +0.47 | +0.50 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*59 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDE2]] | -0.54 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[TBCC]] | -0.53 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[ATRIP]] | -0.52 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[MRPL2]] | -0.52 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[RBM8A]] | -0.51 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[HSCB]] | -0.51 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[ZNF181]] | -0.50 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[YJU2B]] | -0.50 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[TXNL4B]] | -0.49 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[ZNF419]] | -0.49 | -0.49 / -0.40 | both halves | 4e-05 |  |
| [[C1orf131]] | -0.49 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[CPT2]] | -0.49 | -0.47 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MGAT4A]] | B | MGAT4A activity strengthens VOPP1's drug response | lines that do not express MGAT4A (10) vs lines expressing it (37) | the lines without MGAT4A respond 0.89× as strongly (z diff +1.05); strongest at Harringtonine 5 µM: 0.76x vs 0.47x (z diff +5.0) | 0.071 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, ZNF860, EPHA2; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.457). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-38.5, 7.5); signed map (-16.3, 36.2). **Vector** length 104, 26.8% of its response variance represented; |z| ≥ 3 in 1,414 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.6 | +8.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.5 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.3 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +16.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.5 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +5.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +4.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -19.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.8 | -9.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.6 | -9.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.9 | -57.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.6 | -1.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.4 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -4.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -2.3 | -0.9 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | -2.2 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | VOPP1 WW domain binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p11.2 — chr7:55,436,056-55,572,988 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ECop, GASP, FLJ20532, DKFZp564K0822, WBP1L2 |
| Gene groups (HGNC) | WBP1/VOPP1 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AW1](https://www.uniprot.org/uniprotkb/Q96AW1) (WW domain binding protein VOPP1):

> Increases the transcriptional activity of NFKB1 by facilitating its nuclear translocation, DNA-binding and associated apoptotic response, when overexpressed. May sequester WWOX in lysosomal vesicles and thereby regulate WWOX role as tumor suppressor.

**Summary**, from NCBI Gene [81552](https://www.ncbi.nlm.nih.gov/gene/81552):

> Enables enzyme binding activity and protein sequestering activity. Predicted to be involved in DNA-templated transcription. Located in cytoplasmic vesicle membrane; late endosome; and lysosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:34518](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34518) · Entrez [81552](https://www.ncbi.nlm.nih.gov/gene/81552) · UniProt [Q96AW1](https://www.uniprot.org/uniprotkb/Q96AW1) · Ensembl [ENSG00000154978](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154978)

## Data

Gene col 7859: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7859); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7859, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7859]; `tensor/DDL_lfc|DDL_z.npy` [7859]; `embed/gene_vectors.npy` [7859]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7859 or target_col == 7859). Every well: [[VOPP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VOPP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
