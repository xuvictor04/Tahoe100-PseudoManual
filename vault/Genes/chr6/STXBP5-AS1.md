---
symbol: "STXBP5-AS1"
type: "gene"
col: 13903
ensembl_id: "ENSG00000233452"
name: "STXBP5 antisense RNA 1"
location: "6q24.3"
module: 98
arm: "+"
pooled_cpm: 8.22
n_lines_expressing: 46
n_dd_up: 36
n_dd_down: 21
n_dd_up_clean: 32
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# STXBP5-AS1

*STXBP5 antisense RNA 1* — 6q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.11× (z +17.1, q 0e+00, up in 31 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.347× (z -11.2, q 1e-26, down in 29 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00607]] (+0.74, fdr 7e-06), [[TBXAS1]] (+0.73, fdr 7e-06), [[ITGA10]] (+0.67, fdr 7e-06); moves opposite to [[PAFAH1B3]] (-0.51, fdr 4e-04), [[PER3]] (-0.51, fdr 4e-05), [[ARRB2]] (-0.50, fdr 2e-04).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[DNER]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13903.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.11×** | +17.1 | 0e+00 | 31/38 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.34×** | +12.8 | 4e-35 | 31/43 (HOP62, A498, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +8.1 | 1e-13 | 20/35 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.92×** | +6.9 | 5e-10 | 22/38 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +6.6 | 4e-09 | 16/36 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.92×** | +6.4 | 1e-08 | 6/19 (LOX-IMVI, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.78×** | +6.1 | 7e-08 | 19/38 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.78×** | +6.1 | 7e-08 | 22/41 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.77×** | +6.1 | 9e-08 | 20/40 (HOP62, SW 900, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.69×** | +5.6 | 1e-06 | 16/42 (HOP62, SW 900, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.68×** | +5.5 | 2e-06 | 20/43 (HOP62, SW 900, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +5.5 | 2e-06 | 20/42 (SW480, BT-474, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.42×** | +5.3 | 4e-06 | 21/42 (HOP62, H4, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.64×** | +5.3 | 6e-06 | 16/40 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +5.3 | 6e-06 | 15/40 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.54×** | +4.3 | 7e-04 | 16/38 (HOP62, SW 900, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13903.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.347×** | -11.2 | 1e-26 | 29/44 (NCI-H1792, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.348×** | -11.2 | 1e-26 | 32/43 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.385×** | -10.1 | 8e-22 | 32/42 (NCI-H1792, HT-29, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.402×** | -9.7 | 6e-20 | 26/42 (J82, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.597×** | -7.7 | 1e-12 | 24/39 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.508×** | -7.2 | 7e-11 | 26/41 (LS 180, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~25% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.568×** | -5.8 | 6e-07 | 17/31 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.587×** | -5.6 | 1e-06 | 18/41 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.596×** | -5.5 | 3e-06 | 21/35 (NCI-H1573, SW480, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.633×** | -4.8 | 7e-05 | 19/39 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.434×** | -4.6 | 2e-04 | 14/40 (J82, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.652×** | -4.5 | 3e-04 | 16/37 (HEC-1-A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.661×** | -4.4 | 5e-04 | 16/40 (SNU-423, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.687×** | -4.0 | 0.003 | 9/39 (NCI-H1573, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.496×** | -3.9 | 0.004 | 18/39 (SW 900, HT-29, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.715×** | -3.6 | 0.014 | 12/43 (Panc 03.27, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.803×** | -3.3 | 0.033 | 14/42 (SHP-77, NCI-H1573, …) | two highest doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Vilanterol (drug)]] 5 µM |  | **0.812×** | -3.1 | 0.056 | 6/42 (SNU-1, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13903. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 14.0 | 15 | 0 | [[Clobetasol propionate (drug)]] 0.5 µM 11.8× (z +12.0) | — |
| [[SW 900 (line)]] | alt | 9.24 | 4 | 1 (1 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 13.1× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -8.6) ⚠ cell-cycle shift, explains ~59% of this change |
| [[SW480 (line)]] | alt | 9.06 | 2 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0904× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.160× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 13.7 | 1 | 3 | [[Clobetasol propionate (drug)]] 0.5 µM 7.99× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.0774× (z -10.7) |
| [[HS-578T (line)]] | alt | 11.5 | 3 | 0 | [[Clobetasol propionate (drug)]] 0.5 µM 13.2× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 10.6 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0343× (z -13.5) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[NCI-H460 (line)]] | wt | 13.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -12.9) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.133× (z -10.2) |
| [[LoVo (line)]] | wt | 4.78 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.85× (z +10.3) | [[Digitoxin (drug)]] 5 µM 0.0945× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[LS 180 (line)]] | wt | 14.4 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0559× (z -13.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[MIA PaCa-2 (line)]] | alt | 17.7 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0984× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 2.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.93× (z +9.5) | — |
| [[BT-474 (line)]] | alt | 5.28 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.99× (z +8.6) | — |
| [[COLO 205 (line)]] | alt | 7.85 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -9.0) ⚠ cell-cycle shift, explains ~59% of this change |
| [[H4 (line)]] | wt | 10.5 | 1 | 0 | [[Triamcinolone (drug)]] 5 µM 9.27× (z +8.8) | — |
| [[HEC-1-A (line)]] | alt | 4.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.170× (z -8.8) |
| [[J82 (line)]] | alt | 6.89 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.110× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 17.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0779× (z -12.4) |
| [[PANC-1 (line)]] | alt | 3.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.79× (z +9.5) | — |
| [[A-172 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13903), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00607]] | +0.74 | +0.64 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[TBXAS1]] | +0.73 | +0.64 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[ITGA10]] | +0.67 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[B3GNT5]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[ADGRG2]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[SVEP1]] | +0.63 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[ADPRHL1]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[PTPRG]] | +0.62 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ADAMTS9]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[RIPOR2]] | +0.61 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[TOP1]] | +0.60 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[IL18R1]] | +0.60 | +0.44 / +0.65 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAFAH1B3]] | -0.51 | -0.42 / -0.24 | both halves | 4e-04 |  |
| [[PER3]] | -0.51 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[ARRB2]] | -0.50 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[RAB3A]] | -0.50 | -0.32 / -0.29 | both halves | 2e-04 |  |
| [[EML1]] | -0.49 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[CDON]] | -0.49 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[PIM1]] | -0.49 | -0.52 / -0.28 | both halves | 3e-04 |  |
| [[CYRIA]] | -0.48 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[WDFY1]] | -0.48 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[WNT7B]] | -0.48 | -0.56 / -0.30 | both halves | 2e-04 |  |
| [[GPRC5B]] | -0.48 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[FAM102A]] | -0.48 | -0.52 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNER]] | B | DNER activity raises STXBP5-AS1's level | lines that do not express DNER (32) vs lines expressing it (18) | 2.64× lower at baseline in the lines without DNER | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000222032, APCDD1L, GYPC |
| [[TOP2A]] | B | TOP2A activity lowers STXBP5-AS1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.2% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[VSTM2L]] | B | VSTM2L activity lowers STXBP5-AS1's level | lines that do not express VSTM2L (20) vs lines expressing it (30) | 1.27× higher at baseline in the lines without VSTM2L | 0.062 | ⚠ within organs, on part of the lines; also absent: ZNF829, PKD2L2-DT, ZNF625; maybe low, not absent |
| [[DNER]] | B | DNER activity strengthens STXBP5-AS1's drug response | lines that do not express DNER (28) vs lines expressing it (16) | the lines without DNER respond 0.70× as strongly (z diff +1.04); rises at some drug-doses, falls at others (34% from rises): Panobinostat 5 µM: 0.43x vs 0.23x (z diff +2.7); Belinostat 5 µM: 0.43x vs 0.24x (z diff +2.3); Clobetasol propionate 0.5 µM: 1.61x vs 4.40x (z diff +1.9) | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000222032, APCDD1L, GYPC; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[NR3C1]] | B | NR3C1 activity raises STXBP5-AS1's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 6.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.4, 15.3); signed map (17.5, 33.0). **Vector** length 104, 25.4% of its response variance represented; |z| ≥ 3 in 1,280 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.8 | +17.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.6 | +12.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.9 | +3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +8.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +6.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.8 | +6.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +5.0 | +6.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +4.9 | +5.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.3 | -10.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.7 | -9.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.5 | -11.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -2.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.3 | -4.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -0.8 |
|  | [[Hexylresorcinol (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.5 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | STXBP5 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6q24.3 — chr6:146,824,539-147,204,614 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44183](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44183) · Entrez [729178](https://www.ncbi.nlm.nih.gov/gene/729178) · Ensembl [ENSG00000233452](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233452)

## Data

Gene col 13903: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13903); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13903, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13903]; `tensor/DDL_lfc|DDL_z.npy` [13903]; `embed/gene_vectors.npy` [13903]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13903 or target_col == 13903). Every well: [[STXBP5-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STXBP5-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
