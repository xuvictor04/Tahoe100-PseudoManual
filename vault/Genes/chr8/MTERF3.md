---
symbol: "MTERF3"
type: "gene"
col: 7983
ensembl_id: "ENSG00000156469"
name: "mitochondrial transcription termination factor 3"
location: "8q22.1"
module: 18
arm: "+"
pooled_cpm: 19.59
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# MTERF3

*mitochondrial transcription termination factor 3* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.07× (z +12.4, q 1e-32, up in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 2.07× (z +12.3, q 2e-32, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.590× (z -12.7, q 3e-34, down in 34 of 47 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.624× (z -8.0, q 1e-13, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GEMIN5]] (+0.72, fdr 7e-06), [[PRMT7]] (+0.70, fdr 7e-06), [[SNRNP40]] (+0.69, fdr 7e-06); moves opposite to [[STX4]] (-0.63, fdr 7e-06), [[COL11A2]] (-0.61, fdr 3e-05), [[NPHS1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ATXN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7983.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.07×** | +12.4 | 1e-32 | 41/48 (A498, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.07×** | +12.3 | 2e-32 | 42/47 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.76×** | +9.6 | 1e-19 | 39/48 (A498, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.70×** | +8.7 | 7e-16 | 29/44 (SW480, NCI-H1573, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +6.9 | 5e-10 | 29/47 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.38×** | +5.3 | 1e-05 | 17/46 (SW 900, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.35×** | +5.1 | 3e-05 | 18/47 (PANC-1, J82, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.21×** | +4.6 | 4e-04 | 22/47 (NCI-H2030, HOP62, …) | top dose only |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.031 | 3/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.23×** | +3.5 | 0.031 | 7/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.034 | 5/46 (PANC-1, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.3 | 0.046 | 7/26 (SW480, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.046 | 9/46 (NCI-H460, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 1.14× | +3.1 | 0.076 | 11/48 (A-427, SK-MEL-2, …) | top dose only | low cells (technical?); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.076 | 3/48 (AsPC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.082 | 10/46 (HOP62, J82, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7983.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.590×** | -12.7 | 3e-34 | 34/47 (A-172, J82, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.518×** | -11.2 | 1e-26 | 30/41 (RKO, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.548×** | -9.9 | 1e-20 | 22/30 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.624×** | -8.0 | 1e-13 | 32/47 (C32, A-172, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.668×** | -6.3 | 2e-08 | 22/36 (A549, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.796×** | -5.5 | 3e-06 | 23/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -4.6 | 3e-04 | 5/48 (COLO 205, SW 900, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.746×** | -3.6 | 0.025 | 12/48 (SNU-423, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (maleate) (drug)]] 0.05 µM |  | **0.805×** | -3.4 | 0.039 | 12/47 (SW 1271, J82, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.762×** | -3.3 | 0.054 | 12/48 (HS-578T, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.820×** | -3.3 | 0.058 | 19/48 (PANC-1, C32, …) | top dose only | composition shift |
| [[Entrectinib (drug)]] 5 µM |  | 0.837× | -3.0 | 0.10 | 8/47 (LoVo, KATO III, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.779× | -3.0 | 0.10 | 10/48 (Hs 766T, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7983. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 32.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0670× (z -26.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 28.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -10.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 16.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A498 (line)]] | wt | 20.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.91× (z +8.6) ⚠ cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -9.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A549 (line)]] | wt | 22.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0898× (z -15.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 22.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -11.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 30.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.264× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change · without an alert: [[AT7519 (drug)]] 5 µM 0.0828× (z -8.9) |
| [[AN3 CA (line)]] | alt | 29.2 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0661× (z -9.8) |
| [[BT-474 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -12.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 40.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -9.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 31.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.150× (z -12.3) |
| [[CHP-212 (line)]] | wt | 21.5 | 0 | 1 | — | [[Rosiglitazone (drug)]] 0.05 µM 0.0553× (z -9.0) |
| [[H4 (line)]] | wt | 15.1 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0904× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -12.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 12.3 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.143× (z -8.5) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 22.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -9.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H23 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H460 (line)]] | wt | 14.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -8.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[RKO (line)]] | wt | 58.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -14.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -9.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -8.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW48 (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -8.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7983), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GEMIN5]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[PRMT7]] | +0.70 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[SNRNP40]] | +0.69 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[WDR5]] | +0.67 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[WDR3]] | +0.66 | +0.59 / +0.61 | both halves | 7e-06 | pathway: rRNA processing |
| [[EEF1E1]] | +0.65 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[DTD2]] | +0.64 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[NTAQ1]] | +0.64 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[NDC1]] | +0.63 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[ORC5]] | +0.63 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[ASB13]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[TTLL4]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX4]] | -0.63 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[COL11A2]] | -0.61 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[NPHS1]] | -0.60 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[ZBTB4]] | -0.59 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[CDK3]] | -0.58 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[NLGN3]] | -0.58 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[CELF6]] | -0.57 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[DNAH12]] | -0.57 | -0.43 / -0.64 | both halves | 3e-05 |  |
| [[PLA2G6]] | -0.57 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[RGL2]] | -0.56 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[COLQ]] | -0.56 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[CPNE9]] | -0.55 | -0.62 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATXN1]] | B | ATXN1 activity lowers MTERF3's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 1.74× higher at baseline in the lines without ATXN1 | 0.048 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.600). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-6.6, -16.6); signed map (-40.3, -18.8). **Vector** length 91.2, 19.0% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | +5.7 | +8.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.0 | +6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +3.2 | +5.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.8 | +12.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.6 | +2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.5 | +1.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.3 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -8.1 | -12.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.2 | -8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.7 | -11.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -4.6 | -3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.6 | -9.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -5.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial transcription termination factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:96,239,398-96,261,610 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-12, FLJ10939; previously MTERFD1 |
| Reactome | 10 pathways, smallest: rRNA modification in the mitochondrion; Mitochondrial mRNA modification; PINK1-PRKN Mediated Mitophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96E29](https://www.uniprot.org/uniprotkb/Q96E29) (Transcription termination factor 3, mitochondrial):

> Binds promoter DNA and regulates initiation of transcription. Required for normal mitochondrial transcription and translation, and for normal assembly of mitochondrial respiratory complexes. Required for normal mitochondrial function (By similarity). Maintains 16S rRNA levels and functions in mitochondrial ribosome assembly by regulating the biogenesis of the 39S ribosomal subunit (By similarity).

**Summary**, from NCBI Gene [51001](https://www.ncbi.nlm.nih.gov/gene/51001):

> Enables transcription cis-regulatory region binding activity. Involved in negative regulation of DNA-templated transcription. Located in mitochondrial matrix. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24258](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24258) · Entrez [51001](https://www.ncbi.nlm.nih.gov/gene/51001) · UniProt [Q96E29](https://www.uniprot.org/uniprotkb/Q96E29) · Ensembl [ENSG00000156469](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156469)

## Data

Gene col 7983: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7983); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7983, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7983]; `tensor/DDL_lfc|DDL_z.npy` [7983]; `embed/gene_vectors.npy` [7983]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7983 or target_col == 7983). Every well: [[MTERF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTERF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
