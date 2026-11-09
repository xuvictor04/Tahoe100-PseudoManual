---
symbol: "AP3M2"
type: "gene"
col: 960
ensembl_id: "ENSG00000070718"
name: "adaptor related protein complex 3 subunit mu 2"
location: "8p11.21"
module: 35
arm: "-"
pooled_cpm: 28.93
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# AP3M2

*adaptor related protein complex 3 subunit mu 2* — 8p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.22× (z +14.8, q 0e+00, up in 41 of 47 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.65× (z +9.2, q 3e-18, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.205× (z -41.7, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNA12]] (+0.71, fdr 1e-05), [[PPM1F]] (+0.69, fdr 1e-05), [[CKLF]] (+0.68, fdr 1e-05); moves opposite to [[C11orf71]] (-0.73, fdr 3e-05), [[TMEM202-AS1]] (-0.68, fdr 4e-05), [[KRCC1]] (-0.67, fdr 2e-05).
> It sits in the **-** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[KCNC4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 960.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.22×** | +14.8 | 0e+00 | 41/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.89×** | +11.9 | 5e-30 | 39/47 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.81×** | +11.0 | 6e-26 | 37/47 (LoVo, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +9.2 | 3e-18 | 37/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **1.40×** | +6.0 | 3e-07 | 23/44 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **1.37×** | +5.8 | 5e-07 | 25/43 (NCI-H460, LOX-IMVI, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.34×** | +5.5 | 4e-06 | 26/45 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **1.36×** | +5.4 | 4e-06 | 15/35 (LOX-IMVI, SW480, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +4.8 | 7e-05 | 18/47 (LOX-IMVI, SHP-77, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.65×** | +4.8 | 7e-05 | 20/47 (SW480, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.30×** | +4.8 | 7e-05 | 20/46 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +4.7 | 1e-04 | 17/47 (MIA PaCa-2, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 960.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.205×** | -41.7 | 0e+00 | 45/46 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.346×** | -19.7 | 0e+00 | 43/46 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.349×** | -18.8 | 0e+00 | 39/47 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.386×** | -9.3 | 3e-18 | 38/47 (HOP62, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.632×** | -8.5 | 2e-15 | 30/47 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.687×** | -7.0 | 3e-10 | 29/47 (SNU-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.775×** | -6.7 | 2e-09 | 26/47 (A-172, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.725×** | -6.0 | 2e-07 | 23/45 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.769×** | -5.8 | 3e-07 | 23/47 (HOP62, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.735×** | -5.7 | 6e-07 | 25/47 (HEC-1-A, Hs 766T, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.746×** | -5.5 | 2e-06 | 22/47 (HOP62, Hs 766T, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.770×** | -5.4 | 4e-06 | 25/47 (HOP62, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.805×** | -4.3 | 7e-04 | 23/47 (Hs 766T, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.852× | -4.2 | 9e-04 | 18/47 (Panc 03.27, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.858× | -4.0 | 0.002 | 18/47 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 0.861× | -4.0 | 0.003 | 13/47 (RKO, LOX-IMVI, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.669×** | -3.9 | 0.003 | 19/45 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.840× | -3.7 | 0.007 | 14/47 (LS 180, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 960. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 60.6 | 0 | 6 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0628× (z -27.7) |
| [[NCI-H460 (line)]] | wt | 17.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -22.2) |
| [[SW480 (line)]] | alt | 32.4 | 3 (3 ⚠) | 3 | [[Panobinostat (drug)]] 0.5 µM 2.88× (z +11.8) ⚠ cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -29.7) |
| [[HOP62 (line)]] | alt | 57.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0842× (z -28.3) |
| [[LoVo (line)]] | wt | 20.3 | 3 (3 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 3.05× (z +8.8) ⚠ cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -13.5) |
| [[SK-MEL-2 (line)]] | alt | 52.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0727× (z -28.2) |
| [[A498 (line)]] | wt | 24.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -23.0) |
| [[A549 (line)]] | wt | 24.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -20.6) |
| [[HEC-1-A (line)]] | alt | 27.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -17.2) |
| [[HS-578T (line)]] | alt | 47.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -17.9) |
| [[NCI-H2347 (line)]] | alt | 19.5 | 1 (1 ⚠) | 2 | [[Panobinostat (drug)]] 0.5 µM 2.94× (z +9.1) ⚠ cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -13.2) |
| [[PANC-1 (line)]] | alt | 15.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -21.2) |
| [[RKO (line)]] | wt | 32.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.162× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 32.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -15.2) |
| [[AsPC-1 (line)]] | alt | 14.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -13.0) |
| [[C32 (line)]] | wt | 23.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -9.2) |
| [[H4 (line)]] | wt | 36.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -12.3) |
| [[Hs 766T (line)]] | wt | 65.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -21.8) |
| [[hTERT-HPNE (line)]] | wt | 29.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -12.4) |
| [[J82 (line)]] | alt | 50.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -23.8) |
| [[KATO III (line)]] | alt | 46.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -18.7) |
| [[LOX-IMVI (line)]] | wt | 20.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -16.9) |
| [[LS 180 (line)]] | wt | 32.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -18.2) |
| [[MIA PaCa-2 (line)]] | alt | 25.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0948× (z -16.9) |
| [[NCI-H1792 (line)]] | alt | 31.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 45.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -28.8) |
| [[Panc 03.27 (line)]] | alt | 37.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -19.0) |
| [[SW 900 (line)]] | alt | 20.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0927× (z -18.4) |
| [[SW48 (line)]] | wt | 19.0 | 0 | 2 | — | [[Orlistat (drug)]] 0.05 µM 0.0817× (z -10.2) |
| [[A-427 (line)]] | wt | 28.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -17.6) |
| [[BT-474 (line)]] | alt | 21.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -17.1) |
| [[C-33 A (line)]] | alt | 40.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -19.0) |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -9.8) |
| [[HCT15 (line)]] | alt | 19.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 16.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -12.9) |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -14.4) |
| [[SHP-77 (line)]] | alt | 47.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -15.8) |
| [[SNU-1 (line)]] | wt | 29.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.149× (z -10.4) |
| [[SNU-423 (line)]] | alt | 21.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -19.5) |
| [[SW1417 (line)]] | alt | 25.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -16.6) |
| [[AN3 CA (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.87 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 960), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNA12]] | +0.71 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[PPM1F]] | +0.69 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[CKLF]] | +0.68 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[RNF168]] | +0.68 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[CMTM1]] | +0.67 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[KIF21B]] | +0.66 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[ATP13A2]] | +0.66 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[TBC1D24]] | +0.64 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[FANCA]] | +0.63 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[TREX2]] | +0.63 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[CASP2]] | +0.63 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[GPRIN1]] | +0.63 | +0.51 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf71]] | -0.73 | -0.74 / -0.46 | both halves | 3e-05 |  |
| [[TMEM202-AS1]] | -0.68 | -0.67 / -0.42 | both halves | 4e-05 |  |
| [[KRCC1]] | -0.67 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[N4BP2L1]] | -0.66 | -0.68 / -0.36 | both halves | 9e-05 |  |
| [[PIGP]] | -0.65 | -0.69 / -0.37 | both halves | 8e-05 |  |
| [[EIF4EBP3]] | -0.65 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[AK9]] | -0.64 | -0.63 / -0.39 | both halves | 6e-05 |  |
| [[BOLA1]] | -0.64 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[HHLA3]] | -0.64 | -0.65 / -0.32 | both halves | 2e-04 |  |
| [[PPP1R12A-AS2]] | -0.63 | -0.63 / -0.27 | both halves | 3e-04 |  |
| [[LINC00240]] | -0.63 | -0.62 / -0.33 | both halves | 1e-04 |  |
| [[DNAH12]] | -0.62 | -0.63 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNC4]] | B | KCNC4 activity raises AP3M2's level | lines that do not express KCNC4 (6) vs lines expressing it (44) | 1.68× lower at baseline in the lines without KCNC4 | 0.013 | ⚠ within organs, on part of the lines; also absent: CRTAP, FKBP7, SACS; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers AP3M2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers AP3M2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **-** arm (projection on the module's main direction -0.574). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (3.9, 4.9); signed map (-41.4, -10.2). **Vector** length 116, 31.4% of its response variance represented; |z| ≥ 3 in 1,207 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +7.6 | +11.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +6.7 | +14.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +6.3 | +11.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.1 | +9.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +5.0 | +5.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | +4.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.8 | -0.4 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | -1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -11.0 | -41.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.4 | -19.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.7 | -18.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.3 | -5.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -6.0 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.5 | -3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.5 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.3 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 3 subunit mu 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.21 — chr8:42,152,946-42,171,673 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CLA20, AP47B |
| Gene groups (HGNC) | Adaptor related protein complex 3 |
| Matched by | ensembl_id |

