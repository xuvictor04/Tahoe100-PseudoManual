---
symbol: "EML6"
type: "gene"
col: 13210
ensembl_id: "ENSG00000214595"
name: "EMAP like 6"
location: "2p16.1"
module: 95
arm: "-"
pooled_cpm: 39.3
n_lines_expressing: 46
n_dd_up: 19
n_dd_down: 20
n_dd_up_clean: 13
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# EML6

*EMAP like 6* — 2p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 3.93× (z +22.9, q 0e+00, up in 40 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.481× (z -12.3, q 7e-32, down in 33 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.542× (z -10.3, q 3e-22, down in 33 of 44 measured lines).
> Its strongest partners by |cos| (76 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OTUD7A]] (+0.61, fdr 2e-05), [[OSBPL3]] (+0.55, fdr 1e-05), [[SH3GL2]] (+0.54, fdr 4e-05); moves opposite to [[OBSL1]] (-0.59, fdr 1e-05), [[MAIP1]] (-0.54, fdr 3e-04), [[MFF-DT]] (-0.54, fdr 6e-04).
> It sits in the **-** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CYP27A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13210.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **3.93×** | +22.9 | 0e+00 | 40/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.76×** | +22.2 | 0e+00 | 40/44 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.61×** | +21.5 | 0e+00 | 38/44 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.47×** | +21.4 | 0e+00 | 41/44 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.46×** | +20.8 | 0e+00 | 42/44 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.52×** | +15.5 | 0e+00 | 39/44 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.25×** | +13.6 | 4e-40 | 33/43 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **4.06×** | +12.3 | 1e-32 | 38/44 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.55×** | +7.3 | 1e-11 | 20/43 (A549, AsPC-1, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.39×** | +5.5 | 2e-06 | 17/44 (NCI-H460, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.35×** | +5.0 | 3e-05 | 16/43 (SW480, RKO, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.21×** | +4.5 | 3e-04 | 16/44 (SW480, PANC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.18× | +3.9 | 0.005 | 18/43 (HOP62, SW480, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.26×** | +3.8 | 0.006 | 15/43 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.24×** | +3.6 | 0.013 | 13/44 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.031 | 9/44 (LOX-IMVI, SW1417, …) | inconsistent across doses |  |
| [[Ciclopirox (drug)]] 5 µM |  | 1.13× | +3.0 | 0.087 | 7/44 (SW 900, PANC-1, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.40×** | +2.9 | 0.087 | 12/43 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Norepinephrine (hydrochloride) (drug)]] 5 µM |  | 1.13× | +2.9 | 0.099 | 8/44 (CFPAC-1, H4, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13210.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.481×** | -12.3 | 7e-32 | 33/43 (PANC-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.542×** | -10.3 | 3e-22 | 33/44 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.568×** | -9.1 | 1e-17 | 27/43 (SNU-1, A498, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.356×** | -9.0 | 2e-17 | 31/44 (A498, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.411×** | -7.8 | 7e-13 | 30/42 (A-427, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.639×** | -7.5 | 5e-12 | 25/44 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.641×** | -7.5 | 6e-12 | 26/44 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.714×** | -5.7 | 1e-06 | 23/43 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.736×** | -4.9 | 5e-05 | 21/42 (AsPC-1, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | **0.754×** | -4.7 | 1e-04 | 22/40 (SW 900, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.760×** | -4.6 | 2e-04 | 14/44 (HS-578T, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.781×** | -4.2 | 0.002 | 22/43 (A-427, RKO, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.629×** | -4.1 | 0.002 | 15/27 (PANC-1, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.789×** | -4.0 | 0.003 | 18/43 (Hs 766T, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.774×** | -4.0 | 0.003 | 19/38 (Hs 766T, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.816×** | -3.4 | 0.022 | 15/44 (SNU-1, A498, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.819×** | -3.4 | 0.025 | 19/44 (Hs 766T, NCI-H23, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.824×** | -3.3 | 0.034 | 9/43 (NCI-H23, Hs 766T, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.821×** | -3.2 | 0.040 | 7/44 (AsPC-1, A549, …) | top dose only |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.884× | -2.9 | 0.082 | 5/44 (PANC-1, RKO, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.885× | -2.9 | 0.084 | 15/44 (HS-578T, SNU-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13210. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 38.8 | 8 | 7 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 5.04× (z +17.3) | [[Digitoxin (drug)]] 5 µM 0.150× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.199× (z -17.3) |
| [[A-427 (line)]] | wt | 196 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.316× (z -13.7) |
| [[A498 (line)]] | wt | 59.1 | 3 | 8 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.11× (z +9.9) | [[Harringtonine (drug)]] 0.5 µM 0.165× (z -16.9) |
| [[SW480 (line)]] | alt | 23.0 | 8 (1 ⚠) | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.96× (z +15.5) | [[Digitoxin (drug)]] 0.5 µM 0.312× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 34.2 | 5 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.57× (z +11.4) | [[Digitoxin (drug)]] 5 µM 0.191× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 15.5 | 10 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 5.85× (z +17.7) | — |
| [[SW 900 (line)]] | alt | 76.6 | 5 | 5 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.25× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.313× (z -9.8) |
| [[HOP62 (line)]] | alt | 10.9 | 8 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 5.52× (z +14.0) | — |
| [[hTERT-HPNE (line)]] | wt | 12.2 | 7 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 10.4× (z +9.5) | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0831× (z -10.1) |
| [[A549 (line)]] | wt | 23.5 | 5 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.45× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.242× (z -8.9) |
| [[LoVo (line)]] | wt | 90.6 | 1 | 6 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.88× (z +9.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.301× (z -13.2) |
| [[LS 180 (line)]] | wt | 37.1 | 5 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.95× (z +12.0) | [[Digitoxin (drug)]] 5 µM 0.209× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.264× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 27.7 | 6 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.45× (z +12.0) | [[Digitoxin (drug)]] 5 µM 0.282× (z -8.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 16.0 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 11.6× (z +14.8) | — |
| [[C32 (line)]] | wt | 10.5 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.66× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 12.1× (z +10.2) | — |
| [[RKO (line)]] | wt | 50.8 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.153× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.237× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 11.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 9.76× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 19.2 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.98× (z +12.0) | — |
| [[Panc 03.27 (line)]] | alt | 13.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.71× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 21.0 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 3.51× (z +9.9) | — |
| [[KATO III (line)]] | alt | 32.7 | 1 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.33× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.164× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.188× (z -12.4) |
| [[SNU-1 (line)]] | wt | 62.0 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0552× (z -18.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.161× (z -12.0) |
| [[SW1417 (line)]] | alt | 50.9 | 1 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.22× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.147× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -13.1) |
| [[HepG2_C3A (line)]] | wt | 42.2 | 3 | 0 | [[Panobinostat (drug)]] 0.05 µM 4.29× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 137 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.262× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 21.9 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.13× (z +9.7) | [[Adagrasib (drug)]] 0.05 µM 0.625× (z -10.1) ⚠ position not correctable |
| [[SW48 (line)]] | wt | 69.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 63.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.234× (z -8.7) |
| [[HS-578T (line)]] | alt | 32.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +12.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.244× (z -9.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 38.2 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 44.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 184 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 48.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0277× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 78.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.241× (z -9.9) ⚠ toxic |
| [[C-33 A (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0498× (z -18.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 22.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 27.1 | 1 | 0 | [[Belinostat (drug)]] 5 µM 4.85× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 19.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.04× (z +10.6) | — |
| [[J82 (line)]] | alt | 14.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.90× (z +11.1) | — |
| [[NCI-H1792 (line)]] | alt | 14.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.38 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.73 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.66 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.56 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 23.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13210), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OTUD7A]] | +0.61 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[OSBPL3]] | +0.55 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[SH3GL2]] | +0.54 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[PIK3CB]] | +0.54 | +0.31 / +0.49 | both halves | 2e-04 |  |
| [[TIAM1]] | +0.52 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[PIP4K2A]] | +0.51 | +0.27 / +0.49 | both halves | 3e-04 |  |
| [[FAM3C]] | +0.50 | +0.37 / +0.38 | both halves | 8e-05 |  |
| [[ARHGAP44]] | +0.50 | +0.36 / +0.53 | both halves | 1e-04 |  |
| [[RPS6KA5]] | +0.50 | +0.32 / +0.43 | both halves | 2e-04 |  |
| [[ADGRB2]] | +0.50 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[WSCD1]] | +0.49 | +0.37 / +0.37 | both halves | 9e-05 |  |
| [[GALNT12]] | +0.48 | +0.23 / +0.45 | both halves | 5e-04 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 19 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OBSL1]] | -0.59 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[MAIP1]] | -0.54 | -0.26 / -0.50 | both halves | 3e-04 |  |
| [[MFF-DT]] | -0.54 | -0.22 / -0.46 | both halves | 6e-04 |  |
| [[THBS4]] | -0.53 | -0.23 / -0.39 | both halves | 5e-04 |  |
| [[GPALPP1]] | -0.51 | -0.26 / -0.43 | both halves | 3e-04 |  |
| [[LATS1]] | -0.50 | -0.18 / -0.51 | ⚠ one half (not replicated) | 9e-04 |  |
| [[ZRANB2-DT]] | -0.49 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[PNISR-AS1]] | -0.49 | -0.25 / -0.42 | both halves | 4e-04 |  |
| [[SUCLG2-DT]] | -0.49 | -0.26 / -0.34 | both halves | 3e-04 |  |
| [[EXOSC10]] | -0.49 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[DHRS4]] | -0.49 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[MKRN3]] | -0.48 | -0.15 / -0.44 | ⚠ not reproduced | 0.001 |  |
| [[MTERF1]] | -0.47 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[RBM48]] | -0.47 | -0.28 / -0.40 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP27A1]] | B | CYP27A1 activity strengthens EML6's drug response | lines that do not express CYP27A1 (9) vs lines expressing it (35) | the lines without CYP27A1 respond 0.54× as strongly (z diff +2.72); strongest at Belinostat 5 µM: 1.43x vs 4.07x (z diff +5.3) | 0.010 | ⚠ within organs, on part of the lines; also absent: RNF217, ENSG00000224905, ESYT3; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CYP27A1]] | B | CYP27A1 activity lowers EML6's level | lines that do not express CYP27A1 (10) vs lines expressing it (40) | 2.46× higher at baseline in the lines without CYP27A1 | 0.036 | ⚠ within organs, on part of the lines; also absent: RNF217, ENSG00000224905, ESYT3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **-** arm (projection on the module's main direction -0.442). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (0.8, 34.2); signed map (-10.3, 46.2). **Vector** length 90.3, 22.5% of its response variance represented; |z| ≥ 3 in 1,404 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +21.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.3 | +20.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.1 | +15.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.0 | +12.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.3 | +13.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +3.6 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.9 | +1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -2.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -7.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.6 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -3.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -2.8 | -4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -7.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | +1.3 |

## What is on record

|  |  |
|---|---|
| Name | EMAP like 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.1 — chr2:54,723,499-54,972,025 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ42562 |
| Gene groups (HGNC) | WD repeat domain containing; EMAP like |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZMW3](https://www.uniprot.org/uniprotkb/Q6ZMW3) (Echinoderm microtubule-associated protein-like 6):

> Microtubule-associated protein that plays an important role in the regulation of oocyte meiotic progression by maintaining spindle integrity and facilitating proper chromosome alignment.

**Summary**, from NCBI Gene [400954](https://www.ncbi.nlm.nih.gov/gene/400954):

> Predicted to enable microtubule binding activity. Predicted to be involved in meiotic cell cycle. Predicted to be located in cytoplasm; microtubule; and spindle. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:35412](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:35412) · Entrez [400954](https://www.ncbi.nlm.nih.gov/gene/400954) · UniProt [Q6ZMW3](https://www.uniprot.org/uniprotkb/Q6ZMW3) · Ensembl [ENSG00000214595](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214595)

## Data

Gene col 13210: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13210); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13210, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13210]; `tensor/DDL_lfc|DDL_z.npy` [13210]; `embed/gene_vectors.npy` [13210]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13210 or target_col == 13210). Every well: [[EML6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EML6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
