---
symbol: "MT-ND5"
type: "gene"
col: 12675
ensembl_id: "ENSG00000198786"
name: "mitochondrially encoded NADH:ubiquinone oxidoreductase core subunit 5"
location: "mitochondria"
module: null
arm: null
pooled_cpm: 1385.13
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# MT-ND5

*mitochondrially encoded NADH:ubiquinone oxidoreductase core subunit 5* — mitochondria

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.74× (z +14.6, q 1e-45, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bosentan (hydrate) (drug)]] 5 µM: 1.47× (z +3.5, q 0.075, up in 43 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 14 lines (LoVo 7.68×, SW480 5.80×, A498 6.25×, SNU-423 5.10×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-423 4.78×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.186× (z -15.8, q 0e+00, down in 48 of 48 measured lines) ⚠ transcription drop. The strongest without an alert is [[Pentamidine (isethionate) (drug)]] 5 µM: 0.364× (z -13.4, q 1e-38, down in 47 of 48 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12675.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 14 lines (LoVo 7.68×, SW480 5.80×, A498 6.25×, SNU-423 5.10×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-423 4.78×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.74×** | +14.6 | 1e-45 | 49/49 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.20×** | +13.0 | 6e-36 | 44/44 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.16×** | +10.0 | 3e-21 | 45/45 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.075 | 43/47 (SNU-423, HepG2/C3A, …) | top dose only | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.91× | +3.2 | 0.17 | 24/38 (NCI-H2347, SNU-423, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Mebendazole (drug)]] 0.5 µM |  | 1.39× | +3.1 | 0.17 | 45/48 (hTERT-HPNE, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12675.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.186×** | -15.8 | 0e+00 | 48/48 (NCI-H23, SHP-77, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.364×** | -13.4 | 1e-38 | 47/48 (Hs 766T, PANC-1, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.390×** | -8.8 | 2e-16 | 41/48 (RKO, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.515×** | -8.8 | 2e-16 | 44/49 (NCI-H460, Hs 766T, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.486×** | -6.8 | 1e-09 | 39/48 (RKO, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.502×** | -6.5 | 9e-09 | 38/48 (RKO, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.535×** | -5.9 | 3e-07 | 35/48 (RKO, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.585×** | -5.0 | 3e-05 | 37/48 (LS 180, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.647×** | -4.1 | 0.003 | 47/47 (SHP-77, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.685×** | -3.6 | 0.022 | 44/48 (SW 1271, SNU-423, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[crizotinib (drug)]] 5 µM |  | **0.694×** | -3.3 | 0.050 | 34/48 (Hs 766T, H4, …) | top dose only |  |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.706×** | -3.3 | 0.050 | 42/47 (NCI-H23, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | **0.789×** | -3.2 | 0.070 | 27/48 (LOX-IMVI, HEC-1-A, …) | rises with dose |  |
| [[Pimozide (drug)]] 5 µM |  | **0.724×** | -3.0 | 0.096 | 45/48 (SK-MEL-2, RKO, …) | top dose only | position effect removed |
| [[Voriconazole (drug)]] 5 µM |  | **0.726×** | -3.0 | 0.098 | 41/48 (SW1417, PANC-1, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12675. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 1,139 | 3 (3 ⚠) | 5 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.61× (z +13.2) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -13.4) |
| [[C-33 A (line)]] | alt | 1,101 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +9.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.249× (z -12.2) |
| [[H4 (line)]] | wt | 1,061 | 2 (2 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.99× (z +11.0) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.159× (z -18.6) |
| [[Hs 766T (line)]] | wt | 1,524 | 2 (2 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +10.6) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.128× (z -25.7) |
| [[SW1417 (line)]] | alt | 1,520 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +12.2) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.177× (z -14.8) ⚠ transcription drop · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.443× (z -9.8) |
| [[A-172 (line)]] | wt | 865 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.28× (z +13.4) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.329× (z -11.5) |
| [[A498 (line)]] | wt | 1,253 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.25× (z +14.6) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.187× (z -18.8) |
| [[A549 (line)]] | wt | 1,347 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +13.8) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.133× (z -22.0) |
| [[CFPAC-1 (line)]] | alt | 890 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +11.3) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.227× (z -11.8) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.393× (z -10.5) |
| [[HOP62 (line)]] | alt | 801 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 6.33× (z +13.3) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.230× (z -14.9) |
| [[MIA PaCa-2 (line)]] | alt | 1,096 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.15× (z +11.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.142× (z -18.1) |
| [[NCI-H1792 (line)]] | alt | 809 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.67× (z +13.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.253× (z -15.6) |
| [[NCI-H2030 (line)]] | alt | 1,772 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +11.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.167× (z -19.5) |
| [[PANC-1 (line)]] | alt | 1,962 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +12.8) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.128× (z -24.4) |
| [[RKO (line)]] | wt | 1,543 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +12.2) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -14.1) |
| [[SNU-1 (line)]] | wt | 1,012 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +13.1) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.226× (z -15.9) |
| [[SW 900 (line)]] | alt | 1,414 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +11.6) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.208× (z -17.1) |
| [[SW480 (line)]] | alt | 1,041 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +14.7) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.248× (z -16.5) |
| [[A-427 (line)]] | wt | 2,515 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +9.4) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.102× (z -19.0) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.237× (z -16.9) |
| [[AN3 CA (line)]] | alt | 1,028 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.79× (z +12.5) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.188× (z -16.9) |
| [[BT-474 (line)]] | alt | 1,841 | 0 | 5 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.157× (z -16.0) ⚠ transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.285× (z -10.9) |
| [[C32 (line)]] | wt | 1,107 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +11.3) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.338× (z -11.9) |
| [[COLO 205 (line)]] | alt | 1,124 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.77× (z +13.4) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.150× (z -14.4) ⚠ transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.254× (z -10.4) |
| [[HS-578T (line)]] | alt | 877 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.47× (z +12.3) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.241× (z -14.4) |
| [[hTERT-HPNE (line)]] | wt | 912 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +11.6) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.284× (z -9.2) |
| [[LoVo (line)]] | wt | 1,148 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 7.68× (z +15.1) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.175× (z -12.9) ⚠ transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.275× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 2,030 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.70× (z +12.7) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.201× (z -18.7) |
| [[NCI-H2347 (line)]] | alt | 1,073 | 4 (4 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +12.1) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.207× (z -12.8) ⚠ transcription drop |
| [[NCI-H460 (line)]] | wt | 1,680 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.90× (z +13.2) ⚠ toxic; transcription drop | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.161× (z -19.2) |
| [[SHP-77 (line)]] | alt | 2,498 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +11.6) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.106× (z -20.2) ⚠ transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.310× (z -10.5) |
| [[SNU-423 (line)]] | alt | 1,740 | 4 (4 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +14.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.207× (z -13.9) ⚠ transcription drop |
| [[SW 1271 (line)]] | alt | 847 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 5.11× (z +10.1) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.217× (z -13.5) |
| [[CHP-212 (line)]] | wt | 1,027 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +11.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.171× (z -13.2) ⚠ transcription drop |
| [[HCT15 (line)]] | alt | 1,133 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.12× (z +13.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.219× (z -11.2) ⚠ transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 1,323 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +12.8) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.198× (z -12.7) ⚠ transcription drop |
| [[HT-29 (line)]] | alt | 1,102 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +12.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.207× (z -12.9) ⚠ transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.336× (z -8.9) |
| [[J82 (line)]] | alt | 1,362 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +9.0) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.174× (z -13.2) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.433× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 1,013 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.33× (z +13.6) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.223× (z -11.1) ⚠ transcription drop |
| [[NCI-H23 (line)]] | alt | 3,114 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +12.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.105× (z -21.0) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.301× (z -15.8) |
| [[Panc 03.27 (line)]] | alt | 830 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.09× (z +14.0) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.242× (z -11.1) ⚠ transcription drop |
| [[AsPC-1 (line)]] | alt | 940 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.90× (z +12.1) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.209× (z -11.9) ⚠ transcription drop |
| [[HepG2_C3A (line)]] | wt | 907 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +8.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.309× (z -11.9) |
| [[KATO III (line)]] | alt | 2,220 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.68× (z +12.4) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.140× (z -15.6) ⚠ transcription drop |
| [[SW 1088 (line)]] | alt | 974 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.30× (z +11.7) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.195× (z -10.4) ⚠ transcription drop · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.382× (z -8.6) |
| [[SW48 (line)]] | wt | 1,532 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +10.1) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.170× (z -14.1) ⚠ transcription drop |
| [[NCI-H661 (line)]] | alt | 1,651 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.131× (z -12.7) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.323× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 810 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 1,881 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +10.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.0937× (z -19.8) ⚠ transcription drop |
| [[NCI-H2122 (line)]] | alt | 1,247 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1,327 | 0 | 0 | — | — |

## Genes that move with it

Not in the vector space, so no gene relations.

## Genes that move opposite

Not in the vector space, so no gene relations.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

Not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). Its drug and cell-line tables above are complete all the same.

## What is on record

|  |  |
|---|---|
| Name | mitochondrially encoded NADH:ubiquinone oxidoreductase core subunit 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | mitochondria — chrMT:12,337-14,148 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ND5, NAD5; previously MTND5 |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase core subunits; Mitochondrially encoded protein coding genes |
| Reactome | 17 pathways, smallest: FASTK family proteins regulate processing and stability of mitochondrial RNAs; tRNA processing in the mitochondrion; Mitochondrial mRNA modification |
| Matched by | ensembl_id |

**Function**, from UniProt [P03915](https://www.uniprot.org/uniprotkb/P03915) (NADH-ubiquinone oxidoreductase chain 5):

> Core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I) which catalyzes electron transfer from NADH through the respiratory chain, using ubiquinone as an electron acceptor. Essential for the catalytic activity and assembly of complex I.

**Summary**, from NCBI Gene [4540](https://www.ncbi.nlm.nih.gov/gene/4540):

> Enables NADH dehydrogenase (ubiquinone) activity. Involved in mitochondrial electron transport, NADH to ubiquinone and mitochondrial respiratory chain complex I assembly. Located in mitochondrial inner membrane. Part of respiratory chain complex I. Implicated in Leber hereditary optic neuropathy; Leigh disease; and MELAS syndrome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7461](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7461) · Entrez [4540](https://www.ncbi.nlm.nih.gov/gene/4540) · UniProt [P03915](https://www.uniprot.org/uniprotkb/P03915) · Ensembl [ENSG00000198786](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198786)

## Data

Gene col 12675: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12675); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12675, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12675]; `tensor/DDL_lfc|DDL_z.npy` [12675]; `embed/gene_vectors.npy` [12675]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12675 or target_col == 12675). Every well: [[MT-ND5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT-ND5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
