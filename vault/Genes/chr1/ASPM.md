---
symbol: "ASPM"
type: "gene"
col: 823
ensembl_id: "ENSG00000066279"
name: "assembly factor for spindle microtubules"
location: "1q31.3"
module: 22
arm: "+"
pooled_cpm: 147.39
n_lines_expressing: 49
n_dd_up: 35
n_dd_down: 40
n_dd_up_clean: 20
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# ASPM

*assembly factor for spindle microtubules* — 1q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.32× (z +15.8, q 0e+00, up in 41 of 47 measured lines) ⚠ cell-cycle shift, explains ~92% of this change. The strongest without an alert is [[5-Azacytidine (drug)]] 5 µM: 1.38× (z +4.6, q 4e-04, up in 26 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (21 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.472× (z -14.1, q 2e-42, down in 44 of 47 measured lines) ⚠ cell-cycle shift, explains ~60% of this change. The strongest without an alert is [[Amsacrine (drug)]] 5 µM: 0.723× (z -6.4, q 1e-08, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPF]] (+0.92, fdr 7e-06), [[DEPDC1]] (+0.92, fdr 7e-06), [[TPX2]] (+0.91, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[NDC80]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 15 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 823.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **2.32×** | +15.8 | 0e+00 | 41/47 (NCI-H2347, NCI-H2030, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **2.31×** | +11.4 | 1e-27 | 43/47 (NCI-H2347, LoVo, …) | rises with dose | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **2.75×** | +7.5 | 1e-11 | 37/46 (J82, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.44×** | +7.1 | 2e-10 | 38/47 (NCI-H2347, NCI-H23, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~98% of this change | **1.62×** | +6.8 | 1e-09 | 33/47 (HT-29, NCI-H2030, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.54×** | +6.1 | 1e-07 | 29/47 (NCI-H2347, NCI-H2030, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.38×** | +4.6 | 4e-04 | 25/46 (HOP62, SW 900, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.38×** | +4.6 | 4e-04 | 26/47 (MIA PaCa-2, hTERT-HPNE, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.36×** | +4.4 | 7e-04 | 28/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.33×** | +4.0 | 0.004 | 22/48 (A-172, RKO, …) | rises with dose | composition shift |
| [[Mebendazole (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.005 | 20/47 (SHP-77, HT-29, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.34×** | +3.9 | 0.005 | 24/47 (SW 900, NCI-H1792, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.32×** | +3.8 | 0.006 | 23/43 (A-172, NCI-H1792, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.31×** | +3.8 | 0.006 | 23/48 (HT-29, NCI-H2030, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.31×** | +3.7 | 0.008 | 21/47 (NCI-H2347, C32, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.009 | 20/46 (HOP62, hTERT-HPNE, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.019 | 17/47 (CFPAC-1, LOX-IMVI, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.019 | 19/47 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.019 | 20/47 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.58×** | +3.4 | 0.019 | 17/48 (HOP62, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.019 | 15/47 (C32, SW 900, …) | rises with dose |  |
| [[AZD1390 (drug)]] 0.05 µM |  | **1.28×** | +3.3 | 0.028 | 18/47 (Panc 03.27, HT-29, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.037 | 14/48 (AsPC-1, A549, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.037 | 16/48 (MIA PaCa-2, LS 180, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.040 | 21/47 (MIA PaCa-2, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.044 | 20/47 (HOP62, HT-29, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 1.18× | +3.0 | 0.047 | 12/47 (NCI-H460, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 21 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 823.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.472×** | -14.1 | 2e-42 | 44/47 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.421×** | -12.3 | 4e-32 | 44/47 (LS 180, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.441×** | -11.0 | 1e-25 | 42/47 (HCT15, HT-29, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.469×** | -10.7 | 1e-24 | 41/47 (C32, KATO III, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.546×** | -8.2 | 2e-14 | 44/47 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.560×** | -8.2 | 2e-14 | 34/47 (CHP-212, A-172, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **0.342×** | -7.9 | 2e-13 | 38/44 (SHP-77, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.582×** | -7.7 | 1e-12 | 39/47 (J82, SW1417, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.723×** | -6.4 | 1e-08 | 34/47 (CHP-212, A-172, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.635×** | -6.3 | 2e-08 | 34/47 (NCI-H1573, SW48, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.441×** | -6.1 | 7e-08 | 33/47 (BT-474, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.647×** | -5.9 | 1e-07 | 34/47 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.659×** | -5.9 | 1e-07 | 38/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.659×** | -5.8 | 3e-07 | 35/47 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.737×** | -5.8 | 3e-07 | 35/47 (A-427, LS 180, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.676×** | -5.6 | 1e-06 | 26/47 (PANC-1, C32, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.515×** | -4.9 | 3e-05 | 29/47 (C-33 A, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.520×** | -4.8 | 4e-05 | 29/47 (HT-29, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.693×** | -4.8 | 4e-05 | 31/47 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.719×** | -4.7 | 7e-05 | 26/47 (A-427, BT-474, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.715×** | -4.4 | 3e-04 | 24/46 (A-172, LS 180, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.738×** | -4.0 | 0.001 | 23/47 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.634×** | -3.8 | 0.003 | 23/48 (A-427, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.5 µM |  | **0.755×** | -3.3 | 0.015 | 21/47 (CHP-212, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.643×** | -3.3 | 0.018 | 14/47 (HEC-1-A, SW1417, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.650×** | -3.2 | 0.023 | 20/47 (J82, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.813×** | -2.9 | 0.051 | 14/47 (RKO, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.55 per unit of S-phase module lfc, +1.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 823. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 126 | 2 (2 ⚠) | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +11.9) ⚠ cell-cycle shift, explains ~92% of this change | [[Selinexor (drug)]] 5 µM 0.188× (z -14.9) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.199× (z -10.7) |
| [[A-172 (line)]] | wt | 184 | 0 | 9 (6 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.232× (z -14.7) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.338× (z -11.4) |
| [[C32 (line)]] | wt | 198 | 3 (3 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +12.8) ⚠ cell-cycle shift, explains ~92% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.185× (z -12.4) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 0.5 µM 0.278× (z -9.2) |
| [[A-427 (line)]] | wt | 186 | 0 | 8 (7 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.184× (z -18.4) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.316× (z -13.5) |
| [[A549 (line)]] | wt | 142 | 1 (1 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +13.5) ⚠ cell-cycle shift, explains ~92% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.210× (z -12.3) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.277× (z -10.1) |
| [[H4 (line)]] | wt | 168 | 0 | 6 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.157× (z -12.9) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.245× (z -10.4) |
| [[LS 180 (line)]] | wt | 99.4 | 0 | 6 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.155× (z -15.6) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.286× (z -11.0) |
| [[LoVo (line)]] | wt | 95.1 | 2 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +14.6) ⚠ cell-cycle shift, explains ~92% of this change | [[Selinexor (drug)]] 5 µM 0.335× (z -12.2) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.476× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 186 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.280× (z -13.6) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.448× (z -8.9) |
| [[A498 (line)]] | wt | 178 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.132× (z -20.0) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.370× (z -10.3) |
| [[HCT15 (line)]] | alt | 250 | 0 | 4 (4 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.131× (z -12.3) ⚠ cell-cycle shift, explains ~47% of this change |
| [[HOP62 (line)]] | alt | 266 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +10.8) ⚠ cell-cycle shift, explains ~92% of this change | [[Selinexor (drug)]] 5 µM 0.347× (z -11.8) ⚠ cell-cycle shift, explains ~60% of this change |
| [[HT-29 (line)]] | alt | 160 | 0 | 4 (4 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.178× (z -12.2) ⚠ cell-cycle shift, explains ~47% of this change |
| [[KATO III (line)]] | alt | 88.2 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +12.2) ⚠ cell-cycle shift, explains ~92% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.305× (z -10.0) ⚠ cell-cycle shift, explains ~53% of this change |
| [[NCI-H2347 (line)]] | alt | 91.1 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.01× (z +26.3) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[PANC-1 (line)]] | alt | 136 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +14.6) ⚠ cell-cycle shift, explains ~92% of this change | [[Bortezomib (drug)]] 0.05 µM 0.341× (z -9.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SW48 (line)]] | wt | 130 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.165× (z -10.9) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.05 µM 0.234× (z -8.8) |
| [[CHP-212 (line)]] | wt | 227 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0298× (z -14.9) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.145× (z -11.5) |
| [[hTERT-HPNE (line)]] | wt | 107 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +8.7) ⚠ cell-cycle shift, explains ~92% of this change | [[Selinexor (drug)]] 5 µM 0.211× (z -12.5) ⚠ cell-cycle shift, explains ~60% of this change |
| [[NCI-H1573 (line)]] | alt | 69.9 | 0 | 3 (3 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.246× (z -9.4) ⚠ cell-cycle shift, explains ~68% of this change |
| [[NCI-H23 (line)]] | alt | 155 | 2 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.15× (z +11.8) ⚠ cell-cycle shift, explains ~71% of this change | [[Selinexor (drug)]] 5 µM 0.413× (z -10.0) ⚠ cell-cycle shift, explains ~60% of this change |
| [[RKO (line)]] | wt | 106 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.03× (z +20.0) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[SNU-1 (line)]] | wt | 146 | 0 | 3 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.110× (z -12.5) ⚠ cell-cycle shift, explains ~96% of this change |
| [[AsPC-1 (line)]] | alt | 41.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +10.5) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[HS-578T (line)]] | alt | 75.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +13.0) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[NCI-H1792 (line)]] | alt | 59.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +9.6) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[NCI-H2030 (line)]] | alt | 81.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.03× (z +22.1) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[Panc 03.27 (line)]] | alt | 111 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +17.6) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 202 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.1) ⚠ cell-cycle shift, explains ~92% of this change | [[Selinexor (drug)]] 5 µM 0.416× (z -9.2) ⚠ cell-cycle shift, explains ~60% of this change |
| [[BT-474 (line)]] | alt | 207 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +8.6) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[C-33 A (line)]] | alt | 189 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.339× (z -8.6) ⚠ cell-cycle shift, explains ~53% of this change |
| [[CFPAC-1 (line)]] | alt | 85.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.378× (z -9.1) ⚠ cell-cycle shift, explains ~60% of this change |
| [[HEC-1-A (line)]] | alt | 223 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.439× (z -8.8) ⚠ cell-cycle shift, explains ~53% of this change |
| [[Hs 766T (line)]] | wt | 139 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.382× (z -9.1) ⚠ cell-cycle shift, explains ~60% of this change |
| [[J82 (line)]] | alt | 242 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.0) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[RPMI-7951 (line)]] | alt | 139 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +12.1) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[SHP-77 (line)]] | alt | 161 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.106× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~45% of this change |
| [[SNU-423 (line)]] | alt | 123 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +10.3) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[SW 1271 (line)]] | alt | 176 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0640× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[SW1417 (line)]] | alt | 118 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +8.9) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[SW480 (line)]] | alt | 216 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.346× (z -9.8) ⚠ cell-cycle shift, explains ~47% of this change |
| [[AN3 CA (line)]] | alt | 220 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.9 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 206 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 823), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPF]] | +0.92 | +0.93 / +0.94 | both halves | 7e-06 | STRING 987 |
| [[DEPDC1]] | +0.92 | +0.91 / +0.92 | both halves | 7e-06 | STRING 861 |
| [[TPX2]] | +0.91 | +0.87 / +0.92 | both halves | 7e-06 | STRING 949 |
| [[MKI67]] | +0.90 | +0.88 / +0.92 | both halves | 7e-06 | STRING 962 |
| [[BIRC5]] | +0.90 | +0.88 / +0.91 | both halves | 7e-06 | STRING 879 |
| [[CCNB1]] | +0.90 | +0.88 / +0.90 | both halves | 7e-06 | STRING 952 |
| [[CENPE]] | +0.90 | +0.91 / +0.93 | both halves | 7e-06 | STRING 981 |
| [[PRC1]] | +0.90 | +0.88 / +0.88 | both halves | 7e-06 | STRING 921 |
| [[KIF4A]] | +0.89 | +0.88 / +0.90 | both halves | 7e-06 | STRING 952 |
| [[HMMR]] | +0.88 | +0.83 / +0.92 | both halves | 7e-06 | STRING 928 |
| [[NDC80]] | +0.87 | +0.86 / +0.88 | both halves | 7e-06 | STRING 969 |
| [[KIF14]] | +0.87 | +0.82 / +0.90 | both halves | 7e-06 | STRING 963 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDC80]] | C | NDC80 activity raises ASPM's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.80× lower at baseline in the lines without NDC80 | 0.015 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises ASPM's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.87× lower at baseline in the lines without AURKB | 0.031 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[MYLK2]] | C | MYLK2 activity raises ASPM's level | lines that do not express MYLK2 (3) vs lines expressing it (47) | 3.29× lower at baseline in the lines without MYLK2 | 0.074 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, NDC80, SMARCD3; maybe low, not absent |
| [[FAM72D]] | C | FAM72D activity raises ASPM's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without FAM72D | 0.077 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises ASPM's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 2.93× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.901). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.7, -56.3); signed map (-50.4, -44.4). **Vector** length 182, 73.1% of its response variance represented; |z| ≥ 3 in 1,654 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.72 to 60); *DREAM G2/M down* (control, mean cos +0.83 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.69 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | +12.3 | +15.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +10.4 | +11.4 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +6.7 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.6 | +6.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | +5.4 | +7.5 |
|  | [[Docetaxel (drug)]] 5 µM |  | +4.4 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.3 | +3.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.0 | +3.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.7 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +3.6 | +3.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -10.7 | -14.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -10.6 | -12.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -9.3 | -10.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | -8.6 | -11.0 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -7.5 | -8.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | -6.4 | -6.4 |
|  | [[EX229 (drug)]] 5 µM |  | -5.5 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.2 | -5.6 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -4.9 | -5.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.7 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | assembly factor for spindle microtubules |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q31.3 — chr1:197,084,121-197,146,694 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Calmbp1, ASP, FLJ10517, FLJ10549; previously MCPH5 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZT6](https://www.uniprot.org/uniprotkb/Q8IZT6) (Abnormal spindle-like microcephaly-associated protein):

> Involved in mitotic spindle regulation and coordination of mitotic processes. The function in regulating microtubule dynamics at spindle poles including spindle orientation, astral microtubule density and poleward microtubule flux seems to depend on the association with the katanin complex formed by KATNA1 and KATNB1. Enhances the microtubule lattice severing activity of KATNA1 by recruiting the katanin complex to microtubules. Can block microtubule minus-end growth and reversely this function …

**Summary**, from NCBI Gene [259266](https://www.ncbi.nlm.nih.gov/gene/259266):

> This gene is the human ortholog of the Drosophila melanogaster 'abnormal spindle' gene (asp), which is essential for normal mitotic spindle function in embryonic neuroblasts. Studies in mouse also suggest a role of this gene in mitotic spindle regulation, with a preferential role in regulating neurogenesis. Mutations in this gene are associated with microcephaly primary type 5. Multiple transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, May 2011]

**Accessions** — [HGNC:19048](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19048) · Entrez [259266](https://www.ncbi.nlm.nih.gov/gene/259266) · UniProt [Q8IZT6](https://www.uniprot.org/uniprotkb/Q8IZT6) · Ensembl [ENSG00000066279](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066279)

## Data

Gene col 823: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 823); `tables/drug_effects.parquet` (79 rows, flagged included); `relations/gene_relations.parquet` (col_a == 823, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 823]; `tensor/DDL_lfc|DDL_z.npy` [823]; `embed/gene_vectors.npy` [823]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 823 or target_col == 823). Every well: [[ASPM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASPM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
