---
symbol: "HMGN5"
type: "gene"
col: 12541
ensembl_id: "ENSG00000198157"
name: "high mobility group nucleosome binding domain 5"
location: "Xq21.1"
module: 45
arm: "+"
pooled_cpm: 19.82
n_lines_expressing: 43
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 8
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# HMGN5

*high mobility group nucleosome binding domain 5* — Xq21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.13× (z +14.3, q 1e-43, up in 32 of 32 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.62× (z +5.4, q 8e-06, up in 24 of 41 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1573 0.449×; ⚠ cell-cycle shift, would explain all of this change); [[Valdecoxib (drug)]] 0.05 µM in 1 line (C32 0.0607×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 0.390×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BEX3]] (+0.55, fdr 5e-05), [[PDS5B]] (+0.54, fdr 9e-05), [[HMGN3]] (+0.53, fdr 2e-05); moves opposite to [[SMIM12]] (-0.55, fdr 3e-04), [[ZNF696]] (-0.53, fdr 2e-04), [[TPD52L2]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TSPAN12]] → it (grade B ⚠); 8 go from it, the strongest it → [[CA11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12541.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **6.13×** | +14.3 | 1e-43 | 32/32 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **5.04×** | +12.3 | 4e-32 | 24/25 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **4.02×** | +10.1 | 7e-22 | 25/27 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.53×** | +7.0 | 3e-10 | 31/34 (LOX-IMVI, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **2.01×** | +5.5 | 4e-06 | 26/35 (HOP62, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.62×** | +5.4 | 8e-06 | 24/41 (Hs 766T, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.52×** | +4.7 | 2e-04 | 20/36 (NCI-H2347, J82, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +4.4 | 8e-04 | 19/40 (A-427, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.68×** | +4.1 | 0.003 | 20/41 (A-427, PANC-1, …) | all doses, flat | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **1.67×** | +4.1 | 0.003 | 19/38 (NCI-H460, KATO III, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.65×** | +3.8 | 0.008 | 17/38 (SNU-423, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.59×** | +3.6 | 0.013 | 20/38 (A-427, PANC-1, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.60×** | +3.6 | 0.016 | 17/38 (SNU-423, RPMI-7951, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +3.4 | 0.025 | 17/39 (LOX-IMVI, PANC-1, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +3.2 | 0.049 | 17/38 (A-427, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **2.16×** | +3.2 | 0.052 | 17/36 (KATO III, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12541.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1573 0.449×; ⚠ cell-cycle shift, would explain all of this change); [[Valdecoxib (drug)]] 0.05 µM in 1 line (C32 0.0607×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 0.390×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.640× | -3.2 | 0.34 | 14/40 (C32, SW480, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.663× | -3.2 | 0.34 | 13/38 (J82, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.671× | -3.1 | 0.34 | 18/40 (Hs 766T, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12541. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 117 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 53.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.41× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LOX-IMVI (line)]] | wt | 32.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.50× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 5.03× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 49.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.73× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 17.9× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H460 (line)]] | wt | 37.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.3× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SNU-423 (line)]] | alt | 17.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.74× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW480 (line)]] | alt | 37.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A498 (line)]] | wt | 5.94 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.25× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[C32 (line)]] | wt | 7.22 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0607× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 16.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.96× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HOP62 (line)]] | alt | 8.98 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.14× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HT-29 (line)]] | alt | 10.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.25× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[J82 (line)]] | alt | 10.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.05× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[Panc 03.27 (line)]] | alt | 8.74 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.8× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[PANC-1 (line)]] | alt | 9.11 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SHP-77 (line)]] | alt | 48.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.45× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 33.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.46× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 3.76 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.84 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 35.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12541), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BEX3]] | +0.55 | +0.40 / +0.39 | both halves | 5e-05 |  |
| [[PDS5B]] | +0.54 | +0.37 / +0.39 | both halves | 9e-05 |  |
| [[HMGN3]] | +0.53 | +0.46 / +0.66 | both halves | 2e-05 | same gene group; STRING 590 |
| [[CYP39A1]] | +0.53 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[HSF2]] | +0.52 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[SH3BGRL]] | +0.51 | +0.43 / +0.35 | both halves | 1e-04 | ⚠ same locus (0.2 kb: neighbours can correlate without regulation) |
| [[FAM151B-DT]] | +0.51 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[QPRT]] | +0.51 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[BRINP3]] | +0.51 | +0.49 / +0.37 | both halves | 9e-05 |  |
| [[XPO1]] | +0.50 | +0.43 / +0.34 | both halves | 1e-04 |  |
| [[CRISPLD1]] | +0.50 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[TRERF1]] | +0.50 | +0.36 / +0.53 | both halves | 1e-04 |  |
| [[HOXB6]] | +0.49 | +0.42 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM12]] | -0.55 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[ZNF696]] | -0.53 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[TPD52L2]] | -0.52 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[DPH2]] | -0.50 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[ZBED4]] | -0.50 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[B4GALT7]] | -0.50 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[MFSD10]] | -0.50 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[ATP6V0A2]] | -0.49 | -0.33 / -0.32 | both halves | 2e-04 |  |
| [[SLC35C1]] | -0.49 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[GAN]] | -0.48 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[C11orf24]] | -0.48 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[WDR55]] | -0.47 | -0.43 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN12]] | B | TSPAN12 activity raises HMGN5's level | lines that do not express TSPAN12 (13) vs lines expressing it (37) | 1.86× lower at baseline in the lines without TSPAN12 | 0.014 | ⚠ within organs, on part of the lines; also absent: ATP8A1, PPP1R9A, SH3BGRL2; maybe low, not absent |
| [[SH3BGRL]] | C | SH3BGRL activity raises HMGN5's level | lines that do not express SH3BGRL (4) vs lines expressing it (46) | 3.65× lower at baseline in the lines without SH3BGRL | 0.048 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HMGN5, HIPK2, ATP10D; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CA11]] | B | HMGN5 activity lowers CA11's level | lines that do not express HMGN5 (7) vs lines expressing it (43) | 1.68× higher at baseline in the lines without HMGN5 | 0.038 | ⚠ within organs, on part of the lines; also absent: SH3BGRL; maybe low, not absent |
| [[TPD52L2]] | B | HMGN5 activity lowers TPD52L2's level | lines that do not express HMGN5 (7) vs lines expressing it (43) | 1.39× higher at baseline in the lines without HMGN5 | 0.050 | ⚠ within organs, on part of the lines; also absent: SH3BGRL; maybe low, not absent |
| [[GAN]] | B | HMGN5 activity lowers GAN's level | lines that do not express HMGN5 (7) vs lines expressing it (43) | 1.35× higher at baseline in the lines without HMGN5 | 0.058 | ⚠ within organs, on part of the lines; also absent: SH3BGRL; maybe low, not absent |
| [[SNX16]] | B | HMGN5 activity raises SNX16's level | lines that do not express HMGN5 (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without HMGN5 | 0.079 | ⚠ within organs, on part of the lines; also absent: SH3BGRL; maybe low, not absent |
| [[CTU2]] | B | HMGN5 activity lowers CTU2's level | lines that do not express HMGN5 (7) vs lines expressing it (43) | 1.29× higher at baseline in the lines without HMGN5 | 0.082 | ⚠ within organs, on part of the lines; also absent: SH3BGRL; maybe low, not absent |
| [[SLC52A2]] | B | HMGN5 activity lowers SLC52A2's level | lines that do not express HMGN5 (7) vs lines expressing it (43) | 1.47× higher at baseline in the lines without HMGN5 | 0.090 | ⚠ within organs, on part of the lines; also absent: SH3BGRL; maybe low, not absent |
| [[ABCB7]] | B | HMGN5 activity raises ABCB7's level | lines that do not express HMGN5 (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without HMGN5 | 0.095 | ⚠ within organs, on part of the lines; also absent: SH3BGRL; maybe low, not absent |
| [[SH3BGRL]] | C | HMGN5 activity raises SH3BGRL's level | lines that do not express HMGN5 (7) vs lines expressing it (43) | 4.16× lower at baseline in the lines without HMGN5 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH3BGRL; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.479). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (11.0, 5.7); signed map (36.7, -28.8). **Vector** length 57.8, 11.6% of its response variance represented; |z| ≥ 3 in 668 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +3.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.2 | +5.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | +3.1 | +4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.6 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~93% of this change | -2.2 | +3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.9 | -1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | high mobility group nucleosome binding domain 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq21.1 — chrX:81,113,699-81,201,913 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously NSBP1 |
| Gene groups (HGNC) | Canonical high mobility group |
| Matched by | ensembl_id |

**Function**, from UniProt [P82970](https://www.uniprot.org/uniprotkb/P82970) (High mobility group nucleosome-binding domain-containing protein 5):

> Preferentially binds to euchromatin and modulates cellular transcription by counteracting linker histone-mediated chromatin compaction.

**Summary**, from NCBI Gene [79366](https://www.ncbi.nlm.nih.gov/gene/79366):

> This gene encodes a nuclear protein with similarities to the high mobility group proteins, HMG14 and HMG17, which suggests that this protein may function as a nucleosomal binding and transcriptional activating protein. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:8013](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8013) · Entrez [79366](https://www.ncbi.nlm.nih.gov/gene/79366) · UniProt [P82970](https://www.uniprot.org/uniprotkb/P82970) · Ensembl [ENSG00000198157](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198157)

## Data

Gene col 12541: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12541); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12541, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12541]; `tensor/DDL_lfc|DDL_z.npy` [12541]; `embed/gene_vectors.npy` [12541]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12541 or target_col == 12541). Every well: [[HMGN5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMGN5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
