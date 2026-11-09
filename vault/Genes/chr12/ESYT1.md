---
symbol: "ESYT1"
type: "gene"
col: 6328
ensembl_id: "ENSG00000139641"
name: "extended synaptotagmin 1"
location: "12q13.2"
module: 2
arm: "+"
pooled_cpm: 36.29
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ESYT1

*extended synaptotagmin 1* — 12q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.90× (z +11.0, q 2e-25, up in 42 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 1.84× (z +10.5, q 3e-23, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.590× (z -12.8, q 7e-35, down in 38 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.483× (z -12.5, q 3e-33, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLBD2]] (+0.70, fdr 7e-06), [[SBF1]] (+0.68, fdr 8e-06), [[MAN2B2]] (+0.67, fdr 7e-06); moves opposite to [[IWS1]] (-0.62, fdr 1e-05), [[ERCC4]] (-0.62, fdr 7e-06), [[PRPF38B]] (-0.59, fdr 7e-06).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[STARD9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6328.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.90×** | +11.0 | 2e-25 | 42/45 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +10.5 | 3e-23 | 39/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.74×** | +9.5 | 5e-19 | 37/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +9.0 | 3e-17 | 28/38 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +8.9 | 6e-17 | 37/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.58×** | +7.8 | 7e-13 | 37/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +7.5 | 5e-12 | 3/48 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.52×** | +7.1 | 8e-11 | 35/48 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +7.0 | 2e-10 | 30/48 (A549, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.30×** | +6.3 | 1e-08 | 25/48 (A498, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.69×** | +4.7 | 1e-04 | 20/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.34×** | +4.6 | 2e-04 | 23/43 (NCI-H2030, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.29×** | +4.2 | 0.001 | 21/48 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.1 | 0.002 | 19/48 (SW1417, BT-474, …) | top dose only | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +3.7 | 0.007 | 19/48 (A-427, LoVo, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.007 | 17/47 (LoVo, C-33 A, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.48×** | +3.5 | 0.014 | 16/47 (PANC-1, HS-578T, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.024 | 15/47 (LoVo, SW480, …) | two highest doses | low cells (technical?) |
| [[Afatinib (drug)]] 5 µM |  | 1.20× | +3.2 | 0.031 | 13/49 (NCI-H23, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.031 | 14/48 (A498, HT-29, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.059 | 15/47 (RPMI-7951, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.059 | 13/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6328.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.590×** | -12.8 | 7e-35 | 38/48 (NCI-H2347, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.483×** | -12.5 | 3e-33 | 41/48 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.497×** | -11.5 | 2e-28 | 38/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.597×** | -8.9 | 1e-16 | 36/48 (A-427, SW48, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.615×** | -8.4 | 8e-15 | 35/48 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.735×** | -5.0 | 5e-05 | 25/47 (NCI-H2347, SW480, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.839× | -4.3 | 0.001 | 22/48 (RPMI-7951, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.788×** | -3.8 | 0.011 | 22/47 (A-172, A-427, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.829×** | -3.2 | 0.074 | 20/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6328. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 49.8 | 4 (1 ⚠) | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.65× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.555× (z -10.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.467× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 23.3 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 44.5 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.25× (z +9.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -10.0) |
| [[PANC-1 (line)]] | alt | 45.8 | 3 (3 ⚠) | 2 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.78× (z +11.8) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -10.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.444× (z -9.4) |
| [[LoVo (line)]] | wt | 30.3 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 3.14× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 46.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -17.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.321× (z -13.1) |
| [[A-427 (line)]] | wt | 86.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.244× (z -14.4) |
| [[CFPAC-1 (line)]] | alt | 35.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -13.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.245× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 34.8 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.331× (z -10.3) |
| [[HOP62 (line)]] | alt | 31.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -13.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.278× (z -10.6) |
| [[SW1417 (line)]] | alt | 33.4 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.21× (z +9.6) | — |
| [[A549 (line)]] | wt | 19.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +10.5) | — |
| [[HCT15 (line)]] | alt | 79.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -14.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.271× (z -10.3) |
| [[HS-578T (line)]] | alt | 43.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.04× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.306× (z -10.4) |
| [[KATO III (line)]] | alt | 27.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -10.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.323× (z -8.6) |
| [[SNU-423 (line)]] | alt | 49.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -10.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.342× (z -9.6) |
| [[A-172 (line)]] | wt | 39.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +8.5) | — |
| [[A498 (line)]] | wt | 23.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +10.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 53.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0950× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 33.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -10.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[C32 (line)]] | wt | 23.3 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.275× (z -8.5) |
| [[CHP-212 (line)]] | wt | 27.5 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0780× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 37.5 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.211× (z -9.3) |
| [[Hs 766T (line)]] | wt | 21.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -10.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[hTERT-HPNE (line)]] | wt | 40.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.232× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 27.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +10.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 40.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 31.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 51.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -9.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[RKO (line)]] | wt | 51.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +9.3) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 44.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -9.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[AsPC-1 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6328), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLBD2]] | +0.70 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[SBF1]] | +0.68 | +0.57 / +0.62 | both halves | 8e-06 |  |
| [[MAN2B2]] | +0.67 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[HECTD3]] | +0.66 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[CAPN1]] | +0.66 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[COLGALT1]] | +0.65 | +0.68 / +0.57 | both halves | 8e-06 |  |
| [[PLCB3]] | +0.64 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[CDS2]] | +0.64 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[NAGA]] | +0.63 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[INTS11]] | +0.62 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[NTAN1]] | +0.61 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[SH3GLB2]] | +0.61 | +0.62 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IWS1]] | -0.62 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[ERCC4]] | -0.62 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[PRPF38B]] | -0.59 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[HMGXB4]] | -0.59 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[RPP25L]] | -0.58 | -0.63 / -0.46 | both halves | 3e-05 |  |
| [[DDX52]] | -0.58 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[PPIG]] | -0.57 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[MRFAP1L1]] | -0.56 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[PPP4R2]] | -0.56 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[TRIP11]] | -0.56 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[EID2]] | -0.56 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[CEBPZ]] | -0.56 | -0.60 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD9]] | B | STARD9 activity raises ESYT1's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.36× lower at baseline in the lines without STARD9 | 0.034 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.593). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-8.3, -21.8); signed map (-46.9, -10.9). **Vector** length 123, 33.4% of its response variance represented; |z| ≥ 3 in 1,124 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.2 | +7.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +5.0 | +3.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.8 | +7.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.6 | +10.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.4 | +3.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.0 | +4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.5 | +3.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +3.3 | +3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.2 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.6 | -12.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -9.3 | -12.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.4 | -11.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.8 | -8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.4 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.3 | -8.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.2 | -3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | -5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | extended synaptotagmin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.2 — chr12:56,118,250-56,144,674 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MBC2, KIAA0747; previously FAM62A |
| Gene groups (HGNC) | Extended synaptotagmins |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 11 pathways, smallest: Glycosphingolipid transport; RHOF GTPase cycle; RHOD GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSJ8](https://www.uniprot.org/uniprotkb/Q9BSJ8) (Extended synaptotagmin-1):

> Binds calcium (via the C2 domains) and translocates to sites of contact between the endoplasmic reticulum and the cell membrane in response to increased cytosolic calcium levels. Helps tether the endoplasmic reticulum to the cell membrane and promotes the formation of appositions between the endoplasmic reticulum and the cell membrane. Acts as an inhibitor of ADGRD1 G protein-coupled receptor activity in absence of cytosolic calcium. Binds glycerophospholipids in a barrel-like domain and may …

**Summary**, from NCBI Gene [23344](https://www.ncbi.nlm.nih.gov/gene/23344):

> Enables identical protein binding activity and phospholipid transfer activity. Involved in intermembrane lipid transfer. Located in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29534](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29534) · Entrez [23344](https://www.ncbi.nlm.nih.gov/gene/23344) · UniProt [Q9BSJ8](https://www.uniprot.org/uniprotkb/Q9BSJ8) · Ensembl [ENSG00000139641](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139641)

## Data

Gene col 6328: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6328); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6328, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6328]; `tensor/DDL_lfc|DDL_z.npy` [6328]; `embed/gene_vectors.npy` [6328]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6328 or target_col == 6328). Every well: [[ESYT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ESYT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
