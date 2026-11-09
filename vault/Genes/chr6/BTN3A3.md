---
symbol: "BTN3A3"
type: "gene"
col: 3284
ensembl_id: "ENSG00000111801"
name: "butyrophilin subfamily 3 member A3"
location: "6p22.2"
module: 32
arm: "+"
pooled_cpm: 9.31
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 30
n_dd_up_clean: 12
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# BTN3A3

*butyrophilin subfamily 3 member A3* — 6p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.74× (z +6.6, q 2e-08, up in 24 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.400× (z -11.5, q 9e-28, down in 35 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BTN3A1]] (+0.74, fdr 7e-06, ⚠ same locus), [[ERAP2]] (+0.70, fdr 7e-06), [[BTN3A2]] (+0.68, fdr 7e-06), [[RBM43]] (+0.67, fdr 1e-05); moves opposite to [[PACS2]] (-0.62, fdr 1e-05), [[MICAL2]] (-0.60, fdr 3e-05), [[TBC1D16]] (-0.59, fdr 4e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3284.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.74×** | +6.6 | 2e-08 | 24/42 (NCI-H2347, CFPAC-1, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +5.3 | 3e-05 | 19/45 (NCI-H2347, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.37×** | +4.9 | 2e-04 | 16/45 (CFPAC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.45×** | +4.6 | 5e-04 | 14/44 (Hs 766T, SNU-423, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.41×** | +4.5 | 9e-04 | 14/46 (MIA PaCa-2, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.37×** | +4.3 | 0.001 | 10/46 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.27×** | +4.1 | 0.003 | 11/45 (NCI-H2347, Hs 766T, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.39×** | +3.8 | 0.009 | 12/45 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.010 | 13/44 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.036 | 10/44 (SNU-423, LOX-IMVI, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.20×** | +3.2 | 0.081 | 11/45 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.081 | 8/45 (CFPAC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ferulic acid (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.084 | 3/43 (H4, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.29× | +3.0 | 0.10 | 8/41 (NCI-H1573, H4, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3284.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.400×** | -11.5 | 9e-28 | 35/45 (Panc 03.27, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.417×** | -11.0 | 1e-25 | 34/46 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.442×** | -10.2 | 3e-22 | 33/44 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.517×** | -8.3 | 2e-14 | 24/40 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.581×** | -6.8 | 1e-09 | 21/30 (MIA PaCa-2, SNU-423, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.358×** | -6.7 | 2e-09 | 25/41 (Panc 03.27, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.600×** | -6.4 | 1e-08 | 27/46 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.708×** | -6.2 | 5e-08 | 21/45 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.623×** | -5.9 | 2e-07 | 23/44 (KATO III, Hs 766T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.632×** | -5.8 | 4e-07 | 20/42 (RPMI-7951, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.625×** | -5.7 | 7e-07 | 20/35 (SNU-423, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.663×** | -5.2 | 1e-05 | 18/46 (RPMI-7951, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **0.751×** | -5.1 | 1e-05 | 20/42 (COLO 205, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.667×** | -5.1 | 1e-05 | 19/43 (H4, NCI-H460, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.466×** | -5.0 | 2e-05 | 19/41 (C32, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.661×** | -5.0 | 2e-05 | 18/44 (CFPAC-1, HS-578T, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.701×** | -4.5 | 3e-04 | 18/40 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.728×** | -3.8 | 0.003 | 17/43 (LoVo, C-33 A, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.563×** | -3.8 | 0.004 | 12/40 (KATO III, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.744×** | -3.7 | 0.005 | 12/45 (H4, SNU-423, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.749×** | -3.6 | 0.007 | 9/46 (LoVo, COLO 205, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.763×** | -3.4 | 0.015 | 15/42 (LOX-IMVI, A-172, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3284. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 23.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.155× (z -9.9) |
| [[SNU-423 (line)]] | alt | 25.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -15.5) ⚠ cell-cycle shift, explains ~99% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.233× (z -9.6) |
| [[HS-578T (line)]] | alt | 17.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0625× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.133× (z -10.9) |
| [[LoVo (line)]] | wt | 15.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -9.1) ⚠ cell-cycle shift, explains ~99% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.286× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 15.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -12.2) ⚠ cell-cycle shift, explains ~99% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.113× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 17.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.193× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[Hs 766T (line)]] | wt | 19.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 9.34 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0793× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[NCI-H1573 (line)]] | alt | 4.55 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0365× (z -13.4) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 16.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -13.7) ⚠ cell-cycle shift, explains ~99% of this change |
| [[A549 (line)]] | wt | 6.12 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0712× (z -10.7) |
| [[C32 (line)]] | wt | 7.35 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0965× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[COLO 205 (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -16.1) ⚠ cell-cycle shift, explains ~99% of this change |
| [[LOX-IMVI (line)]] | wt | 4.41 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0740× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 7.32 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.127× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 6.90 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0781× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 7.00 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0943× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.143× (z -9.6) |
| [[PANC-1 (line)]] | alt | 3.57 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[SW480 (line)]] | alt | 5.86 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A-427 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3284), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN3A1]] | +0.74 | +0.65 / +0.86 | both halves | 7e-06 | same gene group; pathway: Butyrophilin (BTN) family interactions; STRING 966; ⚠ same locus (25.3 kb, same strand: neighbours can correlate without regulation) |
| [[ERAP2]] | +0.70 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[BTN3A2]] | +0.68 | +0.75 / +0.73 | both halves | 7e-06 | same gene group; pathway: Butyrophilin (BTN) family interactions; STRING 960 |
| [[RBM43]] | +0.67 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[CASP7]] | +0.66 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[TLR3]] | +0.65 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[APOL3]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 | STRING 436 |
| [[LINC02100]] | +0.64 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[MOV10]] | +0.62 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[UBA7]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[APOBEC3F]] | +0.61 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[NMI]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[GBP4]] | +0.60 | +0.56 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACS2]] | -0.62 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[MICAL2]] | -0.60 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[TBC1D16]] | -0.59 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[RSU1]] | -0.59 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[KLF13]] | -0.59 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[BCAR3]] | -0.56 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[ABCA3]] | -0.55 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[SEPTIN10]] | -0.55 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[ZBED4]] | -0.55 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[LYPLA1]] | -0.54 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[SMURF2]] | -0.53 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[BMP2K]] | -0.53 | -0.44 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers BTN3A3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GBP4]] | B | GBP4 activity raises BTN3A3's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.91× lower at baseline in the lines without GBP4 | 0.037 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[MR1]] | B | MR1 activity raises BTN3A3's level | lines that do not express MR1 (5) vs lines expressing it (45) | 2.10× lower at baseline in the lines without MR1 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: GGT7, AGK, TCTN1 |
| [[EPSTI1]] | B | EPSTI1 activity strengthens BTN3A3's drug response | lines that do not express EPSTI1 (25) vs lines expressing it (21) | the lines without EPSTI1 respond 0.61× as strongly (z diff +1.26); strongest at Belinostat 5 µM: 0.53x vs 0.33x (z diff +3.0) | 0.075 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933; target measured in part of the lines; artifact flags |
| [[SAMD9L]] | B | SAMD9L activity strengthens BTN3A3's drug response | lines that do not express SAMD9L (17) vs lines expressing it (29) | the lines without SAMD9L respond 0.53× as strongly (z diff +1.59); strongest at Panobinostat 0.5 µM: 0.58x vs 0.32x (z diff +3.0) | 0.081 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22; target measured in part of the lines; artifact flags |
| [[CASP10]] | B | CASP10 activity raises BTN3A3's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 1.31× lower at baseline in the lines without CASP10 | 0.081 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[IDO1]] | B | IDO1 activity raises BTN3A3's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 1.69× lower at baseline in the lines without IDO1 | 0.085 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3 |
| [[GBP4]] | B | GBP4 activity strengthens BTN3A3's drug response | lines that do not express GBP4 (18) vs lines expressing it (28) | the lines without GBP4 respond 0.54× as strongly (z diff +1.41); strongest at Belinostat 5 µM: 0.54x vs 0.37x (z diff +2.3) | 0.087 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1; target measured in part of the lines; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity lowers BTN3A3's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.518). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.3, 52.6); signed map (60.4, 30.7). **Vector** length 79.5, 15.3% of its response variance represented; |z| ≥ 3 in 1,171 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.2 | +5.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.7 | +4.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.5 | +4.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.4 | +4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +3.8 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.6 | -10.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.3 | -11.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.2 | -11.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.0 | -4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -6.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.9 | -3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -5.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.5 | -0.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | butyrophilin subfamily 3 member A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.2 — chr6:26,440,472-26,453,415 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BTF3, BTN3.3 |
| Gene groups (HGNC) | Butyrophilins; V-set domain containing |
| Reactome | 2 pathways, smallest: Butyrophilin (BTN) family interactions; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [O00478](https://www.uniprot.org/uniprotkb/O00478) (Butyrophilin subfamily 3 member A3):

> Plays a role in T-cell responses in the adaptive immune response.

**Summary**, from NCBI Gene [10384](https://www.ncbi.nlm.nih.gov/gene/10384):

> The butyrophilin (BTN) genes are a group of major histocompatibility complex (MHC)-associated genes that encode type I membrane proteins with 2 extracellular immunoglobulin (Ig) domains and an intracellular B30.2 (PRYSPRY) domain. Three subfamilies of human BTN genes are located in the MHC class I region: the single-copy BTN1A1 gene (MIM 601610) and the BTN2 (e.g., BTN2A1; MIM 613590) and BTN3 (e.g., BNT3A3) genes, which have undergone tandem duplication, resulting in 3 copies of each (summary …

**Accessions** — [HGNC:1140](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1140) · Entrez [10384](https://www.ncbi.nlm.nih.gov/gene/10384) · UniProt [O00478](https://www.uniprot.org/uniprotkb/O00478) · Ensembl [ENSG00000111801](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111801)

## Data

Gene col 3284: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3284); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3284, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3284]; `tensor/DDL_lfc|DDL_z.npy` [3284]; `embed/gene_vectors.npy` [3284]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3284 or target_col == 3284). Every well: [[BTN3A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTN3A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
