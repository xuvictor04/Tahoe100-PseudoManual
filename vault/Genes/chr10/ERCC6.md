---
symbol: "ERCC6"
type: "gene"
col: 13490
ensembl_id: "ENSG00000225830"
name: "ERCC excision repair 6, chromatin remodeling factor"
location: "10q11.23"
module: 11
arm: "+"
pooled_cpm: 44.87
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 20
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# ERCC6

*ERCC excision repair 6, chromatin remodeling factor* — 10q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.45× (z +8.1, q 3e-13, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.591× (z -8.2, q 2e-13, down in 31 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.744× (z -6.5, q 1e-08, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPC2]] (+0.64, fdr 1e-05), [[ZNF776]] (+0.63, fdr 9e-06), [[ZNF181]] (+0.63, fdr 7e-06); moves opposite to [[DCUN1D4]] (-0.60, fdr 1e-05), [[TTC39B]] (-0.58, fdr 3e-05), [[UBTD1]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CDS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13490.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +8.1 | 3e-13 | 31/48 (NCI-H2347, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +5.9 | 1e-06 | 25/47 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +4.8 | 3e-04 | 26/48 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 5 µM |  | 1.46× | +3.1 | 0.17 | 10/49 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.21× | +3.0 | 0.17 | 16/48 (J82, Hs 766T, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.21× | +3.0 | 0.17 | 16/48 (A-427, PANC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.21× | +3.0 | 0.17 | 14/48 (LOX-IMVI, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13490.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.591×** | -8.2 | 2e-13 | 31/48 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.617×** | -6.5 | 1e-08 | 33/47 (C-33 A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.744×** | -6.5 | 1e-08 | 27/48 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.629×** | -6.3 | 5e-08 | 23/40 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.684×** | -5.9 | 4e-07 | 32/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.714×** | -5.3 | 1e-05 | 31/48 (CHP-212, SW48, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.751×** | -4.5 | 7e-04 | 23/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.602×** | -4.1 | 0.003 | 24/48 (NCI-H460, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.770×** | -4.1 | 0.003 | 23/48 (COLO 205, NCI-H2030, …) | two highest doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.690×** | -4.1 | 0.003 | 23/48 (Panc 03.27, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.779×** | -3.9 | 0.005 | 21/48 (NCI-H2030, COLO 205, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.621×** | -3.9 | 0.005 | 24/48 (Panc 03.27, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.623×** | -3.8 | 0.005 | 22/48 (CFPAC-1, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.792×** | -3.6 | 0.011 | 19/47 (NCI-H460, J82, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.642×** | -3.6 | 0.012 | 20/48 (NCI-H460, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.723×** | -3.5 | 0.014 | 23/48 (HCT15, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.755×** | -3.1 | 0.067 | 16/47 (SHP-77, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.697×** | -2.9 | 0.094 | 17/48 (NCI-H460, HOP62, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13490. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 78.0 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -10.4) |
| [[CHP-212 (line)]] | wt | 42.5 | 0 | 3 | — | [[Belinostat (drug)]] 0.5 µM 0.0705× (z -11.3) |
| [[A-427 (line)]] | wt | 31.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +10.4) | — |
| [[HEC-1-A (line)]] | alt | 48.2 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.106× (z -12.3) ⚠ toxic |
| [[J82 (line)]] | alt | 38.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.310× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[KATO III (line)]] | alt | 43.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[LoVo (line)]] | wt | 36.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.3) | [[Belinostat (drug)]] 0.5 µM 0.383× (z -9.5) |
| [[SNU-423 (line)]] | alt | 110 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -10.5) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -9.0) |
| [[A-172 (line)]] | wt | 33.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -9.5) |
| [[BT-474 (line)]] | alt | 51.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 33.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.143× (z -10.1) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 36.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.152× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[HT-29 (line)]] | alt | 39.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 49.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[NCI-H1573 (line)]] | alt | 58.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 79.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[NCI-H23 (line)]] | alt | 66.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[NCI-H2347 (line)]] | alt | 26.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.8) | — |
| [[PANC-1 (line)]] | alt | 41.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SHP-77 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SK-MEL-2 (line)]] | alt | 49.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SNU-1 (line)]] | wt | 39.1 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.367× (z -8.9) |
| [[SW1417 (line)]] | alt | 46.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SW48 (line)]] | wt | 35.1 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.165× (z -9.7) |
| [[SW480 (line)]] | alt | 50.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[A498 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13490), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPC2]] | +0.64 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[ZNF776]] | +0.63 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[ZNF181]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[AASDHPPT]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[ZNF268]] | +0.61 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[ZNF614]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[NAIF1]] | +0.61 | +0.69 / +0.38 | both halves | 6e-05 |  |
| [[PYM1]] | +0.61 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[MRFAP1L1]] | +0.60 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[RPL7L1]] | +0.59 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[CWC22]] | +0.59 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[METTL18]] | +0.59 | +0.64 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCUN1D4]] | -0.60 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[TTC39B]] | -0.58 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[UBTD1]] | -0.57 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[SAP130]] | -0.57 | -0.51 / -0.51 | both halves | 1e-05 | pathway: Epigenetic regulation of gene expression |
| [[CORO7]] | -0.57 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[CDS1]] | -0.57 | -0.59 / -0.39 | both halves | 6e-05 |  |
| [[CARD19]] | -0.57 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[RUSC1]] | -0.57 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[RAB6A]] | -0.56 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[SEC11A]] | -0.56 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[RAB11FIP5]] | -0.55 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[IGSF8]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDS1]] | B | CDS1 activity strengthens ERCC6's drug response | lines that do not express CDS1 (19) vs lines expressing it (30) | the lines without CDS1 respond 0.77× as strongly (z diff +0.82); strongest at Homoharringtonine 5 µM: 1.17x vs 1.55x (z diff +3.4) | 0.041 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[SPINT2]] | B | SPINT2 activity strengthens ERCC6's drug response | lines that do not express SPINT2 (24) vs lines expressing it (25) | the lines without SPINT2 respond 0.74× as strongly (z diff +0.87); strongest at Homoharringtonine 5 µM: 1.15x vs 1.66x (z diff +4.8) | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, ENTPD2; target measured in part of the lines; both ways; artifact flags |
| [[ZNF606]] | B | ZNF606 activity raises ERCC6's level | lines that do not express ZNF606 (13) vs lines expressing it (37) | 1.09× lower at baseline in the lines without ZNF606 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000176593, C19orf18, ZNF569 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.568). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-30.8, 10.2); signed map (3.7, -27.6). **Vector** length 92.5, 21.7% of its response variance represented; |z| ≥ 3 in 1,026 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.3 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +8.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.5 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +2.9 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.9 | -5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -6.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -5.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -3.5 | -3.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.4 | -6.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.4 | -3.6 |
|  | [[EX229 (drug)]] 5 µM |  | -3.1 | -3.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -4.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.6 | -2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.6 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | ERCC excision repair 6, chromatin remodeling factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.23 — chr10:49,454,168-49,539,538 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CSB, RAD26, ARMD5; previously CKN2 |
| Gene groups (HGNC) | SNF2 related family; ERCC excision repair associated; B-WICH chromatin-remodelling complex subunits |
| Reactome | 12 pathways, smallest: ERCC6 (CSB) and EHMT2 (G9a) positively regulate rRNA expression; B-WICH complex positively regulates rRNA expression; RNA Polymerase I Transcription Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [P0DP91](https://www.uniprot.org/uniprotkb/P0DP91) (Chimeric ERCC6-PGBD3 protein):

> Involved in repair of DNA damage following UV irradiation, acting either in the absence of ERCC6 or synergistically with ERCC6. Involved in the regulation of gene expression. In the absence of ERCC6, induces the expression of genes characteristic of interferon-like antiviral responses. This response is almost completely suppressed in the presence of ERCC6. In the presence of ERCC6, regulates the expression of genes involved in metabolism regulation, including IGFBP5 and IGFBP7. In vitro binds …

**Summary**, from NCBI Gene [2074](https://www.ncbi.nlm.nih.gov/gene/2074):

> This gene encodes a DNA-binding protein that is important in transcription-coupled excision repair. The encoded protein has ATP-stimulated ATPase activity, interacts with several transcription and excision repair proteins, and may promote complex formation at DNA repair sites. Mutations in this gene are associated with Cockayne syndrome type B and cerebrooculofacioskeletal syndrome 1. Alternative splicing occurs between a splice site from exon 5 of this gene to the 3' splice site upstream of …

**Accessions** — [HGNC:3438](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3438) · Entrez [2074](https://www.ncbi.nlm.nih.gov/gene/2074) · UniProt [P0DP91](https://www.uniprot.org/uniprotkb/P0DP91) · Ensembl [ENSG00000225830](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225830)

## Data

Gene col 13490: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13490); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13490, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13490]; `tensor/DDL_lfc|DDL_z.npy` [13490]; `embed/gene_vectors.npy` [13490]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13490 or target_col == 13490). Every well: [[ERCC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERCC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
