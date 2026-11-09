---
symbol: "RPS6KA3"
type: "gene"
col: 10801
ensembl_id: "ENSG00000177189"
name: "ribosomal protein S6 kinase A3"
location: "Xp22.12"
module: 112
arm: "+"
pooled_cpm: 234.9
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 17
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# RPS6KA3

*ribosomal protein S6 kinase A3* — Xp22.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.32× (z +20.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.634× (z -10.9, q 5e-25, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TFPI2]] (+0.59, fdr 1e-05), [[LUCAT1]] (+0.57, fdr 1e-05), [[BMAL2-AS1]] (+0.57, fdr 4e-05); moves opposite to [[CDC23]] (-0.53, fdr 3e-05), [[ZDHHC7]] (-0.53, fdr 1e-04), [[COPS8]] (-0.52, fdr 3e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PDGFB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10801.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.32×** | +20.2 | 0e+00 | 48/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +16.7 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +13.9 | 2e-41 | 44/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.50×** | +13.7 | 1e-40 | 38/48 (A549, HEC-1-A, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.73×** | +13.1 | 3e-37 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.68×** | +12.4 | 2e-33 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.32×** | +10.3 | 5e-23 | 43/49 (LoVo, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +9.4 | 4e-19 | 40/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.08×** | +9.0 | 1e-17 | 44/48 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.28×** | +5.8 | 4e-07 | 31/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.24×** | +5.0 | 4e-05 | 27/47 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.20× | +4.3 | 8e-04 | 23/48 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +4.3 | 8e-04 | 15/49 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.39×** | +4.0 | 0.002 | 24/45 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.05 µM |  | 1.16× | +3.6 | 0.012 | 11/48 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.17× | +3.6 | 0.013 | 17/49 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 1.11× | +3.5 | 0.015 | 2/49 (MIA PaCa-2, NCI-H661) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.017 | 25/48 (SHP-77, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.036 | 18/48 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.048 | 18/48 (A498, LoVo, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.053 | 14/48 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 11 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10801.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.634×** | -10.9 | 5e-25 | 37/48 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.755×** | -9.5 | 3e-19 | 35/48 (RKO, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.661×** | -9.5 | 3e-19 | 31/44 (NCI-H1792, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.674×** | -9.5 | 5e-19 | 39/49 (RKO, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.678×** | -9.3 | 1e-18 | 36/48 (HepG2/C3A, A549, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.709×** | -8.2 | 2e-14 | 35/48 (HepG2/C3A, A549, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.726×** | -7.7 | 2e-12 | 38/48 (CFPAC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.817×** | -6.8 | 5e-10 | 28/49 (A549, NCI-H1792, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -5.1 | 2e-05 | 3/50 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.812×** | -5.0 | 3e-05 | 25/48 (HOP62, A549, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.811×** | -4.9 | 6e-05 | 25/48 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.826×** | -4.6 | 2e-04 | 23/48 (NCI-H1573, NCI-H1792, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.832×** | -4.4 | 5e-04 | 23/48 (A549, BT-474, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **0.827×** | -4.4 | 5e-04 | 23/47 (Hs 766T, HepG2/C3A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.836× | -4.3 | 7e-04 | 21/48 (RKO, HepG2/C3A, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.844× | -4.1 | 0.002 | 21/48 (BT-474, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.844× | -4.1 | 0.002 | 22/48 (BT-474, RKO, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.843× | -3.9 | 0.003 | 20/49 (A549, NCI-H1573, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 0.850× | -3.9 | 0.003 | 19/48 (NCI-H2347, A549, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.877× | -3.9 | 0.003 | 13/48 (BT-474, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.05 µM |  | 0.856× | -3.7 | 0.005 | 19/48 (A549, NCI-H1792, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.858× | -3.7 | 0.006 | 19/48 (HCT15, A549, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.859× | -3.6 | 0.006 | 21/48 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 0.850× | -3.6 | 0.007 | 22/47 (BT-474, NCI-H1573, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10801. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 443 | 0 | 33 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.232× (z -11.7) |
| [[NCI-H460 (line)]] | wt | 244 | 12 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.41× (z +21.8) | — |
| [[SW480 (line)]] | alt | 356 | 7 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +18.6) | [[Dinaciclib (drug)]] 5 µM 0.506× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.525× (z -12.0) |
| [[A549 (line)]] | wt | 310 | 4 (3 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +23.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.33× (z +16.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -18.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.448× (z -11.6) |
| [[LoVo (line)]] | wt | 121 | 10 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +18.2) | — |
| [[PANC-1 (line)]] | alt | 214 | 7 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.79× (z +18.9) | [[Panobinostat (drug)]] 0.5 µM 0.469× (z -10.7) |
| [[RKO (line)]] | wt | 292 | 2 (2 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.9) ⚠ cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.479× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 151 | 6 (2 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +14.2) | [[Dinaciclib (drug)]] 0.05 µM 0.304× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.505× (z -9.3) |
| [[A498 (line)]] | wt | 180 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +18.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.34× (z +12.6) | — |
| [[AsPC-1 (line)]] | alt | 231 | 6 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +14.6) | [[Panobinostat (drug)]] 5 µM 0.501× (z -9.2) |
| [[C32 (line)]] | wt | 380 | 4 (1 ⚠) | 3 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.23× (z +15.4) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -12.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.458× (z -10.3) |
| [[Hs 766T (line)]] | wt | 400 | 1 | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.399× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 255 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +13.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.92× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.487× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 439 | 3 (1 ⚠) | 4 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.79× (z +16.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -14.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Triamcinolone (drug)]] 0.5 µM 0.474× (z -9.7) |
| [[H4 (line)]] | wt | 189 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +12.2) | — |
| [[HOP62 (line)]] | alt | 197 | 4 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +12.6) | [[Clobetasol propionate (drug)]] 0.5 µM 0.491× (z -8.6) |
| [[HT-29 (line)]] | alt | 253 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +13.2) | — |
| [[SK-MEL-2 (line)]] | alt | 246 | 3 (1 ⚠) | 3 | [[Harringtonine (drug)]] 5 µM 2.00× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.474× (z -11.0) |
| [[SNU-423 (line)]] | alt | 340 | 4 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +12.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.38× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.497× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.528× (z -8.9) |
| [[SW 900 (line)]] | alt | 225 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.30× (z +16.0) | — |
| [[KATO III (line)]] | alt | 229 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +19.2) | — |
| [[SW1417 (line)]] | alt | 175 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +13.6) | [[Dinaciclib (drug)]] 0.05 µM 0.527× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 159 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +19.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.64× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.461× (z -11.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 400 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.317× (z -13.9) |
| [[HS-578T (line)]] | alt | 171 | 4 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.73× (z +12.2) | — |
| [[J82 (line)]] | alt | 154 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +13.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.79× (z +12.9) | — |
| [[NCI-H1573 (line)]] | alt | 313 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.26× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -11.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 257 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +11.5) | — |
| [[SNU-1 (line)]] | wt | 278 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.412× (z -10.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 367 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.50× (z +11.8) | — |
| [[A-172 (line)]] | wt | 244 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +11.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.19× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.447× (z -10.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 175 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.459× (z -8.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 240 | 2 | 1 | [[Harringtonine (drug)]] 5 µM 2.59× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.414× (z -10.1) |
| [[HCT15 (line)]] | alt | 153 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 204 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +16.2) | — |
| [[A-427 (line)]] | wt | 139 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.0) ⚠ cell-cycle shift, explains ~27% of this change | [[Selinexor (drug)]] 5 µM 0.587× (z -11.0) ⚠ cell-cycle shift, explains ~20% of this change |
| [[CHP-212 (line)]] | wt | 250 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -11.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 226 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 3.13× (z +13.6) | — |
| [[LOX-IMVI (line)]] | wt | 131 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.13× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 111 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +12.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 213 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +16.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +13.5) | — |
| [[Panc 03.27 (line)]] | alt | 206 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.449× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.556× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 246 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.71× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.461× (z -9.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 126 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +9.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[CFPAC-1 (line)]] | alt | 167 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.13× (z +8.7) | — |
| [[NCI-H2122 (line)]] | alt | 266 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 278 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 95.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10801), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFPI2]] | +0.59 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[LUCAT1]] | +0.57 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[BMAL2-AS1]] | +0.57 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[SERPINB7]] | +0.57 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[KIAA1217]] | +0.55 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[CXCL8]] | +0.54 | +0.47 / +0.53 | both halves | 2e-05 | pathway: Cellular Senescence |
| [[FZD8]] | +0.53 | +0.38 / +0.51 | both halves | 7e-05 |  |
| [[INHBA]] | +0.53 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[SLC4A7]] | +0.53 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ACVR1C]] | +0.52 | +0.39 / +0.44 | both halves | 5e-05 |  |
| [[ATXN1]] | +0.52 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[HMGA1]] | +0.52 | +0.39 / +0.62 | both halves | 6e-05 | pathway: Cellular Senescence |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC23]] | -0.53 | -0.44 / -0.50 | both halves | 3e-05 | pathway: Cellular Senescence |
| [[ZDHHC7]] | -0.53 | -0.33 / -0.58 | both halves | 1e-04 |  |
| [[COPS8]] | -0.52 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[DDX42]] | -0.46 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[BAP1]] | -0.46 | -0.42 / -0.37 | both halves | 9e-05 |  |
| [[TSN]] | -0.45 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[MED20]] | -0.45 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[ADPGK]] | -0.45 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[ABCF3]] | -0.44 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[KANSL2]] | -0.44 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[SUPV3L1]] | -0.44 | -0.37 / -0.52 | both halves | 9e-05 |  |
| [[POLDIP3]] | -0.44 | -0.37 / -0.43 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDGFB]] | B | PDGFB activity raises RPS6KA3's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 1.36× lower at baseline in the lines without PDGFB | 0.054 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.568). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.2, -5.7); signed map (18.9, 41.1). **Vector** length 102, 37.1% of its response variance represented; |z| ≥ 3 in 1,943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +11.0 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +8.7 | +2.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.2 | -9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.8 | -9.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.2 | +13.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | -1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.2 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.6 | +3.6 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -6.1 | -5.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -5.8 | -9.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -4.9 | -2.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.8 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.2 | -1.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.9 | -2.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -3.9 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S6 kinase A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.12 — chrX:20,149,911-20,267,519 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RSK2, HU-3; previously MRX19, CLS |
| Gene groups (HGNC) | MAPK activated protein kinases; Ribosomal protein S6 kinase family |
| Hallmark sets | PROTEIN_SECRETION, ANDROGEN_RESPONSE, PI3K_AKT_MTOR_SIGNALING |
| Reactome | 47 pathways, smallest: CREB phosphorylation; RSK activation; Gastrin-CREB signalling pathway via PKC and MAPK |
| Matched by | ensembl_id |

