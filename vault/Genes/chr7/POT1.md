---
symbol: "POT1"
type: "gene"
col: 4887
ensembl_id: "ENSG00000128513"
name: "protection of telomeres 1"
location: "7q31.33"
module: 17
arm: "+"
pooled_cpm: 61.41
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 29
n_dd_up_clean: 0
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# POT1

*protection of telomeres 1* — 7q31.33

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.414× (z -21.4, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATG4C]] (+0.79, fdr 7e-06), [[ELP1]] (+0.77, fdr 7e-06), [[SKIC3]] (+0.76, fdr 1e-05); moves opposite to [[GCNT4]] (-0.67, fdr 3e-05), [[SPON1-AS1]] (-0.67, fdr 3e-05), [[MMADHC-DT]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[KATNAL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4887.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | 1.21× | +3.3 | 0.50 | 23/47 (LoVo, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4887.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.414×** | -21.4 | 0e+00 | 46/47 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.424×** | -14.7 | 0e+00 | 41/47 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.479×** | -12.6 | 4e-34 | 41/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.499×** | -11.9 | 1e-30 | 37/48 (CHP-212, A498, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.527×** | -11.0 | 7e-26 | 38/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.637×** | -10.9 | 1e-25 | 37/47 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.535×** | -10.3 | 6e-23 | 31/41 (HOP62, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.499×** | -10.1 | 4e-22 | 34/44 (C32, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.590×** | -9.0 | 1e-17 | 39/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.592×** | -9.0 | 2e-17 | 38/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.612×** | -8.4 | 3e-15 | 40/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.626×** | -7.7 | 7e-13 | 34/47 (A498, HOP62, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.638×** | -7.7 | 8e-13 | 30/47 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.641×** | -7.6 | 1e-12 | 37/47 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.635×** | -7.5 | 3e-12 | 36/47 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.653×** | -7.0 | 9e-11 | 32/48 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.765×** | -6.5 | 3e-09 | 34/47 (HOP62, A-172, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.759×** | -4.7 | 8e-05 | 31/46 (HOP62, CFPAC-1, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.795×** | -3.9 | 0.002 | 23/47 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.792×** | -3.7 | 0.004 | 23/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.865× | -3.4 | 0.012 | 14/48 (H4, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4887. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 61.1 | 0 | 13 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -16.9) |
| [[C32 (line)]] | wt | 152 | 0 | 12 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -18.9) |
| [[NCI-H460 (line)]] | wt | 68.8 | 0 | 12 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -23.0) |
| [[H4 (line)]] | wt | 89.1 | 0 | 10 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -17.9) |
| [[A-172 (line)]] | wt | 45.6 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -17.9) |
| [[A498 (line)]] | wt | 109 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -21.5) |
| [[HS-578T (line)]] | alt | 88.1 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -17.3) |
| [[MIA PaCa-2 (line)]] | alt | 72.6 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -19.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.257× (z -13.8) |
| [[SNU-423 (line)]] | alt | 61.8 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -15.9) |
| [[SW 900 (line)]] | alt | 79.1 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -12.3) |
| [[SW480 (line)]] | alt | 60.2 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.229× (z -17.9) |
| [[SW1417 (line)]] | alt | 61.0 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -16.1) |
| [[Hs 766T (line)]] | wt | 87.6 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 71.2 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 67.4 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -13.3) |
| [[NCI-H1792 (line)]] | alt | 94.7 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.298× (z -12.3) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 54.2 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 51.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -12.8) |
| [[C-33 A (line)]] | alt | 68.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.337× (z -8.9) |
| [[CHP-212 (line)]] | wt | 63.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0663× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Alpelisib (drug)]] 0.05 µM 0.173× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 49.6 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -13.6) |
| [[J82 (line)]] | alt | 59.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -11.4) |
| [[LoVo (line)]] | wt | 40.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.311× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 53.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -13.4) |
| [[NCI-H23 (line)]] | alt | 100 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 50.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -13.9) |
| [[A549 (line)]] | wt | 54.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -16.4) |
| [[CFPAC-1 (line)]] | alt | 60.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -17.6) |
| [[PANC-1 (line)]] | alt | 70.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -13.2) |
| [[RKO (line)]] | wt | 64.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -11.5) |
| [[SNU-1 (line)]] | wt | 64.0 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.322× (z -11.5) |
| [[SW 1088 (line)]] | alt | 170 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0693× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Flumatinib (mesylate) (drug)]] 0.05 µM 0.0702× (z -9.5) |
| [[A-427 (line)]] | wt | 59.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -13.9) |
| [[AN3 CA (line)]] | alt | 58.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -9.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 30.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -8.8) |
| [[HCT15 (line)]] | alt | 58.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.255× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 35.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -9.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 32.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -8.7) |
| [[KATO III (line)]] | alt | 25.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 27.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 46.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 36.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -14.2) |
| [[SW 1271 (line)]] | alt | 85.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -9.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.67 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4887), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG4C]] | +0.79 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[ELP1]] | +0.77 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[SKIC3]] | +0.76 | +0.77 / +0.50 | both halves | 1e-05 |  |
| [[HACE1]] | +0.75 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[HEATR6]] | +0.73 | +0.74 / +0.57 | both halves | 9e-06 |  |
| [[IFT172]] | +0.72 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[MRPS31P4]] | +0.72 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[ARL6]] | +0.70 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[RFC1]] | +0.69 | +0.68 / +0.43 | both halves | 3e-05 | pathway: Base Excision Repair; STRING 509 |
| [[CEP192]] | +0.69 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[METTL17]] | +0.68 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[ANAPC5]] | +0.68 | +0.69 / +0.52 | both halves | 1e-05 | pathway: Cellular Senescence |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCNT4]] | -0.67 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[SPON1-AS1]] | -0.67 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[MMADHC-DT]] | -0.65 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[GRIP1]] | -0.65 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[CCDC90B-AS1]] | -0.64 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[MCF2]] | -0.64 | -0.56 / -0.37 | both halves | 7e-05 |  |
| [[LINC01762]] | -0.63 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[PPP1R12A-AS2]] | -0.62 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[FBXL19-AS1]] | -0.62 | -0.54 / -0.29 | both halves | 3e-04 |  |
| [[HSD17B3]] | -0.62 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[SPHK1]] | -0.62 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[LINC00571]] | -0.61 | -0.50 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL1]] | B | KATNAL1 activity raises POT1's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 2.27× lower at baseline in the lines without KATNAL1 | 0.013 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[DYNC2H1]] | B | DYNC2H1 activity raises POT1's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 2.16× lower at baseline in the lines without DYNC2H1 | 0.032 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |
| [[TOP2A]] | B | TOP2A activity raises POT1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00888]] | B | LINC00888 activity raises POT1's level | lines that do not express LINC00888 (7) vs lines expressing it (43) | 1.77× lower at baseline in the lines without LINC00888 | 0.069 | ⚠ within organs, on part of the lines; co-absent genes; also absent: KIF3C, TBKBP1, GDAP1; maybe low, not absent |
| [[MGLL]] | B | MGLL activity lowers POT1's level | lines that do not express MGLL (14) vs lines expressing it (36) | 1.33× higher at baseline in the lines without MGLL | 0.089 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.738). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-2.7, -8.2); signed map (-29.1, -10.9). **Vector** length 91.3, 25.8% of its response variance represented; |z| ≥ 3 in 1,207 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Intraflagellar transport* (reactome, mean cos +0.53 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.2 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +2.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +1.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +0.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.5 | +0.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.5 | +0.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.0 | -21.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -11.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -6.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -1.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.3 | -4.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | protection of telomeres 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.33 — chr7:124,822,386-124,929,983 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hPot1, DKFZp586D211 |
| Gene groups (HGNC) | Shelterin complex |
| Reactome | 28 pathways, smallest: Telomere C-strand synthesis initiation; Removal of the Flap Intermediate from the C-strand; Packaging Of Telomere Ends |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUX5](https://www.uniprot.org/uniprotkb/Q9NUX5) (Protection of telomeres protein 1):

> Component of the telomerase ribonucleoprotein (RNP) complex that is essential for the replication of chromosome termini. Is a component of the double-stranded telomeric DNA-binding TRF1 complex which is involved in the regulation of telomere length by cis-inhibition of telomerase. Also acts as a single-stranded telomeric DNA-binding protein and thus may act as a downstream effector of the TRF1 complex and may transduce information about telomere maintenance and/or length to the telomere …

**Summary**, from NCBI Gene [25913](https://www.ncbi.nlm.nih.gov/gene/25913):

> This gene is a member of the telombin family and encodes a nuclear protein involved in telomere maintenance. Specifically, this protein functions as a member of a multi-protein complex that binds to the TTAGGG repeats of telomeres, regulating telomere length and protecting chromosome ends from illegitimate recombination, catastrophic chromosome instability, and abnormal chromosome segregation. Increased transcriptional expression of this gene is associated with stomach carcinogenesis and its …

**Accessions** — [HGNC:17284](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17284) · Entrez [25913](https://www.ncbi.nlm.nih.gov/gene/25913) · UniProt [Q9NUX5](https://www.uniprot.org/uniprotkb/Q9NUX5) · Ensembl [ENSG00000128513](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128513)

## Data

Gene col 4887: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4887); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4887, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4887]; `tensor/DDL_lfc|DDL_z.npy` [4887]; `embed/gene_vectors.npy` [4887]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4887 or target_col == 4887). Every well: [[POT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
