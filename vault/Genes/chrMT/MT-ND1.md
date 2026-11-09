---
symbol: "MT-ND1"
type: "gene"
col: 12722
ensembl_id: "ENSG00000198888"
name: "mitochondrially encoded NADH:ubiquinone oxidoreductase core subunit 1"
location: "mitochondria"
module: null
arm: null
pooled_cpm: 318.03
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 11
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# MT-ND1

*mitochondrially encoded NADH:ubiquinone oxidoreductase core subunit 1* — mitochondria

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.08× (z +10.8, q 2e-24, up in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bosentan (hydrate) (drug)]] 5 µM: 1.80× (z +4.5, q 7e-04, up in 47 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 10 lines (LoVo 7.64×, HT-29 7.38×, SW480 5.22×, MIA PaCa-2 8.22×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LoVo 9.25×, HT-29 7.36×, Panc 03.27 7.44×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LoVo 6.83×, Panc 03.27 6.19×; ⚠ toxic; transcription drop); [[Palmatine (chloride) (drug)]] 5 µM in 1 line (BT-474 2.60×).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.199× (z -12.9, q 2e-35, down in 47 of 48 measured lines) ⚠ transcription drop. The strongest without an alert is [[Pentamidine (isethionate) (drug)]] 5 µM: 0.451× (z -9.0, q 5e-17, down in 45 of 48 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12722.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 10 lines (LoVo 7.64×, HT-29 7.38×, SW480 5.22×, MIA PaCa-2 8.22×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LoVo 9.25×, HT-29 7.36×, Panc 03.27 7.44×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LoVo 6.83×, Panc 03.27 6.19×; ⚠ toxic; transcription drop); [[Palmatine (chloride) (drug)]] 5 µM in 1 line (BT-474 2.60×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.08×** | +10.8 | 2e-24 | 44/44 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.36×** | +9.6 | 4e-19 | 49/49 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.29×** | +8.8 | 3e-16 | 45/45 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **2.01×** | +5.6 | 4e-06 | 47/49 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.80×** | +4.5 | 7e-04 | 47/47 (HEC-1-A, NCI-H2347, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.49× | +3.1 | 0.17 | 28/47 (AsPC-1, COLO 205, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | 1.31× | +3.0 | 0.17 | 25/48 (AsPC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 2.06× | +3.0 | 0.17 | 35/49 (Panc 03.27, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12722.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.199×** | -12.9 | 2e-35 | 47/48 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.451×** | -9.0 | 5e-17 | 45/48 (PANC-1, HS-578T, …) | top dose only | position effect removed |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.510×** | -7.6 | 5e-12 | 46/49 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.467×** | -5.0 | 1e-04 | 46/47 (HEC-1-A, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.553×** | -3.9 | 0.013 | 47/47 (HepG2/C3A, SW 900, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 0.05 µM |  | **0.625×** | -3.8 | 0.015 | 43/48 (CFPAC-1, A498, …) | inconsistent across doses | position effect removed |
| [[Captopril (drug)]] 5 µM |  | **0.633×** | -3.7 | 0.020 | 46/48 (A-427, SW480, …) | rises with dose | position effect removed |
| [[Pimozide (drug)]] 5 µM |  | **0.649×** | -3.5 | 0.036 | 46/48 (NCI-H2347, NCI-H1792, …) | top dose only | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.589×** | -3.4 | 0.036 | 44/48 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.655×** | -3.4 | 0.039 | 29/48 (LS 180, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Methylthiouracil (drug)]] 0.05 µM |  | **0.670×** | -3.2 | 0.069 | 43/50 (HOP62, SW 1088, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12722. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 337 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.97× (z +11.4) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.213× (z -11.5) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.337× (z -11.5) |
| [[A549 (line)]] | wt | 430 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.21× (z +10.8) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.263× (z -12.8) |
| [[HOP62 (line)]] | alt | 289 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.83× (z +10.4) ⚠ toxic; transcription drop | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.266× (z -12.8) |
| [[LS 180 (line)]] | wt | 234 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +9.6) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.193× (z -11.6) ⚠ transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 252 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 8.22× (z +12.0) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.163× (z -10.6) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.320× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 366 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.64× (z +10.4) ⚠ toxic; transcription drop | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.275× (z -12.9) |
| [[SW480 (line)]] | alt | 299 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.22× (z +12.1) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.144× (z -14.8) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.344× (z -11.5) |
| [[A-172 (line)]] | wt | 241 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.26× (z +9.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.131× (z -13.8) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.338× (z -10.4) |
| [[AN3 CA (line)]] | alt | 207 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 7.43× (z +10.8) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.212× (z -8.6) ⚠ transcription drop |
| [[AsPC-1 (line)]] | alt | 268 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.06× (z +9.6) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.220× (z -10.7) ⚠ transcription drop |
| [[HT-29 (line)]] | alt | 196 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 7.38× (z +13.1) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.252× (z -9.4) ⚠ transcription drop |
| [[LOX-IMVI (line)]] | wt | 284 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 6.00× (z +11.1) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.180× (z -11.2) ⚠ transcription drop |
| [[NCI-H1792 (line)]] | alt | 272 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.82× (z +9.7) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.258× (z -12.3) |
| [[Panc 03.27 (line)]] | alt | 246 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 6.57× (z +11.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.158× (z -12.1) ⚠ transcription drop |
| [[PANC-1 (line)]] | alt | 508 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.95× (z +10.6) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.113× (z -15.1) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.231× (z -14.3) |
| [[SW 900 (line)]] | alt | 440 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.43× (z +9.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.131× (z -13.4) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.336× (z -10.2) |
| [[A-427 (line)]] | wt | 438 | 0 | 3 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.130× (z -14.5) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.314× (z -11.7) |
| [[C-33 A (line)]] | alt | 220 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.26× (z +8.6) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.107× (z -12.9) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.313× (z -9.5) |
| [[C32 (line)]] | wt | 196 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.91× (z +8.6) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.252× (z -9.0) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.382× (z -8.8) |
| [[COLO 205 (line)]] | alt | 187 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.66× (z +10.4) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.237× (z -9.8) ⚠ transcription drop |
| [[H4 (line)]] | wt | 220 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 4.78× (z +8.6) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.146× (z -11.5) ⚠ transcription drop · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.357× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 239 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.59× (z +10.4) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.258× (z -9.7) ⚠ transcription drop |
| [[Hs 766T (line)]] | wt | 321 | 0 | 3 (1 ⚠) | — | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.228× (z -14.7) |
| [[LoVo (line)]] | wt | 199 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.64× (z +13.6) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 331 | 1 | 1 (1 ⚠) | [[Palmatine (chloride) (drug)]] 5 µM 2.60× (z +9.4) | [[Docetaxel (drug)]] 0.05 µM 0.164× (z -12.5) ⚠ transcription drop |
| [[CFPAC-1 (line)]] | alt | 218 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.89× (z +9.4) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.275× (z -9.3) ⚠ transcription drop |
| [[HCT15 (line)]] | alt | 167 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.42× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 287 | 0 | 2 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.191× (z -13.7) |
| [[KATO III (line)]] | alt | 365 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.23× (z +9.2) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.157× (z -12.4) ⚠ transcription drop |
| [[NCI-H1573 (line)]] | alt | 507 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.158× (z -13.2) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.312× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 412 | 0 | 2 (1 ⚠) | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.300× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 576 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.125× (z -11.6) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.263× (z -10.5) |
| [[NCI-H661 (line)]] | alt | 388 | 0 | 2 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.266× (z -9.0) |
| [[SNU-1 (line)]] | wt | 193 | 0 | 2 | — | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.280× (z -11.5) |
| [[SW48 (line)]] | wt | 323 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.07× (z +9.6) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.163× (z -11.1) ⚠ transcription drop |
| [[CHP-212 (line)]] | wt | 362 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.206× (z -9.6) ⚠ transcription drop |
| [[hTERT-HPNE (line)]] | wt | 224 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.71× (z +9.4) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 193 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.258× (z -9.3) ⚠ transcription drop |
| [[NCI-H2347 (line)]] | alt | 357 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.156× (z -13.3) ⚠ transcription drop |
| [[RPMI-7951 (line)]] | alt | 180 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.04× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 481 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.144× (z -12.1) ⚠ transcription drop |
| [[SK-MEL-2 (line)]] | alt | 300 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.130× (z -13.4) ⚠ transcription drop |
| [[SNU-423 (line)]] | alt | 361 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.07× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 408 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.159× (z -13.1) ⚠ transcription drop |
| [[HepG2_C3A (line)]] | wt | 291 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 318 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 188 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 162 | 0 | 0 | — | — |

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
| Name | mitochondrially encoded NADH:ubiquinone oxidoreductase core subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | mitochondria — chrMT:3,307-4,262 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ND1, NAD1; previously MTND1 |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase core subunits; Mitochondrially encoded protein coding genes |
| Reactome | 17 pathways, smallest: FASTK family proteins regulate processing and stability of mitochondrial RNAs; tRNA processing in the mitochondrion; Mitochondrial mRNA modification |
| Matched by | ensembl_id |

**Function**, from UniProt [P03886](https://www.uniprot.org/uniprotkb/P03886) (NADH-ubiquinone oxidoreductase chain 1):

> Core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I) which catalyzes electron transfer from NADH through the respiratory chain, using ubiquinone as an electron acceptor. Essential for the catalytic activity and assembly of complex I.

**Summary**, from NCBI Gene [4535](https://www.ncbi.nlm.nih.gov/gene/4535):

> Enables NADH dehydrogenase (ubiquinone) activity. Involved in mitochondrial electron transport, NADH to ubiquinone and mitochondrial respiratory chain complex I assembly. Located in mitochondrial inner membrane. Part of respiratory chain complex I. Implicated in several diseases, including MELAS syndrome; neurodegenerative disease (multiple); optic nerve disease (multiple); toxic shock syndrome; and type 2 diabetes mellitus. Biomarker of Alzheimer's disease; Parkinson's disease; and multiple …

**Accessions** — [HGNC:7455](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7455) · Entrez [4535](https://www.ncbi.nlm.nih.gov/gene/4535) · UniProt [P03886](https://www.uniprot.org/uniprotkb/P03886) · Ensembl [ENSG00000198888](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198888)

## Data

Gene col 12722: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12722); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12722, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12722]; `tensor/DDL_lfc|DDL_z.npy` [12722]; `embed/gene_vectors.npy` [12722]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12722 or target_col == 12722). Every well: [[MT-ND1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT-ND1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
