---
symbol: "RBM7"
type: "gene"
col: 1142
ensembl_id: "ENSG00000076053"
name: "RNA binding motif protein 7"
location: "11q23.1-q23.2"
module: 2
arm: "-"
pooled_cpm: 34.84
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 16
n_dd_up_clean: 9
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# RBM7

*RNA binding motif protein 7* — 11q23.1-q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.17× (z +12.3, q 3e-32, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.413× (z -14.1, q 2e-42, down in 31 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.451× (z -13.2, q 3e-37, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR2M]] (+0.65, fdr 1e-05), [[NDUFA5]] (+0.64, fdr 9e-06), [[PLEKHF2]] (+0.64, fdr 8e-06); moves opposite to [[CORO7]] (-0.65, fdr 1e-05), [[GNA12]] (-0.63, fdr 1e-05), [[PITPNA]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1142.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.17×** | +12.3 | 3e-32 | 45/48 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +11.5 | 7e-28 | 37/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.21×** | +10.1 | 1e-21 | 40/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +9.7 | 3e-20 | 39/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.69×** | +8.7 | 4e-16 | 38/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +7.5 | 6e-12 | 36/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +7.3 | 2e-11 | 36/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +6.5 | 5e-09 | 24/42 (PANC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +5.0 | 3e-05 | 0/48 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +4.9 | 6e-05 | 25/46 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +4.2 | 0.001 | 20/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.2 | 0.001 | 14/33 (NCI-H2030, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +4.2 | 0.001 | 23/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.3 | 0.038 | 18/47 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1142.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.413×** | -14.1 | 2e-42 | 31/35 (KATO III, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.451×** | -13.2 | 3e-37 | 47/48 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.457×** | -13.0 | 3e-36 | 45/48 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.514×** | -11.0 | 4e-26 | 42/48 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.603×** | -8.4 | 5e-15 | 31/45 (NCI-H2347, KATO III, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.711×** | -8.0 | 1e-13 | 34/48 (H4, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.652×** | -7.1 | 1e-10 | 36/48 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.747×** | -4.7 | 2e-04 | 23/47 (A498, AN3 CA, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.830×** | -4.4 | 7e-04 | 18/48 (SW1417, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.831×** | -4.4 | 7e-04 | 25/48 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.764×** | -4.3 | 8e-04 | 22/48 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.710×** | -4.1 | 0.002 | 19/47 (PANC-1, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.647×** | -3.8 | 0.007 | 19/48 (LoVo, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.805×** | -3.6 | 0.012 | 17/48 (NCI-H460, SW1417, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.817×** | -3.4 | 0.028 | 17/48 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.818×** | -3.4 | 0.028 | 16/48 (A549, NCI-H2347, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.874× | -3.2 | 0.048 | 14/48 (CFPAC-1, LoVo, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.876× | -3.1 | 0.052 | 9/48 (A549, HT-29, …) | rises with dose | position effect removed |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.835× | -3.0 | 0.075 | 7/48 (NCI-H2030, RKO, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1142. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 36.8 | 8 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.50× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.445× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.460× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 21.8 | 6 (4 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.87× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.312× (z -10.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 37.5 | 2 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.34× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.399× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.414× (z -10.2) |
| [[A498 (line)]] | wt | 30.7 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 55.4 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.278× (z -11.1) |
| [[KATO III (line)]] | alt | 53.7 | 1 | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.53× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.0697× (z -24.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.371× (z -9.4) |
| [[LoVo (line)]] | wt | 37.0 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.63× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.356× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 50.0 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.342× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 63.4 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.355× (z -9.8) |
| [[SW1417 (line)]] | alt | 56.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.376× (z -9.6) |
| [[AN3 CA (line)]] | alt | 55.2 | 0 | 2 (1 ⚠) | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0687× (z -11.7) |
| [[H4 (line)]] | wt | 40.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -15.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.225× (z -8.9) |
| [[HCT15 (line)]] | alt | 22.8 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.106× (z -12.2) |
| [[HEC-1-A (line)]] | alt | 24.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HepG2_C3A (line)]] | wt | 39.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -9.2) |
| [[Hs 766T (line)]] | wt | 46.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.368× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 33.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 4.05× (z +10.2) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.0594× (z -21.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 36.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 24.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.1) | — |
| [[A549 (line)]] | wt | 28.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 30.1 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.183× (z -10.2) ⚠ toxic |
| [[HOP62 (line)]] | alt | 21.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -8.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 36.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 35.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -17.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 20.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 51.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -10.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 44.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.301× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 40.3 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.270× (z -9.4) |
| [[SW48 (line)]] | wt | 24.3 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0857× (z -11.8) |
| [[A-427 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1142), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2M]] | +0.65 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[NDUFA5]] | +0.64 | +0.69 / +0.57 | both halves | 9e-06 |  |
| [[PLEKHF2]] | +0.64 | +0.58 / +0.57 | both halves | 8e-06 |  |
| [[COPS5]] | +0.64 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[ZXDA]] | +0.63 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[ZNF181]] | +0.62 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[PEX12]] | +0.62 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[TLR3]] | +0.62 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[PSMB8]] | +0.62 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[NCOA4]] | +0.62 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[CLN5]] | +0.62 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[ZXDB]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CORO7]] | -0.65 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[GNA12]] | -0.63 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[PITPNA]] | -0.63 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[DAP3]] | -0.63 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[SLC27A4]] | -0.63 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[MYO9B]] | -0.62 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[TCF3]] | -0.62 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[TPST2]] | -0.61 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[ARPC1B]] | -0.61 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[CTNNBIP1]] | -0.60 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[AP3M2]] | -0.60 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[FOXK2]] | -0.60 | -0.53 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RBM7's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **-** arm (projection on the module's main direction -0.437). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-17.0, 7.5); signed map (8.5, -26.3). **Vector** length 86.0, 20.8% of its response variance represented; |z| ≥ 3 in 1,137 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +7.6 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.8 | +9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +11.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +8.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.1 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.3 | +1.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.0 | +0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.8 | +1.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | +2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | +4.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.4 | -13.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | +4.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.2 | -11.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | +1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | -4.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -0.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.1-q23.2 — chr11:114,400,030-114,414,203 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RNA binding motif containing; Nuclear exosome targeting complex |
| Reactome | 8 pathways, smallest: Regulation of endogenous retroelements by the Human Silencing Hub (HUSH) complex; Nuclear RNA decay; Regulation of endogenous retroelements |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y580](https://www.uniprot.org/uniprotkb/Q9Y580) (RNA-binding protein 7):

> RNA-binding subunit of the trimeric nuclear exosome targeting (NEXT) complex, a complex that functions as an RNA exosome cofactor that directs a subset of non-coding short-lived RNAs for exosomal degradation. NEXT is involved in surveillance and turnover of aberrant transcripts and non-coding RNAs. Binds preferentially polyuridine sequences and associates with newly synthesized RNAs, including pre-mRNAs and short-lived exosome substrates such as promoter upstream transcripts (PROMPTs), enhancer …

**Summary**, from NCBI Gene [10179](https://www.ncbi.nlm.nih.gov/gene/10179):

> Enables 14-3-3 protein binding activity; pre-mRNA intronic binding activity; and snRNA binding activity. Involved in snRNA catabolic process. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9904](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9904) · Entrez [10179](https://www.ncbi.nlm.nih.gov/gene/10179) · UniProt [Q9Y580](https://www.uniprot.org/uniprotkb/Q9Y580) · Ensembl [ENSG00000076053](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076053)

## Data

Gene col 1142: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1142); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1142, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1142]; `tensor/DDL_lfc|DDL_z.npy` [1142]; `embed/gene_vectors.npy` [1142]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1142 or target_col == 1142). Every well: [[RBM7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
