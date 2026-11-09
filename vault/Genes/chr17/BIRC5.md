---
symbol: "BIRC5"
type: "gene"
col: 1594
ensembl_id: "ENSG00000089685"
name: "baculoviral IAP repeat containing 5"
location: "17q25.3"
module: 22
arm: "+"
pooled_cpm: 39.36
n_lines_expressing: 49
n_dd_up: 29
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# BIRC5

*baculoviral IAP repeat containing 5* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (19 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.18× (z +17.8, q 0e+00, up in 43 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Docetaxel (drug)]] 5 µM: 1.34× (z +4.1, q 0.002, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.460× (z -7.6, q 2e-11, down in 41 of 47 measured lines) ⚠ cell-cycle shift, explains ~94% of this change. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.775× (z -3.5, q 0.023, down in 22 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 4 lines (A498 0.137×, LS 180 0.105×, A-427 0.234×, A-172 0.266×; ⚠ cell-cycle shift, would explain all of this change); [[Amsacrine (drug)]] 5 µM in 4 lines (A498 0.347×, H4 0.242×, SW48 0.275×, LS 180 0.255×); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 3 lines (H4 0.0527×, SW48 0.0725×, A498 0.221×; ⚠ cell-cycle shift, would explain all of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (H4 0.265×, A498 0.459×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (RPMI-7951 0.107×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPX2]] (+0.96, fdr 7e-06), [[PRC1]] (+0.94, fdr 7e-06), [[BUB1]] (+0.93, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[MYBL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 19 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1594.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **6.18×** | +17.8 | 0e+00 | 43/43 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **5.79×** | +16.5 | 0e+00 | 39/39 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **4.03×** | +12.6 | 4e-34 | 40/41 (HOP62, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~80% of this change | **2.18×** | +7.6 | 3e-12 | 39/45 (SW1417, NCI-H2030, …) | all doses, flat | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.65×** | +6.9 | 5e-10 | 42/47 (Panc 03.27, HEC-1-A, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.60×** | +6.5 | 7e-09 | 32/47 (NCI-H2030, RKO, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.71×** | +5.2 | 1e-05 | 37/46 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.70×** | +5.2 | 2e-05 | 32/47 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.62×** | +4.5 | 4e-04 | 28/47 (Panc 03.27, PANC-1, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~84% of this change | **1.61×** | +4.5 | 4e-04 | 28/46 (A-172, SW1417, …) | top dose only | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.54×** | +4.2 | 0.001 | 27/46 (HOP62, NCI-H460, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.29×** | +4.2 | 0.001 | 29/46 (PANC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.002 | 27/47 (HT-29, CFPAC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.0 | 0.002 | 22/45 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **1.53×** | +4.0 | 0.002 | 29/47 (HOP62, A549, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.006 | 27/46 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.73×** | +3.7 | 0.007 | 28/47 (HOP62, hTERT-HPNE, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.50×** | +3.7 | 0.007 | 21/47 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.43×** | +3.5 | 0.012 | 25/47 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.014 | 23/46 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.36×** | +3.0 | 0.059 | 18/47 (NCI-H460, KATO III, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | **1.23×** | +2.9 | 0.086 | 21/47 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |
| [[vincristine (drug)]] 0.05 µM |  | **1.43×** | +2.9 | 0.086 | 14/47 (C32, SW 900, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1594.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 4 lines (A498 0.137×, LS 180 0.105×, A-427 0.234×, A-172 0.266×; ⚠ cell-cycle shift, would explain all of this change); [[Amsacrine (drug)]] 5 µM in 4 lines (A498 0.347×, H4 0.242×, SW48 0.275×, LS 180 0.255×); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 3 lines (H4 0.0527×, SW48 0.0725×, A498 0.221×; ⚠ cell-cycle shift, would explain all of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (H4 0.265×, A498 0.459×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (RPMI-7951 0.107×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **0.460×** | -7.6 | 2e-11 | 41/47 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.595×** | -7.2 | 2e-10 | 35/47 (A498, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.436×** | -6.6 | 9e-09 | 37/47 (KATO III, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.581×** | -5.3 | 2e-05 | 37/47 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.583×** | -5.1 | 4e-05 | 35/47 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.616×** | -4.7 | 2e-04 | 26/47 (KATO III, SW48, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.668×** | -4.0 | 0.006 | 24/47 (H4, A-172, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.573×** | -3.8 | 0.012 | 27/47 (A-427, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.588×** | -3.6 | 0.021 | 23/47 (KATO III, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.775×** | -3.5 | 0.023 | 22/47 (A498, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~88% of this change | **0.520×** | -3.3 | 0.040 | 20/42 (SHP-77, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.711×** | -3.3 | 0.040 | 19/47 (A549, NCI-H1573, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.731×** | -3.1 | 0.096 | 15/47 (NCI-H2347, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +1.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1594. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 73.6 | 2 (2 ⚠) | 6 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Selinexor (drug)]] 5 µM 0.137× (z -22.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.347× (z -11.8) |
| [[H4 (line)]] | wt | 67.8 | 1 (1 ⚠) | 6 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 6.30× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0527× (z -14.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.242× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 30.4 | 2 (2 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.66× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Selinexor (drug)]] 5 µM 0.268× (z -10.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.211× (z -8.8) |
| [[A-172 (line)]] | wt | 40.8 | 3 (3 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 11.3× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Selinexor (drug)]] 5 µM 0.266× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 34.0 | 2 (2 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.13× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Selinexor (drug)]] 5 µM 0.292× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 39.4 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 7.31× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Selinexor (drug)]] 5 µM 0.363× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 47.9 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.97× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.187× (z -11.1) ⚠ cell-cycle shift, explains ~74% of this change |
| [[LoVo (line)]] | wt | 14.9 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 7.19× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Selinexor (drug)]] 5 µM 0.320× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 26.8 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 7.22× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Selinexor (drug)]] 5 µM 0.105× (z -14.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.255× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 35.3 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 9.04× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 59.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.21× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SNU-423 (line)]] | alt | 31.5 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.20× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A-427 (line)]] | wt | 69.2 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Selinexor (drug)]] 5 µM 0.234× (z -14.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 62.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.70× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[HOP62 (line)]] | alt | 54.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.48× (z +15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[HS-578T (line)]] | alt | 38.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.27× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H2347 (line)]] | alt | 41.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[Panc 03.27 (line)]] | alt | 28.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.21× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SNU-1 (line)]] | wt | 28.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -12.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 34.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SW480 (line)]] | alt | 49.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.52× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[C32 (line)]] | wt | 27.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.43× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[CFPAC-1 (line)]] | alt | 20.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.91× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[Hs 766T (line)]] | wt | 23.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.71× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[HT-29 (line)]] | alt | 24.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.96× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[J82 (line)]] | alt | 50.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H1792 (line)]] | alt | 16.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.6× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[RPMI-7951 (line)]] | alt | 32.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 8.53× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.107× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 49.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.20× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW 900 (line)]] | alt | 23.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.18× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SW48 (line)]] | wt | 47.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0725× (z -13.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.275× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 26.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.41× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H1573 (line)]] | alt | 14.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.7× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H2030 (line)]] | alt | 34.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +13.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 40.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[RKO (line)]] | wt | 28.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +10.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SHP-77 (line)]] | alt | 90.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[AN3 CA (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.10 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1594), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPX2]] | +0.96 | +0.94 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 952 |
| [[PRC1]] | +0.94 | +0.94 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 940 |
| [[BUB1]] | +0.93 | +0.91 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 979 |
| [[KIF4A]] | +0.93 | +0.94 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 925 |
| [[RACGAP1]] | +0.93 | +0.91 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 827 |
| [[DLGAP5]] | +0.93 | +0.92 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 967 |
| [[MKI67]] | +0.93 | +0.93 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 939 |
| [[KIF11]] | +0.92 | +0.93 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 957 |
| [[TOP2A]] | +0.92 | +0.94 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 976 |
| [[ARHGAP11A]] | +0.92 | +0.92 / +0.89 | both halves | 7e-06 | STRING 581 |
| [[KIF23]] | +0.92 | +0.93 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 885 |
| [[KIF18A]] | +0.92 | +0.91 / +0.91 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 622 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 3, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYBL1]] | B | MYBL1 activity raises BIRC5's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 2.43× lower at baseline in the lines without MYBL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[PIMREG]] | B | PIMREG activity raises BIRC5's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.55× lower at baseline in the lines without PIMREG | 0.007 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises BIRC5's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.21× lower at baseline in the lines without NEURL1B | 0.050 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[AURKB]] | C | AURKB activity raises BIRC5's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.94× lower at baseline in the lines without AURKB | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[PBK]] | C | PBK activity raises BIRC5's level | lines that do not express PBK (4) vs lines expressing it (46) | 3.11× lower at baseline in the lines without PBK | 0.018 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises BIRC5's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.83× lower at baseline in the lines without NDC80 | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[DIAPH3]] | C | DIAPH3 activity raises BIRC5's level | lines that do not express DIAPH3 (3) vs lines expressing it (47) | 3.20× lower at baseline in the lines without DIAPH3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises BIRC5's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.27× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[FAM72D]] | C | FAM72D activity raises BIRC5's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.72× lower at baseline in the lines without FAM72D | 0.084 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[SKA3]] | C | SKA3 activity raises BIRC5's level | lines that do not express SKA3 (3) vs lines expressing it (47) | 3.04× lower at baseline in the lines without SKA3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.962). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.6, -55.4); signed map (-49.3, -43.5). **Vector** length 125, 48.6% of its response variance represented; |z| ≥ 3 in 1,285 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M Transition* (reactome, mean cos +0.73 to 28); *Mitotic G2-G2/M phases* (reactome, mean cos +0.73 to 28); *Cyclin A/B1/B2 associated events during G2/M transition* (reactome, mean cos +0.78 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.9 | +6.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.1 | +2.1 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +4.0 | +6.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~80% of this change | +3.8 | +7.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.7 | +4.5 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.6 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +2.2 | +3.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.1 | +2.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.0 | -0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | -0.1 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | -7.5 | -6.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.3 | -7.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~94% of this change | -7.2 | -7.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -6.9 | -4.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~88% of this change | -4.7 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.7 | -0.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.6 | -1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.3 | -2.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -2.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.6 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | baculoviral IAP repeat containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:78,214,186-78,225,636 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EPR-1, survivin; previously API4 |
| Gene groups (HGNC) | Baculoviral IAP repeat containing; Chromosomal passenger complex |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE, E2F_TARGETS |
| Reactome | 29 pathways, smallest: TP53 regulates transcription of several additional cell death genes whose specific roles in p53-dependent apoptosis remain uncertain; M-decay: degradation of maternal mRNAs by maternally stored factors; TP53 Regulates Transcription of Cell Death Genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O15392](https://www.uniprot.org/uniprotkb/O15392) (Baculoviral IAP repeat-containing protein 5):

> Multitasking protein that has dual roles in promoting cell proliferation and preventing apoptosis. Component of a chromosome passage protein complex (CPC) which is essential for chromosome alignment and segregation during mitosis and cytokinesis. Acts as an important regulator of the localization of this complex; directs CPC movement to different locations from the inner centromere during prometaphase to midbody during cytokinesis and participates in the organization of the center spindle by …

**Summary**, from NCBI Gene [332](https://www.ncbi.nlm.nih.gov/gene/332):

> This gene is a member of the inhibitor of apoptosis (IAP) gene family, which encode negative regulatory proteins that prevent apoptotic cell death. IAP family members usually contain multiple baculovirus IAP repeat (BIR) domains, but this gene encodes proteins with only a single BIR domain. The encoded proteins also lack a C-terminus RING finger domain. Gene expression is high during fetal development and in most tumors, yet low in adult tissues. Alternatively spliced transcript variants …

**Accessions** — [HGNC:593](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:593) · Entrez [332](https://www.ncbi.nlm.nih.gov/gene/332) · UniProt [O15392](https://www.uniprot.org/uniprotkb/O15392) · Ensembl [ENSG00000089685](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089685)

## Data

Gene col 1594: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1594); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1594, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1594]; `tensor/DDL_lfc|DDL_z.npy` [1594]; `embed/gene_vectors.npy` [1594]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1594 or target_col == 1594). Every well: [[BIRC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BIRC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
