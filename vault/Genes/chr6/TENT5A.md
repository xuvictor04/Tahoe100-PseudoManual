---
symbol: "TENT5A"
type: "gene"
col: 3405
ensembl_id: "ENSG00000112773"
name: "terminal nucleotidyltransferase 5A"
location: "6q14.1"
module: 70
arm: "+"
pooled_cpm: 141.97
n_lines_expressing: 39
n_dd_up: 20
n_dd_down: 39
n_dd_up_clean: 18
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 14
direction_downstream: 7
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# TENT5A

*terminal nucleotidyltransferase 5A* — 6q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.27× (z +20.4, q 0e+00, up in 27 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.303× (z -21.0, q 0e+00, down in 34 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.490× (z -12.5, q 1e-33, down in 27 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DIPK2A]] (+0.59, fdr 1e-05), [[IDO1]] (+0.56, fdr 2e-05), [[MEIS2]] (+0.56, fdr 3e-05); moves opposite to [[BCR]] (-0.56, fdr 5e-05), [[ASAP2]] (-0.55, fdr 2e-05), [[LYPLA1]] (-0.53, fdr 4e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[KCNE4]] → it (grade B ⚠); 7 go from it, the strongest it → [[RBFA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3405.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +20.4 | 0e+00 | 27/38 (AsPC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.89×** | +18.0 | 0e+00 | 31/39 (SK-MEL-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +13.0 | 3e-36 | 31/37 (HOP62, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +8.4 | 9e-15 | 23/37 (A498, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.41×** | +6.1 | 1e-07 | 26/38 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.5 | 3e-06 | 20/37 (BT-474, SW1417, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.25×** | +4.8 | 1e-04 | 18/39 (LOX-IMVI, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 7e-04 | 20/37 (C32, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.19× | +4.4 | 8e-04 | 18/37 (NCI-H2347, LoVo, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.28×** | +4.3 | 8e-04 | 19/38 (LOX-IMVI, HOP62, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.22×** | +4.2 | 0.002 | 19/37 (LOX-IMVI, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.003 | 20/36 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.9 | 0.004 | 13/38 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.27×** | +3.8 | 0.007 | 13/37 (A498, LoVo, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.017 | 17/37 (LoVo, C32, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.027 | 16/36 (LOX-IMVI, NCI-H2347, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.027 | 16/37 (HOP62, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3405.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.303×** | -21.0 | 0e+00 | 34/37 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.315×** | -19.5 | 0e+00 | 29/34 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.490×** | -12.5 | 1e-33 | 27/37 (RPMI-7951, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.524×** | -11.3 | 1e-27 | 27/37 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.575×** | -9.7 | 3e-20 | 27/37 (RPMI-7951, H4, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.615×** | -8.2 | 2e-14 | 29/36 (SNU-423, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.729×** | -7.8 | 4e-13 | 20/37 (CHP-212, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.738×** | -7.5 | 4e-12 | 25/38 (SW 900, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.652×** | -7.5 | 4e-12 | 23/36 (SW 900, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.643×** | -7.4 | 5e-12 | 23/36 (NCI-H1792, SW 900, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.659×** | -7.0 | 1e-10 | 28/37 (A498, HepG2/C3A, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.686×** | -6.6 | 2e-09 | 24/36 (SNU-423, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.668×** | -6.2 | 2e-08 | 23/37 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.713×** | -5.9 | 1e-07 | 25/37 (SW48, NCI-H2030, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.736×** | -5.4 | 3e-06 | 21/37 (NCI-H23, SW 900, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.811×** | -5.2 | 8e-06 | 23/37 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 5 µM |  | **0.571×** | -5.1 | 9e-06 | 26/35 (NCI-H23, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.746×** | -5.1 | 9e-06 | 22/37 (CHP-212, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.762×** | -4.8 | 5e-05 | 20/37 (RPMI-7951, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.623×** | -4.6 | 1e-04 | 20/37 (SW 900, NCI-H1792, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.778×** | -4.4 | 3e-04 | 20/36 (SW 900, NCI-H23, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM |  | **0.767×** | -4.4 | 3e-04 | 19/37 (NCI-H1573, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3405. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 162 | 0 | 13 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.136× (z -13.4) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.338× (z -10.7) |
| [[A-172 (line)]] | wt | 170 | 4 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.0789× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.294× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 478 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -20.6) |
| [[A498 (line)]] | wt | 141 | 2 | 7 (3 ⚠) | [[Selinexor (drug)]] 5 µM 2.18× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.448× (z -9.7) |
| [[LoVo (line)]] | wt | 147 | 8 (6 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.140× (z -19.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 767 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.457× (z -13.2) |
| [[HS-578T (line)]] | alt | 232 | 3 | 5 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.235× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.292× (z -11.8) |
| [[BT-474 (line)]] | alt | 83.9 | 4 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.204× (z -11.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 463 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -20.8) |
| [[H4 (line)]] | wt | 245 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -16.6) |
| [[SNU-423 (line)]] | alt | 637 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0482× (z -27.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.244× (z -18.1) |
| [[C32 (line)]] | wt | 260 | 2 | 4 (3 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.205× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.368× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 61.5 | 2 | 4 (2 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.356× (z -10.8) |
| [[HOP62 (line)]] | alt | 143 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +15.6) | — |
| [[Hs 766T (line)]] | wt | 182 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.364× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 86.8 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.96× (z +18.8) | — |
| [[SK-MEL-2 (line)]] | alt | 51.7 | 4 | 1 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 8.63× (z +16.3) | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -9.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 210 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.116× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.483× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 46.5 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +22.2) | — |
| [[CFPAC-1 (line)]] | alt | 45.0 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.70× (z +20.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 59.6 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.302× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 312 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -17.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 110 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 343 | 1 | 3 (2 ⚠) | [[Harringtonine (drug)]] 0.05 µM 2.47× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.548× (z -8.9) |
| [[SW1417 (line)]] | alt | 35.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +16.9) | — |
| [[HepG2_C3A (line)]] | wt | 86.2 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.69× (z +17.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.287× (z -9.7) ⚠ toxic |
| [[J82 (line)]] | alt | 139 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -11.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 145 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -19.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 46.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.25× (z +17.4) | — |
| [[COLO 205 (line)]] | alt | 104 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0876× (z -16.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 81.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +17.0) | — |
| [[hTERT-HPNE (line)]] | wt | 217 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -9.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 164 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -13.4) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 719 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0350× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.234× (z -10.3) |
| [[SW48 (line)]] | wt | 48.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.07× (z +13.4) | — |
| [[A-427 (line)]] | wt | 7.68 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 24.6 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 27.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 18.3 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 19.7 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 23.0 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.9 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 19.3 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 22.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 31.1 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3405), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIPK2A]] | +0.59 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[IDO1]] | +0.56 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[MEIS2]] | +0.56 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[LINC02100]] | +0.55 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[PIK3R3]] | +0.54 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[TET2]] | +0.53 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[HLA-A]] | +0.53 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[INTS6L]] | +0.52 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ARRDC3]] | +0.52 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[HCP5]] | +0.52 | +0.34 / +0.42 | both halves | 1e-04 |  |
| [[EPHX1]] | +0.52 | +0.54 / +0.29 | both halves | 2e-04 |  |
| [[GBP4]] | +0.52 | +0.48 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCR]] | -0.56 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[ASAP2]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[LYPLA1]] | -0.53 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[TBC1D16]] | -0.53 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[PSEN2]] | -0.52 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ZDHHC18]] | -0.52 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[C16orf74]] | -0.52 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[ANKS6]] | -0.51 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[MAPKAPK3]] | -0.51 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[RBFA]] | -0.51 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[LDLRAD3]] | -0.50 | -0.43 / -0.49 | both halves | 4e-05 |  |
| [[ERGIC1]] | -0.50 | -0.37 / -0.40 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNE4]] | B | KCNE4 activity raises TENT5A's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 3.82× lower at baseline in the lines without KCNE4 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN |
| [[MMP13]] | B | MMP13 activity raises TENT5A's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 2.72× lower at baseline in the lines without MMP13 | 0.012 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[IGFBP5]] | B | IGFBP5 activity raises TENT5A's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 3.35× lower at baseline in the lines without IGFBP5 | 0.014 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2 |
| [[TOP2A]] | B | TOP2A activity lowers TENT5A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EDIL3]] | B | EDIL3 activity raises TENT5A's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 3.37× lower at baseline in the lines without EDIL3 | 0.025 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC |
| [[PLAAT4]] | B | PLAAT4 activity raises TENT5A's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 2.02× lower at baseline in the lines without PLAAT4 | 0.028 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[PLOD2]] | B | PLOD2 activity raises TENT5A's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 3.30× lower at baseline in the lines without PLOD2 | 0.028 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[APOL3]] | B | APOL3 activity raises TENT5A's level | lines that do not express APOL3 (14) vs lines expressing it (36) | 2.82× lower at baseline in the lines without APOL3 | 0.034 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |
| [[APLN]] | B | APLN activity raises TENT5A's level | lines that do not express APLN (13) vs lines expressing it (37) | 2.35× lower at baseline in the lines without APLN | 0.048 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC02100]] | B | LINC02100 activity raises TENT5A's level | lines that do not express LINC02100 (9) vs lines expressing it (41) | 2.14× lower at baseline in the lines without LINC02100 | 0.057 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, RASA3 |
| [[JAM2]] | B | JAM2 activity raises TENT5A's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 2.83× lower at baseline in the lines without JAM2 | 0.067 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R |
| [[MAP2K1]] | B | MAP2K1 activity lowers TENT5A's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBFA]] | B | TENT5A activity lowers RBFA's level | lines that do not express TENT5A (11) vs lines expressing it (39) | 1.81× higher at baseline in the lines without TENT5A | 0.040 | ⚠ within organs, on part of the lines; also absent: GBP2, CXCL2, IFI44; maybe low, not absent |
| [[PLAAT4]] | B | TENT5A activity raises PLAAT4's level | lines that do not express TENT5A (11) vs lines expressing it (39) | 2.27× lower at baseline in the lines without TENT5A | 0.082 | ⚠ within organs, on part of the lines; also absent: GBP2, CXCL2, IFI44; maybe low, not absent |
| [[PSEN2]] | B | TENT5A activity lowers PSEN2's level | lines that do not express TENT5A (11) vs lines expressing it (39) | 1.76× higher at baseline in the lines without TENT5A | 0.091 | ⚠ within organs, on part of the lines; also absent: GBP2, CXCL2, IFI44; maybe low, not absent |
| [[LYPLA1]] | B | TENT5A activity lowers LYPLA1's level | lines that do not express TENT5A (11) vs lines expressing it (39) | 1.36× higher at baseline in the lines without TENT5A | 0.095 | ⚠ within organs, on part of the lines; also absent: GBP2, CXCL2, IFI44; maybe low, not absent |
| [[HLA-A]] | B | TENT5A activity raises HLA-A's level | lines that do not express TENT5A (11) vs lines expressing it (39) | 2.72× lower at baseline in the lines without TENT5A | 0.099 | ⚠ within organs, on part of the lines; also absent: GBP2, CXCL2, IFI44; maybe low, not absent |
| [[BCR]] | B | TENT5A activity lowers BCR's level | lines that do not express TENT5A (11) vs lines expressing it (39) | 1.04× higher at baseline in the lines without TENT5A | 0.0999 | ⚠ within organs, on part of the lines; also absent: GBP2, CXCL2, IFI44; maybe low, not absent |
| [[OASL]] | C | TENT5A activity raises OASL's level | lines that do not express TENT5A (11) vs lines expressing it (39) | 3.49× lower at baseline in the lines without TENT5A | 0.014 | ⚠ within organs, on part of the lines; also absent: GBP2, CXCL2, IFI44; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (26.5, -5.6); signed map (58.9, 28.7). **Vector** length 134, 40.8% of its response variance represented; |z| ≥ 3 in 1,436 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +13.3 | +20.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +11.8 | +18.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.4 | +13.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.9 | +5.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.8 | +8.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.7 | +4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.4 | +6.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.2 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +2.6 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.2 | -7.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -5.1 | -6.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -5.1 | -5.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.9 | -3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.8 | -7.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | terminal nucleotidyltransferase 5A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.1 — chr6:81,491,439-81,752,774 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20037; previously C6orf37, FAM46A |
| Gene groups (HGNC) | Terminal nucleotidyltransferases |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96IP4](https://www.uniprot.org/uniprotkb/Q96IP4) (Terminal nucleotidyltransferase 5A):

> Cytoplasmic non-canonical poly(A) RNA polymerase that catalyzes the transfer of one adenosine molecule from an ATP to an mRNA poly(A) tail bearing a 3'-OH terminal group and participates in the cytoplasmic polyadenylation. Polyadenylates mRNA encoding extracellular matrix constituents and other genes crucial for bone mineralization and during osteoblast mineralization, mainly focuses on ER-targeted mRNAs (By similarity).

**Summary**, from NCBI Gene [55603](https://www.ncbi.nlm.nih.gov/gene/55603):

> Enables poly(A) RNA polymerase activity. Predicted to be involved in mRNA stabilization; positive regulation of bone mineralization; and positive regulation of osteoblast differentiation. Predicted to act upstream of or within response to bacterium. Predicted to be located in cytoplasm. Implicated in lung non-small cell carcinoma; osteoarthritis; and osteogenesis imperfecta type 18. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18345](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18345) · Entrez [55603](https://www.ncbi.nlm.nih.gov/gene/55603) · UniProt [Q96IP4](https://www.uniprot.org/uniprotkb/Q96IP4) · Ensembl [ENSG00000112773](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112773)

## Data

Gene col 3405: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3405); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3405, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3405]; `tensor/DDL_lfc|DDL_z.npy` [3405]; `embed/gene_vectors.npy` [3405]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3405 or target_col == 3405). Every well: [[TENT5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TENT5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
