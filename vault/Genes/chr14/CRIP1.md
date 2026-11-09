---
symbol: "CRIP1"
type: "gene"
col: 13085
ensembl_id: "ENSG00000213145"
name: "cysteine rich protein 1"
location: "14q32.33"
module: 58
arm: "+"
pooled_cpm: 52.85
n_lines_expressing: 23
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# CRIP1

*cysteine rich protein 1* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 8.98× (z +11.8, q 2e-29, up in 21 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.64× (z +3.7, q 0.014, up in 15 of 21 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H1573 23.4×, KATO III 7.60×, PANC-1 7.56×, SW 900 6.59×, …; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 10.1×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 11.0×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.461× (z -3.9, q 0.058, down in 19 of 21 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.271×); [[Bortezomib (drug)]] 0.05 µM in 1 line (HT-29 0.136×; ⚠ cell-cycle shift, explains ~50% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[S100A4]] (+0.62, fdr 1e-05), [[CUTA]] (+0.61, fdr 1e-05), [[ADIRF]] (+0.59, fdr 2e-04); moves opposite to [[CCT6A]] (-0.58, fdr 1e-05), [[CCT5]] (-0.52, fdr 3e-05), [[JMJD7]] (-0.51, fdr 8e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CXADR]] → it (grade B ⚠); 6 go from it, the strongest it → [[VAMP8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13085.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H1573 23.4×, KATO III 7.60×, PANC-1 7.56×, SW 900 6.59×, …; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 10.1×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 11.0×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **8.98×** | +11.8 | 2e-29 | 21/21 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.15×** | +8.5 | 6e-15 | 21/21 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.48×** | +7.5 | 2e-11 | 18/21 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.64×** | +5.2 | 2e-05 | 17/21 (NCI-H1573, PANC-1, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.26×** | +4.2 | 0.003 | 14/21 (NCI-H1573, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **2.12×** | +4.0 | 0.005 | 15/21 (SW 900, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.64×** | +3.7 | 0.014 | 15/21 (SW480, HepG2/C3A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.89×** | +3.3 | 0.068 | 16/21 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | 1.83× | +3.1 | 0.11 | 18/21 (CFPAC-1, NCI-H460, …) | top dose only | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.50× | +3.1 | 0.12 | 20/21 (Hs 766T, CFPAC-1, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13085.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.271×); [[Bortezomib (drug)]] 0.05 µM in 1 line (HT-29 0.136×; ⚠ cell-cycle shift, explains ~50% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.461×** | -3.9 | 0.058 | 19/21 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.522× | -3.2 | 0.27 | 16/21 (LS 180, Hs 766T, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | 0.534× | -3.2 | 0.27 | 19/21 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.544× | -3.0 | 0.27 | 18/21 (SW480, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.80 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13085. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 33.8 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 23.4× (z +12.0) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 158 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.38× (z +8.6) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.136× (z -8.6) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A-427 (line)]] | wt | 346 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -8.8) |
| [[A549 (line)]] | wt | 144 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.02× (z +8.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 82.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.60× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 60.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.89× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 18.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.4× (z +8.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 111 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.56× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 53.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.59× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 27.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.10× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 4.07 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.24 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.05 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.34 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.51 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 160 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.21 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.77 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.51 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.16 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.30 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.71 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13085), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[S100A4]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[CUTA]] | +0.61 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[ADIRF]] | +0.59 | +0.32 / +0.64 | both halves | 2e-04 |  |
| [[TSTD1]] | +0.58 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[SPPL3]] | +0.58 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[MDK]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[APOA1]] | +0.55 | +0.33 / +0.48 | both halves | 1e-04 |  |
| [[ARF5]] | +0.55 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[NDUFB11]] ⚠ | +0.55 | +0.50 / +0.47 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[GABARAP]] ⚠ | +0.54 | +0.60 / +0.43 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[WFDC2]] | +0.54 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[NPC2]] | +0.52 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[GCHFR]] | +0.52 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[CKB]] | +0.52 | +0.51 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT6A]] | -0.58 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[CCT5]] | -0.52 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[JMJD7]] | -0.51 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[IKBKG]] | -0.50 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[IDE]] | -0.50 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[TRAPPC12]] | -0.48 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[CCT3]] | -0.48 | -0.49 / -0.40 | both halves | 4e-05 |  |
| [[ABCF2]] | -0.46 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[CCT7]] | -0.46 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[DDX21]] | -0.46 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[LIG3]] | -0.46 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[PRKAG1]] | -0.46 | -0.44 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXADR]] | B | CXADR activity raises CRIP1's level | lines that do not express CXADR (16) vs lines expressing it (34) | 3.75× lower at baseline in the lines without CXADR | 0.057 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[GCHFR]] | B | GCHFR activity raises CRIP1's level | lines that do not express GCHFR (13) vs lines expressing it (37) | 3.34× lower at baseline in the lines without GCHFR | 0.068 | ⚠ within organs, on part of the lines; also absent: ARHGEF5, ATAD3C, PRKCZ; maybe low, not absent |
| [[IGFBP2]] | B | IGFBP2 activity raises CRIP1's level | lines that do not express IGFBP2 (16) vs lines expressing it (34) | 2.38× lower at baseline in the lines without IGFBP2 | 0.096 | ⚠ within organs, on part of the lines; also absent: CBFA2T3, CHRNA7, FSTL4 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VAMP8]] | B | CRIP1 activity raises VAMP8's level | lines that do not express CRIP1 (27) vs lines expressing it (23) | 2.62× lower at baseline in the lines without CRIP1 | 0.010 | ⚠ within organs, on part of the lines; also absent: SPINT2, POF1B, S100P |
| [[GCHFR]] | B | CRIP1 activity raises GCHFR's level | lines that do not express CRIP1 (27) vs lines expressing it (23) | 1.82× lower at baseline in the lines without CRIP1 | 0.018 | ⚠ within organs, on part of the lines; also absent: SPINT2, POF1B, S100P |
| [[BBS9]] | B | CRIP1 activity lowers BBS9's level | lines that do not express CRIP1 (27) vs lines expressing it (23) | 1.71× higher at baseline in the lines without CRIP1 | 0.027 | ⚠ within organs, on part of the lines; also absent: SPINT2, POF1B, S100P |
| cells under [[IQ 1 (drug)]] 5 µM | B | CRIP1 activity raises the cells' numbers under IQ 1 5 µM (protects the cells) | lines that do not express CRIP1 (27) vs lines expressing it (21) | the lines without CRIP1: 0.83× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: SPINT2, POF1B, S100P |
| [[CXADR]] | B | CRIP1 activity raises CXADR's level | lines that do not express CRIP1 (27) vs lines expressing it (23) | 3.18× lower at baseline in the lines without CRIP1 | 0.085 | ⚠ within organs, on part of the lines; also absent: SPINT2, POF1B, S100P |
| [[BBS9]] | C | CRIP1 activity weakens BBS9's drug response | lines that do not express CRIP1 (27) vs lines expressing it (21) | the lines without CRIP1 respond 1.02× as strongly (z diff -0.73); strongest at Dinaciclib 0.5 µM: 0.34x vs 0.51x (z diff -2.0) | 0.096 | ⚠ within organs, on part of the lines; also absent: SPINT2, POF1B, S100P; target measured in part of the lines; rests on the correction; artifact flags |

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.376). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.3, 55.9); signed map (47.0, -4.6). **Vector** length 54.7, 21.3% of its response variance represented; |z| ≥ 3 in 275 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +4.2 | +5.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +11.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.6 | -3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | cysteine rich protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:105,486,317-105,488,947 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CRIP |
| Gene groups (HGNC) | LIM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P50238](https://www.uniprot.org/uniprotkb/P50238) (Cysteine-rich protein 1):

> Seems to have a role in zinc absorption and may function as an intracellular zinc transport protein.

**Summary**, from NCBI Gene [1396](https://www.ncbi.nlm.nih.gov/gene/1396):

> Cysteine-rich intestinal protein (CRIP) belongs to the LIM/double zinc finger protein family, members of which include cysteine- and glycine-rich protein-1 (CSRP1; MIM 123876), rhombotin-1 (RBTN1; MIM 186921), rhombotin-2 (RBTN2; MIM 180385), and rhombotin-3 (RBTN3; MIM 180386). CRIP may be involved in intestinal zinc transport (Hempe and Cousins, 1991 [PubMed 1946385]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:2360](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2360) · Entrez [1396](https://www.ncbi.nlm.nih.gov/gene/1396) · UniProt [P50238](https://www.uniprot.org/uniprotkb/P50238) · Ensembl [ENSG00000213145](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213145)

## Data

Gene col 13085: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13085); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13085, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13085]; `tensor/DDL_lfc|DDL_z.npy` [13085]; `embed/gene_vectors.npy` [13085]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13085 or target_col == 13085). Every well: [[CRIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
