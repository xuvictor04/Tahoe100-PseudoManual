---
symbol: "POLQ"
type: "gene"
col: 577
ensembl_id: "ENSG00000051341"
name: "DNA polymerase theta"
location: "3q13.33"
module: 6
arm: "+"
pooled_cpm: 63.55
n_lines_expressing: 48
n_dd_up: 21
n_dd_down: 29
n_dd_up_clean: 6
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 18
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# POLQ

*DNA polymerase theta* — 3q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.98× (z +10.4, q 1e-22, up in 39 of 46 measured lines) ⚠ cell-cycle shift, explains ~94% of this change. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 0.5 µM: 1.35× (z +4.5, q 5e-04, up in 23 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (11 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.620× (z -10.3, q 4e-22, down in 33 of 46 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.711× (z -5.2, q 2e-05, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MELK]] (+0.93, fdr 7e-06), [[WDHD1]] (+0.92, fdr 7e-06), [[CENPK]] (+0.92, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 577.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.98×** | +10.4 | 1e-22 | 39/46 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.79×** | +8.8 | 3e-16 | 37/46 (A549, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.64×** | +7.6 | 8e-12 | 32/46 (A549, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.47×** | +5.6 | 2e-06 | 30/46 (PANC-1, HT-29, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.41×** | +5.3 | 2e-05 | 25/46 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.25×** | +4.8 | 1e-04 | 26/46 (NCI-H2347, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +4.5 | 5e-04 | 23/46 (NCI-H23, A-427, …) | two highest doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.33×** | +4.3 | 0.001 | 23/46 (SNU-423, SW480, …) | all doses, flat |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.32×** | +4.2 | 0.002 | 20/46 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.21×** | +4.1 | 0.002 | 21/46 (SNU-423, A549, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +3.9 | 0.005 | 18/46 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.28×** | +3.7 | 0.009 | 18/46 (MIA PaCa-2, LS 180, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.57×** | +3.6 | 0.013 | 18/45 (NCI-H2347, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.28×** | +3.6 | 0.015 | 19/46 (SW480, A-427, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.26×** | +3.5 | 0.017 | 17/45 (HS-578T, A549, …) | inconsistent across doses |  |
| [[Irinotecan (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.021 | 17/46 (SW480, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Demeclocycline (drug)]] 5 µM |  | 1.15× | +3.0 | 0.073 | 6/46 (LoVo, LOX-IMVI, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.21×** | +2.9 | 0.093 | 9/46 (A498, CFPAC-1, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **1.23×** | +2.9 | 0.093 | 12/46 (LS 180, LoVo, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 577.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.620×** | -10.3 | 4e-22 | 33/46 (LS 180, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.535×** | -9.4 | 2e-18 | 40/46 (LS 180, A498, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.564×** | -6.2 | 9e-08 | 30/46 (SW480, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.690×** | -5.2 | 2e-05 | 22/42 (SW480, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.711×** | -5.2 | 2e-05 | 26/46 (A-427, NCI-H23, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.721×** | -5.0 | 5e-05 | 28/46 (LoVo, COLO 205, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.795×** | -5.0 | 6e-05 | 22/46 (HCT15, COLO 205, …) | rises with dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.540×** | -4.9 | 6e-05 | 26/45 (SW480, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.798×** | -4.9 | 7e-05 | 24/46 (A-427, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.731×** | -4.8 | 1e-04 | 23/46 (HEC-1-A, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.736×** | -4.6 | 2e-04 | 24/46 (H4, SW 900, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.736×** | -4.6 | 2e-04 | 23/45 (SHP-77, MIA PaCa-2, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.743×** | -4.4 | 4e-04 | 25/46 (HEC-1-A, COLO 205, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.815×** | -4.4 | 4e-04 | 24/46 (COLO 205, SHP-77, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.826×** | -4.1 | 0.001 | 18/46 (SNU-423, A-172, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 5 µM |  | **0.606×** | -4.0 | 0.002 | 21/46 (HT-29, H4, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.05 µM |  | **0.757×** | -4.0 | 0.002 | 18/46 (NCI-H1792, SW480, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.774×** | -3.8 | 0.005 | 21/46 (COLO 205, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **0.794×** | -3.5 | 0.013 | 14/46 (RKO, COLO 205, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.726×** | -3.5 | 0.013 | 18/46 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 0.854× | -3.4 | 0.016 | 18/46 (HT-29, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.800×** | -3.4 | 0.016 | 18/46 (A-427, H4, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.858× | -3.3 | 0.022 | 16/46 (KATO III, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.97 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 577. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 81.8 | 0 | 7 (5 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.107× (z -11.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.254× (z -10.5) |
| [[A-172 (line)]] | wt | 74.8 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.261× (z -12.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM 0.224× (z -9.6) |
| [[A-427 (line)]] | wt | 159 | 0 | 6 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.299× (z -15.2) |
| [[LS 180 (line)]] | wt | 38.9 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.106× (z -19.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.306× (z -10.3) |
| [[A498 (line)]] | wt | 60.3 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.177× (z -17.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.339× (z -10.6) |
| [[COLO 205 (line)]] | alt | 50.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0988× (z -11.8) |
| [[A549 (line)]] | wt | 45.4 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.39× (z +11.6) ⚠ cell-cycle shift, explains ~94% of this change | — |
| [[HEC-1-A (line)]] | alt | 135 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -12.0) |
| [[LoVo (line)]] | wt | 44.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +8.5) | [[Selinexor (drug)]] 5 µM 0.376× (z -10.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 23.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +11.5) | — |
| [[NCI-H23 (line)]] | alt | 108 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.389× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 45.4 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.255× (z -9.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SK-MEL-2 (line)]] | alt | 71.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 96.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.567× (z -8.7) |
| [[HCT15 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.374× (z -9.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HOP62 (line)]] | alt | 72.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.283× (z -8.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 32.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -9.4) |
| [[HS-578T (line)]] | alt | 31.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +10.5) | — |
| [[KATO III (line)]] | alt | 77.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 37.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.367× (z -9.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 74.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -11.1) |
| [[PANC-1 (line)]] | alt | 71.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.27× (z +8.5) ⚠ cell-cycle shift, explains ~94% of this change | — |
| [[RKO (line)]] | wt | 81.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 92.6 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.134× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~15% of this change |
| [[AN3 CA (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 61.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 577), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MELK]] | +0.93 | +0.90 / +0.94 | both halves | 7e-06 | STRING 499 |
| [[WDHD1]] | +0.92 | +0.89 / +0.92 | both halves | 7e-06 | STRING 479 |
| [[CENPK]] | +0.92 | +0.91 / +0.92 | both halves | 7e-06 | **novel candidate** |
| [[FANCI]] | +0.92 | +0.89 / +0.91 | both halves | 7e-06 | STRING 583 |
| [[BLM]] | +0.91 | +0.90 / +0.91 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 669 |
| [[BRIP1]] | +0.91 | +0.88 / +0.93 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 655 |
| [[SPC24]] | +0.90 | +0.88 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[EXO1]] | +0.90 | +0.88 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 805 |
| [[GINS1]] | +0.90 | +0.89 / +0.91 | both halves | 7e-06 | **novel candidate** |
| [[ATAD5]] | +0.90 | +0.90 / +0.91 | both halves | 7e-06 | STRING 401 |
| [[DTL]] | +0.90 | +0.88 / +0.90 | both halves | 7e-06 | STRING 527 |
| [[ZGRF1]] | +0.89 | +0.90 / +0.88 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 8, C 10. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises POLQ's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.85× lower at baseline in the lines without E2F8 | 0.011 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises POLQ's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 3.10× lower at baseline in the lines without TCF19 | 0.017 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[MTOR]] | B | MTOR activity raises POLQ's level | compounds that target MTOR: 5 of 8 lower it (Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 5.3% of all compounds | 0.026 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP1]] | B | TOP1 activity lowers POLQ's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CDC25A]] | B | CDC25A activity raises POLQ's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.44× lower at baseline in the lines without CDC25A | 0.047 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[FAM111B]] | B | FAM111B activity raises POLQ's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.81× lower at baseline in the lines without FAM111B | 0.051 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[ZNF724]] | B | ZNF724 activity weakens POLQ's drug response | lines that do not express ZNF724 (7) vs lines expressing it (39) | the lines without ZNF724 respond 1.28× as strongly (z diff -0.46); strongest at Belinostat 5 µM: 2.46x vs 1.65x (z diff -2.7) | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000283201, ENSG00000269237, ZNF577; target measured in part of the lines; both ways; artifact flags |
| [[TLCD3B]] | B | TLCD3B activity raises POLQ's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 2.23× lower at baseline in the lines without TLCD3B | 0.059 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises POLQ's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.87× lower at baseline in the lines without DSCC1 | 0.015 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent; co-absent with the target |
| [[AURKB]] | C | AURKB activity raises POLQ's level | lines that do not express AURKB (4) vs lines expressing it (46) | 3.44× lower at baseline in the lines without AURKB | 0.039 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[MYBL2]] | C | MYBL2 activity raises POLQ's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 3.46× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises POLQ's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.91× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.914). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.0, -46.8); signed map (-39.8, -43.8). **Vector** length 162, 58.1% of its response variance represented; |z| ≥ 3 in 1,358 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.68 to 65); *DNA strand elongation* (reactome, mean cos +0.72 to 28); *DNA Replication* (reactome, mean cos +0.72 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | +5.1 | +3.5 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +4.8 | +4.8 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | +4.5 | +4.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | +4.3 | +8.8 |
|  | [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +4.2 | +3.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.3 | +2.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +3.2 | +2.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.2 | +2.6 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | +2.7 | +2.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.6 | +2.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -9.3 | -10.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -8.2 | -9.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -7.4 | -4.4 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -5.3 | -6.2 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -5.2 | -4.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.9 | -5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -5.2 |
|  | [[palbociclib (drug)]] 5 µM |  | -4.6 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | DNA polymerase theta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.33 — chr3:121,431,431-121,545,988 (-) |
| Ensembl biotype | protein_coding |
| Also known as | POLH |
| Gene groups (HGNC) | DNA polymerases |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 4 pathways, smallest: HDR through MMEJ (alt-NHEJ); Homology Directed Repair; DNA Double-Strand Break Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [O75417](https://www.uniprot.org/uniprotkb/O75417) (DNA polymerase theta):

> Low-fidelity DNA polymerase with a putative helicase activity that promotes microhomology-mediated end-joining (MMEJ), an alternative non-homologous end-joining (NHEJ) machinery required to repair double-strand breaks in DNA during mitosis. MMEJ is an error-prone repair pathway that produces deletions of sequences from the strand being repaired and promotes genomic rearrangements, such as telomere fusions, some of them leading to cellular transformation. MMEJ is required during mitosis to …

**Summary**, from NCBI Gene [10721](https://www.ncbi.nlm.nih.gov/gene/10721):

> Enables several functions, including catalytic activity, acting on DNA; identical protein binding activity; and magnesium ion binding activity. Involved in DNA metabolic process; negative regulation of double-strand break repair via homologous recombination; and protein homooligomerization. Located in nucleoplasm. Is active in mitochondrial nucleoid; nucleus; and site of double-strand break. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9186](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9186) · Entrez [10721](https://www.ncbi.nlm.nih.gov/gene/10721) · UniProt [O75417](https://www.uniprot.org/uniprotkb/O75417) · Ensembl [ENSG00000051341](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000051341)

## Data

Gene col 577: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 577); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 577, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 577]; `tensor/DDL_lfc|DDL_z.npy` [577]; `embed/gene_vectors.npy` [577]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 577 or target_col == 577). Every well: [[POLQ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLQ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
