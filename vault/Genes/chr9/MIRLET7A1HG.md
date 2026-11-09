---
symbol: "MIRLET7A1HG"
type: "gene"
col: 15642
ensembl_id: "ENSG00000269929"
name: "miRlet-7a-1/let-7f-1/let-7d cluster host gene"
location: "9q22.32"
module: 83
arm: "+"
pooled_cpm: 45.4
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# MIRLET7A1HG

*miRlet-7a-1/let-7f-1/let-7d cluster host gene* — 9q22.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.60× (z +6.7, q 1e-08, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.252× (z -19.2, q 0e+00, down in 38 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.457× (z -11.3, q 2e-27, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR1C]] (+0.72, fdr 7e-06), [[THUMPD3-AS1]] (+0.67, fdr 2e-05), [[PCBP1-AS1]] (+0.65, fdr 3e-05); moves opposite to [[GDE1]] (-0.59, fdr 4e-05), [[HERC1]] (-0.59, fdr 2e-05), [[HTT]] (-0.57, fdr 5e-05).
> It sits in the **+** arm of [[Module 083]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15642.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +6.7 | 1e-08 | 37/48 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +6.1 | 2e-07 | 32/47 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +5.6 | 4e-06 | 35/48 (HOP62, SNU-423, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +5.1 | 4e-05 | 33/48 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +4.4 | 0.001 | 28/48 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +4.2 | 0.002 | 25/47 (SNU-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15642.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.252×** | -19.2 | 0e+00 | 38/41 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.280×** | -17.7 | 0e+00 | 45/49 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.457×** | -11.3 | 2e-27 | 46/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.486×** | -10.4 | 3e-23 | 44/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.499×** | -10.0 | 1e-21 | 46/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.579×** | -7.9 | 2e-13 | 44/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.635×** | -6.6 | 4e-09 | 35/48 (hTERT-HPNE, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.665×** | -5.9 | 2e-07 | 36/48 (HepG2/C3A, H4, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.697×** | -5.0 | 3e-05 | 29/47 (NCI-H2347, A-427, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.708×** | -4.8 | 7e-05 | 27/48 (NCI-H2347, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.562×** | -4.4 | 7e-04 | 30/49 (NCI-H23, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.839× | -3.6 | 0.013 | 23/48 (RKO, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.780×** | -3.6 | 0.013 | 22/48 (J82, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15642. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 80.6 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.310× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 45.9 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -19.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 36.0 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.295× (z -11.3) |
| [[A-172 (line)]] | wt | 66.3 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.0436× (z -28.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 73.2 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.366× (z -9.8) |
| [[SW480 (line)]] | alt | 50.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -23.5) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.432× (z -9.8) |
| [[A-427 (line)]] | wt | 45.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.340× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 51.2 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0581× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.294× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 55.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.358× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 37.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -14.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 39.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 54.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -18.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 53.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -21.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 35.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -9.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 36.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0640× (z -17.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 52.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -11.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 53.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -14.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 43.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0627× (z -19.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 39.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0686× (z -17.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 45.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -11.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 40.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -11.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 60.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -12.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 39.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0919× (z -13.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -8.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 43.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -12.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 50.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0914× (z -15.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 53.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0816× (z -15.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 37.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0836× (z -14.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 54.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -11.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 45.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -9.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 38.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -13.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 33.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -16.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 35.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0578× (z -21.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 25.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.295× (z -8.6) |
| [[RKO (line)]] | wt | 75.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 42.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -8.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15642), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR1C]] | +0.72 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[THUMPD3-AS1]] | +0.67 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[PCBP1-AS1]] | +0.65 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[C2orf49-DT]] | +0.63 | +0.28 / +0.58 | both halves | 3e-04 |  |
| [[ZNF26]] | +0.63 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[SMIM15-AS1]] | +0.63 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[MSANTD2]] | +0.63 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[CENPL]] | +0.62 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[ZKSCAN2-DT]] | +0.62 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[ARMC5]] | +0.60 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[MIRLET7IHG]] | +0.60 | +0.45 / +0.47 | both halves | 3e-05 | same gene group |
| [[MPDU1]] | +0.59 | +0.37 / +0.45 | both halves | 7e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDE1]] | -0.59 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[HERC1]] | -0.59 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[HTT]] | -0.57 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[ATP5F1C]] | -0.56 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[AKTIP]] | -0.55 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[CAT]] | -0.53 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[SERAC1]] | -0.53 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[TTBK2]] | -0.52 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[NDRG3]] | -0.52 | -0.43 / -0.29 | both halves | 2e-04 |  |
| [[STX7]] | -0.52 | -0.32 / -0.34 | both halves | 2e-04 |  |
| [[NSFL1C]] | -0.51 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[ARL3]] | -0.51 | -0.32 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.631). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.6, 9.0); signed map (15.4, 0.2). **Vector** length 97.3, 25.5% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.9 | +5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +7.4 | +2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.3 | +1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +0.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +2.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.4 | +0.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.8 | -0.6 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.7 | -11.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.4 | -5.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.4 | -7.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.8 | -4.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | -3.5 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.8 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | miRlet-7a-1/let-7f-1/let-7d cluster host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 9q22.32 — chr9:94,166,258-94,200,905 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [112903833](https://www.ncbi.nlm.nih.gov/gene/112903833):

> Predicted to be involved in miRNA-mediated post-transcriptional gene silencing. Predicted to be part of RISC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:53970](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53970) · Entrez [112903833](https://www.ncbi.nlm.nih.gov/gene/112903833) · Ensembl [ENSG00000269929](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000269929)

## Data

Gene col 15642: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15642); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15642, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15642]; `tensor/DDL_lfc|DDL_z.npy` [15642]; `embed/gene_vectors.npy` [15642]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15642 or target_col == 15642). Every well: [[MIRLET7A1HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIRLET7A1HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
