---
symbol: "MYOF"
type: "gene"
col: 6129
ensembl_id: "ENSG00000138119"
name: "myoferlin"
location: "10q23.33"
module: 81
arm: "+"
pooled_cpm: 569.75
n_lines_expressing: 44
n_dd_up: 14
n_dd_down: 27
n_dd_up_clean: 11
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 10
direction_downstream: 17
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# MYOF

*myoferlin* — 10q23.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 1.41× (z +7.6, q 2e-11, up in 30 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.211× (z -33.9, q 0e+00, down in 42 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAV1]] (+0.61, fdr 7e-06), [[TNS3]] (+0.57, fdr 1e-05), [[TGFB2]] (+0.55, fdr 2e-05); moves opposite to [[CRYL1]] (-0.55, fdr 1e-05), [[TMEM158]] (-0.52, fdr 3e-05), [[THBD]] (-0.51, fdr 3e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[ALDH3B1]] → it (grade B ⚠); 17 go from it, the strongest it → [[TNS3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6129.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **1.41×** | +7.6 | 2e-11 | 30/44 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +7.5 | 2e-11 | 28/41 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +6.0 | 5e-07 | 24/39 (SW48, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **1.30×** | +5.9 | 5e-07 | 25/43 (A549, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.27×** | +5.2 | 2e-05 | 23/43 (COLO 205, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[RMC-6236 (drug)]] 5 µM |  | **1.58×** | +5.0 | 5e-05 | 30/42 (AsPC-1, A549, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.25×** | +4.9 | 6e-05 | 22/43 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.26×** | +4.7 | 2e-04 | 22/42 (AsPC-1, HOP62, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.21×** | +4.7 | 2e-04 | 20/42 (HOP62, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.53×** | +4.7 | 2e-04 | 28/44 (AsPC-1, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.23×** | +4.6 | 2e-04 | 25/41 (HOP62, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.52×** | +4.6 | 2e-04 | 22/43 (HS-578T, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.19× | +4.3 | 8e-04 | 21/42 (A549, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +4.0 | 0.003 | 16/42 (HOP62, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.19× | +3.5 | 0.016 | 20/42 (HOP62, NCI-H1573, …) | all doses, flat |  |
| [[Posaconazole (drug)]] 5 µM |  | 1.18× | +3.4 | 0.019 | 18/42 (NCI-H1573, J82, …) | top dose only | plate-row cell shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.18× | +3.4 | 0.019 | 18/42 (A549, NCI-H1573, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6129.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.211×** | -33.9 | 0e+00 | 42/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.213×** | -33.7 | 0e+00 | 42/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.240×** | -31.1 | 0e+00 | 42/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.489×** | -22.1 | 0e+00 | 39/43 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.432×** | -18.3 | 0e+00 | 42/42 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.635×** | -14.0 | 2e-42 | 36/42 (NCI-H2347, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.587×** | -11.6 | 4e-29 | 41/42 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.577×** | -11.5 | 8e-29 | 31/41 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.652×** | -9.3 | 7e-19 | 34/42 (HCT15, LOX-IMVI, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.653×** | -9.3 | 1e-18 | 32/42 (LoVo, Panc 03.27, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.433×** | -9.2 | 2e-18 | 40/43 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.674×** | -8.6 | 4e-16 | 35/42 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.667×** | -8.5 | 9e-16 | 30/42 (SW480, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.680×** | -8.4 | 2e-15 | 33/43 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.692×** | -8.0 | 4e-14 | 36/42 (SW1417, NCI-H2030, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.691×** | -7.6 | 1e-12 | 35/42 (KATO III, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.784×** | -5.3 | 3e-06 | 21/42 (LOX-IMVI, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.786×** | -5.2 | 5e-06 | 25/42 (LoVo, Panc 03.27, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.789×** | -5.2 | 7e-06 | 25/43 (PANC-1, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.847× | -5.1 | 9e-06 | 22/42 (Hs 766T, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.56 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6129. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 366 | 9 (1 ⚠) | 5 | [[Triamcinolone (drug)]] 5 µM 2.00× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.157× (z -21.4) |
| [[LoVo (line)]] | wt | 638 | 0 | 14 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0898× (z -25.5) |
| [[SW480 (line)]] | alt | 366 | 0 | 14 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -31.3) |
| [[PANC-1 (line)]] | alt | 888 | 0 | 11 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0799× (z -39.1) |
| [[SW1417 (line)]] | alt | 674 | 0 | 11 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -24.9) |
| [[A-172 (line)]] | wt | 870 | 0 | 10 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.158× (z -27.8) |
| [[A498 (line)]] | wt | 553 | 0 | 10 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.344× (z -17.3) |
| [[AsPC-1 (line)]] | alt | 683 | 3 (1 ⚠) | 7 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.92× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Elimusertib hydrochloride (drug)]] 0.05 µM 2.25× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.164× (z -21.3) |
| [[J82 (line)]] | alt | 379 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.170× (z -24.9) |
| [[Panc 03.27 (line)]] | alt | 728 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.143× (z -29.0) |
| [[SW 900 (line)]] | alt | 402 | 4 (4 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +16.2) ⚠ cell-cycle shift, explains ~86% of this change | [[Panobinostat (drug)]] 0.5 µM 0.346× (z -13.3) |
| [[A549 (line)]] | wt | 587 | 4 (1 ⚠) | 5 | [[Trametinib (drug)]] 5 µM 2.03× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.217× (z -22.8) |
| [[KATO III (line)]] | alt | 651 | 2 (2 ⚠) | 7 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.78× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.107× (z -26.8) |
| [[BT-474 (line)]] | alt | 473 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.141× (z -22.8) |
| [[H4 (line)]] | wt | 330 | 1 (1 ⚠) | 7 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +15.0) ⚠ cell-cycle shift, explains ~86% of this change | [[Belinostat (drug)]] 5 µM 0.175× (z -14.7) |
| [[HEC-1-A (line)]] | alt | 451 | 1 | 7 (1 ⚠) | [[Trametinib (drug)]] 5 µM 1.68× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.213× (z -26.8) |
| [[LOX-IMVI (line)]] | wt | 363 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -20.6) |
| [[NCI-H2030 (line)]] | alt | 767 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -20.2) |
| [[NCI-H2347 (line)]] | alt | 488 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -22.5) |
| [[SNU-423 (line)]] | alt | 823 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.130× (z -23.8) |
| [[Hs 766T (line)]] | wt | 1,781 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -23.4) |
| [[HS-578T (line)]] | alt | 295 | 1 (1 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +15.1) ⚠ cell-cycle shift, explains ~86% of this change | [[Panobinostat (drug)]] 5 µM 0.293× (z -15.2) |
| [[HT-29 (line)]] | alt | 253 | 1 (1 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +16.2) ⚠ cell-cycle shift, explains ~86% of this change | [[Belinostat (drug)]] 5 µM 0.196× (z -17.5) |
| [[CFPAC-1 (line)]] | alt | 891 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -26.7) |
| [[HCT15 (line)]] | alt | 448 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.189× (z -21.1) |
| [[LS 180 (line)]] | wt | 358 | 1 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.9) ⚠ cell-cycle shift, explains ~86% of this change | [[Panobinostat (drug)]] 5 µM 0.151× (z -20.8) |
| [[MIA PaCa-2 (line)]] | alt | 780 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -22.1) |
| [[NCI-H1573 (line)]] | alt | 771 | 2 | 4 (1 ⚠) | [[Trametinib (drug)]] 5 µM 2.23× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.132× (z -21.7) |
| [[RPMI-7951 (line)]] | alt | 427 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -19.4) |
| [[C32 (line)]] | wt | 324 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 2.76× (z +11.0) ⚠ cell-cycle shift, explains ~97% of this change | [[Panobinostat (drug)]] 5 µM 0.209× (z -17.0) |
| [[COLO 205 (line)]] | alt | 173 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 4.77× (z +14.2) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.217× (z -13.8) |
| [[NCI-H1792 (line)]] | alt | 352 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.5) ⚠ cell-cycle shift, explains ~86% of this change | [[Panobinostat (drug)]] 5 µM 0.228× (z -18.8) |
| [[NCI-H23 (line)]] | alt | 271 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +15.0) ⚠ cell-cycle shift, explains ~86% of this change | [[Belinostat (drug)]] 5 µM 0.249× (z -17.5) |
| [[NCI-H460 (line)]] | wt | 1,401 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -25.7) |
| [[SK-MEL-2 (line)]] | alt | 157 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +10.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.278× (z -13.9) |
| [[SNU-1 (line)]] | wt | 552 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0972× (z -26.5) |
| [[SW48 (line)]] | wt | 226 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +10.8) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.204× (z -15.7) |
| [[AN3 CA (line)]] | alt | 487 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -17.0) |
| [[hTERT-HPNE (line)]] | wt | 404 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -13.7) |
| [[SW 1088 (line)]] | alt | 646 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.127× (z -14.0) |
| [[SW 1271 (line)]] | alt | 341 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -10.7) |
| [[A-427 (line)]] | wt | 108 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 63.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 111 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 59.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 495 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 507 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 83.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 42.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6129), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAV1]] | +0.61 | +0.58 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE; STRING 488 |
| [[TNS3]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[TGFB2]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ADAM9]] | +0.53 | +0.37 / +0.61 | both halves | 8e-05 |  |
| [[TPM1]] | +0.50 | +0.37 / +0.56 | both halves | 7e-05 |  |
| [[CPNE1]] | +0.50 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[RBMS3]] | +0.50 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[LPP]] | +0.50 | +0.37 / +0.53 | both halves | 9e-05 |  |
| [[EFEMP1]] | +0.50 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[TGFBI]] | +0.49 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[LATS2]] | +0.49 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[COL12A1]] | +0.49 | +0.45 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYL1]] | -0.55 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[TMEM158]] | -0.52 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[THBD]] | -0.51 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[SH2D2A]] | -0.50 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[CSNK1E]] | -0.50 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[GSTO1]] | -0.49 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[CORO2B]] | -0.48 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[ZNF549]] | -0.48 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[STC1]] | -0.48 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[MMP1]] | -0.48 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[ABTB3]] | -0.48 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[FAM89A]] | -0.48 | -0.42 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALDH3B1]] | B | ALDH3B1 activity raises MYOF's level | lines that do not express ALDH3B1 (9) vs lines expressing it (41) | 2.82× lower at baseline in the lines without ALDH3B1 | 0.007 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[TNS3]] | B | TNS3 activity raises MYOF's level | lines that do not express TNS3 (8) vs lines expressing it (42) | 2.79× lower at baseline in the lines without TNS3 | 0.018 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |
| [[CREG2]] | B | CREG2 activity raises MYOF's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 1.86× lower at baseline in the lines without CREG2 | 0.033 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[MET]] | B | MET activity raises MYOF's level | lines that do not express MET (9) vs lines expressing it (41) | 2.21× lower at baseline in the lines without MET | 0.052 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[MAP2K1]] | B | MAP2K1 activity lowers MYOF's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CAV1]] | B | CAV1 activity raises MYOF's level | lines that do not express CAV1 (13) vs lines expressing it (37) | 2.28× lower at baseline in the lines without CAV1 | 0.059 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, MDFIC, CACNG6 |
| [[THBD]] | B | THBD activity raises MYOF's level | lines that do not express THBD (28) vs lines expressing it (22) | 1.99× lower at baseline in the lines without THBD | 0.062 | ⚠ within organs, on part of the lines; also absent: EFEMP1, KRT7, LINC02742 |
| [[EFEMP1]] | B | EFEMP1 activity raises MYOF's level | lines that do not express EFEMP1 (31) vs lines expressing it (19) | 1.87× lower at baseline in the lines without EFEMP1 | 0.079 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, IL31RA |
| [[CAV2]] | C | CAV2 activity raises MYOF's level | lines that do not express CAV2 (8) vs lines expressing it (42) | 3.17× lower at baseline in the lines without CAV2 | 0.048 | ⚠ within organs, on part of the lines; co-absent genes; also absent: PLAUR, LRRK1, HRH1; maybe low, not absent; co-absent with the target |
| [[BCL9L]] | C | BCL9L activity raises MYOF's level | lines that do not express BCL9L (3) vs lines expressing it (47) | 3.26× lower at baseline in the lines without BCL9L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with SMAD3; also absent: UACA, MYH16, PER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 16, C 1. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNS3]] | B | MYOF activity raises TNS3's level | lines that do not express MYOF (6) vs lines expressing it (44) | 3.32× lower at baseline in the lines without MYOF | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2 |
| [[ANXA2]] | B | MYOF activity raises ANXA2's level | lines that do not express MYOF (6) vs lines expressing it (44) | 2.86× lower at baseline in the lines without MYOF | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2 |
| [[SYTL2]] | B | MYOF activity raises SYTL2's level | lines that do not express MYOF (6) vs lines expressing it (44) | 3.65× lower at baseline in the lines without MYOF | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2 |
| [[ALDH3B1]] | B | MYOF activity raises ALDH3B1's level | lines that do not express MYOF (6) vs lines expressing it (44) | 2.81× lower at baseline in the lines without MYOF | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2 |
| [[ARPC5L]] | B | MYOF activity lowers ARPC5L's level | lines that do not express MYOF (6) vs lines expressing it (44) | 1.28× higher at baseline in the lines without MYOF | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2 |
| [[PARVA]] | B | MYOF activity raises PARVA's level | lines that do not express MYOF (6) vs lines expressing it (44) | 3.32× lower at baseline in the lines without MYOF | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2 |
| [[CAV1]] | B | MYOF activity raises CAV1's level | lines that do not express MYOF (6) vs lines expressing it (44) | 5.43× lower at baseline in the lines without MYOF | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2 |
| [[UQCRH]] | B | MYOF activity lowers UQCRH's level | lines that do not express MYOF (6) vs lines expressing it (44) | 1.28× higher at baseline in the lines without MYOF | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2 |
| [[IL17RA]] | B | MYOF activity strengthens IL17RA's drug response | lines that do not express MYOF (6) vs lines expressing it (43) | the lines without MYOF respond 0.41× as strongly (z diff +2.02); strongest at Dinaciclib 5 µM: 1.16x vs 0.57x (z diff +4.6) | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2; target measured in part of the lines; artifact flags |
| [[ORAI1]] | B | MYOF activity lowers ORAI1's level | lines that do not express MYOF (6) vs lines expressing it (44) | 1.29× higher at baseline in the lines without MYOF | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2 |
| [[BCL9L]] | B | MYOF activity raises BCL9L's level | lines that do not express MYOF (6) vs lines expressing it (44) | 2.34× lower at baseline in the lines without MYOF | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2; its own permutation p |
| [[DIO2]] | B | MYOF activity raises DIO2's level | lines that do not express MYOF (6) vs lines expressing it (44) | 1.57× lower at baseline in the lines without MYOF | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2 |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction -0.432). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.7, 16.2); signed map (50.1, 14.0). **Vector** length 139, 51.5% of its response variance represented; |z| ≥ 3 in 2,108 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +9.1 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | +7.7 | +2.4 |
|  | [[Trametinib (drug)]] 5 µM |  | +6.5 | +7.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.9 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +5.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +5.4 | +4.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.3 | +4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.8 | +4.9 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +4.6 | +4.6 |
| fall | [[Tucidinostat (drug)]] 0.5 µM |  | -8.1 | -8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -8.0 | -14.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -6.0 | -9.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.6 | -5.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.4 | -11.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -5.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.0 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -9.3 |

