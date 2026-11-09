---
symbol: "MT-CO3"
type: "gene"
col: 12748
ensembl_id: "ENSG00000198938"
name: "mitochondrially encoded cytochrome c oxidase III"
location: "mitochondria"
module: null
arm: null
pooled_cpm: 305.8
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# MT-CO3

*mitochondrially encoded cytochrome c oxidase III* — mitochondria

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.33× (z +15.1, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mebendazole (drug)]] 0.5 µM: 1.40× (z +3.4, q 0.048, up in 37 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 14 lines (A498 5.80×, LoVo 6.64×, NCI-H1573 5.13×, NCI-H460 5.10×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 4.95×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Pentamidine (isethionate) (drug)]] 5 µM: 0.366× (z -14.7, q 0e+00, down in 45 of 48 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12748.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 14 lines (A498 5.80×, LoVo 6.64×, NCI-H1573 5.13×, NCI-H460 5.10×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 4.95×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.33×** | +15.1 | 0e+00 | 49/49 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.71×** | +13.0 | 3e-36 | 44/44 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.10×** | +10.8 | 6e-25 | 45/45 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **2.25×** | +8.4 | 7e-15 | 47/49 (AsPC-1, KATO III, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +4.5 | 9e-04 | 41/47 (MIA PaCa-2, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.44×** | +3.7 | 0.017 | 42/47 (BT-474, A498, …) | rises with dose | position effect removed |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.048 | 37/48 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.26×** | +3.4 | 0.057 | 40/48 (KATO III, Hs 766T, …) | rises with dose | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.35× | +3.1 | 0.13 | 39/49 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.34× | +3.0 | 0.14 | 36/48 (BT-474, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12748.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.366×** | -14.7 | 0e+00 | 45/48 (A549, PANC-1, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.341×** | -11.1 | 3e-26 | 46/48 (NCI-H23, BT-474, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.531×** | -9.3 | 4e-18 | 42/49 (NCI-H460, Hs 766T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.484×** | -7.5 | 9e-12 | 38/48 (RKO, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.570×** | -5.8 | 7e-07 | 35/48 (RKO, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.609×** | -5.1 | 3e-05 | 32/48 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.637×** | -4.7 | 3e-04 | 31/48 (LS 180, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.661×** | -4.3 | 0.001 | 32/48 (C32, SW 900, …) | top dose only |  |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | **0.714×** | -3.2 | 0.079 | 38/48 (NCI-H23, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.738×** | -3.1 | 0.096 | 35/48 (HT-29, A-172, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12748. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 340 | 3 (3 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +14.8) ⚠ toxic; transcription drop | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.218× (z -19.5) |
| [[HOP62 (line)]] | alt | 215 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 5.21× (z +13.1) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.231× (z -16.7) |
| [[MIA PaCa-2 (line)]] | alt | 307 | 4 (4 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.03× (z +13.5) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.139× (z -20.7) |
| [[A549 (line)]] | wt | 401 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.50× (z +14.7) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.140× (z -24.0) |
| [[Hs 766T (line)]] | wt | 293 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +10.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.187× (z -21.3) |
| [[NCI-H2030 (line)]] | alt | 548 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +11.7) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.196× (z -20.2) |
| [[PANC-1 (line)]] | alt | 377 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +12.5) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.148× (z -23.5) |
| [[RKO (line)]] | wt | 302 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +12.9) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -13.0) |
| [[SW 900 (line)]] | alt | 314 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +11.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.293× (z -14.2) |
| [[SW480 (line)]] | alt | 315 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +14.5) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.258× (z -17.1) |
| [[A-427 (line)]] | wt | 325 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +9.7) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.220× (z -16.6) |
| [[A498 (line)]] | wt | 358 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +15.0) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.221× (z -18.0) |
| [[C32 (line)]] | wt | 179 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +12.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.418× (z -9.6) |
| [[HS-578T (line)]] | alt | 184 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +12.6) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.210× (z -16.6) |
| [[LS 180 (line)]] | wt | 296 | 2 (2 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.02× (z +12.5) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.256× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 362 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.13× (z +14.8) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.320× (z -14.6) |
| [[SHP-77 (line)]] | alt | 316 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +12.8) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.270× (z -11.8) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.466× (z -9.7) |
| [[A-172 (line)]] | wt | 273 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.96× (z +13.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.247× (z -15.3) |
| [[AsPC-1 (line)]] | alt | 317 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +12.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.276× (z -11.9) ⚠ transcription drop |
| [[CFPAC-1 (line)]] | alt | 188 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +11.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.442× (z -9.8) |
| [[H4 (line)]] | wt | 212 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.46× (z +11.7) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.209× (z -15.3) |
| [[LoVo (line)]] | wt | 322 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.64× (z +14.8) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.255× (z -10.6) ⚠ transcription drop |
| [[NCI-H1792 (line)]] | alt | 189 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +12.4) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.282× (z -14.6) |
| [[NCI-H23 (line)]] | alt | 601 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +10.6) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.182× (z -21.8) |
| [[Panc 03.27 (line)]] | alt | 252 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.56× (z +13.4) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.333× (z -8.5) ⚠ transcription drop |
| [[SK-MEL-2 (line)]] | alt | 460 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.73× (z +10.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.205× (z -13.8) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.430× (z -10.5) |
| [[SNU-423 (line)]] | alt | 241 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +12.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.441× (z -9.5) |
| [[SW1417 (line)]] | alt | 339 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +10.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.328× (z -9.3) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.485× (z -8.5) |
| [[AN3 CA (line)]] | alt | 334 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.47× (z +8.8) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.313× (z -11.9) |
| [[HT-29 (line)]] | alt | 259 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +12.1) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 393 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.83× (z +11.2) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.295× (z -10.4) ⚠ transcription drop |
| [[LOX-IMVI (line)]] | wt | 218 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.77× (z +12.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 217 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 224 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +10.5) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.324× (z -11.7) |
| [[SW 1271 (line)]] | alt | 230 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.75× (z +8.7) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.271× (z -10.4) |
| [[SW48 (line)]] | wt | 309 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +9.8) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.325× (z -8.9) ⚠ transcription drop |
| [[C-33 A (line)]] | alt | 249 | 0 | 2 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.291× (z -10.6) |
| [[CHP-212 (line)]] | wt | 236 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +9.8) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 196 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.02× (z +12.5) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.438× (z -9.1) |
| [[HCT15 (line)]] | alt | 202 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.85× (z +13.2) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 282 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 204 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +8.7) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.344× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 197 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.33× (z +9.4) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 215 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +10.7) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.459× (z -9.5) |
| [[NCI-H661 (line)]] | alt | 207 | 0 | 2 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.155× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 168 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +8.8) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 570 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.198× (z -14.1) ⚠ transcription drop |
| [[NCI-H2122 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 304 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 193 | 0 | 0 | — | — |

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
| Name | mitochondrially encoded cytochrome c oxidase III |
| Locus type | gene with protein product (protein-coding gene) |
| Location | mitochondria — chrMT:9,207-9,990 (+) |
| Ensembl biotype | protein_coding |
| Also known as | COX3, COIII, CO3; previously MTCO3 |
| Gene groups (HGNC) | Mitochondrial complex IV: cytochrome c oxidase subunits; Mitochondrially encoded protein coding genes |
| Reactome | 22 pathways, smallest: FASTK family proteins regulate processing and stability of mitochondrial RNAs; tRNA processing in the mitochondrion; Mitochondrial mRNA modification |
| Matched by | ensembl_id |

**Function**, from UniProt [P00414](https://www.uniprot.org/uniprotkb/P00414) (Cytochrome c oxidase subunit 3):

> Component of the cytochrome c oxidase, the last enzyme in the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to transfer electrons derived from NADH and succinate to molecular oxygen, creating an electrochemical gradient over …

**Summary**, from NCBI Gene [4514](https://www.ncbi.nlm.nih.gov/gene/4514):

> Predicted to enable electron transfer activity. Predicted to contribute to cytochrome-c oxidase activity. Involved in respiratory chain complex IV assembly. Located in mitochondrial membrane. Part of respiratory chain complex IV. Implicated in MELAS syndrome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7422](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7422) · Entrez [4514](https://www.ncbi.nlm.nih.gov/gene/4514) · UniProt [P00414](https://www.uniprot.org/uniprotkb/P00414) · Ensembl [ENSG00000198938](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198938)

## Data

Gene col 12748: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12748); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12748, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12748]; `tensor/DDL_lfc|DDL_z.npy` [12748]; `embed/gene_vectors.npy` [12748]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12748 or target_col == 12748). Every well: [[MT-CO3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT-CO3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
