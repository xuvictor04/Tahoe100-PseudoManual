---
symbol: "POP1"
type: "gene"
col: 2447
ensembl_id: "ENSG00000104356"
name: "POP1 ribonuclease P/MRP subunit"
location: "8q22.2"
module: 4
arm: "+"
pooled_cpm: 11.63
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 9
n_dd_up_clean: 23
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# POP1

*POP1 ribonuclease P/MRP subunit* — 8q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (9 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 3.89× (z +21.0, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.590× (z -11.6, q 3e-28, down in 30 of 44 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.612× (z -7.3, q 7e-11, down in 24 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC123]] (+0.71, fdr 7e-06), [[CCT3]] (+0.70, fdr 7e-06), [[INVS]] (+0.70, fdr 7e-06); moves opposite to [[SMIM14]] (-0.66, fdr 8e-06), [[CHD2]] (-0.64, fdr 7e-06), [[CYLD]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2447.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.89×** | +21.0 | 0e+00 | 44/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.92×** | +15.6 | 0e+00 | 40/45 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.70×** | +15.3 | 0e+00 | 40/47 (HOP62, C32, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.27×** | +12.7 | 1e-34 | 42/47 (A498, NCI-H460, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.95×** | +10.3 | 5e-23 | 36/47 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +10.1 | 4e-22 | 32/48 (CFPAC-1, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.75×** | +8.6 | 7e-16 | 38/44 (SHP-77, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.71×** | +8.3 | 1e-14 | 30/47 (C32, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.72×** | +8.1 | 4e-14 | 22/34 (A498, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +7.5 | 3e-12 | 25/46 (HS-578T, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.61×** | +7.3 | 1e-11 | 25/47 (NCI-H2347, C32, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **2.26×** | +6.6 | 2e-09 | 23/45 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~59% of this change | **1.53×** | +6.3 | 1e-08 | 23/42 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **2.17×** | +6.3 | 2e-08 | 23/43 (A498, HS-578T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.73×** | +6.0 | 6e-08 | 18/47 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.44×** | +5.4 | 2e-06 | 17/45 (LoVo, RKO, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.89×** | +5.1 | 1e-05 | 16/44 (A498, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.72×** | +4.4 | 3e-04 | 9/45 (A498, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.71×** | +4.3 | 4e-04 | 7/40 (PANC-1, RKO, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.66×** | +4.1 | 0.001 | 12/39 (A498, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 0.001 | 9/46 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2447.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.590×** | -11.6 | 3e-28 | 30/44 (RKO, SNU-1, …) | inconsistent across doses | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.612×** | -7.3 | 7e-11 | 24/46 (NCI-H2347, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.702×** | -5.5 | 8e-06 | 19/47 (HOP62, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.592×** | -4.3 | 0.003 | 14/46 (RKO, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.830×** | -4.1 | 0.005 | 18/48 (SHP-77, RKO, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.834× | -4.0 | 0.006 | 16/48 (A-427, PANC-1, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.777×** | -3.9 | 0.007 | 14/47 (KATO III, RKO, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.792×** | -3.4 | 0.056 | 11/43 (HS-578T, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.813×** | -3.2 | 0.078 | 5/48 (HT-29, CHP-212, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.805×** | -3.1 | 0.098 | 8/28 (HOP62, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.62 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2447. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 12.4 | 2 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 5.46× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.0682× (z -16.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 16.9 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 6.27× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -8.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 25.0 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.27× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 22.5 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.94× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 7.83 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.12× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.0788× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 8.16 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.170× (z -9.2) ⚠ cell-cycle shift, explains ~24% of this change |
| [[AN3 CA (line)]] | alt | 16.5 | 0 | 1 | — | [[Furosemide (drug)]] 0.05 µM 0.0595× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 5.62 | 0 | 1 | — | [[Ligustrazine (drug)]] 5 µM 0.0640× (z -9.6) |
| [[BT-474 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -9.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HEC-1-A (line)]] | alt | 11.5 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.12× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -9.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H1792 (line)]] | alt | 6.11 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0711× (z -9.9) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 10.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.86× (z +11.2) | — |
| [[RKO (line)]] | wt | 47.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -14.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SNU-1 (line)]] | wt | 17.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -10.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SNU-423 (line)]] | alt | 8.36 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.11× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -8.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW480 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2447), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC123]] | +0.71 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[CCT3]] | +0.70 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[INVS]] | +0.70 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[EIPR1]] | +0.70 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[NAA25]] | +0.69 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[DFFA]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[TMEM161A]] | +0.68 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[MRPS27]] | +0.68 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[STARD7]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[NKRF]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[SORD]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[HSPE1]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM14]] | -0.66 | -0.58 / -0.67 | both halves | 8e-06 |  |
| [[CHD2]] | -0.64 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[CYLD]] | -0.62 | -0.50 / -0.70 | both halves | 1e-05 |  |
| [[REL]] | -0.61 | -0.59 / -0.57 | both halves | 9e-06 |  |
| [[SGO1-AS1]] | -0.60 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[PIK3IP1]] | -0.60 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[CGGBP1]] | -0.60 | -0.48 / -0.68 | both halves | 2e-05 |  |
| [[TNRC6C]] | -0.59 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[MAK]] | -0.58 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[CREBRF]] | -0.58 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[CDKN1B]] | -0.58 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[ANKRD12]] | -0.58 | -0.62 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-10.0, -33.7); signed map (-11.6, -49.7). **Vector** length 102, 23.1% of its response variance represented; |z| ≥ 3 in 1,045 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.7 | +21.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.3 | +15.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.5 | +15.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.8 | +12.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.9 | +8.1 |
|  | [[EX229 (drug)]] 5 µM |  | +4.6 | +6.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.3 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +7.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.0 | +6.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -5.7 | -11.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.2 | -7.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.6 | -4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.3 | +1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.3 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -2.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.9 | -2.3 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -1.8 | -4.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -3.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | POP1 ribonuclease P/MRP subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.2 — chr8:98,117,293-98,159,835 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Nuclear RNase P complex subunits; RNase MRP complex subunits |
| Reactome | 3 pathways, smallest: tRNA processing in the nucleus; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99575](https://www.uniprot.org/uniprotkb/Q99575) (Ribonucleases P/MRP protein subunit POP1):

> Component of ribonuclease P, a ribonucleoprotein complex that generates mature tRNA molecules by cleaving their 5'-ends. Also a component of the MRP ribonuclease complex, which cleaves pre-rRNA sequences.

**Summary**, from NCBI Gene [10940](https://www.ncbi.nlm.nih.gov/gene/10940):

> This gene encodes the protein subunit of two different small nucleolar ribonucleoprotein complexes: the endoribonuclease for mitochondrial RNA processing complex and the ribonuclease P complex. The encoded protein is a ribonuclease that localizes to the nucleus and functions in pre-RNA processing. This protein is also an autoantigen in patients suffering from connective tissue diseases. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:30129](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30129) · Entrez [10940](https://www.ncbi.nlm.nih.gov/gene/10940) · UniProt [Q99575](https://www.uniprot.org/uniprotkb/Q99575) · Ensembl [ENSG00000104356](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104356)

## Data

Gene col 2447: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2447); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2447, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2447]; `tensor/DDL_lfc|DDL_z.npy` [2447]; `embed/gene_vectors.npy` [2447]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2447 or target_col == 2447). Every well: [[POP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