## What is on record

|  |  |
|---|---|
| Name | myoferlin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.33 — chr10:93,306,429-93,482,334 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1207; previously FER1L3 |
| Gene groups (HGNC) | Ferlin family |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZM1](https://www.uniprot.org/uniprotkb/Q9NZM1) (Myoferlin):

> Calcium/phospholipid-binding protein that plays a role in the plasmalemma repair mechanism of endothelial cells that permits rapid resealing of membranes disrupted by mechanical stress. Involved in endocytic recycling. Implicated in VEGF signal transduction by regulating the levels of the receptor KDR (By similarity).

**Summary**, from NCBI Gene [26509](https://www.ncbi.nlm.nih.gov/gene/26509):

> Mutations in dysferlin, a protein associated with the plasma membrane, can cause muscle weakness that affects both proximal and distal muscles. The protein encoded by this gene is a type II membrane protein that is structurally similar to dysferlin. It is a member of the ferlin family and associates with both plasma and nuclear membranes. The protein contains C2 domains that play a role in calcium-mediated membrane fusion events, suggesting that it may be involved in membrane regeneration and …

**Accessions** — [HGNC:3656](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3656) · Entrez [26509](https://www.ncbi.nlm.nih.gov/gene/26509) · UniProt [Q9NZM1](https://www.uniprot.org/uniprotkb/Q9NZM1) · Ensembl [ENSG00000138119](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138119)

## Data

Gene col 6129: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6129); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6129, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6129]; `tensor/DDL_lfc|DDL_z.npy` [6129]; `embed/gene_vectors.npy` [6129]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6129 or target_col == 6129). Every well: [[MYOF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYOF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
