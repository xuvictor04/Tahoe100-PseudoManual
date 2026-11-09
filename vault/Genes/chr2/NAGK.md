---
symbol: "NAGK"
type: "gene"
col: 4522
ensembl_id: "ENSG00000124357"
name: "N-acetylglucosamine kinase"
location: "2p13.3"
module: 41
arm: "+"
pooled_cpm: 20.12
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 21
n_dd_up_clean: 10
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# NAGK

*N-acetylglucosamine kinase* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.13× (z +11.7, q 3e-29, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.418× (z -13.4, q 3e-38, down in 36 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.514× (z -10.2, q 5e-22, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLXNA3]] (+0.65, fdr 1e-05), [[ZMYM6]] (+0.64, fdr 1e-05), [[SNAP29]] (+0.63, fdr 1e-05); moves opposite to [[PTGR2]] (-0.58, fdr 2e-05), [[TBC1D5]] (-0.57, fdr 1e-05), [[GABPB1-AS1]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[DAB2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4522.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.13×** | +11.7 | 3e-29 | 39/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.13×** | +11.7 | 3e-29 | 37/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.65×** | +7.8 | 1e-12 | 29/48 (PANC-1, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.41×** | +5.1 | 4e-05 | 19/47 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +4.3 | 0.002 | 19/46 (LoVo, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.32×** | +4.3 | 0.002 | 15/47 (NCI-H2030, H4, …) | rises with dose | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.45×** | +4.2 | 0.003 | 15/44 (A-172, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.9 | 0.006 | 16/48 (SW1417, Panc 03.27, …) | rises with dose | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.057 | 12/48 (LS 180, KATO III, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.067 | 8/45 (PANC-1, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trimetrexate (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.081 | 8/48 (A-172, PANC-1, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.31× | +3.0 | 0.11 | 8/46 (CFPAC-1, HEC-1-A, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4522.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.418×** | -13.4 | 3e-38 | 36/47 (LS 180, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.514×** | -10.2 | 5e-22 | 37/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.519×** | -10.1 | 1e-21 | 38/48 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.557×** | -9.0 | 4e-17 | 31/48 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.578×** | -8.4 | 4e-15 | 34/48 (HS-578T, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.387×** | -7.6 | 2e-12 | 32/48 (HOP62, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.615×** | -7.5 | 7e-12 | 31/48 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.605×** | -7.3 | 2e-11 | 29/48 (HOP62, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.418×** | -7.0 | 2e-10 | 28/45 (A-172, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.635×** | -7.0 | 2e-10 | 23/38 (HOP62, HCT15, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.657×** | -5.9 | 1e-07 | 23/33 (NCI-H460, HOP62, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.773×** | -5.5 | 1e-06 | 25/46 (HS-578T, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.518×** | -5.3 | 6e-06 | 20/40 (SK-MEL-2, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.721×** | -5.0 | 2e-05 | 24/48 (SK-MEL-2, MIA PaCa-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.724×** | -4.7 | 8e-05 | 23/42 (NCI-H23, NCI-H1792, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.732×** | -3.4 | 0.020 | 9/48 (hTERT-HPNE, HCT15, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.667×** | -3.2 | 0.034 | 9/45 (Hs 766T, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4522. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 28.5 | 0 | 11 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.168× (z -14.5) |
| [[A-172 (line)]] | wt | 59.2 | 0 | 7 (6 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -12.3) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.373× (z -8.5) |
| [[HS-578T (line)]] | alt | 39.5 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.271× (z -11.0) |
| [[H4 (line)]] | wt | 29.4 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.142× (z -10.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.181× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 29.1 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -14.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 16.7 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.85× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.227× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.311× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 41.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 23.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -9.0) |
| [[HT-29 (line)]] | alt | 14.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 14.4 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.200× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.214× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 12.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0972× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[PANC-1 (line)]] | alt | 15.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.33× (z +10.3) | — |
| [[SHP-77 (line)]] | alt | 14.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Bergenin (drug)]] 0.5 µM 0.189× (z -8.7) |
| [[SNU-423 (line)]] | alt | 27.1 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.262× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[A498 (line)]] | wt | 30.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -13.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 26.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[COLO 205 (line)]] | alt | 17.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HCT15 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.110× (z -11.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0660× (z -11.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 19.0 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.107× (z -9.0) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0966× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[KATO III (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[LS 180 (line)]] | wt | 15.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0427× (z -19.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 14.6 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.196× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 20.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.117× (z -13.9) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[SK-MEL-2 (line)]] | alt | 14.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0377× (z -16.6) |
| [[SW 900 (line)]] | alt | 25.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.165× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~16% of this change |
| [[A-427 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4522), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLXNA3]] | +0.65 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[ZMYM6]] | +0.64 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[SNAP29]] | +0.63 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[METRNL]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[EPOR]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[DLGAP4]] | +0.60 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[ATOSB]] | +0.60 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[RCE1]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[PMM1]] | +0.60 | +0.65 / +0.45 | both halves | 3e-05 | pathway: Asparagine N-linked glycosylation |
| [[ARMCX2]] | +0.59 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[RING1]] | +0.59 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[GOLGA2]] | +0.58 | +0.59 / +0.45 | both halves | 3e-05 | pathway: Asparagine N-linked glycosylation |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTGR2]] | -0.58 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[TBC1D5]] | -0.57 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[GABPB1-AS1]] | -0.55 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[TTC39C]] | -0.54 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[NUDT3]] | -0.54 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[DPY19L1P1]] | -0.54 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[NSMAF]] | -0.54 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[ARID2]] | -0.54 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[SLC12A2-DT]] | -0.54 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[NFIA]] | -0.53 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[KTN1-AS1]] | -0.53 | -0.48 / -0.27 | both halves | 3e-04 |  |
| [[PDE3B]] | -0.53 | -0.50 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DAB2]] | B | DAB2 activity raises NAGK's level | lines that do not express DAB2 (18) vs lines expressing it (32) | 1.45× lower at baseline in the lines without DAB2 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: C9, NNMT, DPYSL3 |
| [[NFIA]] | B | NFIA activity lowers NAGK's level | lines that do not express NFIA (11) vs lines expressing it (39) | 1.75× higher at baseline in the lines without NFIA | 0.050 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |
| [[TMEM92-AS1]] | B | TMEM92-AS1 activity raises NAGK's level | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | 1.49× lower at baseline in the lines without TMEM92-AS1 | 0.051 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |
| [[GPR173]] | B | GPR173 activity strengthens NAGK's drug response | lines that do not express GPR173 (30) vs lines expressing it (18) | the lines without GPR173 respond 0.91× as strongly (z diff +0.52); strongest at Ouabain (Octahydrate) 5 µM: 0.60x vs 0.39x (z diff +2.6) | 0.069 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2; target measured in part of the lines; both ways; artifact flags |
| [[TMEM92-AS1]] | B | TMEM92-AS1 activity strengthens NAGK's drug response | lines that do not express TMEM92-AS1 (16) vs lines expressing it (32) | the lines without TMEM92-AS1 respond 0.74× as strongly (z diff +0.89); strongest at Ouabain (Octahydrate) 0.5 µM: 0.79x vs 0.44x (z diff +3.2) | 0.096 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.578). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (11.8, -2.0); signed map (-22.3, 24.1). **Vector** length 102, 25.2% of its response variance represented; |z| ≥ 3 in 1,146 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.4 | +11.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +4.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.9 | +11.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.5 | +1.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +3.1 | +5.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.0 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +4.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.8 | +4.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.6 | +1.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -5.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -3.1 | -5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.1 | -7.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -2.8 | -1.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.6 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -7.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | N-acetylglucosamine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:71,064,344-71,079,808 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GNK |
| Gene groups (HGNC) | Carbohydrate kinases |
| Hallmark sets | HYPOXIA |
| Reactome | 4 pathways, smallest: Synthesis of UDP-N-acetyl-glucosamine; Synthesis of substrates in N-glycan biosythesis; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJ70](https://www.uniprot.org/uniprotkb/Q9UJ70) (N-acetyl-D-glucosamine kinase):

> Converts endogenous N-acetylglucosamine (GlcNAc), a major component of complex carbohydrates, from lysosomal degradation or nutritional sources into GlcNAc 6-phosphate. Involved in the N-glycolylneuraminic acid (Neu5Gc) degradation pathway: although human is not able to catalyze formation of Neu5Gc due to the inactive CMAHP enzyme, Neu5Gc is present in food and must be degraded. Also has N-acetylmannosamine (ManNAc) kinase activity (By similarity). Also involved in innate immunity by promoting …

**Summary**, from NCBI Gene [55577](https://www.ncbi.nlm.nih.gov/gene/55577):

> This gene encodes a member of the N-acetylhexosamine kinase family. The encoded protein catalyzes the conversion of N-acetyl-D-glucosamine to N-acetyl-D-glucosamine 6-phosphate, and is the major mammalian enzyme which recovers amino sugars. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:17174](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17174) · Entrez [55577](https://www.ncbi.nlm.nih.gov/gene/55577) · UniProt [Q9UJ70](https://www.uniprot.org/uniprotkb/Q9UJ70) · Ensembl [ENSG00000124357](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124357)

## Data

Gene col 4522: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4522); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4522, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4522]; `tensor/DDL_lfc|DDL_z.npy` [4522]; `embed/gene_vectors.npy` [4522]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4522 or target_col == 4522). Every well: [[NAGK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAGK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
