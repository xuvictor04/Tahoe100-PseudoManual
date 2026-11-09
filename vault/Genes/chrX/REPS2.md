---
symbol: "REPS2"
type: "gene"
col: 9866
ensembl_id: "ENSG00000169891"
name: "RALBP1 associated Eps domain containing 2"
location: "Xp22.2"
module: 69
arm: "+"
pooled_cpm: 26.15
n_lines_expressing: 38
n_dd_up: 23
n_dd_down: 37
n_dd_up_clean: 21
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 2
direction_downstream: 7
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# REPS2

*RALBP1 associated Eps domain containing 2* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.55× (z +9.4, q 5e-18, up in 21 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (14 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.195× (z -24.6, q 0e+00, down in 35 of 35 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.167× (z -13.9, q 1e-41, down in 32 of 34 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO25]] (+0.65, fdr 3e-05), [[INSR]] (+0.65, fdr 1e-05), [[CBLB]] (+0.65, fdr 7e-06); moves opposite to [[TAF2]] (-0.52, fdr 2e-05), [[RPTOR]] (-0.51, fdr 2e-05), [[AFG1L]] (-0.51, fdr 5e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); 7 go from it, the strongest it → [[LINC01881]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9866.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +9.4 | 5e-18 | 21/36 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.75×** | +8.5 | 7e-15 | 25/36 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +8.1 | 8e-14 | 24/36 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +7.8 | 9e-13 | 26/35 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +7.0 | 2e-10 | 24/36 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +6.4 | 2e-08 | 21/35 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.05×** | +5.6 | 2e-06 | 19/36 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.39×** | +5.0 | 4e-05 | 16/34 (NCI-H1792, A498, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 5 µM |  | **1.24×** | +4.6 | 3e-04 | 14/36 (KATO III, LoVo, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.31×** | +3.9 | 0.007 | 12/36 (LoVo, BT-474, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.62×** | +3.7 | 0.010 | 10/36 (LoVo, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.014 | 12/35 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.28×** | +3.5 | 0.017 | 10/36 (SHP-77, BT-474, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.029 | 12/35 (NCI-H1792, HOP62, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.54×** | +3.4 | 0.029 | 11/36 (LoVo, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.035 | 10/35 (NCI-H1792, A498, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9866.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.195×** | -24.6 | 0e+00 | 35/35 (SW1417, NCI-H2347, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.167×** | -13.9 | 1e-41 | 32/34 (SW1417, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.217×** | -11.9 | 4e-30 | 32/35 (SW1417, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.496×** | -10.6 | 7e-24 | 31/35 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.262×** | -10.4 | 2e-23 | 33/34 (Panc 03.27, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.264×** | -10.3 | 4e-23 | 32/34 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.510×** | -10.1 | 3e-22 | 26/35 (HEC-1-A, HOP62, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.281×** | -9.9 | 5e-21 | 29/34 (SW1417, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.514×** | -9.6 | 4e-20 | 32/36 (HEC-1-A, A498, …) | all doses, stronger at high dose | composition shift |
| [[EX229 (drug)]] 0.05 µM |  | **0.529×** | -9.0 | 9e-18 | 30/36 (LoVo, SW48, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.317×** | -8.9 | 2e-17 | 28/36 (Panc 03.27, KATO III, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.540×** | -8.6 | 4e-16 | 23/29 (LoVo, HEC-1-A, …) | inconsistent across doses | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.569×** | -8.5 | 9e-16 | 30/35 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.607×** | -7.5 | 2e-12 | 28/35 (HT-29, HOP62, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.443×** | -7.4 | 5e-12 | 31/36 (SW1417, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.409×** | -6.9 | 1e-10 | 30/33 (SW1417, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.670×** | -6.0 | 5e-08 | 23/36 (HEC-1-A, HS-578T, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.681×** | -5.8 | 2e-07 | 19/36 (A-427, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~23% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9866. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 115 | 0 | 11 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.109× (z -21.1) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0974× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 49.1 | 0 | 10 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0937× (z -21.8) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.277× (z -11.8) |
| [[KATO III (line)]] | alt | 80.0 | 0 | 9 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.122× (z -19.4) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.0977× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 28.6 | 0 | 9 (8 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.139× (z -11.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.219× (z -9.1) |
| [[SW1417 (line)]] | alt | 57.7 | 0 | 9 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0823× (z -22.5) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0568× (z -13.3) |
| [[HEC-1-A (line)]] | alt | 22.4 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0902× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.144× (z -14.3) |
| [[HS-578T (line)]] | alt | 36.0 | 0 | 7 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0737× (z -17.6) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.207× (z -10.6) |
| [[A498 (line)]] | wt | 29.7 | 2 | 4 (4 ⚠) | [[Triamcinolone (drug)]] 5 µM 2.38× (z +8.8) | [[Harringtonine (drug)]] 5 µM 0.161× (z -12.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LoVo (line)]] | wt | 36.8 | 0 | 5 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0695× (z -20.6) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.254× (z -10.0) |
| [[A-427 (line)]] | wt | 24.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -10.3) |
| [[SHP-77 (line)]] | alt | 18.0 | 0 | 4 (2 ⚠) | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0826× (z -13.1) |
| [[SW480 (line)]] | alt | 18.2 | 0 | 4 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.106× (z -17.3) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.263× (z -10.3) |
| [[HT-29 (line)]] | alt | 51.8 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0968× (z -19.6) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.131× (z -8.8) |
| [[A-172 (line)]] | wt | 17.8 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0934× (z -12.3) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 49.2 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.148× (z -14.1) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0499× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 35.7 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.258× (z -10.7) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0902× (z -9.9) |
| [[HCT15 (line)]] | alt | 20.4 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0914× (z -11.6) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 24.5 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.226× (z -11.0) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.305× (z -8.8) |
| [[J82 (line)]] | alt | 32.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[LS 180 (line)]] | wt | 25.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[NCI-H1792 (line)]] | alt | 64.1 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0926× (z -18.6) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0841× (z -10.0) |
| [[PANC-1 (line)]] | alt | 6.56 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.73× (z +9.7) | [[Harringtonine (drug)]] 5 µM 0.163× (z -9.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SNU-423 (line)]] | alt | 52.8 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0834× (z -18.7) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.0924× (z -9.2) |
| [[SW 900 (line)]] | alt | 28.6 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.161× (z -11.1) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 17.7 | 0 | 2 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.105× (z -9.0) ⚠ transcription drop · without an alert: [[EX229 (drug)]] 0.05 µM 0.101× (z -8.7) |
| [[A549 (line)]] | wt | 12.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.127× (z -9.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[AsPC-1 (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0831× (z -15.3) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 51.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.200× (z -11.7) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 9.46 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0825× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.208× (z -8.7) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 7.45 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.101× (z -9.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0908× (z -12.4) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 5.39 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.95 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.30 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.52 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.13 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.80 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.85 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.40 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.57 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.67 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.40 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9866), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO25]] | +0.65 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[INSR]] | +0.65 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[CBLB]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[LINC01881]] | +0.63 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[HECA]] | +0.62 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[YPEL2]] | +0.60 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[SPSB3]] | +0.59 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[CCDC28A]] | +0.59 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[IRS2]] | +0.58 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[KLHL24]] | +0.57 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[PLAG1]] | +0.56 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[MTURN]] | +0.56 | +0.47 / +0.66 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF2]] | -0.52 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[RPTOR]] | -0.51 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[AFG1L]] | -0.51 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[DNAJC11]] | -0.49 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[KRR1]] | -0.49 | -0.45 / -0.43 | both halves | 4e-05 |  |
| [[ZNF629]] | -0.48 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[LANCL2]] | -0.48 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[AMMECR1]] | -0.48 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[TACO1]] | -0.48 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[MED1]] | -0.47 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[LYRM2]] | -0.46 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[ZNF346]] | -0.46 | -0.54 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers REPS2's level | compounds that target MTOR: 4 of 8 raise it (Bimiralisib, GSK1059615, Sapanisertib, Temsirolimus) | 50% of the class's compounds vs 3.9% of all compounds | 0.060 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FGD4]] | B | FGD4 activity raises REPS2's level | lines that do not express FGD4 (10) vs lines expressing it (40) | 2.36× lower at baseline in the lines without FGD4 | 0.060 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01881]] | B | REPS2 activity raises LINC01881's level | lines that do not express REPS2 (12) vs lines expressing it (38) | 1.50× lower at baseline in the lines without REPS2 | 0.013 | ⚠ within organs, on part of the lines; also absent: GALNT9, ENSG00000227486, PLPP2; maybe low, not absent |
| [[ABTB1]] | B | REPS2 activity raises ABTB1's level | lines that do not express REPS2 (12) vs lines expressing it (38) | 1.57× lower at baseline in the lines without REPS2 | 0.024 | ⚠ within organs, on part of the lines; also absent: GALNT9, ENSG00000227486, PLPP2; maybe low, not absent |
| [[FGD4]] | B | REPS2 activity raises FGD4's level | lines that do not express REPS2 (12) vs lines expressing it (38) | 2.37× lower at baseline in the lines without REPS2 | 0.040 | ⚠ within organs, on part of the lines; also absent: GALNT9, ENSG00000227486, PLPP2; maybe low, not absent |
| [[UGCG]] | B | REPS2 activity raises UGCG's level | lines that do not express REPS2 (12) vs lines expressing it (38) | 1.86× lower at baseline in the lines without REPS2 | 0.057 | ⚠ within organs, on part of the lines; also absent: GALNT9, ENSG00000227486, PLPP2; maybe low, not absent |
| [[UBALD2]] | B | REPS2 activity raises UBALD2's level | lines that do not express REPS2 (12) vs lines expressing it (38) | 1.31× lower at baseline in the lines without REPS2 | 0.062 | ⚠ within organs, on part of the lines; also absent: GALNT9, ENSG00000227486, PLPP2; maybe low, not absent |
| [[PIK3CA]] | B | REPS2 activity raises PIK3CA's level | lines that do not express REPS2 (12) vs lines expressing it (38) | 1.12× lower at baseline in the lines without REPS2 | 0.077 | ⚠ within organs, on part of the lines; also absent: GALNT9, ENSG00000227486, PLPP2; maybe low, not absent |
| [[TPCN1]] | B | REPS2 activity raises TPCN1's level | lines that do not express REPS2 (12) vs lines expressing it (38) | 1.64× lower at baseline in the lines without REPS2 | 0.089 | ⚠ within organs, on part of the lines; also absent: GALNT9, ENSG00000227486, PLPP2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.552). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.5, -45.2); signed map (-17.8, 10.9). **Vector** length 113, 31.8% of its response variance represented; |z| ≥ 3 in 1,285 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +9.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.9 | +7.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.6 | +2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +8.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.4 | +8.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.2 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +2.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.0 | +2.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.2 | -24.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.7 | -13.9 |
|  | [[EX229 (drug)]] 5 µM |  | -6.9 | -10.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.6 | -9.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.5 | -11.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.4 | -10.4 |

