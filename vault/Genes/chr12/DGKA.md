---
symbol: "DGKA"
type: "gene"
col: 783
ensembl_id: "ENSG00000065357"
name: "diacylglycerol kinase alpha"
location: "12q13.2"
module: 62
arm: "+"
pooled_cpm: 14.11
n_lines_expressing: 44
n_dd_up: 13
n_dd_down: 21
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# DGKA

*diacylglycerol kinase alpha* — 12q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.52× (z +6.0, q 1e-06, up in 21 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.460× (z -15.8, q 0e+00, down in 29 of 41 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.397× (z -13.3, q 1e-37, down in 32 of 39 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SULF2]] (+0.61, fdr 1e-05), [[ADAMTS7]] (+0.57, fdr 6e-05), [[ZMAT3]] (+0.56, fdr 1e-04); moves opposite to [[ST3GAL3]] (-0.47, fdr 4e-05), [[THADA]] (-0.46, fdr 4e-05), [[RAD51B]] (-0.45, fdr 3e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SERPINB5]] → it (grade B ⚠); 2 go from it, the strongest it → [[PJA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 783.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +6.0 | 1e-06 | 21/40 (PANC-1, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +5.2 | 5e-05 | 11/22 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.3 | 0.003 | 1/42 (AN3 CA) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.31×** | +4.2 | 0.004 | 11/42 (A-172, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.004 | 13/41 (A-172, H4, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.005 | 13/41 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +4.0 | 0.005 | 11/40 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +3.8 | 0.010 | 7/41 (PANC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.31×** | +3.8 | 0.011 | 13/40 (A-172, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.29×** | +3.7 | 0.012 | 12/42 (HOP62, SW480, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.19× | +3.6 | 0.016 | 11/42 (LOX-IMVI, A-427, …) | top dose only | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.5 | 0.018 | 8/42 (PANC-1, A498, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.28×** | +3.4 | 0.029 | 15/40 (LS 180, LoVo, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.26×** | +3.4 | 0.031 | 11/41 (NCI-H460, A549, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.055 | 11/41 (NCI-H460, LOX-IMVI, …) | two highest doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.16× | +3.0 | 0.081 | 7/42 (LOX-IMVI, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 783.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.460×** | -15.8 | 0e+00 | 29/41 (AsPC-1, NCI-H2347, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.397×** | -13.3 | 1e-37 | 32/39 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.505×** | -9.8 | 2e-20 | 28/42 (LoVo, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.524×** | -8.9 | 7e-17 | 30/40 (AsPC-1, CFPAC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.558×** | -8.4 | 6e-15 | 26/41 (NCI-H460, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.588×** | -7.6 | 2e-12 | 25/42 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.617×** | -6.9 | 3e-10 | 22/41 (LoVo, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.632×** | -6.6 | 3e-09 | 21/41 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.658×** | -6.0 | 1e-07 | 22/41 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.690×** | -5.3 | 5e-06 | 18/41 (LoVo, SW 1271, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.537×** | -4.7 | 2e-04 | 15/38 (LoVo, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.728×** | -4.6 | 2e-04 | 14/41 (LoVo, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.735×** | -4.4 | 4e-04 | 16/41 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.736×** | -4.4 | 5e-04 | 13/41 (LoVo, A549, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.733×** | -4.2 | 1e-03 | 16/41 (LoVo, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.788×** | -3.3 | 0.027 | 8/41 (SK-MEL-2, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 783. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 46.7 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -16.3) |
| [[CFPAC-1 (line)]] | alt | 20.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -14.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.175× (z -11.7) |
| [[Hs 766T (line)]] | wt | 46.3 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.108× (z -20.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.183× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 43.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0982× (z -21.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[LS 180 (line)]] | wt | 31.5 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.139× (z -12.8) |
| [[COLO 205 (line)]] | alt | 16.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0965× (z -14.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Simotinib (drug)]] 0.05 µM 0.0501× (z -12.0) |
| [[hTERT-HPNE (line)]] | wt | 20.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -12.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.181× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 17.4 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.197× (z -10.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 25.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -20.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.200× (z -12.6) |
| [[A-172 (line)]] | wt | 19.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -15.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HCT15 (line)]] | alt | 15.7 | 0 | 1 | — | [[Busulfan (drug)]] 0.5 µM 0.0558× (z -13.1) |
| [[HT-29 (line)]] | alt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.175× (z -9.0) |
| [[J82 (line)]] | alt | 9.45 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -8.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H1573 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -9.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H460 (line)]] | wt | 7.67 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0902× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[Panc 03.27 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -12.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SNU-423 (line)]] | alt | 6.10 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0738× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SW 900 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -8.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW480 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.176× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A-427 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 783), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SULF2]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[ADAMTS7]] | +0.57 | +0.39 / +0.61 | both halves | 6e-05 |  |
| [[ZMAT3]] | +0.56 | +0.35 / +0.63 | both halves | 1e-04 | pathway: HALLMARK_P53_PATHWAY |
| [[EI24]] | +0.54 | +0.35 / +0.57 | both halves | 1e-04 | pathway: HALLMARK_P53_PATHWAY |
| [[RETSAT]] | +0.53 | +0.35 / +0.58 | both halves | 1e-04 | pathway: HALLMARK_P53_PATHWAY |
| [[PKP1]] | +0.52 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[EFNB1]] | +0.52 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[SDC1]] | +0.52 | +0.50 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[GRHL3]] | +0.51 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[PCDH1]] | +0.51 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[ADGRA2]] | +0.50 | +0.26 / +0.60 | both halves | 4e-04 |  |
| [[SERPINB5]] | +0.50 | +0.50 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_P53_PATHWAY |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST3GAL3]] | -0.47 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[THADA]] | -0.46 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[RAD51B]] | -0.45 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[PRH1]] | -0.43 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[NSMCE2]] | -0.43 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[FBXO17]] | -0.43 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[NCOA5]] | -0.42 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[PRKN]] | -0.42 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[TTC27]] | -0.42 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[WDPCP]] | -0.40 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[SUMF1]] | -0.40 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[LINC01473]] | -0.40 | -0.31 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINB5]] | B | SERPINB5 activity raises DGKA's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 2.16× lower at baseline in the lines without SERPINB5 | 0.033 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[C4BPB]] | B | C4BPB activity raises DGKA's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 1.97× lower at baseline in the lines without C4BPB | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[HS3ST1]] | B | HS3ST1 activity raises DGKA's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 2.01× lower at baseline in the lines without HS3ST1 | 0.080 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[SDC1]] | B | SDC1 activity raises DGKA's level | lines that do not express SDC1 (8) vs lines expressing it (42) | 2.16× lower at baseline in the lines without SDC1 | 0.089 | ⚠ within organs, on part of the lines; also absent: CARD10, MFNG, BMAL2; maybe low, not absent; its own permutation p |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PJA1]] | B | DGKA activity raises PJA1's level | lines that do not express DGKA (6) vs lines expressing it (44) | 1.62× lower at baseline in the lines without DGKA | 0.037 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[EFNB1]] | B | DGKA activity raises EFNB1's level | lines that do not express DGKA (6) vs lines expressing it (44) | 2.20× lower at baseline in the lines without DGKA | 0.063 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.502). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.9, 38.0); signed map (44.7, -24.3). **Vector** length 83.2, 17.2% of its response variance represented; |z| ≥ 3 in 966 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.2 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.4 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | -0.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -13.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -2.3 | -8.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.0 | -15.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -1.7 | -6.9 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.6 | -0.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.5 | +0.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | +0.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.3 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | diacylglycerol kinase alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.2 — chr12:55,927,319-55,954,027 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DGK-alpha; previously DAGK, DAGK1 |
| Gene groups (HGNC) | EF-hand domain containing; Diacylglycerol kinase family |
| Hallmark sets | P53_PATHWAY |
| Reactome | 6 pathways, smallest: Effects of PIP2 hydrolysis; G alpha (q) signalling events; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [P23743](https://www.uniprot.org/uniprotkb/P23743) (Diacylglycerol kinase alpha):

> Diacylglycerol kinase that converts diacylglycerol/DAG into phosphatidic acid/phosphatidate/PA and regulates the respective levels of these two bioactive lipids. Thereby, acts as a central switch between the signaling pathways activated by these second messengers with different cellular targets and opposite effects in numerous biological processes. Also plays an important role in the biosynthesis of complex lipids (Probable). Can also phosphorylate 1-alkyl-2-acylglycerol in vitro as efficiently …

**Summary**, from NCBI Gene [1606](https://www.ncbi.nlm.nih.gov/gene/1606):

> The protein encoded by this gene belongs to the eukaryotic diacylglycerol kinase family. It acts as a modulator that competes with protein kinase C for the second messenger diacylglycerol in intracellular signaling pathways. It also plays an important role in the resynthesis of phosphatidylinositols and phosphorylating diacylglycerol to phosphatidic acid. Several transcript variants encoding different isoforms have been identified for this gene. [provided by RefSeq, Apr 2017]

**Accessions** — [HGNC:2849](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2849) · Entrez [1606](https://www.ncbi.nlm.nih.gov/gene/1606) · UniProt [P23743](https://www.uniprot.org/uniprotkb/P23743) · Ensembl [ENSG00000065357](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065357)

## Data

Gene col 783: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 783); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 783, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 783]; `tensor/DDL_lfc|DDL_z.npy` [783]; `embed/gene_vectors.npy` [783]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 783 or target_col == 783). Every well: [[DGKA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DGKA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
