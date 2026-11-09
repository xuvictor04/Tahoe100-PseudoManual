---
symbol: "KIF18B"
type: "gene"
col: 11788
ensembl_id: "ENSG00000186185"
name: "kinesin family member 18B"
location: "17q21.31"
module: 67
arm: "+"
pooled_cpm: 57.99
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 49
n_dd_up_clean: 2
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# KIF18B

*kinesin family member 18B* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 1.90× (z +8.1, q 3e-13, up in 35 of 46 measured lines) ⚠ cell-cycle shift, explains ~57% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.16× (z +5.1, q 2e-05, up in 30 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 2 lines (KATO III 8.10×, CFPAC-1 5.12×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (Panc 03.27 3.13×, RKO 2.46×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 5.71×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 49 drug-doses (18 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.360× (z -17.9, q 0e+00, down in 43 of 46 measured lines) ⚠ cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.444× (z -10.2, q 3e-22, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTSE1]] (+0.92, fdr 7e-06), [[CCNF]] (+0.90, fdr 7e-06), [[AURKB]] (+0.89, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11788.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 2 lines (KATO III 8.10×, CFPAC-1 5.12×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (Panc 03.27 3.13×, RKO 2.46×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 5.71×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.90×** | +8.1 | 3e-13 | 35/46 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **1.78×** | +7.3 | 7e-11 | 35/45 (KATO III, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.51×** | +7.3 | 7e-11 | 39/46 (NCI-H23, SW 900, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.71×** | +6.8 | 2e-09 | 32/46 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.55×** | +6.2 | 7e-08 | 29/46 (CFPAC-1, J82, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.59×** | +5.9 | 4e-07 | 27/46 (KATO III, A549, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.56×** | +5.7 | 1e-06 | 30/45 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.16×** | +5.1 | 2e-05 | 30/46 (NCI-H23, HS-578T, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.01×** | +4.6 | 2e-04 | 27/45 (RKO, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.40×** | +4.3 | 0.001 | 22/46 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.39×** | +4.1 | 0.002 | 20/46 (SW 900, HT-29, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.34×** | +3.7 | 0.011 | 23/45 (HT-29, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (drug)]] 5 µM |  | 1.20× | +3.2 | 0.059 | 17/46 (HT-29, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 20 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 49 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11788.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.360×** | -17.9 | 0e+00 | 43/46 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.336×** | -13.8 | 1e-40 | 45/46 (A-427, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.444×** | -10.2 | 3e-22 | 36/46 (HEC-1-A, A-427, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.425×** | -10.2 | 4e-22 | 37/46 (A-172, LOX-IMVI, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.490×** | -9.0 | 3e-17 | 38/46 (HEC-1-A, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.509×** | -8.5 | 2e-15 | 33/46 (MIA PaCa-2, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.552×** | -7.5 | 6e-12 | 42/46 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.685×** | -6.7 | 2e-09 | 28/46 (SNU-1, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **0.378×** | -6.4 | 1e-08 | 30/41 (LS 180, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.619×** | -6.0 | 9e-08 | 30/46 (A498, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.533×** | -5.7 | 8e-07 | 28/46 (SW480, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.639×** | -5.6 | 9e-07 | 30/46 (HEC-1-A, NCI-H1573, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.629×** | -5.6 | 9e-07 | 28/46 (SW48, SNU-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.647×** | -5.5 | 2e-06 | 25/46 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.745×** | -5.2 | 6e-06 | 26/46 (H4, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.747×** | -5.1 | 1e-05 | 25/46 (SNU-1, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.666×** | -5.1 | 1e-05 | 26/46 (A-427, NCI-H460, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.773×** | -4.5 | 2e-04 | 19/46 (HCT15, RKO, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.688×** | -4.5 | 2e-04 | 24/45 (A549, A-427, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Amsacrine (drug)]] 5 µM |  | **0.774×** | -4.5 | 2e-04 | 23/46 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.776×** | -4.1 | 9e-04 | 22/46 (A-427, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[palbociclib (drug)]] 5 µM |  | **0.588×** | -3.5 | 0.009 | 19/46 (SW480, LOX-IMVI, …) | two highest doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.781×** | -3.4 | 0.010 | 19/46 (A-427, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.764×** | -3.4 | 0.012 | 16/46 (SHP-77, NCI-H1792, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +1.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11788. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 84.6 | 0 | 14 (6 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.151× (z -14.3) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.190× (z -12.7) |
| [[LOX-IMVI (line)]] | wt | 60.7 | 0 | 12 (6 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.128× (z -18.6) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.121× (z -13.6) |
| [[A-172 (line)]] | wt | 98.8 | 0 | 11 (6 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.162× (z -17.8) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -12.1) |
| [[LS 180 (line)]] | wt | 38.4 | 0 | 11 (7 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.108× (z -18.1) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.254× (z -11.3) |
| [[A-427 (line)]] | wt | 169 | 0 | 9 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.127× (z -23.4) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -11.7) |
| [[A549 (line)]] | wt | 71.6 | 0 | 9 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.196× (z -15.3) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.158× (z -12.4) |
| [[C32 (line)]] | wt | 47.4 | 0 | 9 (6 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.241× (z -12.2) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.213× (z -9.5) |
| [[SNU-1 (line)]] | wt | 73.2 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0681× (z -18.3) |
| [[SW48 (line)]] | wt | 78.4 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -13.0) |
| [[NCI-H460 (line)]] | wt | 62.4 | 0 | 7 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.210× (z -15.2) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.397× (z -9.1) |
| [[A498 (line)]] | wt | 64.0 | 0 | 6 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.253× (z -13.7) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -13.1) |
| [[HOP62 (line)]] | alt | 109 | 0 | 6 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.259× (z -13.9) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.260× (z -10.0) |
| [[KATO III (line)]] | alt | 40.8 | 4 (4 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 8.10× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.173× (z -11.1) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SK-MEL-2 (line)]] | alt | 83.3 | 0 | 5 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.213× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 127 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.223× (z -13.2) |
| [[RKO (line)]] | wt | 70.4 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.2) | [[Selinexor (drug)]] 0.5 µM 0.155× (z -13.4) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.251× (z -9.9) |
| [[SW480 (line)]] | alt | 65.8 | 1 (1 ⚠) | 3 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.60× (z +8.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.250× (z -13.0) |
| [[HCT15 (line)]] | alt | 88.7 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.176× (z -10.5) ⚠ cell-cycle shift, explains ~56% of this change |
| [[HT-29 (line)]] | alt | 38.2 | 0 | 3 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.190× (z -10.0) ⚠ cell-cycle shift, explains ~45% of this change |
| [[LoVo (line)]] | wt | 40.8 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.194× (z -16.6) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.394× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 84.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0462× (z -17.7) |
| [[NCI-H23 (line)]] | alt | 102 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.276× (z -14.8) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.281× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 36.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +9.8) | [[Selinexor (drug)]] 5 µM 0.347× (z -8.9) ⚠ cell-cycle shift, explains ~52% of this change |
| [[PANC-1 (line)]] | alt | 38.7 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.438× (z -9.3) ⚠ cell-cycle shift, explains ~52% of this change |
| [[AN3 CA (line)]] | alt | 86.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 20.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.12× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | — |
| [[Hs 766T (line)]] | wt | 26.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.154× (z -9.4) ⚠ cell-cycle shift, explains ~56% of this change |
| [[HS-578T (line)]] | alt | 35.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.312× (z -9.0) ⚠ cell-cycle shift, explains ~52% of this change |
| [[hTERT-HPNE (line)]] | wt | 33.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.224× (z -9.1) ⚠ cell-cycle shift, explains ~52% of this change |
| [[J82 (line)]] | alt | 69.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.436× (z -10.9) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H1573 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.223× (z -11.4) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H2030 (line)]] | alt | 47.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.277× (z -11.1) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H2347 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.365× (z -9.4) ⚠ cell-cycle shift, explains ~52% of this change |
| [[SHP-77 (line)]] | alt | 77.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.266× (z -9.5) |
| [[SW 1271 (line)]] | alt | 81.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0281× (z -11.2) |
| [[SW1417 (line)]] | alt | 43.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.337× (z -10.9) ⚠ cell-cycle shift, explains ~52% of this change |
| [[AsPC-1 (line)]] | alt | 9.55 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.3 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11788), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTSE1]] | +0.92 | +0.89 / +0.93 | both halves | 7e-06 | STRING 625 |
| [[CCNF]] | +0.90 | +0.90 / +0.91 | both halves | 7e-06 | same gene group; STRING 624 |
| [[AURKB]] | +0.89 | +0.89 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 752 |
| [[CDCA8]] | +0.89 | +0.88 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 838 |
| [[TACC3]] | +0.89 | +0.91 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 470 |
| [[KIF2C]] | +0.89 | +0.87 / +0.90 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 983 |
| [[DEPDC1B]] | +0.88 | +0.86 / +0.86 | both halves | 7e-06 | STRING 413 |
| [[KIF23]] | +0.87 | +0.84 / +0.88 | both halves | 7e-06 | same gene group; pathway: COPI-dependent Golgi-to-ER retrograde traffic; STRING 859 |
| [[BUB1B]] | +0.87 | +0.90 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 838 |
| [[KIFC1]] | +0.87 | +0.88 / +0.84 | both halves | 7e-06 | same gene group; pathway: COPI-dependent Golgi-to-ER retrograde traffic; STRING 882 |
| [[HJURP]] | +0.87 | +0.83 / +0.88 | both halves | 7e-06 | STRING 864 |
| [[NDC80]] | +0.87 | +0.84 / +0.88 | both halves | 7e-06 | STRING 584 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KIF18B's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.6% of all compounds | 0.011 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PIMREG]] | B | PIMREG activity raises KIF18B's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.57× lower at baseline in the lines without PIMREG | 0.016 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises KIF18B's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.24× lower at baseline in the lines without NEURL1B | 0.080 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[ANKRD20A4P]] | B | ANKRD20A4P activity raises KIF18B's level | lines that do not express ANKRD20A4P (24) vs lines expressing it (26) | 1.35× lower at baseline in the lines without ANKRD20A4P | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000253503, ENSG00000253500, ADGRF5 |
| [[NDC80]] | C | NDC80 activity raises KIF18B's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 3.60× lower at baseline in the lines without NDC80 | 0.008 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent; co-absent with the target |
| [[PBK]] | C | PBK activity raises KIF18B's level | lines that do not express PBK (4) vs lines expressing it (46) | 3.25× lower at baseline in the lines without PBK | 0.029 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |
| [[AURKB]] | C | AURKB activity raises KIF18B's level | lines that do not express AURKB (4) vs lines expressing it (46) | 3.16× lower at baseline in the lines without AURKB | 0.034 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[C21orf58]], [[SKA3]] | C | C21orf58, SKA3 activity raises KIF18B's level | lines that do not express C21orf58, SKA3 (3) vs lines expressing them (47) | 3.64× lower at baseline in the lines without C21orf58, SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[CDC20]] | C | CDC20 activity raises KIF18B's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.98× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[FAM72D]] | C | FAM72D activity raises KIF18B's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 3.27× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[CDCA3]] | C | CDCA3 activity raises KIF18B's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 3.77× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.863). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-35.8, -55.5); signed map (-49.0, -41.6). **Vector** length 173, 66.4% of its response variance represented; |z| ≥ 3 in 1,590 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.75 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.71 to 8); *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.74 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +7.8 | +8.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | +7.7 | +5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | +7.0 | +7.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +6.3 | +5.9 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +6.1 | +7.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.7 | +5.1 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +3.8 | +4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +1.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.1 | +1.5 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | +2.9 | +2.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -12.6 | -17.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -11.2 | -13.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | -9.0 | -10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.4 | -10.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -7.9 | -9.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.6 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.9 | -5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -5.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.6 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 18B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:44,924,709-44,947,773 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Kinesins; MicroRNA protein coding host genes |
| Hallmark sets | E2F_TARGETS |
| Reactome | 8 pathways, smallest: Kinesins; COPI-dependent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86Y91](https://www.uniprot.org/uniprotkb/Q86Y91) (Kinesin-like protein KIF18B):

> In complex with KIF2C, constitutes the major microtubule plus-end depolymerizing activity in mitotic cells. Its major role may be to transport KIF2C and/or MAPRE1 along microtubules.

**Summary**, from NCBI Gene [146909](https://www.ncbi.nlm.nih.gov/gene/146909):

> Enables cytoskeletal motor activity and kinesin binding activity. Involved in microtubule depolymerization; mitotic cell cycle; and regulation of cell division. Located in cytosol; microtubule; and nuclear lumen. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27102](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27102) · Entrez [146909](https://www.ncbi.nlm.nih.gov/gene/146909) · UniProt [Q86Y91](https://www.uniprot.org/uniprotkb/Q86Y91) · Ensembl [ENSG00000186185](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186185)

## Data

Gene col 11788: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11788); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11788, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11788]; `tensor/DDL_lfc|DDL_z.npy` [11788]; `embed/gene_vectors.npy` [11788]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11788 or target_col == 11788). Every well: [[KIF18B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF18B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
