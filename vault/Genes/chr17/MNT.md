---
symbol: "MNT"
type: "gene"
col: 951
ensembl_id: "ENSG00000070444"
name: "MAX network transcriptional repressor"
location: "17p13.3"
module: 41
arm: "+"
pooled_cpm: 59.46
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 50
n_dd_up_clean: 2
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# MNT

*MAX network transcriptional repressor* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[PF-06260933 (drug)]] 5 µM: 1.57× (z +3.7, q 0.074, up in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 3.66×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H460 2.91×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 2.82×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 1.95×).
> Pooled over the cell lines (median), lowered significantly by 50 drug-doses (19 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.547× (z -9.3, q 7e-18, down in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.654× (z -9.0, q 4e-17, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCAF11]] (+0.59, fdr 1e-05), [[CDC34]] (+0.59, fdr 1e-05), [[OSBPL2]] (+0.58, fdr 1e-05); moves opposite to [[EPDR1]] (-0.57, fdr 2e-05), [[MTMR2]] (-0.56, fdr 3e-05), [[ZDHHC21]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 951.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 3.66×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H460 2.91×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 2.82×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 1.95×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PF-06260933 (drug)]] 5 µM |  | **1.57×** | +3.7 | 0.074 | 24/48 (CFPAC-1, LS 180, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.074 | 24/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.23 | 18/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.23× | +3.1 | 0.23 | 18/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.22× | +3.0 | 0.23 | 12/47 (SW48, SW480, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 19 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 50 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 951.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.547×** | -9.3 | 7e-18 | 41/48 (A498, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.555×** | -9.1 | 3e-17 | 37/48 (AsPC-1, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.654×** | -9.0 | 4e-17 | 39/48 (KATO III, Hs 766T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.558×** | -8.7 | 6e-16 | 36/47 (LoVo, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.571×** | -8.6 | 6e-16 | 38/48 (KATO III, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.587×** | -7.9 | 3e-13 | 32/48 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.603×** | -7.8 | 5e-13 | 36/48 (AsPC-1, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.589×** | -7.5 | 3e-12 | 30/44 (A-172, A549, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **0.617×** | -7.5 | 6e-12 | 28/48 (HCT15, A-172, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.621×** | -7.4 | 1e-11 | 37/48 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.646×** | -6.7 | 8e-10 | 32/48 (HS-578T, LoVo, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.471×** | -6.1 | 5e-08 | 34/49 (A498, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.754×** | -6.0 | 7e-08 | 36/48 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.700×** | -5.5 | 2e-06 | 26/48 (HOP62, LOX-IMVI, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.691×** | -5.5 | 2e-06 | 29/50 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.696×** | -5.4 | 3e-06 | 39/47 (HEC-1-A, SW1417, …) | rises with dose | position effect removed |
| [[Allantoin (drug)]] 5 µM |  | **0.789×** | -5.0 | 2e-05 | 32/48 (SW48, PANC-1, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.731×** | -4.8 | 4e-05 | 29/48 (A498, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.803×** | -4.7 | 6e-05 | 27/48 (A-172, A549, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.574×** | -4.5 | 2e-04 | 30/48 (A498, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.580×** | -4.4 | 3e-04 | 28/48 (NCI-H1792, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.816×** | -4.3 | 4e-04 | 27/48 (A498, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.749×** | -4.2 | 5e-04 | 28/48 (HS-578T, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.761×** | -4.2 | 5e-04 | 28/48 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.54 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 951. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 111 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -18.4) |
| [[A-172 (line)]] | wt | 140 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.395× (z -10.8) |
| [[SW 900 (line)]] | alt | 88.9 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.201× (z -13.0) |
| [[HS-578T (line)]] | alt | 78.5 | 0 | 5 (5 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0600× (z -13.3) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 69.4 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.66× (z +12.0) | [[Belinostat (drug)]] 5 µM 0.394× (z -8.5) ⚠ cell-cycle shift, explains ~49% of this change |
| [[AsPC-1 (line)]] | alt | 94.0 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.263× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 56.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.244× (z -11.6) |
| [[LoVo (line)]] | wt | 65.0 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.156× (z -16.2) |
| [[A549 (line)]] | wt | 84.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[SW480 (line)]] | alt | 49.3 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.261× (z -13.0) |
| [[Hs 766T (line)]] | wt | 85.2 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.473× (z -9.6) |
| [[KATO III (line)]] | alt | 56.1 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.303× (z -10.5) ⚠ unreliable plate only · without an alert: [[Selinexor (drug)]] 5 µM 0.431× (z -10.1) |
| [[PANC-1 (line)]] | alt | 42.5 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.260× (z -12.9) |
| [[BT-474 (line)]] | alt | 32.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -9.8) |
| [[C32 (line)]] | wt | 43.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.293× (z -9.1) |
| [[CHP-212 (line)]] | wt | 68.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 75.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0642× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[MIA PaCa-2 (line)]] | alt | 64.1 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -8.8) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H1792 (line)]] | alt | 56.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H661 (line)]] | alt | 41.4 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0867× (z -8.7) ⚠ cell-cycle shift, explains ~73% of this change |
| [[SNU-1 (line)]] | wt | 58.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[SNU-423 (line)]] | alt | 58.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -8.5) ⚠ cell-cycle shift, explains ~61% of this change |
| [[A-427 (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 58.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 80.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 44.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 64.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 85.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 951), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCAF11]] | +0.59 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[CDC34]] | +0.59 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[OSBPL2]] | +0.58 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[KLF16]] | +0.58 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[CCDC9]] | +0.57 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[KMT5C]] | +0.57 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[MEF2D]] | +0.57 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[ZFTRAF1]] | +0.56 | +0.41 / +0.68 | both halves | 4e-05 |  |
| [[WIPI1]] | +0.56 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[PKD1]] | +0.55 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[INAFM1]] | +0.55 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[PHF1]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPDR1]] | -0.57 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[MTMR2]] | -0.56 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[ZDHHC21]] | -0.56 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[FAM98B]] | -0.53 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[SLC35B4]] | -0.53 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[FKTN]] | -0.52 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[CCT8]] | -0.52 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[GLO1]] | -0.52 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[PSMD14]] | -0.51 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[CCT4]] | -0.50 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[MTA3]] | -0.50 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[MBTPS2]] | -0.50 | -0.48 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MNT's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.0% of all compounds | 0.089 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.344). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (5.7, -40.3); signed map (-22.4, 12.2). **Vector** length 114, 33.8% of its response variance represented; |z| ≥ 3 in 1,218 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +4.4 | +2.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +3.9 | -4.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.6 | +3.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.8 | +2.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.6 | +1.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.5 | +1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.5 | +3.0 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.7 | -9.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.1 | -8.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.9 | -6.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.4 | -7.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -3.9 | -4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.7 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.7 | -4.4 |
|  | [[EX229 (drug)]] 5 µM |  | -3.6 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | MAX network transcriptional repressor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:2,384,073-2,401,104 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ROX, MXD6, MAD6, bHLHd3, lncRNA-HAL |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; MAX dimerization proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99583](https://www.uniprot.org/uniprotkb/Q99583) (Max-binding protein MNT):

> Binds DNA as a heterodimer with MAX and represses transcription. Binds to the canonical E box sequence 5'-CACGTG-3' and, with higher affinity, to 5'-CACGCG-3'.

**Summary**, from NCBI Gene [4335](https://www.ncbi.nlm.nih.gov/gene/4335):

> The Myc/Max/Mad network comprises a group of transcription factors that co-interact to regulate gene-specific transcriptional activation or repression. This gene encodes a protein member of the Myc/Max/Mad network. This protein has a basic-Helix-Loop-Helix-zipper domain (bHLHzip) with which it binds the canonical DNA sequence CANNTG, known as the E box, following heterodimerization with Max proteins. This protein is likely a transcriptional repressor and an antagonist of Myc-dependent …

**Accessions** — [HGNC:7188](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7188) · Entrez [4335](https://www.ncbi.nlm.nih.gov/gene/4335) · UniProt [Q99583](https://www.uniprot.org/uniprotkb/Q99583) · Ensembl [ENSG00000070444](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070444)

## Data

Gene col 951: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 951); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 951, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 951]; `tensor/DDL_lfc|DDL_z.npy` [951]; `embed/gene_vectors.npy` [951]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 951 or target_col == 951). Every well: [[MNT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MNT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
