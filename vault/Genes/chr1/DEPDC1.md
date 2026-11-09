---
symbol: "DEPDC1"
type: "gene"
col: 357
ensembl_id: "ENSG00000024526"
name: "DEP domain containing 1"
location: "1p31.3"
module: 22
arm: "+"
pooled_cpm: 41.15
n_lines_expressing: 48
n_dd_up: 35
n_dd_down: 40
n_dd_up_clean: 14
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# DEPDC1

*DEP domain containing 1* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (21 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.89× (z +17.4, q 0e+00, up in 38 of 46 measured lines) ⚠ cell-cycle shift, explains ~99% of this change. The strongest without an alert is [[Docetaxel (drug)]] 5 µM: 1.31× (z +4.3, q 6e-04, up in 20 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (22 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.454× (z -9.7, q 2e-19, down in 44 of 46 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.558× (z -7.2, q 6e-11, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASPM]] (+0.92, fdr 7e-06), [[CENPE]] (+0.91, fdr 7e-06), [[HMMR]] (+0.90, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 21 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 357.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **2.89×** | +17.4 | 0e+00 | 38/46 (RKO, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.82×** | +12.7 | 2e-34 | 37/45 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +11.0 | 6e-26 | 31/37 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **2.46×** | +10.6 | 3e-24 | 38/46 (RKO, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~98% of this change | **1.91×** | +7.9 | 3e-13 | 35/43 (HOP62, SW1417, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.88×** | +7.6 | 3e-12 | 29/46 (HS-578T, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.54×** | +7.2 | 4e-11 | 40/46 (NCI-H1792, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.89×** | +7.2 | 4e-11 | 29/42 (A-172, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **2.97×** | +7.0 | 2e-10 | 36/45 (RKO, PANC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.50×** | +5.0 | 4e-05 | 27/46 (A-172, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.49×** | +4.8 | 6e-05 | 27/45 (HOP62, H4, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.44×** | +4.4 | 6e-04 | 25/46 (NCI-H2030, HT-29, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.31×** | +4.3 | 6e-04 | 20/46 (HT-29, HEC-1-A, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.40×** | +4.1 | 0.001 | 20/46 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.39×** | +4.0 | 0.002 | 26/46 (HOP62, HEC-1-A, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.004 | 22/45 (HOP62, H4, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.004 | 22/45 (HOP62, H4, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +3.7 | 0.005 | 20/46 (NCI-H2347, A549, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.006 | 21/46 (H4, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.36×** | +3.5 | 0.013 | 15/45 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.36×** | +3.5 | 0.013 | 20/46 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.022 | 18/46 (J82, SW 900, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.022 | 17/46 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.27×** | +2.9 | 0.071 | 9/46 (SW480, LOX-IMVI, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.05 µM |  | **1.28×** | +2.8 | 0.084 | 14/46 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.26×** | +2.8 | 0.085 | 8/46 (NCI-H460, PANC-1, …) | top dose only | position effect removed |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **1.38×** | +2.8 | 0.085 | 15/46 (HOP62, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 22 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 357.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.454×** | -9.7 | 2e-19 | 44/46 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.460×** | -9.6 | 3e-19 | 35/46 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.453×** | -9.2 | 6e-18 | 35/46 (SW48, PANC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.502×** | -8.5 | 3e-15 | 39/46 (NCI-H460, HCT15, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.617×** | -7.8 | 5e-13 | 29/46 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.526×** | -7.8 | 8e-13 | 35/46 (LOX-IMVI, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.558×** | -7.2 | 6e-11 | 38/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.552×** | -7.0 | 1e-10 | 38/46 (HS-578T, A549, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **0.599×** | -6.3 | 2e-08 | 35/46 (SW48, SHP-77, …) | all doses, flat |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.720×** | -5.6 | 1e-06 | 25/46 (A498, LOX-IMVI, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.629×** | -5.6 | 1e-06 | 25/45 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~73% of this change | **0.419×** | -5.6 | 1e-06 | 27/41 (Hs 766T, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **0.643×** | -5.5 | 2e-06 | 31/46 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.641×** | -5.3 | 5e-06 | 24/45 (NCI-H460, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.751×** | -5.2 | 9e-06 | 24/46 (H4, A498, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.747×** | -4.8 | 5e-05 | 29/46 (HOP62, SW480, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.508×** | -4.4 | 4e-04 | 24/46 (J82, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.713×** | -4.2 | 8e-04 | 20/46 (A-427, NCI-H23, …) | all doses, flat | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **0.532×** | -4.1 | 0.001 | 25/46 (HT-29, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.707×** | -4.0 | 0.002 | 19/46 (HEC-1-A, BT-474, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.728×** | -3.9 | 0.002 | 22/46 (SHP-77, SK-MEL-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.643×** | -3.9 | 0.002 | 23/46 (HS-578T, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.713×** | -3.9 | 0.002 | 18/46 (NCI-H1573, SNU-423, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.733×** | -3.8 | 0.002 | 22/46 (SW48, HEC-1-A, …) | rises with dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.725×** | -3.8 | 0.003 | 17/46 (LOX-IMVI, HOP62, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.743×** | -3.4 | 0.013 | 17/45 (AN3 CA, LOX-IMVI, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.815×** | -3.4 | 0.013 | 16/46 (HS-578T, NCI-H2347, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.67 per unit of S-phase module lfc, +1.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 357. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 78.0 | 0 | 9 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -12.2) ⚠ cell-cycle shift, explains ~82% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.288× (z -8.6) |
| [[PANC-1 (line)]] | alt | 52.4 | 4 (4 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +18.1) ⚠ cell-cycle shift, explains ~99% of this change | [[Bortezomib (drug)]] 0.05 µM 0.300× (z -10.4) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.392× (z -8.6) |
| [[A498 (line)]] | wt | 40.8 | 2 (2 ⚠) | 5 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.54× (z +10.1) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.225× (z -16.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.413× (z -10.0) |
| [[H4 (line)]] | wt | 61.9 | 0 | 7 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.126× (z -12.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.148× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 40.5 | 2 (2 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.52× (z +14.9) ⚠ cell-cycle shift, explains ~99% of this change | [[Selinexor (drug)]] 0.5 µM 0.124× (z -12.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.352× (z -8.8) |
| [[SW48 (line)]] | wt | 47.0 | 0 | 6 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0742× (z -14.0) |
| [[A-172 (line)]] | wt | 30.4 | 4 (4 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.83× (z +11.9) ⚠ toxic; transcription drop | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.170× (z -10.8) ⚠ cell-cycle shift, explains ~91% of this change |
| [[HEC-1-A (line)]] | alt | 59.1 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.4) ⚠ cell-cycle shift, explains ~99% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.207× (z -13.5) ⚠ cell-cycle shift, explains ~67% of this change |
| [[KATO III (line)]] | alt | 33.6 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +13.2) ⚠ cell-cycle shift, explains ~99% of this change | — |
| [[LS 180 (line)]] | wt | 36.4 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.223× (z -10.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.299× (z -8.5) |
| [[A549 (line)]] | wt | 24.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +14.6) ⚠ cell-cycle shift, explains ~99% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.225× (z -8.8) ⚠ cell-cycle shift, explains ~99% of this change |
| [[BT-474 (line)]] | alt | 23.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +9.4) ⚠ cell-cycle shift, explains ~99% of this change | [[AZD2858 (drug)]] 0.5 µM 0.0814× (z -9.5) ⚠ toxic · without an alert: [[Belinostat (drug)]] 0.5 µM 0.193× (z -8.7) |
| [[HT-29 (line)]] | alt | 38.0 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.116× (z -12.6) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[PF-06260933 (drug)]] 5 µM 0.0625× (z -8.5) |
| [[RKO (line)]] | wt | 51.8 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.72× (z +18.8) ⚠ cell-cycle shift, explains ~99% of this change | — |
| [[A-427 (line)]] | wt | 70.8 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.237× (z -14.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 54.1 | 0 | 2 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.196× (z -9.1) ⚠ cell-cycle shift, explains ~67% of this change |
| [[Hs 766T (line)]] | wt | 36.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.42× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 38.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +13.4) ⚠ cell-cycle shift, explains ~99% of this change | — |
| [[J82 (line)]] | alt | 51.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +13.3) ⚠ cell-cycle shift, explains ~99% of this change | — |
| [[NCI-H2030 (line)]] | alt | 49.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +17.4) ⚠ cell-cycle shift, explains ~99% of this change | — |
| [[RPMI-7951 (line)]] | alt | 39.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +10.4) ⚠ cell-cycle shift, explains ~99% of this change | [[Selinexor (drug)]] 5 µM 0.245× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 37.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +11.1) ⚠ cell-cycle shift, explains ~99% of this change | — |
| [[SW480 (line)]] | alt | 45.4 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.272× (z -10.2) ⚠ cell-cycle shift, explains ~66% of this change |
| [[C-33 A (line)]] | alt | 58.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +8.6) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 25.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +10.0) ⚠ cell-cycle shift, explains ~99% of this change | — |
| [[CFPAC-1 (line)]] | alt | 30.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +12.6) ⚠ cell-cycle shift, explains ~99% of this change | — |
| [[HOP62 (line)]] | alt | 34.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +14.1) ⚠ cell-cycle shift, explains ~99% of this change | — |
| [[LoVo (line)]] | wt | 31.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +10.8) ⚠ cell-cycle shift, explains ~99% of this change | — |
| [[NCI-H23 (line)]] | alt | 55.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 37.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +13.1) ⚠ cell-cycle shift, explains ~99% of this change | — |
| [[Panc 03.27 (line)]] | alt | 31.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.56× (z +16.2) ⚠ cell-cycle shift, explains ~99% of this change | — |
| [[SHP-77 (line)]] | alt | 59.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -8.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SNU-423 (line)]] | alt | 35.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +12.9) ⚠ cell-cycle shift, explains ~99% of this change | — |
| [[AN3 CA (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.24 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.82 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 94.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 357), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASPM]] | +0.92 | +0.91 / +0.92 | both halves | 7e-06 | STRING 861 |
| [[CENPE]] | +0.91 | +0.92 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 828 |
| [[HMMR]] | +0.90 | +0.87 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 907 |
| [[CENPF]] | +0.90 | +0.92 / +0.92 | both halves | 7e-06 | STRING 844 |
| [[CCNB2]] | +0.90 | +0.89 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 724 |
| [[CCNB1]] | +0.90 | +0.89 / +0.91 | both halves | 7e-06 | STRING 871 |
| [[BIRC5]] | +0.89 | +0.87 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 821 |
| [[DLGAP5]] | +0.88 | +0.86 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 881 |
| [[TPX2]] | +0.88 | +0.84 / +0.89 | both halves | 7e-06 | STRING 903 |
| [[ARHGAP11A]] | +0.87 | +0.84 / +0.89 | both halves | 7e-06 | STRING 684 |
| [[AURKA]] | +0.87 | +0.94 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 782 |
| [[PRC1]] | +0.87 | +0.84 / +0.87 | both halves | 7e-06 | STRING 557 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DEPDC1's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[NDC80]] | C | NDC80 activity raises DEPDC1's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 3.06× lower at baseline in the lines without NDC80 | 0.016 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent; co-absent with the target |
| [[AURKB]] | C | AURKB activity raises DEPDC1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 3.19× lower at baseline in the lines without AURKB | 0.026 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[FAM72D]] | C | FAM72D activity raises DEPDC1's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.48× lower at baseline in the lines without FAM72D | 0.065 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises DEPDC1's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 4.05× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[CDC20]] | C | CDC20 activity raises DEPDC1's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 3.03× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.882). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.6, -56.8); signed map (-50.8, -44.1). **Vector** length 156, 59.0% of its response variance represented; |z| ≥ 3 in 1,517 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.70 to 60); *DREAM G2/M down* (control, mean cos +0.82 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.68 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | +13.6 | +17.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | +9.4 | +10.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | +8.6 | +7.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~98% of this change | +6.9 | +7.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | +6.1 | +7.0 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.9 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +3.1 | +4.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.0 | +3.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.9 | +3.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -8.6 | -9.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | -7.4 | -9.2 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | -6.2 | -7.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.6 | -7.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~73% of this change | -5.3 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.2 | -3.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.3 | -5.6 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -4.2 | -3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.1 | -3.9 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -3.6 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | DEP domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:68,474,152-68,497,221 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DEP.8, FLJ20354, SDP35, DEPDC1A |
| Gene groups (HGNC) | DEP domain containing |
| Hallmark sets | GLYCOLYSIS, E2F_TARGETS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TB30](https://www.uniprot.org/uniprotkb/Q5TB30) (DEP domain-containing protein 1A):

> May be involved in transcriptional regulation as a transcriptional corepressor. The DEPDC1A-ZNF224 complex may play a critical role in bladder carcinogenesis by repressing the transcription of the A20 gene, leading to transport of NF-KB protein into the nucleus, resulting in suppression of apoptosis of bladder cancer cells.

**Summary**, from NCBI Gene [55635](https://www.ncbi.nlm.nih.gov/gene/55635):

> Predicted to enable GTPase activator activity. Involved in negative regulation of DNA-templated transcription. Located in fibrillar center and nucleoplasm. Part of transcription repressor complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:22949](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22949) · Entrez [55635](https://www.ncbi.nlm.nih.gov/gene/55635) · UniProt [Q5TB30](https://www.uniprot.org/uniprotkb/Q5TB30) · Ensembl [ENSG00000024526](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000024526)

## Data

Gene col 357: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 357); `tables/drug_effects.parquet` (76 rows, flagged included); `relations/gene_relations.parquet` (col_a == 357, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 357]; `tensor/DDL_lfc|DDL_z.npy` [357]; `embed/gene_vectors.npy` [357]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 357 or target_col == 357). Every well: [[DEPDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DEPDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
