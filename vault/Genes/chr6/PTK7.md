---
symbol: "PTK7"
type: "gene"
col: 3389
ensembl_id: "ENSG00000112655"
name: "protein tyrosine kinase 7 (inactive)"
location: "6p21.1"
module: 115
arm: "+"
pooled_cpm: 37.37
n_lines_expressing: 41
n_dd_up: 9
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# PTK7

*protein tyrosine kinase 7 (inactive)* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 1.44× (z +9.8, q 4e-20, up in 25 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.435× (z -22.6, q 0e+00, down in 33 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PARD6G]] (+0.66, fdr 9e-06), [[SEMA4D]] (+0.66, fdr 1e-05), [[ZDHHC20]] (+0.62, fdr 1e-05); moves opposite to [[ANKRD17-DT]] (-0.58, fdr 1e-04), [[APLF]] (-0.57, fdr 5e-05), [[CYP20A1]] (-0.56, fdr 6e-05).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[REEP2]] → it (grade B ⚠); 4 go from it, the strongest it → [[MAP4K2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3389.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +9.8 | 4e-20 | 25/38 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +9.6 | 3e-19 | 25/39 (CFPAC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +9.5 | 3e-19 | 20/39 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.28×** | +6.7 | 2e-09 | 19/39 (NCI-H2030, CFPAC-1, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.59×** | +6.5 | 7e-09 | 21/39 (PANC-1, SW 900, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.18× | +6.2 | 5e-08 | 15/39 (NCI-H23, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +5.3 | 7e-06 | 13/35 (Hs 766T, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.21×** | +5.1 | 3e-05 | 15/39 (CFPAC-1, NCI-H2030, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.18× | +4.6 | 3e-04 | 10/39 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.2 | 0.002 | 14/39 (MIA PaCa-2, CFPAC-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.10× | +3.8 | 0.008 | 12/39 (CFPAC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 1.10× | +3.7 | 0.009 | 5/39 (NCI-H23, hTERT-HPNE, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.013 | 11/38 (SNU-1, LOX-IMVI, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.10× | +3.6 | 0.013 | 1/39 (HepG2/C3A) | inconsistent across doses |  |
| [[Brivudine (drug)]] 0.5 µM |  | 1.20× | +3.5 | 0.020 | 6/39 (A-172, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.023 | 11/37 (SW1417, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.13× | +3.3 | 0.037 | 7/39 (NCI-H2347, CFPAC-1, …) | all doses, flat |  |
| [[Rifaximin (drug)]] 5 µM |  | 1.13× | +3.1 | 0.052 | 4/39 (HOP62, SW1417, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3389.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.435×** | -22.6 | 0e+00 | 33/39 (A-427, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.614×** | -18.7 | 0e+00 | 28/39 (RKO, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.529×** | -16.6 | 0e+00 | 27/39 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.622×** | -12.9 | 9e-36 | 30/39 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.655×** | -11.5 | 2e-28 | 26/39 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.715×** | -9.1 | 1e-17 | 22/39 (SNU-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.748×** | -7.6 | 3e-12 | 19/37 (NCI-H23, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.771×** | -7.0 | 1e-10 | 21/39 (NCI-H23, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.774×** | -7.0 | 2e-10 | 22/39 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.777×** | -6.6 | 3e-09 | 21/39 (AN3 CA, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.799×** | -6.1 | 7e-08 | 18/37 (COLO 205, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.876× | -5.1 | 2e-05 | 12/39 (RKO, SW1417, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.950× | -5.0 | 3e-05 | 0/39 | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.826×** | -5.0 | 3e-05 | 13/39 (AN3 CA, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -4.7 | 1e-04 | 15/38 (NCI-H23, RKO, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.845× | -4.6 | 2e-04 | 15/39 (SW1417, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.890× | -4.5 | 2e-04 | 12/39 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.878× | -3.5 | 0.012 | 11/38 (HT-29, HepG2/C3A, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.883× | -3.4 | 0.020 | 10/38 (COLO 205, LOX-IMVI, …) | inconsistent across doses |  |
| [[Pyridoxine (drug)]] 0.05 µM |  | 0.889× | -3.2 | 0.033 | 3/39 (RKO, NCI-H661, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3389. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 60.7 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -19.9) |
| [[SW1417 (line)]] | alt | 90.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -19.7) |
| [[NCI-H2030 (line)]] | alt | 23.4 | 2 (1 ⚠) | 3 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.12× (z +9.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.294× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 68.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -16.8) |
| [[HOP62 (line)]] | alt | 47.4 | 1 | 3 | [[Auranofin (drug)]] 5 µM 2.87× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -12.2) |
| [[A-427 (line)]] | wt | 38.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -18.5) |
| [[HCT15 (line)]] | alt | 104 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.343× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 36.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -15.9) |
| [[NCI-H23 (line)]] | alt | 25.6 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0868× (z -17.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.158× (z -13.4) |
| [[Panc 03.27 (line)]] | alt | 53.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -19.3) |
| [[PANC-1 (line)]] | alt | 54.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.29× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | [[Homoharringtonine (drug)]] 5 µM 0.601× (z -9.8) |
| [[SNU-1 (line)]] | wt | 32.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0523× (z -15.3) |
| [[SW480 (line)]] | alt | 78.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -13.8) |
| [[A-172 (line)]] | wt | 68.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -15.6) |
| [[COLO 205 (line)]] | alt | 23.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -10.2) |
| [[HT-29 (line)]] | alt | 36.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -12.8) |
| [[LoVo (line)]] | wt | 23.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.319× (z -9.8) |
| [[SW48 (line)]] | wt | 131 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.335× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 70.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -12.0) |
| [[C-33 A (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0753× (z -22.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 30.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.399× (z -8.5) |
| [[H4 (line)]] | wt | 61.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 80.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 23.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -9.7) |
| [[A498 (line)]] | wt | 3.29 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.09 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 132 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.70 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.61 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.21 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.35 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3389), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARD6G]] | +0.66 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[SEMA4D]] | +0.66 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[ZDHHC20]] | +0.62 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[AIF1L]] | +0.62 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[PIK3R2]] | +0.61 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[SCD5]] | +0.60 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[SEPTIN6]] | +0.60 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[IGSF8]] | +0.59 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[GRB2]] | +0.59 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[SLC29A4]] | +0.58 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[SEMA6B]] | +0.58 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[TSPAN33]] | +0.58 | +0.51 / +0.37 | both halves | 9e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD17-DT]] | -0.58 | -0.62 / -0.33 | both halves | 1e-04 |  |
| [[APLF]] | -0.57 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[CYP20A1]] | -0.56 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[ZNF181]] | -0.55 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[RFX3-DT]] | -0.55 | -0.55 / -0.26 | both halves | 4e-04 |  |
| [[RPAP2]] | -0.55 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[ZC3H6]] | -0.55 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[CHD1-DT]] | -0.55 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[ERCC6L2]] | -0.55 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[BCDIN3D]] | -0.54 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[ZNF337-AS1]] | -0.54 | -0.57 / -0.26 | both halves | 4e-04 |  |
| [[HELQ]] | -0.54 | -0.51 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[REEP2]] | B | REEP2 activity raises PTK7's level | lines that do not express REEP2 (12) vs lines expressing it (38) | 2.48× lower at baseline in the lines without REEP2 | 0.040 | ⚠ within organs, on part of the lines; also absent: DLK2, ENSG00000234405, STARD9; maybe low, not absent |
| [[FXYD6]] | B | FXYD6 activity raises PTK7's level | lines that do not express FXYD6 (25) vs lines expressing it (25) | 2.22× lower at baseline in the lines without FXYD6 | 0.059 | ⚠ within organs, on part of the lines; also absent: MARK1, KIF1A, MAP6 |
| [[EMID1]] | B | EMID1 activity raises PTK7's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 2.46× lower at baseline in the lines without EMID1 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers PTK7's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SEMA3F]] | B | SEMA3F activity raises PTK7's level | lines that do not express SEMA3F (6) vs lines expressing it (44) | 2.43× lower at baseline in the lines without SEMA3F | 0.0999 | ⚠ within organs, on part of the lines; also absent: MCM2, PIMREG, GKAP1 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP4K2]] | B | PTK7 activity raises MAP4K2's level | lines that do not express PTK7 (9) vs lines expressing it (41) | 1.83× lower at baseline in the lines without PTK7 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000289985, ZNF433, ENSG00000269755 |
| [[TLE2]] | B | PTK7 activity raises TLE2's level | lines that do not express PTK7 (9) vs lines expressing it (41) | 2.00× lower at baseline in the lines without PTK7 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000289985, ZNF433, ENSG00000269755 |
| [[PIK3R2]] | B | PTK7 activity raises PIK3R2's level | lines that do not express PTK7 (9) vs lines expressing it (41) | 1.36× lower at baseline in the lines without PTK7 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000289985, ZNF433, ENSG00000269755 |
| [[JAM3]] | B | PTK7 activity raises JAM3's level | lines that do not express PTK7 (9) vs lines expressing it (41) | 2.31× lower at baseline in the lines without PTK7 | 0.0995 | ⚠ within organs, on part of the lines; also absent: ENSG00000289985, ZNF433, ENSG00000269755 |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.662). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (2.6, 38.4); signed map (-22.3, 35.9). **Vector** length 91.0, 19.3% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +5.7 | +9.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.3 | +9.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.8 | +9.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +1.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.2 | -12.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.1 | -22.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -7.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -16.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.5 | -4.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -6.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -4.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine kinase 7 (inactive) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:43,076,307-43,161,719 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CCK4 |
| Gene groups (HGNC) | I-set domain containing; Pseudokinases; WNT binding RTK type pseudokinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13308](https://www.uniprot.org/uniprotkb/Q13308) (Inactive tyrosine-protein kinase 7):

> Inactive tyrosine kinase involved in the Wnt signaling pathway. Component of both the non-canonical (also known as the Wnt/planar cell polarity signaling) and the canonical Wnt signaling pathways. Functions in cell adhesion, cell migration, cell polarity, proliferation, actin cytoskeleton reorganization and apoptosis. Has a role in embryogenesis, epithelial tissue organization and angiogenesis. Does not bind ATP.

**Summary**, from NCBI Gene [5754](https://www.ncbi.nlm.nih.gov/gene/5754):

> This gene encodes a member of the receptor protein tyrosine kinase family of proteins that transduce extracellular signals across the cell membrane. The encoded protein lacks detectable catalytic tyrosine kinase activity, is involved in the Wnt signaling pathway and plays a role in multiple cellular processes including polarity and adhesion. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:9618](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9618) · Entrez [5754](https://www.ncbi.nlm.nih.gov/gene/5754) · UniProt [Q13308](https://www.uniprot.org/uniprotkb/Q13308) · Ensembl [ENSG00000112655](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112655)

## Data

Gene col 3389: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3389); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3389, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3389]; `tensor/DDL_lfc|DDL_z.npy` [3389]; `embed/gene_vectors.npy` [3389]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3389 or target_col == 3389). Every well: [[PTK7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTK7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
