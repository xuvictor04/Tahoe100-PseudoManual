---
symbol: "FAM111A"
type: "gene"
col: 9360
ensembl_id: "ENSG00000166801"
name: "FAM111 trypsin like peptidase A"
location: "11q12.1"
module: 91
arm: "+"
pooled_cpm: 26.67
n_lines_expressing: 47
n_dd_up: 33
n_dd_down: 22
n_dd_up_clean: 19
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 13
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# FAM111A

*FAM111 trypsin like peptidase A* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.00× (z +20.5, q 0e+00, up in 41 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.574× (z -7.0, q 2e-09, down in 30 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRCA2]] (+0.78, fdr 7e-06), [[TMPO]] (+0.73, fdr 7e-06), [[ESCO2]] (+0.73, fdr 7e-06); moves opposite to [[TMEM120B]] (-0.67, fdr 1e-05), [[ST6GALNAC6]] (-0.67, fdr 1e-05), [[RPS24]] (-0.66, fdr 7e-06).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 13 go from it, the strongest it → [[SRSF10]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9360.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.00×** | +20.5 | 0e+00 | 41/44 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.37×** | +10.9 | 2e-25 | 35/44 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.22×** | +10.5 | 2e-23 | 35/43 (HS-578T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **2.03×** | +9.2 | 3e-18 | 35/44 (SW480, HT-29, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.96×** | +8.8 | 2e-16 | 31/45 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **1.71×** | +6.8 | 8e-10 | 21/33 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **1.63×** | +6.4 | 2e-08 | 25/40 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.56×** | +5.7 | 1e-06 | 25/45 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.59×** | +5.6 | 1e-06 | 19/35 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.53×** | +5.4 | 4e-06 | 27/44 (PANC-1, J82, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.8 | 7e-05 | 24/45 (J82, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +4.7 | 1e-04 | 21/45 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.38×** | +4.2 | 0.001 | 23/45 (CFPAC-1, A498, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.25×** | +4.2 | 0.001 | 20/43 (BT-474, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.37×** | +4.0 | 0.002 | 18/41 (PANC-1, SW480, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.007 | 20/44 (J82, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.34×** | +3.6 | 0.009 | 15/45 (HT-29, RKO, …) | all doses, flat |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.013 | 15/45 (CFPAC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.014 | 17/43 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.2 | 0.027 | 12/42 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.034 | 14/44 (AsPC-1, Hs 766T, …) | rises with dose |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.27×** | +3.0 | 0.056 | 8/45 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9360.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.574×** | -7.0 | 2e-09 | 30/43 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.720×** | -6.2 | 2e-07 | 31/45 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.634×** | -6.0 | 3e-07 | 28/45 (NCI-H23, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.642×** | -5.9 | 6e-07 | 27/45 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.711×** | -4.5 | 7e-04 | 22/43 (LS 180, Panc 03.27, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.716×** | -4.4 | 8e-04 | 22/45 (HT-29, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.528×** | -4.4 | 8e-04 | 20/37 (HCT15, A-427, …) | all doses, flat | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.536×** | -4.3 | 0.001 | 22/43 (Panc 03.27, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.729×** | -4.2 | 0.002 | 17/45 (COLO 205, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.733×** | -4.1 | 0.002 | 20/45 (J82, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.649×** | -4.1 | 0.002 | 21/45 (HT-29, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.664×** | -3.9 | 0.005 | 20/45 (KATO III, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.826×** | -3.6 | 0.014 | 16/45 (SK-MEL-2, HT-29, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.599×** | -3.5 | 0.016 | 14/43 (HEC-1-A, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.772×** | -3.4 | 0.022 | 19/45 (SW48, PANC-1, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.773×** | -3.4 | 0.022 | 15/45 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.781×** | -3.3 | 0.037 | 14/44 (SK-MEL-2, COLO 205, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.797×** | -3.0 | 0.083 | 13/45 (A-427, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9360. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 26.4 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +14.0) | [[Ixazomib citrate (drug)]] 0.5 µM 0.342× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 59.1 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +12.7) | [[Ixazomib citrate (drug)]] 5 µM 0.336× (z -9.1) |
| [[LoVo (line)]] | wt | 12.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +12.9) | — |
| [[A-172 (line)]] | wt | 45.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +14.9) | — |
| [[HT-29 (line)]] | alt | 48.9 | 1 | 2 | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 3.01× (z +8.8) | [[Bortezomib (drug)]] 0.05 µM 0.253× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 17.1 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +14.9) | [[Hydroxyurea (drug)]] 0.05 µM 0.0988× (z -9.7) |
| [[J82 (line)]] | alt | 48.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +18.1) | — |
| [[NCI-H460 (line)]] | wt | 16.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +14.0) | [[Digitoxin (drug)]] 5 µM 0.235× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 19.2 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +9.3) | [[Ixazomib citrate (drug)]] 0.5 µM 0.0435× (z -13.0) |
| [[BT-474 (line)]] | alt | 33.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +11.4) | — |
| [[Hs 766T (line)]] | wt | 33.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.43× (z +17.0) | — |
| [[HS-578T (line)]] | alt | 18.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +12.7) | — |
| [[NCI-H2347 (line)]] | alt | 21.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +14.4) | — |
| [[RPMI-7951 (line)]] | alt | 33.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +14.1) | — |
| [[SNU-423 (line)]] | alt | 31.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.07× (z +18.9) | — |
| [[SW480 (line)]] | alt | 27.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 2.80× (z +8.8) | — |
| [[C32 (line)]] | wt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 27.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +9.6) | — |
| [[HCT15 (line)]] | alt | 61.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 19.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 26.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +14.9) | — |
| [[NCI-H1792 (line)]] | alt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 20.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +11.8) | — |
| [[NCI-H23 (line)]] | alt | 20.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.120× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 25.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +9.3) | — |
| [[SNU-1 (line)]] | wt | 23.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +8.5) | — |
| [[SW 1271 (line)]] | alt | 59.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +8.9) | — |
| [[A-427 (line)]] | wt | 71.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.66 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.46 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9360), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRCA2]] | +0.78 | +0.80 / +0.78 | both halves | 7e-06 |  |
| [[TMPO]] | +0.73 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[ESCO2]] | +0.73 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[MASTL]] | +0.71 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[SERTAD4]] | +0.71 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[RHNO1]] | +0.71 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[ZNF724]] | +0.71 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[DCLRE1A]] | +0.70 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[GEN1]] | +0.70 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[SENP1]] | +0.69 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[REXO5]] | +0.69 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[ZWINT]] | +0.68 | +0.60 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM120B]] | -0.67 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[ST6GALNAC6]] | -0.67 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[RPS24]] | -0.66 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[RPL26]] | -0.65 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[RPS14]] | -0.64 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[RPS25]] | -0.64 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[RPL13]] | -0.64 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[RPL27A]] | -0.64 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[ANKRD27]] | -0.64 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[RPS10]] | -0.64 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[TOMM20]] | -0.64 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[RPL34]] | -0.64 | -0.66 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FAM111A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 0, C 13. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRSF10]] | C | FAM111A activity weakens SRSF10's drug response | lines that do not express FAM111A (3) vs lines expressing it (46) | the lines without FAM111A respond 1.07× as strongly (z diff -1.85); strongest at Harringtonine 5 µM: 2.64x vs 2.52x (z diff -4.1) | 5e-04 | ⚠ few lines (3 vs 47); across organs; also absent: FXYD5, ACCS, TFAP2A; maybe low, not absent; target measured in part of the lines; rests on the correction; artifact flags |
| [[BCLAF1]] | C | FAM111A activity weakens BCLAF1's drug response | lines that do not express FAM111A (3) vs lines expressing it (46) | the lines without FAM111A respond 0.80× as strongly (z diff +0.23); strongest at Harringtonine 5 µM: 2.01x vs 2.53x (z diff -3.6) | 0.010 | ⚠ few lines (3 vs 47); across organs; also absent: FXYD5, ACCS, TFAP2A; maybe low, not absent; target measured in part of the lines; both ways; rests on the correction; artifact flags |
| [[RPL35A]] | C | FAM111A activity raises RPL35A's level | lines that do not express FAM111A (3) vs lines expressing it (47) | 1.79× lower at baseline in the lines without FAM111A | 0.019 | ⚠ few lines (3 vs 47); across organs; also absent: FXYD5, ACCS, TFAP2A; maybe low, not absent |
| cells under [[Tranilast (drug)]] 0.5 µM | C | FAM111A activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express FAM111A (3) vs lines expressing it (45) | the lines without FAM111A: 0.76× the cells of the other lines | 0.033 | ⚠ few lines (3 vs 47); across organs; also absent: FXYD5, ACCS, TFAP2A; maybe low, not absent |
| [[COG5]] | C | FAM111A activity raises COG5's level | lines that do not express FAM111A (3) vs lines expressing it (47) | 1.81× lower at baseline in the lines without FAM111A | 0.041 | ⚠ few lines (3 vs 47); across organs; also absent: FXYD5, ACCS, TFAP2A; maybe low, not absent |
| cells under [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM | C | FAM111A activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (protects the cells) | lines that do not express FAM111A (3) vs lines expressing it (45) | the lines without FAM111A: 0.78× the cells of the other lines | 0.055 | ⚠ few lines (3 vs 47); across organs; also absent: FXYD5, ACCS, TFAP2A; maybe low, not absent |
| [[C5]] | C | FAM111A activity lowers C5's level | lines that do not express FAM111A (3) vs lines expressing it (47) | 3.61× higher at baseline in the lines without FAM111A | 0.060 | ⚠ few lines (3 vs 47); across organs; also absent: FXYD5, ACCS, TFAP2A; maybe low, not absent |
| [[FAM111A-DT]] | C | FAM111A activity raises FAM111A-DT's level | lines that do not express FAM111A (3) vs lines expressing it (47) | 2.17× lower at baseline in the lines without FAM111A | 0.062 | ⚠ few lines (3 vs 47); across organs; also absent: FXYD5, ACCS, TFAP2A; maybe low, not absent; co-absent with the target |
| cells under [[Posaconazole (drug)]] 0.5 µM | C | FAM111A activity raises the cells' numbers under Posaconazole 0.5 µM (protects the cells) | lines that do not express FAM111A (3) vs lines expressing it (45) | the lines without FAM111A: 0.77× the cells of the other lines | 0.072 | ⚠ few lines (3 vs 47); across organs; also absent: FXYD5, ACCS, TFAP2A; maybe low, not absent |
| [[ANKRD27]] | C | FAM111A activity strengthens ANKRD27's drug response | lines that do not express FAM111A (3) vs lines expressing it (45) | the lines without FAM111A respond 0.51× as strongly (z diff +1.75); strongest at Ouabain (Octahydrate) 5 µM: 1.16x vs 0.63x (z diff +5.6) | 0.081 | ⚠ few lines (3 vs 47); across organs; also absent: FXYD5, ACCS, TFAP2A; maybe low, not absent; target measured in part of the lines; the reference differs; artifact flags |
| cells under [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM | C | FAM111A activity lowers the cells' numbers under Tirabrutinib (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express FAM111A (3) vs lines expressing it (45) | the lines without FAM111A: 1.52× the cells of the other lines | 0.085 | ⚠ few lines (3 vs 47); across organs; also absent: FXYD5, ACCS, TFAP2A; maybe low, not absent |
| [[RBAK-RBAKDN]] | C | FAM111A activity strengthens RBAK-RBAKDN's drug response | lines that do not express FAM111A (3) vs lines expressing it (47) | the lines without FAM111A respond 0.47× as strongly (z diff +2.48); strongest at Ouabain (Octahydrate) 5 µM: 0.84x vs 0.48x (z diff +5.6) | 0.086 | ⚠ few lines (3 vs 47); across organs; also absent: FXYD5, ACCS, TFAP2A; maybe low, not absent; artifact flags |

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.763). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-41.7, -47.8); signed map (-43.8, -48.8). **Vector** length 138, 42.2% of its response variance represented; |z| ≥ 3 in 1,149 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.70 to 5); *Resolution of D-loop Structures through Holliday Junction Intermediates* (reactome, mean cos +0.70 to 4); *Resolution of D-Loop Structures* (reactome, mean cos +0.70 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.6 | +10.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.0 | +20.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +6.4 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.3 | +10.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.1 | +8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +4.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.6 | +4.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.1 | +3.0 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +2.8 | +3.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.6 | +2.2 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -7.4 | -7.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.1 | -4.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.1 | -4.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.0 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.5 | -6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -6.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.0 | -4.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.8 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | FAM111 trypsin like peptidase A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:59,142,748-59,155,039 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22794, KIAA1895 |
| Gene groups (HGNC) | FAM111 trypsin like peptidase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PZ2](https://www.uniprot.org/uniprotkb/Q96PZ2) (Serine protease FAM111A):

> Single-stranded DNA-binding serine protease that mediates the proteolytic cleavage of covalent DNA-protein cross-links (DPCs) during DNA synthesis, thereby playing a key role in maintaining genomic integrity. DPCs are highly toxic DNA lesions that interfere with essential chromatin transactions, such as replication and transcription, and which are induced by reactive agents, such as UV light or formaldehyde. Protects replication fork from stalling by removing DPCs, such as covalently trapped …

**Summary**, from NCBI Gene [63901](https://www.ncbi.nlm.nih.gov/gene/63901):

> The protein encoded by this gene is cell-cycle regulated, and has nuclear localization. The C-terminal half of the protein shares homology with trypsin-like peptidases and it contains a PCNA-interacting peptide (PIP) box, that is necessary for its co-localization with proliferating cell nuclear antigen (PCNA). Reduced expression of this gene resulted in DNA replication defects, consistent with the demonstrated role for this gene in Simian Virus 40 (SV40) viral replication. Mutations in this …

**Accessions** — [HGNC:24725](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24725) · Entrez [63901](https://www.ncbi.nlm.nih.gov/gene/63901) · UniProt [Q96PZ2](https://www.uniprot.org/uniprotkb/Q96PZ2) · Ensembl [ENSG00000166801](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166801)

## Data

Gene col 9360: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9360); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9360, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9360]; `tensor/DDL_lfc|DDL_z.npy` [9360]; `embed/gene_vectors.npy` [9360]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9360 or target_col == 9360). Every well: [[FAM111A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM111A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
