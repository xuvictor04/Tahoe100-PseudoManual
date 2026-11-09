---
symbol: "BET1L"
type: "gene"
col: 10880
ensembl_id: "ENSG00000177951"
name: "Bet1 golgi vesicular membrane trafficking protein like"
location: "11p15.5"
module: 52
arm: "+"
pooled_cpm: 26.29
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 28
n_dd_up_clean: 0
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# BET1L

*Bet1 golgi vesicular membrane trafficking protein like* — 11p15.5

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.354× (z -24.1, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARFGAP1]] (+0.82, fdr 7e-06), [[SSR2]] (+0.79, fdr 7e-06), [[HM13]] (+0.78, fdr 7e-06); moves opposite to [[ATF7IP]] (-0.67, fdr 8e-06).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PPP1R9A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10880.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.37× | +3.7 | 0.13 | 10/45 (SHP-77, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.1 | 0.44 | 15/47 (NCI-H23, RKO, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.44 | 11/44 (SNU-1, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10880.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.354×** | -24.1 | 0e+00 | 43/47 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.285×** | -19.8 | 0e+00 | 46/47 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.402×** | -14.9 | 0e+00 | 42/48 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.403×** | -14.9 | 0e+00 | 39/45 (H4, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.474×** | -11.8 | 7e-30 | 34/43 (SNU-423, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.495×** | -11.5 | 1e-28 | 38/47 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.504×** | -11.2 | 3e-27 | 29/39 (A549, SW480, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.512×** | -11.0 | 4e-26 | 32/47 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.519×** | -10.7 | 4e-25 | 41/48 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.320×** | -9.8 | 1e-20 | 35/47 (J82, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.588×** | -8.7 | 2e-16 | 35/48 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.406×** | -7.7 | 6e-13 | 34/46 (HOP62, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.616×** | -7.3 | 1e-11 | 22/34 (hTERT-HPNE, HCT15, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.635×** | -7.1 | 4e-11 | 22/32 (SW480, A-172, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.667×** | -6.6 | 1e-09 | 32/48 (HS-578T, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.677×** | -6.4 | 7e-09 | 30/48 (H4, A549, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.784×** | -5.6 | 6e-07 | 25/48 (PANC-1, RPMI-7951, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.706×** | -5.5 | 1e-06 | 21/48 (LoVo, J82, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.725×** | -5.3 | 4e-06 | 24/48 (RPMI-7951, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.805×** | -5.0 | 2e-05 | 23/48 (MIA PaCa-2, HOP62, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10880. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 42.2 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -22.5) |
| [[H4 (line)]] | wt | 51.1 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0208× (z -24.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.117× (z -13.4) |
| [[A498 (line)]] | wt | 46.8 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -19.8) |
| [[HOP62 (line)]] | alt | 33.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -14.6) |
| [[LoVo (line)]] | wt | 28.7 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.170× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 26.7 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.125× (z -14.1) |
| [[SNU-423 (line)]] | alt | 33.4 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -17.1) |
| [[SW480 (line)]] | alt | 26.9 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0895× (z -21.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.290× (z -11.5) |
| [[A549 (line)]] | wt | 25.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -16.0) |
| [[HT-29 (line)]] | alt | 34.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -13.2) |
| [[hTERT-HPNE (line)]] | wt | 31.7 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0854× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.165× (z -11.4) |
| [[J82 (line)]] | alt | 38.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -19.2) |
| [[KATO III (line)]] | alt | 22.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.162× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 24.3 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0786× (z -15.3) |
| [[PANC-1 (line)]] | alt | 45.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -18.3) |
| [[RKO (line)]] | wt | 20.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -14.6) |
| [[RPMI-7951 (line)]] | alt | 30.8 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.143× (z -12.2) |
| [[A-172 (line)]] | wt | 29.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -19.8) |
| [[AsPC-1 (line)]] | alt | 36.8 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.219× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 12.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -13.4) |
| [[NCI-H23 (line)]] | alt | 14.9 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -10.5) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.162× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 26.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -16.1) |
| [[NCI-H460 (line)]] | wt | 12.2 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.237× (z -10.3) |
| [[SW1417 (line)]] | alt | 33.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -17.3) |
| [[A-427 (line)]] | wt | 24.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -13.1) |
| [[HCT15 (line)]] | alt | 40.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0947× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[Hs 766T (line)]] | wt | 43.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.226× (z -11.0) |
| [[SK-MEL-2 (line)]] | alt | 15.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -13.7) |
| [[BT-474 (line)]] | alt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -8.8) |
| [[C-33 A (line)]] | alt | 14.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0514× (z -12.8) |
| [[CFPAC-1 (line)]] | alt | 11.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 15.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 16.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.174× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~1% of this change |
| [[LS 180 (line)]] | wt | 25.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.167× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[Panc 03.27 (line)]] | alt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -10.1) |
| [[SNU-1 (line)]] | wt | 19.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.126× (z -9.1) |
| [[SW 1088 (line)]] | alt | 39.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0662× (z -10.6) |
| [[AN3 CA (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10880), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARFGAP1]] | +0.82 | +0.80 / +0.79 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SSR2]] | +0.79 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[HM13]] | +0.78 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.78 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[MGAT1]] | +0.77 | +0.75 / +0.78 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[ATG101]] | +0.75 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[DHDDS]] | +0.75 | +0.76 / +0.69 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SYVN1]] | +0.75 | +0.73 / +0.73 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 486 |
| [[NAT9]] | +0.75 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[TMED9]] | +0.74 | +0.74 / +0.72 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 546 |
| [[GOSR2]] | +0.74 | +0.71 / +0.77 | both halves | 7e-06 | same gene group; pathway: Asparagine N-linked glycosylation; STRING 997 |
| [[PGM3]] | +0.74 | +0.69 / +0.76 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATF7IP]] | -0.67 | -0.68 / -0.57 | both halves | 8e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R9A]] | B | PPP1R9A activity lowers BET1L's level | lines that do not express PPP1R9A (16) vs lines expressing it (34) | 1.60× higher at baseline in the lines without PPP1R9A | 0.020 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| [[KCNK6]] | B | KCNK6 activity raises BET1L's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 1.64× lower at baseline in the lines without KCNK6 | 0.077 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | BET1L's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | BET1L's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.60 | 0.470 over the table, 0.074 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.775). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (10.7, -32.4); signed map (-49.1, 8.3). **Vector** length 104, 27.2% of its response variance represented; |z| ≥ 3 in 1,118 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.0 | +2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +1.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.0 | -0.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.9 | +1.0 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +1.8 | +1.3 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -6.7 | -11.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -19.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -6.1 | -7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -24.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -5.0 | -7.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.1 | -5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -6.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.3 | -2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | Bet1 golgi vesicular membrane trafficking protein like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:167,784-207,399 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GS15, GOLIM3 |
| Gene groups (HGNC) | SNAREs |
| Reactome | 8 pathways, smallest: Intra-Golgi traffic; COPI-mediated anterograde transport; ER to Golgi Anterograde Transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYM9](https://www.uniprot.org/uniprotkb/Q9NYM9) (BET1-like protein):

> Vesicle SNARE required for targeting and fusion of retrograde transport vesicles with the Golgi complex. Required for the integrity of the Golgi complex (By similarity).

**Summary**, from NCBI Gene [51272](https://www.ncbi.nlm.nih.gov/gene/51272):

> Enables SNAP receptor activity. Involved in regulation of retrograde vesicle-mediated transport, Golgi to ER and retrograde transport, endosome to Golgi. Located in Golgi apparatus and endosome. Implicated in uterine fibroid. Biomarker of endometrial adenocarcinoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19348](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19348) · Entrez [51272](https://www.ncbi.nlm.nih.gov/gene/51272) · UniProt [Q9NYM9](https://www.uniprot.org/uniprotkb/Q9NYM9) · Ensembl [ENSG00000177951](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177951)

## Data

Gene col 10880: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10880); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10880, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10880]; `tensor/DDL_lfc|DDL_z.npy` [10880]; `embed/gene_vectors.npy` [10880]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10880 or target_col == 10880). Every well: [[BET1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BET1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
