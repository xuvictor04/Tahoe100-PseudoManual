---
symbol: "CASZ1"
type: "gene"
col: 5147
ensembl_id: "ENSG00000130940"
name: "castor zinc finger 1"
location: "1p36.22"
module: 100
arm: "+"
pooled_cpm: 31.93
n_lines_expressing: 40
n_dd_up: 18
n_dd_down: 19
n_dd_up_clean: 17
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 7
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# CASZ1

*castor zinc finger 1* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.62× (z +21.4, q 0e+00, up in 27 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.561× (z -9.9, q 4e-20, down in 23 of 36 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPB41L4B]] (+0.58, fdr 1e-05), [[NOL4L]] (+0.58, fdr 2e-05), [[NOS1AP]] (+0.57, fdr 2e-05); moves opposite to [[TRMT13]] (-0.54, fdr 3e-05), [[ZNF140]] (-0.54, fdr 4e-05), [[PIGL]] (-0.53, fdr 3e-05).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[P4HA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5147.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.62×** | +21.4 | 0e+00 | 27/37 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.06×** | +19.1 | 0e+00 | 30/37 (NCI-H2030, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.94×** | +18.4 | 0e+00 | 29/37 (CFPAC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.04×** | +16.5 | 0e+00 | 28/38 (NCI-H2347, J82, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.50×** | +15.6 | 0e+00 | 32/37 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.36×** | +14.6 | 0e+00 | 26/37 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.93×** | +11.2 | 2e-27 | 24/37 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.92×** | +9.6 | 9e-20 | 24/38 (A-427, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +8.3 | 6e-15 | 21/36 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +6.7 | 2e-09 | 19/37 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +5.8 | 3e-07 | 16/37 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.5 | 2e-06 | 17/36 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +5.1 | 1e-05 | 15/37 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +4.9 | 5e-05 | 16/36 (NCI-H23, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.31×** | +4.5 | 3e-04 | 14/36 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +3.5 | 0.018 | 8/38 (COLO 205, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5147.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.561×** | -9.9 | 4e-20 | 23/36 (A-427, PANC-1, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.674×** | -6.7 | 5e-09 | 21/37 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.686×** | -6.4 | 2e-08 | 19/37 (PANC-1, KATO III, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.693×** | -6.2 | 6e-08 | 19/37 (NCI-H460, LoVo, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.727×** | -5.4 | 7e-06 | 16/37 (HT-29, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.775×** | -4.3 | 0.001 | 15/37 (NCI-H460, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.775×** | -4.2 | 0.002 | 12/25 (KATO III, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.775×** | -4.0 | 0.004 | 19/28 (SW48, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.646×** | -3.9 | 0.006 | 17/36 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.799×** | -3.8 | 0.007 | 17/37 (NCI-H460, LoVo, …) | two highest doses | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.795×** | -3.8 | 0.009 | 12/37 (BT-474, LS 180, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.812×** | -3.5 | 0.019 | 11/37 (NCI-H460, LS 180, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.807×** | -3.5 | 0.020 | 18/36 (NCI-H460, COLO 205, …) | two highest doses | composition shift; position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.688×** | -3.3 | 0.035 | 11/36 (LoVo, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.827×** | -3.2 | 0.047 | 6/37 (BT-474, SW 1271, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.713×** | -3.0 | 0.077 | 12/34 (NCI-H460, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.718×** | -3.0 | 0.089 | 1/38 (NCI-H460) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5147. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 31.8 | 4 (1 ⚠) | 11 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.29× (z +24.0) | [[Digitoxin (drug)]] 5 µM 0.241× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.284× (z -11.0) |
| [[A549 (line)]] | wt | 11.4 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.9× (z +18.0) | — |
| [[LoVo (line)]] | wt | 42.5 | 3 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.41× (z +24.4) | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -13.0) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.426× (z -8.6) |
| [[LS 180 (line)]] | wt | 132 | 3 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +18.7) | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 8.81 | 5 | 0 | [[Panobinostat (drug)]] 0.05 µM 4.76× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 81.9 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -14.6) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.345× (z -12.8) |
| [[SW480 (line)]] | alt | 57.8 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 0.05 µM 2.07× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.454× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 11.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.65× (z +10.1) | [[AZD2858 (drug)]] 0.5 µM 0.106× (z -9.3) ⚠ toxic |
| [[KATO III (line)]] | alt | 69.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.334× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 23.0 | 2 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 4.17× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -12.5) ⚠ cell-cycle shift, explains ~86% of this change |
| [[NCI-H23 (line)]] | alt | 33.8 | 2 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.96× (z +18.5) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -11.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 76.6 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.37× (z +16.1) | [[Dinaciclib (drug)]] 0.05 µM 0.0988× (z -14.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 29.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -14.2) |
| [[A498 (line)]] | wt | 10.8 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +18.5) | — |
| [[HCT15 (line)]] | alt | 34.0 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 4.35× (z +9.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.239× (z -9.1) |
| [[HT-29 (line)]] | alt | 95.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -12.1) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.368× (z -10.3) |
| [[J82 (line)]] | alt | 8.57 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.09× (z +9.8) | — |
| [[A-172 (line)]] | wt | 11.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +15.0) | — |
| [[COLO 205 (line)]] | alt | 68.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 13.9 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.39× (z +8.7) | — |
| [[RKO (line)]] | wt | 11.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +12.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -9.3) |
| [[H4 (line)]] | wt | 9.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.4× (z +11.1) | — |
| [[LOX-IMVI (line)]] | wt | 9.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +14.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 48.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.257× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 33.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.18× (z +11.6) | — |
| [[SW 900 (line)]] | alt | 13.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0980× (z -10.1) |
| [[SW1417 (line)]] | alt | 58.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.294× (z -10.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.97 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.88 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.66 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.06 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.81 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.77 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.91 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5147), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L4B]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[NOL4L]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[NOS1AP]] | +0.57 | +0.46 / +0.64 | both halves | 2e-05 |  |
| [[RALGDS]] | +0.57 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[SLC29A4]] | +0.56 | +0.39 / +0.61 | both halves | 6e-05 |  |
| [[TANC1]] | +0.56 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[ANKRD9]] | +0.55 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[CASTOR2]] | +0.55 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[AHDC1]] | +0.54 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[PARD6G]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[RALGPS1]] | +0.54 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[CDS1]] | +0.54 | +0.47 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT13]] | -0.54 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[ZNF140]] | -0.54 | -0.41 / -0.53 | both halves | 4e-05 | same gene group |
| [[PIGL]] | -0.53 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[ZNF268]] | -0.53 | -0.43 / -0.51 | both halves | 4e-05 | same gene group |
| [[TAF2]] | -0.53 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[ST7L]] | -0.53 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[ZNF776]] | -0.52 | -0.47 / -0.41 | both halves | 4e-05 | same gene group |
| [[COMMD10]] | -0.51 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[ZNF507]] | -0.51 | -0.39 / -0.48 | both halves | 5e-05 | same gene group |
| [[ZNF280D]] | -0.51 | -0.46 / -0.39 | both halves | 6e-05 | same gene group |
| [[JPX]] | -0.50 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[ZNF606]] | -0.50 | -0.44 / -0.32 | both halves | 2e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CASZ1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P4HA2]] | B | CASZ1 activity lowers P4HA2's level | lines that do not express CASZ1 (10) vs lines expressing it (40) | 2.16× higher at baseline in the lines without CASZ1 | 0.031 | ⚠ within organs, on part of the lines; also absent: SBK1, CPLX1, LLGL2; maybe low, not absent |
| [[CREB3L1]] | B | CASZ1 activity lowers CREB3L1's level | lines that do not express CASZ1 (10) vs lines expressing it (40) | 3.09× higher at baseline in the lines without CASZ1 | 0.053 | ⚠ within organs, on part of the lines; also absent: SBK1, CPLX1, LLGL2; maybe low, not absent |
| [[EPB41L4B]] | B | CASZ1 activity raises EPB41L4B's level | lines that do not express CASZ1 (10) vs lines expressing it (40) | 2.89× lower at baseline in the lines without CASZ1 | 0.054 | ⚠ within organs, on part of the lines; also absent: SBK1, CPLX1, LLGL2; maybe low, not absent |
| [[CYFIP2]] | B | CASZ1 activity raises CYFIP2's level | lines that do not express CASZ1 (10) vs lines expressing it (40) | 3.51× lower at baseline in the lines without CASZ1 | 0.058 | ⚠ within organs, on part of the lines; also absent: SBK1, CPLX1, LLGL2; maybe low, not absent |
| [[ZBTB38]] | B | CASZ1 activity lowers ZBTB38's level | lines that do not express CASZ1 (10) vs lines expressing it (40) | 2.40× higher at baseline in the lines without CASZ1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SBK1, CPLX1, LLGL2; maybe low, not absent |
| [[HERC3]] | B | CASZ1 activity lowers HERC3's level | lines that do not express CASZ1 (10) vs lines expressing it (40) | 1.63× higher at baseline in the lines without CASZ1 | 0.076 | ⚠ within organs, on part of the lines; also absent: SBK1, CPLX1, LLGL2; maybe low, not absent |
| [[RALGPS1]] | B | CASZ1 activity raises RALGPS1's level | lines that do not express CASZ1 (10) vs lines expressing it (40) | 2.22× lower at baseline in the lines without CASZ1 | 0.099 | ⚠ within organs, on part of the lines; also absent: SBK1, CPLX1, LLGL2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.583). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.2, -3.1); signed map (-19.9, 20.6). **Vector** length 106, 26.0% of its response variance represented; |z| ≥ 3 in 1,007 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +16.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +21.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.6 | +8.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.3 | +15.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +9.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.9 | -9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | -5.2 | -3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.5 | -3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.3 | -2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.3 | -3.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -3.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.8 | -3.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.7 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | castor zinc finger 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:10,636,604-10,796,650 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20321, ZNF693, castor, cst, SRG |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86V15](https://www.uniprot.org/uniprotkb/Q86V15) (Zinc finger protein castor homolog 1):

> Transcriptional activator. Involved in vascular assembly and morphogenesis through direct transcriptional regulation of EGFL7.

**Summary**, from NCBI Gene [54897](https://www.ncbi.nlm.nih.gov/gene/54897):

> The protein encoded by this gene is a zinc finger transcription factor. The encoded protein may function as a tumor suppressor, and single nucleotide polymorphisms in this gene are associated with blood pressure variation. Alternative splicing results in multiple transcript variants that encode different protein isoforms. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:26002](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26002) · Entrez [54897](https://www.ncbi.nlm.nih.gov/gene/54897) · UniProt [Q86V15](https://www.uniprot.org/uniprotkb/Q86V15) · Ensembl [ENSG00000130940](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130940)

## Data

Gene col 5147: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5147); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5147, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5147]; `tensor/DDL_lfc|DDL_z.npy` [5147]; `embed/gene_vectors.npy` [5147]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5147 or target_col == 5147). Every well: [[CASZ1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASZ1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
