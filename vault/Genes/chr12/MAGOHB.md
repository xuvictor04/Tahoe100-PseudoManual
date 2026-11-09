---
symbol: "MAGOHB"
type: "gene"
col: 3198
ensembl_id: "ENSG00000111196"
name: "mago homolog B, exon junction complex subunit"
location: "12p13.2"
module: 148
arm: "+"
pooled_cpm: 22.03
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 16
n_dd_up_clean: 8
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# MAGOHB

*mago homolog B, exon junction complex subunit* — 12p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.66× (z +17.8, q 0e+00, up in 41 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.76× (z +10.1, q 6e-22, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.573× (z -10.1, q 3e-21, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ICE2]] (+0.75, fdr 7e-06), [[MIS12]] (+0.72, fdr 7e-06), [[MLH1]] (+0.72, fdr 7e-06); moves opposite to [[COX6A1]] (-0.65, fdr 1e-05), [[SNN]] (-0.64, fdr 4e-05), [[UBA52]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 148]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3198.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.66×** | +17.8 | 0e+00 | 41/43 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.61×** | +16.1 | 0e+00 | 34/36 (A498, SW480, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +13.4 | 7e-39 | 29/34 (NCI-H1792, SW480, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.60×** | +12.0 | 5e-31 | 31/47 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.88×** | +11.0 | 3e-26 | 41/47 (SW 900, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +10.1 | 6e-22 | 35/47 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +8.1 | 6e-14 | 35/48 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +6.5 | 4e-09 | 24/47 (LOX-IMVI, NCI-H23, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.70×** | +5.0 | 3e-05 | 23/48 (LoVo, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **1.28×** | +4.5 | 4e-04 | 19/44 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +4.4 | 6e-04 | 17/48 (PANC-1, SW 900, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.008 | 13/46 (H4, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.008 | 11/46 (PANC-1, HCT15, …) | inconsistent across doses | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.010 | 13/46 (NCI-H1573, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.042 | 9/45 (NCI-H23, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.071 | 9/48 (HOP62, HT-29, …) | inconsistent across doses |  |
| [[LJI308 (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.099 | 6/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.099 | 13/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3198.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.573×** | -10.1 | 3e-21 | 37/48 (KATO III, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.602×** | -9.2 | 8e-18 | 35/48 (HS-578T, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.615×** | -8.8 | 2e-16 | 34/47 (SW 900, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.748×** | -7.5 | 1e-11 | 35/48 (NCI-H1573, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.674×** | -7.0 | 2e-10 | 31/48 (HOP62, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.700×** | -6.5 | 8e-09 | 31/48 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.701×** | -6.5 | 9e-09 | 24/47 (C-33 A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.725×** | -5.8 | 4e-07 | 28/47 (NCI-H1573, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | **0.811×** | -5.4 | 4e-06 | 21/48 (KATO III, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.765×** | -4.9 | 6e-05 | 15/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.773×** | -4.7 | 1e-04 | 17/47 (NCI-H23, SW48, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.800×** | -3.8 | 0.006 | 12/48 (MIA PaCa-2, J82, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.827×** | -3.3 | 0.039 | 12/47 (A-172, NCI-H2030, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -3.3 | 0.042 | 18/47 (NCI-H1792, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.828×** | -3.2 | 0.045 | 17/48 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.722×** | -3.1 | 0.068 | 9/48 (SW1417, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.724×** | -3.1 | 0.072 | 3/48 (SW480, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3198. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 34.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 20.9 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +13.9) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[SW480 (line)]] | alt | 25.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +10.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 33.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +15.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.57× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 49.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.1) ⚠ cell-cycle shift, explains ~39% of this change | [[Digitoxin (drug)]] 5 µM 0.401× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 12.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.58× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 19.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -11.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM 0.106× (z -11.0) |
| [[SW 900 (line)]] | alt | 29.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +11.2) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[A-427 (line)]] | wt | 61.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.453× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 16.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +10.1) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.187× (z -10.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 23.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 17.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.250× (z -8.9) |
| [[HT-29 (line)]] | alt | 19.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +8.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 31.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.362× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 13.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +9.1) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 27.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 35.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +9.1) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 21.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.20× (z +9.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 15.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +11.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3198), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ICE2]] | +0.75 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[MIS12]] | +0.72 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[MLH1]] | +0.72 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[EXOSC8]] | +0.70 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[COX18]] | +0.69 | +0.72 / +0.47 | both halves | 2e-05 |  |
| [[PSME3IP1]] | +0.69 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[MCTS1]] | +0.68 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[PAN2]] | +0.68 | +0.72 / +0.44 | both halves | 3e-05 |  |
| [[FBXO4]] | +0.66 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[GTF2H3]] | +0.64 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[TASOR]] | +0.64 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[SENP1]] | +0.63 | +0.53 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX6A1]] | -0.65 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[SNN]] | -0.64 | -0.70 / -0.41 | both halves | 4e-05 |  |
| [[UBA52]] | -0.64 | -0.52 / -0.64 | both halves | 1e-05 | pathway: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC) |
| [[UBL5]] | -0.64 | -0.60 / -0.49 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[RPLP2]] | -0.64 | -0.57 / -0.58 | both halves | 9e-06 | pathway: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC) |
| [[RPL28]] | -0.64 | -0.52 / -0.66 | both halves | 1e-05 | pathway: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC) |
| [[GNB2]] | -0.63 | -0.64 / -0.46 | both halves | 3e-05 |  |
| [[CYTH3]] | -0.63 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[RPS25]] | -0.63 | -0.57 / -0.59 | both halves | 1e-05 | pathway: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC) |
| [[RPS5]] | -0.62 | -0.57 / -0.56 | both halves | 1e-05 | pathway: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC) |
| [[NENF]] | -0.62 | -0.68 / -0.51 | both halves | 1e-05 |  |
| [[RPS14]] | -0.62 | -0.57 / -0.57 | both halves | 1e-05 | pathway: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC) |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **+** arm (projection on the module's main direction 0.750). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-6.1, 1.9); signed map (15.5, -27.6). **Vector** length 92.7, 20.2% of its response variance represented; |z| ≥ 3 in 958 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.9 | +10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +7.2 | +12.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +6.5 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +16.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.1 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +6.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.2 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | +1.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.8 | +2.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.7 | -6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -7.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.4 | -10.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.3 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | -3.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.7 | -5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -0.4 |
|  | [[4EGI-1 (drug)]] 5 µM |  | -1.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | mago homolog B, exon junction complex subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.2 — chr12:10,604,193-10,613,609 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10292, MGN2 |
| Gene groups (HGNC) | Exon junction complex |
| Reactome | 13 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96A72](https://www.uniprot.org/uniprotkb/Q96A72) (Protein mago nashi homolog 2):

> Required for pre-mRNA splicing as component of the spliceosome. Plays a redundant role with MAGOH in the exon junction complex and in the nonsense-mediated decay (NMD) pathway.

**Summary**, from NCBI Gene [55110](https://www.ncbi.nlm.nih.gov/gene/55110):

> Enables RNA binding activity. Involved in mRNA splicing, via spliceosome and nuclear-transcribed mRNA catabolic process, nonsense-mediated decay. Located in nucleus. Part of U2-type catalytic step 1 spliceosome; U2-type precatalytic spliceosome; and exon-exon junction complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25504](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25504) · Entrez [55110](https://www.ncbi.nlm.nih.gov/gene/55110) · UniProt [Q96A72](https://www.uniprot.org/uniprotkb/Q96A72) · Ensembl [ENSG00000111196](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111196)

## Data

Gene col 3198: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3198); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3198, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3198]; `tensor/DDL_lfc|DDL_z.npy` [3198]; `embed/gene_vectors.npy` [3198]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3198 or target_col == 3198). Every well: [[MAGOHB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAGOHB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
