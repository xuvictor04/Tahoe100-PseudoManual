---
symbol: "RCHY1"
type: "gene"
col: 8770
ensembl_id: "ENSG00000163743"
name: "ring finger and CHY zinc finger domain containing 1"
location: "4q21.1"
module: 198
arm: "+"
pooled_cpm: 33.67
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 11
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/198"]
generated_by: "tahoemap"
---

# RCHY1

*ring finger and CHY zinc finger domain containing 1* — 4q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 3.16× (z +16.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.395× (z -12.6, q 1e-33, down in 34 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.732× (z -4.4, q 0.002, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPATA5L1]] (+0.70, fdr 7e-06), [[MBIP]] (+0.68, fdr 7e-06), [[MRPL39]] (+0.68, fdr 7e-06); moves opposite to [[PRDX1]] (-0.63, fdr 7e-06), [[KPNA4]] (-0.61, fdr 1e-05), [[DIAPH1]] (-0.58, fdr 2e-05).
> It is in [[Module 198]], a single-armed module (Antigen processing: Ubiquitination & Proteasome degradation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HSD11B2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8770.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.16×** | +16.2 | 0e+00 | 47/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +13.6 | 6e-40 | 44/48 (BT-474, RKO, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +13.2 | 2e-37 | 43/46 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.64×** | +12.8 | 3e-35 | 45/49 (BT-474, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.90×** | +9.1 | 2e-17 | 39/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.33×** | +8.9 | 6e-17 | 38/48 (SW480, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.87×** | +8.9 | 6e-17 | 35/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.80×** | +8.0 | 1e-13 | 33/48 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.73×** | +7.8 | 5e-13 | 34/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.8 | 4e-07 | 28/47 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +5.0 | 2e-05 | 24/48 (Panc 03.27, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.36×** | +4.4 | 6e-04 | 22/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.29×** | +3.6 | 0.012 | 17/47 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.039 | 14/47 (SNU-423, HCT15, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.080 | 15/48 (Panc 03.27, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8770.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.395×** | -12.6 | 1e-33 | 34/39 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.415×** | -12.4 | 6e-33 | 41/46 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.677×** | -5.1 | 7e-05 | 26/44 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.732×** | -4.4 | 0.002 | 24/48 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.739×** | -4.3 | 0.002 | 21/48 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | **0.824×** | -3.9 | 0.010 | 22/48 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.762×** | -3.8 | 0.010 | 20/48 (A498, NCI-H2030, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.833× | -3.6 | 0.020 | 20/48 (H4, SW 900, …) | top dose only |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **0.776×** | -3.6 | 0.022 | 14/48 (LS 180, NCI-H460, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.791×** | -3.3 | 0.054 | 12/48 (SW 1088, LOX-IMVI, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.797×** | -3.2 | 0.072 | 12/48 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.803×** | -3.1 | 0.096 | 13/48 (A498, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8770. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 89.9 | 10 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.38× (z +18.4) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -11.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 37.6 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.80× (z +17.4) | — |
| [[LoVo (line)]] | wt | 26.7 | 6 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.16× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.312× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 26.0 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.336× (z -8.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 29.2 | 4 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 16.7× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -14.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 21.2 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.33× (z +16.7) | — |
| [[NCI-H1573 (line)]] | alt | 38.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.34× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 59.7 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.96× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -17.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 45.3 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 6.91× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.132× (z -10.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 21.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.143× (z -12.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 41.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -15.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 54.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.0344× (z -24.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 22.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +10.6) | — |
| [[KATO III (line)]] | alt | 26.1 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.55× (z +13.1) | — |
| [[A498 (line)]] | wt | 39.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +11.9) | — |
| [[C32 (line)]] | wt | 28.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -8.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 29.9 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.05× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -8.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 47.4 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.79× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 32.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.86× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 52.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -9.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 46.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +13.9) | — |
| [[A-427 (line)]] | wt | 41.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +11.0) | — |
| [[AN3 CA (line)]] | alt | 44.7 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0849× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 28.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -11.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -8.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.180× (z -9.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 18.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 26.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.76× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 56.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -15.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -9.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 30.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -10.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8770), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA5L1]] | +0.70 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[MBIP]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[MRPL39]] | +0.68 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[ZNF330]] | +0.68 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[ZNF14]] | +0.66 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[MRPL22]] | +0.66 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[C16orf87]] | +0.65 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[PLEKHF2]] | +0.64 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[METTL14]] | +0.63 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[ZNF428]] | +0.63 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[XPA]] | +0.63 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[VAMP2]] | +0.63 | +0.54 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDX1]] | -0.63 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[KPNA4]] | -0.61 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[DIAPH1]] | -0.58 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[VCP]] | -0.57 | -0.51 / -0.62 | both halves | 1e-05 | pathway: DNA Damage Bypass |
| [[UBR4]] | -0.57 | -0.51 / -0.53 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[SETX]] | -0.57 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[ASPH]] | -0.57 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[ZSWIM6]] | -0.57 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[MSN]] | -0.57 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[GATAD2A]] | -0.55 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[RNF123]] | -0.53 | -0.48 / -0.46 | both halves | 2e-05 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 446 |
| [[TBILA]] | -0.53 | -0.59 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSD11B2]] | B | HSD11B2 activity raises RCHY1's level | lines that do not express HSD11B2 (16) vs lines expressing it (34) | 1.49× lower at baseline in the lines without HSD11B2 | 0.006 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent |
| [[RAB31]] | B | RAB31 activity lowers RCHY1's level | lines that do not express RAB31 (16) vs lines expressing it (34) | 1.22× higher at baseline in the lines without RAB31 | 0.082 | ⚠ within organs, on part of the lines; also absent: VEGFC, HERC5, NR3C1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 198]] — Antigen processing: Ubiquitination & Proteasome degradation; 16 genes; every member is in the + arm (projection on the module's main direction 0.777). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.4, -4.7); signed map (-23.7, -8.8). **Vector** length 80.1, 20.0% of its response variance represented; |z| ≥ 3 in 1,060 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.1 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.6 | +0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.9 | +0.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.0 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.5 | +2.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.4 | +1.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.3 | -0.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.4 | +0.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | +2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.3 | -0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | +7.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.4 | -1.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -0.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.8 | -0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ring finger and CHY zinc finger domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.1 — chr4:75,479,033-75,514,764 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CHIMP, DKFZp586C1620, PRO1996, RNF199, ARNIP, PIRH2, ZCHY; previously ZNF363 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | P53_PATHWAY |
| Reactome | 10 pathways, smallest: Translesion Synthesis by POLH; Translesion synthesis by Y family DNA polymerases bypasses lesions on DNA template; DNA Damage Bypass |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PM5](https://www.uniprot.org/uniprotkb/Q96PM5) (RING finger and CHY zinc finger domain-containing protein 1):

> E3 ubiquitin-protein ligase that mediates ubiquitination of target proteins, including p53/TP53, TP73, HDAC1 and CDKN1B. Mediates ubiquitination and degradation of p53/TP53; preferentially acts on tetrameric p53/TP53. Catalyzes monoubiquitinates the translesion DNA polymerase POLH. Involved in the ribosome-associated quality control (RQC) pathway, which mediates the extraction of incompletely synthesized nascent chains from stalled ribosomes: RCHY1 acts downstream of NEMF and recognizes CAT …

**Summary**, from NCBI Gene [25898](https://www.ncbi.nlm.nih.gov/gene/25898):

> The protein encoded by this gene has ubiquitin ligase activity. It mediates E3-dependent ubiquitination and proteasomal degradation of target proteins, including tumor protein 53, histone deacetylase 1, and cyclin-dependent kinase inhibitor 1B, thus regulating their levels and cell cycle progression. Alternatively spliced transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, Jun 2013]

**Accessions** — [HGNC:17479](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17479) · Entrez [25898](https://www.ncbi.nlm.nih.gov/gene/25898) · UniProt [Q96PM5](https://www.uniprot.org/uniprotkb/Q96PM5) · Ensembl [ENSG00000163743](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163743)

## Data

Gene col 8770: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8770); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8770, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8770]; `tensor/DDL_lfc|DDL_z.npy` [8770]; `embed/gene_vectors.npy` [8770]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8770 or target_col == 8770). Every well: [[RCHY1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RCHY1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
