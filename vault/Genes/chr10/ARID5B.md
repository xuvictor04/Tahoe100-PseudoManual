---
symbol: "ARID5B"
type: "gene"
col: 7429
ensembl_id: "ENSG00000150347"
name: "AT-rich interaction domain 5B"
location: "10q21.2"
module: 123
arm: "+"
pooled_cpm: 101.14
n_lines_expressing: 44
n_dd_up: 44
n_dd_down: 32
n_dd_up_clean: 42
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 11
direction_downstream: 10
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# ARID5B

*AT-rich interaction domain 5B* — 10q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.88× (z +14.1, q 4e-42, up in 41 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.446× (z -12.7, q 2e-34, down in 34 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 0.548× (z -9.0, q 4e-17, down in 35 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF608]] (+0.68, fdr 7e-06), [[FOSL2]] (+0.65, fdr 7e-06), [[ARHGAP24]] (+0.61, fdr 1e-05); moves opposite to [[CTNNBIP1]] (-0.58, fdr 1e-05), [[TPD52L2]] (-0.55, fdr 1e-05), [[CAPN10]] (-0.53, fdr 3e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[RGCC]] → it (grade B ⚠); 10 go from it, the strongest it → [[RHOBTB3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 2 with an alert ⚠; shown: the 15 strongest. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7429.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.88×** | +14.1 | 4e-42 | 41/42 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.22×** | +12.5 | 1e-33 | 31/42 (NCI-H1573, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.97×** | +10.7 | 2e-24 | 35/42 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.90×** | +10.3 | 8e-23 | 36/44 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.57×** | +10.0 | 1e-21 | 28/42 (NCI-H23, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.87×** | +9.8 | 1e-20 | 38/43 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.91×** | +9.8 | 1e-20 | 33/42 (NCI-H1573, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.54×** | +8.2 | 1e-14 | 32/42 (SW480, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.72×** | +8.2 | 2e-14 | 32/41 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.71×** | +8.1 | 3e-14 | 32/42 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.64×** | +8.0 | 5e-14 | 34/43 (SW480, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +7.1 | 4e-11 | 29/42 (PANC-1, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.35×** | +6.5 | 3e-09 | 30/42 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.50×** | +6.3 | 9e-09 | 32/41 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **2.20×** | +6.3 | 1e-08 | 31/44 (SW480, A-172, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7429.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.446×** | -12.7 | 2e-34 | 34/43 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.512×** | -10.6 | 1e-23 | 34/42 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.538×** | -9.4 | 9e-19 | 26/39 (RPMI-7951, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.548×** | -9.0 | 4e-17 | 35/42 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.587×** | -8.4 | 4e-15 | 33/42 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.590×** | -7.7 | 1e-12 | 27/39 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.390×** | -7.5 | 4e-12 | 35/42 (CHP-212, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.626×** | -7.4 | 9e-12 | 31/42 (LoVo, H4, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.642×** | -6.8 | 9e-10 | 29/41 (AN3 CA, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.661×** | -6.6 | 3e-09 | 28/42 (LoVo, BT-474, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -6.6 | 3e-09 | 26/43 (A498, BT-474, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.447×** | -6.5 | 5e-09 | 30/42 (LOX-IMVI, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.693×** | -5.8 | 3e-07 | 28/42 (LoVo, SW1417, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.529×** | -5.1 | 1e-05 | 18/32 (LoVo, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.532×** | -5.1 | 2e-05 | 25/42 (LOX-IMVI, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | **0.811×** | -4.7 | 9e-05 | 21/43 (KATO III, COLO 205, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.568×** | -4.5 | 2e-04 | 22/42 (KATO III, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.761×** | -4.2 | 9e-04 | 19/42 (A498, NCI-H1792, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.612×** | -3.9 | 0.002 | 20/42 (NCI-H1792, J82, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.5 µM |  | **0.781×** | -3.9 | 0.002 | 20/42 (SHP-77, NCI-H1792, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.735×** | -3.5 | 0.012 | 17/43 (HOP62, LoVo, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7429. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 112 | 16 | 9 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.03× (z +16.5) | [[Auranofin (drug)]] 5 µM 0.243× (z -15.0) |
| [[SW480 (line)]] | alt | 160 | 13 | 6 (5 ⚠) | [[Binimetinib (drug)]] 0.5 µM 2.65× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.461× (z -8.7) |
| [[A-172 (line)]] | wt | 107 | 13 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +17.2) | — |
| [[NCI-H460 (line)]] | wt | 94.5 | 10 (3 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 5.21× (z +16.3) | [[Selinexor (drug)]] 5 µM 0.500× (z -9.7) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 76.5 | 10 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.184× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 47.6 | 10 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 22.7× (z +21.5) | — |
| [[hTERT-HPNE (line)]] | wt | 177 | 5 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.04× (z +15.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 111 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +25.6) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -13.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 134 | 2 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +20.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -16.0) |
| [[BT-474 (line)]] | alt | 275 | 1 | 5 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.22× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -15.3) |
| [[J82 (line)]] | alt | 113 | 3 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.30× (z +10.0) | [[Ixazomib citrate (drug)]] 5 µM 0.327× (z -9.4) |
| [[PANC-1 (line)]] | alt | 50.9 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.37× (z +13.9) | — |
| [[CHP-212 (line)]] | wt | 298 | 0 | 5 (3 ⚠) | — | [[Abemaciclib (drug)]] 5 µM 0.0263× (z -10.7) |
| [[LS 180 (line)]] | wt | 225 | 2 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.75× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.438× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 137 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.129× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -8.9) |
| [[SNU-1 (line)]] | wt | 172 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.0684× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.244× (z -11.1) |
| [[SNU-423 (line)]] | alt | 250 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -10.2) |
| [[HOP62 (line)]] | alt | 140 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +17.4) | [[Ixazomib citrate (drug)]] 5 µM 0.252× (z -11.0) |
| [[HS-578T (line)]] | alt | 78.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +17.8) | — |
| [[NCI-H2030 (line)]] | alt | 90.2 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.24× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 73.6 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +25.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -8.5) |
| [[SW 900 (line)]] | alt | 195 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.96× (z +9.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.288× (z -12.2) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 102 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.79× (z +11.0) | — |
| [[CFPAC-1 (line)]] | alt | 83.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +12.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.302× (z -10.0) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 162 | 2 | 1 (1 ⚠) | [[Ponatinib (drug)]] 5 µM 2.65× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -13.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 169 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.144× (z -13.0) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -11.1) |
| [[A549 (line)]] | wt | 32.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +11.2) | — |
| [[H4 (line)]] | wt | 112 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[5-Azacytidine (drug)]] 5 µM 0.270× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 226 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.279× (z -10.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 36.1 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.05× (z +10.2) | — |
| [[SW48 (line)]] | wt | 125 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.225× (z -9.1) |
| [[AN3 CA (line)]] | alt | 60.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0778× (z -11.4) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 63.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.253× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 39.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.82× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 75.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -8.8) |
| [[SW 1088 (line)]] | alt | 236 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0654× (z -10.7) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 90.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0743× (z -9.0) ⚠ toxic |
| [[SW1417 (line)]] | alt | 122 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.42× (z +9.6) | — |
| [[A-427 (line)]] | wt | 13.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.80 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.59 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7429), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF608]] | +0.68 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[FOSL2]] | +0.65 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[ARHGAP24]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ETS2]] | +0.60 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[TGFB2]] | +0.58 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[SPTLC3]] | +0.57 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[FILIP1L]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[LATS2]] | +0.57 | +0.58 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[SEMA3C]] | +0.56 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ALCAM]] | +0.56 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[CFH]] | +0.56 | +0.56 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[CITED2]] | +0.55 | +0.47 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTNNBIP1]] | -0.58 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[TPD52L2]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[CAPN10]] | -0.53 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[NAP1L4]] | -0.52 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[DPP9]] | -0.50 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[PPM1F]] | -0.49 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[NIPA2]] | -0.49 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[LIMK1]] | -0.48 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[SMG1P5]] | -0.48 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[GDAP2]] | -0.48 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ZFYVE21]] | -0.48 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[UFD1]] | -0.48 | -0.44 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGCC]] | B | RGCC activity raises ARID5B's level | lines that do not express RGCC (25) vs lines expressing it (25) | 1.25× lower at baseline in the lines without RGCC | 0.049 | ⚠ within organs, on part of the lines; also absent: IL20RA, TINAGL1, CLIC5 |
| [[ZNF608]] | B | ZNF608 activity raises ARID5B's level | lines that do not express ZNF608 (12) vs lines expressing it (38) | 1.79× lower at baseline in the lines without ZNF608 | 0.067 | ⚠ within organs, on part of the lines; also absent: LINC01170, GDF15 |
| [[CCBE1]] | B | CCBE1 activity raises ARID5B's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 1.53× lower at baseline in the lines without CCBE1 | 0.067 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[SPTLC3]] | B | SPTLC3 activity raises ARID5B's level | lines that do not express SPTLC3 (16) vs lines expressing it (34) | 1.97× lower at baseline in the lines without SPTLC3 | 0.074 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[EYA4]] | B | EYA4 activity raises ARID5B's level | lines that do not express EYA4 (30) vs lines expressing it (20) | 1.79× lower at baseline in the lines without EYA4 | 0.077 | ⚠ within organs, on part of the lines; also absent: SNAP25, BICC1, IL31RA |
| [[TNFAIP6]] | B | TNFAIP6 activity raises ARID5B's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 1.64× lower at baseline in the lines without TNFAIP6 | 0.084 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF |
| [[RNF144B]] | B | RNF144B activity raises ARID5B's level | lines that do not express RNF144B (15) vs lines expressing it (35) | 2.33× lower at baseline in the lines without RNF144B | 0.088 | ⚠ within organs, on part of the lines; also absent: SPTLC3, TMEM92-AS1, ITGA2; maybe low, not absent |
| [[NEDD9]] | B | NEDD9 activity raises ARID5B's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 2.46× lower at baseline in the lines without NEDD9 | 0.089 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[TGFB2]] | B | TGFB2 activity raises ARID5B's level | lines that do not express TGFB2 (15) vs lines expressing it (35) | 1.33× lower at baseline in the lines without TGFB2 | 0.091 | ⚠ within organs, on part of the lines; also absent: CTSF, EHD3, MAP9 |
| [[PPARGC1A]] | B | PPARGC1A activity raises ARID5B's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 2.52× lower at baseline in the lines without PPARGC1A | 0.095 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2 |
| [[TNFAIP3]] | C | TNFAIP3 activity raises ARID5B's level | lines that do not express TNFAIP3 (3) vs lines expressing it (47) | 6.55× lower at baseline in the lines without TNFAIP3 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IER3, JAG1, ATXN1; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHOBTB3]] | B | ARID5B activity raises RHOBTB3's level | lines that do not express ARID5B (6) vs lines expressing it (44) | 3.32× lower at baseline in the lines without ARID5B | 0.038 | ⚠ within organs, on part of the lines; also absent: TNFAIP3, ATXN1, SSUH2 |
| [[ZBTB10]] | B | ARID5B activity raises ZBTB10's level | lines that do not express ARID5B (6) vs lines expressing it (44) | 2.10× lower at baseline in the lines without ARID5B | 0.042 | ⚠ within organs, on part of the lines; also absent: TNFAIP3, ATXN1, SSUH2 |
| [[ETS2]] | B | ARID5B activity raises ETS2's level | lines that do not express ARID5B (6) vs lines expressing it (44) | 2.83× lower at baseline in the lines without ARID5B | 0.050 | ⚠ within organs, on part of the lines; also absent: TNFAIP3, ATXN1, SSUH2 |
| [[PLD1]] | B | ARID5B activity raises PLD1's level | lines that do not express ARID5B (6) vs lines expressing it (44) | 4.13× lower at baseline in the lines without ARID5B | 0.052 | ⚠ within organs, on part of the lines; also absent: TNFAIP3, ATXN1, SSUH2 |
| [[TGFB2]] | B | ARID5B activity raises TGFB2's level | lines that do not express ARID5B (6) vs lines expressing it (44) | 3.23× lower at baseline in the lines without ARID5B | 0.056 | ⚠ within organs, on part of the lines; also absent: TNFAIP3, ATXN1, SSUH2 |
| [[TNS3]] | B | ARID5B activity raises TNS3's level | lines that do not express ARID5B (6) vs lines expressing it (44) | 2.51× lower at baseline in the lines without ARID5B | 0.078 | ⚠ within organs, on part of the lines; also absent: TNFAIP3, ATXN1, SSUH2 |
| [[NR3C1]] | B | ARID5B activity raises NR3C1's level | lines that do not express ARID5B (6) vs lines expressing it (44) | 2.71× lower at baseline in the lines without ARID5B | 0.082 | ⚠ within organs, on part of the lines; also absent: TNFAIP3, ATXN1, SSUH2 |
| [[FOSL2]] | B | ARID5B activity raises FOSL2's level | lines that do not express ARID5B (6) vs lines expressing it (44) | 1.48× lower at baseline in the lines without ARID5B | 0.089 | ⚠ within organs, on part of the lines; also absent: TNFAIP3, ATXN1, SSUH2 |
| cells under [[Epirubicin (hydrochloride) (drug)]] 5 µM | B | ARID5B activity raises the cells' numbers under Epirubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express ARID5B (6) vs lines expressing it (42) | the lines without ARID5B: 0.51× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: TNFAIP3, ATXN1, SSUH2 |
| [[TNFAIP3]] | C | ARID5B activity raises TNFAIP3's level | lines that do not express ARID5B (6) vs lines expressing it (44) | 2.67× lower at baseline in the lines without ARID5B | 0.063 | ⚠ within organs, on part of the lines; also absent: TNFAIP3, ATXN1, SSUH2; co-absent with the target |

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.660). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.0, 13.3); signed map (48.8, 13.0). **Vector** length 138, 45.3% of its response variance represented; |z| ≥ 3 in 1,993 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +12.2 | +14.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +11.0 | +9.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.4 | +9.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +7.9 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.8 | +7.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +7.5 | +8.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.6 | +8.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +6.6 | +8.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.7 | -10.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.1 | -9.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.1 | -7.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.7 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.4 | -8.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.3 | -7.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.1 | -6.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.2 | -0.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.2 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | AT-rich interaction domain 5B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.2 — chr10:61,901,684-62,096,944 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21150, MRF2 |
| Gene groups (HGNC) | AT-rich interaction domain containing |
| Hallmark sets | ANDROGEN_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 3 pathways, smallest: HDMs demethylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14865](https://www.uniprot.org/uniprotkb/Q14865) (AT-rich interactive domain-containing protein 5B):

> Transcription coactivator that binds to the 5'-AATA[CT]-3' core sequence and plays a key role in adipogenesis and liver development. Acts by forming a complex with phosphorylated PHF2, which mediates demethylation at Lys-336, leading to target the PHF2-ARID5B complex to target promoters, where PHF2 mediates demethylation of dimethylated 'Lys-9' of histone H3 (H3K9me2), followed by transcription activation of target genes. The PHF2-ARID5B complex acts as a coactivator of HNF4A in liver. Required …

**Summary**, from NCBI Gene [84159](https://www.ncbi.nlm.nih.gov/gene/84159):

> This gene encodes a member of the AT-rich interaction domain (ARID) family of DNA binding proteins. The encoded protein forms a histone H3K9Me2 demethylase complex with PHD finger protein 2 and regulates the transcription of target genes involved in adipogenesis and liver development. This gene also plays a role in cell growth and differentiation of B-lymphocyte progenitors, and single nucleotide polymorphisms in this gene are associated with acute lymphoblastic leukemia. Alternatively spliced …

**Accessions** — [HGNC:17362](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17362) · Entrez [84159](https://www.ncbi.nlm.nih.gov/gene/84159) · UniProt [Q14865](https://www.uniprot.org/uniprotkb/Q14865) · Ensembl [ENSG00000150347](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150347)

## Data

Gene col 7429: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7429); `tables/drug_effects.parquet` (82 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7429, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7429]; `tensor/DDL_lfc|DDL_z.npy` [7429]; `embed/gene_vectors.npy` [7429]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7429 or target_col == 7429). Every well: [[ARID5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARID5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