## What is on record

|  |  |
|---|---|
| Name | RALBP1 associated Eps domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:16,946,658-17,153,272 (+) |
| Ensembl biotype | protein_coding |
| Also known as | POB1 |
| Gene groups (HGNC) | EF-hand domain containing |
| Reactome | 4 pathways, smallest: Cargo recognition for clathrin-mediated endocytosis; Clathrin-mediated endocytosis; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFH8](https://www.uniprot.org/uniprotkb/Q8NFH8) (RalBP1-associated Eps domain-containing protein 2):

> Involved in ligand-dependent receptor mediated endocytosis of the EGF and insulin receptors as part of the Ral signaling pathway. By controlling growth factor receptors endocytosis may regulate cell survival. Through ASAP1 may regulate cell adhesion and migration.

**Summary**, from NCBI Gene [9185](https://www.ncbi.nlm.nih.gov/gene/9185):

> The product of this gene is part of a protein complex that regulates the endocytosis of growth factor receptors. The encoded protein directly interacts with a GTPase activating protein that functions downstream of the small G protein Ral. Its expression can negatively affect receptor internalization and inhibit growth factor signaling. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9963](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9963) · Entrez [9185](https://www.ncbi.nlm.nih.gov/gene/9185) · UniProt [Q8NFH8](https://www.uniprot.org/uniprotkb/Q8NFH8) · Ensembl [ENSG00000169891](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169891)

## Data

Gene col 9866: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9866); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9866, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9866]; `tensor/DDL_lfc|DDL_z.npy` [9866]; `embed/gene_vectors.npy` [9866]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9866 or target_col == 9866). Every well: [[REPS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/REPS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
