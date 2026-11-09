---
symbol: "TSEN2"
type: "gene"
col: 7834
ensembl_id: "ENSG00000154743"
name: "tRNA splicing endonuclease subunit 2"
location: "3p25.2"
module: 4
arm: "+"
pooled_cpm: 24.15
n_lines_expressing: 47
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 21
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# TSEN2

*tRNA splicing endonuclease subunit 2* — 3p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.57× (z +5.6, q 1e-05, up in 26 of 44 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.44× (z +4.4, q 0.003, up in 20 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.432× (z -14.8, q 0e+00, down in 41 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MDN1]] (+0.83, fdr 7e-06), [[URB2]] (+0.83, fdr 7e-06), [[CMSS1]] (+0.78, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TERT]] → it (grade B ⚠); 21 go from it, the strongest it → [[XYLB]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7834.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.57×** | +5.6 | 1e-05 | 26/44 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.44×** | +4.4 | 0.003 | 20/44 (NCI-H1792, LOX-IMVI, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.041 | 15/45 (NCI-H1792, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.41×** | +3.5 | 0.061 | 18/44 (HOP62, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 1.30× | +3.3 | 0.11 | 15/44 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.29× | +3.1 | 0.16 | 9/44 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7834.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.432×** | -14.8 | 0e+00 | 41/45 (SK-MEL-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.460×** | -13.7 | 2e-40 | 36/44 (PANC-1, NCI-H23, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.398×** | -11.5 | 3e-28 | 34/45 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.512×** | -8.4 | 9e-15 | 32/43 (SW48, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.503×** | -8.3 | 2e-14 | 29/43 (PANC-1, NCI-H460, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.584×** | -6.7 | 2e-09 | 25/44 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.600×** | -6.1 | 7e-08 | 28/45 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.634×** | -5.7 | 8e-07 | 24/44 (LoVo, SHP-77, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.629×** | -5.6 | 2e-06 | 28/44 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.672×** | -5.0 | 4e-05 | 25/44 (RKO, A-172, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.714×** | -4.1 | 0.003 | 21/43 (C-33 A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.543×** | -4.0 | 0.003 | 24/45 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.543×** | -4.0 | 0.003 | 18/43 (HCT15, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.729×** | -4.0 | 0.003 | 24/44 (LS 180, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.736×** | -3.8 | 0.005 | 18/44 (LS 180, LoVo, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 0.842× | -3.0 | 0.081 | 12/45 (LS 180, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7834. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 21.9 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -19.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -12.8) |
| [[PANC-1 (line)]] | alt | 33.0 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -26.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.236× (z -15.2) |
| [[SW48 (line)]] | wt | 63.9 | 0 | 9 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0424× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -14.7) |
| [[NCI-H23 (line)]] | alt | 56.9 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -20.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -12.7) |
| [[RKO (line)]] | wt | 52.0 | 0 | 6 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0872× (z -15.3) |
| [[LoVo (line)]] | wt | 53.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -17.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.131× (z -17.3) |
| [[LS 180 (line)]] | wt | 44.9 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -11.7) |
| [[SW480 (line)]] | alt | 37.4 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.189× (z -14.5) |
| [[J82 (line)]] | alt | 18.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -11.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.175× (z -10.3) |
| [[SNU-1 (line)]] | wt | 28.8 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0497× (z -14.5) |
| [[C-33 A (line)]] | alt | 55.9 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0827× (z -16.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -8.5) |
| [[HOP62 (line)]] | alt | 17.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.163× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 29.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -13.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -10.7) |
| [[SHP-77 (line)]] | alt | 32.5 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 29.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.108× (z -20.8) |
| [[SW1417 (line)]] | alt | 38.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -14.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -13.2) |
| [[A-427 (line)]] | wt | 35.5 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.107× (z -17.2) |
| [[BT-474 (line)]] | alt | 23.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.194× (z -8.7) |
| [[C32 (line)]] | wt | 16.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -13.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 35.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -9.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 24.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -16.9) |
| [[A-172 (line)]] | wt | 12.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.177× (z -9.1) |
| [[A498 (line)]] | wt | 8.70 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -9.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 22.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -13.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[H4 (line)]] | wt | 13.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0721× (z -10.0) |
| [[HCT15 (line)]] | alt | 14.6 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0864× (z -8.7) |
| [[KATO III (line)]] | alt | 29.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.179× (z -10.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.85 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.64 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.92 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7834), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDN1]] | +0.83 | +0.82 / +0.82 | both halves | 7e-06 |  |
| [[URB2]] | +0.83 | +0.82 / +0.81 | both halves | 7e-06 |  |
| [[CMSS1]] | +0.78 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.78 | +0.78 / +0.78 | both halves | 7e-06 |  |
| [[DKC1]] | +0.77 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[DPH6]] | +0.77 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.77 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[NLE1]] | +0.77 | +0.71 / +0.78 | both halves | 7e-06 |  |
| [[MRPS27]] | +0.76 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[NAA25]] | +0.76 | +0.72 / +0.79 | both halves | 7e-06 |  |
| [[TMEM177]] | +0.76 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[WDR4]] | +0.75 | +0.79 / +0.79 | both halves | 7e-06 | pathway: tRNA processing |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | TERT activity raises TSEN2's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.78× lower at baseline in the lines without TERT | 0.002 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[LDLRAD3]] | B | LDLRAD3 activity raises TSEN2's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 1.94× lower at baseline in the lines without LDLRAD3 | 0.014 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PDE3B]] | B | PDE3B activity raises TSEN2's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 1.65× lower at baseline in the lines without PDE3B | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[NT5M]] | B | NT5M activity raises TSEN2's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.80× lower at baseline in the lines without NT5M | 0.039 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[MVB12B]] | C | MVB12B activity raises TSEN2's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 2.51× lower at baseline in the lines without MVB12B | 0.031 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 0, C 21. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XYLB]] | C | TSEN2 activity raises XYLB's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.97× lower at baseline in the lines without TSEN2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent; its own permutation p |
| [[FXN]] | C | TSEN2 activity raises FXN's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.90× lower at baseline in the lines without TSEN2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent; co-absent with the target; its own permutation p |
| [[SPATA5]] | C | TSEN2 activity raises SPATA5's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.57× lower at baseline in the lines without TSEN2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent; its own permutation p |
| [[SCAP]] | C | TSEN2 activity raises SCAP's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.34× lower at baseline in the lines without TSEN2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent; its own permutation p |
| [[LARS2]] | C | TSEN2 activity raises LARS2's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.25× lower at baseline in the lines without TSEN2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent; its own permutation p |
| [[DPH5]] | C | TSEN2 activity raises DPH5's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.14× lower at baseline in the lines without TSEN2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent; its own permutation p |
| [[NLE1]] | C | TSEN2 activity raises NLE1's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.13× lower at baseline in the lines without TSEN2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent; its own permutation p |
| [[CHCHD4]] | C | TSEN2 activity raises CHCHD4's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.05× lower at baseline in the lines without TSEN2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent; its own permutation p |
| [[ABCE1]] | C | TSEN2 activity raises ABCE1's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.02× lower at baseline in the lines without TSEN2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent; its own permutation p |
| [[TCOF1]] | C | TSEN2 activity raises TCOF1's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.34× lower at baseline in the lines without TSEN2 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent |
| [[GEMIN5]] | C | TSEN2 activity raises GEMIN5's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 1.86× lower at baseline in the lines without TSEN2 | 0.070 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent |
| [[RFT1]] | C | TSEN2 activity raises RFT1's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 1.73× lower at baseline in the lines without TSEN2 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.776). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-12.0, -37.8); signed map (-5.8, -50.1). **Vector** length 116, 33.1% of its response variance represented; |z| ≥ 3 in 1,024 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.3 | +5.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.6 | +4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.4 | +2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.5 | +2.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.2 | +3.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.9 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | -1.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.4 | -14.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -6.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.6 | -13.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.9 | -1.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.8 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | tRNA splicing endonuclease subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.2 — chr3:12,484,421-12,541,549 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SEN2, SEN2L, MGC2776 |
| Gene groups (HGNC) | tRNA-splicing endonuclease subunits |
| Reactome | 3 pathways, smallest: tRNA processing in the nucleus; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCE0](https://www.uniprot.org/uniprotkb/Q8NCE0) (tRNA-splicing endonuclease subunit Sen2):

> Constitutes one of the two catalytic subunit of the tRNA-splicing endonuclease complex, a complex responsible for identification and cleavage of the splice sites in pre-tRNA. It cleaves pre-tRNA at the 5'- and 3'-splice sites to release the intron. The products are an intron and two tRNA half-molecules bearing 2',3'-cyclic phosphate and 5'-OH termini. There are no conserved sequences at the splice sites, but the intron is invariably located at the same site in the gene, placing the splice sites …

**Summary**, from NCBI Gene [80746](https://www.ncbi.nlm.nih.gov/gene/80746):

> This gene encodes one of the subunits of the tRNA splicing endonuclease. This endonuclease catalyzes the first step in RNA splicing which is the removal of introns. Mutations in this gene have been associated with pontocerebellar hypoplasia type 2. A pseudogene has been identified on chromosome 4. Multiple transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:28422](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28422) · Entrez [80746](https://www.ncbi.nlm.nih.gov/gene/80746) · UniProt [Q8NCE0](https://www.uniprot.org/uniprotkb/Q8NCE0) · Ensembl [ENSG00000154743](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154743)

## Data

Gene col 7834: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7834); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7834, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7834]; `tensor/DDL_lfc|DDL_z.npy` [7834]; `embed/gene_vectors.npy` [7834]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7834 or target_col == 7834). Every well: [[TSEN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSEN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
