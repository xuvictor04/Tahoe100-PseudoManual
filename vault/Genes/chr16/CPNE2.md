---
symbol: "CPNE2"
type: "gene"
col: 6455
ensembl_id: "ENSG00000140848"
name: "copine 2"
location: "16q13"
module: 2
arm: "+"
pooled_cpm: 20.02
n_lines_expressing: 48
n_dd_up: 14
n_dd_down: 25
n_dd_up_clean: 7
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CPNE2

*copine 2* — 16q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.57× (z +7.8, q 3e-12, up in 26 of 46 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.52× (z +7.7, q 4e-12, up in 23 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.372× (z -25.6, q 0e+00, down in 36 of 45 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.332× (z -20.2, q 0e+00, down in 40 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TYRO3]] (+0.68, fdr 7e-06), [[KLC1]] (+0.65, fdr 7e-06), [[MICALL1]] (+0.65, fdr 7e-06); moves opposite to [[DOP1A]] (-0.54, fdr 2e-05), [[RNF5]] (-0.53, fdr 3e-05), [[ATG3]] (-0.52, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6455.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.57×** | +7.8 | 3e-12 | 26/46 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +7.7 | 4e-12 | 23/45 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +6.1 | 2e-07 | 16/29 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.34×** | +5.2 | 3e-05 | 21/45 (NCI-H2030, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +4.8 | 2e-04 | 19/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +4.3 | 0.002 | 14/45 (NCI-H2030, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.004 | 10/45 (SW480, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.24×** | +3.9 | 0.006 | 11/39 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.006 | 11/45 (NCI-H1573, NCI-H460, …) | rises with dose | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.23×** | +3.8 | 0.009 | 11/45 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.24×** | +3.8 | 0.009 | 7/46 (C-33 A, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +3.7 | 0.011 | 10/46 (NCI-H1792, A-427, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.22×** | +3.6 | 0.013 | 8/45 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.013 | 10/43 (SW480, NCI-H1573, …) | two highest doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.021 | 4/45 (HEC-1-A, HT-29, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +3.0 | 0.092 | 12/46 (SW480, NCI-H1573, …) | all doses, flat | position effect removed |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.17× | +2.9 | 0.097 | 8/45 (hTERT-HPNE, C-33 A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6455.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.372×** | -25.6 | 0e+00 | 36/45 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.332×** | -20.2 | 0e+00 | 40/45 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.342×** | -18.9 | 0e+00 | 37/46 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.392×** | -17.1 | 0e+00 | 40/46 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.402×** | -16.7 | 0e+00 | 42/46 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.439×** | -15.1 | 0e+00 | 32/45 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.617×** | -12.5 | 7e-34 | 30/45 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.510×** | -12.3 | 4e-33 | 35/46 (LoVo, SNU-1, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.320×** | -10.9 | 7e-26 | 38/46 (LoVo, H4, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.579×** | -10.0 | 1e-21 | 34/46 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.580×** | -10.0 | 1e-21 | 31/44 (MIA PaCa-2, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.588×** | -9.7 | 1e-20 | 30/44 (SNU-1, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.596×** | -9.5 | 1e-19 | 34/46 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.420×** | -8.3 | 4e-15 | 24/42 (RKO, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.629×** | -8.2 | 1e-14 | 28/44 (J82, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.816×** | -5.3 | 4e-06 | 16/46 (BT-474, A-172, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.590×** | -5.0 | 1e-05 | 17/46 (A549, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.804×** | -4.0 | 0.002 | 19/46 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6455. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 23.1 | 1 | 7 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.04× (z +9.0) | [[PH-797804 (drug)]] 5 µM 0.0647× (z -11.6) |
| [[LoVo (line)]] | wt | 34.1 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -18.2) |
| [[NCI-H460 (line)]] | wt | 22.4 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -17.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.167× (z -14.1) |
| [[A-172 (line)]] | wt | 41.6 | 2 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +12.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.47× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -13.7) |
| [[SNU-1 (line)]] | wt | 57.8 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0866× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.129× (z -11.7) |
| [[A549 (line)]] | wt | 31.1 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -18.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -11.4) |
| [[MIA PaCa-2 (line)]] | alt | 19.1 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0710× (z -16.9) |
| [[HEC-1-A (line)]] | alt | 17.5 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.121× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 17.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -17.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0827× (z -15.6) |
| [[RKO (line)]] | wt | 27.1 | 0 | 5 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0351× (z -12.0) |
| [[SNU-423 (line)]] | alt | 18.4 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.130× (z -12.0) |
| [[A498 (line)]] | wt | 29.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -21.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.315× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 12.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -10.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -8.8) |
| [[BT-474 (line)]] | alt | 18.0 | 0 | 3 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.193× (z -12.4) |
| [[C-33 A (line)]] | alt | 31.6 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.143× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~53% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.239× (z -8.6) |
| [[HS-578T (line)]] | alt | 20.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -11.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.254× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 14.7 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0322× (z -21.4) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0887× (z -15.1) |
| [[SW48 (line)]] | wt | 27.2 | 0 | 3 (1 ⚠) | — | [[TAK-901 (drug)]] 0.05 µM 0.0391× (z -16.0) |
| [[SW480 (line)]] | alt | 14.8 | 1 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.77× (z +8.9) | [[Harringtonine (drug)]] 5 µM 0.254× (z -11.5) |
| [[Hs 766T (line)]] | wt | 26.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -11.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.267× (z -9.0) |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -11.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[J82 (line)]] | alt | 27.9 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -9.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.347× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 49.0 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.304× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 15.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -18.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.249× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -11.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[PANC-1 (line)]] | alt | 15.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -18.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -12.3) |
| [[A-427 (line)]] | wt | 19.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -12.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[AN3 CA (line)]] | alt | 28.5 | 0 | 1 | — | [[Monocrotaline (drug)]] 5 µM 0.0867× (z -8.6) |
| [[H4 (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -10.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HepG2_C3A (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.156× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[hTERT-HPNE (line)]] | wt | 18.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[RPMI-7951 (line)]] | alt | 28.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -8.5) |
| [[SHP-77 (line)]] | alt | 5.33 | 0 | 1 (1 ⚠) | — | [[OTS514 (drug)]] 0.05 µM 0.0638× (z -9.0) ⚠ transcription drop |
| [[SK-MEL-2 (line)]] | alt | 12.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.153× (z -9.3) |
| [[SW 900 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -10.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[C32 (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6455), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TYRO3]] | +0.68 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[KLC1]] | +0.65 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[MICALL1]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[ADCY7]] | +0.63 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[MELTF]] | +0.62 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[SANBR]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[TTC7B]] | +0.62 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[LIMK1]] | +0.60 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[TANGO2]] | +0.59 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[FPGS]] | +0.58 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[MPP3]] | +0.58 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[SFXN5]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOP1A]] | -0.54 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[RNF5]] | -0.53 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[ATG3]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[TRIM7-AS2]] | -0.49 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[TXNIP]] | -0.49 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[CA9]] | -0.48 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[CSTF1]] | -0.48 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[REL]] | -0.48 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[RSPRY1]] | -0.48 | -0.51 / -0.42 | both halves | 4e-05 | ⚠ same locus (37.8 kb, same strand: neighbours can correlate without regulation) |
| [[DYNC2I1]] | -0.48 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[TBCK]] | -0.48 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[WDPCP]] | -0.47 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[GALK2]] | -0.47 | -0.42 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CPNE2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MELTF]] | B | MELTF activity raises CPNE2's level | lines that do not express MELTF (7) vs lines expressing it (43) | 1.43× lower at baseline in the lines without MELTF | 0.060 | ⚠ within organs, on part of the lines; also absent: EPHX2, ACCS; maybe low, not absent; its own permutation p |
| [[FSD1L]] | C | FSD1L activity raises CPNE2's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 4.44× lower at baseline in the lines without FSD1L | 0.003 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent; co-absent with the target |
| [[PGGHG]] | C | PGGHG activity raises CPNE2's level | lines that do not express PGGHG (4) vs lines expressing it (46) | 2.52× lower at baseline in the lines without PGGHG | 0.044 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GARIN1B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.433). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (18.0, -11.8); signed map (-7.6, 25.0). **Vector** length 82.3, 17.7% of its response variance represented; |z| ≥ 3 in 1,243 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +9.0 | +7.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | +8.0 | +7.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.0 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.7 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | -1.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.5 | +2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.9 | +3.9 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.5 | -10.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.6 | -9.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -8.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -2.5 | -3.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.2 | -18.9 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | -0.9 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | copine 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q13 — chr16:57,092,583-57,148,369 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CPN2 |
| Gene groups (HGNC) | Copines |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FN4](https://www.uniprot.org/uniprotkb/Q96FN4) (Copine-2):

> Calcium-dependent phospholipid-binding protein that plays a role in calcium-mediated intracellular processes. Exhibits calcium-dependent cell membrane binding properties.

**Summary**, from NCBI Gene [221184](https://www.ncbi.nlm.nih.gov/gene/221184):

> Calcium-dependent membrane-binding proteins may regulate molecular events at the interface of the cell membrane and cytoplasm. This gene is one of several genes that encode a calcium-dependent protein containing two N-terminal type II C2 domains and an integrin A domain-like sequence in the C-terminus. Sequence analysis identified multiple alternatively spliced transcript variants but their full-length natures could not be determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2315](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2315) · Entrez [221184](https://www.ncbi.nlm.nih.gov/gene/221184) · UniProt [Q96FN4](https://www.uniprot.org/uniprotkb/Q96FN4) · Ensembl [ENSG00000140848](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140848)

## Data

Gene col 6455: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6455); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6455, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6455]; `tensor/DDL_lfc|DDL_z.npy` [6455]; `embed/gene_vectors.npy` [6455]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6455 or target_col == 6455). Every well: [[CPNE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPNE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
