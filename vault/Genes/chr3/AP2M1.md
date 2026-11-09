---
symbol: "AP2M1"
type: "gene"
col: 8420
ensembl_id: "ENSG00000161203"
name: "adaptor related protein complex 2 subunit mu 1"
location: "3q27.1"
module: 25
arm: "+"
pooled_cpm: 66.72
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 5
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# AP2M1

*adaptor related protein complex 2 subunit mu 1* — 3q27.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.64× (z +16.3, q 0e+00, up in 47 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.26× (z +4.1, q 0.004, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.660× (z -7.5, q 4e-11, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VAMP3]] (+0.76, fdr 7e-06), [[TWF1]] (+0.76, fdr 7e-06), [[TGOLN2]] (+0.75, fdr 7e-06); moves opposite to [[NSUN5P2-1]] (-0.70, fdr 7e-06, ⚠ NSUN5P2-1 in the vector space only through flagged drug-doses), [[CTBP1-AS]] (-0.69, fdr 1e-05, ⚠ CTBP1-AS in the vector space only through flagged drug-doses), [[SNHG8]] (-0.65, fdr 1e-05), [[CROCCP2-1]] (-0.65, fdr 9e-06), [[PRPF38B]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8420.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.64×** | +16.3 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.75×** | +16.1 | 0e+00 | 42/42 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.71×** | +11.7 | 4e-29 | 43/44 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.52×** | +5.1 | 5e-05 | 38/49 (MIA PaCa-2, SNU-423, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.46×** | +4.8 | 2e-04 | 33/48 (PANC-1, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.41×** | +4.4 | 0.001 | 30/48 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.004 | 32/48 (A-172, SNU-1, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.33×** | +3.6 | 0.025 | 30/48 (LOX-IMVI, SW 900, …) | inconsistent across doses | position effect removed |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.32×** | +3.5 | 0.029 | 26/48 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.030 | 26/48 (BT-474, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.51×** | +3.3 | 0.049 | 24/47 (A-427, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.054 | 24/48 (A-427, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.29×** | +3.1 | 0.096 | 22/47 (MIA PaCa-2, SW1417, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.27×** | +3.0 | 0.097 | 23/48 (PANC-1, SW480, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8420.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.660×** | -7.5 | 4e-11 | 37/48 (A-427, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.663×** | -5.2 | 5e-05 | 33/48 (hTERT-HPNE, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.715×** | -4.3 | 0.004 | 31/48 (A-172, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.728×** | -4.0 | 0.007 | 32/48 (Panc 03.27, H4, …) | all doses, flat | cell-cycle shift (explains ~21% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.801×** | -4.0 | 0.007 | 25/48 (KATO III, A498, …) | all doses, flat | position effect removed |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.788× | -3.0 | 0.22 | 25/48 (NCI-H23, A-427, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8420. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 65.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.72× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -8.8) |
| [[HOP62 (line)]] | alt | 88.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -9.6) |
| [[J82 (line)]] | alt | 129 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 41.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 8.08× (z +15.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -13.0) |
| [[NCI-H2347 (line)]] | alt | 85.5 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +11.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 141 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +11.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 103 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -17.5) |
| [[A498 (line)]] | wt | 90.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.94× (z +14.1) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 51.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.54× (z +12.6) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 84.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +12.3) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 149 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +12.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 42.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.39× (z +11.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 71.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +13.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 82.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +13.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -10.4) |
| [[PANC-1 (line)]] | alt | 49.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.39× (z +16.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 74.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -10.0) |
| [[SNU-423 (line)]] | alt | 56.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +11.7) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 60.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -8.6) |
| [[SW480 (line)]] | alt | 57.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +16.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 50.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.23× (z +11.4) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 107 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +10.7) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 53.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.62× (z +10.9) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 28.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.91× (z +15.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 85.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +10.3) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 43.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +11.2) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 56.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +11.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 41.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.32× (z +13.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 80.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 37.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.56× (z +12.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 71.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -12.9) |
| [[SW1417 (line)]] | alt | 59.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.58× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 41.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +9.9) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 27.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.36× (z +10.5) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 49.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -9.5) |
| [[Hs 766T (line)]] | wt | 41.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.4) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 101 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.272× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 28.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -10.9) |
| [[NCI-H661 (line)]] | alt | 38.3 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0853× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 116 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 44.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 32.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.03× (z +11.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 82.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8420), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VAMP3]] | +0.76 | +0.71 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 608 |
| [[TWF1]] | +0.76 | +0.70 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[TGOLN2]] | +0.75 | +0.64 / +0.80 | both halves | 7e-06 | pathway: Cargo recognition for clathrin-mediated endocytosis; STRING 988 |
| [[EIF4H]] | +0.72 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[NAGA]] | +0.72 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[PGRMC1]] | +0.71 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[GPS1]] | +0.71 | +0.75 / +0.56 | both halves | 1e-05 | pathway: Cargo recognition for clathrin-mediated endocytosis |
| [[PIGT]] | +0.71 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[MOB1A]] | +0.70 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[COPS6]] | +0.70 | +0.67 / +0.64 | both halves | 7e-06 | pathway: Cargo recognition for clathrin-mediated endocytosis |
| [[LIN7C]] | +0.70 | +0.66 / +0.67 | both halves | 7e-06 | pathway: Neuronal System |
| [[MMGT1]] | +0.69 | +0.58 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSUN5P2-1]] ⚠ | -0.70 | -0.59 / -0.69 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[CTBP1-AS]] ⚠ | -0.69 | -0.57 / -0.62 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG8]] | -0.65 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | -0.65 | -0.62 / -0.57 | both halves | 9e-06 |  |
| [[PRPF38B]] | -0.63 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[ZBTB7A]] | -0.63 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[MRPL33]] | -0.62 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[NSUN5P1-1]] | -0.62 | -0.51 / -0.68 | both halves | 1e-05 |  |
| [[SNHG9]] | -0.61 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[SNHG6]] | -0.61 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.60 | -0.58 / -0.54 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SELENOH]] | -0.60 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[COX17]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[SNHG25]] | -0.60 | -0.47 / -0.68 | both halves | 2e-05 |  |
| [[ZNF316]] | -0.59 | -0.56 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AP2M1's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.717). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-28.4, -21.9); signed map (-20.9, -37.5). **Vector** length 112, 33.7% of its response variance represented; |z| ≥ 3 in 783 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.7 | +1.8 |
|  | [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.4 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +16.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +3.1 | +1.2 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | +3.0 | +1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +2.8 | +0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +2.7 | +0.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.9 | -7.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.5 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.3 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.7 | -2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -4.1 | -2.3 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -3.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 2 subunit mu 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.1 — chr3:184,174,689-184,184,214 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AP50, mu2; previously CLAPM1 |
| Gene groups (HGNC) | Adaptor related protein complex 2 |
| Hallmark sets | PROTEIN_SECRETION, PI3K_AKT_MTOR_SIGNALING |
| Reactome | 47 pathways, smallest: Nef Mediated CD8 Down-regulation; Nef Mediated CD4 Down-regulation; Formation of annular gap junctions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CW1](https://www.uniprot.org/uniprotkb/Q96CW1) (AP-2 complex subunit mu):

> Component of the adaptor protein complex 2 (AP-2). Adaptor protein complexes function in protein transport via transport vesicles in different membrane traffic pathways. Adaptor protein complexes are vesicle coat components and appear to be involved in cargo selection and vesicle formation. AP-2 is involved in clathrin-dependent endocytosis in which cargo proteins are incorporated into vesicles surrounded by clathrin (clathrin-coated vesicles, CCVs) which are destined for fusion with the early …

**Summary**, from NCBI Gene [1173](https://www.ncbi.nlm.nih.gov/gene/1173):

> This gene encodes a subunit of the heterotetrameric coat assembly protein complex 2 (AP2), which belongs to the adaptor complexes medium subunits family. The encoded protein is required for the activity of a vacuolar ATPase, which is responsible for proton pumping occurring in the acidification of endosomes and lysosomes. The encoded protein may also play an important role in regulating the intracellular trafficking and function of CTLA-4 protein. Three transcript variants encoding different …

**Accessions** — [HGNC:564](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:564) · Entrez [1173](https://www.ncbi.nlm.nih.gov/gene/1173) · UniProt [Q96CW1](https://www.uniprot.org/uniprotkb/Q96CW1) · Ensembl [ENSG00000161203](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161203)

## Data

Gene col 8420: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8420); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8420, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8420]; `tensor/DDL_lfc|DDL_z.npy` [8420]; `embed/gene_vectors.npy` [8420]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8420 or target_col == 8420). Every well: [[AP2M1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP2M1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
