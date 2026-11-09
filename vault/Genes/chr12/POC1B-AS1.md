---
symbol: "POC1B-AS1"
type: "gene"
col: 15662
ensembl_id: "ENSG00000270344"
name: "POC1B antisense RNA 1"
location: "12q21.33"
module: 15
arm: "+"
pooled_cpm: 9.6
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 30
n_dd_up_clean: 5
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# POC1B-AS1

*POC1B antisense RNA 1* — 12q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.75× (z +16.0, q 0e+00, up in 42 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.228× (z -16.6, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLUD1P3]] (+0.68, fdr 2e-05), [[MOSMO]] (+0.66, fdr 1e-05), [[LEMD3]] (+0.64, fdr 6e-05); moves opposite to [[STARD5]] (-0.60, fdr 4e-05), [[MOSPD2]] (-0.59, fdr 1e-04), [[ARRB2]] (-0.58, fdr 8e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15662.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.75×** | +16.0 | 0e+00 | 42/44 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +6.8 | 3e-09 | 27/43 (LOX-IMVI, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.0 | 1e-04 | 21/48 (A-172, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.2 | 0.004 | 18/45 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +4.0 | 0.007 | 16/47 (LS 180, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.32× | +3.1 | 0.16 | 11/46 (A549, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15662.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.228×** | -16.6 | 0e+00 | 44/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.392×** | -14.9 | 0e+00 | 37/46 (A-172, SNU-423, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.342×** | -12.0 | 5e-31 | 36/44 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.359×** | -11.1 | 3e-26 | 32/46 (A498, LOX-IMVI, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.387×** | -10.7 | 2e-24 | 37/47 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.434×** | -9.4 | 7e-19 | 38/47 (Hs 766T, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.453×** | -8.9 | 6e-17 | 34/47 (HepG2/C3A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.450×** | -8.6 | 6e-16 | 29/39 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.282×** | -7.4 | 8e-12 | 35/46 (SHP-77, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.536×** | -7.0 | 1e-10 | 28/46 (HEC-1-A, Hs 766T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.571×** | -6.3 | 2e-08 | 26/42 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.345×** | -6.2 | 2e-08 | 26/41 (SW 900, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.586×** | -6.0 | 9e-08 | 23/46 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.590×** | -5.9 | 1e-07 | 26/47 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.608×** | -5.6 | 9e-07 | 23/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.638×** | -5.0 | 2e-05 | 20/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.623×** | -5.0 | 2e-05 | 24/44 (HEC-1-A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.674×** | -4.4 | 3e-04 | 19/47 (SNU-1, Panc 03.27, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.690×** | -4.2 | 8e-04 | 18/47 (BT-474, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15662. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 7.57 | 1 | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +9.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0647× (z -14.9) |
| [[HOP62 (line)]] | alt | 10.9 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.0264× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0851× (z -13.2) |
| [[Hs 766T (line)]] | wt | 17.6 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0981× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.170× (z -9.7) |
| [[LoVo (line)]] | wt | 21.1 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +9.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0801× (z -17.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -15.2) |
| [[LOX-IMVI (line)]] | wt | 11.3 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +11.7) | [[Digitoxin (drug)]] 5 µM 0.135× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.167× (z -9.8) |
| [[PANC-1 (line)]] | alt | 6.27 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.152× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.191× (z -8.9) |
| [[A-172 (line)]] | wt | 9.95 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -15.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.115× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 12.8 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0352× (z -13.3) |
| [[SNU-423 (line)]] | alt | 10.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0813× (z -15.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0896× (z -10.3) |
| [[SW480 (line)]] | alt | 9.19 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.133× (z -12.3) |
| [[A498 (line)]] | wt | 7.81 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +9.8) | [[Harringtonine (drug)]] 5 µM 0.0868× (z -11.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[COLO 205 (line)]] | alt | 16.6 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.117× (z -9.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 7.43 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +8.9) | [[Ixazomib citrate (drug)]] 0.5 µM 0.169× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 8.25 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0457× (z -12.5) |
| [[SNU-1 (line)]] | wt | 9.94 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0294× (z -11.7) |
| [[A549 (line)]] | wt | 9.86 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -9.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[BT-474 (line)]] | alt | 5.64 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -10.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[C32 (line)]] | wt | 11.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -9.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[H4 (line)]] | wt | 11.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0759× (z -8.8) |
| [[HCT15 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0989× (z -8.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 4.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.61× (z +9.6) | — |
| [[J82 (line)]] | alt | 6.65 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0802× (z -11.2) |
| [[LS 180 (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -10.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 7.33 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.113× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -9.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -8.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 5.55 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0331× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 9.88 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -11.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW 900 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -10.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW1417 (line)]] | alt | 7.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +9.0) | — |
| [[A-427 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15662), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLUD1P3]] | +0.68 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[MOSMO]] | +0.66 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[LEMD3]] | +0.64 | +0.43 / +0.38 | both halves | 6e-05 |  |
| [[MSANTD2]] | +0.63 | +0.56 / +0.37 | both halves | 8e-05 |  |
| [[PHC2-AS1]] | +0.63 | +0.39 / +0.56 | both halves | 5e-05 | same gene group |
| [[LINC01909]] | +0.62 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ZNF213-AS1]] | +0.62 | +0.46 / +0.45 | both halves | 3e-05 | same gene group |
| [[CCNJ]] | +0.61 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[ANXA2R-OT1]] | +0.61 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[LINC01829]] | +0.60 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[LENG8-AS1]] | +0.60 | +0.43 / +0.48 | both halves | 3e-05 | same gene group |
| [[GTF3C2-AS2]] | +0.60 | +0.54 / +0.34 | both halves | 1e-04 | same gene group |

## Genes that move opposite

*17 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STARD5]] | -0.60 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[MOSPD2]] | -0.59 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[ARRB2]] | -0.58 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[RPAP3]] | -0.57 | -0.24 / -0.53 | both halves | 4e-04 |  |
| [[ALAD]] | -0.57 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[ATP1A3]] | -0.56 | -0.22 / -0.41 | both halves | 6e-04 |  |
| [[HLTF]] | -0.54 | -0.20 / -0.49 | ⚠ not reproduced | 7e-04 |  |
| [[NSFL1C]] | -0.53 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[NDRG3]] | -0.52 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[SPTAN1]] | -0.52 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[CYB5R1]] | -0.52 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[NAA40]] | -0.52 | -0.19 / -0.51 | ⚠ one half (not replicated) | 8e-04 |  |
| [[EHMT2]] | -0.52 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[SKIC3]] | -0.51 | -0.37 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers POC1B-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 1.4% of all compounds | 0.004 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDK6-AS1]] | B | CDK6-AS1 activity raises POC1B-AS1's level | lines that do not express CDK6-AS1 (6) vs lines expressing it (44) | 1.53× lower at baseline in the lines without CDK6-AS1 | 0.057 | ⚠ within organs, on part of the lines; also absent: PLS3, CDK6, UACA; maybe low, not absent |
| [[TOP2B]] | B | TOP2B activity lowers POC1B-AS1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.710). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-3.9, 20.2); signed map (17.8, -5.1). **Vector** length 66.3, 12.1% of its response variance represented; |z| ≥ 3 in 1,255 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.4 | +16.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +6.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.4 | +1.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.3 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | -6.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.2 | -0.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.2 | +1.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.3 | -5.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.2 | -5.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | -5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.9 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | +1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -0.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.5 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | POC1B antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q21.33 — chr12:89,524,594-89,548,005 (+) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-734K2.4 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52949](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52949) · Entrez [109729146](https://www.ncbi.nlm.nih.gov/gene/109729146) · Ensembl [ENSG00000270344](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000270344)

## Data

Gene col 15662: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15662); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15662, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15662]; `tensor/DDL_lfc|DDL_z.npy` [15662]; `embed/gene_vectors.npy` [15662]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15662 or target_col == 15662). Every well: [[POC1B-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POC1B-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
