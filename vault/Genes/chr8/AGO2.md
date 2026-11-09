---
symbol: "AGO2"
type: "gene"
col: 4464
ensembl_id: "ENSG00000123908"
name: "argonaute RISC catalytic component 2"
location: "8q24.3"
module: 92
arm: "+"
pooled_cpm: 244.03
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 35
n_dd_up_clean: 10
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# AGO2

*argonaute RISC catalytic component 2* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.75× (z +17.3, q 0e+00, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.387× (z -20.8, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABR]] (+0.74, fdr 7e-06), [[SPRY4-AS1]] (+0.73, fdr 7e-06), [[CCND1]] (+0.69, fdr 7e-06); moves opposite to [[CAT]] (-0.66, fdr 7e-06), [[SCPEP1]] (-0.66, fdr 7e-06), [[TENT2]] (-0.66, fdr 1e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4464.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +17.3 | 0e+00 | 36/48 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +11.5 | 6e-28 | 37/48 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +10.9 | 1e-25 | 39/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +10.7 | 2e-24 | 37/48 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +9.8 | 1e-20 | 42/48 (Panc 03.27, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.50×** | +8.9 | 4e-17 | 41/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +7.8 | 5e-13 | 39/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +5.9 | 3e-07 | 32/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +5.5 | 2e-06 | 28/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.24×** | +4.8 | 9e-05 | 27/48 (SHP-77, PANC-1, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.59×** | +4.5 | 3e-04 | 31/48 (HEC-1-A, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.21×** | +4.2 | 0.001 | 23/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.20× | +4.0 | 0.003 | 19/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +3.8 | 0.005 | 20/48 (A498, HOP62, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.006 | 26/48 (SHP-77, NCI-H2347, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4464.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.387×** | -20.8 | 0e+00 | 48/48 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.406×** | -19.7 | 0e+00 | 48/48 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.492×** | -15.5 | 0e+00 | 48/48 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.640×** | -9.4 | 1e-18 | 38/47 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.655×** | -9.2 | 2e-18 | 34/49 (RKO, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.675×** | -9.2 | 2e-18 | 38/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.645×** | -9.2 | 2e-18 | 39/47 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.680×** | -9.2 | 2e-18 | 38/50 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.682×** | -8.6 | 3e-16 | 40/49 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.673×** | -8.6 | 3e-16 | 40/49 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.678×** | -8.2 | 2e-14 | 31/44 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.686×** | -7.9 | 1e-13 | 41/48 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.718×** | -7.4 | 8e-12 | 35/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.772×** | -7.3 | 1e-11 | 33/49 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.722×** | -7.1 | 4e-11 | 33/47 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.729×** | -6.9 | 2e-10 | 34/48 (H4, KATO III, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.808×** | -6.5 | 4e-09 | 30/48 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.724×** | -6.0 | 6e-08 | 35/48 (SW480, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4464. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 227 | 1 | 16 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.12× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -17.5) |
| [[NCI-H460 (line)]] | wt | 128 | 14 (4 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +15.6) | [[Panobinostat (drug)]] 0.5 µM 0.506× (z -9.4) |
| [[RKO (line)]] | wt | 757 | 0 | 16 (6 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.381× (z -18.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.302× (z -15.8) |
| [[AsPC-1 (line)]] | alt | 439 | 1 | 14 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +14.9) | [[Panobinostat (drug)]] 0.5 µM 0.383× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 163 | 2 | 13 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +17.5) | [[Panobinostat (drug)]] 5 µM 0.376× (z -12.6) |
| [[HEC-1-A (line)]] | alt | 222 | 0 | 13 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -17.6) |
| [[HOP62 (line)]] | alt | 205 | 8 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +28.4) | [[Panobinostat (drug)]] 0.5 µM 0.401× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 697 | 2 | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.63× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.259× (z -12.4) |
| [[A549 (line)]] | wt | 293 | 4 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.299× (z -16.7) |
| [[SK-MEL-2 (line)]] | alt | 235 | 0 | 9 | — | [[Panobinostat (drug)]] 0.5 µM 0.311× (z -15.4) |
| [[A498 (line)]] | wt | 166 | 5 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +21.8) | [[Panobinostat (drug)]] 5 µM 0.457× (z -12.3) |
| [[HS-578T (line)]] | alt | 220 | 6 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +27.4) | [[Panobinostat (drug)]] 5 µM 0.418× (z -11.1) |
| [[PANC-1 (line)]] | alt | 212 | 4 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +21.9) | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -20.4) |
| [[NCI-H2347 (line)]] | alt | 246 | 2 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -17.8) |
| [[SW 900 (line)]] | alt | 267 | 1 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.16× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.336× (z -12.5) |
| [[J82 (line)]] | alt | 190 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.400× (z -13.5) |
| [[MIA PaCa-2 (line)]] | alt | 231 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.171× (z -25.5) |
| [[NCI-H1792 (line)]] | alt | 164 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +16.6) | [[Panobinostat (drug)]] 5 µM 0.426× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 279 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -27.7) |
| [[A-172 (line)]] | wt | 133 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +16.9) | [[Panobinostat (drug)]] 0.5 µM 0.405× (z -10.6) |
| [[C32 (line)]] | wt | 212 | 1 | 4 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.09× (z +9.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.375× (z -12.1) ⚠ toxic · without an alert: [[Binimetinib (drug)]] 5 µM 0.468× (z -9.1) |
| [[COLO 205 (line)]] | alt | 187 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +15.9) | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 353 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -18.9) |
| [[hTERT-HPNE (line)]] | wt | 138 | 3 | 2 | [[Harringtonine (drug)]] 5 µM 4.59× (z +14.5) | [[Panobinostat (drug)]] 5 µM 0.343× (z -10.6) |
| [[KATO III (line)]] | alt | 190 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.8) | [[Selinexor (drug)]] 5 µM 0.534× (z -11.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.503× (z -8.8) |
| [[LoVo (line)]] | wt | 201 | 1 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.76× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.293× (z -19.6) |
| [[NCI-H2030 (line)]] | alt | 375 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -14.3) |
| [[Panc 03.27 (line)]] | alt | 241 | 2 | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.30× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.385× (z -14.2) |
| [[SNU-1 (line)]] | wt | 158 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.372× (z -11.3) |
| [[Hs 766T (line)]] | wt | 179 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +20.3) | — |
| [[HT-29 (line)]] | alt | 503 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.447× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 262 | 1 | 3 | [[Homoharringtonine (drug)]] 0.5 µM 1.95× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.413× (z -11.7) |
| [[LS 180 (line)]] | wt | 206 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -12.9) |
| [[SNU-423 (line)]] | alt | 112 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +21.4) | [[Panobinostat (drug)]] 5 µM 0.394× (z -11.2) |
| [[A-427 (line)]] | wt | 160 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.205× (z -20.8) |
| [[C-33 A (line)]] | alt | 214 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -18.8) |
| [[H4 (line)]] | wt | 134 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +15.7) | [[Ponatinib (drug)]] 5 µM 0.350× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 140 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.3) | — |
| [[SHP-77 (line)]] | alt | 199 | 1 (1 ⚠) | 2 | [[Daptomycin (drug)]] 5 µM 1.98× (z +8.8) ⚠ unreliable plate only | [[Panobinostat (drug)]] 5 µM 0.460× (z -10.0) |
| [[SW48 (line)]] | wt | 293 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.195× (z -18.5) |
| [[AN3 CA (line)]] | alt | 199 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.294× (z -10.6) |
| [[BT-474 (line)]] | alt | 331 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +14.8) | — |
| [[HCT15 (line)]] | alt | 268 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -12.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 254 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.453× (z -13.0) |
| [[CHP-212 (line)]] | wt | 156 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 269 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 181 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4464), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABR]] | +0.74 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[SPRY4-AS1]] | +0.73 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[CCND1]] | +0.69 | +0.76 / +0.61 | both halves | 7e-06 | pathway: Co-inhibition by PD-1; STRING 728 |
| [[MSRA]] | +0.68 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[SPRY4]] | +0.67 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[TNFRSF12A]] | +0.66 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[LINC01844]] | +0.65 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[LTBP2]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 | pathway: Signaling by TGFB family members |
| [[ADGRL4]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[DUSP5-DT]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[MCL1]] | +0.64 | +0.63 / +0.63 | both halves | 7e-06 | pathway: Signaling by ALK fusions and activated point mutants; STRING 465 |
| [[NEK10]] | +0.64 | +0.53 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAT]] | -0.66 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[SCPEP1]] | -0.66 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[TENT2]] | -0.66 | -0.65 / -0.55 | both halves | 1e-05 | STRING 463 |
| [[COPS4]] | -0.63 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[CRYZL1]] | -0.63 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[USP30]] | -0.62 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[JKAMP]] | -0.61 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[ARNT]] | -0.61 | -0.51 / -0.52 | both halves | 1e-05 | pathway: Transcriptional Regulation by NPAS4 |
| [[ALG9]] | -0.60 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[PKIG]] | -0.60 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[DNASE2]] | -0.59 | -0.57 / -0.57 | both halves | 9e-06 |  |
| [[SNX4]] | -0.59 | -0.50 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises AGO2's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 5.3% of all compounds | 0.019 | ⚠ off-target possible; 4 compounds |
| [[MBP]] | B | MBP activity raises AGO2's level | lines that do not express MBP (9) vs lines expressing it (41) | 1.54× lower at baseline in the lines without MBP | 0.056 | ⚠ within organs, on part of the lines; co-occurs with PTEN; also absent: RHPN1, CHMP4C, EVPL |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.725). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.3, 8.5); signed map (10.3, 44.0). **Vector** length 131, 51.9% of its response variance represented; |z| ≥ 3 in 1,948 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MAPK output* (control, mean cos +0.55 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.8 | +9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.9 | +11.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.9 | +17.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.8 | +5.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.6 | +10.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.6 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.2 | +3.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +4.1 | +4.5 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -8.8 | -9.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -8.7 | -9.2 |
|  | [[NG25 (drug)]] 5 µM |  | -8.0 | -4.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -7.9 | -8.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -7.5 | -8.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -7.4 | -9.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -7.3 | -7.9 |

