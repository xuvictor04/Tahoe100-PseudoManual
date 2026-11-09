---
symbol: "VLDLR-AS1"
type: "gene"
col: 14077
ensembl_id: "ENSG00000236404"
name: "VLDLR antisense RNA 1"
location: "9p24.2"
module: 133
arm: "+"
pooled_cpm: 9.64
n_lines_expressing: 43
n_dd_up: 29
n_dd_down: 19
n_dd_up_clean: 27
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# VLDLR-AS1

*VLDLR antisense RNA 1* — 9p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.24× (z +16.3, q 0e+00, up in 35 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.276× (z -12.6, q 2e-33, down in 30 of 40 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.387× (z -9.3, q 2e-18, down in 25 of 36 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCK2]] (+0.77, fdr 7e-06), [[DMGDH]] (+0.72, fdr 7e-06), [[COP1-DT]] (+0.71, fdr 7e-06); moves opposite to [[NAA40]] (-0.52, fdr 1e-04).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14077.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.24×** | +16.3 | 0e+00 | 35/35 (HOP62, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.98×** | +10.7 | 3e-24 | 28/36 (NCI-H460, SK-MEL-2, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **2.56×** | +9.2 | 7e-18 | 27/39 (SW480, SHP-77, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **2.28×** | +8.1 | 9e-14 | 30/35 (SW480, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **2.17×** | +7.6 | 4e-12 | 26/39 (SHP-77, HepG2/C3A, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **2.15×** | +7.5 | 6e-12 | 24/37 (SHP-77, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.62×** | +6.7 | 1e-09 | 27/41 (SW480, HEC-1-A, …) | two highest doses |  |
| [[Artesunate (drug)]] 5 µM |  | **1.55×** | +6.1 | 9e-08 | 22/40 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.76×** | +5.5 | 2e-06 | 18/39 (A498, COLO 205, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +5.4 | 3e-06 | 17/32 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.8 | 7e-05 | 12/40 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.62×** | +4.8 | 9e-05 | 20/41 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Neratinib (drug)]] 0.5 µM |  | **1.58×** | +4.5 | 3e-04 | 16/38 (SHP-77, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.38×** | +4.5 | 3e-04 | 17/40 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.56×** | +4.4 | 4e-04 | 15/37 (SHP-77, HEC-1-A, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.58×** | +4.3 | 7e-04 | 13/37 (SHP-77, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14077.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.276×** | -12.6 | 2e-33 | 30/40 (SW480, H4, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.358×** | -9.7 | 1e-19 | 34/38 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.379×** | -9.5 | 5e-19 | 27/34 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.387×** | -9.3 | 2e-18 | 25/36 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.424×** | -8.4 | 5e-15 | 32/36 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.472×** | -7.3 | 2e-11 | 25/38 (SNU-1, HCT15, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.511×** | -6.6 | 4e-09 | 25/38 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.548×** | -5.9 | 3e-07 | 21/38 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.573×** | -5.4 | 3e-06 | 20/38 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.604×** | -4.9 | 5e-05 | 19/38 (COLO 205, LOX-IMVI, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.641×** | -4.3 | 7e-04 | 20/34 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.567×** | -4.3 | 9e-04 | 17/37 (H4, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.573×** | -4.2 | 0.001 | 10/39 (H4, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.689×** | -3.6 | 0.011 | 16/39 (SW480, LOX-IMVI, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.694×** | -3.4 | 0.028 | 17/36 (HS-578T, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.722×** | -3.2 | 0.048 | 10/35 (A-172, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14077. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 24.8 | 2 | 9 (5 ⚠) | [[Artesunate (drug)]] 5 µM 2.80× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.0424× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0957× (z -15.1) |
| [[H4 (line)]] | wt | 38.2 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0527× (z -12.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0992× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 28.0 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +8.6) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.115× (z -9.4) |
| [[HS-578T (line)]] | alt | 25.4 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0608× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A549 (line)]] | wt | 6.19 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.72× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.0886× (z -12.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Mozavaptan (drug)]] 0.05 µM 0.0786× (z -8.9) |
| [[HOP62 (line)]] | alt | 8.56 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.86× (z +14.5) | [[Digitoxin (drug)]] 5 µM 0.0528× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H460 (line)]] | wt | 6.46 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.06× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.115× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.193× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 12.3 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.60× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0671× (z -9.8) |
| [[HT-29 (line)]] | alt | 6.52 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +10.2) | [[Silodosin (drug)]] 5 µM 0.0795× (z -10.0) |
| [[PANC-1 (line)]] | alt | 4.78 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0178× (z -19.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +15.7) ⚠ cell-cycle shift, would explain all of this change | [[Ixazomib citrate (drug)]] 0.5 µM 0.140× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 13.1 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0903× (z -11.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[LS 180 (line)]] | wt | 7.58 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0756× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SNU-1 (line)]] | wt | 21.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0717× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 28.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.19× (z +11.4) | — |
| [[CFPAC-1 (line)]] | alt | 4.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.4× (z +13.1) | — |
| [[COLO 205 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0418× (z -10.9) ⚠ cell-cycle shift, explains ~40% of this change |
| [[HEC-1-A (line)]] | alt | 6.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.41× (z +12.0) | — |
| [[J82 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0594× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H1573 (line)]] | alt | 4.29 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0751× (z -8.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SNU-423 (line)]] | alt | 6.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.87× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.124× (z -9.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14077), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCK2]] | +0.77 | +0.61 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[DMGDH]] | +0.72 | +0.61 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[COP1-DT]] | +0.71 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[TARS1]] | +0.68 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[SLC6A9]] | +0.67 | +0.47 / +0.74 | both halves | 2e-05 |  |
| [[NBR2]] | +0.66 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[CEBPG]] | +0.65 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[YARS1]] | +0.64 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[SMG1P7]] | +0.63 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[NRSN2-AS1]] | +0.63 | +0.43 / +0.61 | both halves | 3e-05 | same gene group |
| [[PLAC8L1]] | +0.63 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[SLC1A4]] | +0.61 | +0.53 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA40]] | -0.52 | -0.36 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers VLDLR-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CCDC171]] | C | CCDC171 activity raises VLDLR-AS1's level | lines that do not express CCDC171 (3) vs lines expressing it (47) | 2.61× lower at baseline in the lines without CCDC171 | 0.099 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.787). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.0, 47.0); signed map (-13.2, 22.6). **Vector** length 93.0, 20.9% of its response variance represented; |z| ≥ 3 in 1,139 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +16.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.4 | +10.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +5.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +4.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.4 | +7.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.3 | +9.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.1 | +6.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.0 | -7.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.5 | -4.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.1 | -8.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.8 | -4.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.8 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -1.4 |
|  | [[Methotrexate (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -5.9 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | VLDLR antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 9p24.2 — chr9:2,421,597-2,622,457 (-) |
| Ensembl biotype | lncRNA |
| Also known as | lincRNA-VLDLR |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49621](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49621) · Entrez [401491](https://www.ncbi.nlm.nih.gov/gene/401491) · Ensembl [ENSG00000236404](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236404)

## Data

Gene col 14077: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14077); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14077, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14077]; `tensor/DDL_lfc|DDL_z.npy` [14077]; `embed/gene_vectors.npy` [14077]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14077 or target_col == 14077). Every well: [[VLDLR-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VLDLR-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
