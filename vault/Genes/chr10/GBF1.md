---
symbol: "GBF1"
type: "gene"
col: 2889
ensembl_id: "ENSG00000107862"
name: "golgi brefeldin A resistant guanine nucleotide exchange factor 1"
location: "10q24.32"
module: 56
arm: "+"
pooled_cpm: 282.17
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 18
n_dd_up_clean: 11
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# GBF1

*golgi brefeldin A resistant guanine nucleotide exchange factor 1* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.21× (z +12.5, q 4e-33, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.340× (z -17.3, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.612× (z -8.2, q 4e-14, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF2AK3]] (+0.76, fdr 7e-06), [[ACBD3]] (+0.75, fdr 7e-06), [[ERLEC1]] (+0.74, fdr 7e-06); moves opposite to [[PRRC2B]] (-0.68, fdr 1e-05), [[ZNF124]] (-0.66, fdr 2e-05), [[ZNF507]] (-0.65, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SNHG18]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Belzutifan (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2889.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.21×** | +12.5 | 4e-33 | 48/49 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +12.0 | 1e-30 | 42/48 (A-427, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.98×** | +11.3 | 2e-27 | 45/48 (A-427, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.77×** | +9.5 | 2e-19 | 44/48 (A-427, SNU-423, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.71×** | +8.9 | 7e-17 | 45/48 (A-427, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.71×** | +8.7 | 4e-16 | 43/48 (BT-474, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.67×** | +8.5 | 1e-15 | 41/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +7.5 | 3e-12 | 37/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +5.2 | 1e-05 | 30/48 (A-427, NCI-H460, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +4.5 | 4e-04 | 30/48 (PANC-1, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +4.5 | 4e-04 | 33/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.27×** | +4.0 | 0.003 | 26/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.25×** | +3.8 | 0.008 | 27/48 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.24×** | +3.5 | 0.017 | 26/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.028 | 24/48 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2889.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.340×** | -17.3 | 0e+00 | 43/44 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.388×** | -14.3 | 4e-44 | 47/49 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.396×** | -14.3 | 6e-44 | 42/45 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.612×** | -8.2 | 4e-14 | 41/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.674×** | -6.3 | 3e-08 | 36/47 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.773×** | -6.0 | 1e-07 | 31/48 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.778×** | -5.9 | 3e-07 | 31/49 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.711×** | -5.7 | 1e-06 | 37/48 (RPMI-7951, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.762×** | -4.4 | 8e-04 | 35/48 (J82, LoVo, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.775×** | -4.2 | 0.001 | 36/48 (SNU-423, HOP62, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.815×** | -3.4 | 0.034 | 27/48 (HS-578T, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.819×** | -3.3 | 0.042 | 28/49 (Hs 766T, SW48, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.805×** | -3.3 | 0.045 | 31/48 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.809×** | -3.2 | 0.051 | 24/48 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.825×** | -3.2 | 0.051 | 23/48 (COLO 205, LoVo, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.698×** | -3.1 | 0.062 | 23/49 (NCI-H2347, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | **0.831×** | -3.1 | 0.068 | 20/47 (LS 180, KATO III, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.824×** | -3.0 | 0.088 | 22/47 (A-172, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.882× | -2.9 | 0.094 | 22/48 (NCI-H2347, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2889. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 137 | 15 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +19.4) | [[Dinaciclib (drug)]] 5 µM 0.455× (z -10.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 192 | 10 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +18.8) | [[Dinaciclib (drug)]] 0.5 µM 0.398× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 225 | 11 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +18.3) | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -10.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 204 | 8 (1 ⚠) | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.94× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.399× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.495× (z -9.5) |
| [[BT-474 (line)]] | alt | 182 | 10 (3 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +13.6) | [[Auranofin (drug)]] 5 µM 0.500× (z -9.4) |
| [[C-33 A (line)]] | alt | 131 | 8 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.38× (z +14.6) | — |
| [[HOP62 (line)]] | alt | 366 | 3 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.84× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.291× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.407× (z -11.5) |
| [[RKO (line)]] | wt | 222 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +14.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 169 | 6 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +15.2) | [[Auranofin (drug)]] 5 µM 0.262× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 251 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +17.1) | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -11.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 257 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +14.4) | — |
| [[A-172 (line)]] | wt | 237 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.28× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -13.5) |
| [[AsPC-1 (line)]] | alt | 372 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -29.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.475× (z -10.4) |
| [[J82 (line)]] | alt | 194 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.98× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -18.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 341 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.12× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -17.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 130 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +13.5) | [[Dinaciclib (drug)]] 0.05 µM 0.340× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 378 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.35× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.233× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -14.2) |
| [[SNU-423 (line)]] | alt | 273 | 5 | 1 | [[Panobinostat (drug)]] 5 µM 3.67× (z +17.7) | [[Auranofin (drug)]] 5 µM 0.436× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 365 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -16.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 271 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.292× (z -12.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 263 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.92× (z +13.5) | — |
| [[HS-578T (line)]] | alt | 356 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -11.4) |
| [[LoVo (line)]] | wt | 286 | 2 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.167× (z -19.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 255 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.199× (z -13.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 152 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.36× (z +15.2) | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -13.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 390 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -15.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 479 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -13.4) |
| [[A549 (line)]] | wt | 307 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -10.1) |
| [[AN3 CA (line)]] | alt | 291 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.49× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.208× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.277× (z -12.0) |
| [[HT-29 (line)]] | alt | 299 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -14.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 296 | 1 | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 6.15× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 257 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.12× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.278× (z -14.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 269 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -8.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 348 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -13.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 289 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -14.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 417 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.290× (z -11.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 316 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.336× (z -12.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 469 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -15.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 241 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -10.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 408 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.303× (z -12.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 323 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -11.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 153 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.17× (z +9.4) | [[Auranofin (drug)]] 5 µM 0.432× (z -10.2) |
| [[SW48 (line)]] | wt | 257 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 246 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -10.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 244 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -15.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 234 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 280 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 285 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 417 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 251 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2889), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2AK3]] | +0.76 | +0.82 / +0.63 | both halves | 7e-06 |  |
| [[ACBD3]] | +0.75 | +0.81 / +0.59 | both halves | 7e-06 | pathway: trans-Golgi Network Vesicle Budding; STRING 536 |
| [[ERLEC1]] | +0.74 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[RAB1A]] | +0.74 | +0.80 / +0.66 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 875 |
| [[TMED9]] | +0.74 | +0.70 / +0.61 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 524 |
| [[COG6]] | +0.73 | +0.80 / +0.60 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SEC22A]] | +0.73 | +0.68 / +0.62 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SRP54]] | +0.72 | +0.83 / +0.61 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.71 | +0.81 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION |
| [[TMEM263]] | +0.69 | +0.77 / +0.58 | both halves | 7e-06 |  |
| [[SUCO]] | +0.69 | +0.75 / +0.58 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.69 | +0.72 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRRC2B]] | -0.68 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[ZNF124]] | -0.66 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[ZNF507]] | -0.65 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[NCR3LG1]] | -0.65 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ZNF300]] | -0.64 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[ZC3HAV1L]] | -0.64 | -0.40 / -0.61 | both halves | 5e-05 |  |
| [[UTP20]] | -0.60 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[PRMT3]] | -0.59 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[FBXO30]] | -0.59 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[DHX37]] | -0.59 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[ZNF121]] | -0.58 | -0.53 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNHG18]] | B | SNHG18 activity raises GBF1's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.28× lower at baseline in the lines without SNHG18 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[PCSK1N]] | B | PCSK1N activity lowers GBF1's level | lines that do not express PCSK1N (21) vs lines expressing it (29) | 1.17× higher at baseline in the lines without PCSK1N | 0.095 | ⚠ within organs, on part of the lines; also absent: MAP6, CERS4, CACNG4 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Belzutifan (drug)]] 5 µM | C | GBF1's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | GBF1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.491 over the table, 0.090 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.762). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.8, -34.5); signed map (-49.3, 12.4). **Vector** length 128, 57.6% of its response variance represented; |z| ≥ 3 in 1,461 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *COPII-mediated vesicle transport* (reactome, mean cos +0.63 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.60 to 8); *Antigen Presentation: Folding, assembly and peptide loading of class I MHC* (reactome, mean cos +0.63 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +6.7 | +11.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.3 | +8.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.8 | +9.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.6 | +1.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | +3.4 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +2.4 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.8 | +1.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.7 | +0.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.5 | +1.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.0 | -8.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -8.7 | -6.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.1 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.0 | -3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -6.0 | +3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.4 | -0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.4 | -3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.1 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | golgi brefeldin A resistant guanine nucleotide exchange factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:102,245,371-102,382,899 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0248, ARF1GEF |
| Gene groups (HGNC) | Sec7 family |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 19 pathways, smallest: Assembly and Release of Dengue Virus Virions; VxPx cargo-targeting to cilium; Cargo trafficking to the periciliary membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92538](https://www.uniprot.org/uniprotkb/Q92538) (Golgi-specific brefeldin A-resistance guanine nucleotide exchange factor 1):

> Guanine-nucleotide exchange factor (GEF) for members of the Arf family of small GTPases involved in trafficking in the early secretory pathway; its GEF activity initiates the coating of nascent vesicles via the localized generation of activated ARFs through replacement of GDP with GTP. Recruitment to cis-Golgi membranes requires membrane association of Arf-GDP and can be regulated by ARF1, ARF3, ARF4 and ARF5. Involved in the recruitment of the COPI coat complex to the endoplasmic reticulum …

**Summary**, from NCBI Gene [8729](https://www.ncbi.nlm.nih.gov/gene/8729):

> This gene encodes a member of the Sec7 domain family. The encoded protein is a guanine nucleotide exchange factor that regulates the recruitment of proteins to membranes by mediating GDP to GTP exchange. The encoded protein is localized to the Golgi apparatus and plays a role in vesicular trafficking by activating ADP ribosylation factor 1. The encoded protein has also been identified as an important host factor for viral replication. Multiple transcript variants have been observed for this …

**Accessions** — [HGNC:4181](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4181) · Entrez [8729](https://www.ncbi.nlm.nih.gov/gene/8729) · UniProt [Q92538](https://www.uniprot.org/uniprotkb/Q92538) · Ensembl [ENSG00000107862](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107862)

## Data

Gene col 2889: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2889); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2889, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2889]; `tensor/DDL_lfc|DDL_z.npy` [2889]; `embed/gene_vectors.npy` [2889]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2889 or target_col == 2889). Every well: [[GBF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GBF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
