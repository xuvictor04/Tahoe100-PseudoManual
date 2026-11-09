---
symbol: "GDPGP1"
type: "gene"
col: 11381
ensembl_id: "ENSG00000183208"
name: "GDP-D-glucose phosphorylase 1"
location: "15q26.1"
module: 34
arm: "+"
pooled_cpm: 6.45
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 22
n_dd_up_clean: 10
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 9
direction_downstream: 1
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# GDPGP1

*GDP-D-glucose phosphorylase 1* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.59× (z +11.3, q 5e-27, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.300× (z -14.4, q 6e-44, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEMA4B]] (+0.77, fdr 7e-06, ⚠ read-through risk), [[TTLL13]] (+0.75, fdr 7e-06, ⚠ same locus), [[CIB1]] (+0.66, fdr 1e-05, ⚠ same locus), [[DUSP5]] (+0.65, fdr 1e-05), [[LYPD3]] (+0.64, fdr 1e-05), [[GPRC5A]] (+0.64, fdr 1e-05); moves opposite to [[ARFGAP2]] (-0.61, fdr 3e-05), [[EFCAB2]] (-0.60, fdr 6e-05), [[ZMYND11]] (-0.59, fdr 2e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TNFRSF11A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[TTLL13]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11381.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.59×** | +11.3 | 5e-27 | 38/45 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.55×** | +11.1 | 2e-26 | 34/46 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.38×** | +10.3 | 1e-22 | 35/45 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.77×** | +9.6 | 1e-19 | 29/45 (MIA PaCa-2, A498, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **2.16×** | +9.2 | 6e-18 | 25/37 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.41×** | +7.9 | 2e-13 | 29/45 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +5.8 | 7e-07 | 22/42 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +4.0 | 0.005 | 2/12 (NCI-H2030, LoVo) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.34×** | +3.5 | 0.034 | 4/37 (HEC-1-A, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.068 | 6/42 (NCI-H2347, RPMI-7951, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.67×** | +3.2 | 0.068 | 6/43 (NCI-H1573, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.098 | 3/44 (J82, NCI-H460, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11381.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.300×** | -14.4 | 6e-44 | 38/47 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.433×** | -14.1 | 8e-43 | 32/38 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.422×** | -10.3 | 1e-22 | 28/43 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.447×** | -9.6 | 1e-19 | 31/44 (LoVo, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.433×** | -9.0 | 2e-17 | 25/42 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.476×** | -8.8 | 9e-17 | 25/44 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.511×** | -8.0 | 1e-13 | 24/37 (NCI-H2030, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.536×** | -7.4 | 7e-12 | 25/38 (PANC-1, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.512×** | -7.2 | 3e-11 | 23/30 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.574×** | -6.6 | 2e-09 | 22/45 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.605×** | -6.0 | 1e-07 | 19/44 (CFPAC-1, SHP-77, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.661×** | -4.9 | 4e-05 | 15/46 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.607×** | -4.5 | 3e-04 | 16/46 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.521×** | -4.1 | 0.002 | 14/34 (CFPAC-1, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.719×** | -3.9 | 0.003 | 10/47 (BT-474, PANC-1, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.720×** | -3.9 | 0.003 | 10/45 (SNU-1, H4, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.553×** | -3.7 | 0.007 | 11/40 (A549, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.735×** | -3.7 | 0.008 | 11/44 (SHP-77, SK-MEL-2, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.722×** | -3.5 | 0.013 | 13/41 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.752×** | -3.4 | 0.019 | 6/45 (NCI-H1792, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11381. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 13.4 | 0 | 6 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0695× (z -13.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.145× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 17.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -19.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.205× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 7.36 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0610× (z -10.0) |
| [[PANC-1 (line)]] | alt | 11.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -10.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -8.5) |
| [[A549 (line)]] | wt | 13.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -13.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.136× (z -9.1) |
| [[COLO 205 (line)]] | alt | 13.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 19.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -13.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 3.66 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.100× (z -9.0) |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0754× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 5.39 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0444× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 10.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.101× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 8.33 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0673× (z -12.5) |
| [[NCI-H23 (line)]] | alt | 7.81 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0909× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 6.68 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0706× (z -9.1) |
| [[A-172 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11381), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA4B]] | +0.77 | +0.68 / +0.69 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 4.1 kb 3′ of SEMA4B on the same strand (can correlate by spillover, not regulation) |
| [[TTLL13]] | +0.75 | +0.76 / +0.70 | both halves | 7e-06 | ⚠ same locus (3.7 kb, same strand: neighbours can correlate without regulation) |
| [[CIB1]] | +0.66 | +0.62 / +0.52 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[DUSP5]] | +0.65 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[LYPD3]] | +0.64 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[GPRC5A]] | +0.64 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[WNT7B]] | +0.63 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[EHBP1L1]] | +0.63 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[KRT15]] | +0.63 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[UBA6]] | +0.63 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[SHB]] | +0.62 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[ETHE1]] | +0.62 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[PLEK2]] | +0.62 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[CDCP1]] | +0.62 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[ABHD17C]] | +0.61 | +0.64 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARFGAP2]] | -0.61 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[EFCAB2]] | -0.60 | -0.59 / -0.39 | both halves | 6e-05 |  |
| [[ZMYND11]] | -0.59 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[CASD1]] | -0.59 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[POLR3C]] | -0.59 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[RNF115]] | -0.58 | -0.49 / -0.43 | both halves | 4e-05 |  |
| [[TRAF3IP2-AS1]] | -0.57 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[ZFX]] | -0.56 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[RNF146]] | -0.55 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[SORBS2]] | -0.55 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[BRPF3]] | -0.55 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[NNT]] | -0.55 | -0.48 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF11A]] | B | TNFRSF11A activity raises GDPGP1's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 1.67× lower at baseline in the lines without TNFRSF11A | 0.018 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[CDCP1]] | B | CDCP1 activity raises GDPGP1's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 1.83× lower at baseline in the lines without CDCP1 | 0.026 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[TNFRSF6B]] | B | TNFRSF6B activity raises GDPGP1's level | lines that do not express TNFRSF6B (33) vs lines expressing it (17) | 1.81× lower at baseline in the lines without TNFRSF6B | 0.050 | ⚠ within organs, on part of the lines; also absent: WFDC2, GABRP, FGF19 |
| [[P2RY2]] | B | P2RY2 activity raises GDPGP1's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 1.65× lower at baseline in the lines without P2RY2 | 0.050 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[PLEK2]] | B | PLEK2 activity raises GDPGP1's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 1.75× lower at baseline in the lines without PLEK2 | 0.055 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[FGD6]] | B | FGD6 activity raises GDPGP1's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 1.60× lower at baseline in the lines without FGD6 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |
| [[SLCO4A1]] | B | SLCO4A1 activity raises GDPGP1's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 1.56× lower at baseline in the lines without SLCO4A1 | 0.081 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[PTK6]] | B | PTK6 activity raises GDPGP1's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 1.70× lower at baseline in the lines without PTK6 | 0.082 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |
| [[SYT13]] | B | SYT13 activity raises GDPGP1's level | lines that do not express SYT13 (33) vs lines expressing it (17) | 1.71× lower at baseline in the lines without SYT13 | 0.089 | ⚠ within organs, on part of the lines; also absent: SCEL, HS3ST1, FGFBP1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTLL13]] | C | GDPGP1's natural level strengthens TTLL13's drug response | GDPGP1's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.52; direction not clear | 0.033 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.3, -1.1); signed map (-2.4, 45.8). **Vector** length 77.5, 14.6% of its response variance represented; |z| ≥ 3 in 1,113 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM |  | +4.0 | +7.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.8 | +9.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.6 | +11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +9.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | +10.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.4 | +1.5 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.3 | +0.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.2 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.1 | -14.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.8 | -9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -8.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.7 | -14.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.5 | -3.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.4 | -1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | GDP-D-glucose phosphorylase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:90,233,808-90,245,811 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C15orf58 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZNW5](https://www.uniprot.org/uniprotkb/Q6ZNW5) (GDP-D-glucose phosphorylase 1):

> Specific and highly efficient GDP-D-glucose phosphorylase regulating the levels of GDP-D-glucose in cells. Is involved in adaptive response to stress conditions, and plays a key role in neuronal stress resistance by modulating neuronal glycogen levels and maintaining glucose balance (By similarity).

**Summary**, from NCBI Gene [390637](https://www.ncbi.nlm.nih.gov/gene/390637):

> Enables GDP-D-glucose phosphorylase activity. Involved in glucose metabolic process. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:34360](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34360) · Entrez [390637](https://www.ncbi.nlm.nih.gov/gene/390637) · UniProt [Q6ZNW5](https://www.uniprot.org/uniprotkb/Q6ZNW5) · Ensembl [ENSG00000183208](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183208)

## Data

Gene col 11381: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11381); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11381, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11381]; `tensor/DDL_lfc|DDL_z.npy` [11381]; `embed/gene_vectors.npy` [11381]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11381 or target_col == 11381). Every well: [[GDPGP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GDPGP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
