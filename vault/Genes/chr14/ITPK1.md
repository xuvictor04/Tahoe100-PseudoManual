---
symbol: "ITPK1"
type: "gene"
col: 2000
ensembl_id: "ENSG00000100605"
name: "inositol-tetrakisphosphate 1-kinase"
location: "14q32.12"
module: 31
arm: "+"
pooled_cpm: 57.63
n_lines_expressing: 46
n_dd_up: 13
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 17
direction_downstream: 23
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# ITPK1

*inositol-tetrakisphosphate 1-kinase* — 14q32.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.37× (z +7.8, q 5e-12, up in 23 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.676× (z -13.6, q 2e-39, down in 27 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCR]] (+0.73, fdr 7e-06), [[TNS4]] (+0.62, fdr 7e-06), [[ZDHHC3]] (+0.58, fdr 1e-05); moves opposite to [[THAP6]] (-0.50, fdr 7e-05), [[SLC41A2]] (-0.50, fdr 4e-05), [[THAP1]] (-0.50, fdr 4e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[IGFL2]] → it (grade B ⚠); 23 go from it, the strongest it → cells under [[Canagliflozin (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2000.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +7.8 | 5e-12 | 23/44 (NCI-H1792, RKO, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.37×** | +7.7 | 5e-12 | 20/43 (NCI-H1792, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **1.34×** | +7.2 | 1e-10 | 18/40 (NCI-H1792, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +7.1 | 2e-10 | 20/43 (NCI-H1792, H4, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.30×** | +6.5 | 9e-09 | 18/44 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +5.4 | 8e-06 | 14/44 (NCI-H2347, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.24×** | +5.3 | 8e-06 | 18/43 (SW48, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.24×** | +5.2 | 1e-05 | 17/44 (NCI-H1792, CFPAC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.23×** | +5.0 | 3e-05 | 17/43 (NCI-H1792, J82, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.24×** | +4.9 | 5e-05 | 14/44 (NCI-H1573, NCI-H1792, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +4.9 | 6e-05 | 12/43 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.23×** | +4.6 | 2e-04 | 13/35 (NCI-H1792, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +4.5 | 4e-04 | 7/44 (BT-474, NCI-H1792, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +4.3 | 7e-04 | 14/44 (NCI-H2347, J82, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.18× | +4.1 | 0.002 | 11/41 (NCI-H2347, A549, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.18× | +4.0 | 0.002 | 9/43 (NCI-H1573, CFPAC-1, …) | all doses, flat |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.12× | +3.9 | 0.004 | 7/44 (LS 180, LoVo, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.005 | 6/41 (hTERT-HPNE, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | 1.16× | +3.6 | 0.008 | 11/43 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 5 µM |  | 1.13× | +3.0 | 0.080 | 0/45 | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.14× | +2.9 | 0.081 | 12/42 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 1.13× | +2.9 | 0.087 | 14/44 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.13× | +2.9 | 0.090 | 11/44 (SW48, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2000.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.676×** | -13.6 | 2e-39 | 27/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.634×** | -11.2 | 1e-26 | 27/44 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.775×** | -8.9 | 1e-16 | 21/44 (J82, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.779×** | -6.2 | 1e-07 | 16/44 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.807×** | -5.3 | 2e-05 | 20/42 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.814×** | -5.1 | 4e-05 | 17/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -4.3 | 0.001 | 15/44 (SW480, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.835× | -4.3 | 0.001 | 17/44 (LoVo, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.830×** | -4.3 | 0.001 | 10/43 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.838× | -4.2 | 0.002 | 10/43 (KATO III, NCI-H460, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **0.791×** | -4.1 | 0.002 | 12/40 (RKO, SHP-77, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.843× | -4.0 | 0.002 | 20/41 (HepG2/C3A, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.852× | -3.9 | 0.003 | 14/43 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.855× | -3.9 | 0.004 | 11/43 (NCI-H460, LoVo, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.868× | -3.5 | 0.018 | 13/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.05 µM |  | 0.880× | -3.0 | 0.088 | 9/44 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.882× | -3.0 | 0.088 | 14/43 (NCI-H460, LoVo, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2000. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 246 | 0 | 21 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -27.4) |
| [[LoVo (line)]] | wt | 142 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -26.8) |
| [[Hs 766T (line)]] | wt | 141 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -21.7) |
| [[AsPC-1 (line)]] | alt | 101 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -19.7) |
| [[KATO III (line)]] | alt | 93.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -12.6) |
| [[SW48 (line)]] | wt | 150 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.57× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.0541× (z -23.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.278× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 25.1 | 3 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.54× (z +8.7) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SNU-1 (line)]] | wt | 43.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -12.3) |
| [[LS 180 (line)]] | wt | 132 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -17.2) |
| [[RKO (line)]] | wt | 37.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0848× (z -21.3) |
| [[HCT15 (line)]] | alt | 39.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[HEC-1-A (line)]] | alt | 52.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.462× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 55.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0779× (z -17.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 46.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -10.1) |
| [[J82 (line)]] | alt | 32.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.497× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 26.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 22.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 81.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -13.2) |
| [[SHP-77 (line)]] | alt | 36.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[A-172 (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.23 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 52.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2000), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCR]] | +0.73 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[TNS4]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[ZDHHC3]] | +0.58 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[PYGB]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[IGSF9]] | +0.57 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[TBC1D14]] | +0.57 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[KRT6A]] | +0.56 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[CYRIB]] | +0.56 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[SLC45A4]] | +0.56 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ARHGAP8]] | +0.55 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[ANO1]] | +0.55 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[TSPAN14]] | +0.55 | +0.62 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP6]] | -0.50 | -0.52 / -0.37 | both halves | 7e-05 |  |
| [[SLC41A2]] | -0.50 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[THAP1]] | -0.50 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[ZDBF2]] | -0.49 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[THAP2]] | -0.48 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[TRPC1]] | -0.48 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[METTL6]] | -0.47 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[DNAI4]] | -0.47 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[PPP4R3B]] | -0.47 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[GPR158]] | -0.46 | -0.47 / -0.27 | both halves | 3e-04 |  |
| [[DCP1A]] | -0.46 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[ZNF764]] | -0.46 | -0.42 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 15, C 2. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IGFL2]] | B | IGFL2 activity raises ITPK1's level | lines that do not express IGFL2 (38) vs lines expressing it (12) | 2.61× lower at baseline in the lines without IGFL2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, REG4, GPA33 |
| [[HR]] | B | HR activity raises ITPK1's level | lines that do not express HR (23) vs lines expressing it (27) | 2.03× lower at baseline in the lines without HR | 0.007 | ⚠ within organs, on part of the lines; also absent: SULF2, CEACAM1, HNF1A-AS1 |
| [[SERPINB5]] | B | SERPINB5 activity raises ITPK1's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 2.47× lower at baseline in the lines without SERPINB5 | 0.007 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[MAOB]] | B | MAOB activity raises ITPK1's level | lines that do not express MAOB (34) vs lines expressing it (16) | 2.16× lower at baseline in the lines without MAOB | 0.022 | ⚠ within organs, on part of the lines; also absent: SLC44A4, LGR6, AZGP1 |
| [[KRT6A]] | B | KRT6A activity raises ITPK1's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 2.57× lower at baseline in the lines without KRT6A | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588 |
| [[LINC02582]] | B | LINC02582 activity weakens ITPK1's drug response | lines that do not express LINC02582 (37) vs lines expressing it (8) | the lines without LINC02582 respond 2.10× as strongly (z diff -1.33); strongest at Panobinostat 5 µM: 1.45x vs 0.61x (z diff -7.1) | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; target measured in part of the lines; artifact flags |
| [[NRCAM]] | B | NRCAM activity raises ITPK1's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 1.57× lower at baseline in the lines without NRCAM | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG |
| [[MMP28]] | B | MMP28 activity raises ITPK1's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.38× lower at baseline in the lines without MMP28 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |
| [[DSG4]] | B | DSG4 activity raises ITPK1's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 2.87× lower at baseline in the lines without DSG4 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031 |
| [[IGFL2]] | B | IGFL2 activity weakens ITPK1's drug response | lines that do not express IGFL2 (34) vs lines expressing it (11) | the lines without IGFL2 respond 1.83× as strongly (z diff -1.17); strongest at Panobinostat 5 µM: 1.47x vs 0.75x (z diff -5.2) | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, REG4, GPA33; target measured in part of the lines; artifact flags |
| [[LINC02320]] | B | LINC02320 activity raises ITPK1's level | lines that do not express LINC02320 (19) vs lines expressing it (31) | 1.96× lower at baseline in the lines without LINC02320 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000258919, TSPAN1, ENSG00000266088 |
| [[LINC02582]] | B | LINC02582 activity raises ITPK1's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 2.52× lower at baseline in the lines without LINC02582 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975 |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 0, C 23. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Canagliflozin (drug)]] 5 µM | C | ITPK1 activity raises the cells' numbers under Canagliflozin 5 µM (protects the cells) | lines that do not express ITPK1 (4) vs lines expressing it (44) | the lines without ITPK1: 0.78× the cells of the other lines | 0.013 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent |
| cells under [[Isocorydine (drug)]] 5 µM | C | ITPK1 activity raises the cells' numbers under Isocorydine 5 µM (protects the cells) | lines that do not express ITPK1 (4) vs lines expressing it (44) | the lines without ITPK1: 0.84× the cells of the other lines | 0.027 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent |
| cells under [[Pitavastatin (Calcium) (drug)]] 0.5 µM | C | ITPK1 activity raises the cells' numbers under Pitavastatin (Calcium) 0.5 µM (protects the cells) | lines that do not express ITPK1 (4) vs lines expressing it (44) | the lines without ITPK1: 0.65× the cells of the other lines | 0.028 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent |
| cells under [[Pimozide (drug)]] 0.05 µM | C | ITPK1 activity raises the cells' numbers under Pimozide 0.05 µM (protects the cells) | lines that do not express ITPK1 (4) vs lines expressing it (44) | the lines without ITPK1: 0.79× the cells of the other lines | 0.030 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent |
| cells under [[Furosemide (drug)]] 0.5 µM | C | ITPK1 activity raises the cells' numbers under Furosemide 0.5 µM (protects the cells) | lines that do not express ITPK1 (4) vs lines expressing it (44) | the lines without ITPK1: 0.80× the cells of the other lines | 0.034 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent |
| cells under [[Pravastatin (sodium) (drug)]] 5 µM | C | ITPK1 activity lowers the cells' numbers under Pravastatin (sodium) 5 µM (makes them more sensitive) | lines that do not express ITPK1 (4) vs lines expressing it (44) | the lines without ITPK1: 1.24× the cells of the other lines | 0.035 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent |
| cells under [[AZD2858 (drug)]] 5 µM | C | ITPK1 activity raises the cells' numbers under AZD2858 5 µM (protects the cells) | lines that do not express ITPK1 (4) vs lines expressing it (44) | the lines without ITPK1: 0.69× the cells of the other lines | 0.043 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent |
| cells under [[Pemetrexed (drug)]] 0.5 µM | C | ITPK1 activity raises the cells' numbers under Pemetrexed 0.5 µM (protects the cells) | lines that do not express ITPK1 (4) vs lines expressing it (44) | the lines without ITPK1: 0.66× the cells of the other lines | 0.044 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent |
| [[IGFBP4]] | C | ITPK1 activity strengthens IGFBP4's drug response | lines that do not express ITPK1 (3) vs lines expressing it (26) | the lines without ITPK1 respond 0.66× as strongly (z diff +2.79); strongest at Homoharringtonine 5 µM: 0.92x vs 0.31x (z diff +7.6) | 0.047 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent; target measured in part of the lines; artifact flags |
| cells under [[Piroxicam (drug)]] 0.05 µM | C | ITPK1 activity lowers the cells' numbers under Piroxicam 0.05 µM (makes them more sensitive) | lines that do not express ITPK1 (4) vs lines expressing it (44) | the lines without ITPK1: 1.29× the cells of the other lines | 0.047 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent |
| cells under [[Neratinib (maleate) (drug)]] 0.05 µM | C | ITPK1 activity lowers the cells' numbers under Neratinib (maleate) 0.05 µM (makes them more sensitive) | lines that do not express ITPK1 (4) vs lines expressing it (44) | the lines without ITPK1: 1.26× the cells of the other lines | 0.055 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent |
| cells under [[Adagrasib (drug)]] 0.05 µM | C | ITPK1 activity lowers the cells' numbers under Adagrasib 0.05 µM (makes them more sensitive) | lines that do not express ITPK1 (4) vs lines expressing it (44) | the lines without ITPK1: 1.07× the cells of the other lines | 0.057 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent; cell counts less trustworthy |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.407). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.8, 50.4); signed map (4.7, 37.0). **Vector** length 125, 33.5% of its response variance represented; |z| ≥ 3 in 1,183 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.5 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | +4.0 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +4.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +3.0 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +3.0 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +3.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.7 | +3.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.4 | +4.0 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.3 | -8.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.7 | -11.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.4 | -13.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.0 | -4.3 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.8 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.6 | -3.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -2.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | inositol-tetrakisphosphate 1-kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.12 — chr14:92,936,914-93,116,320 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Inositol phosphate kinases; ATP-grasp fold containing |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 5 pathways, smallest: Synthesis of pyrophosphates in the cytosol; Synthesis of IP3 and IP4 in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13572](https://www.uniprot.org/uniprotkb/Q13572) (Inositol-tetrakisphosphate 1-kinase):

