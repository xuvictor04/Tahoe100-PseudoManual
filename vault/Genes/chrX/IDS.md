---
symbol: "IDS"
type: "gene"
col: 210
ensembl_id: "ENSG00000010404"
name: "iduronate 2-sulfatase"
location: "Xq28"
module: 50
arm: "+"
pooled_cpm: 97.42
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# IDS

*iduronate 2-sulfatase* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.65× (z +11.0, q 2e-25, up in 39 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.20× (z +5.7, q 1e-06, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.536× (z -19.4, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSAP]] (+0.71, fdr 7e-06), [[CTSB]] (+0.66, fdr 1e-05), [[BSG]] (+0.66, fdr 1e-05); moves opposite to [[BRIX1]] (-0.66, fdr 7e-06), [[TOE1]] (-0.64, fdr 1e-05), [[MTG2]] (-0.60, fdr 7e-06).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 210.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +11.0 | 2e-25 | 39/49 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +10.8 | 7e-25 | 34/44 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +6.5 | 1e-08 | 27/45 (RKO, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.22×** | +6.3 | 3e-08 | 24/48 (J82, A498, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +5.7 | 1e-06 | 23/48 (SW480, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +5.1 | 4e-05 | 25/49 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.20×** | +4.1 | 0.004 | 21/48 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +3.6 | 0.020 | 23/48 (KATO III, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.6 | 0.020 | 20/48 (SW480, SW1417, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.5 | 0.023 | 21/48 (KATO III, SW480, …) | all doses, flat |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.086 | 14/48 (HEC-1-A, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.086 | 22/47 (NCI-H23, C32, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 210.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.536×** | -19.4 | 0e+00 | 41/48 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.582×** | -11.9 | 6e-30 | 35/47 (NCI-H661, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.592×** | -11.1 | 3e-26 | 41/48 (Hs 766T, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.912× | -6.8 | 1e-09 | 4/50 (NCI-H661, AN3 CA, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.782×** | -5.4 | 8e-06 | 27/48 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.783×** | -5.4 | 8e-06 | 28/48 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~14% of this change | **0.783×** | -5.1 | 2e-05 | 25/47 (C32, SW48, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.801×** | -4.9 | 9e-05 | 23/48 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.802×** | -4.6 | 2e-04 | 24/49 (NCI-H2030, SW 900, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | **0.802×** | -4.6 | 2e-04 | 25/47 (H4, SNU-423, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.863× | -4.5 | 3e-04 | 19/48 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.813×** | -4.3 | 9e-04 | 21/48 (SNU-423, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.847× | -3.6 | 0.012 | 22/48 (NCI-H460, Hs 766T, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.847× | -3.6 | 0.012 | 19/48 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.849× | -3.6 | 0.013 | 20/48 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.860× | -3.3 | 0.035 | 9/48 (CFPAC-1, C32, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.751×** | -3.3 | 0.035 | 14/48 (NCI-H23, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.864× | -3.2 | 0.044 | 16/48 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.902× | -3.2 | 0.044 | 15/48 (SNU-1, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 210. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 131 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.77× (z +11.7) ⚠ toxic; transcription drop | [[Clobetasol propionate (drug)]] 0.5 µM 0.468× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 148 | 2 (2 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +9.9) ⚠ cell-cycle shift, explains ~51% of this change | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -18.3) |
| [[PANC-1 (line)]] | alt | 93.8 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.30× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -15.9) |
| [[SW480 (line)]] | alt | 60.7 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.09× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 105 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -14.3) |
| [[NCI-H1792 (line)]] | alt | 83.5 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.07× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -13.7) |
| [[A-427 (line)]] | wt | 75.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -11.8) |
| [[C32 (line)]] | wt | 56.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -12.6) |
| [[H4 (line)]] | wt | 136 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -12.6) |
| [[A549 (line)]] | wt | 93.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -10.4) |
| [[BT-474 (line)]] | alt | 52.2 | 0 | 2 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.191× (z -11.7) ⚠ toxic · without an alert: [[Neratinib (drug)]] 0.05 µM 0.312× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 64.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -11.2) |
| [[HOP62 (line)]] | alt | 136 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -10.6) |
| [[Hs 766T (line)]] | wt | 178 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -15.2) |
| [[HT-29 (line)]] | alt | 116 | 2 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.71× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 83.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -18.3) |
| [[NCI-H2030 (line)]] | alt | 160 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -17.0) |
| [[NCI-H23 (line)]] | alt | 130 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.473× (z -10.0) |
| [[SHP-77 (line)]] | alt | 54.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.24× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 84.3 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0762× (z -12.1) ⚠ toxic · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.466× (z -9.7) |
| [[SNU-423 (line)]] | alt | 142 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -17.7) |
| [[SW 900 (line)]] | alt | 241 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +11.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 159 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 82.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.50× (z +9.7) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 73.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -18.3) |
| [[COLO 205 (line)]] | alt | 60.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +12.5) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 87.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -12.5) |
| [[HepG2_C3A (line)]] | wt | 63.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -9.2) |
| [[HS-578T (line)]] | alt | 94.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -14.4) |
| [[J82 (line)]] | alt | 80.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -11.6) |
| [[KATO III (line)]] | alt | 54.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -14.9) |
| [[LoVo (line)]] | wt | 41.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.69× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 83.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -15.5) |
| [[NCI-H661 (line)]] | alt | 83.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0990× (z -12.9) |
| [[RKO (line)]] | wt | 49.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.99× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 190 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.600× (z -9.0) |
| [[SW 1271 (line)]] | alt | 149 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0615× (z -10.5) |
| [[SW48 (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.339× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~14% of this change |
| [[AN3 CA (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 75.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 103 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 70.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 210), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSAP]] | +0.71 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[CTSB]] | +0.66 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[BSG]] | +0.66 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[DYNLT3]] | +0.64 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[ALDOA]] | +0.62 | +0.73 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_HYPOXIA |
| [[TMEM30A]] | +0.61 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[TMED4]] | +0.61 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[MMP2]] | +0.60 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[PLTP]] | +0.60 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[SARAF]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[TMBIM6]] | +0.59 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[LAMP2]] | +0.59 | +0.49 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRIX1]] | -0.66 | -0.59 / -0.70 | both halves | 7e-06 |  |
| [[TOE1]] | -0.64 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[MTG2]] | -0.60 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[CCDC137]] | -0.59 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[PPIG]] | -0.59 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[MRM2]] | -0.57 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[IWS1]] | -0.57 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[C1orf131]] | -0.57 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[BAZ1B]] | -0.56 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[SART3]] | -0.55 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[NSUN4]] | -0.54 | -0.36 / -0.56 | both halves | 9e-05 |  |
| [[CRCP]] | -0.54 | -0.55 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers IDS's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.8, -20.5); signed map (-10.4, 39.4). **Vector** length 138, 41.6% of its response variance represented; |z| ≥ 3 in 1,142 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Degradation of the extracellular matrix* (reactome, mean cos +0.50 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +11.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +5.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.5 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +3.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.4 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +0.2 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.7 | +3.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.4 | -19.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.9 | -11.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -11.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -5.3 | -5.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.8 | -4.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.2 | -4.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.5 | -4.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | -3.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | iduronate 2-sulfatase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:149,476,988-149,521,096 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ID2S; previously SIDS |
| Gene groups (HGNC) | Sulfatases |
| Hallmark sets | HYPOXIA |
| Reactome | 9 pathways, smallest: Mucopolysaccharidoses; CS/DS degradation; HS-GAG degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P22304](https://www.uniprot.org/uniprotkb/P22304) (Iduronate 2-sulfatase):

> Lysosomal enzyme involved in the degradation pathway of dermatan sulfate and heparan sulfate.

**Summary**, from NCBI Gene [3423](https://www.ncbi.nlm.nih.gov/gene/3423):

> This gene encodes a member of the sulfatase family of proteins. The encoded preproprotein is proteolytically processed to generate two polypeptide chains. This enzyme is involved in the lysosomal degradation of heparan sulfate and dermatan sulfate. Mutations in this gene are associated with the X-linked lysosomal storage disease mucopolysaccharidosis type II, also known as Hunter syndrome. Alternative splicing results in multiple transcript variants, at least one of which encodes a …

**Accessions** — [HGNC:5389](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5389) · Entrez [3423](https://www.ncbi.nlm.nih.gov/gene/3423) · UniProt [P22304](https://www.uniprot.org/uniprotkb/P22304) · Ensembl [ENSG00000010404](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000010404)

## Data

Gene col 210: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 210); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 210, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 210]; `tensor/DDL_lfc|DDL_z.npy` [210]; `embed/gene_vectors.npy` [210]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 210 or target_col == 210). Every well: [[IDS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IDS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
