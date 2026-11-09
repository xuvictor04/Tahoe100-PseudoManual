---
symbol: "PDS5B"
type: "gene"
col: 1376
ensembl_id: "ENSG00000083642"
name: "PDS5 cohesin associated factor B"
location: "13q13.1"
module: 146
arm: "+"
pooled_cpm: 173.88
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# PDS5B

*PDS5 cohesin associated factor B* — 13q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.05× (z +13.7, q 7e-40, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.420× (z -15.9, q 0e+00, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.503× (z -13.1, q 3e-37, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAA16]] (+0.68, fdr 7e-06), [[HSF2]] (+0.64, fdr 7e-06), [[RSBN1L]] (+0.63, fdr 1e-05); moves opposite to [[ATP6V1D]] (-0.57, fdr 1e-05), [[PLEKHM1]] (-0.54, fdr 2e-05), [[PLXNA3]] (-0.54, fdr 5e-05).
> It sits in the **+** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LRRC34]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1376.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.05×** | +13.7 | 7e-40 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.15×** | +11.5 | 4e-28 | 45/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +11.5 | 4e-28 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +11.1 | 2e-26 | 43/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.41×** | +8.8 | 2e-16 | 43/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +7.6 | 2e-12 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +7.6 | 3e-12 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +5.7 | 9e-07 | 33/48 (RPMI-7951, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.28×** | +4.8 | 1e-04 | 29/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +4.5 | 4e-04 | 28/48 (RKO, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.27×** | +4.5 | 4e-04 | 27/48 (A-427, RKO, …) | top dose only | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.3 | 8e-04 | 31/45 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.003 | 28/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.21×** | +3.7 | 0.010 | 22/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.20×** | +3.5 | 0.017 | 23/48 (NCI-H23, AsPC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.045 | 22/49 (RKO, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.048 | 24/48 (NCI-H2030, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.19× | +3.2 | 0.048 | 20/49 (A-427, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1376.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.420×** | -15.9 | 0e+00 | 39/44 (J82, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.464×** | -14.7 | 0e+00 | 43/49 (Panc 03.27, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.503×** | -13.1 | 3e-37 | 47/48 (SW480, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.593×** | -10.0 | 2e-21 | 43/48 (SW480, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.665×** | -7.2 | 7e-11 | 28/45 (A-427, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.708×** | -6.6 | 4e-09 | 38/48 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.779×** | -4.6 | 4e-04 | 29/47 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.661×** | -4.1 | 0.002 | 26/47 (SW480, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.865× | -3.9 | 0.005 | 20/48 (A-172, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.866× | -3.9 | 0.006 | 21/49 (SHP-77, J82, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.818×** | -3.9 | 0.006 | 27/49 (NCI-H2347, KATO III, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.870× | -3.8 | 0.008 | 18/48 (BT-474, NCI-H2347, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.837× | -3.4 | 0.028 | 22/48 (A-172, KATO III, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.784×** | -3.3 | 0.035 | 22/48 (NCI-H23, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.719×** | -3.3 | 0.037 | 21/45 (HepG2/C3A, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.845× | -3.2 | 0.043 | 18/48 (HEC-1-A, RPMI-7951, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 5 µM |  | **0.737×** | -3.0 | 0.077 | 19/48 (MIA PaCa-2, Panc 03.27, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1376. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 237 | 8 (3 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +18.9) | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -18.2) |
| [[PANC-1 (line)]] | alt | 141 | 9 (4 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.47× (z +21.2) | [[Dinaciclib (drug)]] 5 µM 0.469× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.575× (z -9.4) |
| [[J82 (line)]] | alt | 405 | 4 (2 ⚠) | 6 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.293× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.473× (z -11.4) |
| [[LS 180 (line)]] | wt | 200 | 7 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.57× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -14.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 287 | 3 (2 ⚠) | 6 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.51× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.299× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.400× (z -11.7) |
| [[NCI-H460 (line)]] | wt | 123 | 6 (3 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 2.01× (z +11.1) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.88× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.371× (z -15.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 190 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.382× (z -12.6) |
| [[HT-29 (line)]] | alt | 321 | 4 (2 ⚠) | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.56× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.421× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.451× (z -11.0) |
| [[COLO 205 (line)]] | alt | 275 | 5 (2 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 5.37× (z +19.6) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 11.4× (z +15.5) | [[Dinaciclib (drug)]] 0.5 µM 0.464× (z -9.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 263 | 2 | 4 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.39× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.299× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.406× (z -11.1) |
| [[KATO III (line)]] | alt | 182 | 4 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.67× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.495× (z -9.6) |
| [[LoVo (line)]] | wt | 138 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.80× (z +18.0) | [[Dinaciclib (drug)]] 0.5 µM 0.471× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 159 | 4 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -12.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 227 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +16.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.81× (z +9.9) | — |
| [[A-427 (line)]] | wt | 133 | 2 (1 ⚠) | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.05× (z +9.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.44× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.325× (z -13.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 166 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.386× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 247 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.30× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -13.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 165 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.57× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -14.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 120 | 2 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.01× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.458× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 165 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.05× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.396× (z -9.4) |
| [[C-33 A (line)]] | alt | 243 | 1 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.401× (z -10.1) |
| [[C32 (line)]] | wt | 142 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.42× (z +10.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.428× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 93.6 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.86× (z +11.5) | — |
| [[HepG2_C3A (line)]] | wt | 198 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.93× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.334× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 91.7 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -13.3) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 234 | 1 (1 ⚠) | 3 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.06× (z +8.5) ⚠ toxic | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.464× (z -9.5) |
| [[SW1417 (line)]] | alt | 221 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.413× (z -9.7) |
| [[BT-474 (line)]] | alt | 168 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.90× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -11.5) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.464× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 141 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.332× (z -11.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 161 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -8.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 87.9 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.34× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.348× (z -11.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 89.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.463× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 299 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -10.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 135 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.61× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 92.1 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.59× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 260 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -13.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 187 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.348× (z -10.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 146 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.494× (z -8.7) |
| [[SW 900 (line)]] | alt | 144 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.427× (z -8.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 197 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 318 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 219 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1376), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA16]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 | same gene group |
| [[HSF2]] | +0.64 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[RSBN1L]] | +0.63 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[NFIA]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[PPP4R1]] | +0.61 | +0.69 / +0.50 | both halves | 1e-05 | same gene group |
| [[PPP2R5E]] | +0.61 | +0.72 / +0.53 | both halves | 1e-05 | same gene group; pathway: Mitotic Anaphase |
| [[ZNF618]] | +0.61 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[HAUS1]] | +0.61 | +0.66 / +0.58 | both halves | 8e-06 | pathway: Mitotic Prometaphase |
| [[CNOT6L]] | +0.60 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[CEP78]] | +0.60 | +0.57 / +0.58 | both halves | 8e-06 | pathway: Mitotic Prometaphase |
| [[PDE7A]] | +0.60 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[KCTD3]] | +0.60 | +0.57 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1D]] | -0.57 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[PLEKHM1]] | -0.54 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[PLXNA3]] | -0.54 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[ZBTB43]] | -0.54 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[ZNF674]] | -0.52 | -0.63 / -0.40 | both halves | 5e-05 |  |
| [[FAM83G]] | -0.52 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[MIR22HG]] | -0.51 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[STK40]] | -0.50 | -0.39 / -0.49 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC34]] | B | LRRC34 activity raises PDS5B's level | lines that do not express LRRC34 (20) vs lines expressing it (30) | 1.28× lower at baseline in the lines without LRRC34 | 0.034 | ⚠ within organs, on part of the lines; also absent: PLTP, SLC45A1, GNA15; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.707). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-8.5, -7.1); signed map (-28.9, -16.4). **Vector** length 112, 43.2% of its response variance represented; |z| ≥ 3 in 1,317 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.4 | +11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.7 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.6 | -0.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | -1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +4.0 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.7 | +2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | -0.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.1 | -2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.6 | +0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.5 | -2.8 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -1.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.6 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | +1.1 |
|  | [[Posaconazole (drug)]] 5 µM |  | -2.5 | -1.8 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | PDS5 cohesin associated factor B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q13.1 — chr13:32,586,452-32,778,019 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AS3, KIAA0979, FLJ23236, CG008; previously APRIN |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 12 pathways, smallest: Cohesin Loading onto Chromatin; Establishment of Sister Chromatid Cohesion; Mitotic Telophase/Cytokinesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NTI5](https://www.uniprot.org/uniprotkb/Q9NTI5) (Sister chromatid cohesion protein PDS5 homolog B):

> Regulator of sister chromatid cohesion in mitosis which may stabilize cohesin complex association with chromatin. May couple sister chromatid cohesion during mitosis to DNA replication. Cohesion ensures that chromosome partitioning is accurate in both meiotic and mitotic cells and plays an important role in DNA repair. Plays a role in androgen-induced proliferative arrest in prostate cells.

**Summary**, from NCBI Gene [23047](https://www.ncbi.nlm.nih.gov/gene/23047):

> This gene encodes a protein that interacts with the conserved protein complex termed cohesin. The cohesin complex holds together sister chromatids and facilitates accurate chromosome segregation during mitosis and meiosis. This protein is also a negative regulator of cell proliferation and may be a tumor-suppressor gene. [provided by RefSeq, Jul 2015]

**Accessions** — [HGNC:20418](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20418) · Entrez [23047](https://www.ncbi.nlm.nih.gov/gene/23047) · UniProt [Q9NTI5](https://www.uniprot.org/uniprotkb/Q9NTI5) · Ensembl [ENSG00000083642](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083642)

## Data

Gene col 1376: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1376); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1376, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1376]; `tensor/DDL_lfc|DDL_z.npy` [1376]; `embed/gene_vectors.npy` [1376]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1376 or target_col == 1376). Every well: [[PDS5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDS5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