## What is on record

|  |  |
|---|---|
| Name | argonaute RISC catalytic component 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:140,520,156-140,635,633 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hAGO2, Q10, LINC00980; previously EIF2C2, CASC7 |
| Gene groups (HGNC) | Endoribonucleases; RISC loading complex subunits; Argonaute RISC component family |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 65 pathways, smallest: Post-transcriptional silencing by small RNAs; Regulation of NPAS4 mRNA translation; Regulation of CDH11 mRNA translation by microRNAs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKV8](https://www.uniprot.org/uniprotkb/Q9UKV8) (Protein argonaute-2):

> Required for RNA-mediated gene silencing (RNAi) by the RNA-induced silencing complex (RISC). The 'minimal RISC' appears to include AGO2 bound to a short guide RNA such as a microRNA (miRNA) or short interfering RNA (siRNA). These guide RNAs direct RISC to complementary mRNAs that are targets for RISC-mediated gene silencing. The precise mechanism of gene silencing depends on the degree of complementarity between the miRNA or siRNA and its target. Binding of RISC to a perfectly complementary …

**Summary**, from NCBI Gene [27161](https://www.ncbi.nlm.nih.gov/gene/27161):

> This gene encodes a member of the Argonaute family of proteins which play a role in RNA interference. The encoded protein is highly basic, and contains a PAZ domain and a PIWI domain. It may interact with dicer1 and play a role in short-interfering-RNA-mediated gene silencing. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:3263](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3263) · Entrez [27161](https://www.ncbi.nlm.nih.gov/gene/27161) · UniProt [Q9UKV8](https://www.uniprot.org/uniprotkb/Q9UKV8) · Ensembl [ENSG00000123908](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123908)

## Data

Gene col 4464: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4464); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4464, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4464]; `tensor/DDL_lfc|DDL_z.npy` [4464]; `embed/gene_vectors.npy` [4464]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4464 or target_col == 4464). Every well: [[AGO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
