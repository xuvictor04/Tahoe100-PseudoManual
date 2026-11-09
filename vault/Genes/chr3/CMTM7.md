---
symbol: "CMTM7"
type: "gene"
col: 7727
ensembl_id: "ENSG00000153551"
name: "CKLF like MARVEL transmembrane domain containing 7"
location: "3p22.3"
module: 18
arm: "+"
pooled_cpm: 44.47
n_lines_expressing: 45
n_dd_up: 2
n_dd_down: 20
n_dd_up_clean: 1
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# CMTM7

*CKLF like MARVEL transmembrane domain containing 7* — 3p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.05 µM: 1.25× (z +5.4, q 4e-05, up in 17 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 1.89×; ⚠ cell-cycle shift, explains ~6% of this change).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.358× (z -35.0, q 0e+00, down in 42 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3TC2-DT]] (+0.58, fdr 1e-05), [[CTDSPL]] (+0.56, fdr 1e-05), [[EBPL]] (+0.56, fdr 1e-05); moves opposite to [[CYLD]] (-0.50, fdr 3e-05), [[KYNU]] (-0.48, fdr 6e-05), [[C1RL]] (-0.47, fdr 2e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CTDSPL]] → it (grade B ⚠); 2 go from it, the strongest it → [[CTDSPL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7727.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 1.89×; ⚠ cell-cycle shift, explains ~6% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM |  | **1.25×** | +5.4 | 4e-05 | 17/43 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.16× | +5.2 | 7e-05 | 16/43 (AsPC-1, Hs 766T, …) | all doses, flat | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.22×** | +4.6 | 7e-04 | 14/36 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.16× | +3.6 | 0.038 | 15/43 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | 1.29× | +3.2 | 0.12 | 7/42 (NCI-H460, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Ritonavir (drug)]] 5 µM |  | 1.10× | +3.2 | 0.12 | 5/43 (A498, Hs 766T, …) | top dose only |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.13 | 4/42 (SNU-423, CFPAC-1, …) | two highest doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.13 | 10/43 (CFPAC-1, Hs 766T, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 1.28× | +3.1 | 0.13 | 8/38 (A498, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.13× | +3.0 | 0.15 | 9/42 (A-172, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7727.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.358×** | -35.0 | 0e+00 | 42/43 (SK-MEL-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.426×** | -20.5 | 0e+00 | 35/43 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.434×** | -19.3 | 0e+00 | 38/43 (SK-MEL-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.479×** | -17.7 | 0e+00 | 30/43 (Panc 03.27, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.520×** | -15.7 | 0e+00 | 31/43 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.360×** | -12.8 | 9e-36 | 34/43 (HEC-1-A, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.595×** | -12.5 | 1e-33 | 30/42 (SW1417, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.611×** | -11.8 | 2e-30 | 29/43 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.704×** | -8.4 | 2e-15 | 27/43 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.717×** | -8.0 | 8e-14 | 24/42 (RKO, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.737×** | -7.3 | 1e-11 | 23/43 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.744×** | -6.8 | 4e-10 | 20/42 (Panc 03.27, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.763×** | -6.3 | 1e-08 | 19/43 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.786×** | -5.8 | 3e-07 | 20/43 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.779×** | -5.8 | 3e-07 | 20/42 (J82, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.833× | -5.3 | 5e-06 | 19/43 (J82, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7727. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 156 | 0 | 19 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -21.6) |
| [[Panc 03.27 (line)]] | alt | 249 | 0 | 18 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -22.4) |
| [[SW1417 (line)]] | alt | 157 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -17.6) |
| [[MIA PaCa-2 (line)]] | alt | 80.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -19.9) |
| [[RKO (line)]] | wt | 51.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -13.9) |
| [[SK-MEL-2 (line)]] | alt | 81.6 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.0906× (z -31.7) |
| [[SW480 (line)]] | alt | 44.6 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -16.2) |
| [[A-172 (line)]] | wt | 38.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -20.6) |
| [[C32 (line)]] | wt | 73.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -14.5) |
| [[NCI-H460 (line)]] | wt | 22.3 | 1 (1 ⚠) | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +8.6) ⚠ cell-cycle shift, explains ~6% of this change | [[Harringtonine (drug)]] 0.5 µM 0.279× (z -12.1) |
| [[HOP62 (line)]] | alt | 33.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -13.1) |
| [[KATO III (line)]] | alt | 34.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -14.6) |
| [[LoVo (line)]] | wt | 45.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -11.1) |
| [[PANC-1 (line)]] | alt | 46.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -21.6) |
| [[J82 (line)]] | alt | 35.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -23.2) |
| [[AsPC-1 (line)]] | alt | 16.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.110× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.323× (z -9.7) |
| [[C-33 A (line)]] | alt | 59.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.308× (z -10.1) |
| [[Hs 766T (line)]] | wt | 50.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -18.2) |
| [[NCI-H2030 (line)]] | alt | 15.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -12.9) |
| [[NCI-H2347 (line)]] | alt | 39.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -12.6) |
| [[SNU-423 (line)]] | alt | 62.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -16.8) |
| [[SW48 (line)]] | wt | 47.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -11.7) |
| [[A-427 (line)]] | wt | 22.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -12.3) |
| [[A498 (line)]] | wt | 14.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -13.8) |
| [[A549 (line)]] | wt | 23.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -14.0) |
| [[AN3 CA (line)]] | alt | 69.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 38.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -13.0) |
| [[CHP-212 (line)]] | wt | 39.0 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0997× (z -9.5) |
| [[HS-578T (line)]] | alt | 25.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -11.9) |
| [[LS 180 (line)]] | wt | 37.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -16.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 45.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.331× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -14.0) |
| [[SNU-1 (line)]] | wt | 49.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -15.5) |
| [[SW 900 (line)]] | alt | 23.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -8.7) |
| [[BT-474 (line)]] | alt | 8.49 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.80 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.52 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.60 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7727), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3TC2-DT]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[CTDSPL]] | +0.56 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[EBPL]] | +0.56 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[XYLB]] | +0.55 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[CMTM4]] | +0.55 | +0.56 / +0.51 | both halves | 1e-05 | same gene group; STRING 426 |
| [[CCDC88C]] | +0.55 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[ADCY3]] | +0.54 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[GARNL3]] | +0.54 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[SORD]] | +0.53 | +0.52 / +0.49 | both halves | 2e-05 |  |
| [[CENPV]] | +0.52 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[PPM1F]] | +0.52 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ANKS6]] | +0.52 | +0.62 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYLD]] | -0.50 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[KYNU]] | -0.48 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[C1RL]] | -0.47 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[PNRC1]] | -0.47 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[FOSL2]] | -0.47 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[SMIM14]] | -0.46 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[WASHC3]] | -0.46 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[NR3C1]] | -0.45 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[CUTALP]] | -0.45 | -0.56 / -0.37 | both halves | 7e-05 |  |
| [[RHCG]] | -0.45 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[CGGBP1]] | -0.45 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[METTL25B]] | -0.44 | -0.52 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTDSPL]] | B | CTDSPL activity raises CMTM7's level | lines that do not express CTDSPL (5) vs lines expressing it (45) | 3.48× lower at baseline in the lines without CTDSPL | 0.047 | ⚠ within organs, on part of the lines; also absent: ITGA9-AS1, SLC43A2, PLAAT3; maybe low, not absent |
| [[WNT7A]] | B | WNT7A activity raises CMTM7's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 1.94× lower at baseline in the lines without WNT7A | 0.076 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTDSPL]] | B | CMTM7 activity raises CTDSPL's level | lines that do not express CMTM7 (5) vs lines expressing it (45) | 2.74× lower at baseline in the lines without CMTM7 | 0.022 | ⚠ within organs, on part of the lines; also absent: EPB41L2, FAM3C2P, P3H1 |
| [[PRR7-AS1]] | B | CMTM7 activity raises PRR7-AS1's level | lines that do not express CMTM7 (5) vs lines expressing it (45) | 1.95× lower at baseline in the lines without CMTM7 | 0.082 | ⚠ within organs, on part of the lines; also absent: EPB41L2, FAM3C2P, P3H1 |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.550). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-8.6, -38.8); signed map (-6.2, -55.5). **Vector** length 101, 25.1% of its response variance represented; |z| ≥ 3 in 1,197 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | -0.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +3.5 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.9 | +3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +1.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +2.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +1.9 | +0.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -19.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.0 | -5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.7 | -5.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.6 | -3.7 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.5 | -6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.2 | -3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.8 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | CKLF like MARVEL transmembrane domain containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.3 — chr3:32,391,698-32,483,067 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30992; previously CKLFSF7 |
| Gene groups (HGNC) | CKLF like MARVEL transmembrane domain containing |
| Matched by | ensembl_id |

UniProt [Q96FZ5](https://www.uniprot.org/uniprotkb/Q96FZ5) carries no function annotation.

**Summary**, from NCBI Gene [112616](https://www.ncbi.nlm.nih.gov/gene/112616):

> This gene belongs to the chemokine-like factor gene superfamily, a novel family that is similar to the chemokine and transmembrane 4 superfamilies. This gene is one of several chemokine-like factor genes located in a cluster on chromosome 3. This gene acts as a tumor suppressor that regulates G1/S transition in the cell cycle, and epidermal growth factor receptor/protein kinase B signaling during tumor pathogenesis. Alternative splicing results in multiple transcript variants encoding different …

**Accessions** — [HGNC:19178](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19178) · Entrez [112616](https://www.ncbi.nlm.nih.gov/gene/112616) · UniProt [Q96FZ5](https://www.uniprot.org/uniprotkb/Q96FZ5) · Ensembl [ENSG00000153551](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153551)

## Data

Gene col 7727: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7727); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7727, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7727]; `tensor/DDL_lfc|DDL_z.npy` [7727]; `embed/gene_vectors.npy` [7727]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7727 or target_col == 7727). Every well: [[CMTM7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CMTM7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
