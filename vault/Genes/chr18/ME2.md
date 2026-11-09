---
symbol: "ME2"
type: "gene"
col: 1340
ensembl_id: "ENSG00000082212"
name: "malic enzyme 2"
location: "18q21.2"
module: 18
arm: "+"
pooled_cpm: 45.63
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# ME2

*malic enzyme 2* — 18q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.28× (z +19.9, q 0e+00, up in 35 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 1.51× (z +9.9, q 5e-21, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.554× (z -7.9, q 2e-12, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAE1]] (+0.69, fdr 7e-06), [[USP45]] (+0.69, fdr 7e-06), [[PAQR3]] (+0.63, fdr 7e-06); moves opposite to [[CFAP20]] (-0.57, fdr 6e-05), [[TBCC]] (-0.57, fdr 6e-05), [[METTL25B]] (-0.55, fdr 6e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MFAP3L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 18 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1340.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.28×** | +19.9 | 0e+00 | 35/43 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +19.7 | 0e+00 | 34/39 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.63×** | +11.5 | 3e-28 | 30/42 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +9.9 | 5e-21 | 34/46 (MIA PaCa-2, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +9.7 | 4e-20 | 35/45 (HEC-1-A, HT-29, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +9.0 | 2e-17 | 28/46 (MIA PaCa-2, A498, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +8.9 | 4e-17 | 33/45 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +8.2 | 2e-14 | 29/46 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.71×** | +7.1 | 7e-11 | 27/41 (SK-MEL-2, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +7.0 | 1e-10 | 30/46 (HEC-1-A, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +6.7 | 9e-10 | 20/46 (NCI-H2347, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.21×** | +4.6 | 2e-04 | 16/45 (A498, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.20× | +4.5 | 3e-04 | 18/45 (MIA PaCa-2, H4, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 1.19× | +4.4 | 4e-04 | 18/46 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.20× | +4.4 | 5e-04 | 19/46 (SNU-1, MIA PaCa-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 1e-03 | 15/46 (MIA PaCa-2, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.001 | 13/45 (NCI-H1792, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.001 | 15/46 (NCI-H460, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.9 | 0.002 | 12/46 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.002 | 10/46 (NCI-H2347, C32, …) | rises with dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.9 | 0.002 | 10/45 (LOX-IMVI, LoVo, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.16× | +3.6 | 0.006 | 10/46 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.10× | +3.4 | 0.015 | 2/46 (A549, SW 900) | top dose only |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.017 | 8/46 (A498, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.037 | 7/45 (PANC-1, SNU-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1340.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.554×** | -7.9 | 2e-12 | 27/47 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.582×** | -7.2 | 2e-10 | 26/46 (NCI-H1573, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -6.3 | 7e-08 | 0/46 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.795×** | -5.6 | 3e-06 | 24/46 (NCI-H460, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1340. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 99.4 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.16× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 50.1 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.76× (z +16.7) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 0.5 µM 0.489× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.499× (z -8.7) |
| [[A498 (line)]] | wt | 35.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.01× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.25× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 95.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +14.4) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 27.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +12.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 69.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.31× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 46.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.98× (z +13.8) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 50.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +10.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 54.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +12.6) ⚠ toxic; transcription drop | [[TAK-901 (drug)]] 5 µM 0.151× (z -12.5) |
| [[LS 180 (line)]] | wt | 56.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.72× (z +13.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 33.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 48.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.79× (z +12.4) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 44.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 15.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.49× (z +9.8) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 32.4 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.235× (z -8.9) |
| [[KATO III (line)]] | alt | 42.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +10.4) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 56.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 46.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +8.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 54.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.606× (z -9.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SHP-77 (line)]] | alt | 64.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +9.2) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 145 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 97.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 61.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 71.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1340), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAE1]] | +0.69 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[USP45]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[PAQR3]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[WWP1]] | +0.62 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[FAM20B]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[USP46]] | +0.60 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[CMTM4]] | +0.58 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[NAPB]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[IDE]] | +0.57 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[SORD]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[TNPO1]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[VPS36]] | +0.57 | +0.45 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP20]] | -0.57 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[TBCC]] | -0.57 | -0.39 / -0.61 | both halves | 6e-05 |  |
| [[METTL25B]] | -0.55 | -0.38 / -0.61 | both halves | 6e-05 |  |
| [[ZNF324]] | -0.54 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[RSPRY1]] | -0.54 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[TOGARAM1]] | -0.53 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[KLF10]] | -0.53 | -0.39 / -0.60 | both halves | 5e-05 |  |
| [[C6orf47]] | -0.53 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[FBXO48]] | -0.53 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[KDM5A]] | -0.53 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[HES1]] | -0.52 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[GPANK1]] | -0.52 | -0.39 / -0.59 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MFAP3L]] | B | MFAP3L activity raises ME2's level | lines that do not express MFAP3L (9) vs lines expressing it (41) | 1.89× lower at baseline in the lines without MFAP3L | 0.040 | ⚠ within organs, on part of the lines; also absent: CRACD, FILIP1, TSPAN33; maybe low, not absent |
| [[ADCY3]] | B | ADCY3 activity raises ME2's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.43× lower at baseline in the lines without ADCY3 | 0.067 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-6.0, -34.0); signed map (-11.2, -41.7). **Vector** length 91.3, 19.7% of its response variance represented; |z| ≥ 3 in 875 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +5.8 | +9.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.3 | +9.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +8.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.0 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +9.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.6 | +4.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.3 | +1.7 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -7.0 | -7.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.4 | -7.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | -1.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.6 | -6.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -0.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | malic enzyme 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.2 — chr18:50,879,080-50,954,257 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Malic enzyme family |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 3 pathways, smallest: Pyruvate metabolism; Mitochondrial protein degradation; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P23368](https://www.uniprot.org/uniprotkb/P23368) (NAD-dependent malic enzyme, mitochondrial):

> NAD-dependent mitochondrial malic enzyme that catalyzes the oxidative decarboxylation of malate to pyruvate.

**Summary**, from NCBI Gene [4200](https://www.ncbi.nlm.nih.gov/gene/4200):

> This gene encodes a mitochondrial NAD-dependent malic enzyme, a homotetrameric protein, that catalyzes the oxidative decarboxylation of malate to pyruvate. It had previously been weakly linked to a syndrome known as Friedreich ataxia that has since been shown to be the result of mutation in a completely different gene. Certain single-nucleotide polymorphism haplotypes of this gene have been shown to increase the risk for idiopathic generalized epilepsy. Alternatively spliced transcript variants …

**Accessions** — [HGNC:6984](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6984) · Entrez [4200](https://www.ncbi.nlm.nih.gov/gene/4200) · UniProt [P23368](https://www.uniprot.org/uniprotkb/P23368) · Ensembl [ENSG00000082212](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082212)

## Data

Gene col 1340: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1340); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1340, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1340]; `tensor/DDL_lfc|DDL_z.npy` [1340]; `embed/gene_vectors.npy` [1340]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1340 or target_col == 1340). Every well: [[ME2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ME2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
