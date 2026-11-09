---
symbol: "MTHFR"
type: "gene"
col: 10778
ensembl_id: "ENSG00000177000"
name: "methylenetetrahydrofolate reductase"
location: "1p36.22"
module: 4
arm: "-"
pooled_cpm: 25.54
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 21
n_dd_up_clean: 27
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# MTHFR

*methylenetetrahydrofolate reductase* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.88× (z +19.4, q 0e+00, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.541× (z -8.0, q 6e-13, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INAFM1]] (+0.67, fdr 7e-06), [[ZMYM5]] (+0.65, fdr 7e-06), [[JUND]] (+0.62, fdr 7e-06); moves opposite to [[IPO5]] (-0.70, fdr 7e-06), [[NAE1]] (-0.66, fdr 7e-06), [[HACD3]] (-0.63, fdr 2e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TYMP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 1 with an alert ⚠; shown: the 15 strongest. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10778.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.88×** | +19.4 | 0e+00 | 35/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.37×** | +11.2 | 2e-26 | 29/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +7.4 | 2e-11 | 26/47 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.67×** | +6.7 | 4e-09 | 30/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.4 | 1e-08 | 23/46 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +6.4 | 2e-08 | 25/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.39×** | +6.0 | 2e-07 | 23/48 (NCI-H23, C-33 A, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.49×** | +5.2 | 2e-05 | 29/47 (AsPC-1, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +4.7 | 1e-04 | 20/48 (SW480, SW1417, …) | top dose only |  |
| [[Berbamine (drug)]] 5 µM |  | **1.29×** | +4.7 | 1e-04 | 25/49 (NCI-H23, KATO III, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +4.2 | 0.001 | 20/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.002 | 20/47 (KATO III, LS 180, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.004 | 20/47 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ritonavir (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.004 | 14/48 (KATO III, HT-29, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.004 | 17/47 (Panc 03.27, C-33 A, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10778.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.541×** | -8.0 | 6e-13 | 34/47 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.591×** | -6.9 | 2e-09 | 26/46 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.383×** | -6.5 | 1e-08 | 30/45 (PANC-1, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.619×** | -6.3 | 5e-08 | 25/48 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.644×** | -5.8 | 1e-06 | 27/47 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.649×** | -5.6 | 2e-06 | 28/47 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.655×** | -5.5 | 2e-06 | 27/47 (CFPAC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.655×** | -5.5 | 2e-06 | 27/47 (H4, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.663×** | -5.4 | 5e-06 | 24/47 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.658×** | -5.0 | 3e-05 | 24/38 (CFPAC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.698×** | -4.5 | 3e-04 | 24/44 (LoVo, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.788×** | -4.4 | 5e-04 | 25/48 (SW 900, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.726×** | -3.9 | 0.005 | 17/47 (SW1417, J82, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.773×** | -3.4 | 0.030 | 14/48 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.772×** | -3.3 | 0.042 | 19/33 (KATO III, Panc 03.27, …) | inconsistent across doses | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.769×** | -3.2 | 0.042 | 14/48 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.776×** | -3.2 | 0.048 | 17/47 (LoVo, NCI-H1573, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.637×** | -3.1 | 0.063 | 18/49 (HT-29, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10778. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 97.1 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -13.2) |
| [[MIA PaCa-2 (line)]] | alt | 16.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +17.8) | — |
| [[HS-578T (line)]] | alt | 7.86 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.0467× (z -12.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 43.3 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.213× (z -12.7) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 19.1 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.127× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 19.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.12× (z +20.0) | — |
| [[PANC-1 (line)]] | alt | 29.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.09× (z +21.1) | — |
| [[SW 900 (line)]] | alt | 24.8 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.257× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 29.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +10.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0717× (z -12.5) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 53.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +13.6) | — |
| [[NCI-H23 (line)]] | alt | 33.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +15.2) | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[Panc 03.27 (line)]] | alt | 31.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 10.4 | 0 | 2 (2 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.100× (z -9.5) ⚠ toxic |
| [[SW480 (line)]] | alt | 19.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +14.6) | — |
| [[A-172 (line)]] | wt | 12.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +11.2) | — |
| [[A-427 (line)]] | wt | 54.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -15.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 16.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 23.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +9.4) | — |
| [[C32 (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[COLO 205 (line)]] | alt | 26.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +12.5) | — |
| [[H4 (line)]] | wt | 10.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0640× (z -9.4) |
| [[HCT15 (line)]] | alt | 20.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 12.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +12.0) | — |
| [[Hs 766T (line)]] | wt | 33.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 46.7 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.297× (z -9.0) |
| [[J82 (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +11.8) | — |
| [[KATO III (line)]] | alt | 40.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 9.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 17.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +13.9) | — |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 9.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.26× (z +14.8) | — |
| [[A498 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10778), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*35 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INAFM1]] | +0.67 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[ZMYM5]] | +0.65 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[JUND]] | +0.62 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[ACAP1]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[NFKBIL1]] | +0.60 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[TMEM205]] | +0.59 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[TP53INP2]] | +0.59 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[MED19]] | +0.59 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[ZFAND2B]] | +0.59 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[OFD1]] | +0.59 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[MIDN]] | +0.59 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[POLD4]] | +0.59 | +0.40 / +0.63 | both halves | 5e-05 |  |

## Genes that move opposite

*65 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO5]] | -0.70 | -0.68 / -0.73 | both halves | 7e-06 |  |
| [[NAE1]] | -0.66 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[HACD3]] | -0.63 | -0.73 / -0.46 | both halves | 2e-05 |  |
| [[EEF1E1]] | -0.63 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[RPE]] | -0.62 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[FAM136A]] | -0.62 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[PPT1]] | -0.62 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[CSE1L]] | -0.62 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[NAA50]] | -0.62 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[PRKDC]] | -0.61 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[GMPS]] | -0.61 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[NUP155]] | -0.61 | -0.57 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TYMP]] | B | TYMP activity raises MTHFR's level | lines that do not express TYMP (20) vs lines expressing it (30) | 1.55× lower at baseline in the lines without TYMP | 0.039 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |
| [[TRIM15]] | B | TRIM15 activity raises MTHFR's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 1.58× lower at baseline in the lines without TRIM15 | 0.043 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[CRTAP]] | C | CRTAP activity lowers MTHFR's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.66× higher at baseline in the lines without CRTAP | 0.065 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.592). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-24.8, -29.4); signed map (-7.8, 6.6). **Vector** length 117, 32.3% of its response variance represented; |z| ≥ 3 in 1,037 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.3 | +19.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +11.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +4.5 | +5.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +3.6 | +6.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.5 | +7.4 |
|  | [[Berbamine (drug)]] 5 µM |  | +3.5 | +4.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.4 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +3.0 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.8 | -4.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.3 | -5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -4.2 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.0 | -5.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.8 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -5.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.2 | -3.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | methylenetetrahydrofolate reductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:11,785,723-11,806,455 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Flavoproteins; Oxidoreductases |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 3 pathways, smallest: Metabolism of folate and pterines; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [P42898](https://www.uniprot.org/uniprotkb/P42898) (Methylenetetrahydrofolate reductase):

> Catalyzes the conversion of 5,10-methylenetetrahydrofolate to 5-methyltetrahydrofolate, a cosubstrate for homocysteine remethylation to methionine. Represents a key regulatory connection between the folate and methionine cycles (Probable).

**Summary**, from NCBI Gene [4524](https://www.ncbi.nlm.nih.gov/gene/4524):

> The protein encoded by this gene catalyzes the conversion of 5,10-methylenetetrahydrofolate to 5-methyltetrahydrofolate, a co-substrate for homocysteine remethylation to methionine. Genetic variation in this gene influences susceptibility to occlusive vascular disease, neural tube defects, colon cancer and acute leukemia, and mutations in this gene are associated with methylenetetrahydrofolate reductase deficiency.[provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:7436](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7436) · Entrez [4524](https://www.ncbi.nlm.nih.gov/gene/4524) · UniProt [P42898](https://www.uniprot.org/uniprotkb/P42898) · Ensembl [ENSG00000177000](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177000)

## Data

Gene col 10778: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10778); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10778, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10778]; `tensor/DDL_lfc|DDL_z.npy` [10778]; `embed/gene_vectors.npy` [10778]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10778 or target_col == 10778). Every well: [[MTHFR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTHFR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
