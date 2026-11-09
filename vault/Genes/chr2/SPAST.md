---
symbol: "SPAST"
type: "gene"
col: 327
ensembl_id: "ENSG00000021574"
name: "spastin"
location: "2p22.3"
module: 171
arm: "+"
pooled_cpm: 54.0
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# SPAST

*spastin* — 2p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.21× (z +4.0, q 0.029, up in 20 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.687× (z -11.5, q 5e-28, down in 26 of 48 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.800× (z -6.9, q 2e-09, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (PANC-1 0.442×, LOX-IMVI 0.378×, HS-578T 0.367×, NCI-H1573 0.439×, …; ⚠ cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (Panc 03.27 0.0992×, NCI-H2347 0.240×, SW48 0.142×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.318×, AsPC-1 0.318×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.467×); [[Auranofin (drug)]] 5 µM in 1 line (SW480 0.523×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.614×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETD3]] (+0.65, fdr 8e-06), [[SACM1L]] (+0.64, fdr 7e-06), [[AKTIP]] (+0.63, fdr 7e-06); moves opposite to [[SLC9A8]] (-0.58, fdr 3e-05), [[PPIF]] (-0.55, fdr 2e-05), [[CD163L1]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 327.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.029 | 20/48 (CFPAC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.047 | 12/49 (HEC-1-A, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.19× | +3.7 | 0.047 | 19/47 (HOP62, J82, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.5 | 0.073 | 18/48 (CFPAC-1, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 327.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (PANC-1 0.442×, LOX-IMVI 0.378×, HS-578T 0.367×, NCI-H1573 0.439×, …; ⚠ cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (Panc 03.27 0.0992×, NCI-H2347 0.240×, SW48 0.142×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.318×, AsPC-1 0.318×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.467×); [[Auranofin (drug)]] 5 µM in 1 line (SW480 0.523×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.614×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.687×** | -11.5 | 5e-28 | 26/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.800×** | -6.9 | 2e-09 | 24/48 (A-427, PANC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.754×** | -6.1 | 1e-07 | 27/48 (SW480, SHP-77, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.765×** | -5.8 | 8e-07 | 23/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.780×** | -5.2 | 2e-05 | 25/48 (NCI-H1573, PANC-1, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.848× | -5.1 | 4e-05 | 21/48 (A549, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.804×** | -4.8 | 2e-04 | 24/47 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.805×** | -4.7 | 2e-04 | 21/48 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.825×** | -4.0 | 0.003 | 19/47 (NCI-H2347, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.894× | -3.5 | 0.030 | 13/48 (SW 900, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.854× | -3.4 | 0.030 | 19/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.706×** | -3.2 | 0.065 | 15/36 (HS-578T, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | 0.719× | -3.0 | 0.10 | 12/48 (NCI-H2347, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 327. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 63.3 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -12.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[PANC-1 (line)]] | alt | 64.7 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -15.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[LOX-IMVI (line)]] | wt | 107 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -13.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H2347 (line)]] | alt | 48.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 114 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.614× (z -9.2) |
| [[A549 (line)]] | wt | 79.8 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -10.9) ⚠ cell-cycle shift, explains ~8% of this change |
| [[AN3 CA (line)]] | alt | 77.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -11.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H23 (line)]] | alt | 63.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -12.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H460 (line)]] | wt | 54.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.463× (z -9.8) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.467× (z -9.8) |
| [[A-172 (line)]] | wt | 48.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.431× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[AsPC-1 (line)]] | alt | 57.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 36.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 45.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -12.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[J82 (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -8.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H1792 (line)]] | alt | 45.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.380× (z -9.3) ⚠ cell-cycle shift, explains ~18% of this change |
| [[NCI-H2030 (line)]] | alt | 86.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -10.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Panc 03.27 (line)]] | alt | 50.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0992× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 54.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 60.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.523× (z -9.2) |
| [[A498 (line)]] | wt | 70.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 77.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 65.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 327), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD3]] | +0.65 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[SACM1L]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[AKTIP]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[VPS26B]] | +0.63 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[PAPSS1]] | +0.60 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[SLC9A6]] | +0.60 | +0.64 / +0.40 | both halves | 5e-05 |  |
| [[TMEM183A]] | +0.60 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[KIF3A]] | +0.59 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[GK5]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[SERAC1]] | +0.58 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[CNOT6L]] | +0.58 | +0.73 / +0.45 | both halves | 3e-05 |  |
| [[CROT]] | +0.58 | +0.56 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A8]] | -0.58 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[PPIF]] | -0.55 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[CD163L1]] | -0.55 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[CAVIN4]] | -0.54 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[RPAP1]] | -0.53 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[CHTF8]] | -0.52 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[FAM200A]] | -0.52 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[ANGPT2]] | -0.51 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[FAM83G]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[TRPM2]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[ZNF764]] | -0.51 | -0.53 / -0.29 | both halves | 3e-04 |  |
| [[ARMC5]] | -0.51 | -0.54 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.569). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (-8.6, -13.9); signed map (-36.7, -14.2). **Vector** length 95.1, 21.9% of its response variance represented; |z| ≥ 3 in 771 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +4.3 | +3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.4 | +3.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.4 | +1.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +1.7 | +1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.7 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +1.6 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +1.6 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -7.1 | -11.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -4.8 | -5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -6.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -3.4 | -4.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.4 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | spastin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.3 — chr2:32,063,556-32,157,637 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FSP2, ADPSP, KIAA1083; previously SPG4 |
| Gene groups (HGNC) | AAA ATPases |
| Reactome | 7 pathways, smallest: Sealing of the nuclear envelope (NE) by ESCRT-III; Nuclear Envelope (NE) Reassembly; Mitotic Anaphase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBP0](https://www.uniprot.org/uniprotkb/Q9UBP0) (Spastin):

> ATP-dependent microtubule severing protein that specifically recognizes and cuts microtubules that are polyglutamylated. Preferentially recognizes and acts on microtubules decorated with short polyglutamate tails: severing activity increases as the number of glutamates per tubulin rises from one to eight, but decreases beyond this glutamylation threshold. Severing activity is not dependent on tubulin acetylation or detyrosination. Microtubule severing promotes reorganization of cellular …

**Summary**, from NCBI Gene [6683](https://www.ncbi.nlm.nih.gov/gene/6683):

> This gene encodes a member of the AAA (ATPases associated with a variety of cellular activities) protein family. Members of this protein family share an ATPase domain and have roles in diverse cellular processes including membrane trafficking, intracellular motility, organelle biogenesis, protein folding, and proteolysis. The use of alternative translational initiation sites in this gene results in a single transcript variant that can produce isoforms that differ in the length of their …

**Accessions** — [HGNC:11233](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11233) · Entrez [6683](https://www.ncbi.nlm.nih.gov/gene/6683) · UniProt [Q9UBP0](https://www.uniprot.org/uniprotkb/Q9UBP0) · Ensembl [ENSG00000021574](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000021574)

## Data

Gene col 327: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 327); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 327, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 327]; `tensor/DDL_lfc|DDL_z.npy` [327]; `embed/gene_vectors.npy` [327]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 327 or target_col == 327). Every well: [[SPAST — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPAST.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
