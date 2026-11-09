---
symbol: "LRP10"
type: "gene"
col: 12382
ensembl_id: "ENSG00000197324"
name: "LDL receptor related protein 10"
location: "14q11.2"
module: 33
arm: "-"
pooled_cpm: 55.98
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 27
n_dd_up_clean: 2
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# LRP10

*LDL receptor related protein 10* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.98× (z +10.5, q 6e-23, up in 39 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[DTP3 (drug)]] 5 µM: 1.53× (z +3.4, q 0.059, up in 15 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HEC-1-A 3.57×, NCI-H1573 3.37×, SNU-423 2.76×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (HEC-1-A 3.21×, PANC-1 2.43×, J82 3.21×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.283× (z -27.5, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHOC]] (+0.59, fdr 7e-06), [[HECA]] (+0.57, fdr 3e-05), [[GRN]] (+0.56, fdr 1e-05); moves opposite to [[RBM26]] (-0.58, fdr 1e-05), [[ZNHIT6]] (-0.58, fdr 1e-05), [[FAM133B]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CASTOR2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12382.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HEC-1-A 3.57×, NCI-H1573 3.37×, SNU-423 2.76×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (HEC-1-A 3.21×, PANC-1 2.43×, J82 3.21×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.98×** | +10.5 | 6e-23 | 39/48 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +10.2 | 6e-22 | 31/39 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +4.6 | 8e-04 | 26/41 (HEC-1-A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.28×** | +3.8 | 0.024 | 24/47 (SNU-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.26×** | +3.6 | 0.039 | 20/49 (CFPAC-1, HCT15, …) | inconsistent across doses |  |
| [[DTP3 (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.059 | 15/47 (HEC-1-A, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.068 | 16/48 (LoVo, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.3 | 0.069 | 16/43 (LOX-IMVI, KATO III, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12382.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.283×** | -27.5 | 0e+00 | 45/47 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.367×** | -15.4 | 0e+00 | 43/47 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.392×** | -13.9 | 2e-41 | 45/47 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.503×** | -10.6 | 5e-24 | 43/48 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.556×** | -9.0 | 2e-17 | 39/48 (NCI-H1573, LoVo, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.573×** | -8.6 | 1e-15 | 39/48 (NCI-H23, LoVo, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.613×** | -7.5 | 4e-12 | 38/48 (AsPC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.656×** | -6.3 | 3e-08 | 37/49 (A-427, HS-578T, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.678×** | -6.0 | 1e-07 | 31/48 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.493×** | -5.7 | 7e-07 | 32/48 (A-427, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.506×** | -5.5 | 2e-06 | 32/48 (SW48, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.787×** | -5.2 | 8e-06 | 29/48 (NCI-H1573, NCI-H23, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.552×** | -4.8 | 7e-05 | 28/48 (AsPC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.554×** | -4.8 | 8e-05 | 27/48 (LoVo, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.741×** | -4.6 | 1e-04 | 26/48 (SNU-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.750×** | -4.4 | 3e-04 | 24/48 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12382. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 50.1 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -22.0) |
| [[NCI-H1573 (line)]] | alt | 131 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -26.5) |
| [[HEC-1-A (line)]] | alt | 40.6 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -14.4) |
| [[KATO III (line)]] | alt | 50.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -17.8) |
| [[AsPC-1 (line)]] | alt | 44.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -23.5) |
| [[CFPAC-1 (line)]] | alt | 132 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -30.0) |
| [[COLO 205 (line)]] | alt | 80.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -18.5) |
| [[MIA PaCa-2 (line)]] | alt | 70.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -17.7) |
| [[NCI-H460 (line)]] | wt | 43.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -15.4) |
| [[Panc 03.27 (line)]] | alt | 78.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -20.2) |
| [[PANC-1 (line)]] | alt | 33.0 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.43× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -13.8) |
| [[A549 (line)]] | wt | 79.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -16.3) |
| [[HCT15 (line)]] | alt | 53.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -14.4) |
| [[HT-29 (line)]] | alt | 45.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -18.2) |
| [[NCI-H23 (line)]] | alt | 71.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -14.5) |
| [[NCI-H2347 (line)]] | alt | 95.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -28.7) |
| [[RKO (line)]] | wt | 37.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -23.2) |
| [[A-172 (line)]] | wt | 48.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -16.0) |
| [[A-427 (line)]] | wt | 65.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.350× (z -10.5) |
| [[BT-474 (line)]] | alt | 66.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -14.7) |
| [[H4 (line)]] | wt | 50.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.120× (z -13.6) |
| [[HOP62 (line)]] | alt | 47.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -20.4) |
| [[HS-578T (line)]] | alt | 39.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -11.5) |
| [[J82 (line)]] | alt | 29.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -14.2) |
| [[LOX-IMVI (line)]] | wt | 33.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -14.6) |
| [[LS 180 (line)]] | wt | 39.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -18.2) |
| [[NCI-H2030 (line)]] | alt | 144 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -22.9) |
| [[SK-MEL-2 (line)]] | alt | 52.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -17.9) |
| [[SNU-423 (line)]] | alt | 59.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -12.2) |
| [[SW48 (line)]] | wt | 30.3 | 0 | 2 | — | [[TAK-901 (drug)]] 0.05 µM 0.106× (z -10.4) |
| [[SW480 (line)]] | alt | 25.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -10.1) |
| [[C32 (line)]] | wt | 38.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -11.6) |
| [[Hs 766T (line)]] | wt | 55.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -17.3) |
| [[hTERT-HPNE (line)]] | wt | 56.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.278× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 63.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -17.3) |
| [[SHP-77 (line)]] | alt | 22.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -11.4) |
| [[SNU-1 (line)]] | wt | 72.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -10.4) |
| [[SW 1271 (line)]] | alt | 66.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -11.0) |
| [[SW 900 (line)]] | alt | 32.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -10.4) |
| [[SW1417 (line)]] | alt | 31.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -10.5) |
| [[A498 (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12382), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHOC]] | +0.59 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[HECA]] | +0.57 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[GRN]] | +0.56 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[YPEL5]] | +0.56 | +0.38 / +0.65 | both halves | 7e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[CASTOR3P-1]] | +0.56 | +0.30 / +0.49 | both halves | 2e-04 |  |
| [[TMEM127]] | +0.54 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[WDR45]] | +0.54 | +0.24 / +0.69 | both halves | 5e-04 |  |
| [[ZNF394]] | +0.53 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[GTPBP1]] | +0.53 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[TP53I11]] | +0.51 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[HIGD1A]] | +0.51 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[RAB22A]] | +0.51 | +0.45 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM26]] | -0.58 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[ZNHIT6]] | -0.58 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[FAM133B]] | -0.57 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[KAT14]] | -0.56 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[THOC1]] | -0.55 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[WDR75]] | -0.55 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[NUFIP1]] | -0.54 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[BRIX1]] | -0.54 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[ESF1]] | -0.53 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[PTBP2]] | -0.52 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[LEO1]] | -0.51 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[PRPF39]] | -0.51 | -0.49 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASTOR2]] | C | CASTOR2's natural level weakens LRP10's drug response | CASTOR2's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.20; direction not clear | 0.076 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **-** arm (projection on the module's main direction -0.374). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-24.8, -5.7); signed map (-13.5, 14.1). **Vector** length 97.6, 28.0% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.5 | +1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +4.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +0.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.3 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +3.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +3.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.0 | -8.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.1 | -4.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.1 | -5.7 |
|  | [[EX229 (drug)]] 5 µM |  | -5.0 | -5.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.6 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | LDL receptor related protein 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:22,871,740-22,881,713 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564C1940, MGC8675, LRP9, MST087, MSTP087 |
| Gene groups (HGNC) | Low density lipoprotein receptors |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 5 pathways, smallest: Retinoid metabolism and transport; Metabolism of fat-soluble vitamins; Visual phototransduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z4F1](https://www.uniprot.org/uniprotkb/Q7Z4F1) (Low-density lipoprotein receptor-related protein 10):

> Probable receptor, which is involved in the internalization of lipophilic molecules and/or signal transduction. May be involved in the uptake of lipoprotein APOE in liver (By similarity).

**Summary**, from NCBI Gene [26020](https://www.ncbi.nlm.nih.gov/gene/26020):

> This gene encodes a low density lipoprotein receptor family protein. A similar protein in mouse is thought to play a role in the uptake of apolipoprotein E-containing lipoproteins. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:14553](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14553) · Entrez [26020](https://www.ncbi.nlm.nih.gov/gene/26020) · UniProt [Q7Z4F1](https://www.uniprot.org/uniprotkb/Q7Z4F1) · Ensembl [ENSG00000197324](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197324)

## Data

Gene col 12382: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12382); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12382, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12382]; `tensor/DDL_lfc|DDL_z.npy` [12382]; `embed/gene_vectors.npy` [12382]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12382 or target_col == 12382). Every well: [[LRP10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRP10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
