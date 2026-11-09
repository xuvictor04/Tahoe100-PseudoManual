---
symbol: "XNDC1N-ZNF705EP-ALG1L9P"
type: "gene"
col: 16436
ensembl_id: "ENSG00000289716"
name: "XNDC1N-ZNF705EP-ALG1L9P readthrough"
location: "11q13.4"
module: 26
arm: "+"
pooled_cpm: 3.39
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 21
n_dd_up_clean: 16
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# XNDC1N-ZNF705EP-ALG1L9P

*XNDC1N-ZNF705EP-ALG1L9P readthrough* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.73× (z +15.3, q 0e+00, up in 35 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.290× (z -10.2, q 1e-21, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XNDC1N]] (+0.83, fdr 7e-06, ⚠ same locus), [[ALG1L9P]] (+0.77, fdr 7e-06, ⚠ same locus), [[MYLK4]] (+0.74, fdr 1e-05), [[MAMDC2-AS1]] (+0.73, fdr 1e-05), [[ZNF876P]] (+0.72, fdr 7e-06); moves opposite to [[CCDC112]] (-0.66, fdr 3e-05), [[COMMD2]] (-0.63, fdr 5e-05), [[PIGH]] (-0.62, fdr 9e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16436.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.73×** | +15.3 | 0e+00 | 35/35 (Panc 03.27, LoVo, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.16×** | +11.3 | 6e-27 | 24/26 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.09×** | +8.9 | 1e-16 | 28/36 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.81×** | +6.9 | 8e-10 | 21/46 (SW1417, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +5.6 | 3e-06 | 1/6 (HEC-1-A) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.67×** | +4.2 | 0.002 | 12/45 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +4.2 | 0.002 | 12/41 (SHP-77, NCI-H23, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.54×** | +3.5 | 0.031 | 9/40 (HT-29, NCI-H1573, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.52×** | +3.4 | 0.038 | 9/43 (NCI-H23, HepG2/C3A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.41×** | +3.3 | 0.047 | 7/46 (NCI-H1573, NCI-H23, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.047 | 9/34 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.49×** | +3.2 | 0.055 | 5/47 (PANC-1, RPMI-7951, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.092 | 9/45 (RKO, HOP62, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.61×** | +3.0 | 0.097 | 7/44 (LoVo, PANC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.098 | 4/43 (SW480, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.00×** | +3.0 | 0.098 | 2/40 (PANC-1, SW480) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16436.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.290×** | -10.2 | 1e-21 | 39/46 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.292×** | -10.1 | 1e-21 | 30/44 (PANC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.381×** | -7.6 | 5e-12 | 26/41 (HOP62, HEC-1-A, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.482×** | -6.0 | 3e-07 | 23/44 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.501×** | -5.7 | 2e-06 | 25/45 (CFPAC-1, H4, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.509×** | -5.5 | 3e-06 | 18/29 (SW480, COLO 205, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.633×** | -5.3 | 8e-06 | 18/36 (COLO 205, A498, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.526×** | -5.3 | 9e-06 | 19/33 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.544×** | -5.0 | 4e-05 | 22/42 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.359×** | -4.4 | 6e-04 | 18/38 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.601×** | -4.2 | 0.001 | 14/43 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.625×** | -3.9 | 0.005 | 15/44 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.723×** | -3.8 | 0.007 | 18/44 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.649×** | -3.6 | 0.015 | 15/46 (NCI-H2030, HEC-1-A, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.682×** | -3.1 | 0.061 | 14/42 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.482×** | -3.1 | 0.061 | 8/20 (SW480, J82, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.484×** | -3.1 | 0.061 | 5/36 (A549, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.683×** | -3.0 | 0.080 | 7/44 (CFPAC-1, SNU-423, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.497×** | -3.0 | 0.080 | 6/31 (HEC-1-A, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.690×** | -2.9 | 0.094 | 8/42 (Panc 03.27, SNU-423, …) | rises with dose |  |
| [[Ranolazine (drug)]] 0.5 µM |  | **0.701×** | -2.9 | 0.095 | 8/44 (SNU-423, SNU-1, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.68 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16436. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.81 | 2 | 3 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.68× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.0427× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.120× (z -9.9) |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0698× (z -15.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0738× (z -10.7) |
| [[PANC-1 (line)]] | alt | 2.58 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0693× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~37% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0957× (z -8.7) |
| [[A498 (line)]] | wt | 3.39 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 5.97 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0896× (z -8.5) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 4.21 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0553× (z -9.8) |
| [[LS 180 (line)]] | wt | 3.08 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0396× (z -9.4) |
| [[SHP-77 (line)]] | alt | 8.24 | 0 | 1 | — | [[EX229 (drug)]] 0.05 µM 0.0746× (z -9.2) |
| [[A-172 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.986 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.982 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16436), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 6 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XNDC1N]] | +0.83 | +0.79 / +0.75 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ALG1L9P]] | +0.77 | +0.75 / +0.64 | both halves | 7e-06 | ⚠ same locus (0.4 kb, same strand: neighbours can correlate without regulation) |
| [[MYLK4]] | +0.74 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[MAMDC2-AS1]] | +0.73 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[ZNF876P]] | +0.72 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[SIAH2-AS1]] | +0.67 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[GOLGA2P5-1]] | +0.67 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[SNHG31]] | +0.66 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[PSMD7-DT]] | +0.65 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[LAMTOR5-AS1]] | +0.65 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[CDNF]] | +0.65 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[PIPOX]] | +0.65 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[FAM174B]] | +0.63 | +0.48 / +0.37 | both halves | 8e-05 |  |
| [[PKN2-AS1]] | +0.63 | +0.58 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC112]] | -0.66 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[COMMD2]] | -0.63 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[PIGH]] | -0.62 | -0.47 / -0.37 | both halves | 9e-05 |  |
| [[POLM]] | -0.60 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[KDM1B]] | -0.60 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[METTL5]] | -0.59 | -0.27 / -0.55 | both halves | 3e-04 |  |
| [[EML2]] | -0.56 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[SNAP29]] | -0.55 | -0.31 / -0.28 | both halves | 3e-04 |  |
| [[TTC38]] | -0.55 | -0.42 / -0.25 | both halves | 4e-04 |  |
| [[SYP]] | -0.55 | -0.24 / -0.42 | both halves | 5e-04 |  |
| [[RSAD1]] | -0.54 | -0.32 / -0.36 | both halves | 1e-04 |  |
| [[PKN1]] | -0.54 | -0.47 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers XNDC1N-ZNF705EP-ALG1L9P's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP7D3]] | B | MAP7D3 activity lowers XNDC1N-ZNF705EP-ALG1L9P's level | lines that do not express MAP7D3 (6) vs lines expressing it (44) | 1.51× higher at baseline in the lines without MAP7D3 | 0.022 | ⚠ within organs, on part of the lines; also absent: ROBO3, KIRREL1, ANKRD44 |
| [[LRRC17]] | B | LRRC17 activity raises XNDC1N-ZNF705EP-ALG1L9P's level | lines that do not express LRRC17 (27) vs lines expressing it (23) | 1.36× lower at baseline in the lines without LRRC17 | 0.077 | ⚠ within organs, on part of the lines; also absent: AEBP1, ARHGAP6, LINC02240; maybe low, not absent |
| [[XNDC1N]] | C | XNDC1N's natural level strengthens XNDC1N-ZNF705EP-ALG1L9P's drug response | XNDC1N's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.47; direction not clear | 0.007 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.641). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (10.4, 18.9); signed map (37.1, -15.8). **Vector** length 57.6, 8.50% of its response variance represented; |z| ≥ 3 in 1,079 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +15.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +11.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +4.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +3.2 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +1.2 | +3.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.1 | +3.4 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | -0.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -1.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | +0.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -3.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | XNDC1N-ZNF705EP-ALG1L9P readthrough |
| Locus type | readthrough (other) |
| Location | 11q13.4 — chr11:71,804,997-71,928,656 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [122319435](https://www.ncbi.nlm.nih.gov/gene/122319435):

> This locus represents naturally occurring readthrough transcription between the neighboring XNDC1N (XRCC1 N-terminal domain containing 1-like), ZNF705P (zinc finger protein 705, pseudogene) and ALG1L9P (ALG1 like 9, pseudogene) genes on chromosome 11q13.4. These readthrough transcripts are candidates for nonsense-mediated mRNA decay (NMD), and are unlikely to produce a protein product. [provided by RefSeq, Aug 2021]

**Accessions** — [HGNC:55871](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55871) · Entrez [122319435](https://www.ncbi.nlm.nih.gov/gene/122319435) · Ensembl [ENSG00000289716](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000289716)

## Data

Gene col 16436: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16436); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16436, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16436]; `tensor/DDL_lfc|DDL_z.npy` [16436]; `embed/gene_vectors.npy` [16436]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16436 or target_col == 16436). Every well: [[XNDC1N-ZNF705EP-ALG1L9P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XNDC1N-ZNF705EP-ALG1L9P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