**Function**, from UniProt [P51812](https://www.uniprot.org/uniprotkb/P51812) (Ribosomal protein S6 kinase alpha-3):

> Serine/threonine-protein kinase that acts downstream of ERK (MAPK1/ERK2 and MAPK3/ERK1) signaling and mediates mitogenic and stress-induced activation of the transcription factors CREB1, ETV1/ER81 and NR4A1/NUR77, regulates translation through RPS6 and EIF4B phosphorylation, and mediates cellular proliferation, survival, and differentiation by modulating mTOR signaling and repressing pro-apoptotic function of BAD and DAPK1. In fibroblast, is required for EGF-stimulated phosphorylation of CREB1 …

**Summary**, from NCBI Gene [6197](https://www.ncbi.nlm.nih.gov/gene/6197):

> This gene encodes a member of the RSK (ribosomal S6 kinase) family of serine/threonine kinases. This kinase contains 2 non-identical kinase catalytic domains and phosphorylates various substrates, including members of the mitogen-activated kinase (MAPK) signalling pathway. The activity of this protein has been implicated in controlling cell growth and differentiation. Mutations in this gene have been associated with Coffin-Lowry syndrome (CLS). [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10432](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10432) · Entrez [6197](https://www.ncbi.nlm.nih.gov/gene/6197) · UniProt [P51812](https://www.uniprot.org/uniprotkb/P51812) · Ensembl [ENSG00000177189](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177189)

## Data

Gene col 10801: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10801); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10801, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10801]; `tensor/DDL_lfc|DDL_z.npy` [10801]; `embed/gene_vectors.npy` [10801]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10801 or target_col == 10801). Every well: [[RPS6KA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS6KA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
