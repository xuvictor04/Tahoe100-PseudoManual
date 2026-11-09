---
symbol: "ZNF45"
type: "gene"
col: 4531
ensembl_id: "ENSG00000124459"
name: "zinc finger protein 45"
location: "19q13.31"
module: 17
arm: "+"
pooled_cpm: 13.67
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 10
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ZNF45

*zinc finger protein 45* — 19q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.68× (z +12.5, q 5e-33, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.433× (z -20.0, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF180]] (+0.77, fdr 7e-06), [[KBTBD6]] (+0.75, fdr 7e-06), [[DDX19B]] (+0.74, fdr 1e-05); moves opposite to [[ATP11C]] (-0.71, fdr 1e-05), [[CCDC200]] (-0.62, fdr 2e-04), [[PRDM10]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ZNF420]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, none with an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4531.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.68×** | +12.5 | 5e-33 | 30/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.65×** | +8.5 | 6e-15 | 30/47 (HT-29, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +7.5 | 8e-12 | 24/48 (KATO III, RPMI-7951, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +7.1 | 2e-10 | 23/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +6.9 | 5e-10 | 24/47 (HT-29, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.18×** | +6.9 | 5e-10 | 24/48 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +6.5 | 6e-09 | 23/47 (HT-29, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +5.3 | 1e-05 | 15/46 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +4.8 | 1e-04 | 14/47 (HT-29, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +4.3 | 9e-04 | 14/47 (SW480, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.61×** | +4.2 | 0.001 | 18/45 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.1 | 0.002 | 17/48 (NCI-H2347, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.005 | 7/47 (KATO III, LS 180, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.027 | 6/48 (LOX-IMVI, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.072 | 6/42 (KATO III, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4531.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.433×** | -20.0 | 0e+00 | 44/47 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.397×** | -15.6 | 0e+00 | 30/36 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.479×** | -11.9 | 2e-30 | 27/45 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.504×** | -11.1 | 1e-26 | 20/25 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.562×** | -9.0 | 3e-17 | 22/32 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.628×** | -7.5 | 4e-12 | 26/46 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.699×** | -5.8 | 6e-07 | 24/42 (SNU-423, SHP-77, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.909× | -5.2 | 2e-05 | 7/48 (Hs 766T, H4, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.777×** | -4.2 | 0.001 | 18/45 (KATO III, LoVo, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.849× | -3.9 | 0.006 | 14/48 (LOX-IMVI, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.806×** | -3.6 | 0.015 | 12/47 (SW 900, KATO III, …) | top dose only | composition shift |
| [[Everolimus (drug)]] 0.05 µM |  | 0.865× | -3.2 | 0.053 | 11/48 (Hs 766T, H4, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.693×** | -3.2 | 0.053 | 15/46 (CFPAC-1, C-33 A, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4531. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.7 | 4 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -11.2) |
| [[A-172 (line)]] | wt | 13.4 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.201× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 19.9 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -13.2) |
| [[SW480 (line)]] | alt | 23.5 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +23.0) | [[Dinaciclib (drug)]] 5 µM 0.0814× (z -24.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.349× (z -10.5) |
| [[A549 (line)]] | wt | 18.5 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -11.3) |
| [[HOP62 (line)]] | alt | 17.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -13.9) |
| [[RPMI-7951 (line)]] | alt | 20.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -10.1) |
| [[SNU-423 (line)]] | alt | 10.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0748× (z -13.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 14.0 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -10.3) |
| [[KATO III (line)]] | alt | 14.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[LOX-IMVI (line)]] | wt | 13.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 13.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0849× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.212× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 18.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 12.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 9.33 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -9.0) |
| [[SW1417 (line)]] | alt | 13.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.0818× (z -13.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 18.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +11.6) | — |
| [[A498 (line)]] | wt | 9.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +13.4) | — |
| [[CFPAC-1 (line)]] | alt | 8.23 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -11.0) |
| [[Hs 766T (line)]] | wt | 9.15 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.101× (z -10.1) |
| [[HS-578T (line)]] | alt | 14.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -9.0) |
| [[J82 (line)]] | alt | 12.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +11.3) | — |
| [[LS 180 (line)]] | wt | 9.21 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -11.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 9.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +11.2) | — |
| [[SHP-77 (line)]] | alt | 33.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.293× (z -8.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4531), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF180]] | +0.77 | +0.73 / +0.80 | both halves | 7e-06 | same gene group |
| [[KBTBD6]] | +0.75 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[DDX19B]] | +0.74 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[RIOK2]] | +0.73 | +0.64 / +0.79 | both halves | 7e-06 |  |
| [[MRPS31P4]] | +0.73 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[NEPRO]] | +0.72 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ZNF461]] | +0.70 | +0.60 / +0.70 | both halves | 7e-06 | same gene group |
| [[RP9]] | +0.70 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[BBS5]] | +0.70 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[ZNF420]] | +0.70 | +0.64 / +0.68 | both halves | 7e-06 | same gene group |
| [[ZNF567]] | +0.69 | +0.60 / +0.67 | both halves | 7e-06 | same gene group |
| [[TTC26]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP11C]] | -0.71 | -0.57 / -0.70 | both halves | 1e-05 |  |
| [[CCDC200]] | -0.62 | -0.32 / -0.63 | both halves | 2e-04 |  |
| [[PRDM10]] | -0.62 | -0.53 / -0.57 | both halves | 1e-05 | same gene group |
| [[HCFC1]] | -0.58 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[DDX5]] | -0.58 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[CCDC168]] | -0.58 | -0.62 / -0.34 | both halves | 1e-04 |  |
| [[LINC00910]] | -0.57 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[RAB22A]] | -0.56 | -0.52 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF420]] | B | ZNF420 activity raises ZNF45's level | lines that do not express ZNF420 (7) vs lines expressing it (43) | 1.64× lower at baseline in the lines without ZNF420 | 0.024 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF850, ZNF540 |
| [[ZNF571]] | B | ZNF571 activity raises ZNF45's level | lines that do not express ZNF571 (6) vs lines expressing it (44) | 1.66× lower at baseline in the lines without ZNF571 | 0.026 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF420, ZNF850, ZNF540 |
| [[TOP2A]] | B | TOP2A activity raises ZNF45's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF566]] | B | ZNF566 activity raises ZNF45's level | lines that do not express ZNF566 (5) vs lines expressing it (45) | 1.68× lower at baseline in the lines without ZNF566 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZFP14, MPP1, ZNF540 |
| [[IL18]] | B | IL18 activity lowers ZNF45's level | lines that do not express IL18 (18) vs lines expressing it (32) | 1.36× higher at baseline in the lines without IL18 | 0.066 | ⚠ within organs, on part of the lines; also absent: LSR, SPINT2, LAMA3 |
| [[ZNF540]] | B | ZNF540 activity raises ZNF45's level | lines that do not express ZNF540 (5) vs lines expressing it (45) | 1.84× lower at baseline in the lines without ZNF540 | 0.071 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZFP14, ZNF573; maybe low, not absent |
| [[ZNF329]] | B | ZNF329 activity raises ZNF45's level | lines that do not express ZNF329 (7) vs lines expressing it (43) | 1.54× lower at baseline in the lines without ZNF329 | 0.078 | ⚠ within organs, on part of the lines; also absent: C2orf27A |
| [[ZNF573]] | C | ZNF573 activity raises ZNF45's level | lines that do not express ZNF573 (4) vs lines expressing it (46) | 2.19× lower at baseline in the lines without ZNF573 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with FBXW7; also absent: ZNF540, ZNF675, ZNF571; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.758). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-29.7, -2.9); signed map (-19.1, -16.3). **Vector** length 86.9, 17.0% of its response variance represented; |z| ≥ 3 in 958 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +12.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.4 | +6.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.8 | +7.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.0 | +2.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.9 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.1 | -20.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -11.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.8 | -15.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.5 | -11.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -3.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 45 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.31 — chr19:43,912,624-43,935,282 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ZNF13 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02386](https://www.uniprot.org/uniprotkb/Q02386) (Zinc finger protein 45):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7596](https://www.ncbi.nlm.nih.gov/gene/7596):

> Predicted to enable DNA-binding transcription factor activity. Predicted to be involved in DNA-templated transcription and regulation of DNA-templated transcription. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13111](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13111) · Entrez [7596](https://www.ncbi.nlm.nih.gov/gene/7596) · UniProt [Q02386](https://www.uniprot.org/uniprotkb/Q02386) · Ensembl [ENSG00000124459](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124459)

## Data

Gene col 4531: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4531); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4531, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4531]; `tensor/DDL_lfc|DDL_z.npy` [4531]; `embed/gene_vectors.npy` [4531]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4531 or target_col == 4531). Every well: [[ZNF45 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF45.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
