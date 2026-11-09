---
symbol: "KIF14"
type: "gene"
col: 3968
ensembl_id: "ENSG00000118193"
name: "kinesin family member 14"
location: "1q32.1"
module: 22
arm: "+"
pooled_cpm: 87.79
n_lines_expressing: 49
n_dd_up: 25
n_dd_down: 35
n_dd_up_clean: 7
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# KIF14

*kinesin family member 14* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.86× (z +14.9, q 0e+00, up in 34 of 47 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Docetaxel (drug)]] 5 µM: 1.23× (z +4.9, q 4e-05, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (16 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.551× (z -14.3, q 7e-44, down in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~69% of this change. The strongest without an alert is [[Amsacrine (drug)]] 5 µM: 0.711× (z -8.2, q 5e-14, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF4A]] (+0.91, fdr 7e-06), [[KNL1]] (+0.90, fdr 7e-06), [[DLGAP5]] (+0.90, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 18 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3968.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.86×** | +14.9 | 0e+00 | 34/47 (NCI-H2347, NCI-H2030, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.72×** | +9.3 | 6e-18 | 39/47 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.59×** | +7.7 | 4e-12 | 29/47 (NCI-H2347, C32, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **1.55×** | +7.4 | 2e-11 | 30/47 (KATO III, C-33 A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.46×** | +6.5 | 1e-08 | 29/47 (KATO III, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.45×** | +6.3 | 3e-08 | 29/47 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.41×** | +5.9 | 3e-07 | 27/47 (A-172, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.26×** | +5.7 | 9e-07 | 26/47 (SW 900, NCI-H1792, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.39×** | +5.7 | 9e-07 | 26/46 (A549, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.35×** | +5.1 | 2e-05 | 24/47 (HT-29, SW 900, …) | all doses, flat | low cells (technical?) |
| [[Docetaxel (drug)]] 5 µM |  | **1.23×** | +4.9 | 4e-05 | 23/47 (HT-29, NCI-H2030, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.74×** | +4.9 | 4e-05 | 23/46 (J82, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.33×** | +4.9 | 4e-05 | 28/47 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change | **1.33×** | +4.7 | 1e-04 | 22/43 (KATO III, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.31×** | +4.7 | 1e-04 | 25/46 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.019 | 17/47 (RKO, HT-29, …) | rises with dose |  |
| [[vincristine (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.021 | 16/47 (HT-29, RKO, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.023 | 18/47 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.024 | 16/47 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.027 | 19/46 (RKO, HOP62, …) | all doses, flat |  |
| [[AZD1390 (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.054 | 17/47 (Panc 03.27, KATO III, …) | inconsistent across doses |  |
| [[Hexylresorcinol (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.054 | 14/47 (SW 900, LS 180, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 0.5 µM |  | 1.18× | +2.9 | 0.091 | 11/47 (SW 900, HT-29, …) | rises with dose |  |
| [[Furosemide (drug)]] 5 µM |  | 1.12× | +2.8 | 0.096 | 3/47 (Hs 766T, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3968.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.551×** | -14.3 | 7e-44 | 43/47 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.460×** | -13.2 | 2e-37 | 45/47 (A498, LoVo, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.711×** | -8.2 | 5e-14 | 29/47 (A549, A498, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.648×** | -7.1 | 2e-10 | 28/47 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.679×** | -6.6 | 5e-09 | 36/47 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.720×** | -5.6 | 2e-06 | 27/47 (A549, LS 180, …) | two highest doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.726×** | -5.2 | 1e-05 | 30/47 (A-172, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.776×** | -5.2 | 2e-05 | 31/47 (A-427, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.756×** | -5.0 | 3e-05 | 24/47 (A-427, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.744×** | -5.0 | 3e-05 | 24/47 (NCI-H1573, SW 1088, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.745×** | -4.8 | 7e-05 | 27/47 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.787×** | -4.8 | 7e-05 | 22/47 (SW480, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.755×** | -4.8 | 8e-05 | 22/47 (HEC-1-A, J82, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.765×** | -4.6 | 2e-04 | 25/47 (SW 1088, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.760×** | -4.5 | 3e-04 | 21/47 (SW48, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.780×** | -4.5 | 3e-04 | 24/47 (A-427, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[palbociclib (drug)]] 5 µM |  | **0.612×** | -4.4 | 4e-04 | 23/47 (SW480, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.837× | -4.3 | 6e-04 | 23/47 (HCT15, A-427, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.845× | -4.0 | 0.002 | 20/47 (NCI-H1792, HOP62, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.848× | -3.9 | 0.002 | 19/47 (A-427, A498, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.651×** | -3.8 | 0.003 | 22/47 (SW 900, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.05 µM |  | 0.854× | -3.6 | 0.007 | 15/47 (SNU-1, NCI-H460, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.805×** | -3.5 | 0.008 | 16/46 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.680×** | -3.4 | 0.012 | 14/47 (HEC-1-A, Hs 766T, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.93 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3968. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 99.6 | 1 (1 ⚠) | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +11.9) ⚠ cell-cycle shift, would explain all of this change | [[Amsacrine (drug)]] 5 µM 0.361× (z -13.2) |
| [[A-172 (line)]] | wt | 93.1 | 2 (2 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.9) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.296× (z -15.0) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.384× (z -11.8) |
| [[A498 (line)]] | wt | 88.2 | 0 | 8 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.232× (z -19.2) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.400× (z -12.0) |
| [[H4 (line)]] | wt | 124 | 0 | 7 (6 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.145× (z -15.8) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.295× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 82.4 | 0 | 7 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.195× (z -15.0) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.181× (z -11.0) |
| [[LS 180 (line)]] | wt | 75.3 | 0 | 7 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.120× (z -18.8) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.311× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 113 | 0 | 6 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.367× (z -12.4) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -10.4) |
| [[C32 (line)]] | wt | 129 | 3 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +14.1) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.448× (z -9.6) ⚠ cell-cycle shift, explains ~69% of this change |
| [[A-427 (line)]] | wt | 104 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.161× (z -21.6) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.400× (z -10.8) |
| [[KATO III (line)]] | alt | 51.4 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.29× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | — |
| [[HOP62 (line)]] | alt | 173 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +12.3) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.433× (z -12.6) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -10.0) |
| [[LoVo (line)]] | wt | 55.0 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.355× (z -13.2) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.457× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 65.5 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +22.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 81.4 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.123× (z -11.5) ⚠ cell-cycle shift, explains ~60% of this change |
| [[AN3 CA (line)]] | alt | 121 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.180× (z -10.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.202× (z -9.8) |
| [[HS-578T (line)]] | alt | 40.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +15.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[hTERT-HPNE (line)]] | wt | 58.9 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.309× (z -10.3) ⚠ cell-cycle shift, explains ~69% of this change |
| [[MIA PaCa-2 (line)]] | alt | 138 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.210× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 57.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +18.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 70.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +17.9) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.366× (z -12.1) ⚠ cell-cycle shift, explains ~69% of this change |
| [[RPMI-7951 (line)]] | alt | 88.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 0.5 µM 0.246× (z -9.9) ⚠ cell-cycle shift, explains ~60% of this change |
| [[SW48 (line)]] | wt | 85.8 | 0 | 2 (1 ⚠) | — | [[Amsacrine (drug)]] 5 µM 0.370× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 39.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CFPAC-1 (line)]] | alt | 59.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HT-29 (line)]] | alt | 70.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.251× (z -9.8) ⚠ cell-cycle shift, explains ~60% of this change |
| [[J82 (line)]] | alt | 95.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +12.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 99.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +14.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 114 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +15.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW480 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.420× (z -9.3) ⚠ cell-cycle shift, explains ~60% of this change |
| [[BT-474 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 104 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 81.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 120 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.5 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 82.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 94.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 77.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3968), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF4A]] | +0.91 | +0.91 / +0.89 | both halves | 7e-06 | same gene group; STRING 921 |
| [[KNL1]] | +0.90 | +0.88 / +0.88 | both halves | 7e-06 | pathway: RHO GTPase Effectors; STRING 665 |
| [[DLGAP5]] | +0.90 | +0.89 / +0.89 | both halves | 7e-06 | STRING 933 |
| [[MKI67]] | +0.89 | +0.87 / +0.88 | both halves | 7e-06 | STRING 894 |
| [[BIRC5]] | +0.89 | +0.85 / +0.89 | both halves | 7e-06 | pathway: RHO GTPase Effectors; STRING 741 |
| [[BUB1]] | +0.88 | +0.85 / +0.89 | both halves | 7e-06 | pathway: RHO GTPase Effectors; STRING 817 |
| [[TACC3]] | +0.88 | +0.88 / +0.88 | both halves | 7e-06 |  |
| [[NDC80]] | +0.88 | +0.86 / +0.88 | both halves | 7e-06 | pathway: RHO GTPase Effectors; STRING 736 |
| [[TPX2]] | +0.88 | +0.85 / +0.88 | both halves | 7e-06 | STRING 903 |
| [[GTSE1]] | +0.88 | +0.89 / +0.85 | both halves | 7e-06 | STRING 689 |
| [[CKAP2L]] | +0.88 | +0.87 / +0.87 | both halves | 7e-06 | STRING 852 |
| [[TOP2A]] | +0.88 | +0.86 / +0.87 | both halves | 7e-06 | STRING 927 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KIF14's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.2% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[IHO1]] | B | IHO1 activity lowers KIF14's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 1.06× higher at baseline in the lines without IHO1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent |
| [[PIMREG]] | B | PIMREG activity raises KIF14's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.85× lower at baseline in the lines without PIMREG | 0.050 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises KIF14's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.22× lower at baseline in the lines without NDC80 | 0.046 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[FAM72D]] | C | FAM72D activity raises KIF14's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 1.88× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises KIF14's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 2.81× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[PBK]] | C | PBK activity raises KIF14's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.31× lower at baseline in the lines without PBK | 0.094 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[TP53]] | C | TP53 activity strengthens KIF14's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 16 not recorded | the TP53-altered lines respond 0.69× as strongly (z diff +1.21); strongest at Amsacrine 5 µM: 0.79x vs 0.45x (z diff +4.2) | 0.467 over the table, 0.023 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; the reference differs; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.913). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.7, -55.9); signed map (-49.7, -43.5). **Vector** length 167, 63.8% of its response variance represented; |z| ≥ 3 in 1,481 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.72 to 60); *DREAM G2/M down* (control, mean cos +0.82 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.70 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.1 | +14.9 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | +5.9 | +5.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~73% of this change | +5.7 | +5.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.6 | +4.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.3 | +7.7 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.5 | +4.9 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +3.0 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +1.2 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | +2.7 | +2.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.6 | +2.5 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -10.7 | -14.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -9.5 | -13.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | -5.7 | -8.2 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | -5.7 | -6.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.2 | -4.8 |
|  | [[EX229 (drug)]] 5 µM |  | -4.3 | -3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.3 | -5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.8 | -4.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.8 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:200,551,497-200,620,751 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0042 |
| Gene groups (HGNC) | Kinesins |
| Reactome | 7 pathways, smallest: RHO GTPases activate CIT; RND1 GTPase cycle; RND2 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15058](https://www.uniprot.org/uniprotkb/Q15058) (Kinesin-like protein KIF14):

> Microtubule motor protein that binds to microtubules with high affinity through each tubulin heterodimer and has an ATPase activity (By similarity). Plays a role in many processes like cell division, cytokinesis and also in cell proliferation and apoptosis. During cytokinesis, targets to central spindle and midbody through its interaction with PRC1 and CIT respectively. Regulates cell growth through regulation of cell cycle progression and cytokinesis. During cell cycle progression acts through …

**Summary**, from NCBI Gene [9928](https://www.ncbi.nlm.nih.gov/gene/9928):

> This gene encodes a member of the kinesin-3 superfamily of microtubule motor proteins. These proteins are involved in numerous processes including vesicle transport, chromosome segregation, mitotic spindle formation, and cytokinesis. In human HeLa-S3 and 293T cells, this protein is localized to the cytoplasm during interphase, to the spindle poles and spindle microtubules during mitosis, and to the midbody during cytokinesis. An internal motor domain displays microtubule-dependent ATPase …

**Accessions** — [HGNC:19181](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19181) · Entrez [9928](https://www.ncbi.nlm.nih.gov/gene/9928) · UniProt [Q15058](https://www.uniprot.org/uniprotkb/Q15058) · Ensembl [ENSG00000118193](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118193)

## Data

Gene col 3968: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3968); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3968, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3968]; `tensor/DDL_lfc|DDL_z.npy` [3968]; `embed/gene_vectors.npy` [3968]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3968 or target_col == 3968). Every well: [[KIF14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
