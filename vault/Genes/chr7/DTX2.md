---
symbol: "DTX2"
type: "gene"
col: 1650
ensembl_id: "ENSG00000091073"
name: "deltex E3 ubiquitin ligase 2"
location: "7q11.23"
module: 31
arm: "+"
pooled_cpm: 23.44
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 25
direction_downstream: 0
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# DTX2

*deltex E3 ubiquitin ligase 2* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 1.46× (z +5.0, q 3e-04, up in 20 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (CFPAC-1 3.27×, J82 3.51×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A498 2.71×, A-172 3.30×; ⚠ cell-cycle shift, explains ~28% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-172 3.78×; ⚠ cell-cycle shift, explains ~35% of this change).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.456× (z -14.7, q 0e+00, down in 30 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.724× (z -8.5, q 2e-15, down in 24 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DTX2P1-UPK3BP1-PMS2P11]] (+0.78, fdr 7e-06), [[IL10RB]] (+0.66, fdr 1e-05), [[HSH2D]] (+0.58, fdr 1e-05); moves opposite to [[ERLIN2]] (-0.54, fdr 2e-04), [[PUS7L]] (-0.54, fdr 5e-05), [[PAK2]] (-0.53, fdr 2e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[INAVA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1650.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (CFPAC-1 3.27×, J82 3.51×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A498 2.71×, A-172 3.30×; ⚠ cell-cycle shift, explains ~28% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-172 3.78×; ⚠ cell-cycle shift, explains ~35% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +5.0 | 3e-04 | 20/43 (SHP-77, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.027 | 9/43 (HepG2/C3A, SW 900, …) | inconsistent across doses |  |
| [[Almonertinib (mesylate) (drug)]] 0.05 µM |  | 1.22× | +3.3 | 0.15 | 7/45 (NCI-H2030, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.21× | +3.2 | 0.15 | 6/44 (SW48, A549, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.2 | 0.15 | 6/47 (A-172, C32, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.38× | +3.1 | 0.15 | 5/31 (BT-474, J82, …) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.26× | +3.1 | 0.15 | 7/45 (RPMI-7951, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1650.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.456×** | -14.7 | 0e+00 | 30/37 (A549, KATO III, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.488×** | -12.9 | 1e-35 | 25/29 (A549, A498, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.465×** | -12.8 | 3e-35 | 25/31 (Panc 03.27, A498, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.724×** | -8.5 | 2e-15 | 24/46 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.759×** | -5.0 | 7e-05 | 20/40 (Panc 03.27, C32, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.768×** | -4.9 | 7e-05 | 20/47 (SW1417, A498, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.787×** | -4.5 | 6e-04 | 20/46 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.660×** | -4.1 | 0.003 | 13/45 (MIA PaCa-2, A498, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.811×** | -3.9 | 0.006 | 14/47 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.813×** | -3.7 | 0.011 | 12/45 (LoVo, RKO, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.877× | -3.5 | 0.028 | 13/48 (HOP62, A549, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.826×** | -3.4 | 0.035 | 8/47 (SW480, BT-474, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | 0.841× | -3.2 | 0.053 | 9/46 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.850× | -3.0 | 0.095 | 15/48 (LoVo, NCI-H460, …) | inconsistent across doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1650. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 94.7 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.71× (z +9.7) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 5 µM 0.124× (z -20.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 59.1 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0612× (z -20.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 31.7 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -20.5) |
| [[Panc 03.27 (line)]] | alt | 47.1 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0702× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.375× (z -8.9) |
| [[A-172 (line)]] | wt | 25.9 | 2 (2 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.78× (z +9.8) ⚠ cell-cycle shift, explains ~35% of this change | [[Dinaciclib (drug)]] 5 µM 0.127× (z -14.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 37.9 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.284× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.358× (z -8.5) |
| [[J82 (line)]] | alt | 12.1 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +10.7) | [[Selinexor (drug)]] 5 µM 0.299× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 54.6 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.521× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 39.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -18.5) |
| [[NCI-H2347 (line)]] | alt | 22.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -10.7) |
| [[SW1417 (line)]] | alt | 35.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -14.3) |
| [[C32 (line)]] | wt | 20.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -11.3) |
| [[COLO 205 (line)]] | alt | 48.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -19.1) |
| [[LS 180 (line)]] | wt | 36.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -14.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 14.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -10.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 15.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0814× (z -13.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 19.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -11.7) |
| [[SW480 (line)]] | alt | 17.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -12.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 30.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -14.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 11.8 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0939× (z -9.4) |
| [[HS-578T (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 7.40 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.256× (z -8.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[PANC-1 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -9.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 10.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -11.7) ⚠ cell-cycle shift, explains ~22% of this change |
| [[A-427 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1650), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTX2P1-UPK3BP1-PMS2P11]] | +0.78 | +0.73 / +0.78 | both halves | 7e-06 |  |
| [[IL10RB]] | +0.66 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[HSH2D]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[TNFRSF1B]] | +0.58 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[IL22RA1]] | +0.57 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[GRAMD1A]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[RHOG]] | +0.56 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[FBXO46]] | +0.56 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[ELF3]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 | pathway: Signaling by NOTCH |
| [[SLC11A2]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[IFNAR2]] | +0.55 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[CBLC]] | +0.55 | +0.39 / +0.54 | both halves | 5e-05 | same gene group |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERLIN2]] | -0.54 | -0.32 / -0.61 | both halves | 2e-04 |  |
| [[PUS7L]] | -0.54 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[PAK2]] | -0.53 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[BTBD1]] | -0.52 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[EIF4H]] | -0.52 | -0.29 / -0.58 | both halves | 2e-04 |  |
| [[SBDSP1]] | -0.51 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[RPN1]] | -0.50 | -0.26 / -0.58 | both halves | 4e-04 |  |
| [[IPO5]] | -0.50 | -0.29 / -0.59 | both halves | 3e-04 |  |
| [[HNRNPA1L3]] | -0.50 | -0.37 / -0.51 | both halves | 9e-05 |  |
| [[TWF1]] | -0.49 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[UBQLN1]] | -0.49 | -0.28 / -0.56 | both halves | 3e-04 |  |
| [[PAPOLA]] | -0.48 | -0.29 / -0.54 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 24, C 1. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[INAVA]] | B | INAVA activity raises DTX2's level | lines that do not express INAVA (29) vs lines expressing it (21) | 2.16× lower at baseline in the lines without INAVA | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[ELF3]] | B | ELF3 activity raises DTX2's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 1.88× lower at baseline in the lines without ELF3 | 0.003 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[ADGRF1]] | B | ADGRF1 activity raises DTX2's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 2.10× lower at baseline in the lines without ADGRF1 | 0.004 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises DTX2's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 1.93× lower at baseline in the lines without TMPRSS4 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[TMPRSS2]] | B | TMPRSS2 activity raises DTX2's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 2.02× lower at baseline in the lines without TMPRSS2 | 0.007 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises DTX2's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 1.88× lower at baseline in the lines without ELF3-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[FA2H]] | B | FA2H activity raises DTX2's level | lines that do not express FA2H (27) vs lines expressing it (23) | 1.78× lower at baseline in the lines without FA2H | 0.008 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[GCNT3]] | B | GCNT3 activity raises DTX2's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 2.02× lower at baseline in the lines without GCNT3 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[HSH2D]] | B | HSH2D activity raises DTX2's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 1.79× lower at baseline in the lines without HSH2D | 0.016 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[CLIC5]] | B | CLIC5 activity raises DTX2's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 1.86× lower at baseline in the lines without CLIC5 | 0.020 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[C6orf132]] | B | C6orf132 activity raises DTX2's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 1.88× lower at baseline in the lines without C6orf132 | 0.020 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1 |
| [[HNF4A]] | B | HNF4A activity raises DTX2's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 2.11× lower at baseline in the lines without HNF4A | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.487). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.6, 41.6); signed map (49.9, 0.5). **Vector** length 90.7, 18.3% of its response variance represented; |z| ≥ 3 in 988 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +4.5 | +5.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +1.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.6 | +3.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.5 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.1 | +2.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.3 | -12.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.2 | -12.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.1 | -14.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -4.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.4 | -5.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.1 | +0.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.8 | -1.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -1.8 | +0.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | deltex E3 ubiquitin ligase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:76,461,676-76,505,995 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RNF58, KIAA1528 |
| Gene groups (HGNC) | Ring finger proteins; Deltex E3 ubiquitin ligase family |
| Hallmark sets | NOTCH_SIGNALING |
| Reactome | 3 pathways, smallest: Activated NOTCH1 Transmits Signal to the Nucleus; Signaling by NOTCH1; Signaling by NOTCH |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UW9](https://www.uniprot.org/uniprotkb/Q86UW9) (Probable E3 ubiquitin-protein ligase DTX2):

> E3 ubiquitin ligase that conjugates ubiquitin to ADP-ribosylated cysteine residues, independently of lysine side chains or free N-termini. For example, PARP7 generates an ADP-ribosyl degron within the DNA-binding domain of the androgen receptor (AR), which is recognized by DTX2 and targeted for proteasomal degradation. Functions in genome stability maintenance by acting as an ADP-ribosylation-dependent regulator of DNA double-strand break repair. Mechanistically, recognizes PARylated substrates …

**Summary**, from NCBI Gene [113878](https://www.ncbi.nlm.nih.gov/gene/113878):

> DTX2 functions as an E3 ubiquitin ligase (Takeyama et al., 2003 [PubMed 12670957]).[supplied by OMIM, Nov 2009]

**Accessions** — [HGNC:15973](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15973) · Entrez [113878](https://www.ncbi.nlm.nih.gov/gene/113878) · UniProt [Q86UW9](https://www.uniprot.org/uniprotkb/Q86UW9) · Ensembl [ENSG00000091073](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091073)

## Data

Gene col 1650: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1650); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1650, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1650]; `tensor/DDL_lfc|DDL_z.npy` [1650]; `embed/gene_vectors.npy` [1650]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1650 or target_col == 1650). Every well: [[DTX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DTX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
