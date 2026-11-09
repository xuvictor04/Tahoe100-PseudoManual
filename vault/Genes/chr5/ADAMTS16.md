---
symbol: "ADAMTS16"
type: "gene"
col: 7002
ensembl_id: "ENSG00000145536"
name: "ADAM metallopeptidase with thrombospondin type 1 motif 16"
location: "5p15.32"
module: 13
arm: "+"
pooled_cpm: 47.13
n_lines_expressing: 25
n_dd_up: 28
n_dd_down: 32
n_dd_up_clean: 22
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 38
direction_downstream: 27
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# ADAMTS16

*ADAM metallopeptidase with thrombospondin type 1 motif 16* — 5p15.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.74× (z +13.2, q 3e-37, up in 15 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.580× (z -12.9, q 2e-35, down in 21 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01411]] (+0.75, fdr 7e-06), [[KIRREL3]] (+0.67, fdr 7e-06), [[INSYN2B]] (+0.65, fdr 7e-06); moves opposite to [[CCND3]] (-0.64, fdr 7e-06), [[FOXG1]] (-0.62, fdr 6e-05), [[YAP1]] (-0.60, fdr 1e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 38 arrows point to it, the strongest [[NAV3]] → it (grade B ⚠); 27 go from it, the strongest it → [[HRH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7002.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +13.2 | 3e-37 | 15/23 (SW1417, LOX-IMVI, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.93×** | +11.1 | 5e-26 | 12/23 (NCI-H2347, SW 900, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.64×** | +8.3 | 2e-14 | 20/23 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +6.8 | 1e-09 | 9/23 (PANC-1, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +6.7 | 3e-09 | 14/23 (AsPC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +6.4 | 1e-08 | 12/23 (LOX-IMVI, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.31×** | +6.4 | 1e-08 | 11/23 (PANC-1, A498, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.46×** | +6.3 | 2e-08 | 15/23 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.41×** | +5.5 | 2e-06 | 11/22 (PANC-1, A498, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.37×** | +5.3 | 6e-06 | 6/23 (PANC-1, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.23×** | +5.0 | 4e-05 | 8/23 (CFPAC-1, AsPC-1, …) | two highest doses | composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.33×** | +4.8 | 8e-05 | 10/22 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.32×** | +4.6 | 2e-04 | 8/22 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.67×** | +4.5 | 3e-04 | 15/23 (PANC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.66×** | +4.5 | 3e-04 | 14/24 (HOP62, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.41×** | +4.1 | 0.001 | 1/23 (PANC-1) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.58×** | +4.0 | 0.002 | 8/23 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.51×** | +3.6 | 0.009 | 5/23 (PANC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +3.6 | 0.009 | 11/23 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 5 with an alert ⚠; shown: the 15 strongest. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7002.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.580×** | -12.9 | 2e-35 | 21/23 (J82, HOP62, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.597×** | -12.2 | 6e-32 | 23/23 (hTERT-HPNE, A498, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.548×** | -9.7 | 6e-20 | 19/23 (hTERT-HPNE, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.571×** | -9.4 | 8e-19 | 19/23 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.572×** | -9.4 | 8e-19 | 18/23 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.679×** | -9.2 | 4e-18 | 18/23 (Hs 766T, HOP62, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.579×** | -9.2 | 4e-18 | 17/23 (HOP62, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.590×** | -8.9 | 6e-17 | 16/23 (HOP62, Hs 766T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.597×** | -8.7 | 3e-16 | 18/23 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.581×** | -8.4 | 2e-15 | 17/22 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.622×** | -8.0 | 8e-14 | 19/23 (Hs 766T, HOP62, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.631×** | -7.7 | 5e-13 | 15/23 (Hs 766T, HOP62, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.620×** | -7.7 | 6e-13 | 19/23 (HOP62, Hs 766T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.633×** | -7.7 | 7e-13 | 19/23 (HOP62, Hs 766T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.658×** | -7.0 | 7e-11 | 18/23 (Hs 766T, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7002. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 581 | 0 | 26 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0589× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -15.4) |
| [[HOP62 (line)]] | alt | 145 | 0 | 24 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.152× (z -13.4) |
| [[hTERT-HPNE (line)]] | wt | 355 | 0 | 13 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0986× (z -23.5) |
| [[NCI-H1792 (line)]] | alt | 172 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -15.9) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -14.2) |
| [[CFPAC-1 (line)]] | alt | 79.9 | 1 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +12.9) ⚠ cell-cycle shift, explains ~12% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 18.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -14.1) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0901× (z -13.4) |
| [[PANC-1 (line)]] | alt | 25.8 | 1 (1 ⚠) | 5 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.71× (z +10.6) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -12.2) |
| [[J82 (line)]] | alt | 92.8 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -16.3) |
| [[A498 (line)]] | wt | 95.7 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -19.2) |
| [[LOX-IMVI (line)]] | wt | 39.5 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 2.58× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 18.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +11.7) ⚠ cell-cycle shift, explains ~12% of this change | — |
| [[H4 (line)]] | wt | 51.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 13.2 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.228× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 20.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.85× (z +9.2) | — |
| [[SW 900 (line)]] | alt | 50.7 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 4.05× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -10.6) |
| [[A-172 (line)]] | wt | 30.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -13.4) |
| [[A549 (line)]] | wt | 20.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 110 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 36.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 23.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -9.6) |
| [[SNU-423 (line)]] | alt | 26.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +11.6) ⚠ cell-cycle shift, explains ~12% of this change | — |
| [[SW1417 (line)]] | alt | 17.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.55× (z +12.3) | — |
| [[A-427 (line)]] | wt | 7.94 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.63 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.93 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.49 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.94 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.73 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.38 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.24 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.07 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.95 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 7.62 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.16 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 11.4 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.80 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.82 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.78 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.91 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.38 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7002), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01411]] | +0.75 | +0.69 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[KIRREL3]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[INSYN2B]] | +0.65 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[AFF3]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[NGF]] | +0.64 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[SMS]] | +0.61 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[MEG3]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[MEG8]] | +0.61 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[ADAMTS6]] | +0.61 | +0.57 / +0.58 | both halves | 1e-05 | same gene group; pathway: Defective B3GALTL causes PpS |
| [[SLC8A1]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[CREB5]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[SPOCD1]] | +0.60 | +0.49 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCND3]] | -0.64 | -0.70 / -0.62 | both halves | 7e-06 | **novel candidate** |
| [[FOXG1]] | -0.62 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[YAP1]] | -0.60 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[KLF9]] | -0.58 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[FOXC2]] | -0.57 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[ITGA10]] | -0.55 | -0.50 / -0.57 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[SRGN]] | -0.54 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[TMEM164]] | -0.53 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[RIPOR2]] | -0.52 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[COPS8]] | -0.52 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[UBE2E1]] | -0.52 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[UGP2]] | -0.51 | -0.49 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 6, C 32. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NAV3]] | B | NAV3 activity raises ADAMTS16's level | lines that do not express NAV3 (16) vs lines expressing it (34) | 3.07× lower at baseline in the lines without NAV3 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, PRR16, ADAM12 |
| [[APCDD1L-DT]] | B | APCDD1L-DT activity raises ADAMTS16's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 2.62× lower at baseline in the lines without APCDD1L-DT | 0.042 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[BMPER]] | B | BMPER activity raises ADAMTS16's level | lines that do not express BMPER (21) vs lines expressing it (29) | 2.84× lower at baseline in the lines without BMPER | 0.052 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[NR3C1]] | B | NR3C1 activity lowers ADAMTS16's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[ADAMTS6]] | B | ADAMTS6 activity raises ADAMTS16's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 2.80× lower at baseline in the lines without ADAMTS6 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2 |
| [[HRH1]] | B | HRH1 activity raises ADAMTS16's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 4.22× lower at baseline in the lines without HRH1 | 0.084 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[ADAMTS12]] | C | ADAMTS12 activity raises ADAMTS16's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 6.23× lower at baseline in the lines without ADAMTS12 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1; co-absent with the target |
| [[FRMD4A]] | C | FRMD4A activity raises ADAMTS16's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 4.87× lower at baseline in the lines without FRMD4A | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |
| [[PTHLH]] | C | PTHLH activity raises ADAMTS16's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 4.67× lower at baseline in the lines without PTHLH | 0.005 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1; co-absent with the target |
| [[SPOCD1]] | C | SPOCD1 activity raises ADAMTS16's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 5.58× lower at baseline in the lines without SPOCD1 | 0.006 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises ADAMTS16's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 6.16× lower at baseline in the lines without COL5A1 | 0.007 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[C5orf46]] | C | C5orf46 activity raises ADAMTS16's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 4.17× lower at baseline in the lines without C5orf46 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 10, C 17. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HRH1]] | B | ADAMTS16 activity raises HRH1's level | lines that do not express ADAMTS16 (25) vs lines expressing it (25) | 3.14× lower at baseline in the lines without ADAMTS16 | 0.009 | ⚠ within organs, on part of the lines; also absent: PLAU, ADAMTS12, GBP5 |
| [[ARL4C]] | B | ADAMTS16 activity raises ARL4C's level | lines that do not express ADAMTS16 (25) vs lines expressing it (25) | 3.38× lower at baseline in the lines without ADAMTS16 | 0.013 | ⚠ within organs, on part of the lines; also absent: PLAU, ADAMTS12, GBP5 |
| [[MYO10]] | B | ADAMTS16 activity raises MYO10's level | lines that do not express ADAMTS16 (25) vs lines expressing it (25) | 2.12× lower at baseline in the lines without ADAMTS16 | 0.022 | ⚠ within organs, on part of the lines; also absent: PLAU, ADAMTS12, GBP5 |
| [[UBE2E1]] | B | ADAMTS16 activity raises UBE2E1's level | lines that do not express ADAMTS16 (25) vs lines expressing it (25) | 1.26× lower at baseline in the lines without ADAMTS16 | 0.035 | ⚠ within organs, on part of the lines; also absent: PLAU, ADAMTS12, GBP5 |
| [[EXT1]] | B | ADAMTS16 activity raises EXT1's level | lines that do not express ADAMTS16 (25) vs lines expressing it (25) | 1.54× lower at baseline in the lines without ADAMTS16 | 0.039 | ⚠ within organs, on part of the lines; also absent: PLAU, ADAMTS12, GBP5 |
| [[TRIO]] | B | ADAMTS16 activity raises TRIO's level | lines that do not express ADAMTS16 (25) vs lines expressing it (25) | 1.89× lower at baseline in the lines without ADAMTS16 | 0.049 | ⚠ within organs, on part of the lines; also absent: PLAU, ADAMTS12, GBP5 |
| [[SYNJ2]] | B | ADAMTS16 activity raises SYNJ2's level | lines that do not express ADAMTS16 (25) vs lines expressing it (25) | 1.82× lower at baseline in the lines without ADAMTS16 | 0.050 | ⚠ within organs, on part of the lines; also absent: PLAU, ADAMTS12, GBP5 |
| [[DLG1]] | B | ADAMTS16 activity raises DLG1's level | lines that do not express ADAMTS16 (25) vs lines expressing it (25) | 1.36× lower at baseline in the lines without ADAMTS16 | 0.073 | ⚠ within organs, on part of the lines; also absent: PLAU, ADAMTS12, GBP5 |
| [[NRIP3]] | B | ADAMTS16 activity raises NRIP3's level | lines that do not express ADAMTS16 (25) vs lines expressing it (25) | 2.27× lower at baseline in the lines without ADAMTS16 | 0.093 | ⚠ within organs, on part of the lines; also absent: PLAU, ADAMTS12, GBP5 |
| [[NHS]] | B | ADAMTS16 activity raises NHS's level | lines that do not express ADAMTS16 (25) vs lines expressing it (25) | 2.73× lower at baseline in the lines without ADAMTS16 | 0.094 | ⚠ within organs, on part of the lines; also absent: PLAU, ADAMTS12, GBP5 |
| [[PTHLH]] | C | ADAMTS16 activity raises PTHLH's level | lines that do not express ADAMTS16 (25) vs lines expressing it (25) | 3.18× lower at baseline in the lines without ADAMTS16 | 0.002 | ⚠ within organs, on part of the lines; also absent: PLAU, ADAMTS12, GBP5; co-absent with the target |
| [[SPOCD1]] | C | ADAMTS16 activity raises SPOCD1's level | lines that do not express ADAMTS16 (25) vs lines expressing it (25) | 4.96× lower at baseline in the lines without ADAMTS16 | 0.005 | ⚠ within organs, on part of the lines; also absent: PLAU, ADAMTS12, GBP5; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.608). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.0, 16.7); signed map (22.6, 49.3). **Vector** length 110, 35.0% of its response variance represented; |z| ≥ 3 in 986 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +13.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +6.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.1 | +3.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.1 | +8.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +6.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +5.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.3 | +4.5 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -5.4 | -9.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.9 | -8.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.9 | -7.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -4.8 | -9.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.8 | -9.4 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase with thrombospondin type 1 motif 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.32 — chr5:5,140,330-5,320,304 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ADAMTS16s |
| Gene groups (HGNC) | ADAM metallopeptidases with thrombospondin type 1 motif |
| Reactome | 8 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

UniProt [Q8TE57](https://www.uniprot.org/uniprotkb/Q8TE57) carries no function annotation.

**Summary**, from NCBI Gene [170690](https://www.ncbi.nlm.nih.gov/gene/170690):

> This gene encodes a member of the ADAMTS (a disintegrin and metalloproteinase with thrombospondin motifs) protein family. ADAMTS family members share several distinct protein modules, including a propeptide region, a metalloproteinase domain, a disintegrin-like domain, and a thrombospondin type 1 (TS) motif. Individual members of this family differ in the number of C-terminal TS motifs, and some have unique C-terminal domains. The encoded preproprotein is proteolytically processed to generate …

**Accessions** — [HGNC:17108](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17108) · Entrez [170690](https://www.ncbi.nlm.nih.gov/gene/170690) · UniProt [Q8TE57](https://www.uniprot.org/uniprotkb/Q8TE57) · Ensembl [ENSG00000145536](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145536)

## Data

Gene col 7002: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7002); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7002, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7002]; `tensor/DDL_lfc|DDL_z.npy` [7002]; `embed/gene_vectors.npy` [7002]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7002 or target_col == 7002). Every well: [[ADAMTS16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAMTS16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