> Kinase that can phosphorylate various inositol polyphosphate such as Ins(3,4,5,6)P4 or Ins(1,3,4)P3. Phosphorylates Ins(3,4,5,6)P4 at position 1 to form Ins(1,3,4,5,6)P5. This reaction is thought to have regulatory importance, since Ins(3,4,5,6)P4 is an inhibitor of plasma membrane Ca(2+)-activated Cl(-) channels, while Ins(1,3,4,5,6)P5 is not. Also phosphorylates Ins(1,3,4)P3 on O-5 and O-6 to form Ins(1,3,4,6)P4, an essential molecule in the hexakisphosphate (InsP6) pathway. Also acts as an …

**Summary**, from NCBI Gene [3705](https://www.ncbi.nlm.nih.gov/gene/3705):

> This gene encodes an enzyme that belongs to the inositol 1,3,4-trisphosphate 5/6-kinase family. This enzyme regulates the synthesis of inositol tetraphosphate, and downstream products, inositol pentakisphosphate and inositol hexakisphosphate. Inositol metabolism plays a role in the development of the neural tube. Disruptions in this gene are thought to be associated with neural tube defects. A pseudogene of this gene has been identified on chromosome X. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:6177](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6177) · Entrez [3705](https://www.ncbi.nlm.nih.gov/gene/3705) · UniProt [Q13572](https://www.uniprot.org/uniprotkb/Q13572) · Ensembl [ENSG00000100605](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100605)

## Data

Gene col 2000: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2000); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2000, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2000]; `tensor/DDL_lfc|DDL_z.npy` [2000]; `embed/gene_vectors.npy` [2000]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2000 or target_col == 2000). Every well: [[ITPK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITPK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
