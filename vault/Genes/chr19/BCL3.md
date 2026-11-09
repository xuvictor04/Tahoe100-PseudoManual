---
symbol: "BCL3"
type: "gene"
col: 916
ensembl_id: "ENSG00000069399"
name: "BCL3 transcription coactivator"
location: "19q13.32"
module: 14
arm: "+"
pooled_cpm: 35.51
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 34
n_dd_up_clean: 10
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 22
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# BCL3

*BCL3 transcription coactivator* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.65× (z +30.5, q 0e+00, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (15 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.235× (z -18.0, q 0e+00, down in 43 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFAIP2]] (+0.77, fdr 7e-06), [[IRF1]] (+0.73, fdr 7e-06), [[NFKBIA]] (+0.73, fdr 7e-06); moves opposite to [[GPR89A]] (-0.65, fdr 1e-05), [[MFN1]] (-0.61, fdr 1e-05), [[TNPO3]] (-0.59, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[GATA6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 916.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.65×** | +30.5 | 0e+00 | 44/45 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **5.10×** | +19.6 | 0e+00 | 42/45 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.30×** | +10.4 | 4e-23 | 30/44 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.94×** | +8.9 | 6e-17 | 38/47 (HEC-1-A, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.00×** | +8.6 | 7e-16 | 27/46 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +5.9 | 3e-07 | 27/43 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +4.6 | 4e-04 | 23/46 (Panc 03.27, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~23% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +4.6 | 4e-04 | 16/35 (HS-578T, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.006 | 20/45 (LOX-IMVI, A549, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.32×** | +3.5 | 0.026 | 17/43 (AsPC-1, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.043 | 15/46 (HepG2/C3A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.045 | 15/46 (C32, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.047 | 15/46 (MIA PaCa-2, HOP62, …) | two highest doses | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.27× | +3.0 | 0.10 | 10/46 (LS 180, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 916.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.235×** | -18.0 | 0e+00 | 43/46 (Panc 03.27, Hs 766T, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.299×** | -15.1 | 0e+00 | 43/46 (LoVo, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.321×** | -14.1 | 4e-43 | 45/46 (HT-29, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.411×** | -10.4 | 2e-23 | 38/46 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.564×** | -10.1 | 8e-22 | 33/45 (HT-29, Hs 766T, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.449×** | -10.0 | 2e-21 | 38/46 (HT-29, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.530×** | -7.9 | 2e-13 | 29/46 (NCI-H460, HT-29, …) | rises with dose | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.318×** | -7.5 | 6e-12 | 36/44 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.613×** | -6.1 | 7e-08 | 26/46 (SW 900, HT-29, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.709×** | -6.0 | 8e-08 | 29/46 (H4, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.606×** | -6.0 | 1e-07 | 22/34 (NCI-H2347, Hs 766T, …) | rises with dose | composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | **0.719×** | -5.8 | 3e-07 | 35/46 (C32, COLO 205, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.639×** | -5.4 | 4e-06 | 24/45 (SNU-423, LOX-IMVI, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.745×** | -5.2 | 9e-06 | 28/46 (H4, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.674×** | -4.9 | 4e-05 | 27/45 (H4, NCI-H1573, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.701×** | -4.4 | 3e-04 | 27/45 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.779×** | -4.4 | 3e-04 | 26/46 (C32, SHP-77, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.723×** | -4.0 | 0.001 | 23/46 (Panc 03.27, NCI-H1573, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.725×** | -4.0 | 0.002 | 20/46 (MIA PaCa-2, LoVo, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.728×** | -3.8 | 0.004 | 20/46 (MIA PaCa-2, LOX-IMVI, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.575×** | -3.6 | 0.007 | 22/46 (HT-29, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.61 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 916. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 105 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -20.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0814× (z -16.9) |
| [[A498 (line)]] | wt | 44.1 | 4 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.57× (z +24.9) | [[Auranofin (drug)]] 5 µM 0.231× (z -11.5) |
| [[A549 (line)]] | wt | 86.4 | 4 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.89× (z +23.2) | [[Panobinostat (drug)]] 5 µM 0.283× (z -10.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.323× (z -9.6) |
| [[LoVo (line)]] | wt | 41.9 | 3 (1 ⚠) | 5 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 4.74× (z +11.1) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 4.30× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.101× (z -17.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.237× (z -10.7) |
| [[C32 (line)]] | wt | 38.1 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +10.9) | [[Auranofin (drug)]] 5 µM 0.0914× (z -15.6) |
| [[NCI-H460 (line)]] | wt | 26.8 | 3 | 4 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 5.99× (z +13.6) | [[Auranofin (drug)]] 5 µM 0.256× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 48.6 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.60× (z +20.7) | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 25.8 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 20.0× (z +24.1) | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -8.5) |
| [[Hs 766T (line)]] | wt | 70.3 | 0 | 6 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.112× (z -17.3) |
| [[HS-578T (line)]] | alt | 46.7 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.54× (z +20.0) | [[Panobinostat (drug)]] 5 µM 0.208× (z -10.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[PANC-1 (line)]] | alt | 25.7 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +27.2) | [[Auranofin (drug)]] 5 µM 0.214× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 43.6 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +17.8) | [[Auranofin (drug)]] 5 µM 0.217× (z -11.5) |
| [[HOP62 (line)]] | alt | 51.4 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -11.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.226× (z -9.3) |
| [[KATO III (line)]] | alt | 49.0 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.81× (z +17.9) | [[Auranofin (drug)]] 5 µM 0.146× (z -12.6) |
| [[NCI-H2347 (line)]] | alt | 27.3 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +17.7) | [[Auranofin (drug)]] 5 µM 0.199× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 68.8 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +18.1) | [[Auranofin (drug)]] 5 µM 0.0391× (z -26.0) |
| [[SW 900 (line)]] | alt | 62.6 | 0 | 5 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0868× (z -16.7) |
| [[SW48 (line)]] | wt | 16.4 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.88× (z +12.4) | [[Panobinostat (drug)]] 0.5 µM 0.0277× (z -14.3) |
| [[A-172 (line)]] | wt | 22.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +21.8) | — |
| [[H4 (line)]] | wt | 18.9 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +10.1) | [[Selinexor (drug)]] 5 µM 0.167× (z -11.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Temsirolimus (drug)]] 0.5 µM 0.122× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 24.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.74× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 28.9 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +21.9) | [[Auranofin (drug)]] 5 µM 0.234× (z -9.1) |
| [[LS 180 (line)]] | wt | 31.8 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.131× (z -12.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.191× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 34.3 | 2 (1 ⚠) | 2 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.73× (z +11.6) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.16× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -11.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.168× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 25.7 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -10.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.250× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 59.6 | 1 | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 5.07× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -10.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SHP-77 (line)]] | alt | 37.5 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.154× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~83% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.180× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 11.4 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.94× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.0945× (z -10.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.128× (z -8.9) |
| [[SNU-423 (line)]] | alt | 32.0 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.25× (z +19.6) | [[Dinaciclib (drug)]] 5 µM 0.172× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Peretinoin (drug)]] 5 µM 0.238× (z -8.6) |
| [[BT-474 (line)]] | alt | 50.9 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.160× (z -12.3) |
| [[COLO 205 (line)]] | alt | 39.0 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.103× (z -11.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.162× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 34.4 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +18.0) | [[Auranofin (drug)]] 5 µM 0.160× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 23.6 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +11.1) | [[Auranofin (drug)]] 5 µM 0.210× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 32.8 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.91× (z +16.0) | [[Auranofin (drug)]] 5 µM 0.139× (z -10.8) |
| [[SW1417 (line)]] | alt | 24.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.31× (z +18.6) | — |
| [[SW480 (line)]] | alt | 16.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.169× (z -11.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HCT15 (line)]] | alt | 24.4 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.118× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 21.8 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -12.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[CHP-212 (line)]] | wt | 29.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.26× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 20.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +10.3) | — |
| [[RKO (line)]] | wt | 9.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +10.0) | — |
| [[A-427 (line)]] | wt | 6.89 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.23 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 916), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFAIP2]] | +0.77 | +0.72 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[IRF1]] | +0.73 | +0.72 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 545 |
| [[NFKBIA]] | +0.73 | +0.68 / +0.71 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 904 |
| [[CX3CL1]] | +0.72 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[NFKB2]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 999 |
| [[EFNA1]] | +0.70 | +0.62 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[STAT5A]] | +0.70 | +0.67 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 411 |
| [[REL]] | +0.70 | +0.61 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 952 |
| [[SYNPO]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[ZC3H12A]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 617 |
| [[TEF]] | +0.68 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[PLXNB2]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR89A]] | -0.65 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[MFN1]] | -0.61 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[TNPO3]] | -0.59 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[THOC5]] | -0.58 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[ZCCHC17]] | -0.57 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[RAP1GDS1]] | -0.57 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[DIP2A]] | -0.57 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[SLC30A6]] | -0.55 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[VPS53]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 20, C 2. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GATA6]] | B | GATA6 activity raises BCL3's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 1.84× lower at baseline in the lines without GATA6 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[TNFAIP2]] | B | TNFAIP2 activity raises BCL3's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 1.97× lower at baseline in the lines without TNFAIP2 | 0.005 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[ELF3]] | B | ELF3 activity raises BCL3's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 1.73× lower at baseline in the lines without ELF3 | 0.008 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[GBP2]] | B | GBP2 activity raises BCL3's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.18× lower at baseline in the lines without GBP2 | 0.010 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[CXCL3]] | B | CXCL3 activity raises BCL3's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 1.95× lower at baseline in the lines without CXCL3 | 0.010 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[ETS2]] | B | ETS2 activity raises BCL3's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 2.09× lower at baseline in the lines without ETS2 | 0.012 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[BDKRB2]] | B | BDKRB2 activity raises BCL3's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 1.84× lower at baseline in the lines without BDKRB2 | 0.019 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[STAT5A]] | B | STAT5A activity raises BCL3's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 1.87× lower at baseline in the lines without STAT5A | 0.022 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[PTGES]] | B | PTGES activity raises BCL3's level | lines that do not express PTGES (17) vs lines expressing it (33) | 1.82× lower at baseline in the lines without PTGES | 0.034 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[LGALS3]] | B | LGALS3 activity raises BCL3's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 2.10× lower at baseline in the lines without LGALS3 | 0.041 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[SLC6A7]] | B | SLC6A7 activity raises BCL3's level | lines that do not express SLC6A7 (27) vs lines expressing it (23) | 1.56× lower at baseline in the lines without SLC6A7 | 0.041 | ⚠ within organs, on part of the lines; also absent: IL1B, UGT1A6, UGT1A9 |
| [[ANO9]] | B | ANO9 activity raises BCL3's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 1.57× lower at baseline in the lines without ANO9 | 0.060 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.832). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.2, 4.9); signed map (44.0, 6.7). **Vector** length 139, 44.1% of its response variance represented; |z| ≥ 3 in 1,374 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NF-kB* (control, mean cos +0.59 to 12); *inflammatory response* (hallmark, mean cos +0.51 to 22); *Chemokine receptors bind chemokines* (reactome, mean cos +0.50 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +15.2 | +30.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +13.3 | +19.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.3 | +10.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.6 | +4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.3 | +3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.9 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.6 | +1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.6 | +3.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.4 | -18.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -7.7 | -7.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -7.6 | -10.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -6.3 | -5.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -6.2 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.9 | -6.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -5.0 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | BCL3 transcription coactivator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:44,747,705-44,760,044 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously D19S37, BCL4 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; MicroRNA protein coding host genes; NFKB inhibitor family |
| Hallmark sets | ALLOGRAFT_REJECTION, TNFA_SIGNALING_VIA_NFKB, G2M_CHECKPOINT |
| Matched by | ensembl_id |

