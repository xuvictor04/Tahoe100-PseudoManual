---
symbol: "ARSG"
type: "gene"
col: 6503
ensembl_id: "ENSG00000141337"
name: "arylsulfatase G"
location: "17q24.2"
module: 92
arm: "+"
pooled_cpm: 25.08
n_lines_expressing: 44
n_dd_up: 18
n_dd_down: 34
n_dd_up_clean: 11
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# ARSG

*arylsulfatase G* — 17q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.42× (z +7.0, q 1e-09, up in 23 of 42 measured lines) ⚠ cell-cycle shift, explains ~63% of this change. The strongest without an alert is [[Osimertinib (mesylate) (drug)]] 5 µM: 1.48× (z +5.6, q 4e-06, up in 23 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (13 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.397× (z -13.2, q 9e-37, down in 35 of 42 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.486× (z -10.3, q 2e-22, down in 28 of 41 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC16A6]] (+0.76, fdr 7e-06, ⚠ same locus), [[CNIH3]] (+0.57, fdr 2e-05), [[LINC02454]] (+0.57, fdr 1e-05), [[LINC00467]] (+0.51, fdr 3e-05); moves opposite to [[KIAA1522]] (-0.51, fdr 3e-05), [[RASSF7]] (-0.41, fdr 6e-04), [[PDE5A]] (-0.41, fdr 1e-04).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SLC16A6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CNIH3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6503.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.42×** | +7.0 | 1e-09 | 23/42 (NCI-H1573, HT-29, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.61×** | +6.7 | 4e-09 | 28/42 (PANC-1, HT-29, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +5.9 | 8e-07 | 14/36 (SHP-77, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.48×** | +5.6 | 4e-06 | 23/41 (PANC-1, HepG2/C3A, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.43×** | +5.1 | 5e-05 | 20/41 (NCI-H1573, HT-29, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.8 | 1e-04 | 15/42 (SK-MEL-2, HT-29, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +4.6 | 3e-04 | 19/40 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.37×** | +4.5 | 6e-04 | 16/40 (HepG2/C3A, BT-474, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 5 µM |  | **1.63×** | +3.6 | 0.019 | 14/38 (HOP62, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.29×** | +3.6 | 0.020 | 9/41 (A498, SNU-423, …) | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.032 | 13/42 (SW48, SW480, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.27×** | +3.4 | 0.033 | 11/42 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[Naproxen (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.049 | 7/42 (NCI-H23, A549, …) | all doses, flat | position effect removed |
| [[Meloxicam (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.053 | 10/42 (C-33 A, HepG2/C3A, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.053 | 6/40 (C-33 A, HT-29, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.17× | +3.2 | 0.053 | 7/42 (SNU-423, SW480, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.069 | 12/41 (NCI-H1792, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6503.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.397×** | -13.2 | 9e-37 | 35/42 (SW480, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.413×** | -12.6 | 6e-34 | 30/40 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.486×** | -10.3 | 2e-22 | 28/41 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.524×** | -9.2 | 5e-18 | 27/42 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.541×** | -8.7 | 3e-16 | 27/41 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.567×** | -8.1 | 6e-14 | 26/40 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.571×** | -8.0 | 1e-13 | 26/41 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.582×** | -7.7 | 1e-12 | 28/42 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.584×** | -7.6 | 1e-12 | 27/40 (A-427, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.704×** | -7.1 | 8e-11 | 23/41 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.612×** | -6.7 | 9e-10 | 22/41 (NCI-H1792, SNU-1, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.637×** | -6.4 | 6e-09 | 23/42 (SW480, SW 900, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.464×** | -5.7 | 5e-07 | 20/38 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.672×** | -5.7 | 6e-07 | 22/40 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.661×** | -5.6 | 1e-06 | 22/41 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.730×** | -4.5 | 2e-04 | 19/42 (SW480, HOP62, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.802×** | -4.5 | 2e-04 | 18/42 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.805×** | -4.0 | 0.002 | 17/42 (SW480, SK-MEL-2, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.793×** | -3.2 | 0.030 | 16/40 (A549, SW480, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.794×** | -3.2 | 0.032 | 10/42 (Panc 03.27, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6503. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 54.1 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -19.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.206× (z -12.6) |
| [[SW480 (line)]] | alt | 90.2 | 0 | 12 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.118× (z -17.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.143× (z -16.1) |
| [[RPMI-7951 (line)]] | alt | 58.3 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -15.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.214× (z -10.1) |
| [[A-427 (line)]] | wt | 44.5 | 0 | 8 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -17.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.201× (z -13.6) |
| [[PANC-1 (line)]] | alt | 16.1 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -19.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.292× (z -10.3) |
| [[SW 900 (line)]] | alt | 49.2 | 0 | 7 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.123× (z -12.0) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.202× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 57.8 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0716× (z -15.9) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.156× (z -11.6) |
| [[SNU-423 (line)]] | alt | 38.6 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -14.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.207× (z -9.6) |
| [[HOP62 (line)]] | alt | 42.0 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -13.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.219× (z -10.3) |
| [[C-33 A (line)]] | alt | 29.4 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.184× (z -9.5) |
| [[J82 (line)]] | alt | 20.4 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.132× (z -12.6) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[A549 (line)]] | wt | 17.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -12.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 30.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0913× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 25.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0976× (z -16.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 19.1 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 32.2 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0431× (z -15.2) ⚠ cell-cycle shift, explains ~57% of this change |
| [[AN3 CA (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0427× (z -9.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[C32 (line)]] | wt | 48.9 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.181× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -13.1) ⚠ cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 28.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0744× (z -9.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 9.04 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.0692× (z -9.3) |
| [[LoVo (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.116× (z -14.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -8.7) ⚠ cell-cycle shift, explains ~50% of this change |
| [[NCI-H1573 (line)]] | alt | 8.15 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 4.14× (z +9.5) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[A-172 (line)]] | wt | 9.50 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.74 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.35 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.86 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.51 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.82 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.25 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6503), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC16A6]] | +0.76 | +0.67 / +0.79 | both halves | 7e-06 | STRING 574; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[CNIH3]] | +0.57 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[LINC02454]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[LINC00467]] | +0.51 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[SHC3]] | +0.51 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[RPSAP52]] | +0.49 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[STEAP1B-AS1]] | +0.49 | +0.34 / +0.47 | both halves | 1e-04 |  |
| [[METAP1D]] | +0.49 | +0.52 / +0.38 | both halves | 7e-05 |  |
| [[TPK1]] | +0.49 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[LINC02813]] | +0.49 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[NPAS2]] | +0.48 | +0.40 / +0.50 | both halves | 4e-05 |  |
| [[ETV1]] | +0.47 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[SGIP1]] | +0.47 | +0.35 / +0.54 | both halves | 1e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA1522]] | -0.51 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[RASSF7]] | -0.41 | -0.45 / -0.22 | both halves | 6e-04 |  |
| [[PDE5A]] | -0.41 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[CREB3L1]] | -0.40 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[SORT1]] | -0.40 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[CDS1]] | -0.40 | -0.32 / -0.30 | both halves | 2e-04 |  |
| [[DOK4]] | -0.39 | -0.43 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[DNM2]] | -0.39 | -0.33 / -0.33 | both halves | 1e-04 |  |
| [[KRAS]] | -0.38 | -0.29 / -0.35 | both halves | 3e-04 |  |
| [[PDLIM1]] | -0.38 | -0.32 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A6]] | B | SLC16A6 activity raises ARSG's level | lines that do not express SLC16A6 (27) vs lines expressing it (23) | 2.57× lower at baseline in the lines without SLC16A6 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENPP2, TMEM47, IGFBP7 |
| [[RASGRF2]] | B | RASGRF2 activity raises ARSG's level | lines that do not express RASGRF2 (21) vs lines expressing it (29) | 2.03× lower at baseline in the lines without RASGRF2 | 0.006 | ⚠ within organs, on part of the lines; also absent: SFRP1, MT1A, RGCC |
| [[LINC02813]] | B | LINC02813 activity raises ARSG's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 1.68× lower at baseline in the lines without LINC02813 | 0.014 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN |
| [[ETV1]] | B | ETV1 activity raises ARSG's level | lines that do not express ETV1 (11) vs lines expressing it (39) | 1.52× lower at baseline in the lines without ETV1 | 0.051 | ⚠ within organs, on part of the lines; also absent: LINC02454, KATNAL1, CCDC136 |
| [[TMEM163]] | B | TMEM163 activity raises ARSG's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 1.86× lower at baseline in the lines without TMEM163 | 0.053 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNIH3]] | B | ARSG activity raises CNIH3's level | lines that do not express ARSG (6) vs lines expressing it (44) | 1.77× lower at baseline in the lines without ARSG | 0.084 | ⚠ within organs, on part of the lines; also absent: PHGDH, RNF157, C2orf92; maybe low, not absent |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.561). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.4, 9.0); signed map (11.9, 49.6). **Vector** length 94.7, 22.9% of its response variance represented; |z| ≥ 3 in 1,265 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +4.0 | +7.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +3.4 | +5.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.5 | +2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.8 | +4.5 |
|  | [[Benztropine (mesylate) (drug)]] 0.05 µM |  | +1.8 | +3.6 |
|  | [[Abiraterone acetate (drug)]] 0.05 µM |  | +1.7 | +3.4 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -4.3 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.3 | -4.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.1 | -2.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.1 | -3.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | arylsulfatase G |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q24.2 — chr17:68,259,182-68,422,731 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1001 |
| Gene groups (HGNC) | Sulfatases |
| Reactome | 6 pathways, smallest: The activation of arylsulfatases; Glycosphingolipid catabolism; Glycosphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EG1](https://www.uniprot.org/uniprotkb/Q96EG1) (Arylsulfatase G):

> Displays arylsulfatase activity at acidic pH towards artificial substrates, such as p-nitrocatechol sulfate and also, but with a lower activity towards p-nitrophenyl sulfate and 4-methylumbelliferyl sulfate. Catalyzes the hydrolysis of the 3-sulfate groups of the N-sulfo-D-glucosamine 3-O-sulfate units of heparin.

**Summary**, from NCBI Gene [22901](https://www.ncbi.nlm.nih.gov/gene/22901):

> The protein encoded by this gene belongs to the sulfatase enzyme family. Sulfatases hydrolyze sulfate esters from sulfated steroids, carbohydrates, proteoglycans, and glycolipids. They are involved in hormone biosynthesis, modulation of cell signaling, and degradation of macromolecules. This protein displays arylsulfatase activity at acidic pH, as is typical of lysosomal sulfatases, and has been shown to localize in the lysosomes. Alternatively spliced transcript variants have been found for …

**Accessions** — [HGNC:24102](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24102) · Entrez [22901](https://www.ncbi.nlm.nih.gov/gene/22901) · UniProt [Q96EG1](https://www.uniprot.org/uniprotkb/Q96EG1) · Ensembl [ENSG00000141337](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141337)

## Data

Gene col 6503: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6503); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6503, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6503]; `tensor/DDL_lfc|DDL_z.npy` [6503]; `embed/gene_vectors.npy` [6503]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6503 or target_col == 6503). Every well: [[ARSG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARSG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