**Function**, from UniProt [P53677](https://www.uniprot.org/uniprotkb/P53677) (AP-3 complex subunit mu-2):

> Part of the AP-3 complex, an adaptor-related complex which is not clathrin-associated. The complex is associated with the Golgi region as well as more peripheral structures. It facilitates the budding of vesicles from the Golgi membrane and may be directly involved in trafficking to lysosomes. In concert with the BLOC-1 complex, AP-3 is required to target cargos into vesicles assembled at cell bodies for delivery into neurites and nerve terminals.

**Summary**, from NCBI Gene [10947](https://www.ncbi.nlm.nih.gov/gene/10947):

> This gene encodes a subunit of the heterotetrameric adaptor-related protein comlex 3 (AP-3), which belongs to the adaptor complexes medium subunits family. The AP-3 complex plays a role in protein trafficking to lysosomes and specialized organelles. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Aug 2008]

**Accessions** — [HGNC:570](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:570) · Entrez [10947](https://www.ncbi.nlm.nih.gov/gene/10947) · UniProt [P53677](https://www.uniprot.org/uniprotkb/P53677) · Ensembl [ENSG00000070718](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070718)

## Data

Gene col 960: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 960); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 960, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 960]; `tensor/DDL_lfc|DDL_z.npy` [960]; `embed/gene_vectors.npy` [960]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 960 or target_col == 960). Every well: [[AP3M2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP3M2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
