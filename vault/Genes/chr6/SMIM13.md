---
symbol: "SMIM13"
type: "gene"
col: 13401
ensembl_id: "ENSG00000224531"
name: "small integral membrane protein 13"
location: "6p24.2"
module: 18
arm: "+"
pooled_cpm: 20.87
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# SMIM13

*small integral membrane protein 13* — 6p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (11 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.49× (z +13.5, q 1e-38, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.643× (z -9.1, q 4e-17, down in 24 of 43 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (A549 0.158×, MIA PaCa-2 0.117×, J82 0.272×, SW480 0.341×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.119×, NCI-H23 0.264×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.290×, NCI-H460 0.391×; ⚠ cell-cycle shift, explains ~42% of this change); [[Darinaparsin (drug)]] 0.5 µM in 1 line (H4 0.129×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UCK2]] (+0.65, fdr 7e-06), [[FAM24B]] (+0.64, fdr 7e-06), [[POMGNT2]] (+0.62, fdr 7e-06); moves opposite to [[SGO1-AS1]] (-0.50, fdr 4e-05), [[GOLGB1]] (-0.50, fdr 3e-05), [[EFCAB10]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[BVES]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13401.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.49×** | +13.5 | 1e-38 | 37/48 (C32, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +8.9 | 2e-16 | 33/47 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +7.1 | 3e-10 | 23/48 (SW480, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +6.3 | 5e-08 | 24/48 (NCI-H23, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +6.2 | 6e-08 | 21/47 (NCI-H23, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **1.37×** | +5.9 | 3e-07 | 22/44 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.33×** | +5.9 | 4e-07 | 15/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +5.2 | 2e-05 | 18/46 (C32, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.19× | +5.0 | 4e-05 | 17/48 (J82, HEC-1-A, …) | top dose only | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.27×** | +4.9 | 7e-05 | 16/47 (NCI-H1573, CFPAC-1, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +4.6 | 2e-04 | 17/47 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.53×** | +4.6 | 2e-04 | 12/47 (HT-29, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +4.5 | 3e-04 | 19/47 (HepG2/C3A, H4, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.24×** | +4.5 | 3e-04 | 13/47 (LoVo, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.24×** | +4.5 | 3e-04 | 16/47 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +4.3 | 7e-04 | 18/47 (LoVo, NCI-H460, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +4.1 | 0.001 | 11/48 (HT-29, NCI-H2030, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +4.1 | 0.001 | 15/47 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.45×** | +4.0 | 0.002 | 7/47 (PANC-1, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.003 | 14/47 (NCI-H2030, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.20×** | +3.8 | 0.004 | 11/47 (HepG2/C3A, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.20×** | +3.8 | 0.004 | 11/48 (J82, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.006 | 9/47 (NCI-H460, J82, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13401.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (A549 0.158×, MIA PaCa-2 0.117×, J82 0.272×, SW480 0.341×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.119×, NCI-H23 0.264×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.290×, NCI-H460 0.391×; ⚠ cell-cycle shift, explains ~42% of this change); [[Darinaparsin (drug)]] 0.5 µM in 1 line (H4 0.129×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.643×** | -9.1 | 4e-17 | 24/43 (C-33 A, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.646×** | -8.2 | 5e-14 | 23/32 (A549, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.849× | -4.8 | 3e-04 | 25/47 (A-427, NCI-H460, …) | top dose only | composition shift |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.837× | -3.7 | 0.032 | 4/48 (NCI-H2030, NCI-H2347, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.858× | -3.2 | 0.14 | 4/48 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[Nimesulide (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.859× | -3.2 | 0.14 | 5/47 (HOP62, HepG2/C3A, …) | inconsistent across doses |  |
| [[Phenytoin (sodium) (drug)]] 5 µM |  | 0.848× | -3.1 | 0.14 | 7/47 (PANC-1, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13401. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 21.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 17.6× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 22.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.35× (z +8.6) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -13.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A-427 (line)]] | wt | 28.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -14.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A549 (line)]] | wt | 20.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -13.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -14.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 15.6 | 0 | 1 | — | [[Darinaparsin (drug)]] 0.5 µM 0.129× (z -8.8) |
| [[HOP62 (line)]] | alt | 19.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.33× (z +8.8) | — |
| [[J82 (line)]] | alt | 47.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -10.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 54.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 29.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -11.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.406× (z -8.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 18.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -9.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 30.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.166× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.341× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13401), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UCK2]] | +0.65 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[FAM24B]] | +0.64 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[POMGNT2]] | +0.62 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[CHST10]] | +0.61 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[EEF1E1]] | +0.59 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[RFXAP]] | +0.59 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[RNF2]] | +0.59 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[PCGF6]] | +0.57 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[PALS2]] | +0.57 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[MFSD14CP]] | +0.56 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[LRP12]] | +0.56 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[CDYL]] | +0.55 | +0.60 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGO1-AS1]] | -0.50 | -0.52 / -0.40 | both halves | 4e-05 |  |
| [[GOLGB1]] | -0.50 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[EFCAB10]] | -0.50 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[MED29]] | -0.50 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[XRN1]] | -0.48 | -0.43 / -0.50 | both halves | 4e-05 |  |
| [[RC3H1]] | -0.48 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[CHMP4A]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[USP11]] | -0.47 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[BAZ2B]] | -0.47 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[USP8]] | -0.47 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[BPTF]] | -0.46 | -0.49 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BVES]] | B | BVES activity raises SMIM13's level | lines that do not express BVES (19) vs lines expressing it (31) | 1.46× lower at baseline in the lines without BVES | 0.014 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2 |
| [[GNAZ]] | B | GNAZ activity raises SMIM13's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.63× lower at baseline in the lines without GNAZ | 0.024 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[ADCY3]] | B | ADCY3 activity raises SMIM13's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.18× lower at baseline in the lines without ADCY3 | 0.093 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[ANKRD13B]] | C | ANKRD13B activity raises SMIM13's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 2.19× lower at baseline in the lines without ANKRD13B | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.510). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-6.6, -3.3); signed map (-37.5, -18.7). **Vector** length 81.9, 15.8% of its response variance represented; |z| ≥ 3 in 790 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | +4.9 | +5.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +8.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.4 | +5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +7.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -5.5 | -4.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.1 | -9.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.8 | -8.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.2 | -0.9 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[Filgotinib (drug)]] 0.05 µM |  | -1.1 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | small integral membrane protein 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.2 — chr6:11,093,834-11,138,733 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C6orf228 |
| Matched by | ensembl_id |

UniProt [P0DJ93](https://www.uniprot.org/uniprotkb/P0DJ93) carries no function annotation.

**Summary**, from NCBI Gene [221710](https://www.ncbi.nlm.nih.gov/gene/221710):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27356](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27356) · Entrez [221710](https://www.ncbi.nlm.nih.gov/gene/221710) · UniProt [P0DJ93](https://www.uniprot.org/uniprotkb/P0DJ93) · Ensembl [ENSG00000224531](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224531)

## Data

Gene col 13401: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13401); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13401, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13401]; `tensor/DDL_lfc|DDL_z.npy` [13401]; `embed/gene_vectors.npy` [13401]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13401 or target_col == 13401). Every well: [[SMIM13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMIM13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