**Function**, from UniProt [P20749](https://www.uniprot.org/uniprotkb/P20749) (B-cell lymphoma 3 protein):

> Contributes to the regulation of transcriptional activation of NF-kappa-B target genes. In the cytoplasm, inhibits the nuclear translocation of the NF-kappa-B p50 subunit. In the nucleus, acts as transcriptional activator that promotes transcription of NF-kappa-B target genes. Contributes to the regulation of cell proliferation (By similarity).

**Summary**, from NCBI Gene [602](https://www.ncbi.nlm.nih.gov/gene/602):

> This gene is a proto-oncogene candidate. It is identified by its translocation into the immunoglobulin alpha-locus in some cases of B-cell leukemia. The protein encoded by this gene contains seven ankyrin repeats, which are most closely related to those found in I kappa B proteins. This protein functions as a transcriptional co-activator that activates through its association with NF-kappa B homodimers. The expression of this gene can be induced by NF-kappa B, which forms a part of the …

**Accessions** — [HGNC:998](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:998) · Entrez [602](https://www.ncbi.nlm.nih.gov/gene/602) · UniProt [P20749](https://www.uniprot.org/uniprotkb/P20749) · Ensembl [ENSG00000069399](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069399)

## Data

Gene col 916: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 916); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 916, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 916]; `tensor/DDL_lfc|DDL_z.npy` [916]; `embed/gene_vectors.npy` [916]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 916 or target_col == 916). Every well: [[BCL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
