---
symbol: "ANKZF1"
type: "gene"
col: 8706
ensembl_id: "ENSG00000163516"
name: "ankyrin repeat and zinc finger peptidyl tRNA hydrolase 1"
location: "2q35"
module: 79
arm: "+"
pooled_cpm: 43.93
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 20
n_dd_up_clean: 10
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# ANKZF1

*ankyrin repeat and zinc finger peptidyl tRNA hydrolase 1* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.65× (z +11.9, q 1e-29, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.440× (z -19.3, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NARF]] (+0.75, fdr 7e-06), [[KDM3A]] (+0.71, fdr 7e-06), [[CNOT8]] (+0.68, fdr 7e-06); moves opposite to [[COA7]] (-0.62, fdr 7e-06), [[ZMYM4]] (-0.62, fdr 1e-05), [[COMMD10]] (-0.61, fdr 1e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8706.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +11.9 | 1e-29 | 39/48 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +7.3 | 8e-11 | 35/49 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +6.2 | 9e-08 | 30/48 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +6.1 | 2e-07 | 29/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +5.8 | 8e-07 | 28/48 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +5.0 | 5e-05 | 26/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.9 | 7e-05 | 28/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Pimitespib (drug)]] 5 µM |  | **1.51×** | +3.6 | 0.025 | 13/47 (HS-578T, SK-MEL-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.028 | 14/48 (HEC-1-A, A-172, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.029 | 20/48 (NCI-H23, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | 1.14× | +3.1 | 0.086 | 14/48 (Hs 766T, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8706.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.440×** | -19.3 | 0e+00 | 41/47 (SK-MEL-2, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.436×** | -13.3 | 1e-37 | 43/48 (SK-MEL-2, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.484×** | -11.6 | 7e-29 | 34/40 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.538×** | -10.3 | 1e-22 | 39/48 (NCI-H2030, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.329×** | -9.7 | 5e-20 | 39/49 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.577×** | -9.2 | 5e-18 | 45/48 (SW1417, A498, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.593×** | -8.7 | 3e-16 | 33/47 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.598×** | -8.2 | 2e-14 | 30/47 (C-33 A, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.463×** | -6.7 | 1e-09 | 32/48 (LOX-IMVI, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.679×** | -5.9 | 2e-07 | 27/43 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.545×** | -5.3 | 7e-06 | 34/48 (A498, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.739×** | -5.0 | 2e-05 | 31/48 (AsPC-1, BT-474, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.610×** | -4.3 | 7e-04 | 28/48 (A498, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.777×** | -4.0 | 0.002 | 22/48 (NCI-H23, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.791×** | -3.9 | 0.004 | 22/48 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.645×** | -3.8 | 0.005 | 19/47 (HEC-1-A, A498, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.664×** | -3.6 | 0.012 | 20/48 (SK-MEL-2, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.666×** | -3.5 | 0.012 | 19/48 (SW 1271, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.818×** | -3.3 | 0.024 | 19/48 (C32, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8706. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 78.4 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -20.2) |
| [[NCI-H1573 (line)]] | alt | 43.2 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -15.5) |
| [[PANC-1 (line)]] | alt | 33.3 | 2 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -16.1) |
| [[CFPAC-1 (line)]] | alt | 51.2 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.218× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.408× (z -13.3) |
| [[MIA PaCa-2 (line)]] | alt | 45.3 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +11.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -16.2) |
| [[NCI-H2030 (line)]] | alt | 49.8 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.311× (z -14.9) |
| [[NCI-H460 (line)]] | wt | 48.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -15.4) |
| [[RPMI-7951 (line)]] | alt | 58.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -16.9) |
| [[SK-MEL-2 (line)]] | alt | 58.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0801× (z -31.3) |
| [[COLO 205 (line)]] | alt | 46.7 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.182× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 60.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 58.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -16.4) |
| [[SNU-423 (line)]] | alt | 58.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -18.5) |
| [[SW 900 (line)]] | alt | 53.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -20.8) |
| [[AsPC-1 (line)]] | alt | 48.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -19.5) |
| [[H4 (line)]] | wt | 39.3 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.205× (z -8.8) |
| [[HCT15 (line)]] | alt | 73.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 66.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -13.6) |
| [[Hs 766T (line)]] | wt | 37.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.377× (z -9.3) |
| [[HT-29 (line)]] | alt | 46.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 33.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -11.8) |
| [[Panc 03.27 (line)]] | alt | 45.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -10.1) |
| [[A-172 (line)]] | wt | 44.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -15.4) |
| [[A-427 (line)]] | wt | 22.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.157× (z -11.1) ⚠ toxic |
| [[A498 (line)]] | wt | 32.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.305× (z -10.0) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 40.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.103× (z -9.7) ⚠ toxic |
| [[BT-474 (line)]] | alt | 40.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -9.7) |
| [[C-33 A (line)]] | alt | 42.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0994× (z -14.3) ⚠ toxic |
| [[HOP62 (line)]] | alt | 46.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -10.4) |
| [[HS-578T (line)]] | alt | 27.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.300× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 34.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -8.8) |
| [[J82 (line)]] | alt | 34.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -8.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 40.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 27.4 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0517× (z -11.6) |
| [[LS 180 (line)]] | wt | 53.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -14.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 43.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.281× (z -9.7) |
| [[SHP-77 (line)]] | alt | 49.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -10.0) |
| [[SW1417 (line)]] | alt | 44.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.257× (z -12.2) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 35.6 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.128× (z -10.8) |
| [[SW480 (line)]] | alt | 42.6 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.219× (z -8.5) |
| [[A549 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8706), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NARF]] | +0.75 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[KDM3A]] | +0.71 | +0.70 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[CNOT8]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[KDM4B]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[ANKRD37]] | +0.64 | +0.59 / +0.66 | both halves | 7e-06 | same gene group |
| [[HDAC3]] | +0.63 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[SAP30-DT]] | +0.63 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[UNC119]] | +0.63 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[FBXO42]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[KMT5C]] | +0.62 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[SH3D21]] | +0.62 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[RBPJ]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COA7]] | -0.62 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[ZMYM4]] | -0.62 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[COMMD10]] | -0.61 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[ABCE1]] | -0.59 | -0.52 / -0.57 | both halves | 1e-05 | pathway: Ribosome-associated quality control; STRING 549 |
| [[FKTN]] | -0.59 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[CEP41]] | -0.58 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[TRIM44]] | -0.57 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[STAG1]] | -0.57 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[UTP20]] | -0.57 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[SFPQ]] | -0.57 | -0.35 / -0.61 | both halves | 1e-04 |  |
| [[DDX10]] | -0.56 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[RRP15]] | -0.56 | -0.47 / -0.59 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ANKZF1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TCAF2]] | C | TCAF2 activity raises ANKZF1's level | lines that do not express TCAF2 (4) vs lines expressing it (46) | 1.46× lower at baseline in the lines without TCAF2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.661). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.2, -17.0); signed map (-34.9, 22.9). **Vector** length 132, 38.3% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.56 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +7.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +11.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +2.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.1 | +2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +1.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.7 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -11.8 | -19.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -10.9 | -11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -9.9 | -10.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.9 | -13.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.9 | -5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.9 | -6.7 |
|  | [[EX229 (drug)]] 5 µM |  | -4.7 | -5.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.3 | -4.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.2 | -3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and zinc finger peptidyl tRNA hydrolase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:219,229,783-219,236,679 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10415, ZNF744, Vms1 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Ankyrin repeat domain containing |
| Hallmark sets | GLYCOLYSIS, HYPOXIA |
| Reactome | 3 pathways, smallest: Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide; Ribosome-associated quality control; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H8Y5](https://www.uniprot.org/uniprotkb/Q9H8Y5) (tRNA endonuclease ANKZF1):

> Endonuclease that cleaves polypeptidyl-tRNAs downstream of the ribosome-associated quality control (RQC) pathway to release incompletely synthesized polypeptides for degradation. The RQC pathway disassembles aberrantly stalled translation complexes to recycle or degrade the constituent parts. ANKZF1 acts downstream disassembly of stalled ribosomes and specifically cleaves off the terminal 3'-CCA nucleotides universal to all tRNAs from polypeptidyl-tRNAs, releasing (1) ubiquitinated polypeptides …

**Summary**, from NCBI Gene [55139](https://www.ncbi.nlm.nih.gov/gene/55139):

> Enables RNA endonuclease activity and catalytic activity, acting on a tRNA. Involved in cellular response to hydrogen peroxide; protein quality control for misfolded or incompletely synthesized proteins; and rescue of stalled cytosolic ribosome. Located in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25527](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25527) · Entrez [55139](https://www.ncbi.nlm.nih.gov/gene/55139) · UniProt [Q9H8Y5](https://www.uniprot.org/uniprotkb/Q9H8Y5) · Ensembl [ENSG00000163516](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163516)

## Data

Gene col 8706: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8706); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8706, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8706]; `tensor/DDL_lfc|DDL_z.npy` [8706]; `embed/gene_vectors.npy` [8706]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8706 or target_col == 8706). Every well: [[ANKZF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKZF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
