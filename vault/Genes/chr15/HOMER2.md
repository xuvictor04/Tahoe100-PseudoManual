---
symbol: "HOMER2"
type: "gene"
col: 2402
ensembl_id: "ENSG00000103942"
name: "homer scaffold protein 2"
location: "15q25.2"
module: 102
arm: "+"
pooled_cpm: 26.1
n_lines_expressing: 39
n_dd_up: 13
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# HOMER2

*homer scaffold protein 2* — 15q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.52× (z +7.1, q 8e-10, up in 23 of 37 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 1.41× (z +5.9, q 1e-06, up in 18 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.447× (z -13.3, q 1e-37, down in 27 of 37 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.701× (z -5.9, q 4e-07, down in 20 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC7B]] (+0.62, fdr 1e-05), [[MAP6]] (+0.60, fdr 1e-05), [[MAP1B]] (+0.57, fdr 1e-05); moves opposite to [[NR4A2]] (-0.53, fdr 3e-05), [[GPRC5C]] (-0.53, fdr 1e-05), [[ATOSA]] (-0.52, fdr 6e-05).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PTPRR]] → it (grade B ⚠); 3 go from it, the strongest it → [[NR4A3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2402.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.52×** | +7.1 | 8e-10 | 23/37 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +5.9 | 1e-06 | 18/37 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +5.5 | 8e-06 | 19/37 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.34×** | +5.0 | 7e-05 | 20/36 (A498, NCI-H460, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.9 | 1e-04 | 1/37 (MIA PaCa-2) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.32×** | +4.8 | 2e-04 | 16/36 (RPMI-7951, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.22×** | +4.7 | 2e-04 | 13/37 (NCI-H23, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.31×** | +4.7 | 2e-04 | 16/37 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +4.3 | 0.001 | 11/26 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.61×** | +4.3 | 0.001 | 15/37 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.007 | 11/37 (NCI-H1573, HEC-1-A, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.49×** | +3.6 | 0.017 | 10/36 (A498, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.20×** | +3.2 | 0.069 | 16/36 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.20×** | +3.1 | 0.073 | 8/30 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2402.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.447×** | -13.3 | 1e-37 | 27/37 (PANC-1, J82, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.539×** | -10.7 | 5e-24 | 23/36 (NCI-H2030, J82, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.609×** | -8.5 | 3e-15 | 20/37 (J82, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.631×** | -7.9 | 3e-13 | 22/37 (NCI-H460, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **0.731×** | -7.6 | 3e-12 | 23/37 (A549, A498, …) | top dose only | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.701×** | -5.9 | 4e-07 | 20/37 (SK-MEL-2, A-427, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.748×** | -5.0 | 4e-05 | 17/37 (HOP62, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.749×** | -5.0 | 4e-05 | 18/37 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -4.8 | 8e-05 | 18/36 (J82, A-427, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | **0.760×** | -4.5 | 3e-04 | 16/36 (A-172, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.633×** | -4.1 | 0.002 | 10/37 (A-427, SW 900, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.800×** | -3.9 | 0.006 | 16/37 (MIA PaCa-2, A549, …) | two highest doses | position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.662×** | -3.7 | 0.009 | 10/36 (A549, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.871× | -3.4 | 0.028 | 6/37 (NCI-H23, A-427, …) | top dose only | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **0.825×** | -3.2 | 0.053 | 11/37 (BT-474, SW 1271, …) | top dose only |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.879× | -3.1 | 0.059 | 6/37 (SW 1088, NCI-H1792, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.837× | -3.0 | 0.098 | 12/37 (SW 1088, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2402. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 56.5 | 0 | 6 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.181× (z -13.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A498 (line)]] | wt | 60.7 | 1 (1 ⚠) | 4 (4 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.83× (z +12.6) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -20.2) ⚠ cell-cycle shift, explains ~98% of this change |
| [[MIA PaCa-2 (line)]] | alt | 35.2 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -18.0) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 44.9 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -17.3) ⚠ cell-cycle shift, explains ~98% of this change |
| [[A-427 (line)]] | wt | 45.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -14.7) ⚠ cell-cycle shift, explains ~98% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -14.2) |
| [[J82 (line)]] | alt | 27.0 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.135× (z -14.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -9.0) |
| [[A549 (line)]] | wt | 40.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -21.0) ⚠ cell-cycle shift, explains ~98% of this change |
| [[BT-474 (line)]] | alt | 57.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 29.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.44× (z +8.9) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -10.6) ⚠ cell-cycle shift, explains ~98% of this change |
| [[NCI-H2030 (line)]] | alt | 41.9 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.246× (z -11.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H460 (line)]] | wt | 18.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.22× (z +9.9) ⚠ unreliable plate only | [[Harringtonine (drug)]] 5 µM 0.287× (z -10.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SK-MEL-2 (line)]] | alt | 27.0 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0872× (z -15.5) |
| [[SW 1271 (line)]] | alt | 52.4 | 0 | 2 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0670× (z -9.6) |
| [[AN3 CA (line)]] | alt | 50.0 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.117× (z -9.4) |
| [[C32 (line)]] | wt | 13.5 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.102× (z -9.0) |
| [[H4 (line)]] | wt | 41.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -15.7) ⚠ cell-cycle shift, explains ~98% of this change |
| [[AsPC-1 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.72 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 67.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.73 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.86 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.22 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.63 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.26 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.81 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 39.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2402), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC7B]] | +0.62 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[MAP6]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[MAP1B]] | +0.57 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[NDST1]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[SLC4A3]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[MCF2L2]] | +0.56 | +0.43 / +0.54 | both halves | 4e-05 |  |
| [[GRID1]] | +0.55 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[USP46]] | +0.54 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[PRELID3A]] | +0.53 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[SHTN1]] | +0.53 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[FAM124A]] | +0.53 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[DGCR5]] | +0.53 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR4A2]] | -0.53 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[GPRC5C]] | -0.53 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[ATOSA]] | -0.52 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[DHRS3]] | -0.50 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[TMEM205]] | -0.49 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[PTPRR]] | -0.48 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[ARID4A]] | -0.48 | -0.30 / -0.54 | both halves | 2e-04 |  |
| [[MAML2]] | -0.48 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[TPCN1]] | -0.47 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[GCC2]] | -0.46 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[ADAM28]] | -0.46 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[HES1]] | -0.46 | -0.38 / -0.49 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRR]] | B | PTPRR activity lowers HOMER2's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 1.82× higher at baseline in the lines without PTPRR | 0.027 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2 |
| [[MAP3K15]] | B | MAP3K15 activity raises HOMER2's level | lines that do not express MAP3K15 (19) vs lines expressing it (31) | 2.21× lower at baseline in the lines without MAP3K15 | 0.056 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, NEXMIF, BARX1 |
| [[EBF4]] | B | EBF4 activity raises HOMER2's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 3.00× lower at baseline in the lines without EBF4 | 0.060 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[RAB6B]] | B | RAB6B activity raises HOMER2's level | lines that do not express RAB6B (14) vs lines expressing it (36) | 3.14× lower at baseline in the lines without RAB6B | 0.069 | ⚠ within organs, on part of the lines; also absent: FAM124A, WNT9A, MRAS |
| [[ULK2]] | C | ULK2 activity raises HOMER2's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 2.97× lower at baseline in the lines without ULK2 | 0.015 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR4A3]] | B | HOMER2 activity lowers NR4A3's level | lines that do not express HOMER2 (11) vs lines expressing it (39) | 1.09× higher at baseline in the lines without HOMER2 | 0.049 | ⚠ within organs, on part of the lines; also absent: ZNF529-AS1, ZNF420, ENSG00000282381; maybe low, not absent |
| [[NR4A2]] | B | HOMER2 activity lowers NR4A2's level | lines that do not express HOMER2 (11) vs lines expressing it (39) | 1.52× higher at baseline in the lines without HOMER2 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF529-AS1, ZNF420, ENSG00000282381; maybe low, not absent |
| cells under [[Dinaciclib (drug)]] 0.05 µM | B | HOMER2 activity lowers the cells' numbers under Dinaciclib 0.05 µM (makes them more sensitive) | lines that do not express HOMER2 (11) vs lines expressing it (37) | the lines without HOMER2: 1.29× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: ZNF529-AS1, ZNF420, ENSG00000282381; maybe low, not absent |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.522). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (5.0, 40.6); signed map (-8.5, 24.6). **Vector** length 86.7, 18.9% of its response variance represented; |z| ≥ 3 in 987 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.7 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.7 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.7 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +2.8 |
|  | [[EX229 (drug)]] 5 µM |  | +3.4 | +4.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.1 | -13.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -1.7 | -5.9 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -1.5 | -10.7 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.4 | -3.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.2 | -0.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -1.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | homer scaffold protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.2 — chr15:82,836,946-82,986,153 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CPD, Cupidin, Vesl-2, HOMER-2B, HOMER-2, HOMER-2A, DFNA68 |
| Gene groups (HGNC) | Homer scaffold proteins |
| Hallmark sets | ANDROGEN_RESPONSE, ESTROGEN_RESPONSE_LATE |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NSB8](https://www.uniprot.org/uniprotkb/Q9NSB8) (Homer protein homolog 2):

> Postsynaptic density scaffolding protein. Binds and cross-links cytoplasmic regions of GRM1, GRM5, ITPR1, DNM3, RYR1, RYR2, SHANK1 and SHANK3. By physically linking GRM1 and GRM5 with ER-associated ITPR1 receptors, it aids the coupling of surface receptors to intracellular calcium release. May also couple GRM1 to PI3 kinase through its interaction with AGAP2. Isoforms can be differently regulated and may play an important role in maintaining the plasticity at glutamatergic synapses. Required …

**Summary**, from NCBI Gene [9455](https://www.ncbi.nlm.nih.gov/gene/9455):

> This gene encodes a member of the homer family of dendritic proteins. Members of this family regulate group 1 metabotrophic glutamate receptor function. The encoded protein is a postsynaptic density scaffolding protein. Alternative splicing results in multiple transcript variants. Two related pseudogenes have been identified on chromosome 14. [provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:17513](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17513) · Entrez [9455](https://www.ncbi.nlm.nih.gov/gene/9455) · UniProt [Q9NSB8](https://www.uniprot.org/uniprotkb/Q9NSB8) · Ensembl [ENSG00000103942](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103942)

## Data

Gene col 2402: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2402); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2402, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2402]; `tensor/DDL_lfc|DDL_z.npy` [2402]; `embed/gene_vectors.npy` [2402]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2402 or target_col == 2402). Every well: [[HOMER2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOMER2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
