---
symbol: "COG6"
type: "gene"
col: 5413
ensembl_id: "ENSG00000133103"
name: "component of oligomeric golgi complex 6"
location: "13q14.11"
module: 56
arm: "+"
pooled_cpm: 158.5
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 48
n_dd_up_clean: 0
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# COG6

*component of oligomeric golgi complex 6* — 13q14.11

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 48 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.296× (z -23.9, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM263]] (+0.88, fdr 7e-06), [[PRRC1]] (+0.86, fdr 7e-06), [[SEC23A]] (+0.86, fdr 7e-06); moves opposite to [[PRRC2B]] (-0.66, fdr 1e-05), [[SLC25A13]] (-0.65, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SNHG18]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Anethole trithione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 18 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 48 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5413.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.296×** | -23.9 | 0e+00 | 45/48 (AsPC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.269×** | -19.0 | 0e+00 | 47/48 (AsPC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.327×** | -16.8 | 0e+00 | 42/48 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.370×** | -14.9 | 0e+00 | 42/49 (A498, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.412×** | -13.3 | 2e-38 | 47/48 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.399×** | -13.3 | 3e-38 | 41/44 (Panc 03.27, A498, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.509×** | -13.3 | 3e-38 | 42/49 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.421×** | -13.0 | 8e-37 | 43/48 (HOP62, AsPC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.426×** | -12.8 | 9e-36 | 44/48 (HOP62, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.470×** | -10.5 | 5e-24 | 42/45 (RPMI-7951, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.548×** | -9.0 | 9e-18 | 43/48 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.557×** | -8.8 | 7e-17 | 41/48 (HOP62, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.563×** | -8.6 | 3e-16 | 38/48 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.593×** | -7.5 | 2e-12 | 40/48 (J82, LoVo, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.604×** | -7.3 | 1e-11 | 37/50 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.695×** | -7.3 | 1e-11 | 42/48 (HOP62, HS-578T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.636×** | -6.8 | 4e-10 | 38/48 (CFPAC-1, HOP62, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.679×** | -5.8 | 2e-07 | 32/48 (CFPAC-1, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.695×** | -5.0 | 1e-05 | 37/47 (A549, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.718×** | -5.0 | 2e-05 | 33/48 (LoVo, H4, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.539×** | -4.9 | 3e-05 | 38/49 (HS-578T, A498, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.550×** | -4.7 | 6e-05 | 28/48 (RPMI-7951, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5413. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 164 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -28.8) |
| [[SW 900 (line)]] | alt | 212 | 0 | 17 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -22.9) |
| [[HS-578T (line)]] | alt | 181 | 0 | 16 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -28.0) |
| [[RPMI-7951 (line)]] | alt | 209 | 0 | 16 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -27.7) |
| [[H4 (line)]] | wt | 238 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -21.8) |
| [[hTERT-HPNE (line)]] | wt | 271 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -20.6) |
| [[A-172 (line)]] | wt | 109 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -23.7) |
| [[CFPAC-1 (line)]] | alt | 138 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -27.2) |
| [[AsPC-1 (line)]] | alt | 179 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0881× (z -34.8) |
| [[NCI-H1573 (line)]] | alt | 132 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 114 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -20.5) |
| [[NCI-H2347 (line)]] | alt | 142 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -20.5) |
| [[Hs 766T (line)]] | wt | 314 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -19.0) |
| [[J82 (line)]] | alt | 203 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -29.1) |
| [[Panc 03.27 (line)]] | alt | 193 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.315× (z -17.1) |
| [[A498 (line)]] | wt | 341 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -27.6) |
| [[A549 (line)]] | wt | 116 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -15.9) |
| [[KATO III (line)]] | alt | 236 | 0 | 9 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.322× (z -13.9) |
| [[LoVo (line)]] | wt | 202 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.324× (z -11.6) |
| [[SW1417 (line)]] | alt | 127 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -20.6) |
| [[SW480 (line)]] | alt | 170 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.477× (z -9.2) |
| [[C32 (line)]] | wt | 125 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -17.6) |
| [[HepG2_C3A (line)]] | wt | 81.2 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -12.6) |
| [[HT-29 (line)]] | alt | 179 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -16.6) |
| [[LOX-IMVI (line)]] | wt | 107 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -20.4) |
| [[NCI-H2030 (line)]] | alt | 89.9 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -21.1) |
| [[COLO 205 (line)]] | alt | 421 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -14.9) |
| [[HCT15 (line)]] | alt | 318 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.179× (z -12.2) |
| [[SNU-423 (line)]] | alt | 108 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -23.8) |
| [[SW 1088 (line)]] | alt | 323 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -14.9) |
| [[HEC-1-A (line)]] | alt | 190 | 0 | 4 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.124× (z -11.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.459× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 85.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 96.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -25.2) |
| [[PANC-1 (line)]] | alt | 76.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -14.0) |
| [[RKO (line)]] | wt | 139 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -11.8) |
| [[SNU-1 (line)]] | wt | 210 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.405× (z -9.2) |
| [[AN3 CA (line)]] | alt | 128 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.118× (z -15.2) |
| [[A-427 (line)]] | wt | 73.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.250× (z -14.2) |
| [[BT-474 (line)]] | alt | 72.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.315× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CHP-212 (line)]] | wt | 151 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[LS 180 (line)]] | wt | 159 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.306× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 67.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -12.2) |
| [[SW48 (line)]] | wt | 178 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[C-33 A (line)]] | alt | 98.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 197 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5413), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM263]] | +0.88 | +0.90 / +0.85 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.86 | +0.87 / +0.80 | both halves | 7e-06 |  |
| [[SEC23A]] | +0.86 | +0.86 / +0.75 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[TMEM39A]] | +0.84 | +0.89 / +0.78 | both halves | 7e-06 |  |
| [[TTC3]] | +0.84 | +0.87 / +0.78 | both halves | 7e-06 |  |
| [[COPB1]] | +0.84 | +0.86 / +0.79 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 404 |
| [[SEC24D]] | +0.84 | +0.86 / +0.78 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[ERLEC1]] | +0.83 | +0.85 / +0.75 | both halves | 7e-06 | STRING 500 |
| [[PDXDC1]] | +0.83 | +0.87 / +0.75 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.82 | +0.87 / +0.73 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.82 | +0.86 / +0.74 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[PDXDC2P]] | +0.82 | +0.85 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRRC2B]] | -0.66 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[SLC25A13]] | -0.65 | -0.67 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNHG18]] | B | SNHG18 activity raises COG6's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.42× lower at baseline in the lines without SNHG18 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | COG6's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | COG6's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64 | 0.390 over the table, 0.056 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Belzutifan (drug)]] 5 µM | C | COG6's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | COG6's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.59 | 0.475 over the table, 0.080 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.933). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.6, -33.4); signed map (-50.9, 10.3). **Vector** length 137, 59.4% of its response variance represented; |z| ≥ 3 in 1,605 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *protein secretion* (hallmark, mean cos +0.71 to 10); *COPI-dependent Golgi-to-ER retrograde traffic* (reactome, mean cos +0.74 to 9); *COPII-mediated vesicle transport* (reactome, mean cos +0.75 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | +5.3 | -3.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | +5.1 | -4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +4.6 | -4.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.8 | +2.2 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +3.5 | +1.7 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +3.2 | +1.4 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.8 | +0.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.8 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.7 | -9.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.2 | -13.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -7.1 | -7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.0 | -7.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.5 | -8.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -5.0 | -3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.9 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | component of oligomeric golgi complex 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.11 — chr13:39,655,627-39,791,665 (+) |
| Ensembl biotype | protein_coding |
| Also known as | COD2, KIAA1134 |
| Gene groups (HGNC) | Components of oligomeric golgi complex |
| Reactome | 9 pathways, smallest: Intra-Golgi traffic; Retrograde transport at the Trans-Golgi-Network; COPI-mediated anterograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2V7](https://www.uniprot.org/uniprotkb/Q9Y2V7) (Conserved oligomeric Golgi complex subunit 6):

> Required for normal Golgi function.

**Summary**, from NCBI Gene [57511](https://www.ncbi.nlm.nih.gov/gene/57511):

> This gene encodes a subunit of the conserved oligomeric Golgi complex that is required for maintaining normal structure and activity of the Golgi apparatus. The encoded protein is organized with conserved oligomeric Golgi complex components 5, 7 and 8 into a sub-complex referred to as lobe B. Alternative splicing results in multiple transcript variants.[provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:18621](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18621) · Entrez [57511](https://www.ncbi.nlm.nih.gov/gene/57511) · UniProt [Q9Y2V7](https://www.uniprot.org/uniprotkb/Q9Y2V7) · Ensembl [ENSG00000133103](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133103)

## Data

Gene col 5413: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5413); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5413, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5413]; `tensor/DDL_lfc|DDL_z.npy` [5413]; `embed/gene_vectors.npy` [5413]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5413 or target_col == 5413). Every well: [[COG6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COG6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
