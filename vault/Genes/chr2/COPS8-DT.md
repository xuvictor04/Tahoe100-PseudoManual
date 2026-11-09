---
symbol: "COPS8-DT"
type: "gene"
col: 13580
ensembl_id: "ENSG00000227252"
name: "COPS8 divergent transcript"
location: "2q37.3"
module: 146
arm: "+"
pooled_cpm: 6.12
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 21
n_dd_up_clean: 16
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# COPS8-DT

*COPS8 divergent transcript* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 2.13× (z +5.9, q 2e-06, up in 27 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.284× (z -13.9, q 3e-41, down in 36 of 41 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.278× (z -10.0, q 2e-21, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGEF7]] (+0.62, fdr 4e-05), [[LINC03006-1]] (+0.61, fdr 1e-05), [[PRDX6-AS1]] (+0.61, fdr 1e-05); moves opposite to [[DLGAP4]] (-0.59, fdr 1e-05), [[ARID5A]] (-0.51, fdr 4e-05), [[ZNF674]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[KLRG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13580.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **2.13×** | +5.9 | 2e-06 | 27/46 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.91×** | +5.1 | 1e-04 | 26/47 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.52×** | +4.6 | 6e-04 | 16/47 (NCI-H460, RKO, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.76×** | +4.5 | 0.001 | 17/45 (NCI-H1792, LS 180, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.84×** | +4.1 | 0.005 | 19/46 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +4.1 | 0.005 | 17/38 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.42×** | +3.9 | 0.008 | 19/41 (A549, PANC-1, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.94×** | +3.8 | 0.009 | 11/47 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.65×** | +3.8 | 0.009 | 10/42 (LoVo, SW480, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.61×** | +3.8 | 0.009 | 12/46 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.92×** | +3.7 | 0.010 | 15/45 (NCI-H1573, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.019 | 13/46 (A498, H4, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.32×** | +3.4 | 0.024 | 8/43 (SW480, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +3.4 | 0.027 | 12/46 (CFPAC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.65×** | +3.4 | 0.029 | 11/42 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.040 | 10/46 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.075 | 9/46 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.50×** | +3.0 | 0.080 | 4/46 (C-33 A, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13580.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.284×** | -13.9 | 3e-41 | 36/41 (LoVo, Panc 03.27, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.256×** | -10.3 | 3e-22 | 38/45 (NCI-H23, HOP62, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.278×** | -10.0 | 2e-21 | 41/47 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.337×** | -8.5 | 3e-15 | 29/39 (NCI-H1792, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.374×** | -7.7 | 2e-12 | 27/37 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.381×** | -7.6 | 4e-12 | 36/46 (Hs 766T, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.386×** | -6.4 | 1e-08 | 25/44 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.394×** | -6.3 | 3e-08 | 26/45 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.451×** | -6.2 | 3e-08 | 28/46 (A549, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.485×** | -4.9 | 7e-05 | 22/44 (C-33 A, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.679×** | -4.3 | 0.001 | 22/46 (Panc 03.27, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.481×** | -4.2 | 0.002 | 16/47 (NCI-H23, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.598×** | -4.0 | 0.003 | 18/46 (NCI-H23, J82, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.588×** | -3.9 | 0.004 | 17/43 (SW480, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.612×** | -3.8 | 0.005 | 17/47 (HEC-1-A, NCI-H460, …) | two highest doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.420×** | -3.5 | 0.013 | 16/35 (HEC-1-A, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.646×** | -3.3 | 0.033 | 16/45 (RKO, AsPC-1, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.665×** | -3.0 | 0.074 | 9/45 (SHP-77, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.83 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13580. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 15.9 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0443× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.104× (z -10.5) |
| [[A498 (line)]] | wt | 9.72 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -11.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HOP62 (line)]] | alt | 6.53 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0565× (z -11.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 9.77 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0735× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.126× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 9.78 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0600× (z -10.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 8.35 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0603× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 3.77 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -9.1) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A-172 (line)]] | wt | 5.20 | 0 | 1 | — | [[Roxadustat (drug)]] 5 µM 0.0454× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 6.93 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -12.8) ⚠ cell-cycle shift, explains ~42% of this change |
| [[J82 (line)]] | alt | 4.24 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0972× (z -10.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[LoVo (line)]] | wt | 7.04 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -13.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0782× (z -9.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Panc 03.27 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -13.3) ⚠ cell-cycle shift, explains ~42% of this change |
| [[PANC-1 (line)]] | alt | 3.67 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -9.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SNU-423 (line)]] | alt | 6.30 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0948× (z -10.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SW48 (line)]] | wt | 10.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0440× (z -8.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.26 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13580), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF7]] | +0.62 | +0.40 / +0.51 | both halves | 4e-05 |  |
| [[LINC03006-1]] | +0.61 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[PRDX6-AS1]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[NUDT13]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CUL2]] | +0.57 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[SCAF4]] | +0.56 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[PPP1CB]] | +0.56 | +0.36 / +0.49 | both halves | 9e-05 |  |
| [[MSL2]] | +0.56 | +0.57 / +0.36 | both halves | 1e-04 |  |
| [[GVQW3]] | +0.56 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[COPS7B]] | +0.55 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[KLRG1]] | +0.55 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[FAM174A-DT]] | +0.54 | +0.62 / +0.41 | both halves | 4e-05 | same gene group |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLGAP4]] | -0.59 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[ARID5A]] | -0.51 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[ZNF674]] | -0.50 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[TBRG1]] | -0.50 | -0.45 / -0.25 | both halves | 4e-04 |  |
| [[KBTBD8]] | -0.49 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[STK10]] | -0.49 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[CCSER2]] | -0.48 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[ARVCF]] | -0.48 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[C6orf62]] | -0.48 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[NPIPP1]] | -0.47 | -0.37 / -0.29 | both halves | 2e-04 |  |
| [[GLRX2]] | -0.47 | -0.39 / -0.25 | both halves | 4e-04 |  |
| [[RNF34]] | -0.47 | -0.41 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLRG1]] | B | KLRG1 activity raises COPS8-DT's level | lines that do not express KLRG1 (8) vs lines expressing it (42) | 1.72× lower at baseline in the lines without KLRG1 | 0.027 | ⚠ within organs, on part of the lines; also absent: DUXAP10, CD226, DUXAP8; maybe low, not absent |
| [[FBXO15]] | B | FBXO15 activity raises COPS8-DT's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 1.56× lower at baseline in the lines without FBXO15 | 0.097 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |
| [[TMCC1-DT]] | C | TMCC1-DT activity raises COPS8-DT's level | lines that do not express TMCC1-DT (3) vs lines expressing it (47) | 2.43× lower at baseline in the lines without TMCC1-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, WWOX, DBNDD1; maybe low, not absent; its own permutation p |
| [[LRRIQ3]] | C | LRRIQ3 activity raises COPS8-DT's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 1.97× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.480). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-5.6, -13.4); signed map (-35.4, -20.1). **Vector** length 60.2, 10.4% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.6 | +1.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.7 | -2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.3 | +0.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.1 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | -2.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | +3.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -4.7 | -13.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.1 | -10.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.8 | -8.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.9 | -7.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -3.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -0.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | COPS8 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q37.3 — chr2:236,910,797-237,085,838 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55816](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55816) · Entrez [105373951](https://www.ncbi.nlm.nih.gov/gene/105373951) · Ensembl [ENSG00000227252](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227252)

## Data

Gene col 13580: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13580); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13580, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13580]; `tensor/DDL_lfc|DDL_z.npy` [13580]; `embed/gene_vectors.npy` [13580]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13580 or target_col == 13580). Every well: [[COPS8-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COPS8-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
