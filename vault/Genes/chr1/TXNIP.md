---
symbol: "TXNIP"
type: "gene"
col: 15471
ensembl_id: "ENSG00000265972"
name: "thioredoxin interacting protein"
location: "1q21.1"
module: 123
arm: "+"
pooled_cpm: 238.23
n_lines_expressing: 39
n_dd_up: 24
n_dd_down: 27
n_dd_up_clean: 20
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 17
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# TXNIP

*thioredoxin interacting protein* — 1q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.44× (z +31.3, q 0e+00, up in 37 of 37 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 5.37× (z +22.0, q 0e+00, up in 37 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (14 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.193× (z -20.6, q 0e+00, down in 35 of 36 measured lines) ⚠ toxic. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.205× (z -19.8, q 0e+00, down in 37 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL4A]] (+0.73, fdr 7e-06), [[CEP350]] (+0.67, fdr 7e-06), [[PNRC1]] (+0.66, fdr 7e-06); moves opposite to [[AHSA1]] (-0.65, fdr 7e-06), [[ATP2C1]] (-0.64, fdr 1e-05), [[THOC5]] (-0.60, fdr 1e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SNAI2]] → it (grade B ⚠); 17 go from it, the strongest it → [[POMT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15471.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **5.44×** | +31.3 | 0e+00 | 37/37 (C32, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.37×** | +22.0 | 0e+00 | 37/37 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **4.16×** | +17.9 | 0e+00 | 36/37 (C32, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.80×** | +13.5 | 3e-39 | 35/37 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.79×** | +13.4 | 5e-39 | 31/37 (HepG2/C3A, BT-474, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.51×** | +12.0 | 3e-31 | 31/37 (HepG2/C3A, HT-29, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.94×** | +8.7 | 4e-16 | 35/37 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.94×** | +8.6 | 4e-16 | 27/37 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.63×** | +6.4 | 9e-09 | 23/37 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +5.6 | 1e-06 | 26/37 (HCT15, HOP62, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.45×** | +4.8 | 7e-05 | 22/38 (H4, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +4.8 | 9e-05 | 27/38 (LS 180, CHP-212, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.40×** | +4.4 | 4e-04 | 22/37 (AsPC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.42×** | +4.4 | 4e-04 | 26/38 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.36×** | +4.0 | 0.002 | 19/37 (Hs 766T, AsPC-1, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.004 | 21/37 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **1.33×** | +3.8 | 0.005 | 21/37 (AsPC-1, SW 900, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.072 | 18/37 (Hs 766T, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15471.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.193×** | -20.6 | 0e+00 | 35/36 (LOX-IMVI, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.205×** | -19.8 | 0e+00 | 37/37 (LOX-IMVI, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.265×** | -17.3 | 0e+00 | 35/37 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.301×** | -15.6 | 0e+00 | 36/37 (HCT15, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.327×** | -14.5 | 1e-45 | 34/38 (COLO 205, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.339×** | -13.6 | 7e-40 | 31/33 (SW48, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.487×** | -13.2 | 5e-38 | 37/38 (LOX-IMVI, SNU-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.345×** | -13.1 | 3e-37 | 36/37 (HOP62, C32, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.414×** | -11.5 | 1e-28 | 34/37 (C32, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.406×** | -10.9 | 1e-25 | 29/34 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.232×** | -10.0 | 1e-21 | 32/35 (H4, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.266×** | -9.0 | 9e-18 | 34/38 (CFPAC-1, SW 900, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **0.493×** | -8.9 | 4e-17 | 34/36 (SW480, COLO 205, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.523×** | -8.1 | 2e-14 | 33/37 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.553×** | -7.4 | 5e-12 | 29/39 (LOX-IMVI, H4, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.423×** | -5.9 | 2e-07 | 30/37 (Hs 766T, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.609×** | -4.6 | 1e-04 | 27/38 (COLO 205, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 5 µM |  | **0.578×** | -3.7 | 0.006 | 24/37 (HCT15, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.820×** | -3.6 | 0.008 | 18/37 (SNU-1, SW480, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.834× | -3.3 | 0.023 | 19/38 (CFPAC-1, LOX-IMVI, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.630×** | -3.1 | 0.039 | 17/37 (MIA PaCa-2, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Fusidic acid (drug)]] 5 µM |  | 0.848× | -3.0 | 0.057 | 12/37 (NCI-H460, H4, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.650×** | -2.9 | 0.070 | 17/37 (LOX-IMVI, SW 900, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.56 per unit of S-phase module lfc, +0.82 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15471. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 622 | 23 (3 ⚠) | 12 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +24.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.37× (z +15.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.121× (z -19.0) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.215× (z -14.4) |
| [[Hs 766T (line)]] | wt | 371 | 20 (2 ⚠) | 13 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.87× (z +23.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 5.01× (z +15.0) | [[Ixazomib citrate (drug)]] 5 µM 0.203× (z -14.8) |
| [[CFPAC-1 (line)]] | alt | 536 | 8 (3 ⚠) | 13 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +20.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.84× (z +17.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.175× (z -18.6) ⚠ toxic · without an alert: [[Belumosudil (drug)]] 5 µM 0.178× (z -18.4) |
| [[LOX-IMVI (line)]] | wt | 462 | 6 (3 ⚠) | 15 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +17.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.27× (z +14.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0661× (z -27.0) ⚠ toxic · without an alert: [[Belumosudil (drug)]] 5 µM 0.104× (z -22.5) |
| [[SW480 (line)]] | alt | 286 | 10 (4 ⚠) | 11 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +27.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 6.23× (z +21.2) | [[Auranofin (drug)]] 5 µM 0.195× (z -18.9) |
| [[SW 900 (line)]] | alt | 659 | 4 (2 ⚠) | 15 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +22.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.84× (z +18.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0824× (z -22.6) ⚠ toxic · without an alert: [[Belumosudil (drug)]] 5 µM 0.173× (z -15.9) |
| [[H4 (line)]] | wt | 359 | 6 (1 ⚠) | 11 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +18.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.10× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.105× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -14.1) |
| [[C32 (line)]] | wt | 239 | 8 (2 ⚠) | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 21.1× (z +41.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 17.0× (z +27.0) | [[Belumosudil (drug)]] 5 µM 0.106× (z -20.5) |
| [[HT-29 (line)]] | alt | 234 | 8 (3 ⚠) | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +24.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 9.04× (z +21.9) | [[Auranofin (drug)]] 5 µM 0.218× (z -15.1) |
| [[LS 180 (line)]] | wt | 746 | 7 (3 ⚠) | 9 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.11× (z +22.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 9.44× (z +18.0) | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.120× (z -16.4) |
| [[SNU-423 (line)]] | alt | 376 | 3 (1 ⚠) | 13 (7 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.92× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.139× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.142× (z -17.6) |
| [[Panc 03.27 (line)]] | alt | 621 | 5 (3 ⚠) | 10 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +20.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.60× (z +15.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.157× (z -17.6) ⚠ toxic · without an alert: [[Belumosudil (drug)]] 5 µM 0.206× (z -15.1) |
| [[SW48 (line)]] | wt | 346 | 3 (1 ⚠) | 12 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +13.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.80× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.0258× (z -23.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.133× (z -13.7) |
| [[COLO 205 (line)]] | alt | 790 | 4 (3 ⚠) | 10 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +24.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.26× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.188× (z -16.3) |
| [[HOP62 (line)]] | alt | 282 | 5 (2 ⚠) | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.82× (z +12.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0778× (z -19.6) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0950× (z -18.8) |
| [[KATO III (line)]] | alt | 318 | 9 (3 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.49× (z +28.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.39× (z +21.3) | [[Belumosudil (drug)]] 5 µM 0.204× (z -15.3) |
| [[MIA PaCa-2 (line)]] | alt | 479 | 3 (1 ⚠) | 11 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +13.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.14× (z +12.3) | [[Belumosudil (drug)]] 5 µM 0.124× (z -17.5) |
| [[RKO (line)]] | wt | 112 | 8 (4 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +26.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 13.2× (z +20.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -13.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.205× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 222 | 5 (2 ⚠) | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.73× (z +29.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 10.2× (z +23.7) | [[Belumosudil (drug)]] 5 µM 0.130× (z -20.0) |
| [[BT-474 (line)]] | alt | 122 | 9 (4 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +29.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 17.7× (z +22.2) | [[Belumosudil (drug)]] 5 µM 0.120× (z -15.7) |
| [[HCT15 (line)]] | alt | 354 | 2 (1 ⚠) | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +11.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.32× (z +9.9) | [[Auranofin (drug)]] 5 µM 0.0918× (z -19.9) |
| [[hTERT-HPNE (line)]] | wt | 206 | 3 (1 ⚠) | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +11.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.42× (z +11.4) | [[Ixazomib citrate (drug)]] 5 µM 0.148× (z -14.5) |
| [[NCI-H1792 (line)]] | alt | 190 | 6 (3 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +32.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.07× (z +19.3) | [[Belumosudil (drug)]] 5 µM 0.135× (z -17.7) |
| [[SNU-1 (line)]] | wt | 416 | 5 (2 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +13.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.58× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.0352× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -18.5) |
| [[SW1417 (line)]] | alt | 272 | 7 (3 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.99× (z +29.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.00× (z +19.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.284× (z -11.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 226 | 5 (2 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 22.3× (z +26.4) | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.273× (z -11.1) |
| [[LoVo (line)]] | wt | 146 | 4 (2 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.31× (z +24.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.01× (z +15.4) | [[Belumosudil (drug)]] 5 µM 0.202× (z -12.2) |
| [[NCI-H2347 (line)]] | alt | 288 | 2 (2 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +13.1) ⚠ cell-cycle shift, explains ~29% of this change | [[Belumosudil (drug)]] 5 µM 0.139× (z -11.8) |
| [[SHP-77 (line)]] | alt | 125 | 6 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.58× (z +20.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.52× (z +15.6) | [[Belumosudil (drug)]] 5 µM 0.176× (z -12.9) |
| [[A498 (line)]] | wt | 78.2 | 3 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.76× (z +17.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.36× (z +11.9) | [[Auranofin (drug)]] 5 µM 0.265× (z -9.4) |
| [[A-172 (line)]] | wt | 149 | 3 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.65× (z +17.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.35× (z +10.7) | [[Auranofin (drug)]] 5 µM 0.186× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 91.8 | 3 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +26.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.16× (z +12.9) | [[Ixazomib citrate (drug)]] 5 µM 0.240× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 144 | 0 | 4 (1 ⚠) | — | [[Belumosudil (drug)]] 5 µM 0.180× (z -13.2) |
| [[CHP-212 (line)]] | wt | 141 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +9.4) ⚠ cell-cycle shift, explains ~29% of this change | [[Belumosudil (drug)]] 5 µM 0.0965× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 71.0 | 1 | 2 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 3.43× (z +8.5) | [[Ixazomib citrate (drug)]] 5 µM 0.196× (z -11.4) |
| [[SW 1088 (line)]] | alt | 344 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.54× (z +12.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 9.12× (z +10.7) | — |
| [[SW 1271 (line)]] | alt | 327 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +11.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.09× (z +8.8) | — |
| [[A-427 (line)]] | wt | 12.5 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 17.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 39.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 31.9 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 17.3 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 50.7 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 48.3 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 21.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 346 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 47.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 254 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.4 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 43.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15471), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL4A]] | +0.73 | +0.63 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[CEP350]] | +0.67 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[PNRC1]] | +0.66 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[PPP1R3B]] | +0.65 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[BIRC3]] | +0.64 | +0.52 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_APOPTOSIS |
| [[ANKRD12]] | +0.64 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[THAP1]] | +0.63 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[REST]] | +0.63 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[IRF2BP2]] | +0.62 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[SNAPC1]] | +0.62 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[MRPS18B]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[CLK4]] | +0.61 | +0.62 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHSA1]] | -0.65 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[ATP2C1]] | -0.64 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[THOC5]] | -0.60 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[GDAP2]] | -0.59 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[C1orf216]] | -0.59 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[PSMB7]] | -0.57 | -0.54 / -0.58 | both halves | 1e-05 | pathway: Cellular response to chemical stress |
| [[UFD1]] | -0.57 | -0.53 / -0.63 | both halves | 1e-05 | pathway: Cellular response to chemical stress |
| [[CACYBP]] | -0.56 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[ZNF731P]] | -0.56 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[NIPA2]] | -0.56 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[NAA50]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[OTULIN]] | -0.55 | -0.64 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNAI2]] | B | SNAI2 activity raises TXNIP's level | lines that do not express SNAI2 (23) vs lines expressing it (27) | 2.07× lower at baseline in the lines without SNAI2 | 0.038 | ⚠ within organs, on part of the lines; also absent: GNG2, LBH, PLAT |
| [[TOP2A]] | B | TOP2A activity raises TXNIP's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MT1G]] | B | MT1G activity raises TXNIP's level | lines that do not express MT1G (31) vs lines expressing it (19) | 3.09× lower at baseline in the lines without MT1G | 0.071 | ⚠ within organs, on part of the lines; also absent: TFF2, PROM1, FOXQ1 |
| [[TNFAIP3]] | C | TNFAIP3 activity raises TXNIP's level | lines that do not express TNFAIP3 (3) vs lines expressing it (47) | 4.99× lower at baseline in the lines without TNFAIP3 | 0.087 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IER3, JAG1, ATXN1; maybe low, not absent |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POMT2]] | B | TXNIP activity lowers POMT2's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 1.51× higher at baseline in the lines without TXNIP | 0.006 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |
| [[PER2]] | B | TXNIP activity raises PER2's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 1.88× lower at baseline in the lines without TXNIP | 0.012 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |
| [[PHACTR4]] | B | TXNIP activity lowers PHACTR4's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 1.40× higher at baseline in the lines without TXNIP | 0.014 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |
| [[IRS2]] | B | TXNIP activity raises IRS2's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 2.27× lower at baseline in the lines without TXNIP | 0.015 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |
| [[B4GALNT1]] | B | TXNIP activity lowers B4GALNT1's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 3.00× higher at baseline in the lines without TXNIP | 0.021 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |
| [[PPP1R3B]] | B | TXNIP activity raises PPP1R3B's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 2.28× lower at baseline in the lines without TXNIP | 0.044 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |
| [[FAM227A]] | B | TXNIP activity lowers FAM227A's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 1.77× higher at baseline in the lines without TXNIP | 0.050 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |
| [[COIL]] | B | TXNIP activity lowers COIL's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 1.13× higher at baseline in the lines without TXNIP | 0.053 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |
| [[C1orf216]] | B | TXNIP activity lowers C1orf216's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 1.73× higher at baseline in the lines without TXNIP | 0.062 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |
| [[LIPT1]] | B | TXNIP activity lowers LIPT1's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 1.30× higher at baseline in the lines without TXNIP | 0.065 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |
| [[UBFD1]] | B | TXNIP activity lowers UBFD1's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 1.10× higher at baseline in the lines without TXNIP | 0.071 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |
| [[NUDCD2]] | B | TXNIP activity lowers NUDCD2's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 1.43× higher at baseline in the lines without TXNIP | 0.072 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.659). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-17.9, -13.6); signed map (-4.0, 11.5). **Vector** length 147, 47.4% of its response variance represented; |z| ≥ 3 in 1,586 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +11.4 | +13.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +11.2 | +22.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +9.7 | +31.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +8.7 | +17.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +8.3 | +8.7 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +4.9 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +5.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.4 | +3.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +4.4 | +4.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -11.7 | -17.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -10.4 | -13.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -9.5 | -11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.8 | -15.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.4 | -13.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -5.2 | -4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | thioredoxin interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.1 — chr1:145,992,435-145,996,579 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VDUP1, EST01027, HHCPA78, THIF, ARRDC6 |
| Gene groups (HGNC) | Alpha arrestins |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, APOPTOSIS, INTERFERON_GAMMA_RESPONSE, P53_PATHWAY |
| Reactome | 14 pathways, smallest: Regulation of FOXO transcriptional activity by acetylation; The NLRP3 inflammasome; Inflammasomes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3M7](https://www.uniprot.org/uniprotkb/Q9H3M7) (Thioredoxin-interacting protein):

> May act as an oxidative stress mediator by inhibiting thioredoxin activity or by limiting its bioavailability. Interacts with COPS5 and restores COPS5-induced suppression of CDKN1B stability, blocking the COPS5-mediated translocation of CDKN1B from the nucleus to the cytoplasm (By similarity). Functions as a transcriptional repressor, possibly by acting as a bridge molecule between transcription factors and corepressor complexes, and over-expression will induce G0/G1 cell cycle arrest. Required …

**Summary**, from NCBI Gene [10628](https://www.ncbi.nlm.nih.gov/gene/10628):

> This gene encodes a thioredoxin-binding protein that is a member of the alpha arrestin protein family. Thioredoxin is a thiol-oxidoreductase that is a major regulator of cellular redox signaling which protects cells from oxidative stress. This protein inhibits the antioxidative function of thioredoxin resulting in the accumulation of reactive oxygen species and cellular stress. This protein also functions as a regulator of cellular metabolism and of endoplasmic reticulum (ER) stress. This …

**Accessions** — [HGNC:16952](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16952) · Entrez [10628](https://www.ncbi.nlm.nih.gov/gene/10628) · UniProt [Q9H3M7](https://www.uniprot.org/uniprotkb/Q9H3M7) · Ensembl [ENSG00000265972](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000265972)

## Data

Gene col 15471: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15471); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15471, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15471]; `tensor/DDL_lfc|DDL_z.npy` [15471]; `embed/gene_vectors.npy` [15471]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15471 or target_col == 15471). Every well: [[TXNIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TXNIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
