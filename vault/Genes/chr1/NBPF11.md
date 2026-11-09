---
symbol: "NBPF11"
type: "gene"
col: 15431
ensembl_id: "ENSG00000263956"
name: "NBPF member 11"
location: "1q21.2"
module: 20
arm: "-"
pooled_cpm: 28.87
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# NBPF11

*NBPF member 11* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.34× (z +8.2, q 1e-13, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.482× (z -14.5, q 4e-45, down in 33 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.524× (z -12.9, q 8e-36, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBPF12]] (+0.92, fdr 7e-06), [[SUGP1]] (+0.69, fdr 7e-06), [[PSMD5]] (+0.66, fdr 7e-06); moves opposite to [[VMA21]] (-0.65, fdr 7e-06), [[EIF5A]] (-0.62, fdr 1e-05), [[MAT2A]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15431.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +8.2 | 1e-13 | 29/47 (HEC-1-A, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.63×** | +5.1 | 9e-05 | 19/49 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.0 | 9e-05 | 21/46 (NCI-H23, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.012 | 11/48 (SW 900, LoVo, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.36× | +3.2 | 0.15 | 5/48 (NCI-H460, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.15 | 5/48 (COLO 205, SHP-77, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.17 | 5/48 (COLO 205, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | 1.34× | +3.0 | 0.17 | 7/45 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15431.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.482×** | -14.5 | 4e-45 | 33/44 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.476×** | -14.2 | 1e-43 | 30/38 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.524×** | -12.9 | 8e-36 | 38/47 (A-172, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.565×** | -10.5 | 1e-23 | 32/42 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.620×** | -9.5 | 2e-19 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.642×** | -8.8 | 1e-16 | 29/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.741×** | -6.0 | 2e-07 | 24/46 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.810×** | -5.9 | 2e-07 | 24/48 (Hs 766T, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.748×** | -5.8 | 4e-07 | 22/45 (NCI-H23, HCT15, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.766×** | -5.3 | 6e-06 | 21/48 (A549, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.774×** | -5.1 | 2e-05 | 24/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.859× | -4.3 | 9e-04 | 14/48 (NCI-H460, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.811×** | -4.2 | 0.001 | 16/48 (CFPAC-1, SW 1088, …) | two highest doses |  |
| [[OTS514 (drug)]] 5 µM |  | **0.682×** | -4.0 | 0.003 | 18/44 (HCT15, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.821×** | -3.8 | 0.006 | 19/47 (C32, NCI-H460, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.844× | -3.4 | 0.024 | 7/48 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.887× | -3.4 | 0.024 | 10/48 (SW 1271, C32, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.858× | -3.1 | 0.072 | 7/48 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15431. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 46.5 | 1 | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -20.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.287× (z -15.8) |
| [[SW480 (line)]] | alt | 28.9 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0733× (z -28.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.287× (z -14.1) |
| [[HEC-1-A (line)]] | alt | 26.6 | 3 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +16.1) | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -12.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 42.9 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +8.8) | [[Auranofin (drug)]] 5 µM 0.190× (z -16.4) |
| [[Hs 766T (line)]] | wt | 29.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[XRK3F2 (drug)]] 0.5 µM 0.0690× (z -13.4) |
| [[NCI-H1792 (line)]] | alt | 39.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0575× (z -22.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 37.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -13.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 36.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -18.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 32.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.313× (z -12.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 26.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.239× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.317× (z -8.5) |
| [[BT-474 (line)]] | alt | 15.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.139× (z -10.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 26.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -10.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 24.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 36.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0491× (z -27.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 40.9 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.328× (z -9.1) |
| [[A-427 (line)]] | wt | 29.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -14.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 34.6 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0824× (z -10.2) |
| [[C32 (line)]] | wt | 32.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.160× (z -13.2) |
| [[H4 (line)]] | wt | 22.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 19.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -15.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 46.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -15.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 18.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +13.0) | — |
| [[Panc 03.27 (line)]] | alt | 25.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.300× (z -8.5) |
| [[SHP-77 (line)]] | alt | 43.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -12.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15431), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF12]] | +0.92 | +0.89 / +0.91 | both halves | 7e-06 | same gene group; STRING 786 |
| [[SUGP1]] | +0.69 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[PSMD5]] | +0.66 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[MTIF3]] | +0.63 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[CCDC115]] | +0.62 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[NKAP]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[CDK7]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[SUMO4]] | +0.61 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[NFKBIL1]] | +0.61 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[HADHB]] | +0.60 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[CCDC174]] | +0.60 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[RBMX2]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMA21]] | -0.65 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[EIF5A]] | -0.62 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[MAT2A]] | -0.60 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[MMGT1]] | -0.59 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[MAPRE1]] | -0.58 | -0.41 / -0.67 | both halves | 4e-05 |  |
| [[PSME3]] | -0.58 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[TARDBP]] | -0.57 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[MOB1A]] | -0.56 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[RNF32-AS1]] | -0.54 | -0.37 / -0.56 | both halves | 8e-05 |  |
| [[DIAPH1]] | -0.54 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[SPCS3]] | -0.54 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[TMX1]] | -0.54 | -0.51 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.553). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-37.9, -11.9); signed map (-15.6, -4.6). **Vector** length 93.9, 20.3% of its response variance represented; |z| ≥ 3 in 887 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +8.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.1 | +1.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.9 | +5.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.7 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +2.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.9 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +1.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.2 | -12.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.9 | -10.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.9 | -8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.2 | -14.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -0.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.1 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | NBPF member 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:148,102,047-148,152,322 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously NBPF24 |
| Gene groups (HGNC) | NBPF members |
| Matched by | ensembl_id |

UniProt [Q86T75](https://www.uniprot.org/uniprotkb/Q86T75) carries no function annotation.

**Summary**, from NCBI Gene [200030](https://www.ncbi.nlm.nih.gov/gene/200030):

> Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31993](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31993) · Entrez [200030](https://www.ncbi.nlm.nih.gov/gene/200030) · UniProt [Q86T75](https://www.uniprot.org/uniprotkb/Q86T75) · Ensembl [ENSG00000263956](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000263956)

## Data

Gene col 15431: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15431); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15431, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15431]; `tensor/DDL_lfc|DDL_z.npy` [15431]; `embed/gene_vectors.npy` [15431]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15431 or target_col == 15431). Every well: [[NBPF11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NBPF11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
