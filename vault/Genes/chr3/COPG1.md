---
symbol: "COPG1"
type: "gene"
col: 11212
ensembl_id: "ENSG00000181789"
name: "coat protein complex I subunit gamma 1"
location: "3q21.3"
module: 42
arm: "+"
pooled_cpm: 98.76
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 33
n_dd_up_clean: 0
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# COPG1

*coat protein complex I subunit gamma 1* — 3q21.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.511× (z -16.0, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC61A1]] (+0.82, fdr 7e-06), [[TMEM214]] (+0.77, fdr 7e-06), [[TMEM39A]] (+0.77, fdr 7e-06); moves opposite to [[KAT6A]] (-0.59, fdr 2e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11212.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.97 | 17/48 (LoVo, SHP-77, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11212.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.511×** | -16.0 | 0e+00 | 45/48 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.427×** | -14.4 | 2e-44 | 46/48 (AsPC-1, H4, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.435×** | -14.1 | 1e-42 | 45/48 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.472×** | -12.7 | 1e-34 | 43/48 (AsPC-1, H4, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.632×** | -11.0 | 6e-26 | 40/49 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.536×** | -10.1 | 4e-22 | 44/48 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.570×** | -9.5 | 2e-19 | 40/48 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.593×** | -8.8 | 9e-17 | 35/48 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.599×** | -8.6 | 4e-16 | 44/48 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.618×** | -8.1 | 3e-14 | 38/48 (H4, HS-578T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.611×** | -8.0 | 7e-14 | 38/47 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.623×** | -7.7 | 7e-13 | 38/48 (H4, HOP62, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.656×** | -7.1 | 5e-11 | 38/48 (H4, HOP62, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.752×** | -6.8 | 4e-10 | 35/48 (HOP62, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.694×** | -6.2 | 3e-08 | 35/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.707×** | -5.8 | 2e-07 | 31/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.729×** | -5.1 | 9e-06 | 34/48 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.814×** | -4.9 | 3e-05 | 25/48 (A-172, H4, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.753×** | -4.8 | 5e-05 | 31/48 (CFPAC-1, HOP62, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.789×** | -4.0 | 0.002 | 26/48 (HS-578T, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.657×** | -3.7 | 0.005 | 27/49 (H4, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.802×** | -3.5 | 0.010 | 20/48 (HT-29, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11212. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 150 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -11.6) |
| [[H4 (line)]] | wt | 178 | 0 | 11 (9 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -16.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -10.7) |
| [[HOP62 (line)]] | alt | 121 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -13.8) |
| [[HS-578T (line)]] | alt | 158 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -19.3) |
| [[NCI-H1792 (line)]] | alt | 88.6 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.215× (z -14.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.419× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 141 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -23.8) |
| [[NCI-H460 (line)]] | wt | 61.5 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.357× (z -10.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 142 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -20.2) |
| [[AsPC-1 (line)]] | alt | 71.7 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -19.7) |
| [[hTERT-HPNE (line)]] | wt | 119 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -14.6) |
| [[A498 (line)]] | wt | 104 | 0 | 5 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.376× (z -11.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.523× (z -10.9) |
| [[LoVo (line)]] | wt | 98.5 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.303× (z -12.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 102 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.291× (z -13.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -9.2) |
| [[SNU-423 (line)]] | alt | 89.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -16.1) |
| [[CFPAC-1 (line)]] | alt | 104 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -18.3) |
| [[Hs 766T (line)]] | wt | 92.5 | 0 | 4 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.315× (z -11.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -9.0) |
| [[HT-29 (line)]] | alt | 116 | 0 | 4 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.320× (z -11.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.487× (z -10.4) |
| [[SW1417 (line)]] | alt | 108 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.396× (z -10.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.528× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 121 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -10.8) |
| [[PANC-1 (line)]] | alt | 92.1 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -11.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 59.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -13.4) |
| [[A549 (line)]] | wt | 60.3 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.400× (z -8.6) |
| [[J82 (line)]] | alt | 103 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -19.1) |
| [[KATO III (line)]] | alt | 186 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.400× (z -9.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 75.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -13.2) |
| [[SK-MEL-2 (line)]] | alt | 102 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -24.1) |
| [[SNU-1 (line)]] | wt | 95.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -19.4) |
| [[SW480 (line)]] | alt | 96.3 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.431× (z -9.4) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-427 (line)]] | wt | 80.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -16.9) |
| [[BT-474 (line)]] | alt | 86.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.394× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[C32 (line)]] | wt | 69.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.308× (z -9.7) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.316× (z -8.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[MIA PaCa-2 (line)]] | alt | 98.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -17.0) |
| [[SHP-77 (line)]] | alt | 64.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -8.7) |
| [[AN3 CA (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 93.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 99.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 75.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 96.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11212), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC61A1]] | +0.82 | +0.83 / +0.83 | both halves | 7e-06 | STRING 528 |
| [[TMEM214]] | +0.77 | +0.82 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[TMEM39A]] | +0.77 | +0.82 / +0.74 | both halves | 7e-06 |  |
| [[SEC23A]] | +0.76 | +0.79 / +0.78 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 546 |
| [[COPA]] | +0.75 | +0.80 / +0.78 | both halves | 7e-06 | same gene group; pathway: Asparagine N-linked glycosylation; STRING 998 |
| [[GMPPA]] | +0.75 | +0.82 / +0.67 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SEC13]] | +0.75 | +0.83 / +0.70 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 669 |
| [[HDLBP]] | +0.74 | +0.76 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[STT3A]] | +0.74 | +0.76 / +0.73 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 519 |
| [[COG3]] | +0.74 | +0.80 / +0.68 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[OSTC]] | +0.73 | +0.78 / +0.69 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[COPB1]] | +0.73 | +0.84 / +0.63 | both halves | 7e-06 | same gene group; pathway: Asparagine N-linked glycosylation; STRING 999 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KAT6A]] | -0.59 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises COPG1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.791). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.6, -31.5); signed map (-54.5, 9.8). **Vector** length 111, 37.6% of its response variance represented; |z| ≥ 3 in 1,202 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.58 to 11); *Maturation of DENV proteins* (reactome, mean cos +0.56 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.58 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.1 | +0.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.2 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.9 | -2.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +1.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.5 | +2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.0 | +2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.0 | +0.7 |
|  | [[EX229 (drug)]] 0.05 µM |  | +2.7 | +2.3 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -5.4 | -8.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -4.5 | -4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -4.5 | -3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -5.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.7 | -3.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.6 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -6.2 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -3.3 | -3.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -3.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | coat protein complex I subunit gamma 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:129,249,606-129,277,773 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously COPG |
| Gene groups (HGNC) | Clathrin/coatomer adaptor, adaptin-like, N-terminal domain containing; MicroRNA protein coding host genes; Coat protein complex I |
| Reactome | 9 pathways, smallest: COPI-dependent Golgi-to-ER retrograde traffic; COPI-mediated anterograde transport; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y678](https://www.uniprot.org/uniprotkb/Q9Y678) (Coatomer subunit gamma-1):

> The coatomer is a cytosolic protein complex that binds to dilysine motifs and reversibly associates with Golgi non-clathrin-coated vesicles, which further mediate biosynthetic protein transport from the ER, via the Golgi up to the trans Golgi network. Coatomer complex is required for budding from Golgi membranes, and is essential for the retrograde Golgi-to-ER transport of dilysine-tagged proteins. In mammals, the coatomer can only be recruited by membranes associated to ADP-ribosylation …

**Summary**, from NCBI Gene [22820](https://www.ncbi.nlm.nih.gov/gene/22820):

> Predicted to enable structural molecule activity. Predicted to be involved in several processes, including Golgi vesicle transport; establishment of Golgi localization; and organelle transport along microtubule. Located in Golgi apparatus. Implicated in immunodeficiency 128. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:2236](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2236) · Entrez [22820](https://www.ncbi.nlm.nih.gov/gene/22820) · UniProt [Q9Y678](https://www.uniprot.org/uniprotkb/Q9Y678) · Ensembl [ENSG00000181789](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181789)

## Data

Gene col 11212: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11212); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11212, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11212]; `tensor/DDL_lfc|DDL_z.npy` [11212]; `embed/gene_vectors.npy` [11212]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11212 or target_col == 11212). Every well: [[COPG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COPG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
