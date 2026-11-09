---
symbol: "TRIB3"
type: "gene"
col: 2105
ensembl_id: "ENSG00000101255"
name: "tribbles pseudokinase 3"
location: "20p13"
module: 63
arm: "+"
pooled_cpm: 33.22
n_lines_expressing: 47
n_dd_up: 49
n_dd_down: 43
n_dd_up_clean: 41
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 2
direction_downstream: 6
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# TRIB3

*tribbles pseudokinase 3* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 49 drug-doses (8 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 2.41× (z +16.8, q 0e+00, up in 42 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.197× (z -30.9, q 0e+00, down in 40 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GARS1]] (+0.86, fdr 7e-06), [[SARS1]] (+0.85, fdr 7e-06), [[SESN2]] (+0.84, fdr 7e-06).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → cells under [[NG25 (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 49 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2105.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **2.41×** | +16.8 | 0e+00 | 42/45 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.47×** | +12.6 | 4e-34 | 44/44 (SHP-77, A-172, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **2.38×** | +12.2 | 1e-31 | 42/44 (LoVo, SW480, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **2.33×** | +11.9 | 3e-30 | 39/44 (SW480, Panc 03.27, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.40×** | +11.8 | 5e-30 | 34/42 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **2.31×** | +11.7 | 8e-30 | 41/45 (SW480, HEC-1-A, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.26×** | +11.4 | 2e-28 | 40/45 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.99×** | +10.1 | 3e-22 | 34/45 (NCI-H460, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **2.03×** | +9.9 | 2e-21 | 39/44 (SHP-77, NCI-H460, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.90×** | +9.0 | 2e-17 | 33/44 (NCI-H460, SHP-77, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.57×** | +8.8 | 8e-17 | 38/45 (LoVo, NCI-H460, …) | two highest doses |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.56×** | +8.5 | 1e-15 | 28/46 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.89×** | +7.8 | 4e-13 | 39/45 (NCI-H460, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | **1.73×** | +7.6 | 9e-13 | 33/44 (NCI-H460, SHP-77, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.67×** | +7.2 | 3e-11 | 31/44 (SHP-77, RKO, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.63×** | +6.8 | 3e-10 | 27/45 (SW480, Hs 766T, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.40×** | +6.5 | 3e-09 | 24/45 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2105.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.197×** | -30.9 | 0e+00 | 40/44 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.195×** | -22.1 | 0e+00 | 41/44 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.302×** | -16.8 | 0e+00 | 38/45 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.315×** | -16.2 | 0e+00 | 39/45 (HT-29, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.354×** | -14.6 | 0e+00 | 33/44 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.471×** | -14.4 | 6e-45 | 32/45 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.372×** | -13.9 | 6e-42 | 40/45 (HT-29, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.393×** | -13.1 | 2e-37 | 34/44 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.406×** | -12.7 | 6e-35 | 40/45 (HT-29, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.408×** | -12.6 | 2e-34 | 33/44 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.427×** | -11.9 | 4e-31 | 32/45 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.449×** | -11.2 | 1e-27 | 30/43 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.462×** | -10.4 | 1e-23 | 35/42 (A-427, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.490×** | -10.0 | 6e-22 | 36/45 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.485×** | -9.8 | 6e-21 | 24/32 (HT-29, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.639×** | -8.7 | 8e-17 | 27/45 (HepG2/C3A, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.584×** | -7.6 | 1e-12 | 29/45 (PANC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.630×** | -6.5 | 2e-09 | 27/43 (SW1417, RKO, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.738×** | -5.9 | 1e-07 | 24/45 (HT-29, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.463×** | -5.6 | 4e-07 | 24/44 (HT-29, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.668×** | -5.2 | 4e-06 | 22/43 (PANC-1, LoVo, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.57 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2105. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 101 | 1 | 21 (10 ⚠) | [[Artesunate (drug)]] 5 µM 2.10× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.0478× (z -40.1) |
| [[PANC-1 (line)]] | alt | 47.0 | 1 | 21 (10 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.89× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.0572× (z -41.1) |
| [[LoVo (line)]] | wt | 57.5 | 2 | 18 (9 ⚠) | [[Neratinib (maleate) (drug)]] 0.5 µM 2.46× (z +8.9) | [[Harringtonine (drug)]] 5 µM 0.0377× (z -31.4) |
| [[SW480 (line)]] | alt | 39.1 | 6 (1 ⚠) | 13 (5 ⚠) | [[Artesunate (drug)]] 5 µM 3.65× (z +16.1) | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -27.0) |
| [[H4 (line)]] | wt | 51.2 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0367× (z -17.0) |
| [[NCI-H460 (line)]] | wt | 32.1 | 4 (1 ⚠) | 11 (5 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 3.34× (z +14.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -13.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -12.8) |
| [[KATO III (line)]] | alt | 56.2 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0549× (z -31.2) |
| [[NCI-H2347 (line)]] | alt | 39.2 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -18.6) |
| [[LS 180 (line)]] | wt | 77.2 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -15.4) |
| [[MIA PaCa-2 (line)]] | alt | 46.2 | 2 | 10 (5 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 4.91× (z +12.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0362× (z -18.1) ⚠ toxic; cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0599× (z -15.3) |
| [[SW48 (line)]] | wt | 54.5 | 1 | 9 (2 ⚠) | [[Artesunate (drug)]] 5 µM 3.35× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.0951× (z -17.2) |
| [[CFPAC-1 (line)]] | alt | 60.2 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0751× (z -30.2) |
| [[SNU-423 (line)]] | alt | 36.6 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -21.2) |
| [[SW1417 (line)]] | alt | 27.2 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -16.8) |
| [[A498 (line)]] | wt | 32.4 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -13.1) |
| [[A549 (line)]] | wt | 31.5 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -21.0) |
| [[HS-578T (line)]] | alt | 36.0 | 0 | 8 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0978× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -13.4) |
| [[COLO 205 (line)]] | alt | 41.9 | 1 | 6 (2 ⚠) | [[Artesunate (drug)]] 5 µM 3.23× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -16.2) |
| [[RKO (line)]] | wt | 32.1 | 2 | 5 (3 ⚠) | [[Artesunate (drug)]] 5 µM 4.08× (z +10.3) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0792× (z -13.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 28.3 | 2 | 4 (2 ⚠) | [[Artesunate (drug)]] 5 µM 3.28× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -13.2) |
| [[A-427 (line)]] | wt | 21.7 | 0 | 5 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0676× (z -15.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.117× (z -12.7) |
| [[HCT15 (line)]] | alt | 56.7 | 1 | 4 (1 ⚠) | [[Artesunate (drug)]] 5 µM 3.75× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.0989× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.232× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 18.1 | 1 (1 ⚠) | 3 | [[Niclosamide (olamine) (drug)]] 5 µM 5.56× (z +9.9) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -13.8) |
| [[BT-474 (line)]] | alt | 34.5 | 1 | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.77× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.0835× (z -18.9) |
| [[HepG2_C3A (line)]] | wt | 56.4 | 1 (1 ⚠) | 3 | [[Niclosamide (olamine) (drug)]] 5 µM 5.77× (z +10.1) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -15.4) |
| [[HOP62 (line)]] | alt | 33.9 | 1 | 3 | [[Artesunate (drug)]] 5 µM 3.26× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -15.2) |
| [[A-172 (line)]] | wt | 16.6 | 1 | 2 | [[Auranofin (drug)]] 5 µM 6.16× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -13.9) |
| [[NCI-H1792 (line)]] | alt | 20.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -9.9) |
| [[SHP-77 (line)]] | alt | 15.5 | 3 | 0 | [[Auranofin (drug)]] 5 µM 9.55× (z +11.4) | — |
| [[SW 900 (line)]] | alt | 21.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.140× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.155× (z -9.1) |
| [[J82 (line)]] | alt | 14.3 | 1 | 1 | [[Artesunate (drug)]] 5 µM 3.23× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 16.7 | 1 | 1 | [[5-Azacytidine (drug)]] 5 µM 4.21× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -14.6) |
| [[Panc 03.27 (line)]] | alt | 10.5 | 1 | 1 | [[5-Azacytidine (drug)]] 5 µM 7.49× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 46.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -16.0) |
| [[LOX-IMVI (line)]] | wt | 8.45 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.27× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 11.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.176× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 9.86 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0809× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[AN3 CA (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.93 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.59 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.89 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2105), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GARS1]] | +0.86 | +0.83 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[SARS1]] | +0.85 | +0.83 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[SESN2]] | +0.84 | +0.81 / +0.82 | both halves | 7e-06 | pathway: Cellular response to starvation; STRING 564 |
| [[XPOT]] | +0.82 | +0.83 / +0.81 | both halves | 7e-06 |  |
| [[AARS1]] | +0.81 | +0.79 / +0.80 | both halves | 7e-06 |  |
| [[GOT1]] | +0.81 | +0.73 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[CHAC1]] | +0.80 | +0.68 / +0.83 | both halves | 7e-06 | pathway: Response of EIF2AK1 (HRI) to heme deficiency; STRING 966 |
| [[CARS1]] | +0.79 | +0.73 / +0.80 | both halves | 7e-06 | STRING 429 |
| [[ADM2]] | +0.78 | +0.62 / +0.81 | both halves | 7e-06 | STRING 466 |
| [[EIF2S2]] | +0.78 | +0.70 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[MARS1]] | +0.78 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[IARS1]] | +0.78 | +0.78 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TRIB3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01564]] | B | LINC01564 activity raises TRIB3's level | lines that do not express LINC01564 (24) vs lines expressing it (26) | 2.03× lower at baseline in the lines without LINC01564 | 0.097 | ⚠ within organs, on part of the lines; also absent: LINC03040, INAVA, CYP4F11; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[NG25 (drug)]] 5 µM | C | TRIB3 activity raises the cells' numbers under NG25 5 µM (protects the cells) | lines that do not express TRIB3 (3) vs lines expressing it (45) | the lines without TRIB3: 0.40× the cells of the other lines | 0.009 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ARHGAP27, KIAA1522, ALOXE3; maybe low, not absent |
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.05 µM | C | TRIB3 activity raises the cells' numbers under Idarubicin (hydrochloride) 0.05 µM (protects the cells) | lines that do not express TRIB3 (3) vs lines expressing it (45) | the lines without TRIB3: 0.65× the cells of the other lines | 0.025 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ARHGAP27, KIAA1522, ALOXE3; maybe low, not absent |
| cells under [[SBI-0640756 (drug)]] 5 µM | C | TRIB3 activity lowers the cells' numbers under SBI-0640756 5 µM (makes them more sensitive) | lines that do not express TRIB3 (3) vs lines expressing it (45) | the lines without TRIB3: 1.46× the cells of the other lines | 0.059 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ARHGAP27, KIAA1522, ALOXE3; maybe low, not absent |
| [[MARS1]] | C | TRIB3's natural level weakens MARS1's drug response | TRIB3's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.65, reverse +0.24; direction not clear | 0.061 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[AZD-7648 (drug)]] 5 µM | C | TRIB3 activity raises the cells' numbers under AZD-7648 5 µM (protects the cells) | lines that do not express TRIB3 (3) vs lines expressing it (45) | the lines without TRIB3: 0.62× the cells of the other lines | 0.073 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ARHGAP27, KIAA1522, ALOXE3; maybe low, not absent |
| cells under [[Binimetinib (drug)]] 0.5 µM | C | TRIB3 activity raises the cells' numbers under Binimetinib 0.5 µM (protects the cells) | lines that do not express TRIB3 (3) vs lines expressing it (45) | the lines without TRIB3: 0.70× the cells of the other lines | 0.073 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ARHGAP27, KIAA1522, ALOXE3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.897). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.1, 48.5); signed map (-12.8, 24.8). **Vector** length 145, 52.6% of its response variance represented; |z| ≥ 3 in 1,848 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.77 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.77 to 9); *unfolded protein response* (hallmark, mean cos +0.71 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +12.7 | +12.6 |
|  | [[Artesunate (drug)]] 5 µM |  | +10.5 | +16.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.8 | +11.4 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +9.7 | +12.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +9.2 | +8.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +8.9 | +11.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +7.9 | +9.9 |
|  | [[Neratinib (drug)]] 5 µM |  | +7.2 | +7.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -8.8 | -16.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -8.3 | -11.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -7.7 | -12.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -7.6 | -11.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.9 | -22.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.8 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.3 | -7.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.9 | -2.2 |
|  | [[Methotrexate (drug)]] 5 µM |  | -2.8 | -2.0 |
|  | [[Arbutin (drug)]] 0.05 µM |  | -2.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | tribbles pseudokinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:362,835-397,559 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1103G7.3, TRB3, SINK; previously C20orf97 |
| Gene groups (HGNC) | Pseudokinases; Tribbles pseudokinase family |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, PI3K_AKT_MTOR_SIGNALING, P53_PATHWAY, MTORC1_SIGNALING |
| Reactome | 27 pathways, smallest: Activation of AKT2; Response of EIF2AK1 (HRI) to heme deficiency; CD28 dependent PI3K/Akt signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RU7](https://www.uniprot.org/uniprotkb/Q96RU7) (Tribbles homolog 3):

> Inactive protein kinase which acts as a regulator of the integrated stress response (ISR), a process for adaptation to various stress. Inhibits the transcriptional activity of DDIT3/CHOP and is involved in DDIT3/CHOP-dependent cell death during ER stress. May play a role in programmed neuronal cell death but does not appear to affect non-neuronal cells. Acts as a negative feedback regulator of the ATF4-dependent transcription during the ISR: while TRIB3 expression is promoted by ATF4, TRIB3 …

**Summary**, from NCBI Gene [57761](https://www.ncbi.nlm.nih.gov/gene/57761):

> The protein encoded by this gene is a putative protein kinase that is induced by the transcription factor NF-kappaB. The encoded protein is a negative regulator of NF-kappaB and can also sensitize cells to TNF- and TRAIL-induced apoptosis. In addition, this protein can negatively regulate the cell survival serine-threonine kinase AKT1. Differential promoter usage and alternate splicing result in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:16228](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16228) · Entrez [57761](https://www.ncbi.nlm.nih.gov/gene/57761) · UniProt [Q96RU7](https://www.uniprot.org/uniprotkb/Q96RU7) · Ensembl [ENSG00000101255](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101255)

## Data

Gene col 2105: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2105); `tables/drug_effects.parquet` (99 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2105, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2105]; `tensor/DDL_lfc|DDL_z.npy` [2105]; `embed/gene_vectors.npy` [2105]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2105 or target_col == 2105). Every well: [[TRIB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
