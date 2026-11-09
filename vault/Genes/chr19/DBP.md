---
symbol: "DBP"
type: "gene"
col: 2614
ensembl_id: "ENSG00000105516"
name: "D-box binding PAR bZIP transcription factor"
location: "19q13.33"
module: 59
arm: "+"
pooled_cpm: 5.21
n_lines_expressing: 48
n_dd_up: 17
n_dd_down: 27
n_dd_up_clean: 13
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# DBP

*D-box binding PAR bZIP transcription factor* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.27× (z +8.7, q 2e-15, up in 26 of 41 measured lines) ⚠ cell-cycle shift, explains ~62% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.70× (z +5.6, q 4e-06, up in 24 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.390× (z -7.1, q 7e-10, down in 30 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Megestrol (drug)]] 5 µM: 0.581× (z -5.8, q 2e-06, down in 28 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CXXC5]] (+0.73, fdr 7e-06), [[KMT2E]] (+0.70, fdr 7e-06), [[CBX8]] (+0.69, fdr 7e-06); moves opposite to [[TTL]] (-0.70, fdr 7e-06), [[ENOX2]] (-0.67, fdr 1e-05), [[ZNF731P]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CXXC5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2614.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **2.27×** | +8.7 | 2e-15 | 26/41 (HEC-1-A, A-172, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **2.28×** | +5.9 | 8e-07 | 23/42 (HEC-1-A, A-427, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.70×** | +5.6 | 4e-06 | 24/45 (KATO III, A498, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.56×** | +4.7 | 4e-04 | 21/44 (SK-MEL-2, RPMI-7951, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.83×** | +4.5 | 8e-04 | 17/45 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.81×** | +4.5 | 8e-04 | 20/43 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.78×** | +4.3 | 0.001 | 16/44 (A549, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM |  | **1.74×** | +4.2 | 0.002 | 15/45 (HEC-1-A, LS 180, …) | all doses, stronger at high dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.63×** | +3.7 | 0.015 | 13/44 (MIA PaCa-2, SW 900, …) | top dose only |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | **1.58×** | +3.4 | 0.038 | 12/41 (HEC-1-A, HT-29, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.056 | 11/45 (SHP-77, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.54×** | +3.2 | 0.056 | 9/44 (BT-474, H4, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.83×** | +3.2 | 0.056 | 5/29 (Hs 766T, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~73% of this change | **1.52×** | +3.1 | 0.067 | 7/25 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.79×** | +3.1 | 0.068 | 6/41 (LS 180, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +3.1 | 0.072 | 9/43 (J82, A-172, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2614.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.390×** | -7.1 | 7e-10 | 30/45 (HT-29, A-427, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 5 µM |  | **0.581×** | -5.8 | 2e-06 | 28/45 (NCI-H2347, H4, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.473×** | -5.6 | 3e-06 | 24/45 (LoVo, LS 180, …) | rises with dose |  |
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | **0.498×** | -5.3 | 2e-05 | 26/45 (Hs 766T, RPMI-7951, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.486×** | -5.2 | 2e-05 | 23/43 (SK-MEL-2, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.512×** | -5.0 | 4e-05 | 18/39 (RPMI-7951, SNU-423, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.624×** | -5.0 | 4e-05 | 21/44 (SNU-423, SW 900, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.515×** | -5.0 | 4e-05 | 21/43 (NCI-H2347, SK-MEL-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.641×** | -4.8 | 1e-04 | 22/45 (Hs 766T, SW 900, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.532×** | -4.6 | 2e-04 | 18/38 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~23% here); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.546×** | -4.6 | 2e-04 | 21/43 (RPMI-7951, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.547×** | -4.6 | 2e-04 | 18/45 (SNU-423, MIA PaCa-2, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.567×** | -4.0 | 0.002 | 20/41 (HT-29, H4, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.686×** | -4.0 | 0.002 | 20/36 (Hs 766T, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.589×** | -4.0 | 0.003 | 16/43 (MIA PaCa-2, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **0.624×** | -3.6 | 0.012 | 18/45 (Hs 766T, NCI-H1573, …) | rises with dose | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.632×** | -3.5 | 0.017 | 15/44 (Hs 766T, RPMI-7951, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.636×** | -3.4 | 0.019 | 19/44 (LoVo, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.423×** | -3.4 | 0.020 | 16/42 (COLO 205, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.637×** | -3.2 | 0.033 | 14/43 (SW480, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.658×** | -3.2 | 0.039 | 19/44 (NCI-H460, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.666×** | -3.1 | 0.050 | 15/44 (SNU-423, MIA PaCa-2, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.680×** | -2.9 | 0.082 | 11/45 (Hs 766T, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.56 per unit of S-phase module lfc, +0.84 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2614. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 8.26 | 0 | 2 (2 ⚠) | — | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.0544× (z -10.2) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 2.18 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0490× (z -8.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0497× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 9.87 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 2.04× (z +9.1) ⚠ position not correctable | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -8.9) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H2347 (line)]] | alt | 8.20 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0806× (z -11.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 2 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0811× (z -9.2) |
| [[SNU-423 (line)]] | alt | 8.12 | 0 | 2 (1 ⚠) | — | [[Peretinoin (drug)]] 0.5 µM 0.0469× (z -12.3) |
| [[A-172 (line)]] | wt | 3.13 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.76× (z +9.7) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[HEC-1-A (line)]] | alt | 13.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.73× (z +14.5) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[HT-29 (line)]] | alt | 8.98 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0460× (z -12.4) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.373× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2614), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CXXC5]] | +0.73 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[KMT2E]] | +0.70 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[CBX8]] | +0.69 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[BMF]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[CCDC88B]] | +0.68 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[AFTPH]] | +0.67 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[KBTBD3]] | +0.65 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[RAB30]] | +0.64 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[TEF]] | +0.64 | +0.71 / +0.68 | both halves | 7e-06 | same gene group; STRING 567 |
| [[SNX2]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[HCFC1R1]] | +0.64 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[GALM]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTL]] | -0.70 | -0.70 / -0.64 | both halves | 7e-06 |  |
| [[ENOX2]] | -0.67 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.67 | -0.61 / -0.70 | both halves | 7e-06 |  |
| [[ABCF2]] | -0.66 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[AVEN]] | -0.65 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[SPOPL-DT]] | -0.64 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[RBM19]] | -0.64 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[TIMM23B-AGAP6]] | -0.63 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[LETM1]] | -0.63 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[PRMT3]] | -0.62 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[MFSD14CP-1]] | -0.61 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[SLFNL1-AS1]] | -0.61 | -0.49 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXXC5]] | B | CXXC5 activity raises DBP's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 1.89× lower at baseline in the lines without CXXC5 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |
| [[ADGRG1]] | B | ADGRG1 activity raises DBP's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 1.43× lower at baseline in the lines without ADGRG1 | 0.064 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.762). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (21.1, -5.8); signed map (-5.5, 15.1). **Vector** length 102, 23.8% of its response variance represented; |z| ≥ 3 in 982 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *BH3-only proteins associate with and inactivate anti-apoptotic BCL-2 members* (reactome, mean cos +0.51 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +4.4 | +8.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.9 | +4.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +3.7 | +5.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +3.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -7.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -4.1 | -5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -3.9 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -5.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.5 | -5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.3 | -5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | D-box binding PAR bZIP transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,630,030-48,637,379 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DABP |
| Gene groups (HGNC) | PAR bZIP family |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 6 pathways, smallest: Phosphorylated BMAL1:CLOCK (ARNTL:CLOCK) activates expression of core clock genes; HCMV Late Events; HCMV Early Events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q10586](https://www.uniprot.org/uniprotkb/Q10586) (D site-binding protein):

> This transcriptional activator recognizes and binds to the sequence 5'-RTTAYGTAAY-3' found in the promoter of genes such as albumin, CYP2A4 and CYP2A5. It is not essential for circadian rhythm generation, but modulates important clock output genes. May be a direct target for regulation by the circadian pacemaker component clock. May affect circadian period and sleep regulation. Activates transcription of coagulation factors F8 and F9; transactivation activity is enhanced by formation of a …

**Summary**, from NCBI Gene [1628](https://www.ncbi.nlm.nih.gov/gene/1628):

> The protein encoded by this gene is a member of the PAR bZIP transcription factor family and binds to specific sequences in the promoters of several genes, such as albumin, CYP2A4, and CYP2A5. The encoded protein can bind DNA as a homo- or heterodimer and is involved in the regulation of some circadian rhythm genes. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:2697](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2697) · Entrez [1628](https://www.ncbi.nlm.nih.gov/gene/1628) · UniProt [Q10586](https://www.uniprot.org/uniprotkb/Q10586) · Ensembl [ENSG00000105516](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105516)

## Data

Gene col 2614: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2614); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2614, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2614]; `tensor/DDL_lfc|DDL_z.npy` [2614]; `embed/gene_vectors.npy` [2614]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2614 or target_col == 2614). Every well: [[DBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
