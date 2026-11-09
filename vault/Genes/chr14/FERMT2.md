---
symbol: "FERMT2"
type: "gene"
col: 1057
ensembl_id: "ENSG00000073712"
name: "FERM domain containing kindlin 2"
location: "14q22.1"
module: 111
arm: "+"
pooled_cpm: 118.19
n_lines_expressing: 42
n_dd_up: 4
n_dd_down: 22
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# FERMT2

*FERM domain containing kindlin 2* — 14q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.03× (z +7.6, q 1e-11, up in 29 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 2 lines (A498 2.66×, J82 2.05×; ⚠ cell-cycle shift, explains ~64% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 2.20×; ⚠ cell-cycle shift, explains ~0% of this change); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (CFPAC-1 2.09×); [[TAK-901 (drug)]] 5 µM in 1 line (MIA PaCa-2 4.24×).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.534× (z -18.3, q 0e+00, down in 37 of 41 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RTN4]] (+0.57, fdr 1e-05), [[ELL2]] (+0.56, fdr 1e-05), [[KLF7]] (+0.54, fdr 1e-05); moves opposite to [[ZCCHC4]] (-0.49, fdr 5e-05), [[ALG14]] (-0.45, fdr 9e-05), [[MIATNB]] (-0.44, fdr 0.001, ⚠ not reproduced), [[CAB39L]] (-0.44, fdr 7e-04).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[GLIPR2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1057.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 2 lines (A498 2.66×, J82 2.05×; ⚠ cell-cycle shift, explains ~64% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 2.20×; ⚠ cell-cycle shift, explains ~0% of this change); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (CFPAC-1 2.09×); [[TAK-901 (drug)]] 5 µM in 1 line (MIA PaCa-2 4.24×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.03×** | +7.6 | 1e-11 | 29/41 (MIA PaCa-2, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.33×** | +5.8 | 1e-06 | 25/40 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +5.0 | 1e-04 | 20/40 (A-172, A498, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +4.6 | 7e-04 | 18/41 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.20×** | +3.6 | 0.030 | 16/40 (HOP62, hTERT-HPNE, …) | two highest doses |  |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 1.19× | +3.4 | 0.054 | 13/40 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.17 | 11/39 (LoVo, J82, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1057.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.534×** | -18.3 | 0e+00 | 37/41 (A549, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.466×** | -15.7 | 0e+00 | 36/40 (J82, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.487×** | -14.8 | 0e+00 | 33/40 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.515×** | -13.1 | 3e-37 | 32/39 (NCI-H2347, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.536×** | -12.4 | 5e-33 | 30/37 (C-33 A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.619×** | -9.9 | 5e-21 | 28/40 (HOP62, J82, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.650×** | -8.5 | 1e-15 | 26/40 (HOP62, A549, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.749×** | -8.4 | 3e-15 | 28/40 (A549, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.663×** | -8.2 | 2e-14 | 31/40 (A549, CHP-212, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.675×** | -7.5 | 4e-12 | 23/38 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.689×** | -7.4 | 8e-12 | 28/42 (NCI-H2347, hTERT-HPNE, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.786×** | -7.0 | 1e-10 | 26/40 (HOP62, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.720×** | -6.8 | 6e-10 | 26/41 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.726×** | -6.6 | 2e-09 | 26/40 (NCI-H23, SNU-423, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.743×** | -6.1 | 4e-08 | 24/40 (NCI-H2347, C32, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.763×** | -5.4 | 3e-06 | 23/40 (A549, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.801×** | -4.6 | 2e-04 | 21/40 (NCI-H23, HOP62, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.863× | -4.3 | 6e-04 | 15/40 (A549, J82, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.834× | -3.7 | 0.005 | 19/40 (A549, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.830×** | -3.7 | 0.005 | 19/40 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.838× | -3.6 | 0.007 | 16/40 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Riluzole hydrochloride (drug)]] 5 µM |  | 0.892× | -3.3 | 0.020 | 2/41 (NCI-H23, CFPAC-1) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.853× | -3.3 | 0.024 | 16/41 (HS-578T, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1057. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 247 | 0 | 13 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -22.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -18.3) |
| [[HOP62 (line)]] | alt | 184 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.274× (z -15.7) |
| [[A549 (line)]] | wt | 222 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -23.4) |
| [[A498 (line)]] | wt | 107 | 3 (3 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +15.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.416× (z -12.1) |
| [[J82 (line)]] | alt | 188 | 1 (1 ⚠) | 6 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.05× (z +10.1) ⚠ cell-cycle shift, explains ~64% of this change | [[Panobinostat (drug)]] 0.5 µM 0.306× (z -17.3) |
| [[HepG2_C3A (line)]] | wt | 237 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -18.9) |
| [[HS-578T (line)]] | alt | 175 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -15.3) |
| [[A-172 (line)]] | wt | 115 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -13.4) |
| [[C32 (line)]] | wt | 166 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -14.1) |
| [[LOX-IMVI (line)]] | wt | 150 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.332× (z -14.6) |
| [[NCI-H1792 (line)]] | alt | 150 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -13.9) |
| [[Panc 03.27 (line)]] | alt | 104 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.414× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 178 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.377× (z -11.4) |
| [[SNU-423 (line)]] | alt | 155 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.307× (z -12.6) |
| [[CFPAC-1 (line)]] | alt | 154 | 1 | 3 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.09× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 113 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.24× (z +8.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.397× (z -10.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.415× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 139 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -14.7) |
| [[C-33 A (line)]] | alt | 177 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0785× (z -24.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 144 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.393× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -12.1) |
| [[Hs 766T (line)]] | wt | 103 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -13.7) |
| [[hTERT-HPNE (line)]] | wt | 203 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -10.9) |
| [[SW480 (line)]] | alt | 61.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.468× (z -10.1) |
| [[AN3 CA (line)]] | alt | 134 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0804× (z -17.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 248 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -9.0) |
| [[H4 (line)]] | wt | 123 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -14.9) |
| [[NCI-H460 (line)]] | wt | 102 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.543× (z -10.1) |
| [[BT-474 (line)]] | alt | 70.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.346× (z -9.1) ⚠ cell-cycle shift, explains ~53% of this change |
| [[NCI-H2030 (line)]] | alt | 255 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.486× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 111 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -11.1) |
| [[SHP-77 (line)]] | alt | 134 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -9.4) |
| [[SW 900 (line)]] | alt | 169 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[A-427 (line)]] | wt | 100 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.83 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.80 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.34 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.46 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.00 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1057), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTN4]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[ELL2]] | +0.56 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[KLF7]] | +0.54 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[MRTFA]] | +0.52 | +0.36 / +0.49 | both halves | 1e-04 |  |
| [[VCL]] | +0.51 | +0.40 / +0.53 | both halves | 5e-05 | pathway: Cell junction organization; STRING 896 |
| [[CLIC4]] | +0.51 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[DENND5A]] | +0.51 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[DAPK3]] | +0.49 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[STK17A]] | +0.48 | +0.51 / +0.33 | both halves | 1e-04 |  |
| [[TPM4]] | +0.47 | +0.47 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[GLIPR1]] | +0.46 | +0.45 / +0.48 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[TANC2]] | +0.46 | +0.43 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCCHC4]] | -0.49 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[ALG14]] | -0.45 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[MIATNB]] | -0.44 | -0.42 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[CAB39L]] | -0.44 | -0.39 / -0.21 | both halves | 7e-04 |  |
| [[SLC16A4-AS1]] | -0.43 | -0.31 / -0.33 | both halves | 2e-04 |  |
| [[TNFSF13B]] | -0.43 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[GLIPR1-AS1]] | -0.42 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[ITPKB]] | -0.41 | -0.28 / -0.30 | both halves | 3e-04 |  |
| [[DENND11]] | -0.41 | -0.26 / -0.44 | both halves | 4e-04 |  |
| [[TRMT2B]] | -0.40 | -0.23 / -0.34 | both halves | 5e-04 |  |
| [[CEP20]] | -0.40 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[MGST2]] | -0.40 | -0.31 / -0.31 | both halves | 2e-04 |  |
| [[NAF1]] | -0.39 | -0.41 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises FERMT2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GLIPR2]] | B | GLIPR2 activity raises FERMT2's level | lines that do not express GLIPR2 (9) vs lines expressing it (41) | 2.30× lower at baseline in the lines without GLIPR2 | 0.081 | ⚠ within organs, on part of the lines; also absent: OSBPL6, HAPLN3, LHFPL6 |
| [[CLTCL1]] | C | CLTCL1 activity raises FERMT2's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 9.57× lower at baseline in the lines without CLTCL1 | 0.006 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |
| [[DENND5A]] | C | DENND5A activity raises FERMT2's level | lines that do not express DENND5A (3) vs lines expressing it (47) | 9.54× lower at baseline in the lines without DENND5A | 0.018 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23 |
| [[DNAAF9]] | C | DNAAF9 activity raises FERMT2's level | lines that do not express DNAAF9 (12) vs lines expressing it (38) | 7.59× lower at baseline in the lines without DNAAF9 | 0.060 | ⚠ within organs, on part of the lines; also absent: CHST10, ENSG00000268163, RIMKLB; co-absent with the target; its own permutation p |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLIPR2]] | B | FERMT2 activity raises GLIPR2's level | lines that do not express FERMT2 (8) vs lines expressing it (42) | 2.67× lower at baseline in the lines without FERMT2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ZNF512B, HLTF, SIX1 |
| [[CDC42EP3]] | B | FERMT2 activity raises CDC42EP3's level | lines that do not express FERMT2 (8) vs lines expressing it (42) | 3.00× lower at baseline in the lines without FERMT2 | 0.068 | ⚠ within organs, on part of the lines; also absent: ZNF512B, HLTF, SIX1 |

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.426). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.5, 10.1); signed map (-8.6, 36.2). **Vector** length 111, 33.3% of its response variance represented; |z| ≥ 3 in 1,086 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +3.8 | +1.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | -1.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.2 | -3.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.2 | -9.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | -0.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +4.6 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | +2.0 | +1.7 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -4.9 | -3.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.8 | -2.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.1 | -1.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -4.0 | -8.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.9 | -8.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.3 | -6.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.7 | -3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -0.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | FERM domain containing kindlin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.1 — chr14:52,857,268-52,952,435 (-) |
| Ensembl biotype | protein_coding |
| Also known as | mig-2, KIND2, UNC112B; previously PLEKHC1 |
| Gene groups (HGNC) | Fermitins; Pleckstrin homology domain containing; FERM domain containing |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 8 pathways, smallest: Cell-extracellular matrix interactions; RAC3 GTPase cycle; RAC1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AC1](https://www.uniprot.org/uniprotkb/Q96AC1) (Fermitin family homolog 2):

> Scaffolding protein that enhances integrin activation mediated by TLN1 and/or TLN2, but activates integrins only weakly by itself. Binds to membranes enriched in phosphoinositides. Enhances integrin-mediated cell adhesion onto the extracellular matrix and cell spreading; this requires both its ability to interact with integrins and with phospholipid membranes. Required for the assembly of focal adhesions. Participates in the connection between extracellular matrix adhesion sites and the actin …

**Summary**, from NCBI Gene [10979](https://www.ncbi.nlm.nih.gov/gene/10979):

> Enables several functions, including phosphatidylinositol-3,4,5-trisphosphate binding activity; protein serine/threonine kinase binding activity; and type I transforming growth factor beta receptor binding activity. Involved in several processes, including cell surface receptor signaling pathway; positive regulation of cellular component biogenesis; and positive regulation of intracellular signal transduction. Acts upstream of or within cell adhesion and protein localization to cell junction. …

**Accessions** — [HGNC:15767](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15767) · Entrez [10979](https://www.ncbi.nlm.nih.gov/gene/10979) · UniProt [Q96AC1](https://www.uniprot.org/uniprotkb/Q96AC1) · Ensembl [ENSG00000073712](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073712)

## Data

Gene col 1057: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1057); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1057, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1057]; `tensor/DDL_lfc|DDL_z.npy` [1057]; `embed/gene_vectors.npy` [1057]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1057 or target_col == 1057). Every well: [[FERMT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FERMT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
