---
symbol: "DPYD"
type: "gene"
col: 12034
ensembl_id: "ENSG00000188641"
name: "dihydropyrimidine dehydrogenase"
location: "1p21.3"
module: 167
arm: "+"
pooled_cpm: 210.47
n_lines_expressing: 38
n_dd_up: 18
n_dd_down: 41
n_dd_up_clean: 18
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/167"]
generated_by: "tahoemap"
---

# DPYD

*dihydropyrimidine dehydrogenase* — 1p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.50× (z +6.8, q 4e-09, up in 28 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (11 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.476× (z -8.9, q 4e-16, down in 36 of 36 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.485× (z -8.7, q 1e-15, down in 32 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC16A7]] (+0.63, fdr 1e-05), [[MBNL1]] (+0.62, fdr 1e-05), [[CFH]] (+0.61, fdr 7e-06); moves opposite to [[RABGEF1P3]] (-0.48, fdr 4e-05), [[ADCY7]] (-0.47, fdr 9e-05), [[KBTBD11-OT1-1]] (-0.46, fdr 7e-05).
> It is in [[Module 167]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, none with an alert; shown: the 15 strongest. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12034.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +6.8 | 4e-09 | 28/36 (BT-474, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.66×** | +5.6 | 8e-06 | 27/36 (J82, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.58×** | +5.3 | 3e-05 | 26/35 (NCI-H2347, AsPC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +4.8 | 2e-04 | 21/36 (NCI-H2030, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +4.5 | 6e-04 | 23/37 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.84×** | +3.8 | 0.013 | 23/38 (NCI-H2347, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.019 | 19/36 (NCI-H2030, J82, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.39×** | +3.6 | 0.019 | 20/36 (HOP62, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.019 | 20/36 (A549, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.022 | 21/38 (NCI-H2347, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.022 | 21/36 (NCI-H2347, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.40×** | +3.5 | 0.025 | 22/35 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.033 | 21/36 (NCI-H2347, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.34×** | +3.3 | 0.046 | 22/36 (CFPAC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.065 | 18/36 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12034.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.476×** | -8.9 | 4e-16 | 36/36 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.485×** | -8.7 | 1e-15 | 32/36 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.498×** | -8.0 | 2e-13 | 32/35 (SNU-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.560×** | -6.9 | 6e-10 | 29/36 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.564×** | -6.8 | 8e-10 | 27/36 (HT-29, SNU-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.679×** | -6.5 | 5e-09 | 26/36 (BT-474, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.583×** | -6.5 | 9e-09 | 32/36 (RPMI-7951, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.693×** | -6.2 | 4e-08 | 25/37 (Panc 03.27, BT-474, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.581×** | -6.2 | 5e-08 | 30/36 (SNU-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.377×** | -6.1 | 6e-08 | 31/37 (A498, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.599×** | -5.3 | 6e-06 | 23/37 (NCI-H1792, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.649×** | -5.0 | 3e-05 | 22/35 (BT-474, Panc 03.27, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.452×** | -5.0 | 3e-05 | 33/36 (NCI-H1792, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.461×** | -4.8 | 5e-05 | 27/36 (NCI-H1792, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.463×** | -4.8 | 5e-05 | 32/36 (NCI-H1792, A498, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.463×** | -4.8 | 5e-05 | 30/36 (NCI-H1792, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.670×** | -4.8 | 6e-05 | 25/36 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.496×** | -4.4 | 3e-04 | 21/36 (SNU-1, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.664×** | -4.3 | 6e-04 | 24/35 (BT-474, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12034. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 148 | 1 | 16 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.12× (z +11.3) | [[Selinexor (drug)]] 5 µM 0.165× (z -18.1) |
| [[NCI-H1792 (line)]] | alt | 858 | 0 | 12 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -21.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.145× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 279 | 0 | 12 (6 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.233× (z -13.0) |
| [[SNU-1 (line)]] | wt | 539 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0996× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.285× (z -11.9) |
| [[A498 (line)]] | wt | 218 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.341× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.152× (z -10.4) |
| [[HT-29 (line)]] | alt | 169 | 0 | 6 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.250× (z -12.6) |
| [[A-427 (line)]] | wt | 803 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.336× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 71.0 | 4 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.27× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 256 | 0 | 4 | — | [[Auranofin (drug)]] 5 µM 0.266× (z -10.7) |
| [[A-172 (line)]] | wt | 136 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.74× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 902 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.275× (z -9.5) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.298× (z -9.2) |
| [[LoVo (line)]] | wt | 74.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +14.0) ⚠ cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.353× (z -9.1) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 466 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.269× (z -12.2) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 67.3 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.275× (z -13.3) |
| [[NCI-H2030 (line)]] | alt | 100 | 2 | 0 | [[Belinostat (drug)]] 5 µM 3.22× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 75.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.315× (z -9.0) |
| [[C32 (line)]] | wt | 329 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.292× (z -9.3) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 316 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.388× (z -10.3) |
| [[HCT15 (line)]] | alt | 98.6 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.322× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 53.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.41× (z +10.3) | — |
| [[HOP62 (line)]] | alt | 115 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HS-578T (line)]] | alt | 684 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 301 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.61× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 257 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.386× (z -8.7) ⚠ transcription drop |
| [[SW 900 (line)]] | alt | 233 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.242× (z -11.9) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 132 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 21.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.6 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 183 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.7 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 315 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.0 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 14.9 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 568 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 51.5 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 327 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 48.6 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 15.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 576 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 395 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 17.8 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 19.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12034), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC16A7]] | +0.63 | +0.53 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[MBNL1]] | +0.62 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[CFH]] | +0.61 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ARHGAP24]] | +0.56 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[ARID5B]] | +0.55 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[CD38]] | +0.54 | +0.43 / +0.57 | both halves | 3e-05 | pathway: HALLMARK_APOPTOSIS |
| [[SAA2-SAA4]] | +0.53 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[PLD1]] | +0.53 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[IGFBP4]] | +0.53 | +0.37 / +0.52 | both halves | 8e-05 |  |
| [[SAA2]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[BICC1]] | +0.52 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[ARHGEF12]] | +0.52 | +0.56 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABGEF1P3]] | -0.48 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[ADCY7]] | -0.47 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[KBTBD11-OT1-1]] | -0.46 | -0.39 / -0.37 | both halves | 7e-05 |  |
| [[ANO10]] | -0.46 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[PLEKHG5]] | -0.46 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[FAM131A]] | -0.45 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[DEF6]] | -0.45 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[DGCR5]] | -0.44 | -0.29 / -0.48 | both halves | 2e-04 |  |
| [[SLC15A4]] | -0.44 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[PARL]] | -0.44 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[ZNF74]] | -0.44 | -0.48 / -0.25 | both halves | 4e-04 |  |
| [[ZDHHC6]] | -0.44 | -0.45 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers DPYD's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[CYP1B1]] | B | CYP1B1 activity strengthens DPYD's drug response | lines that do not express CYP1B1 (19) vs lines expressing it (18) | the lines without CYP1B1 respond 0.79× as strongly (z diff +1.21); strongest at Bortezomib 0.05 µM: 0.68x vs 0.46x (z diff +2.9) | 0.063 | ⚠ within organs, on part of the lines; also absent: EFEMP1, CCL2, ENSG00000282849; target measured in part of the lines; artifact flags |
| [[CYP1B1]] | B | CYP1B1 activity raises DPYD's level | lines that do not express CYP1B1 (29) vs lines expressing it (21) | 2.67× lower at baseline in the lines without CYP1B1 | 0.097 | ⚠ within organs, on part of the lines; also absent: EFEMP1, CCL2, ENSG00000282849 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 167]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.660). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.4, 20.0); signed map (48.9, 25.5). **Vector** length 127, 42.7% of its response variance represented; |z| ≥ 3 in 1,588 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +9.5 | +3.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.8 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.6 | +1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.7 | +0.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +6.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.6 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +5.3 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | +2.7 | +2.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.1 | -6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.3 | -8.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.0 | -8.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.0 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.6 | -8.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.2 | -6.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.0 | -3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.9 | -4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.9 | -4.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.8 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | dihydropyrimidine dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.3 — chr1:97,077,743-97,995,000 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DPD, DHPDHase |
| Gene groups (HGNC) | Flavoproteins; Oxidoreductases |
| Hallmark sets | APOPTOSIS |
| Reactome | 3 pathways, smallest: Pyrimidine catabolism; Nucleotide catabolism; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12882](https://www.uniprot.org/uniprotkb/Q12882) (Dihydropyrimidine dehydrogenase):

> Catalyzes the reduction of uracil and thymine in the initial step of reductive pyrimidine catabolism, a pathway that yields beta-alanine from uracil and beta-aminoisobutyrate from thymine. Also capable of degrading the chemotherapeutic drug 5-fluorouracil.

**Summary**, from NCBI Gene [1806](https://www.ncbi.nlm.nih.gov/gene/1806):

> The protein encoded by this gene is a pyrimidine catabolic enzyme and the initial and rate-limiting factor in the pathway of uracil and thymidine catabolism. Mutations in this gene result in dihydropyrimidine dehydrogenase deficiency, an error in pyrimidine metabolism associated with thymine-uraciluria and an increased risk of toxicity in cancer patients receiving 5-fluorouracil chemotherapy. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, …

**Accessions** — [HGNC:3012](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3012) · Entrez [1806](https://www.ncbi.nlm.nih.gov/gene/1806) · UniProt [Q12882](https://www.uniprot.org/uniprotkb/Q12882) · Ensembl [ENSG00000188641](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188641)

## Data

Gene col 12034: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12034); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12034, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12034]; `tensor/DDL_lfc|DDL_z.npy` [12034]; `embed/gene_vectors.npy` [12034]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12034 or target_col == 12034). Every well: [[DPYD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPYD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
