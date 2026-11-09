---
symbol: "COG3"
type: "gene"
col: 5822
ensembl_id: "ENSG00000136152"
name: "component of oligomeric golgi complex 3"
location: "13q14.13"
module: 49
arm: "+"
pooled_cpm: 68.09
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# COG3

*component of oligomeric golgi complex 3* — 13q14.13

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 2.80×; ⚠ cell-cycle shift, explains ~80% of this change).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.355× (z -16.0, q 0e+00, down in 34 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.608× (z -9.5, q 3e-19, down in 43 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC30A5]] (+0.82, fdr 7e-06), [[SEC23IP]] (+0.80, fdr 7e-06), [[KDELR2]] (+0.80, fdr 7e-06).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SNHG18]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Anethole trithione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5822.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 2.80×; ⚠ cell-cycle shift, explains ~80% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.22× | +3.2 | 0.57 | 18/47 (SW480, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5822.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.355×** | -16.0 | 0e+00 | 34/39 (hTERT-HPNE, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.459×** | -12.5 | 3e-33 | 43/49 (COLO 205, A498, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.608×** | -9.5 | 3e-19 | 43/49 (A549, SNU-1, …) | rises with dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.633×** | -6.8 | 2e-09 | 33/43 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.666×** | -6.3 | 4e-08 | 40/48 (RKO, hTERT-HPNE, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.715×** | -5.4 | 7e-06 | 31/48 (A498, NCI-H1573, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.723×** | -5.0 | 5e-05 | 27/50 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.734×** | -5.0 | 5e-05 | 28/48 (SW 900, A498, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.737×** | -4.9 | 6e-05 | 26/48 (SW 900, H4, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.756×** | -4.3 | 1e-03 | 27/48 (LoVo, NCI-H2030, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **0.750×** | -4.2 | 0.001 | 26/48 (H4, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.759×** | -4.1 | 0.002 | 28/48 (KATO III, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.783×** | -3.9 | 0.004 | 26/48 (SW 900, A549, …) | all doses, flat |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.775×** | -3.8 | 0.007 | 23/48 (A498, KATO III, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.808×** | -3.4 | 0.025 | 22/48 (NCI-H1573, H4, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.843× | -3.3 | 0.029 | 22/48 (HOP62, J82, …) | top dose only | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 0.05 µM |  | **0.805×** | -3.3 | 0.034 | 20/48 (A498, COLO 205, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.684×** | -3.2 | 0.043 | 18/48 (HS-578T, A498, …) | top dose only | noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.811×** | -3.1 | 0.055 | 19/49 (H4, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5822. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 124 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -9.9) |
| [[HOP62 (line)]] | alt | 60.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.358× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -9.0) |
| [[Hs 766T (line)]] | wt | 159 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -10.2) |
| [[J82 (line)]] | alt | 67.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -8.5) |
| [[A-172 (line)]] | wt | 58.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -9.3) |
| [[H4 (line)]] | wt | 93.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -13.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 66.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -8.6) |
| [[HT-29 (line)]] | alt | 95.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[hTERT-HPNE (line)]] | wt | 92.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0768× (z -20.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 84.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -10.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 60.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 94.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.381× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 102 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0599× (z -16.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 58.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[KATO III (line)]] | alt | 97.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -15.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 80.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[LS 180 (line)]] | wt | 91.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 58.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -19.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 60.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.347× (z -9.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 57.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.80× (z +8.6) ⚠ cell-cycle shift, explains ~80% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -11.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-1 (line)]] | wt | 50.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -11.2) |
| [[SW 900 (line)]] | alt | 92.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -16.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 85.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -16.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 66.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -10.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 48.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -8.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 36.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.336× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~50% of this change |
| [[COLO 205 (line)]] | alt | 208 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0392× (z -28.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H2030 (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.322× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 54.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H2347 (line)]] | alt | 50.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.329× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[PANC-1 (line)]] | alt | 50.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.351× (z -9.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 33.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -11.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SNU-423 (line)]] | alt | 46.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -15.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 66.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 54.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 99.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 70.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5822), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC30A5]] | +0.82 | +0.77 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[SEC23IP]] | +0.80 | +0.73 / +0.78 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[KDELR2]] | +0.80 | +0.80 / +0.76 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SSR2]] | +0.78 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[SEC13]] | +0.78 | +0.76 / +0.74 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 552 |
| [[MCEE]] | +0.77 | +0.74 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[OSTC]] | +0.77 | +0.80 / +0.74 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[ACBD3]] | +0.76 | +0.81 / +0.63 | both halves | 7e-06 |  |
| [[SLC33A1]] | +0.76 | +0.69 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[TMEM39A]] | +0.76 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[OSBP]] | +0.75 | +0.83 / +0.62 | both halves | 7e-06 |  |
| [[COG6]] | +0.75 | +0.77 / +0.70 | both halves | 7e-06 | same gene group; pathway: Asparagine N-linked glycosylation; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNHG18]] | B | SNHG18 activity raises COG3's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.37× lower at baseline in the lines without SNHG18 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | COG3's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | COG3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.71 | 0.260 over the table, 0.012 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.890). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.5, -34.8); signed map (-52.6, 11.3). **Vector** length 102, 29.3% of its response variance represented; |z| ≥ 3 in 869 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *XBP1(S) activates chaperone genes* (reactome, mean cos +0.60 to 8); *IRE1alpha activates chaperones* (reactome, mean cos +0.60 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.60 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.6 | -0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.6 | -0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.6 | +2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.5 | +1.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.5 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -9.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -0.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.0 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -3.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.4 | -2.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.3 | -4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | component of oligomeric golgi complex 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.13 — chr13:45,464,898-45,536,701 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SEC34 |
| Gene groups (HGNC) | Components of oligomeric golgi complex |
| Reactome | 9 pathways, smallest: Intra-Golgi traffic; Retrograde transport at the Trans-Golgi-Network; COPI-mediated anterograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JB2](https://www.uniprot.org/uniprotkb/Q96JB2) (Conserved oligomeric Golgi complex subunit 3):

> Involved in ER-Golgi transport. Also involved in retrograde (Golgi to ER) transport.

**Summary**, from NCBI Gene [83548](https://www.ncbi.nlm.nih.gov/gene/83548):

> This gene encodes a component of the conserved oligomeric Golgi (COG) complex which is composed of eight different subunits and is required for normal Golgi morphology and localization. Defects in the COG complex result in multiple deficiencies in protein glycosylation. The protein encoded by this gene is involved in ER-Golgi transport.[provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:18619](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18619) · Entrez [83548](https://www.ncbi.nlm.nih.gov/gene/83548) · UniProt [Q96JB2](https://www.uniprot.org/uniprotkb/Q96JB2) · Ensembl [ENSG00000136152](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136152)

## Data

Gene col 5822: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5822); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5822, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5822]; `tensor/DDL_lfc|DDL_z.npy` [5822]; `embed/gene_vectors.npy` [5822]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5822 or target_col == 5822). Every well: [[COG3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COG3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
