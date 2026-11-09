---
symbol: "FBXO7"
type: "gene"
col: 1896
ensembl_id: "ENSG00000100225"
name: "F-box protein 7"
location: "22q12.3"
module: 171
arm: "+"
pooled_cpm: 47.6
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# FBXO7

*F-box protein 7* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.44× (z +5.1, q 2e-04, up in 28 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.94× (z +5.0, q 2e-04, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.515× (z -9.4, q 4e-18, down in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Celecoxib (drug)]] 0.5 µM: 0.727× (z -3.2, q 0.066, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (C32 0.268×, AsPC-1 0.376×, Hs 766T 0.438×; ⚠ cell-cycle shift, explains ~27% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (hTERT-HPNE 0.301×, NCI-H1792 0.380×, Hs 766T 0.450×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (SW480 0.378×, KATO III 0.343×, Hs 766T 0.332×; ⚠ cell-cycle shift, explains ~33% of this change); [[Oleic acid (drug)]] 0.05 µM in 1 line (NCI-H661 0.0505×); [[Elimusertib hydrochloride (drug)]] 0.5 µM in 1 line (NCI-H596 0.412×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (AN3 CA 0.158×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPP30]] (+0.70, fdr 7e-06), [[MRS2]] (+0.69, fdr 7e-06), [[HSF2]] (+0.68, fdr 1e-05); moves opposite to [[KCNJ14]] (-0.65, fdr 7e-06), [[NABP1]] (-0.62, fdr 7e-06), [[ERCC1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1896.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +5.1 | 2e-04 | 28/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.94×** | +5.0 | 2e-04 | 32/48 (SW480, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +4.8 | 3e-04 | 29/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +4.6 | 5e-04 | 25/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.75×** | +4.2 | 0.003 | 26/49 (SW480, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.004 | 26/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.016 | 22/48 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +3.6 | 0.021 | 25/48 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.049 | 16/48 (SW480, SNU-423, …) | rises with dose | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 11 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1896.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (C32 0.268×, AsPC-1 0.376×, Hs 766T 0.438×; ⚠ cell-cycle shift, explains ~27% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (hTERT-HPNE 0.301×, NCI-H1792 0.380×, Hs 766T 0.450×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (SW480 0.378×, KATO III 0.343×, Hs 766T 0.332×; ⚠ cell-cycle shift, explains ~33% of this change); [[Oleic acid (drug)]] 0.05 µM in 1 line (NCI-H661 0.0505×); [[Elimusertib hydrochloride (drug)]] 0.5 µM in 1 line (NCI-H596 0.412×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (AN3 CA 0.158×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.515×** | -9.4 | 4e-18 | 44/48 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.527×** | -9.0 | 4e-17 | 44/48 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.620×** | -6.7 | 3e-09 | 39/48 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.725×** | -6.4 | 2e-08 | 33/48 (C32, AsPC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.690×** | -5.0 | 6e-05 | 31/48 (C32, HS-578T, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.705×** | -4.9 | 8e-05 | 27/48 (A-427, COLO 205, …) | two highest doses | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.725×** | -4.4 | 0.001 | 27/49 (C32, AsPC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.739×** | -4.3 | 0.001 | 25/48 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **0.730×** | -4.2 | 0.001 | 24/40 (CHP-212, C32, …) | two highest doses | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.818×** | -4.0 | 0.004 | 27/48 (NCI-H2347, SNU-423, …) | rises with dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.727×** | -3.2 | 0.066 | 18/48 (KATO III, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.796×** | -3.2 | 0.066 | 19/48 (SNU-423, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1896. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 214 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -13.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Hs 766T (line)]] | wt | 113 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -10.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H460 (line)]] | wt | 34.5 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.92× (z +10.7) | — |
| [[SW480 (line)]] | alt | 54.3 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.378× (z -11.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[AsPC-1 (line)]] | alt | 41.3 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -11.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[KATO III (line)]] | alt | 48.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.48× (z +8.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.343× (z -10.4) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 29.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[A549 (line)]] | wt | 38.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.365× (z -8.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[AN3 CA (line)]] | alt | 66.6 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.158× (z -8.9) |
| [[BT-474 (line)]] | alt | 32.2 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.298× (z -8.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[CHP-212 (line)]] | wt | 76.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0953× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[COLO 205 (line)]] | alt | 40.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[hTERT-HPNE (line)]] | wt | 48.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 46.1 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.17× (z +10.4) ⚠ toxic | — |
| [[LS 180 (line)]] | wt | 53.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 41.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 56.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.339× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H596 (line)]] | alt | 55.8 | 0 | 1 | — | [[Elimusertib hydrochloride (drug)]] 0.5 µM 0.412× (z -10.4) |
| [[NCI-H661 (line)]] | alt | 48.4 | 0 | 1 | — | [[Oleic acid (drug)]] 0.05 µM 0.0505× (z -11.1) |
| [[A-172 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 95.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 69.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 54.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1896), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP30]] | +0.70 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[MRS2]] | +0.69 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[HSF2]] | +0.68 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[COPS7B]] | +0.65 | +0.67 / +0.67 | both halves | 7e-06 | pathway: Neddylation; STRING 470 |
| [[GNPDA2]] | +0.64 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[TMEM183A]] | +0.64 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[RAD23B]] | +0.64 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[KDM1A]] | +0.64 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[CDC40]] | +0.64 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[KCTD3]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[FHIP2A]] | +0.63 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[RTCA]] | +0.63 | +0.72 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNJ14]] | -0.65 | -0.66 / -0.71 | both halves | 7e-06 |  |
| [[NABP1]] | -0.62 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[ERCC1]] | -0.60 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[ATG7]] | -0.59 | -0.60 / -0.43 | both halves | 3e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[BLZF2P]] | -0.59 | -0.40 / -0.68 | both halves | 5e-05 |  |
| [[SLC20A2]] | -0.58 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[DMPK]] | -0.57 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[CFAP251]] | -0.57 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[CRK]] | -0.56 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[WNT2B]] | -0.56 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[MYL12A]] | -0.56 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[C11orf91]] | -0.56 | -0.46 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises FBXO7's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.775). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (-7.7, -9.9); signed map (-31.4, -16.6). **Vector** length 85.9, 20.6% of its response variance represented; |z| ≥ 3 in 889 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.7 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.5 | -1.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | +4.4 | -4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | +4.4 | -4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +4.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.9 | +1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.8 | +0.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | +1.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | +2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.4 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | +3.7 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -1.8 | -1.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -0.5 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | -1.7 | -1.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.6 | -1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:32,474,676-32,498,829 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FBX7, Fbx, PARK15 |
| Gene groups (HGNC) | F-boxes other |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3I1](https://www.uniprot.org/uniprotkb/Q9Y3I1) (F-box only protein 7):

> Substrate recognition component of a SCF (SKP1-CUL1-F-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins and plays a role in several biological processes such as cell cycle, cell proliferation, or maintenance of chromosome stability. Recognizes and ubiquitinates BIRC2 and the cell cycle regulator DLGAP5. Plays a role downstream of PINK1 in the clearance of damaged mitochondria via selective autophagy …

**Summary**, from NCBI Gene [25793](https://www.ncbi.nlm.nih.gov/gene/25793):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of the ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:13586](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13586) · Entrez [25793](https://www.ncbi.nlm.nih.gov/gene/25793) · UniProt [Q9Y3I1](https://www.uniprot.org/uniprotkb/Q9Y3I1) · Ensembl [ENSG00000100225](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100225)

## Data

Gene col 1896: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1896); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1896, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1896]; `tensor/DDL_lfc|DDL_z.npy` [1896]; `embed/gene_vectors.npy` [1896]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1896 or target_col == 1896). Every well: [[FBXO7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
