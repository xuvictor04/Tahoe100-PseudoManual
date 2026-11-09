---
symbol: "FAM120A"
type: "gene"
col: 541
ensembl_id: "ENSG00000048828"
name: "family with sequence similarity 120 member A"
location: "9q22.31"
module: 18
arm: "+"
pooled_cpm: 177.02
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 15
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# FAM120A

*family with sequence similarity 120 member A* — 9q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.45× (z +26.2, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.41× (z +5.3, q 9e-06, up in 24 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.582× (z -22.4, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GSPT1]] (+0.71, fdr 1e-05), [[UBE2G2]] (+0.66, fdr 7e-06), [[IPO5]] (+0.66, fdr 1e-05); moves opposite to [[IFI27L2]] (-0.68, fdr 1e-05), [[IL10RB]] (-0.66, fdr 7e-06), [[LINC01273]] (-0.64, fdr 8e-06).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PRR5L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 541.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.45×** | +26.2 | 0e+00 | 48/49 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +20.4 | 0e+00 | 42/44 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +15.1 | 0e+00 | 43/45 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +8.7 | 4e-16 | 39/47 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +8.3 | 1e-14 | 41/48 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.24×** | +6.3 | 3e-08 | 24/48 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.24×** | +6.2 | 5e-08 | 26/48 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.41×** | +5.3 | 9e-06 | 24/49 (LS 180, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.40×** | +5.2 | 1e-05 | 28/48 (LS 180, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.38×** | +4.9 | 5e-05 | 27/48 (Hs 766T, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.36×** | +4.8 | 1e-04 | 26/48 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | 1.18× | +4.7 | 1e-04 | 20/48 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.34×** | +4.5 | 3e-04 | 26/48 (CFPAC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.15× | +4.0 | 0.002 | 17/48 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.20×** | +3.8 | 0.005 | 19/48 (LOX-IMVI, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Terfenadine (drug)]] 0.5 µM |  | 1.14× | +3.7 | 0.007 | 2/48 (NCI-H2030, SW48) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.13× | +3.5 | 0.015 | 14/48 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.029 | 11/48 (NCI-H2030, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.12× | +3.2 | 0.034 | 10/48 (PANC-1, Panc 03.27, …) | top dose only |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 1.11× | +3.2 | 0.036 | 4/48 (C-33 A, RPMI-7951, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.11× | +2.9 | 0.083 | 8/49 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.089 | 16/48 (NCI-H2030, AsPC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 541.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.582×** | -22.4 | 0e+00 | 43/48 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.511×** | -19.6 | 0e+00 | 47/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.529×** | -18.6 | 0e+00 | 45/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.589×** | -15.5 | 0e+00 | 44/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.666×** | -11.4 | 5e-28 | 35/47 (H4, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.789×** | -9.8 | 1e-20 | 29/49 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.717×** | -9.3 | 9e-19 | 34/48 (J82, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.729×** | -9.2 | 2e-18 | 37/49 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.804×** | -9.0 | 1e-17 | 32/48 (KATO III, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.736×** | -8.9 | 2e-17 | 36/48 (SW48, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.772×** | -7.6 | 2e-12 | 34/48 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.775×** | -7.4 | 5e-12 | 35/48 (J82, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 0.861× | -6.2 | 3e-08 | 17/48 (LOX-IMVI, RKO, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.802×** | -5.8 | 3e-07 | 27/48 (HOP62, LoVo, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **0.691×** | -5.6 | 6e-07 | 33/49 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 0.5 µM |  | 0.873× | -3.9 | 0.002 | 13/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.864× | -3.9 | 0.002 | 14/47 (J82, SW480, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.913× | -3.7 | 0.004 | 6/48 (J82, SW480, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.913× | -3.7 | 0.004 | 8/48 (J82, SW1417, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.884× | -3.6 | 0.007 | 13/48 (Panc 03.27, KATO III, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.885× | -3.4 | 0.012 | 15/47 (C32, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 541. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 184 | 6 (6 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.82× (z +19.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.352× (z -20.3) |
| [[J82 (line)]] | alt | 290 | 1 (1 ⚠) | 10 (5 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.89× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -32.6) |
| [[LS 180 (line)]] | wt | 244 | 6 (6 ⚠) | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +14.6) ⚠ cell-cycle shift, explains ~48% of this change | [[Panobinostat (drug)]] 5 µM 0.356× (z -18.1) |
| [[HEC-1-A (line)]] | alt | 239 | 3 (3 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.07× (z +13.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.390× (z -16.9) |
| [[HOP62 (line)]] | alt | 161 | 3 (3 ⚠) | 7 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +16.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -23.0) |
| [[C32 (line)]] | wt | 157 | 1 (1 ⚠) | 8 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -14.4) |
| [[A-172 (line)]] | wt | 140 | 3 (3 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -20.6) |
| [[A549 (line)]] | wt | 158 | 3 (3 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +18.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.428× (z -13.6) |
| [[HS-578T (line)]] | alt | 180 | 3 (3 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +14.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -20.1) |
| [[KATO III (line)]] | alt | 213 | 3 (3 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +19.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.319× (z -20.5) |
| [[LoVo (line)]] | wt | 187 | 3 (3 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +15.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -14.9) |
| [[PANC-1 (line)]] | alt | 137 | 3 (3 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +14.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.588× (z -14.4) |
| [[RKO (line)]] | wt | 311 | 1 (1 ⚠) | 7 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.94× (z +11.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -18.9) |
| [[LOX-IMVI (line)]] | wt | 209 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +14.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -18.8) |
| [[MIA PaCa-2 (line)]] | alt | 242 | 3 (3 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +16.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -14.8) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.511× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 171 | 4 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +14.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.587× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 205 | 2 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +14.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -20.9) |
| [[SW48 (line)]] | wt | 280 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.90× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.296× (z -17.0) |
| [[NCI-H1792 (line)]] | alt | 172 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +15.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -13.3) |
| [[SW1417 (line)]] | alt | 192 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +17.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.489× (z -13.4) |
| [[A498 (line)]] | wt | 245 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +16.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -17.5) |
| [[SNU-423 (line)]] | alt | 194 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -20.2) |
| [[CFPAC-1 (line)]] | alt | 84.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +13.6) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 190 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +12.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.465× (z -9.3) |
| [[Hs 766T (line)]] | wt | 225 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +13.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.511× (z -10.1) |
| [[HT-29 (line)]] | alt | 221 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +15.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.566× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 188 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -15.9) |
| [[NCI-H1573 (line)]] | alt | 76.8 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.13× (z +16.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.584× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 104 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -13.0) |
| [[Panc 03.27 (line)]] | alt | 155 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +16.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.593× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 136 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -14.7) |
| [[SHP-77 (line)]] | alt | 119 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +11.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.419× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 153 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -22.4) |
| [[A-427 (line)]] | wt | 106 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -13.8) |
| [[C-33 A (line)]] | alt | 162 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +11.4) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 163 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -11.2) |
| [[H4 (line)]] | wt | 135 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +11.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.376× (z -11.8) |
| [[SW 900 (line)]] | alt | 116 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.571× (z -9.4) |
| [[BT-474 (line)]] | alt | 117 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.371× (z -12.3) |
| [[HepG2_C3A (line)]] | wt | 116 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.439× (z -9.5) |
| [[AN3 CA (line)]] | alt | 175 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 157 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.95× (z +10.9) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 152 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.298× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 137 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.634× (z -9.1) |
| [[SNU-1 (line)]] | wt | 188 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +11.7) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 169 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.174× (z -9.0) |
| [[NCI-H2122 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 143 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 541), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSPT1]] | +0.71 | +0.57 / +0.71 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[UBE2G2]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[IPO5]] | +0.66 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[PRKDC]] | +0.65 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[LRPPRC]] | +0.65 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[MDN1]] | +0.65 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[SYNCRIP]] | +0.64 | +0.48 / +0.72 | both halves | 2e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 749 |
| [[TXNDC5]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[EMC1]] | +0.63 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[URB1]] | +0.61 | +0.66 / +0.58 | both halves | 8e-06 |  |
| [[NDUFA10]] | +0.61 | +0.42 / +0.68 | both halves | 4e-05 |  |
| [[CAD]] | +0.61 | +0.57 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |

## Genes that move opposite

*37 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFI27L2]] | -0.68 | -0.51 / -0.70 | both halves | 1e-05 |  |
| [[IL10RB]] | -0.66 | -0.62 / -0.65 | both halves | 7e-06 |  |
| [[LINC01273]] | -0.64 | -0.57 / -0.66 | both halves | 8e-06 |  |
| [[TRAPPC2B]] | -0.63 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[NDUFB4]] | -0.63 | -0.46 / -0.64 | both halves | 3e-05 |  |
| [[RNF181]] | -0.62 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[BTN2A2]] | -0.59 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[C15orf48]] | -0.59 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[SIRT6]] | -0.58 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[BSDC1]] | -0.58 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[EAPP]] | -0.57 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[IER5]] | -0.57 | -0.45 / -0.62 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRR5L]] | B | PRR5L activity raises FAM120A's level | lines that do not express PRR5L (10) vs lines expressing it (40) | 1.43× lower at baseline in the lines without PRR5L | 0.051 | ⚠ within organs, on part of the lines; also absent: RASA3, DUSP5-DT, HOXA13; maybe low, not absent |
| [[IFI27L2]] | B | IFI27L2 activity raises FAM120A's level | lines that do not express IFI27L2 (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without IFI27L2 | 0.062 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.545). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-31.2, -30.9); signed map (-19.9, -45.4). **Vector** length 113, 37.3% of its response variance represented; |z| ≥ 3 in 1,498 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.3 | +26.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.2 | +20.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.8 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +15.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +4.5 | +2.7 |
|  | [[Budesonide (drug)]] 5 µM |  | +4.4 | +2.7 |
|  | [[EX229 (drug)]] 5 µM |  | +4.1 | +4.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.8 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +5.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.3 | -9.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.7 | -11.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.4 | -22.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.7 | -9.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.7 | -3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -9.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.1 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.7 | -3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 120 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.31 — chr9:93,451,685-93,566,112 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0183, OSSA; previously C9orf10 |
| Gene groups (HGNC) | PIN-like domain superfamily |
| Hallmark sets | MYC_TARGETS_V1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZB2](https://www.uniprot.org/uniprotkb/Q9NZB2) (Constitutive coactivator of PPAR-gamma-like protein 1):

> Membrane-associated scaffold protein that participates in multiple cellular processes, including oxidative stress-induced survival signaling, RNA trafficking and translational regulation, and the modulation of membrane signaling through its interaction with RNA-binding proteins and lipid raft-associated domains. Functions as a regulator of activation of several intracellular kinases, including SRC, FAK, and PI3K, following oxidative stress. Promotes RNA splicing and stability of lipogenic …

**Summary**, from NCBI Gene [23196](https://www.ncbi.nlm.nih.gov/gene/23196):

> Enables RNA binding activity. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13247](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13247) · Entrez [23196](https://www.ncbi.nlm.nih.gov/gene/23196) · UniProt [Q9NZB2](https://www.uniprot.org/uniprotkb/Q9NZB2) · Ensembl [ENSG00000048828](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000048828)

## Data

Gene col 541: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 541); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 541, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 541]; `tensor/DDL_lfc|DDL_z.npy` [541]; `embed/gene_vectors.npy` [541]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 541 or target_col == 541). Every well: [[FAM120A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM120A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
