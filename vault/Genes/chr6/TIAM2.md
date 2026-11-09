---
symbol: "TIAM2"
type: "gene"
col: 7095
ensembl_id: "ENSG00000146426"
name: "TIAM Rac1 associated GEF 2"
location: "6q25.2-q25.3"
module: 39
arm: "+"
pooled_cpm: 101.55
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 18
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# TIAM2

*TIAM Rac1 associated GEF 2* — 6q25.2-q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.92× (z +14.1, q 1e-42, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (15 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.538× (z -9.5, q 1e-18, down in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.581× (z -8.3, q 1e-14, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00486]] (+0.79, fdr 7e-06), [[C3orf20]] (+0.78, fdr 7e-06), [[SCUBE2]] (+0.75, fdr 7e-06); moves opposite to [[PMS2P3-1]] (-0.67, fdr 1e-05), [[GMCL1]] (-0.66, fdr 1e-05), [[SNHG30]] (-0.65, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[FSIP2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7095.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +14.1 | 1e-42 | 45/48 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +8.1 | 2e-13 | 39/48 (HS-578T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.29×** | +5.4 | 1e-05 | 35/48 (SW1417, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **1.38×** | +4.9 | 1e-04 | 37/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +4.7 | 3e-04 | 33/48 (J82, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.37×** | +4.6 | 5e-04 | 34/47 (A-172, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.005 | 27/48 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.63×** | +3.9 | 0.007 | 34/49 (LoVo, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.011 | 26/47 (A-172, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.26×** | +3.5 | 0.025 | 25/48 (HT-29, LoVo, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.025 | 22/47 (A-172, J82, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.031 | 22/50 (A-172, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.048 | 23/48 (KATO III, A498, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.085 | 19/48 (A-172, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.085 | 16/48 (LoVo, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 15 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7095.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.538×** | -9.5 | 1e-18 | 45/48 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.529×** | -9.4 | 2e-18 | 41/47 (MIA PaCa-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **0.570×** | -8.6 | 2e-15 | 33/49 (A-172, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.581×** | -8.3 | 1e-14 | 44/48 (KATO III, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.683×** | -8.2 | 2e-14 | 35/49 (PANC-1, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.600×** | -7.8 | 5e-13 | 41/48 (SK-MEL-2, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **0.590×** | -7.8 | 7e-13 | 28/44 (NCI-H1792, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.654×** | -6.5 | 5e-09 | 38/48 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.654×** | -6.5 | 5e-09 | 32/48 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.645×** | -6.2 | 3e-08 | 28/45 (A-427, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.703×** | -5.4 | 4e-06 | 33/48 (SK-MEL-2, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **0.722×** | -5.0 | 3e-05 | 32/48 (PANC-1, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.767×** | -3.9 | 0.004 | 25/48 (SNU-423, NCI-H23, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.788×** | -3.6 | 0.012 | 23/48 (MIA PaCa-2, HT-29, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.642×** | -3.6 | 0.014 | 23/49 (HEC-1-A, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.811×** | -3.2 | 0.044 | 24/48 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.51 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7095. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 135 | 1 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +13.4) | [[Panobinostat (drug)]] 5 µM 0.267× (z -13.6) ⚠ cell-cycle shift, explains ~83% of this change |
| [[SK-MEL-2 (line)]] | alt | 171 | 1 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +16.4) | [[Panobinostat (drug)]] 0.5 µM 0.270× (z -13.9) ⚠ cell-cycle shift, explains ~57% of this change |
| [[HepG2_C3A (line)]] | wt | 243 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[KATO III (line)]] | alt | 75.4 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +13.9) | [[Panobinostat (drug)]] 0.5 µM 0.346× (z -9.9) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.358× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 166 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.0846× (z -24.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.443× (z -8.5) |
| [[PANC-1 (line)]] | alt | 153 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[SW480 (line)]] | alt | 115 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.348× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[HEC-1-A (line)]] | alt | 146 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.295× (z -11.6) ⚠ cell-cycle shift, explains ~83% of this change |
| [[NCI-H1573 (line)]] | alt | 91.4 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.262× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[SNU-1 (line)]] | wt | 144 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.205× (z -13.2) ⚠ toxic |
| [[A-172 (line)]] | wt | 120 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[HT-29 (line)]] | alt | 73.1 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.0) | [[Belinostat (drug)]] 5 µM 0.306× (z -11.2) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SNU-423 (line)]] | alt | 166 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +13.8) | [[Dinaciclib (drug)]] 0.05 µM 0.353× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[A498 (line)]] | wt | 69.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.71× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.375× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[AsPC-1 (line)]] | alt | 90.2 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.335× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[C32 (line)]] | wt | 104 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.91× (z +11.8) | — |
| [[J82 (line)]] | alt | 159 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +20.0) | — |
| [[LoVo (line)]] | wt | 121 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +12.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.406× (z -9.7) ⚠ toxic |
| [[RKO (line)]] | wt | 68.2 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.244× (z -9.7) ⚠ cell-cycle shift, explains ~50% of this change |
| [[RPMI-7951 (line)]] | alt | 149 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +14.1) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -8.7) ⚠ cell-cycle shift, explains ~82% of this change |
| [[AN3 CA (line)]] | alt | 213 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[HCT15 (line)]] | alt | 111 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +14.3) | — |
| [[Hs 766T (line)]] | wt | 52.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[HS-578T (line)]] | alt | 123 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +18.9) | — |
| [[LS 180 (line)]] | wt | 80.4 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.337× (z -9.7) ⚠ cell-cycle shift, explains ~57% of this change |
| [[NCI-H23 (line)]] | alt | 91.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +15.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.367× (z -9.6) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 57.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +13.3) | — |
| [[SW 900 (line)]] | alt | 91.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.202× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[SW48 (line)]] | wt | 107 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +8.6) | [[Belinostat (drug)]] 0.5 µM 0.255× (z -9.4) |
| [[A-427 (line)]] | wt | 81.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[A549 (line)]] | wt | 74.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.410× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[C-33 A (line)]] | alt | 97.6 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.337× (z -8.6) |
| [[H4 (line)]] | wt | 92.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.281× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 95.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 103 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.12× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 89.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.184× (z -14.9) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 95.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 31.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.3) | — |
| [[NCI-H596 (line)]] | alt | 96.8 | 1 | 0 | [[Atazanavir (sulfate) (drug)]] 0.05 µM 3.22× (z +9.1) | — |
| [[SW 1088 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.0903× (z -9.1) ⚠ transcription drop |
| [[BT-474 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 58.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7095), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00486]] | +0.79 | +0.85 / +0.60 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.78 | +0.86 / +0.63 | both halves | 7e-06 |  |
| [[SCUBE2]] | +0.75 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[SLC22A1]] | +0.75 | +0.82 / +0.68 | both halves | 7e-06 |  |
| [[CFAP70]] | +0.73 | +0.83 / +0.52 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | +0.72 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[BPTF]] | +0.71 | +0.80 / +0.56 | both halves | 1e-05 |  |
| [[MTNR1A]] | +0.70 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[ZMYM4]] | +0.70 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[LINC01191]] | +0.70 | +0.75 / +0.57 | both halves | 1e-05 |  |
| [[USP50]] | +0.70 | +0.81 / +0.49 | both halves | 1e-05 |  |
| [[LZIC]] | +0.69 | +0.75 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2P3-1]] | -0.67 | -0.73 / -0.53 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.66 | -0.70 / -0.49 | both halves | 1e-05 |  |
| [[SNHG30]] | -0.65 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[IDH2]] | -0.63 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[UBTD1]] | -0.63 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[MLEC]] | -0.63 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[POGLUT2]] | -0.63 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[IFI27L1]] | -0.62 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[SDHAP4]] | -0.62 | -0.70 / -0.40 | both halves | 5e-05 |  |
| [[PIGF]] | -0.61 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[SHQ1]] | -0.61 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[ABHD12]] | -0.61 | -0.62 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises TIAM2's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.49× lower at baseline in the lines without FSIP2-AS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[SCUBE2]] | B | SCUBE2 activity raises TIAM2's level | lines that do not express SCUBE2 (7) vs lines expressing it (43) | 1.56× lower at baseline in the lines without SCUBE2 | 0.080 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises TIAM2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ITPR2-AS1]] | C | ITPR2-AS1 activity raises TIAM2's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 1.79× lower at baseline in the lines without ITPR2-AS1 | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.717). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.0, -10.7); signed map (21.5, 4.4). **Vector** length 121, 39.3% of its response variance represented; |z| ≥ 3 in 1,191 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +14.4 | +14.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +13.8 | +8.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +10.1 | +4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.6 | +4.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +7.2 | +5.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +5.9 | +4.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +5.8 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.8 | +2.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.9 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | -1.9 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.8 | -8.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -5.3 | -9.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -4.1 | -7.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.8 | -5.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.7 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.6 | -3.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.3 | -1.1 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -2.6 | -1.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | TIAM Rac1 associated GEF 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.2-q25.3 — chr6:154,832,697-155,257,723 (+) |
| Ensembl biotype | protein_coding |
| Also known as | STEF |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs; PDZ domain containing |
| Reactome | 14 pathways, smallest: NRAGE signals death through JNK; G alpha (12/13) signalling events; Cell death signalling via NRAGE, NRIF and NADE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVF5](https://www.uniprot.org/uniprotkb/Q8IVF5) (Rho guanine nucleotide exchange factor TIAM2):

> Modulates the activity of RHO-like proteins and connects extracellular signals to cytoskeletal activities. Acts as a GDP-dissociation stimulator protein that stimulates the GDP-GTP exchange activity of RHO-like GTPases and activates them. Mediates extracellular laminin signals to activate Rac1, contributing to neurite growth. Involved in lamellipodial formation and advancement of the growth cone of embryonic hippocampal neurons. Promotes migration of neurons in the cerebral cortex. When …

**Summary**, from NCBI Gene [26230](https://www.ncbi.nlm.nih.gov/gene/26230):

> This gene encodes a guanine nucleotide exchange factor. A highly similar mouse protein specifically activates ras-related C3 botulinum substrate 1, converting this Rho-like guanosine triphosphatase (GTPase) from a guanosine diphosphate-bound inactive state to a guanosine triphosphate-bound active state. The encoded protein may play a role in neural cell development. Alternatively spliced transcript variants encoding different isoforms have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11806](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11806) · Entrez [26230](https://www.ncbi.nlm.nih.gov/gene/26230) · UniProt [Q8IVF5](https://www.uniprot.org/uniprotkb/Q8IVF5) · Ensembl [ENSG00000146426](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146426)

## Data

Gene col 7095: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7095); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7095, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7095]; `tensor/DDL_lfc|DDL_z.npy` [7095]; `embed/gene_vectors.npy` [7095]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7095 or target_col == 7095). Every well: [[TIAM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIAM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
