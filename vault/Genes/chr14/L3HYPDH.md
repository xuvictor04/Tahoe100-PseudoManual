---
symbol: "L3HYPDH"
type: "gene"
col: 4767
ensembl_id: "ENSG00000126790"
name: "trans-L-3-hydroxyproline dehydratase"
location: "14q23.1"
module: 5
arm: "+"
pooled_cpm: 19.09
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 12
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# L3HYPDH

*trans-L-3-hydroxyproline dehydratase* — 14q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.39× (z +3.9, q 0.062, up in 15 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.36× (z +3.6, q 0.093, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.420× (z -14.6, q 3e-45, down in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.707× (z -4.1, q 0.003, down in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (PANC-1 0.178×, NCI-H460 0.213×, Panc 03.27 0.124×, A498 0.186×, …; ⚠ cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-172 0.0857×, LoVo 0.116×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 2 lines (Hs 766T 0.146×, SW1417 0.113×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (SW 900 0.0760×); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (SW48 0.0824×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPR135]] (+0.86, fdr 7e-06, ⚠ same locus), [[RPTOR]] (+0.63, fdr 7e-06), [[NAA25]] (+0.61, fdr 1e-05), [[ATPSCKMT]] (+0.60, fdr 1e-05); moves opposite to [[CDKN2D]] (-0.59, fdr 1e-05), [[DDAH2]] (-0.58, fdr 1e-05), [[PPP1R13B]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[BIK]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Bendamustine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4767.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +3.9 | 0.062 | 15/48 (NCI-H2347, SW480, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.093 | 22/48 (AsPC-1, CFPAC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.34× | +3.4 | 0.12 | 12/48 (NCI-H1792, NCI-H1573, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 1.30× | +3.1 | 0.22 | 9/48 (LOX-IMVI, A549, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.33× | +3.1 | 0.22 | 12/48 (NCI-H23, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4767.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (PANC-1 0.178×, NCI-H460 0.213×, Panc 03.27 0.124×, A498 0.186×, …; ⚠ cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-172 0.0857×, LoVo 0.116×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 2 lines (Hs 766T 0.146×, SW1417 0.113×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (SW 900 0.0760×); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (SW48 0.0824×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.420×** | -14.6 | 3e-45 | 43/47 (PANC-1, NCI-H460, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.501×** | -8.2 | 6e-14 | 30/48 (PANC-1, LoVo, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.536×** | -7.1 | 2e-10 | 33/47 (PANC-1, HOP62, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.567×** | -6.7 | 2e-09 | 30/46 (NCI-H460, HepG2/C3A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.677×** | -4.5 | 9e-04 | 20/40 (HT-29, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.707×** | -4.1 | 0.003 | 20/48 (LOX-IMVI, AN3 CA, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.710×** | -4.1 | 0.004 | 20/48 (HepG2/C3A, C-33 A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **0.701×** | -4.1 | 0.004 | 21/43 (LoVo, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.540×** | -3.8 | 0.008 | 16/48 (NCI-H460, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.743×** | -3.5 | 0.024 | 20/47 (NCI-H460, SW48, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.747×** | -3.5 | 0.027 | 17/48 (NCI-H460, H4, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.768×** | -3.1 | 0.078 | 16/48 (H4, LOX-IMVI, …) | top dose only |  |
| [[Sinomenine (drug)]] 0.5 µM |  | 0.775× | -3.0 | 0.11 | 16/48 (SNU-1, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4767. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 29.0 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -23.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LoVo (line)]] | wt | 14.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 13.8 | 0 | 4 (1 ⚠) | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0824× (z -9.2) |
| [[A-172 (line)]] | wt | 19.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0857× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 38.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -15.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A498 (line)]] | wt | 26.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -14.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[H4 (line)]] | wt | 52.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 30.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -11.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LOX-IMVI (line)]] | wt | 32.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -10.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-427 (line)]] | wt | 20.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 29.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -9.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[BT-474 (line)]] | alt | 5.07 | 0 | 1 | — | [[Diphenhydramine (drug)]] 0.05 µM 0.0615× (z -8.7) |
| [[C32 (line)]] | wt | 7.28 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0978× (z -8.9) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 14.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0767× (z -10.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HEC-1-A (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -11.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HepG2_C3A (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0728× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[Hs 766T (line)]] | wt | 13.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.146× (z -9.5) |
| [[HS-578T (line)]] | alt | 9.81 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -9.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HT-29 (line)]] | alt | 5.18 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.111× (z -8.9) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 23.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -13.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[J82 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -14.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[RPMI-7951 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -11.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SHP-77 (line)]] | alt | 27.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 16.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -10.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW 900 (line)]] | alt | 9.99 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0760× (z -10.0) |
| [[SW1417 (line)]] | alt | 5.10 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.113× (z -9.1) |
| [[SW480 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.236× (z -10.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[AN3 CA (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4767), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR135]] | +0.86 | +0.84 / +0.84 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[RPTOR]] | +0.63 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[NAA25]] | +0.61 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[ATPSCKMT]] | +0.60 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[FIRRE]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[ABCF2]] | +0.60 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[METTL3]] | +0.60 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[MRPS27]] | +0.60 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[TSR1]] | +0.59 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[HSPA4]] | +0.59 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[CCT5]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[PRMT3]] | +0.59 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[ALG8]] | +0.59 | +0.57 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN2D]] | -0.59 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[DDAH2]] | -0.58 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[PPP1R13B]] | -0.57 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[HDAC5]] | -0.57 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[ZFYVE1]] | -0.55 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[SIRT2]] | -0.55 | -0.49 / -0.50 | both halves | 2e-05 |  |
| [[SHOC2]] | -0.54 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[CNNM4]] | -0.53 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[RNASE4]] | -0.53 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[BIK]] | -0.53 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[RAB11FIP1]] | -0.52 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[GRB7]] | -0.52 | -0.48 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BIK]] | B | BIK activity lowers L3HYPDH's level | lines that do not express BIK (15) vs lines expressing it (35) | 1.73× higher at baseline in the lines without BIK | 0.017 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |
| [[PRR5L]] | B | PRR5L activity raises L3HYPDH's level | lines that do not express PRR5L (10) vs lines expressing it (40) | 1.38× lower at baseline in the lines without PRR5L | 0.063 | ⚠ within organs, on part of the lines; also absent: RASA3, DUSP5-DT, HOXA13; maybe low, not absent |
| [[GBX2-AS1]] | B | GBX2-AS1 activity raises L3HYPDH's level | lines that do not express GBX2-AS1 (13) vs lines expressing it (37) | 1.76× lower at baseline in the lines without GBX2-AS1 | 0.077 | ⚠ within organs, on part of the lines; also absent: ANTXR1, KCNK13, TTC7B |
| [[GPR135]] | C | GPR135 activity raises L3HYPDH's level | lines that do not express GPR135 (3) vs lines expressing it (47) | 2.93× lower at baseline in the lines without GPR135 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CAVIN4, SYCP2L, FAM229B; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Bendamustine (drug)]] 0.5 µM | C | L3HYPDH's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | L3HYPDH's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62 | 0.417 over the table, 0.085 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Hydroxyurea (drug)]] 0.5 µM | C | L3HYPDH's natural level lowers the cells' numbers under Hydroxyurea 0.5 µM (makes them more sensitive) | L3HYPDH's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62 | 0.421 over the table, 0.091 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.585). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-12.8, -32.2); signed map (-9.8, -44.3). **Vector** length 85.2, 17.7% of its response variance represented; |z| ≥ 3 in 911 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.2 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +0.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -5.6 | -14.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -3.1 | -7.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.1 | -4.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.8 | -3.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.5 | -3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.3 | -2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -2.8 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -2.0 | -1.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | trans-L-3-hydroxyproline dehydratase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.1 — chr14:59,460,363-59,484,408 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25436; previously C14orf149 |
| Gene groups (HGNC) | Carbon-oxygen lyases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EM0](https://www.uniprot.org/uniprotkb/Q96EM0) (Trans-3-hydroxy-L-proline dehydratase):

> Catalyzes the dehydration of trans-3-hydroxy-L-proline to Delta(1)-pyrroline-2-carboxylate (Pyr2C). May be required to degrade trans-3-hydroxy-L-proline from the diet and originating from the degradation of proteins such as collagen-IV that contain it.

**Summary**, from NCBI Gene [112849](https://www.ncbi.nlm.nih.gov/gene/112849):

> The protein encoded by this gene is a dehydratase that converts trans-3-hydroxy-L-proline to delta(1)-pyrroline-2-carboxylate. This enzyme may function to degrade dietary proteins that contain trans-3-hydroxy-L-proline as well as other proteins such as collagen IV. The encoded protein can be converted to an epimerase by changing a threonine to a cysteine at a catalytic site. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:20488](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20488) · Entrez [112849](https://www.ncbi.nlm.nih.gov/gene/112849) · UniProt [Q96EM0](https://www.uniprot.org/uniprotkb/Q96EM0) · Ensembl [ENSG00000126790](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126790)

## Data

Gene col 4767: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4767); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4767, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4767]; `tensor/DDL_lfc|DDL_z.npy` [4767]; `embed/gene_vectors.npy` [4767]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4767 or target_col == 4767). Every well: [[L3HYPDH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/L3HYPDH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
