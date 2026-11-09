---
symbol: "NUDCD3"
type: "gene"
col: 297
ensembl_id: "ENSG00000015676"
name: "NudC domain containing 3"
location: "7p13"
module: 33
arm: "+"
pooled_cpm: 98.51
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# NUDCD3

*NudC domain containing 3* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.98× (z +7.5, q 5e-11, up in 36 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.565× (z -16.9, q 0e+00, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAMM41]] (+0.75, fdr 7e-06), [[ORC5]] (+0.73, fdr 7e-06), [[DDX55]] (+0.72, fdr 7e-06); moves opposite to [[STX17-DT]] (-0.59, fdr 4e-05), [[NPHS1]] (-0.58, fdr 2e-05), [[STARD4-AS1]] (-0.56, fdr 4e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 297.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.98×** | +7.5 | 5e-11 | 36/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +7.3 | 7e-11 | 38/48 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +6.1 | 2e-07 | 33/48 (NCI-H2347, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +5.9 | 7e-07 | 37/48 (HT-29, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +5.1 | 4e-05 | 29/48 (LoVo, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.004 | 26/48 (A498, NCI-H2347, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.7 | 0.019 | 19/48 (LoVo, NCI-H23, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +3.6 | 0.024 | 22/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.097 | 21/49 (BT-474, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 297.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.565×** | -16.9 | 0e+00 | 41/49 (A-172, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.561×** | -12.1 | 4e-31 | 42/49 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.514×** | -12.0 | 6e-31 | 37/44 (A-427, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.688×** | -7.2 | 8e-11 | 37/45 (RKO, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.717×** | -6.0 | 2e-07 | 28/50 (SK-MEL-2, A-172, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.757×** | -5.8 | 6e-07 | 25/48 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.731×** | -5.6 | 1e-06 | 31/47 (J82, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.779×** | -5.2 | 1e-05 | 30/48 (NCI-H460, SNU-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.854× | -4.6 | 2e-04 | 18/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.773×** | -4.6 | 2e-04 | 29/48 (A498, MIA PaCa-2, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.819×** | -4.2 | 0.002 | 22/48 (NCI-H460, HOP62, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.814×** | -3.7 | 0.010 | 24/48 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -3.5 | 0.019 | 21/49 (Panc 03.27, HEC-1-A, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.840× | -3.2 | 0.054 | 14/49 (NCI-H2030, A-427, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.899× | -3.1 | 0.068 | 6/48 (A549, HS-578T, …) | top dose only |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.901× | -3.1 | 0.080 | 5/49 (SW1417, SW 1088, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 297. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 76.0 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -15.9) |
| [[MIA PaCa-2 (line)]] | alt | 158 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -15.7) |
| [[A-172 (line)]] | wt | 130 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -19.9) |
| [[HEC-1-A (line)]] | alt | 126 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -22.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -17.3) |
| [[NCI-H460 (line)]] | wt | 87.7 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.360× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[C32 (line)]] | wt | 102 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.296× (z -13.9) |
| [[PANC-1 (line)]] | alt | 128 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 122 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -16.3) |
| [[SW1417 (line)]] | alt | 110 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -13.8) |
| [[SW480 (line)]] | alt | 117 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -12.9) |
| [[A498 (line)]] | wt | 158 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -17.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -16.5) |
| [[AN3 CA (line)]] | alt | 156 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -10.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 93.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -15.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -14.8) |
| [[J82 (line)]] | alt | 81.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -12.3) |
| [[LoVo (line)]] | wt | 105 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.88× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -16.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 108 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.462× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 111 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -9.8) |
| [[SNU-1 (line)]] | wt | 76.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -14.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 80.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -15.7) |
| [[H4 (line)]] | wt | 180 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -11.7) |
| [[LS 180 (line)]] | wt | 74.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.400× (z -9.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 82.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -19.4) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 161 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0612× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 0.168× (z -8.7) |
| [[A-427 (line)]] | wt | 90.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -24.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 92.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -13.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 126 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 49.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -10.3) |
| [[CHP-212 (line)]] | wt | 84.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -9.2) |
| [[COLO 205 (line)]] | alt | 56.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -15.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 74.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.382× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 77.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -14.1) |
| [[Panc 03.27 (line)]] | alt | 104 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -9.1) |
| [[SW 900 (line)]] | alt | 74.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -10.2) |
| [[SW48 (line)]] | wt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0770× (z -20.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 61.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 134 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 89.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 297), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAMM41]] | +0.75 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[ORC5]] | +0.73 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[DDX55]] | +0.72 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[MRPS23]] | +0.71 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[POLR3A]] | +0.68 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[PWP1]] | +0.67 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[NLE1]] | +0.66 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[DIS3L2]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[CTU1]] | +0.66 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[CHCHD6]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[DHODH]] | +0.65 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[GEMIN5]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX17-DT]] | -0.59 | -0.52 / -0.40 | both halves | 4e-05 |  |
| [[NPHS1]] | -0.58 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[STARD4-AS1]] | -0.56 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[ATP1B1]] | -0.56 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[PIK3R3]] | -0.55 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[ERO1B]] | -0.55 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[MKLN1-AS]] | -0.55 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[KANSL1L]] | -0.54 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[PEAK1]] | -0.54 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[GSTM3]] | -0.54 | -0.48 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NUDCD3's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers NUDCD3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.706). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-32.2, -7.7); signed map (-16.3, -22.1). **Vector** length 109, 31.3% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.7 | +7.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.4 | +5.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +3.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.6 | +7.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +6.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.0 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +2.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.3 | -16.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.0 | -4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.9 | -3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -3.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -2.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.7 | -0.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | NudC domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p13 — chr7:44,379,119-44,490,658 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1068, NudCL |
| Gene groups (HGNC) | NudC family |
| Matched by | ensembl_id |

UniProt [Q8IVD9](https://www.uniprot.org/uniprotkb/Q8IVD9) carries no function annotation.

**Summary**, from NCBI Gene [23386](https://www.ncbi.nlm.nih.gov/gene/23386):

> The product of this gene functions to maintain the stability of dynein intermediate chain. Depletion of this gene product results in aggregation and degradation of dynein intermediate chain, mislocalization of the dynein complex from kinetochores, spindle microtubules, and spindle poles, and loss of gamma-tubulin from spindle poles. The protein localizes to the Golgi apparatus during interphase, and levels of the protein increase after the G1/S transition. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:22208](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22208) · Entrez [23386](https://www.ncbi.nlm.nih.gov/gene/23386) · UniProt [Q8IVD9](https://www.uniprot.org/uniprotkb/Q8IVD9) · Ensembl [ENSG00000015676](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000015676)

## Data

Gene col 297: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 297); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 297, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 297]; `tensor/DDL_lfc|DDL_z.npy` [297]; `embed/gene_vectors.npy` [297]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 297 or target_col == 297). Every well: [[NUDCD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDCD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
