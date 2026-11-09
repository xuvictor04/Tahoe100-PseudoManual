---
symbol: "CUL7"
type: "gene"
col: 497
ensembl_id: "ENSG00000044090"
name: "cullin 7"
location: "6p21.1"
module: 49
arm: "+"
pooled_cpm: 34.11
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 41
n_dd_up_clean: 0
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# CUL7

*cullin 7* — 6p21.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (14 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.268× (z -20.8, q 0e+00, down in 47 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.299× (z -19.1, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGSM3]] (+0.70, fdr 7e-06), [[PMM2]] (+0.69, fdr 7e-06), [[RINT1]] (+0.69, fdr 7e-06); moves opposite to [[ROCK2]] (-0.60, fdr 7e-06), [[PTBP3]] (-0.55, fdr 5e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 497.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.1 | 2e-04 | 2/48 (HOP62, SW 1271) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 497.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.268×** | -20.8 | 0e+00 | 47/47 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.299×** | -19.1 | 0e+00 | 47/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.302×** | -18.9 | 0e+00 | 48/48 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.431×** | -18.1 | 0e+00 | 45/47 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.335×** | -17.3 | 0e+00 | 47/48 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.328×** | -17.0 | 0e+00 | 46/48 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.354×** | -16.4 | 0e+00 | 46/48 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.384×** | -15.1 | 0e+00 | 45/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.388×** | -15.0 | 0e+00 | 44/48 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.398×** | -14.0 | 9e-43 | 44/47 (H4, SNU-1, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.467×** | -12.0 | 2e-31 | 47/48 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.486×** | -11.4 | 2e-28 | 44/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.593×** | -11.3 | 7e-28 | 39/48 (HOP62, SNU-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.523×** | -10.3 | 5e-23 | 34/47 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.540×** | -9.7 | 8e-21 | 40/48 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.554×** | -9.3 | 3e-19 | 38/48 (MIA PaCa-2, C-33 A, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.713×** | -7.4 | 4e-12 | 37/48 (hTERT-HPNE, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 497. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 81.6 | 0 | 17 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0506× (z -20.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0793× (z -18.3) |
| [[HOP62 (line)]] | alt | 73.3 | 0 | 17 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0736× (z -27.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0982× (z -24.0) |
| [[NCI-H1792 (line)]] | alt | 57.6 | 0 | 15 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0778× (z -18.0) |
| [[hTERT-HPNE (line)]] | wt | 50.9 | 0 | 10 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.180× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 19.7 | 0 | 10 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.178× (z -12.8) |
| [[PANC-1 (line)]] | alt | 50.1 | 0 | 10 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -16.3) |
| [[RPMI-7951 (line)]] | alt | 55.2 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -13.9) |
| [[HS-578T (line)]] | alt | 36.8 | 0 | 7 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.225× (z -11.1) |
| [[KATO III (line)]] | alt | 29.4 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.146× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.176× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 34.0 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.212× (z -12.2) |
| [[NCI-H2347 (line)]] | alt | 27.0 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -18.5) |
| [[SW 900 (line)]] | alt | 27.5 | 0 | 7 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0870× (z -16.1) |
| [[SW480 (line)]] | alt | 18.7 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.215× (z -12.7) |
| [[A549 (line)]] | wt | 28.8 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -11.9) |
| [[J82 (line)]] | alt | 19.3 | 0 | 6 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.158× (z -11.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.303× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 39.1 | 0 | 6 | — | [[Harringtonine (drug)]] 5 µM 0.240× (z -11.1) |
| [[SNU-423 (line)]] | alt | 47.7 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -16.7) |
| [[LOX-IMVI (line)]] | wt | 44.0 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.259× (z -10.7) |
| [[A-172 (line)]] | wt | 37.5 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.250× (z -11.3) |
| [[BT-474 (line)]] | alt | 19.8 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.235× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 39.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -14.1) |
| [[CHP-212 (line)]] | wt | 31.6 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0575× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.143× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 45.3 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.153× (z -11.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.181× (z -10.5) |
| [[HT-29 (line)]] | alt | 28.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.164× (z -12.1) |
| [[LS 180 (line)]] | wt | 21.2 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.222× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.253× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 61.4 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.203× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.316× (z -14.0) |
| [[SNU-1 (line)]] | wt | 38.4 | 0 | 4 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0966× (z -13.2) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.127× (z -11.7) |
| [[A498 (line)]] | wt | 23.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -13.0) |
| [[HCT15 (line)]] | alt | 43.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.195× (z -9.5) |
| [[Hs 766T (line)]] | wt | 26.4 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.202× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 47.2 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.186× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 30.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -11.8) |
| [[SW1417 (line)]] | alt | 21.3 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.238× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 13.3 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0867× (z -12.8) |
| [[C-33 A (line)]] | alt | 37.4 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.209× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 21.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.228× (z -10.5) |
| [[RKO (line)]] | wt | 30.4 | 0 | 2 | — | [[venetoclax (drug)]] 5 µM 0.0618× (z -9.0) |
| [[SHP-77 (line)]] | alt | 16.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -10.1) |
| [[SW48 (line)]] | wt | 37.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[A-427 (line)]] | wt | 47.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[AN3 CA (line)]] | alt | 34.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -10.6) |
| [[C32 (line)]] | wt | 28.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -9.1) |
| [[COLO 205 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0710× (z -11.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[NCI-H2122 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 497), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGSM3]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[PMM2]] | +0.69 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[RINT1]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[BET1L]] | +0.69 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[AKAP17A]] | +0.68 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[DHDDS]] | +0.67 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[GMPPA]] | +0.67 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[SSR2]] | +0.67 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[DIS3]] | +0.66 | +0.70 / +0.54 | both halves | 1e-05 | pathway: Unfolded Protein Response (UPR) |
| [[NANS]] | +0.66 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[DRG1]] | +0.66 | +0.57 / +0.61 | both halves | 9e-06 | STRING 483 |
| [[DNAJC25]] | +0.65 | +0.68 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ROCK2]] | -0.60 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[PTBP3]] | -0.55 | -0.40 / -0.48 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CUL7's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.674). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.5, -33.1); signed map (-48.7, 8.7). **Vector** length 92.2, 27.6% of its response variance represented; |z| ≥ 3 in 1,429 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.8 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | +3.4 | -5.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.1 | -3.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.4 | +5.1 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.4 | +2.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.2 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.0 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | -2.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.2 | -20.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.1 | -15.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.5 | -15.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.4 | -14.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.5 | -17.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.4 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -6.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.9 | -3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | cullin 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:43,037,617-43,053,943 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ20C7.5; previously KIAA0076 |
| Gene groups (HGNC) | Cullins; 3M complex subunits |
| Reactome | 9 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; Unfolded Protein Response (UPR) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14999](https://www.uniprot.org/uniprotkb/Q14999) (Cullin-7):

> Core component of the 3M and Cul7-RING(FBXW8) complexes, which mediate the ubiquitination and subsequent proteasomal degradation of target proteins. Core component of the 3M complex, a complex required to regulate microtubule dynamics and genome integrity. It is unclear how the 3M complex regulates microtubules, it could act by controlling the level of a microtubule stabilizer. The Cul7-RING(FBXW8) complex alone lacks ubiquitination activity and does not promote polyubiquitination and …

**Summary**, from NCBI Gene [9820](https://www.ncbi.nlm.nih.gov/gene/9820):

> The protein encoded by this gene is a component of an E3 ubiquitin-protein ligase complex. The encoded protein interacts with TP53, CUL9, and FBXW8 proteins. Defects in this gene are a cause of 3M syndrome type 1 (3M1). Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2009]

**Accessions** — [HGNC:21024](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21024) · Entrez [9820](https://www.ncbi.nlm.nih.gov/gene/9820) · UniProt [Q14999](https://www.uniprot.org/uniprotkb/Q14999) · Ensembl [ENSG00000044090](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000044090)

## Data

Gene col 497: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 497); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 497, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 497]; `tensor/DDL_lfc|DDL_z.npy` [497]; `embed/gene_vectors.npy` [497]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 497 or target_col == 497). Every well: [[CUL7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CUL7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
